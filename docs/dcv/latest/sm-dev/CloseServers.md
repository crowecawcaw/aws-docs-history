# CloseServers

Closes one or more Amazon DCV servers. When you close a Amazon DCV server, you make it
unavailable for Amazon DCV session placement. You cannot create Amazon DCV sessions on
_closed_ servers. Closing a server ensures that no sessions
are running on it and that users cannot create new sessions on it.

###### Topics

- [Request parameters](#request "#request")
- [Response parameters](#response "#response")
- [Example](#example "#example")

## Request parameters

**`ServerId`**

The ID of the server to close.

Type: String

Required: Yes

**`Force`**

Forces the close operation. If you specify `true`, the server is closed even
if it has running sessions. The sessions continue to run.

Type: Boolean

Required: No

## Response parameters

**`RequestId`**

The unique ID of the request.

**`SuccessfulList`**

Information about the Amazon DCV servers that were successfully closed. This data structure
includes the following nested response parameter:

**`ServerId`**

The ID of the server that was successfully closed.

**`UnsuccessfulList`**

Information about the Amazon DCV servers that could not be closed. This data structure
includes the following nested response parameters:

**`CloseServerRequestData`**

Information about the original request that failed. This data structure
includes the following nested response parameter:

**`ServerId`**

The ID of the Amazon DCV server that could not be closed.

**`Force`**

The requested force parameter.

**`FailureCode`**

The code of the failure.

**`FailureReason`**

The reason for the failure.

## Example

Python

###### Request

The following example closes two Amazon DCV servers (`serverId1` and
`serverId2`). Server `serverId2` doesn't
exist and results in a failure.

```
from swagger_client.models import CloseServerRequestData

def get_servers_api():
    api_instance = swagger_client.ServersApi(swagger_client.ApiClient(get_client_configuration()))
    set_request_headers(api_instance.api_client)
    return api_instance

def close_servers(server_ids):
    request = [CloseServerRequestData(server_id=server_id) for server_id in server_ids]
    print('Close Servers Request:', request)
    api_instance = get_servers_api()
    api_response = api_instance.close_servers(body=request)
    print('Close Servers Response:', api_response)
    open_servers(server_ids)

def main():
    close_servers(["serverId1", "serverId2"])
```

###### Response

The following is the sample output.

```
{
    "RequestId": "4d7839b2-a03c-4b34-a40d-06c8b21099e6",
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
