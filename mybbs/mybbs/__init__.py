import pymysql
pymysql.version_info = (2, 1, 1, "final", 0)  # 指定了pymysql的版本,按照你版本修改
pymysql.install_as_MySQLdb()