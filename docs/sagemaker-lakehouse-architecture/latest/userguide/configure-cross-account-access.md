

# Tutorial: configure cross-account access for Redshift federated catalog table
<a name="configure-cross-account-access"></a>

This tutorial provides step-by-step instructions on how to configure cross account sharing of Redshift federated catalog tables using Lake Formation permissions. For more information, see [Sharing a data lake using Lake Formation fine-grained access control](https://docs.aws.amazon.com/lake-formation/latest/dg/share-dl-fgac-tutorial.html).

## Prerequisites
<a name="configure-cross-account-prerequisites"></a>

Before proceeding, ensure you have the following prerequisites:
+ Two accounts; account A as the sharing account, account B as the recipient account. 
+ Two AWS accounts with Lake Formation [cross-account sharing version 4](https://docs.aws.amazon.com/lake-formation/latest/dg/optimize-ram.html) and Lake Formation administrator configured. For more information, see [Data lake administrator permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/permissions-reference.html#persona-dl-admin) and initial [setup of Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/initial-lf-config.html).
+ Permissions for [managing Amazon Redshift namespaces in the Data Catalog](https://docs.aws.amazon.com/lake-formation/latest/dg/redshift-ns-prereqs.html) granted to the Lake Formation administrator role on both accounts. 
+ An Amazon S3 bucket in the account A account to host the sample Iceberg table data.
+ An IAM role in the account A account to register your Amazon S3 location for Iceberg table with Lake Formation. For more information, see [Registering an Amazon S3 location](https://docs.aws.amazon.com/lake-formation/latest/dg/register-location.html) and [Requirements for roles used to register locations](https://docs.aws.amazon.com/lake-formation/latest/dg/registration-role.html).
+ An Redshift Serverless namespace in the account A account. Follow the instructions in [Creating a data warehouse with Amazon Redshift Serverless](https://docs.aws.amazon.com/redshift/latest/gsg/new-user-serverless.html#serverless-console-resource-creation) to launch a serverless namespace with default settings.
+ An IAM role, `Glue-execution-role`, in account B with appropriate policies.

### Required IAM policies for `Glue-execution-role`
<a name="configure-cross-account-iam-policies"></a>

The `Glue-execution-role` in account B requires the following AWS managed policies:
+ `AWSGlueServiceRole`
+ `AmazonRedshiftDataFullAccess`

Additionally, create an inline policy with the following permissions:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "LFandRSserverlessAccess",
            "Effect": "Allow",
            "Action": [
                "lakeformation:GetDataAccess",
                "redshift-serverless:GetCredentials"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "glue.amazonaws.com"
                }
            }
        }
    ]
}
```

------

Add the following trust policy to `Glue-execution-role`:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "glue.amazonaws.com"
                ]
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

------