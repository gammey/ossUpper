Requirements:

python2.7
<<<<<<< HEAD
pip install oss2 flask uwsgi
=======

pip install oss2 flask
>>>>>>> 55252410ffaa55ec5aabce8830c028e0abd52fa6


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
<<<<<<< HEAD
You can start server with command in develop env:
=======

You can start server with command:

>>>>>>> 55252410ffaa55ec5aabce8830c028e0abd52fa6
python server.py

Or you can start it with nohup:

nohup python server.py &> /dev/null

<<<<<<< HEAD
You can start server with command in product env:
uwsgi --http 0.0.0.0:5001 --module server:app
Or you can start it with nohup:
nohup uwsgi --http 0.0.0.0:5001 --module server:app &> /dev/null
=======
>>>>>>> 55252410ffaa55ec5aabce8830c028e0abd52fa6

Use:

After you start server,you can view the url: http://[youripaddress]:5001/

