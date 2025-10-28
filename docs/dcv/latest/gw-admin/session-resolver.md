# Setting up a Session Resolver

The _Session Resolver_ is the component responsible for mapping _Session IDs_
to a destination host running the Amazon DCV server. The logic of this mapping is specific to how each customer designs and plans
to use its infrastructure.

The following topics describe how customers can implement a _Session Resolver_ that matches
their requirements and configure it in the Amazon DCV Connection Gateway. Customers using the [Amazon DCV Session Manager](../sm-admin/what-is-sm.md "../sm-admin/what-is-sm.md")
can refer to [Integrating Connection Gateway with Session Manager](sm-integration.md "sm-integration.md") to learn how to use the Session Resolver end-point included in the Amazon DCV Session Manager.

###### Topics

- [Implementing a Session Resolver](#implementing-session-resolver "#implementing-session-resolver")
- [Configuration](#configure-resolver "#configure-resolver")

## Implementing a Session Resolver

Your session resolver service can run on the same host as the Amazon DCV Connection Gateway or it can run on a separate host.
The authentication service must listen for HTTP(S) POST requests from the Connection Gateway.

The following shows the POST request format used by the Connection Gateway.

```
POST /resolveSession?sessionId=`session_id`&transport=`transport`&clientIpAddress=`clientIpAddress` HTTP/1.1
accept: application/json
```

The `sessionId` parameter contains a string which uniquely identifies a DCV session,
the `transport` parameter will either be `HTTP` or `QUIC`,
the `clientIpAddress` will be the ip address of the client, or the load balancer ip address if the gateway is fronted by a load balancer,
the `clientIpAddress` can either be an IPv4 or IPv6 address. In case the gateway cannot get the client ip, it will not be present in the request.

Your session resolver service is responsible for determining the destination host, if any, where to forward
the connection and returns its response to the Connection Gateway.

- If a destination is not found, the session resolver service returns an HTTP status `404`
- If a destination is successfully identified, the session resolver service returns an HTTP status `200`
  and the response body must contain the following JSON:

```
{
    "SessionId": `session_id`,
    "TransportProtocol": `transport_protocol`,
    "DcvServerEndpoint": `dns_name`,
    "Port": `port`,
    "WebUrlPath": `web_url_path`
}
```

The `SessionId` field normally would just return the same ID that was provided as input, however,
if it is useful for your use case, you can also use this field to map a client-facing session ID to a different
session ID used internally by your infrastructure. The `TransportProtocol` field must be either
`HTTP` or `QUIC` (uppercase).

Example session resolver python implementation

```
from flask import Flask, request
import json

app = Flask(__name__)

dcv_sessions = {
  "session-123": {
    "SessionId": "session-123",
    "Host": "dcv123.mycompany.com",
    "HttpPort": 8443,
    "QuicPort": 8443,
    "WebUrlPath": "/"
  },
  "session-456": {
    "SessionId": "session-456",
    "Host": "dcv456.mycompany.com",
    "HttpPort": 8443,
    "QuicPort": 8443,
    "WebUrlPath": "/"
  }
}

@app.route('/resolveSession', methods=['POST'])
def resolve_session():
    session_id = request.args.get('sessionId')
    transport = request.args.get('transport')
    client_ip_address = request.args.get('clientIpAddress')

    if session_id is None:
        return "Missing sessionId parameter", 400

    if transport != "HTTP" and transport != "QUIC":
        return "Invalid transport parameter: " + transport, 400

    print("Requested sessionId: " + session_id + ", transport: " + transport + ", clientIpAddress: " + client_ip_address)
    dcv_session = dcv_sessions.get(session_id);
    if dcv_session is None:
        return "Session id not found", 404

    response = {
        "SessionId": dcv_session['SessionId'],
        "TransportProtocol": transport,
        "DcvServerEndpoint": dcv_session['Host'],
        "Port": dcv_session["HttpPort"] if transport == "HTTP" else dcv_session['QuicPort'],
        "WebUrlPath": dcv_session['WebUrlPath']
    }
    return json.dumps(response)


if __name__ == '__main__':
    app.run(port=9000, host='0.0.0.0')
```

## Configuration

You must configure the Amazon DCV Connection Gateway to use the Session Resolver service.

###### To specify a session resolver

1. Navigate to the `/etc/dcv-connection-gateway/` folder and open the `dcv-connection-gateway.conf` with your preferred text editor.
2. Locate the `[resolver]` and set the `url` parameter to the URL of your session resolver.

```
[resolver]
url = "http://localhost:9000"
```

3. Save and close the file.
