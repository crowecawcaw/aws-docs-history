# Managing access to data sources

CloudWatch uses CloudFormation to create the required resources in your account. We recommend that you
use the `cloudformation:TemplateUrl` condition to control access to CloudFormation templates when
you grant `CreateStack` permissions to IAM users.

###### Warning

Any user that you grant data source invoke permission to can query metrics from that
data source even if that user does not have direct IAM permissions to the data source.
For example, if you grant `lambda:InvokeFunction` permissions on a Amazon Managed Service for Prometheus data source Lambda function
to a user, that user will be able to query metrics from the corresponding Amazon Managed Service for Prometheus workspace even if you didn't
grant them direct IAM access to that workspace.

You can find template URLs for data sources on the **Create stack**
page in the CloudWatch Settings Console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCloudFormationCreateStack",
 "Effect": "Allow",
 "Action": [
 "cloudformation:CreateStack"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "cloudformation:TemplateUrl": [
 "https://s3.`us-east-1`.amazonaws.com/`amzn-s3-demo-bucket`/template.json"
 ]
 }
 }
 }
 ]
}`

```

For more information about controlling CloudFormation access, see [Controlling access with AWS Identity and Access Management](../../../AWSCloudFormation/latest/UserGuide/using-iam-template.md "../../../AWSCloudFormation/latest/UserGuide/using-iam-template.md")
