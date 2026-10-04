

Amazon WorkSpaces Secure Browser will no longer be open to new customers starting October 29, 2026. If you would like to use Amazon WorkSpaces Secure Browser, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon WorkSpaces Secure Browser availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html). 

# Session events in User Access logging for Amazon WorkSpaces Secure Browser
<a name="session-events-logging"></a>

The following session events are available for User Acess logging:
+ **Validation**: The event is sucessfully put to the Kinesis data stream.
+ **StartSession**: The user has started a session and is connected to the secure browser session.
+ **VisitPage**: The user is visiting a page in the session.
+ **EndSession**: The user has terminated the session.

URL navigation logs are recorded from the browser history. URLs not recorded in browser history (either visited in incognito mode or deleted from browser history) are not recorded in logs. It's up to customers to determine whether to turn off incognito mode or history deletion with their browser policy.

Below is an example of each available event. The following fields are always included for each event:
+ **timestamp** is included as epoch time in milliseconds.
+ **eventType** is included as a string.
+ **details** is included as another json object.
+ **portalArn** and **userName** are included for every event except for **Validation**.

```
{
  "timestamp": "1665430373875",
  "eventType": "Validation",
  "details": {
    "permission": "Kinesis:PutRecord",
    "userArn": "{{userArn}}",
    "operation": "AssociateUserAccessLoggingSettings",
    "userAccessLoggingSettingsArn": "{{userAccessLoggingSettingsArn}}"
  }
}

{
  "timestamp": "1665179071723",
  "eventType": "StartSession",
  "details": {},
  "portalArn": "{{portalArn}}",
  "userName": "{{userName}}"
}

{
  "timestamp": "1665179084578",
  "eventType": "VisitPage",
  "details": {
    "title": "Amazon",
    "url": "https://www.amazon.com/"
  },
  "portalArn": "{{portalArn}}",
  "userName": "{{userName}}"
}

{
  "timestamp": "1665179155953",
  "eventType": "EndSession",
  "details": {},
  "portalArn": "{{portalArn}}",
  "userName": "{{userName}}"
}
```