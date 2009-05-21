# Copyright 2008 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# gift = Gift(name='GC-101', discription=rmc,  under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import cgi

from google.appengine.api import users

from google.appengine.ext import db
from google.appengine.ext.db import djangoforms

import django
from django import http
from django.http import HttpResponse
from django import shortcuts

class Gift(db.Model):
  name = db.StringProperty(required=True)
  giver = db.UserProperty()
  latitude = db.StringProperty(required=True)

  longitude = db.TextProperty()
  url = db.URLProperty()
  created = db.DateTimeProperty(auto_now_add=True)
  modified = db.DateTimeProperty(auto_now=True)

class GiftForm(djangoforms.ModelForm):
  class Meta:
    model = Gift
    exclude = ['giver', 'created', 'modified']

def respond(request, user, template, params=None):
  """Helper to render a response, passing standard stuff to the response.

  Args:
    request: The request object.
    user: The User object representing the current user; or None if nobody
      is logged in.
    template: The template name; '.html' is appended automatically.
    params: A dict giving the template parameters; modified in-place.

  Returns:
    Whatever render_to_response(template, params) returns.

  Raises:
    Whatever render_to_response(template, params) raises.
  """
  if params is None:
    params = {}
  if user:
    params['user'] = user
    params['sign_out'] = users.CreateLogoutURL('/')
    params['is_admin'] = (users.IsCurrentUserAdmin() and
                          'Dev' in os.getenv('SERVER_SOFTWARE'))
  else:
    params['sign_in'] = users.CreateLoginURL(request.path)
  if not template.endswith('.html'):
    template += '.html'
  return shortcuts.render_to_response(template, params)


def placemark(request):
    user = users.GetCurrentUser()
#    gift = Gift.get(db.Key.from_path(Gift.kind(), int(126)))
    gifts3 = db.GqlQuery('SELECT * FROM Gift')
    gift = Gift.get(db.Key.from_path(Gift.kind(), gifts3.count()))
    return respond(request,user, 'placemark', {'gift': gift})

def home(request):
    user = users.GetCurrentUser()
    return respond(request,user, 'home2',{})
	
def css(request):
    user = users.GetCurrentUser()
    return respond(request,user, 'css',{})
	

def index(request):
    r = http.HttpResponse('<xsd:schema')
    r.write(' xmlns:xsd="http://www.w3.org/2001/XMLSchema">')
    r.write('      <xsd:element name="country" type="Country"/>')
    r.write('              <xsd:complexType name="Country">')
    r.write('                      <xsd:sequence>')
    r.write('                                  <xsd:element name="name" type="xsd:string"/>')
    r.write('                                              <xsd:element name="population" type="xsd:decimal"/>')
    r.write('                                                      </xsd:sequence>')
    r.write('                                                          </xsd:complexType>')
    r.write('                                                          </xsd:schema>')
    return r
    
def index2(request):
  """Request / -- show all places."""
  user = users.GetCurrentUser()
  gifts = db.GqlQuery('SELECT * FROM Gift ORDER BY created DESC')
  return respond(request, user, 'list', {'gifts': gifts})

def gps(request):
    imei = request.REQUEST["imei"]
    rmc = request.REQUEST["rmc"]
    gifts2 = db.GqlQuery('SELECT * FROM Gift')
    count = gifts2.count()
    html = "<html><body>count is %s.</body></html>" %count
    gift = Gift(name='GC-101', latitude=imei, longitude=rmc)
    gift.put()
    return http.HttpResponse(html)

#    user = users.GetCurrentUser()
#    imei = request.REQUEST("imei")
#    rmc = request.REQUEST("rmc")
#    return respond(request, user, 'gps', {'imei': imei, 'rmc': rmc})

def edit(request, gift_id):
  """Create or edit a gift.  GET shows a blank form, POST processes it."""
  user = users.GetCurrentUser()
#  if user is None:
#    return http.HttpResponseForbidden('You must be signed in to add or edit a place.')

  gift = None
  if gift_id:
    gift = Gift.get(db.Key.from_path(Gift.kind(), int(gift_id)))
    if gift is None:
      return http.HttpResponseNotFound('No place exists with that key (%r)' %
                                       gift_id)

  form = GiftForm(data=request.POST or None, instance=gift)

  if not request.POST:
    return respond(request, user, 'gift', {'form': form, 'gift': gift})

  errors = form.errors
  if not errors:
    try:
      gift = form.save(commit=False)
    except ValueError, err:
      errors['__all__'] = unicode(err)
  if errors:
    return respond(request, user, 'gift', {'form': form, 'gift': gift})

  if not gift.giver:
    gift.giver = user
  gift.put()

  return http.HttpResponseRedirect('/')

def new(request):
  """Create a gift.  GET shows a blank form, POST processes it."""
  return edit(request, None)
  
def newgpslocation(request):
	return gps(request)
