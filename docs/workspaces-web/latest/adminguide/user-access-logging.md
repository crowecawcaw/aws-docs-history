

Amazon WorkSpaces Secure Browser will no longer be open to new customers starting October 29, 2026. If you would like to use Amazon WorkSpaces Secure Browser, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon WorkSpaces Secure Browser availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html). 

# Setting up User Access logging for Amazon WorkSpaces Secure Browser
<a name="user-access-logging"></a>

To activate user access logging in the WorkSpaces Secure Browser console, under **User access logging**, select the **Kinesis Stream ID** that you want to use to receive data. The data recorded will be delivered directly to that stream.

For more information about how to create an Amazon Kinesis Data Stream, see [What Is Amazon Kinesis Data Streams?](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)

In order to receive logs from WorkSpaces Secure Browser, you must have an Amazon Kinesis Data Stream that starts with "amazon-workspaces-web-\*". Your Amazon Kinesis data stream must either have server-side encryption turned off, or must use AWS managed keys for server-side encryption.

For more information about setting server-side encryption in Amazon Kinesis, see [How Do I Get Started with Server-Side Encryption?](https://docs.aws.amazon.com/streams/latest/dev/getting-started-with-sse.html).