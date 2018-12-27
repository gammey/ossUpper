# -*- coding: utf-8 -*-
#!/usr/bin/python

import oss2
import os;
import sys;


class ossController:
	def __init__(self, aid, akey, endp, bkname):
      		self.aid = aid;
      		self.akey = akey;
      		self.endp = endp;
		self.bkname = bkname;
		self.auth = oss2.Auth(self.aid, self.akey)
	def UpLoad(self,remotefile,localfile):
		service = oss2.Service(self.auth, self.endp);
		bk = oss2.Bucket(self.auth,"http://"+self.endp,self.bkname);
		ans = {};
		try:
			bk.put_object_from_file(remotefile,localfile);
			ans["status"] = 0;
			ans["info"] = "http://"+self.bkname+"."+self.endp+"/"+remotefile
			return ans;
		except:
			ans["status"] = -1;
                        ans["info"] = "Upload Failed."
	def listfile(self,dirpath):
    		_files = []
    		list = os.listdir(dirpath)
    		for i in range(0,len(list)):
           		path = os.path.join(dirpath,list[i])
           		if os.path.isdir(path):
              			_files.extend(self.listfile(path))
           		if os.path.isfile(path):
              			_files.append(path)
    		return _files
	def UpLoadDir(self,remotedir,localdir):
		filelist=self.listfile(localdir);
		localfilelist=[];
		remotefilelist=[];
		ans=[];
		for i in filelist:
			localfile = i;
			remotefile = remotedir.lstrip("/")+i.split(localdir)[-1].lstrip("/");
			print "upload "+localfile+" to "+remotefile;
			localfilelist.append(localfile);
                        remotefilelist.append(remotefile);
			ans.append(self.UpLoad(remotefile,localfile))
		return ans;

#ossc = ossController(AccessKeyId,AccessKeySecret,endPoint,myBucketName);
#print ossc.UpLoadDir("/upload-dir-test/","/var/log/")
#print ossc.UpLoad("upload-dir-test/20181012-L1800-Selleck-Tyrosine-Kinase-Inhibitor-Library-384.xlsx","/tmp/upload/20181012-L1800-Selleck-Tyrosine-Kinase-Inhibitor-Library-384.xlsx")
#ossUpFile(myossinfo,'123/index.txt','./123/local-backup.txt');
#print listfile("/tmp/gitaly-ruby611943089");

