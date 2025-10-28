# ListAlertManagerAlertGroups

The `ListAlertManagerAlertGroups` operation retrieves a list of alert
groups configured in alert manager in the workspace.

Valid HTTP verbs:

`GET`

Valid URIs:

`/workspaces/`workspaceId`/alertmanager/api/v2/alerts/groups`

URL query parameters:

`active` Boolean. If true, the returned list includes active
alerts. The default is true. Optional

`silenced` Boolean. If true, the returned list includes
silenced alerts. The default is true. Optional

`inhibited` Boolean. If true, the returned list includes
inhibited alerts. The default is true. Optional

`filter` An array of strings. A list of matchers to filter
alerts by. Optional

`receiver` String. A regular expression matching receivers to
filter alerts by. Optional

**Sample request**

```
GET /workspaces/ws-b226cc2a-a446-46a9-933a-ac50479a5568/alertmanager/api/v2/alerts/groups HTTP/1.1
Content-Length: 0,
Authorization: AUTHPARAMS
X-Amz-Date: 20201201T193725Z
User-Agent: Grafana/8.1.0
```

**Sample response**

```
HTTP/1.1 200 OK
x-amzn-RequestId: 12345678-abcd-4442-b8c5-262b45e9b535
Content-Length: 443
Connection: keep-alive
Date: Tue, 01 Dec 2020 19:37:25 GMT
Content-Type: application/json
Server: amazon
vary: Origin

[
    {
        "alerts": [
            {
                "annotations": {
                    "summary": "this is a test alert used for demo purposes"
                },
                "endsAt": "2021-10-21T22:07:31.501Z",
                "fingerprint": "375eab7b59892505",
                "receivers": [
                    {
                        "name": "sns-0"
                    }
                ],
                "startsAt": "2021-10-21T22:02:31.501Z",
                "status": {
                    "inhibitedBy": [],
                    "silencedBy": [],
                    "state": "unprocessed"
                },
                "updatedAt": "2021-10-21T22:02:31.501Z",
                "generatorURL": "https://www.amazon.com/",
                "labels": {
                    "alertname": "test-alert"
                }
            }
        ],
        "labels": {},
        "receiver": {
            "name": "sns-0"
        }
    }
]
```
