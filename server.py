#!/usr/bin/python
import json
import os
import zipfile
import shutil
from flask import Flask,url_for,request
from configLoader import configLoader 
from ossController import ossController

confloader = configLoader("des.config");

app = Flask(__name__)

@app.route('/')
def index():
    f = open("static/up.html","r").read()
    return f;

@app.route("/upload/",methods=["POST"])
def upload():
	if request.method == 'POST':
		f = request.files["file"];
		filename = request.form["url"].split("/")[-1];
		url = request.form["url"];
		bucket = request.form["bucket"];
		endpoint = request.form["endpoint"];
		if confloader.isExistBucket(bucket) == False:
			return json.dumps({"status":-1,"info":"Bucket Not Exist"});
		elif confloader.isExistBucket(bucket)["endpoint"] != endpoint:
			return json.dumps({"status":-1,"info":"Bucket or Endpoints not fit."});
		osscon = ossController(confloader.getAccessId(),confloader.getAccessSecret(),endpoint,bucket);
		remoteDes = url.split("//")[-1].lstrip(bucket+"."+endpoint+"/");
		if os.path.exists("upload-tmp") == False:
			 os.makedirs("upload-tmp"); 
		localfile = "upload-tmp/"+filename;
		f.save("upload-tmp/"+filename);
		ans = json.dumps(osscon.UpLoad(remoteDes,localfile));
		f.close();
		os.remove(localfile);
		return ans;
		
@app.route("/uploadZip/",methods=["POST"])
def uploadZip():
	ans = {}
	f = request.files["file"];
	filename = request.form["url"].rstrip("/").split("/")[-1];
        url = request.form["url"];
        bucket = request.form["bucket"];	
	endpoint = request.form["endpoint"];
	if confloader.isExistBucket(bucket) == False:
          return json.dumps({"status":-1,"info":"Bucket Not Exist"});
        elif confloader.isExistBucket(bucket)["endpoint"] != endpoint:
          return json.dumps({"status":-1,"info":"Bucket or Endpoints not fit."});
	osscon = ossController(confloader.getAccessId(),confloader.getAccessSecret(),endpoint,bucket);
	remoteDes = url.split("//")[-1].lstrip(bucket+"."+endpoint).lstrip("/");
	if os.path.exists("upload-tmp") == False:
          os.makedirs("upload-tmp");
	localfile = "upload-tmp/"+f.filename;
	f.save(localfile);
	localdir = "upload-tmp/"+f.filename.split(".")[0]+"/"
	f.close();
	f = zipfile.ZipFile(localfile,'r')	
	for file in f.namelist():
	  f.extract(file,localdir)
	shutil.rmtree(localdir);
	ans["info"] = osscon.UpLoadDir(remoteDes,localdir);
	ans["status"] = 0;
	return json.dumps(ans);


if __name__ == '__main__':
    app.run(host="0.0.0.0",port="5001")
