# GetAlertManagerStatus

The `GetAlertManagerStatus` retrieves information about the status of alert
manager.

Valid HTTP verbs:

`GET`

Valid URIs:

`/workspaces/`workspaceId`/alertmanager/api/v2/status`

URL query parameters: none

**Sample request**

```
GET /workspaces/ws-b226cc2a-a446-46a9-933a-ac50479a5568/alertmanager/api/v2/status HTTP/1.1
Content-Length: 0,
Authorization: AUTHPARAMS
X-Amz-Date: 20201201T193725Z
User-Agent: Grafana/8.1.0
```

**Sample response**

```
HTTP/1.1 200 OK
x-amzn-RequestId: 12345678-abcd-4442-b8c5-262b45e9b535
Content-Length: 941
Connection: keep-alive
Date: Tue, 01 Dec 2020 19:37:25 GMT
Content-Type: application/json
Server: amazon
vary: Origin

{
    "cluster": null,
    "config": {
        "original": "global:\n  resolve_timeout: 5m\n  http_config:\n    follow_redirects: true\n  smtp_hello: localhost\n  smtp_require_tls: true\nroute:\n  receiver: sns-0\n  group_by:\n  - label\n  continue: false\nreceivers:\n- name: sns-0\n  sns_configs:\n  - send_resolved: false\n    http_config:\n      follow_redirects: true\n    sigv4: {}\n    topic_arn: arn:aws:sns:us-west-2:123456789012:test\n    subject: '{{ template \"sns.default.subject\" . }}'\n    message: '{{ template \"sns.default.message\" . }}'\n    workspace_arn: arn:aws:aps:us-west-2:123456789012:workspace/ws-58a6a446-5ec4-415b-9052-a449073bbd0a\ntemplates: []\n"
    },
    "uptime": null,
    "versionInfo": null
}
```
