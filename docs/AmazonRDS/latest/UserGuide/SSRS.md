# Using SSRS Email to send reports

SSRS includes the SSRS Email extension, which you can use to send reports to
users.

To configure SSRS Email, use the `SSRS` option settings. For more
information, see [Adding the SSRS option to your option group](SSRS.md#SSRS.Add "SSRS.md#SSRS.Add").

After configuring SSRS Email, you can subscribe to reports on the report server. For more information, see [Email
delivery in Reporting Services](https://docs.microsoft.com/en-us/sql/reporting-services/subscriptions/e-mail-delivery-in-reporting-services "https://docs.microsoft.com/en-us/sql/reporting-services/subscriptions/e-mail-delivery-in-reporting-services") in the Microsoft documentation.

Integration with AWS Secrets Manager is required for SSRS Email to function on RDS. To integrate with Secrets Manager, you create a secret.

###### Note

If you change the secret later, you also have to update the `SSRS` option in the option group.

###### To create a secret for SSRS Email

1. Follow the steps in [Create a
   secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the _AWS Secrets Manager User Guide_.
   1. For **Select secret type**, choose **Other type of secrets**.
   2. For **Key/value pairs**, enter the following:
      - `SMTP_USERNAME` – Enter a user with permission to send mail from the SMTP
        server.
      - `SMTP_PASSWORD` – Enter a password for the SMTP user.

   3. For **Encryption key**, don't use the default AWS KMS key. Use your own existing key,
      or create a new one.

   The KMS key policy must allow the `kms:Decrypt` action, for example:

   ```
   {
       "Sid": "Allow use of the key",
       "Effect": "Allow",
       "Principal": {
           "Service": [
               "rds.amazonaws.com"
           ]
       },
       "Action": [
           "kms:Decrypt"
       ],
       "Resource": "*"
   }
   ```

2. Follow the steps in [Attach a permissions policy to a
   secret](../../../secretsmanager/latest/userguide/auth-and-access_resource-policies.md "../../../secretsmanager/latest/userguide/auth-and-access_resource-policies.md") in the _AWS Secrets Manager User Guide_. The permissions policy gives the
   `secretsmanager:GetSecretValue` action to the `rds.amazonaws.com` service principal.

We recommend that you use the `aws:sourceAccount` and `aws:sourceArn` conditions in the policy
to avoid the _confused deputy_ problem. Use your AWS account for `aws:sourceAccount` and
the option group ARN for `aws:sourceArn`. For more information, see [Preventing cross-service confused deputy problems](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md").

The following example shows a permissions policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement" : [ {
 "Effect" : "Allow",
 "Principal" : {
 "Service" : "rds.amazonaws.com"
 },
 "Action" : "secretsmanager:GetSecretValue",
 "Resource" : "*",
 "Condition" : {
 "StringEquals" : {
 "aws:sourceAccount" : "`123456789012`"
 },
 "ArnLike" : {
 "aws:sourceArn" : "arn:aws:rds:us-west-2:`123456789012`:og:`ssrs-se-2017`"
 }
 }
 } ]
}`

```

For more examples, see [Permissions policy examples for AWS Secrets Manager](../../../secretsmanager/latest/userguide/auth-and-access_examples.md "../../../secretsmanager/latest/userguide/auth-and-access_examples.md") in the _AWS Secrets Manager User
Guide_.
