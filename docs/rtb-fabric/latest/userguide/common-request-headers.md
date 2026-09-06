

# Common request headers
<a name="common-request-headers"></a>

The following table describes request headers that are common to most RTB Fabric requests.


| Header | Description | 
| --- | --- | 
| x-forwarded-proto | Request header which identifies the protocol (HTTP or HTTPS) that the client used to connect to the gateway. This is available only for external inbound links.<br />Type: String | 
| x-forwarded-port | Request header which identifies the port that the client used to connect to the gateway. This is available only for external inbound links.<br />Type: String | 
| x-forwarded-host | Request header which identifies the original host requested by the client in the Host HTTP request header. This is available only for external inbound links.<br />Type: String | 