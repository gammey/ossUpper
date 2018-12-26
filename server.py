#!/usr/bin/python
import json
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
			return "Bucket Not Exist";
		elif confloader.isExistBucket(bucket)["endpoint"] != endpoint:
			return "Endpoint Not Fit.";
		osscon = ossController(confloader.getAccessId(),confloader.getAccessSecret(),endpoint,bucket);
		remoteDes = url.split("//")[-1].lstrip(bucket+"."+endpoint+"/");
		localfile = "upload-tmp/"+filename;
		f.save("upload-tmp/"+filename);
		ans = osscon.UpLoad(remoteDes,localfile);
		return ans;
		

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="5001",debug=True)
