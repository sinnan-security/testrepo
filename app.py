from flask import Flask,jsonify,request,make_response
from dotenv import load_dotenv
from urllib.parse import urlparse
import psycopg2
import psutil
app = Flask(__name__)
config=dotenv_values("/etc/generic.conf")
p = urlparse(config['db'])
pg_connection_dict = {'dbname': p.hostname,'user': p.username,'password': p.password,'port': p.port,'host': p.scheme}

@app.route('/health', methods=['GET'])
def health():
	try:
		psycopg2.connect(**pg_connection_dict).close()
		db="True"
	except:
		db="False"
	return make_response(jsonify({
		'auth_service':{
			'key','value'
		}
	}),200)

@app.route('/SomeRoute', methods=['GET'])
@app.route('/SomeRoute', methods=['POST'])
@app.route('/SomeRoute', methods=['PUT'])
@app.route('/SomeRoute', methods=['DELETE'])
def SomeFunctionality():
	response={}
	logger(request,response)
	return "<h1>PLACEHOLDER</H1>"

def logger(request,response):
	tmp='headers:{'
	for header in request.headers:
		tmp=tmp+'"'+header[0]+'":"'+header[1]+'"'
	tmp=tmp+'}'
	p=open(config["log_path"],"a")
	p.write("\nRequest Log-[")
	p.write(" "+request.method)
	p.write(" "+request.full_path)
	p.write(" "+tmp)
	p.write(" "+"body:"+request.get_data(as_text=True)+"]")
	p.close()

if __name__ == "__main__":
	app.run(host=config["host"],port=config["port"])
