"""
第 0003 题： 将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。

"""
import uuid
import redis

def getcode(count):
    codelist = []
    for i in range(count):
        code = str(uuid.uuid4())
        codelist.append(code)
    return codelist

def save_code(codelist):
    r = redis.Redis(host='127.0.0.1', port='6379', password='')
    p = r.pipeline()
    for code in codelist:
        p.sadd('code', code)
    p.execute()
    return r.scard('code')

if __name__ == "__main__":
    save_code(getcode(200))
    print("OK")