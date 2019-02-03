#!/usr/bin/env python
# coding: utf-8

import asana
from workflow import Workflow3


try:
	personal_access_token = Workflow3().get_password('asana')
	client = asana.Client.access_token(personal_access_token)
	me = client.users.me()
	workspace_id = me['workspaces'][0]['id']
	tasks = {'assignee': 'me', 'workspace': workspace_id}
	fields = ['assignee_status','name', 'completed', 'notes']

	i = 0
	for task in client.tasks.find_all(tasks,fields=fields):
		should_show = task['assignee_status'] == 'today'
		should_show &= not task['completed']
		should_show &= not task['name'].endswith(':')
		if should_show:
			if i == 0:
				print task['name']
				print "---"
			i += 1 
			print "{}|href=https://app.asana.com/0/1/{}".format(task['name'],task['id'])
except:
    print "🤔"
    print "---"
    print "Sorry, something went wrong!"

