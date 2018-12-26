#!/usr/bin/python
import ConfigParser
import oss2

class configLoader:
	def __init__(self,configfile):
		self.parser=ConfigParser.SafeConfigParser()
		self.parser.read(configfile);
	def getAccessId(self):
		return self.parser.get("oss","access-id");
	def getAccessSecret(self):
		return self.parser.get("oss","access-secret");
	def getEndpoint(self):
		endpoint = self.parser.get("oss","endpoint");
		ans = [];
		for i in endpoint.split(","):
			ans.append(i)
		return ans;
	def getBucketList(self):
		ans=[];
		auth = oss2.Auth(self.getAccessId(),self.getAccessSecret());
		service = oss2.Service(auth, "oss-cn-hangzhou.aliyuncs.com");
		for i in service.list_buckets().buckets:
			bkinfo={};
			bkinfo = {"endpoint":i.location+".aliyuncs.com","bkname":i.name,"domain":i.location+"."+i.location+".aliyuncs.com"}
			ans.append(bkinfo);
		return ans;
	def isExistBucket(self,bkname):
		bklist = self.getBucketList();
		for i in bklist:
			if i["bkname"] == bkname:
				return i
		return False

#confloader=configLoader("des.config");
#print confloader.isExistBucket("2publicimtest");
#print confloader.getBucketList()
