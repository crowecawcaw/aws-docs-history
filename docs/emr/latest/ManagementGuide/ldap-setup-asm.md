# Add AWS Secrets Manager permissions to the Amazon EMR instance

role

Amazon EMR uses an IAM service role to perform actions on your behalf to provision and
manage clusters. The service role for cluster EC2 instances, also called
_the EC2 instance profile for Amazon EMR_, is a special type of
service role that Amazon EMR assigns to every EC2 instance in a cluster at launch.

To define permissions for an EMR cluster to interact with Amazon S3 data and other
AWS services, define a custom Amazon EC2 instance profile instead of the
`EMR_EC2_DefaultRole` when you launch your cluster. For more
information, see [Service role for cluster EC2 instances (EC2
instance profile)](emr-iam-role-for-ec2.md "emr-iam-role-for-ec2.md") and [Customize IAM roles with Amazon EMR](emr-iam-roles-custom.md "emr-iam-roles-custom.md").

Add the following statements to the default EC2 instance profile to allow Amazon EMR to
tag sessions and access the AWS Secrets Manager that stores LDAP certificates.

```
    {
      "Sid": "AllowAssumeOfRolesAndTagging",
      "Effect": "Allow",
      "Action": ["sts:TagSession", "sts:AssumeRole"],
      "Resource": [
        "arn:aws:iam::`111122223333`:role/`LDAP_DATA_ACCESS_ROLE_NAME`",
        "arn:aws:iam::`111122223333`:role/`LDAP_USER_ACCESS_ROLE_NAME`"
      ]
    },
    {
        "Sid": "AllowSecretsRetrieval",
        "Effect": "Allow",
        "Action": "secretsmanager:GetSecretValue",
        "Resource": [
            "arn:aws:secretsmanager:`us-east-1`:`111122223333`:secret:`LDAP_SECRET_NAME`*",
            "arn:aws:secretsmanager:`us-east-1`:`111122223333`:secret:`ADMIN_LDAP_SECRET_NAME`*"
        ]
    }
```

###### Note

Your cluster requests will fail if you forget the wildcard `*`
character at the end of the secret name when you set Secrets Manager permissions. The
wildcard represents the secret versions.

You should aslo limit the scope of the AWS Secrets Manager policy to only the
certificates that your cluster needs to provision instances.
