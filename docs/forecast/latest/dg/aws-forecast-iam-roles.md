Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# Set Up Permissions for Amazon Forecast

Amazon Forecast uses Amazon Simple Storage Service (Amazon S3) to store the target time-series data that are used to
train predictors that can generate forecasts. To access Amazon S3 on your behalf, Amazon Forecast
needs your permission.

To grant Amazon Forecast permission to use Amazon S3 on your behalf, you must have an AWS Identity and Access Management
(IAM) role and IAM policy in your account. The IAM policy specifies the required
permissions, and must be attached to the IAM role.

To create the IAM role and policy and to attach the policy to the role, you can use the
IAM console or the AWS Command Line Interface (AWS CLI).

###### Note

Forecast does not communicate with Amazon Virtual Private Cloud and is unable to support the Amazon S3 VPCE
gateway. Using S3 buckets that only allow VPC access will result in an
`AccessDenied` error.

###### Topics

- [Create an IAM Role for
  Amazon Forecast (IAM Console)](#aws-forecast-create-iam-role-with-console "#aws-forecast-create-iam-role-with-console")
- [Create an IAM Role for Amazon Forecast (AWS CLI)](#aws-forecast-create-iam-role-with-cli "#aws-forecast-create-iam-role-with-cli")
- [Cross-service confused deputy
  prevention](#aws-forecast-confused-deputy "#aws-forecast-confused-deputy")

## Create an IAM Role for

Amazon Forecast (IAM Console)

You can use the AWS IAM console to do the following:

- Create an IAM role with Amazon Forecast as a trusted entity
- Create an IAM policy with permissions that allows Amazon Forecast to show,
  read, and write data in an Amazon S3 bucket
- Attach the IAM policy to the IAM role

###### To create an IAM role and policy that allows Amazon Forecast to access Amazon S3

(IAM console)

1. Sign in to the IAM console ([https://console.aws.amazon.com/iam](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam")).
2. Choose **Policies** and do the following to create the
   required policy:
   1. Click **Create policy**.
   2. On the **Create policy** page, in the policy editor,
      choose the **JSON** tab.
   3. Copy the following policy and replace the text in the editor by
      pasting the this policy over it. Be sure to replace
      `bucket-name` with the
      name of your S3 bucket, then choose **Review
      policy**.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement":[
    {
    "Effect":"Allow",
    "Action":[
    "s3:Get*",
    "s3:List*",
    "s3:PutObject"
    ],
    "Resource":[
    "arn:aws:s3:::`bucket-name`",
    "arn:aws:s3:::`bucket-name`/*"
    ]
    }
    ]
   }`

   ```

   Click **Next: Tags** 4. Optionally, you can assign tags to this policy. Click **Next: Review**. 5. In **Review policy**, for **Name**,
   enter a name for the policy. For example,
   `AWSS3BucketAccess`. Optionally, provide a description for
   this policy, then choose **Create policy**.

3. In the navigation pane, choose **Roles**. Then do the
   following to create the IAM role:
   1. Choose **Create role**.
   2. For **Trusted entity type**, choose **AWS service**.

   For **Use case**, select **Forecast** from either the
   **Common use cases** section or the **Use cases for other AWS services** drop-down list. If you cannot find **Forecast**, choose
   **EC2**.

   Click **Next**. 3. In the **Add permissions** section, click **Next**. 4. In the **Name, review, and create** section, for **Role
   name**, enter a name for the role (for example, `ForecastRole`). Update the
   description for the role in **Role description**, then choose **Create
   role**. 5. You should now be back at the **Roles** page. Choose the new role to open
   the role's details page. 6. In the **Summary**, copy the **Role
   ARN** value and save it. You need it to import a dataset
   into Amazon Forecast. 7. If you didn't choose **Amazon Forecast** as the
   service that will use this role, choose **Trust
   relationships**, and then choose **Edit trust
   relationship** to update the trust policy as follows. 8. **[OPTIONAL]** When using a KMS key to
   enable encryption, attach the KMS key and ARN:

## Create an IAM Role for Amazon Forecast (AWS CLI)

You can use the AWS CLI to do the following:

- Create an IAM role with Amazon Forecast as a trusted entity
- Create an IAM policy with permissions that allows Amazon Forecast to show,
  read, and write data in an Amazon S3 bucket
- Attach the IAM policy to the IAM role

###### To create an IAM role and policy that allows Amazon Forecast to access Amazon S3

(AWS CLI)

1. Create an IAM role with Amazon Forecast as a trusted entity that can assume
   the role for you:

```
aws iam create-role \
 --role-name `ForecastRole` \
 --assume-role-policy-document '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "forecast.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "`account-id`"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:forecast:`region`:`account-id`:*"
        }
      }
    }
  ]
}'
```

This command assumes that the default AWS configuration profile is targeted
for an AWS Region supported by Amazon Forecast. If you have configured another
profile (for example, `aws-forecast`) to target an AWS Region that is
not supported by Amazon Forecast, you must explicitly specify that configuration
by including the `profile` parameter in the command, for example,
`--profile aws-forecast`. For more information about setting up
an AWS CLI configuration profile, see the AWS CLI [configure](../../../cli/latest/reference/configure.md "../../../cli/latest/reference/configure.md") command.

If the command successfully creates the role, it returns it as output, which
should look similar to the following:

```
{
    "Role": {
        "Path": "/",
        "RoleName": "ForecastRole",
        "RoleId": `your-role-ID`,
        "Arn": "arn:aws:iam::`your-acct-ID`:role/ForecastRole",
        "CreateDate": "`creation-date`",
        "AssumeRolePolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "",
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "forecast.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole",
                    "Condition": {
                        "StringEquals": {
                            "aws:SourceAccount": "`your-acct-ID`"
                        },
                        "ArnLike": {
                            "aws:SourceArn": "arn:aws:forecast:`region`:`your-acct-ID`:*"
                        }
                    }
                }
            ]
        }
    }
}
```

Record the role's ARN. You need it when you import a dataset to train an
Amazon Forecast predictor. 2. Create an IAM policy with permissions to list, read, and write data in Amazon S3,
and attach it to the IAM role that you created in Step 1:

```
aws iam put-role-policy \
  --role-name `ForecastRole` \
  --policy-name `ForecastBucketAccessPolicy` \
  --policy-document '{
   "Version": "2012-10-17",
   "Statement":[
      {
         "Effect":"Allow",
         "Action":[
            "s3:Get*",
            "s3:List*",
            "s3:PutObject"
         ],
         "Resource":[
            "arn:aws:s3:::`bucket-name`",
            "arn:aws:s3:::`bucket-name`/*"
         ]
      }
   ]
}'
```

3. **[OPTIONAL]** When using a KMS key to enable
   encryption, attach the KMS key and ARN:

```
aws iam put-role-policy \
  --role-name `ForecastRole` \
  --policy-name `ForecastBucketAccessPolicy` \
  --policy-document '{
   "Version": "2012-10-17",
   "Statement":[
      {
         "Effect":"Allow",
         "Action":[
            "s3:Get*",
            "s3:List*",
            "s3:PutObject"
         ],
         "Resource":[
            "arn:aws:s3:::`bucket-name`",
            "arn:aws:s3:::`bucket-name`/*"
         ]
      }
   ]
}'aws iam put-role-policy \
  --role-name `ForecastRole` \
  --policy-name `ForecastKMSAccessPolicy` \
  --policy-document ‘{
   "Version": "2012-10-17",
   "Statement":[
      {
         "Effect":"Allow",
         "Action":[
        "kms:DescribeKey",
        "kms:CreateGrant",
        "kms:RetireGrant"
         ],
         "Resource":[
         "arn:aws:kms:`region`:`account-id`:key/`KMS-key-id`"
         ]
      }
   ]
}’
```

## Cross-service confused deputy

prevention

The confused deputy problem is a security issue where an entity that doesn’t have
permission to perform an action can coerce a more-privileged entity to perform the
action. In AWS, cross-service impersonation can result in the confused deputy problem.
Cross-service impersonation can occur when one service (the calling service) calls
another service (the called service). The calling service can be manipulated to use its
permissions to act on another customer’s resources in a way it should not otherwise have
permission to access. To prevent this, AWS provides tools that help you protect your
data for all services with service principals that have been given access to resources
in your account.

We recommend using the `aws:SourceArn` and `aws:SourceAccount`
global condition context keys in resource policies to limit the permissions that
Identity and Access Management (IAM) gives Amazon Forecast access to your resources. If you
use both global condition context keys, the `aws:SourceAccount` value and the
account in the `aws:SourceArn` value must use the same account id when used
in the same policy statement.
