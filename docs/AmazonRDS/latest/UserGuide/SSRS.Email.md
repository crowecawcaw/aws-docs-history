

# Using reporting services email to send reports
<a name="SSRS.Email"></a>

SSRS and PBIRS include an email extension that you can use to send reports to users.

To configure email for SSRS, use the `SSRS` option settings. To configure email for PBIRS, use the `PBIRS` option settings. For more information, see [Adding the SSRS or PBIRS option to your option group](SSRS.Enabling.md#SSRS.Add).

After configuring email, you can subscribe to reports on the report server. For more information, see [Email delivery in Reporting Services](https://docs.microsoft.com/en-us/sql/reporting-services/subscriptions/e-mail-delivery-in-reporting-services) in the Microsoft documentation.

Integration with AWS Secrets Manager is required for reporting services email to function on RDS. To integrate with Secrets Manager, you create a secret.

**Note**  
If you change the secret later, you must also update the `SSRS` or `PBIRS` option in the option group.

**To create a secret for reporting services email**

1. Follow the steps in [Create a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) in the *AWS Secrets Manager User Guide*.

   1. For **Select secret type**, choose **Other type of secrets**.

   1. For **Key/value pairs**, enter the following:
      + **SMTP\_USERNAME** – Enter a user with permission to send mail from the SMTP server.
      + **SMTP\_PASSWORD** – Enter a password for the SMTP user.

   1. For **Encryption key**, don't use the default AWS KMS key. Use your own existing key, or create a new one.

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

1. Follow the steps in [Attach a permissions policy to a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-policies.html) in the *AWS Secrets Manager User Guide*. The permissions policy gives the `secretsmanager:GetSecretValue` action to the `rds.amazonaws.com` service principal.

   We recommend that you use the `aws:sourceAccount` and `aws:sourceArn` conditions in the policy to avoid the *confused deputy* problem. Use your AWS account for `aws:sourceAccount` and the option group ARN for `aws:sourceArn`. For more information, see [Preventing cross-service confused deputy problems](cross-service-confused-deputy-prevention.md).

   The following example shows a permissions policy.

------
#### [ JSON ]

****  

   ```
   {
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
           "aws:sourceAccount" : "{{123456789012}}"
         },
         "ArnLike" : {
           "aws:sourceArn" : "arn:aws:rds:us-west-2:{{123456789012}}:og:{{ssrs-se-2017}}"
         }
       }
     } ]
   }
   ```

------

   For more examples, see [Permissions policy examples for AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html) in the *AWS Secrets Manager User Guide*.