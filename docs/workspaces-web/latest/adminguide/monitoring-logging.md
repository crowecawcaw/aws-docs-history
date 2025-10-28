# User activity logging in Amazon WorkSpaces Secure Browser

Amazon WorkSpaces Secure Browser enables customers to log session events related to user activities in the
Secure browser sessions.

WorkSpaces Secure Browser offers two options for logging user activity and security-related events:

- Session Logger captures a wide range of session events. These logs are delivered to an
  Amazon S3 bucket in your account, enabling easy integration with your preferred SIEM
  platform.
- User Access Logging captures the most critical session events. These logs are streamed
  to an Amazon Kinesis stream for real-time processing and analysis.
  For more information about how to set up these options, see [Setting up Session Logger for Amazon WorkSpaces Secure Browser](session-logger.md "session-logger.md") and [Setting up User Access logging for Amazon WorkSpaces Secure Browser](user-access-logging.md "user-access-logging.md").

###### Topics

- [Session events in Session Logger for Amazon WorkSpaces Secure Browser](session-events-session-logger.md "session-events-session-logger.md")
- [Session events in User Access logging for Amazon WorkSpaces Secure Browser](session-events-logging.md "session-events-logging.md")
