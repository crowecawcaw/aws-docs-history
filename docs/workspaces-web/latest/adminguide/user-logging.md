# Setting up user activity logging in Amazon WorkSpaces Secure Browser

WorkSpaces Secure Browser offers two options for logging user activity and security-related events:

- Session Logger captures a wide range of session events. These logs are delivered to an
  Amazon S3 bucket in your account, enabling easy integration with your preferred SIEM
  platform.
- User Access Logging captures the most critical session events. These logs are streamed to
  an Amazon Kinesis stream for real-time processing and analysis.
  Both logging options are configured at the portal level. You must set up each option
  individually for every portal where you want logging to be active. You can enable either option
  or both, depending on your requirements for each portal.

You are responsible for complying with any requirements that apply to the logging or
monitoring of user activity when using this feature, including logging or monitoring of employee
activity.

###### Topics

- [Setting up Session Logger for Amazon WorkSpaces Secure Browser](session-logger.md "session-logger.md")
- [Setting up User Access logging for Amazon WorkSpaces Secure Browser](user-access-logging.md "user-access-logging.md")
