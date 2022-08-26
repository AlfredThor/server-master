from . import BaseCurd
from model.model import Auth


class AuthCurd(BaseCurd):
    def get_(self, data={'curd': {}}):
        """ 查询操作
            in: {
                    'time_range': '2000-09-10 00:26:46/2020-11-10 00:26:46',    # 搜索的起止时间
                    # 搜索的具体字段
                    'curd': {
                        'xxxx': '', ,,,
                    },
                    # 下面是分页
                    'page_size': 10,
                    'current': 1,
                    'query_type': '查询类型，or/and',
                    'query_fuzzy': '模糊查询',
                    'is_all': '单个/全部数据',
                    'reverse': '正反向取值',
                    'export': '取值列表',
                    'discard': '分页过滤个数',
                }
            out: {'code': '100200', 'msg': '👌', 'data':{'list':[{},{},,,],'pagination':{} } }
        """
        query_ = self.db.query(Auth)
        pass

    def add_(self, data={'curd': {}}):
        pass

    def update_(self, data={'curd': {}}):
        pass

    def delete_(self, data={'curd': {}}):
        pass
