import consul
from django.http import HttpResponseRedirect

client = consul.Consul(host='172.19.0.100', port=8500)

home = "http://{}:{}/".format(client.catalog.service("main")[1][0]['Address'],
                              client.catalog.service("main")[1][0]['ServicePort'])
signin = "http://{}:{}/signin/".format(client.catalog.service("sign")[1][0]['Address'],
                                       client.catalog.service("sign")[1][0]['ServicePort'])

item_link = "http://{}:{}/items/".format(client.catalog.service("itemDetail")[1][0]['Address'],
                                         client.catalog.service("itemDetail")[1][0]['ServicePort'])
user_link = "http://{}:{}/user_detail/".format(client.catalog.service("userDetail")[1][0]['Address'],
                                               client.catalog.service("userDetail")[1][0]['ServicePort'])
search = "http://{}:{}/search/".format(client.catalog.service("search")[1][0]['Address'],
                                       client.catalog.service("search")[1][0]['ServicePort'])

# home = 'http://127.0.0.1:8001/'
# signin = 'http://127.0.0.1:8002/signin/'
# item_link = 'http://127.0.0.1:8003/items/'
# user_link = 'http://127.0.0.1:8004/user/'

link = {'home': home, 'signin': signin, 'item_link': item_link, 'user_link': user_link,'search':search}


def logout(request):
    response = HttpResponseRedirect(home)
    response.delete_cookie('TOKEN')
    return response
