# GetSessionConnectionData

Gets connection information for a specific user's connection to a specific Amazon DCV session.

###### Topics

- [Request parameters](#request "#request")
- [Response parameters](#response "#response")
- [Additional info](#additional-info "#additional-info")
- [Example](#example "#example")

## Request parameters

**`SessionId`**

The ID of the session for which to view connection information.

Type: String

Required: Yes

**`User`**

The name of the user for which to view connection information.

Type: String

Required: Yes

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

**`WebUrlPath`**

The path to the Amazon DCV server's configuration file.

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

**`CreationTime`**

The date and time the session was created.

**`LastDisconnectionTime`**

The date and time of the last client disconnection.

**`NumOfConnections`**

The number of concurrent connections the user has to the session.

**`ConnectionToken`**

The authentication token used to connect to the session.

## Additional info

The information obtained from this API can be passed to a Amazon DCV client in order to connect to the Amazon DCV session.

In the case of the Amazon DCV Web client, you can build an URL that can be opened in the browser. The URL has the following format:

```
https://`{Ip}`:`{Port}{WebUrlPath}`?authToken=`{ConnectionToken}`#`{SessionId}`.
```

In the case of the Amazon DCV native client, you can build an URL with the `dcv://` schema. When the Amazon DCV native client is installed, it registers itself with the system as the handler for `dcv://` URLs. The URL has the following format:

```
dcv://`{Ip}`:`{Port}{WebUrlPath}`?authToken=`{ConnectionToken}`#`{SessionId}`.
```

###### Note

If you're using Amazon EC2, the IP address should be the public one. If your configuration has Amazon DCV hosts behind a gateway, specify the gateway address rather than the one returned by the SessionConnectionData API.

## Example

Python

###### Request

The following example gets connection information for a user with a user name of
`user1` and a session with an ID of
`sessionId12345`.

```
def get_session_connection_api():
    api_instance = swagger_client.GetSessionConnectionDataApi(swagger_client.ApiClient(get_client_configuration()))
    set_request_headers(api_instance.api_client)
    return api_instance


def get_url_to_connect(api_response):
    ip_address = api_response.session.server.ip
    port = api_response.session.server.port
    web_url_path = api_response.session.server.web_url_path
    connection_token = api_response.connection_token
    session_id = api_response.session.id
    url = f'https://{ip_address}:{port}{web_url_path}?authToken={connection_token}#{session_id}'
    return url


def get_session_connection_data(session_id, user):
    api_response = get_session_connection_api().get_session_connection_data(session_id=session_id, user=user)
    url_to_connect = get_url_to_connect(api_response)
    print('Get Session Connection Data Response:', api_response)
    print('URL to connect: ', url_to_connect)


def main():
    get_session_connection_data('sessionId12345', 'user1')

```

###### Response

The following is the sample output.

```
{
    "Session": {
        "Id": "sessionId12345",
        "Name": "a session name",
        "Owner": "an owner 1890",
        "Server": {
            "Ip": "1.1.1.123",
            "Hostname": "server hostname",
            "Port": "1222",
            "endpoints": [
                {
                    "port": 8443,
                    "web_url_path": "/",
                    "protocol": "HTTP"
                },
                {
                    "port": 9443,
                    "web_url_path": "/",
                    "protocol": "HTTP"
                },
                {
                    "port": 8443,
                    "web_url_path": "",
                    "protocol": "QUIC"
                }
            ],
            "WebUrlPath": "/path",
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
        "State": "UNKNOWN",
        "CreationTime": "2020-10-06T10:15:31.633Z",
        "LastDisconnectionTime": "2020-10-06T10:15:31.633Z",
        "NumOfConnections": 2
    },
    "ConnectionToken": "EXAMPLEiOiJmOWM1YTRhZi1jZmU0LTQ0ZjEtYjZlOC04ZjY0YjM4ZTE2ZDkiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJkY3ZTZXNzaW9uSWQiOiJTZXNzaW9uSWQxODk5IiwiZGN2U2Vzc2lvbk93bmVyIjoiYW4gb3duZXIgMTEXAMPLEmRjdlNlc3Npb25Vc2VyIjoibXlVc2VyIiwiZXhwIjoxNjAxOTg1NDA4LCJpYXQiOjE2MDE5ODE4MDgsImp0aSI6IjgwMjljNDUwLTQwMDUtNDJhMy04YTQzLWFmZTM3ZTc4NTQ0ZCJ9.N0RRRT1FZuBgex_0iFwKBAdHdM2JSSADc-tngiKXevUxhhJvm3BPJYRs9NPE4GCJRTc13EXAMPLEIxNEPPh5IMcVmROfU1WKPnry4ypPTp3rsZ7YWjCTSfs1GoN3R_nLFyAxfhPD2yY-Kqtpd5GH0D-E8FwsedV-Q2bRQ4y9y1q0MgFU4QjaSMypUuYR0YjkCaoainjmEZew4A33fG40wATrBvoivBiNWdNpytHX2CDOuk_k0k_DWeZjMvv9jF1f5EXAMPLEm9h5zj_Nb1PKKfBSx9_O6gSJwC9UD-h_GaMgHmltqBIA4jdPD7i0CmC2e7413KFy-EQ4Ej1cM7RjLwhFuWpKWAVJxogJjYpfoKKaPo4KxvJjJIPYhkscklINQpe2W5rnlxCq7sC7ptcGw17DUobP7egRv9H37VD8SrkLyq-hK1G4G8erHvl9HIrTR9_c884fNrTCC8DvC062e4KYdLkAhhJmboN9CAGIGFyd2c1AY_CzzvDL0EXAMLE"
}
```
