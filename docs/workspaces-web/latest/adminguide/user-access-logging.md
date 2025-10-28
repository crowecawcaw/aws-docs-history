# Setting up User Access logging for Amazon WorkSpaces Secure Browser

To activate user access logging in the WorkSpaces Secure Browser console, under **User access
logging**, select the **Kinesis Stream ID** that you want to use to
receive data. The data recorded will be delivered directly to that stream.

For more information about how to create an Amazon Kinesis Data Stream, see [What Is Amazon Kinesis Data
Streams?](../../../streams/latest/dev/introduction.md "../../../streams/latest/dev/introduction.md")

In order to receive logs from WorkSpaces Secure Browser, you must have an Amazon Kinesis Data Stream that starts
with "amazon-workspaces-web-\*". Your Amazon Kinesis data stream must either have server-side
encryption turned off, or must use AWS managed keys for server-side encryption.

For more information about setting server-side encryption in Amazon Kinesis, see [How Do I Get
Started with Server-Side Encryption?](../../../streams/latest/dev/getting-started-with-sse.md "../../../streams/latest/dev/getting-started-with-sse.md").
