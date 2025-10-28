# DescribeSessions

Describes one or more Amazon DCV sessions.

###### Topics

- [Request parameters](#request "#request")
- [Response parameters](#response "#response")
- [Example](#example "#example")

## Request parameters

**`SessionIds`**

The IDs of the sessions to describe.

Type: String

Required: No

**`NextToken`**

The token to use to retrieve the next page of results.

Type: String

Required: No

**`Filters`**

Additional filters to apply to the request. Supported filters include:

- tag:key—The tags assigned to the session.
- owner—The session owner.

Type: String

Required: No

## Response parameters

**`Id`**

The unique ID of the session.

**`Name`**

The name of the session.

**`Owner`**

The owner of the session.

**`Server`**

Information about the server on which the session is running. This data structure includes the following
nested response parameters:

**`Ip`**

The IP address of the Amazon DCV server host.

**`Hostname`**

The hostname of the Amazon DCV server host.

**`Port`**

The port over which the Amazon DCV server communicates with Amazon DCV clients.

**`Endpoints`**

Information about the Amazon DCV server endpoints. This data structure includes
the following nested response parameters:

**`IpAddress`**

The IP address of the server endpoint.

**`Port`**

The port of the server endpoint.

**`Protocol`**

The protocol used by the server endpoint. Possible values include:

- `HTTP` — The endpoint uses the WebSocket (TCP) protocol.
- `QUIC` — The endpoint uses the QUIC (UDP) protocol.

**`WebUrlPath`**

The web URL path of the server endpoint. Available for the HTTP protocol only.

**`Tags`**

The tags assigned to the server. This data structure includes the following nested response parameters:

**`Key`**

The tag key.

**`Value`**

The tag value.

**`Type`**

The type of session.

**`State`**

The current state of the session. Possible values are:

- `CREATING` - the Broker is in the process of creating the session.
- `READY` - the session is ready to accept client connections.
- `DELETING` - the session is being deleted.
- `DELETED` - the session has been deleted.
- `UNKNOWN` - unable to determine the session's state. The Broker and the
  Agent might be unable to communicate.

**`Substate`**

The current substate of the session. Possible values are:

- `SESSION_PLACING` - the session is waiting to be placed on an available DCV Server.
- `PENDING_PREPARATION` - the session is created but not usable; linked to a DCV Server.

**`CreationTime`**

The date and time the session was created.

**`LastDisconnectionTime`**

The date and time of the last client disconnection.

**`NumOfConnections`**

The number of active client connections.

**`StorageRoot`**

Specifies the path to the folder used for session storage. For more information about the
Amazon DCV session storage, see [Enabling Session Storage](../adminguide/manage-storage.md "../adminguide/manage-storage.md") in the
_Amazon DCV Administrator Guide_.

Type: String

Required: No

## Example

Python

###### Request

The following example describes sessions that are owned by `user1` and have a tag
of `os=windows`.

```
from swagger_client.models.describe_sessions_request_data import DescribeSessionsRequestData
from swagger_client.models.key_value_pair import KeyValuePair

def get_sessions_api():
    api_instance = swagger_client.SessionsApi(swagger_client.ApiClient(get_client_configuration()))
    set_request_headers(api_instance.api_client)
    return api_instance

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
        owner='user1',
        tags=[{'Key': 'os', 'Value': 'windows'}])
```

###### Response

The following is the sample output.

```
{
    "Sessions": [
        {
            "Id": "SessionId1897",
            "Name": "a session name",
            "Owner": "an owner 1890",
            "Server": {
                "Ip": "1.1.1.123",
                "Hostname": "server hostname",
                "Port": "1222",
                "Endpoints": [
                    {
                        "IpAddress": "x.x.x.x",
                        "Port": 8443,
                        "WebUrlPath": "/",
                        "Protocol": "HTTP"
                    },
                    {
                        "IpAddress": "x.x.x.x",
                        "Port": 9443,
                        "WebUrlPath": "/",
                        "Protocol": "HTTP"
                    },
                    {
                        "IpAddress": "x.x.x.x",
                        "Port": 8443,
                        "WebUrlPath": "",
                        "Protocol": "QUIC"
                    }
                ],
                "Tags": [
                    {
                        "Key": "os",
                        "Value": "windows"
                    },
                    {
                        "Key": "ram",
                        "Value": "4gb"
                    }
                ]
            },
            "Type": "VIRTUAL",
            "State": "READY",
            "CreationTime": "2020-10-06T10:15:31.633Z",
            "LastDisconnectionTime": "2020-10-06T10:15:31.633Z",
            "NumOfConnections": 2,
            "StorageRoot" : "/storage/root"
        },
        {
            "Id": "SessionId1895",
            "Name": "a session name",
            "Owner": "an owner 1890",
            "Server": {
                "Ip": "1.1.1.123",
                "Hostname": "server hostname",
                "Port": "1222",
                "Endpoints": [
                    {
                        "IpAddress": "x.x.x.x",
                        "Port": 8443,
                        "WebUrlPath": "/",
                        "Protocol": "HTTP"
                    },
                    {
                        "IpAddress": "x.x.x.x",
                        "Port": 9443,
                        "WebUrlPath": "/",
                        "Protocol": "HTTP"
                    },
                    {
                        "IpAddress": "x.x.x.x",
                        "Port": 8443,
                        "WebUrlPath": "",
                        "Protocol": "QUIC"
                    }
                ],
                "Tags": [
                    {
                        "Key": "os",
                        "Value": "windows"
                    },
                    {
                        "Key": "ram",
                        "Value": "4gb"
                    }
                ]
            },
            "Type": "VIRTUAL",
            "State": "DELETING",
            "CreationTime": "2020-10-06T10:15:31.633Z",
            "LastDisconnectionTime": "2020-10-06T10:15:31.633Z",
            "NumOfConnections": 2,
            "StorageRoot" : "/storage/root"
        }
    ]
}
```
