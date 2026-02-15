# Step 3: Get an access token and make an API request

This example will walk through the steps to get your access token set up, then
show you how to make a basic API request. This will give you the foundational knowledge
to start building more advanced applications powered by the Amazon DCV API.

In this example, we'll show you how to do this by using the `DescribeSessions` API.

###### Example

First we import the models needed for the application.

Then we declare variables for the client ID (`__CLIENT_ID`), client password
(`__CLIENT_SECRET`), and the Broker URL, including the port number
(`__PROTOCOL_HOST_PORT`).

Next, we create a function called `build_client_credentials` that generates the
client credentials. To generate the client credentials, you must first concatenate the
client ID and client password and separate the values with a colon
(``client_ID`:`client_password``),
and then Base64 encode the entire string.

```
import swagger_client
import base64
import requests
import json
from swagger_client.models.describe_sessions_request_data import DescribeSessionsRequestData
from swagger_client.models.key_value_pair import KeyValuePair
from swagger_client.models.delete_session_request_data import DeleteSessionRequestData
from swagger_client.models.update_session_permissions_request_data import UpdateSessionPermissionsRequestData
from swagger_client.models.create_session_request_data import CreateSessionRequestData

__CLIENT_ID = '794b2dbb-bd82-4707-a2f7-f3d9899cb386'
__CLIENT_SECRET = 'MzcxNzJhN2UtYjEzNS00MjNjLTg2N2YtMjFlZmRlZWNjMDU1'
__PROTOCOL_HOST_PORT = 'https://<broker-hostname>:8443'

def build_client_credentials():
    client_credentials = '{client_id}:{client_secret}'.format(client_id=__CLIENT_ID, client_secret=__CLIENT_SECRET)
    return base64.b64encode(client_credentials.encode('utf-8')).decode('utf-8')

```

Now that we have our client credentials, we can use it to request an access token from the Broker.
To do this, we create a function called `get_access_token`. You must call a `POST` on
`https://`Broker_IP`:`8443`/oauth2/token?grant_type=client_credentials`,
and provide an authorization header, which includes the Basic-encoded client credentials, and a
content type of `application/x-www-form-urlencoded`.

```

def get_access_token():
    client_credentials = build_client_credentials()
    headers = {
        'Authorization': 'Basic {}'.format(client_credentials),
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    endpoint = __PROTOCOL_HOST_PORT + '/oauth2/token?grant_type=client_credentials'
    print('Calling', endpoint, 'using headers', headers)
    res = requests.post(endpoint, headers=headers, verify=True)
    if res.status_code != 200:
        print('Cannot get access token:', res.text)
        return None
    access_token = json.loads(res.text)['access_token']
    print('Access token is', access_token)
    return access_token
```

Now, we create the functions needed to instantiate a client API. To instantiate a client
API, you must specify the client configuration and the headers to be used for requests.
The `get_client_configuration` function creates a configuration object that
includes the Broker's IP address and port and the path to Broker's self-signed
certificate, which you should have received from the Broker administrator. The
`set_request_headers` function creates a request header object that
includes the client credentials and the access token.

```
def get_client_configuration():
    configuration = swagger_client.Configuration()
    configuration.host = __PROTOCOL_HOST_PORT
    configuration.verify_ssl = True
    # configuration.ssl_ca_cert = cert_file.pem
    return configuration

def set_request_headers(api_client):
    access_token = get_access_token()
    api_client.set_default_header(header_name='Authorization',
                                  header_value='Bearer {}'.format(access_token))

def get_sessions_api():
    api_instance = swagger_client.SessionsApi(swagger_client.ApiClient(get_client_configuration()))
    set_request_headers(api_instance.api_client)
    return api_instance

```

Finally, we create a main method that calls the `DescribeSessions` API. For
more information, see [DescribeSessions](DescribeSessions.md "DescribeSessions.md").

```

def describe_sessions(session_ids=None, next_token=None, tags=None, owner=None):
    filters = list()
    if tags:
        for tag in tags:
            filter_key_value_pair = KeyValuePair(key='tag:' + tag['Key'], value=tag['Value'])
            filters.append(filter_key_value_pair)
    if owner:
        filter_key_value_pair = KeyValuePair(key='owner', value=owner)
        filters.append(filter_key_value_pair)

    request = DescribeSessionsRequestData(session_ids=session_ids, filters=filters, next_token=next_token)
    print('Describe Sessions Request:', request)
    api_instance = get_sessions_api()
    api_response = api_instance.describe_sessions(body=request)
    print('Describe Sessions Response', api_response)

def main():
    describe_sessions(
        session_ids=['SessionId1895', 'SessionId1897'],
        owner='an owner 1890',
        tags=[{'Key': 'ram', 'Value': '4gb'}])
```
