from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext, loader, context
from dynamodb import *
import json

# Create your views here.

logger = logging.getLogger('django')


def index(request):
	return render_to_response('index.html', context=RequestContext(request))


def getdata(request, uuid=''):
	"""
	Get Plant Name
	"""
	if uuid == '':
		uuid = 'None'
	res_data = []
	dict_data = aws.read_from_db()
	logger.info('dict_data: {}'.format(dict_data))
	for dict_item in dict_data:
		res_data.append({'name': uuid,
		                 'temperature': str(dict_item['temperature']),
		                 'light': str(dict_item['light']),
		                 'humidity': str(dict_item['humidity']),
		                 'moisture': str(dict_item['moisture']),
		                 'timestamp': str(dict_item['TimeStamp'])})

	json_data = json.dumps(res_data)
	logger.info("json_data: {}".format(json_data))
	response = HttpResponse()
	response['Content-Type'] = "text/javascript"
	response.write(json_data)
	return response


def getplant(request):
	"""
	Get data from plant
	"""

	res_data = [{'name': 'plant 1'}, {'name': 'plant 2'}, {'name': 'plant 3'}]

	json_data = json.dumps(res_data)
	logger.info("json_data: {}".format(json_data))
	response = HttpResponse()
	response['Content-Type'] = "text/javascript"
	response.write(json_data)
	return response