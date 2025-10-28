# GetSessionScreenshots

Gets screenshots of one or more Amazon DCV sessions.

To modify the image format, configure the `session-screenshot-format`
parameter on the Session Manager Broker configuration. See
[Broker configuration file](../sm-admin/broker-file.md "../sm-admin/broker-file.md")
in the _Amazon DCV Session Manager Administrator Guide_.

When the `MaxWidth` or `MaxHeight` parameters of the
`GetSessionScreenshots` request are not specified, the
`session-screenshot-max-width` and `session-screenshot-max-height`
values set in the Session Manager Broker configuration file will be used. To
modify those parameters, also see [Broker configuration file](../sm-admin/broker-file.md "../sm-admin/broker-file.md")
in the _Amazon DCV Session Manager Administrator Guide_.

The upper value for the screenshot resolution is limited to the remote session resolution. If the
`MaxWidth` and `MaxHeight` parameters are set to values higher than the current
remote session resolution, the resulting screenshot will be limited to the actual session resolution.

###### Note

To modify these values from the Access Console, see the
[Web Client configuration file](../access-console/web-client-config-files.md "../access-console/web-client-config-files.md")
in the _Amazon DCV Access Console Administrator Guide_.
To modify these values with the Session Manager CLI, see `get-session-screenshots` in the _Amazon DCV CLI Guide_.

###### Topics

- [Request parameters](#request "#request")
- [Response parameters](#response "#response")
- [Example](#example "#example")

## Request parameters

**`SessionId`**

The ID of the Amazon DCV session from which to get the screenshot.

Type: String

Required: Yes

**`MaxWidth`**

The maximum width, in pixels, of session screenshots. If not specified,
the values from the Session Manager Broker configuration will apply. If
provided, this must be a number greater than 0.

Type: Integer

Required: No

**`MaxHeight`**

The maximum height, in pixels, of session screenshots. If not specified,
the values from the Session Manager Broker configuration will apply. If provided, this must
be a number greater than 0.

Type: Integer

Required: Yes

## Response parameters

**`RequestId`**

The unique ID of the request.

**`SuccessfulList`**

Information about the successful screenshots. This data structure includes the following
nested response parameters:

**`SessionScreenshot`**

Information about the screenshots. This data structure includes the following
nested response parameters:

**`SessionId`**

The ID of the Amazon DCV session from which the screenshot was taken.

**`Images`**

Information about the images. This data structure includes the following
nested response parameters:

**`Format`**

The format of the image. Possible values include: `jpeg`
and `png`.

**`Data`**

The screenshot image base64 encoded format.

**`CreationTime`**

The date and time the screenshot was taken.

**`Primary`**

Indicates whether the screenshot is of the Amazon DCV session's primary
display.

**`UnsuccessfulList`**

Information about the unsuccessful screenshots. This data structure includes the following
nested response parameters:

**`GetSesionScreenshotRequestData`**

The original request that failed.

**`SessionId`**

The ID of the Amazon DCV session from which the screenshot was to be taken.

**`FailureReason`**

The reason for the failure.

**`GetSessionScreenshotRequestData`**

The original request that failed.

## Example

Python

###### Request

The following example gets screenshots from two sessions (`sessionId1` and
`sessionId2`) with the max width set at 800 and the max height set at 600. Session
`sessionId2` doesn't exist and results in a failure.

```
from swagger_client.models.describe_servers_request_data import GetSessionScreenshotRequestData

def get_sessions_api():
    api_instance = swagger_client.ServersApi(swagger_client.ApiClient(get_client_configuration()))
    set_request_headers(api_instance.api_client)
    return api_instance

def get_session_screenshots(session_ids, max_width=None, max_height=None):
    request = [GetSessionScreenshotRequestData(session_id=session_id, max_width=max_width, max_height=max_height) for session_id in session_ids]
    print('Get Session Screenshots Request:', request)
    api_instance = get_sessions_api()
    api_response = api_instance.get_session_screenshots(body=request)
    print('Get Session Screenshots Response:', api_response)

def main():
    get_session_screenshots(["sessionId1", "sessionId2"]), 800, 600)
```

###### Response

The following is the sample output.

```
{
    "RequestId": "542735ef-f6ab-47d8-90e5-23df31d8d166",
    "SuccessfulList": [
        {
            "SessionScreenshot": {
                "SessionId": "sessionId1",
                "Images": [
                    {
                        "Format": "png",
                        "Data": "iVBORw0KGgoAAAANSUhEUgAAAEXAMPLE",
                        "CreationTime": "2021-03-30T15:47:06.822Z",
                        "Primary": true
                    }
                ]
            }
        }
    ],
    "UnsuccessfulList": [
        {
            "GetSessionScreenshotRequestData": {
                "SessionId": "sessionId2"
            },
            "FailureReason": "Dcv session not found."
        }
    ]
}
```
