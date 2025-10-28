# OpenServers

Opens one or more Amazon DCV servers. Before you can create Amazon DCV sessions on a Amazon DCV server,
you must change the server's state to _open_. After the Amazon DCV server is
_open_, you can create Amazon DCV sessions on the server.

###### Topics

- [Request parameters](#request "#request")
- [Response parameters](#response "#response")
- [Example](#example "#example")

## Request parameters

**`ServerId`**

The ID of the server to open.

Type: String

Required: Yes

## Response parameters

**`RequestId`**

The unique ID of the request.

**`SuccessfulList`**

Information about the Amazon DCV servers that were successfully opened. This data structure
includes the following nested response parameter:

**`ServerId`**

The ID of the server that was successfully opened.

**`UnsuccessfulList`**

Information about the Amazon DCV servers that could not be opened. This data structure
includes the following nested response parameters:

**`OpenServerRequestData`**

Information about the original request that failed. This data structure
includes the following nested response parameter:

**`ServerId`**

The ID of the Amazon DCV server that could not be opened.

**`FailureCode`**

The code of the failure.

**`FailureReason`**

The reason for the failure.

## Example

Python

###### Request

The following example opens two Amazon DCV servers (`serverId1` and
`serverId2`).

```
from swagger_client.models import OpenServerRequestData


def get_servers_api():
    api_instance = swagger_client.ServersApi(swagger_client.ApiClient(get_client_configuration()))
    set_request_headers(api_instance.api_client)
    return api_instance

def open_servers(server_ids):
    request = [OpenServerRequestData(server_id=server_id) for server_id in server_ids]
    print('Open Servers Request:', request)
    api_instance = get_servers_api()
    api_response = api_instance.open_servers(body=request)
    print('Open Servers Response:', api_response)

def main():
    open_servers(["serverId1", "serverId2"])
```

###### Response

The following is the sample output.

```
{
    "RequestId": "1e64830f-0a27-41bf-8147-0f3411791b64",
    "SuccessfulList": [
        {
            "ServerId": "serverId1"
        }
    ],
    "UnsuccessfulList": [
        {
            "OpenServerRequestData": {
                "ServerId": "serverId2"
            },
            "FailureCode": "DCV_SERVER_NOT_FOUND",
            "FailureReason": "Dcv server not found."
        }
    ]
}
```
