# !/usr/bin/python
# -*- coding: UTF-8 -*-
DUMP=/usr/bin/mysqldump
OUT_DIR=/mysqlback-sql
DB_NAME=wj kettle
DB_USER="root"
DB_PASS="Edoctor123!"
cd $OUT_DIR
DATE=`date +%Y_%m_%d`
OUT_SQL="$DATE.sql"
TAR_SQL="mysql_$DATE.tar.gz"
$DUMP --default-character-set=utf8 --opt -u$DB_USER -p$DB_PASS --all-databases