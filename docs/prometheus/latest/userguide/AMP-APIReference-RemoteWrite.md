# RemoteWrite

The `RemoteWrite` operation writes metrics from a Prometheus server to a
remote URL in a standardized format. Typically, you will use an existing client such as
a Prometheus server to call this operation.

Valid HTTP verbs:

`POST`

Valid URIs:

`/workspaces/`workspaceId`/api/v1/remote_write`

URL query parameters:

None

`RemoteWrite` has an ingestion rate of 70,000 samples per second and
ingestion burst size of 1,000,000 samples.

**Sample request**

```
POST /workspaces/ws-b226cc2a-a446-46a9-933a-ac50479a5568/api/v1/remote_write --data-binary "@real-dataset.sz" HTTP/1.1
Authorization: AUTHPARAMS
X-Amz-Date: 20201201T193725Z
User-Agent: Prometheus/2.20.1
Content-Type: application/x-protobuf
Content-Encoding: snappy
X-Prometheus-Remote-Write-Version: 0.1.0

`body`
```

###### Note

For the request body syntax, see to the protocol buffer definition at [https://github.com/prometheus/prometheus/blob/1c624c58ca934f618be737b4995e22051f5724c1/prompb/remote.pb.go#L64](https://github.com/prometheus/prometheus/blob/1c624c58ca934f618be737b4995e22051f5724c1/prompb/remote.pb.go#L64 "https://github.com/prometheus/prometheus/blob/1c624c58ca934f618be737b4995e22051f5724c1/prompb/remote.pb.go#L64").

**Sample response**

```
HTTP/1.1 200 OK
x-amzn-RequestId: 12345678-abcd-4442-b8c5-262b45e9b535
Content-Length:0
Connection: keep-alive
Date: Tue, 01 Dec 2020 19:37:25 GMT
Content-Type: application/json
Server: amazon
vary: Origin
```
