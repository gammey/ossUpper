Requirements:

python2.7

pip install oss2 flask uwsgi



Configration:

cp des.config-sample des.conf

modify des.config such as

##########################

[oss]

access-id=[your aliyun accessid]

access-secret=[your aliyun accesssecret]

endpoint=[your endpoints of your buckets] #if you have different buckets with different endpoints you can fill your endpoints split 
with ','.

##########################


Start Server:

You can start server with command in develop env:

You can start server with command:

python server.py

Or you can start it with nohup:

nohup python server.py &> /dev/null

You can start server with command in product env:

uwsgi --http 0.0.0.0:5001 --module server:app

Or you can start it with nohup:

nohup uwsgi --http 0.0.0.0:5001 --module server:app &> /dev/null

Use:

After you start server,you can view the url: http://[youripaddress]:5001/

