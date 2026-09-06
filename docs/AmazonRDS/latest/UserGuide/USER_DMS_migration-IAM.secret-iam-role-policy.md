

# Creating a secret access policy and role
<a name="USER_DMS_migration-IAM.secret-iam-role-policy"></a>

Follow the procedures below to create your secret access policy and role which allow DMS to access the user credentials for your source and target databases.

**To create the secret access policy and role, which allows Amazon RDS to access AWS Secrets Manager to access your appropriate secret**

1. Sign in to the AWS Management Console and open the AWS Identity and Access Management (IAM) console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. Choose **Policies**, then choose **Create policy**.

1. Choose **JSON** and enter the following policy to enable access to and decryption of your secret.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": "secretsmanager:GetSecretValue",
               "Resource": "arn:aws:secretsmanager:{{us-east-1}}:{{111122223333}}:secret:SecretName-ABCDEF"
           },
           {
               "Effect": "Allow",
               "Action": [
                   "kms:Decrypt",
                   "kms:DescribeKey"
               ],
               "Resource": "arn:aws:kms:{{us-east-1}}:111122223333:key/{{1234abcd-12ab-34cd-56ef-1234567890ab}}"
           }
       ]
   }
   ```

------

   Here, `{{secret_arn}}` is the ARN of your secret, which you can get from either `SecretsManagerSecretId` as appropriate, and `{{kms_key_arn}}` is the ARN of the AWS KMS key that you are using to encrypt your secret, as in the following example.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": "secretsmanager:GetSecretValue",
               "Resource": "arn:aws:secretsmanager:us-east-2:123456789012:secret:MySQLTestSecret-qeHamH"
           },
           {
                "Effect": "Allow",
                "Action": [
                           "kms:Decrypt",
                           "kms:DescribeKey"
                         ],
                "Resource": "arn:aws:kms:us-east-2:123456789012:key/761138dc-0542-4e58-947f-4a3a8458d0fd"
           }
        ]
   }
   ```

------
**Note**  
If you use the default encryption key created by AWS Secrets Manager, you do not have to specify the AWS KMS permissions for `{{kms_key_arn}}`.  
If you want your policy to provide access to both secrets, simply specify an additional JSON resource object for the other {{secret\_arn}}.

1. Review and create the policy with a friendly name and optional description.

1. Choose **Roles**, then choose **Create role**.

1. Choose **AWS service** as the type of trusted entity.

1. Choose **DMS** from the list of services as the trusted service, then choose **Next: Permissions**.

1. Look up and attach the policy you created in step 4, then proceed through adding any tags and review your role. At this point, edit the trust relationships for the role to use your Amazon RDS regional service principal as the trusted entity. This principal has the following format.

   ```
   dms.{{region-name}}.amazonaws.com
   ```

   Here, {{`region-name`}} is the name of your region, such as `us-east-1`. Thus, an Amazon RDS regional service principal for this region follows.

   ```
   dms.us-east-1.amazonaws.com
   dms-data-migrations.amazonaws.com
   ```