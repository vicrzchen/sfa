from scrapy_db.models import Bacs, BacsItem, BacsApprovalProcess
from scrapy_db.dbkits import DBOperationBase, DBKits


class BacsDBOperation(DBOperationBase):
    def __init__(self, db_engine: DBKits=None):
        super(DBOperationBase, self).__init__(db_engine,
                                              table_type_name='bacs',
                                              data_struct_name='_Bacs')
        self.record_type = Bacs
        pass

    def get_duplicate_condition(self, compare_obj=None):
        if compare_obj is not None:
            return {Bacs.BACS_code == compare_obj.BACS_code}
        return None


class BacsItemDBOperation(DBOperationBase):
    def __init__(self, db_engine: DBKits=None):
        super(BacsItemDBOperation, self).__init__(db_engine,
                                                  table_type_name='bacs_item',
                                                  data_struct_name='_BacsItem')
        self.record_type = BacsItem
        pass

    def get_duplicate_condition(self, compare_obj=None):
        if compare_obj is not None:
            return {BacsItem.bacs_item_sys_id == compare_obj.bacs_item_sys_id}
        return None


class BacsApprovalProcessDBOperation(DBOperationBase):
    def __init__(self, db_engine: DBKits=None):
        super(BacsApprovalProcessDBOperation, self).__init__(db_engine,
                                                             table_type_name='bacs_approval_process',
                                                             data_struct_name='_BacsApprovalProcess')
        self.record_type = Bacs
        pass

    def get_duplicate_condition(self, compare_obj=None):
        if compare_obj is not None:
            return {BacsApprovalProcess.BACS_approval_process_id == compare_obj.BACS_approval_process_id}
        return None

