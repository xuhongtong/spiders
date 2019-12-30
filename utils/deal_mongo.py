import pymongo
from setting import mongo_info


class DealMongo:
    def __init__(self):
        self.client = pymongo.MongoClient(host=mongo_info['host'], username=mongo_info['username'],
                                          password=mongo_info['password'], authSource=mongo_info['authSource'])
        self.db = self.client[mongo_info['mongodb_name']]

    # 批量存数据
    def mongo_insert_many(self, record_list, table_name):
        collection = self.db[table_name]
        collection.insert_many(record_list, ordered=False)

    # 单条存数据
    def mongo_insert_one(self, record_dic, table_name):
        collection = self.db[table_name]
        collection.insert_one(record_dic)

    # 给指定字段添加索引
    def mongo_index(self, pattern, table_name):
        collection = self.db[table_name]
        value = collection.create_index({f"{pattern}": 1})
        return value

    # 更新指定记录
    def mongo_update_one(self, pattern_dic, record_dic, table_name):
        collection = self.db[table_name]
        collection.update_one(pattern_dic, {'$set': record_dic})

    # 插入去重
    def isexist(self, record_dic, table_name):
        collection = self.db[table_name]
        history_record = collection.find_one(record_dic, {'_id': 1})
        return history_record

    # 获取指定字段数据
    def mongo_query_pattern(self, pattern, table_name):
        collection = self.db[table_name]
        results = collection.find({}, {f"{pattern}": 1})
        result_list = [value.get(pattern) for value in results]
        return result_list

    def get_error_info(self, table_name):
        collection = self.db[table_name]
        values = collection.find({'status': 1})
        value_list = [value for value in values]
        return value_list

    def get_developer(self, table_name):
        collection = self.db[table_name]
        developer = collection.find({'developer': {'$ne': 'MIFUN'}}).distinct('developer')
        return developer

    # 补数据
    def get_record(self, accound_id, region, table_name):
        collection = self.db[table_name]
        values = collection.find({'accound_id': accound_id, 'region': region, 'disable': 0})
        value_list = [value for value in values]
        return value_list


if __name__ == '__main__':
    d = DealMongo()
    a = {'amazon-order-id': '', 'account_id': 'A37AKKCPBMVLA4', 'region': 'UK', 'report_id': '19114181009018241',
         'merchant-order-id': None, 'sku': None, 'asin': None, 'item-status': None}
    print(d.isexist(a, '_get_flat_file_all_orders_data_by_last_update_'))
