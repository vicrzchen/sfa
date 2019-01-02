# coding: utf-8
from sqlalchemy import Column, Float, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Bacs(Base):
    __tablename__ = 'bacs'

    BACS_sys_id = Column(INTEGER(64), primary_key=True, unique=True)
    BACS_code = Column(String(20))
    est_name = Column(String(200))
    case_num = Column(String(20))
    epricing_num = Column(String(20))
    status = Column(String(40))
    applicant = Column(String(40))
    team = Column(String(40))
    apply_date = Column(String(20))
    epricing_status = Column(String(40))
    offer_price = Column(Float)
    total_sr_price = Column(Float)
    discount_rate = Column(Float)
    last_update_date = Column(String(20))


class BacsApprovalProcess(Base):
    __tablename__ = 'bacs_approval_process'

    BACS_approval_process_id = Column(INTEGER(64), primary_key=True, unique=True)
    BACS_code = Column(String(20))
    approval_action = Column(String(20))
    aproval_remark = Column(String(500))
    action_by = Column(String(100))
    status = Column(String(20))


class BacsItem(Base):
    __tablename__ = 'bacs_item'

    bacs_item_sys_id = Column(INTEGER(64), primary_key=True, unique=True)
    bacs_code = Column(String(20))
    item_num = Column(String(40))
    item_name = Column(String(200))
    qty = Column(INTEGER(11))
    unit_price = Column(Float)
    total = Column(Float)
    rev_allocate = Column(Float)
