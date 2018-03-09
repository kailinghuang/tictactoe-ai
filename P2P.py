import requests
import re
class P2P:
	def __init__(self):
		return
		
		 
		

	def CreateTeam(self,TeamName):
		url="http://www.notexponential.com/aip2pgaming/api/index.php"
		payload={'name':TeamName,'type':"team"}
		headers={'Authorization': "BASIC Og==",	'x-api-key': "a86936f2610c6d9d4627",'userId': "427",'Content-Type': "application/x-www-form-urlencoded"}
		response=requests.request("POST", url, data=payload, headers=headers)
		return response

	def AddTeamMember(self,TeamId,userId):
		url = "http://www.notexponential.com/aip2pgaming/api/index.php"
		payload = {'teamId':TeamId,'userId':userId,'type':"member"}
		
		headers = {'x-api-key': "a86936f2610c6d9d4627",'userid': "427",'Content-Type': "application/x-www-form-urlencoded"}
		response = requests.request("POST", url, data=payload, headers=headers)
		return response
	
	def GetTeamList(self,TeamId):
		url="http://www.notexponential.com/aip2pgaming/api/index.php"
		querystring={"type":"team","teamId":TeamId}
		headers = {'x-api-key': "a86936f2610c6d9d4627",'userId': "427",'Cache-Control': "no-cache"}
		response = requests.request("GET", url, headers=headers, params=querystring)
		
		return response
	
	def CreateGame(self,TeamId,RivalId):
		url = "http://www.notexponential.com/aip2pgaming/api/index.php"
		payload = {'teamId1':TeamId,'teamId2':RivalId,'type':"game"}
		headers = {
			'Authorization': "BASIC Og==",
    		'Content-Type': "application/x-www-form-urlencoded",
    		'x-api-key': "a86936f2610c6d9d4627",
    		'userId': "427"
    	}


		response = requests.request("POST", url, data=payload, headers=headers)
		
		return response
	def MakeMove(self,TeamId,Move,GameId):
		url = "http://www.notexponential.com/aip2pgaming/api/index.php"
		payload={'teamId':TeamId,'move':Move,'type':"move",'gameId':GameId}
		headers = {'Content-Type': "application/x-www-form-urlencoded",'x-api-key': "a86936f2610c6d9d4627",'userid': "427" }
		response = requests.request("POST", url, data=payload, headers=headers)

		return response
	def GetMoveList(self,GameId,count):
		url = "http://www.notexponential.com/aip2pgaming/api/index.php"
		querystring = {"type":"moves","gameId":GameId,"count":count}
		headers = {'x-api-key': "a86936f2610c6d9d4627",'userid': "427",'Cache-Control': "no-cache"}
		response = requests.request("GET", url, headers=headers, params=querystring)
		return response

		





if __name__ == '__main__':
	test=P2P()
	#response=test.AddTeamMember("1079","427")
	#response=test.CreateTeam("qunimagebide")
	#response=test.CreateGame("1070","1051")
	#response=test.MakeMove("1078","12,13","1128")
    
	response=test.GetMoveList("1171",6)
	print(response.text)
	#prog = re.compile(r'?<=\b"teamId":"\d\b)')
	#temp=prog.match(response)
	#result = re.findall(r'(?<=\b"teamId":")\d+\b',response.text)  
	#print(result)  
	
   
	


"""
	teamID = r[moves][teamID]
	move = r[moves][move]
	print(move)
"""

	



	


	#r=test.MakeMove("1070","4,4","427")
