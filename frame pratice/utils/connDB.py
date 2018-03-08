import psycopg2,os,sys
from utils.log import logger
from utils.config import Config

class PostgreDB:
    def __init__(self):
        '''
        初始化数据库连接参数
        db_name:数据库名称
        db_user:数据库用户
        db_password:数据库用户密码
        db_ip:数据库host ip
        db_port:数据库ip端口
        '''
        c = Config().get('DB')
        self.db_name = c.get('db_name') if c and c.get('db_name') else 'jmtool0705'
        self.db_user = c.get('db_user') if c and c.get('db_user') else 'postgres'
        self.db_password = c.get('db_password') if c and c.get('db_password') else 'postgres'
        self.db_ip = c.get('db_ip') if c and c.get('db_ip') else '121.196.200.254'
        self.db_port = c.get('db_port') if c and c.get('db_port') else '5432'

    def connectDB(self):
        try:
            # connect to DB 连接数据库
            self.db = psycopg2.connect(database=self.db_name,user=self.db_user,password=self.db_password,host=self.db_ip,port=self.db_port)
            # create cursor
            self.cursor = self.db.cursor()
            logger.info(self.db)
            print("Connect DB successfully!") #连接成功
        except ConnectionError as ex:
            print(ex)
            logger.error('数据库连接失败:%s' % str(ex))

    def executeSQL(self, sql, params):
        self.connectDB()
        # executing sql 执行sql语句
        try:
            self.cursor.execute(sql, params) #sql语句，与sql语句里的查询条件params分别定义
            # executing by committing to DB 提交到数据库
            logger.info(sql)
            self.db.commit()
            return self.cursor
        except Exception as e:
            self.db.rollback()  # 如果出错，则事务回滚
            logger.error('执行sql语句出错:%s' % e)
            return False

    def get_all(self):
        value = self.cursor.fetchall() #获取所有结果
        logger.info(value)
        return value

    def get_one(self,cursor):
        value = self.cursor.fetchone() #获取一条结果
        logger.info(value)
        return value

    def closeDB(self):
        self.db.close() #断开数据库连接
        logger.info('Database closed!')
        print("Database closed!")

