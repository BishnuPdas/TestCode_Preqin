from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func
from typing import Optional

from db.getdatabase import  get_db
from dao.models import Investor, Commitment

router = APIRouter()


@router.get("/investors/")
def read_investors(db: Session = Depends(get_db)):
    investors = db.query(Investor).options(joinedload(Investor.commitments)).all()
    results = []
    for inv in investors:
        total_commitment = sum(c.amount for c in inv.commitments) if inv.commitments else 0

        if total_commitment >= 1_000_000_000:
            total_str = f"{total_commitment/1_000_000_000:.1f}B"
        elif total_commitment >= 1_000_000:
            total_str = f"{total_commitment/1_000_000:.1f}M"
        else:
            total_str = str(total_commitment)

        results.append({
            "id": inv.id,
            "name": inv.name,
            "type": inv.type,
            "date_added": inv.date_added.strftime("%B %d, %Y") if inv.date_added else "",
            "country": inv.country,
            "total_commitment": total_str
        })
    return results


@router.get("/investors/{investor_id}")
def get_single_investor(investor_id: int, db: Session = Depends(get_db)):
    investor = db.query(Investor).options(joinedload(Investor.commitments))\
        .filter(Investor.id == investor_id).first()

    if not investor:
        raise HTTPException(status_code=404, detail="Investor not found")

    total_commitment = sum(c.amount for c in investor.commitments) if investor.commitments else 0
    if total_commitment >= 1_000_000_000:
        total_str = f"{total_commitment/1_000_000_000:.1f}B"
    elif total_commitment >= 1_000_000:
        total_str = f"{total_commitment/1_000_000:.1f}M"
    else:
        total_str = str(total_commitment)

    return {
        "id": investor.id,
        "name": investor.name,
        "type": investor.type,
        "date_added": investor.date_added.strftime("%B %d, %Y") if investor.date_added else "",
        "country": investor.country,
        "total_commitment": total_str
    }


@router.get("/commitments/")
def read_commitments(db: Session = Depends(get_db)):
    commitments = db.query(Commitment).all()
    results = []
    for c in commitments:
        amt = c.amount
        if amt >= 1_000_000_000:
            amt_str = f"{amt/1_000_000_000:.1f}B"
        elif amt >= 1_000_000:
            amt_str = f"{amt/1_000_000:.1f}M"
        else:
            amt_str = f"{amt:.1f}"
        results.append({
            "id": c.id,
            "asset_class": c.asset_class,
            "currency": c.currency,
            "amount": amt_str,
        })
    return results


@router.get("/commitments/summary")
def commitment_summary(db: Session = Depends(get_db)):
    data = db.query(
        Commitment.asset_class,
        func.sum(Commitment.amount)
    ).group_by(Commitment.asset_class).all()

    summaries = []
    total_all = 0
    for asset_class, total in data:
        total_all += total
        if total >= 1_000_000_000:
            total_str = f"£{total/1_000_000_000:.1f}B"
        elif total >= 1_000_000:
            total_str = f"£{total/1_000_000:.1f}M"
        else:
            total_str = f"£{total:.1f}"
        summaries.append({"asset_class": asset_class, "total": total_str})

    if total_all >= 1_000_000_000:
        all_str = f"£{total_all/1_000_000_000:.1f}B"
    elif total_all >= 1_000_000:
        all_str = f"£{total_all/1_000_000:.1f}M"
    else:
        all_str = f"£{total_all:.1f}"
    summaries.insert(0, {"asset_class": "All", "total": all_str})

    return summaries


@router.get("/investors/{investor_id}/commitments/")
def get_investor_commitments(
    investor_id: int,
    asset_class: Optional[str] = Query(None, description="Asset class filter"),
    db: Session = Depends(get_db)
):
    query = db.query(Commitment).filter(Commitment.investor_id == investor_id)
    if asset_class:
        query = query.filter(Commitment.asset_class == asset_class)
    commitments = query.all()

    results = []
    for c in commitments:
        amt = c.amount
        if amt >= 1_000_000_000:
            amt_str = f"{amt/1_000_000_000:.1f}B"
        elif amt >= 1_000_000:
            amt_str = f"{amt/1_000_000:.1f}M"
        else:
            amt_str = f"{amt:.1f}"

        results.append({
            "id": c.id,
            "asset_class": c.asset_class,
            "currency": c.currency,
            "amount": amt_str,
        })
    return results
