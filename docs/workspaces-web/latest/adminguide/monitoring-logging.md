

Amazon WorkSpaces Secure Browser will no longer be open to new customers starting October 29, 2026. If you would like to use Amazon WorkSpaces Secure Browser, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon WorkSpaces Secure Browser availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html). 

# User activity logging in Amazon WorkSpaces Secure Browser
<a name="monitoring-logging"></a>

Amazon WorkSpaces Secure Browser enables customers to log session events related to user activities in the Secure browser sessions.

WorkSpaces Secure Browser offers two options for logging user activity and security-related events:
+ Session Logger captures a wide range of session events. These logs are delivered to an Amazon S3 bucket in your account, enabling easy integration with your preferred SIEM platform.
+ User Access Logging captures the most critical session events. These logs are streamed to an Amazon Kinesis stream for real-time processing and analysis.

For more information about how to set up these options, see [Setting up Session Logger for Amazon WorkSpaces Secure Browser](session-logger.md) and [Setting up User Access logging for Amazon WorkSpaces Secure Browser](user-access-logging.md).

**Topics**
+ [Session events in Session Logger for Amazon WorkSpaces Secure Browser](session-events-session-logger.md)
+ [Session events in User Access logging for Amazon WorkSpaces Secure Browser](session-events-logging.md)