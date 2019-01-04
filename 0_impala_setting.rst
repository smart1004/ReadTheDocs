impala

https://stackoverflow.com/questions/21370431/how-to-access-hive-via-python/21380783


import jaydebeapi
import glob
# Creates a list of jar files in the /path/to/jar/files/ directory
jar_files = glob.glob('/path/to/jar/files/*.jar')

host='localhost'
port='10000'
database='default'

# note: your driver will depend on your environment and drivers you've
# downloaded in step 2
# this is the driver for my environment (jdbc3, hive2, cloudera enterprise)
driver='com.cloudera.hive.jdbc3.HS2Driver'

conn_hive = jaydebeapi.connect(driver,
        'jdbc:hive2://'+host+':' +port+'/'+database+';AuthMech=1;KrbHostFQDN='+host+';KrbServiceName=hive'
                           ,jars=jar_files)
