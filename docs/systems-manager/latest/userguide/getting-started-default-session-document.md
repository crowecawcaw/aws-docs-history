• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Start a default shell

session by specifying the default session document in IAM policies

When you configure Session Manager for your AWS account or when you change session
preferences in the Systems Manager console, the system creates an SSM session document
called `SSM-SessionManagerRunShell`. This is the default
session document. Session Manager uses this document to store your session preferences,
which include information like the following:

- A location where you want to save session data, such an Amazon Simple Storage Service
  (Amazon S3) bucket or a Amazon CloudWatch Logs log group.
- An AWS Key Management Service (AWS KMS) key ID for encrypting session data.
- Whether Run As support is allowed for your sessions.
  Here is an example of the information contained in the
  `SSM-SessionManagerRunShell` session preferences
  document.

```
{
  "schemaVersion": "1.0",
  "description": "Document to hold regional settings for Session Manager",
  "sessionType": "Standard_Stream",
  "inputs": {
    "s3BucketName": "amzn-s3-demo-bucket",
    "s3KeyPrefix": "MyS3Prefix",
    "s3EncryptionEnabled": true,
    "cloudWatchLogGroupName": "MyCWLogGroup",
    "cloudWatchEncryptionEnabled": false,
    "kmsKeyId": "1a2b3c4d",
    "runAsEnabled": true,
    "runAsDefaultUser": "RunAsUser"
  }
}
```

By default, Session Manager uses the default session document when a user starts a
session from the AWS Management Console. This applies to either Fleet Manager or Session Manager in the
Systems Manager console, or EC2 Connect in the Amazon EC2 console. Session Manager also uses the
default session document when a user starts a session by using an AWS CLI command
like the following example:

```
aws ssm start-session \
    --target i-02573cafcfEXAMPLE
```

To start a default shell session, you must specify the default session
document in the IAM policy, as shown in the following example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EnableSSMSession",
 "Effect": "Allow",
 "Action": [
 "ssm:StartSession"
 ],
 "Resource": [
 "arn:aws:ec2:`us-east-1`:`111122223333`:instance/`instance-id`",
 "arn:aws:ssm:`us-east-1`:`111122223333`:document/SSM-SessionManagerRunShell"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssmmessages:OpenDataChannel"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```
