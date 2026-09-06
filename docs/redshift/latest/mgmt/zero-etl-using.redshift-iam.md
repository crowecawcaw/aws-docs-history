

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Configure authorization for your Amazon Redshift data warehouse
<a name="zero-etl-using.redshift-iam"></a>

To replicate data from your integration source into your Amazon Redshift data warehouse, you must initially add the following two entities:
+ *Authorized principal* – identifies the user or role that can create zero-ETL integrations into the data warehouse.
+ *Authorized integration source* – identifies the source database that can update the data warehouse.

You can configure authorized principals and authorized integration sources from the **Resource Policy** tab on the Amazon Redshift console or using the Amazon Redshift `PutResourcePolicy` API operation.

## Add authorized principals
<a name="zero-etl-using.redshift-iam-ap"></a>

To create a zero-ETL integration into your Redshift Serverless workgroup or provisioned cluster, authorize access to the associated namespace or provisioned cluster. 

You can skip this step if both of the following conditions are true:
+ The AWS account that owns the Redshift Serverless workgroup or provisioned cluster also owns the source database.
+ That principal is associated with an identity-based IAM policy with permissions to create zero-ETL integrations into this Redshift Serverless namespace or provisioned cluster.

### Add authorized principals to an Amazon Redshift Serverless namespace
<a name="iam-ap-serverless"></a>

1. In the Amazon Redshift console, in the left navigation pane, choose **Redshift Serverless**.

1. Choose **Namespace configuration**, then choose your namespace, and go to the **Resource Policy** tab.

1. Choose **Add authorized principals**.

1. For each authorized principal that you want to add, enter into the namespace either the ARN of the AWS user or role, or the ID of the AWS account that you want to grant access to create zero-ETL integrations. An account ID is stored as an ARN.

1. Choose **Save changes**.

### Add authorized principals to an Amazon Redshift provisioned cluster
<a name="iam-ap-cluster"></a>

1. In the Amazon Redshift console, in the left navigation pane, choose **Provisioned clusters dashboard**.

1. Choose **Clusters**, then choose the cluster, and go to the **Resource Policy** tab.

1. Choose **Add authorized principals**.

1. For each authorized principal that you want to add, enter into the cluster either the ARN of the AWS user or role, or the ID of the AWS account that you want to grant access to create zero-ETL integrations. An account ID is stored as an ARN.

1. Choose **Save changes**.

## Add authorized integration sources
<a name="zero-etl-using.redshift-iam-air"></a>

To allow your source to update your Amazon Redshift data warehouse, you must add it as an authorized integration source to the namespace.

### Add an authorized integration source to an Amazon Redshift Serverless namespace
<a name="iam-air-serverless"></a>

1. In the Amazon Redshift console, go to **Serverless dashboard**. 

1. Choose the name of the namespace.

1. Go to the **Resource Policy** tab.

1. Choose **Add authorized integration source**.

1. Specify the ARN of the source for the zero-ETL integration.

**Note**  
Removing an authorized integration source stops data from replicating into the namespace. This action deactivates all zero-ETL integrations from that source into this namespace.

### Add an authorized integration source to an Amazon Redshift provisioned cluster
<a name="iam-air-cluster"></a>

1. In the Amazon Redshift console, go to **Provisioned clusters dashboard**. 

1. Choose the name of the provisioned cluster.

1. Go to the **Resource Policy** tab.

1. Choose **Add authorized integration source**.

1. Specify the ARN of the source that's the data source for the zero-ETL integration.

**Note**  
Removing an authorized integration source stops data from replicating into the provisioned cluster. This action deactivates all zero-ETL integrations from that source into this Amazon Redshift provisioned cluster.

## Configure authorization using the Amazon Redshift API
<a name="zero-etl-using.resource-policies"></a>

You can use the Amazon Redshift API operations to configure resource policies that work with zero-ETL integrations.

To control the source that can create an inbound integration into the namespace, create a resource policy and attach it to the namespace. With the resource policy, you can specify the source that has access to the integration. The resource policy is attached to the namespace of your target data warehouse to allow the source to create an inbound integration to replicate live data from the source into Amazon Redshift.

The following is a sample resource policy.

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "redshift.amazonaws.com"
      },
      "Action": "redshift:AuthorizeInboundIntegration",
      "Resource": "arn:aws:redshift-serverless:us-east-1:123456789012:namespace/cc4ffe56-ad2c-4fd1-a5a2-f29124a56433",
      "Condition": {
        "StringEquals": {
          "aws:SourceArn": "arn:aws:rds:us-east-1:111122223333:cluster:foo"
        }
      }
    },
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:root"
      },
      "Action": "redshift:CreateInboundIntegration",
      "Resource": "arn:aws:redshift-serverless:us-east-1:123456789012:namespace/cc4ffe56-ad2c-4fd1-a5a2-f29124a56433"
    }
  ]
}
```

The following summarizes the Amazon Redshift API operations applicable to configuring resource policies for integrations:
+ Use the [PutResourcePolicy](https://docs.aws.amazon.com/redshift/latest/APIReference/API_PutResourcePolicy.html) API operation to persist the resource policy. When you provide another resource policy, the previous resource policy on the resource is replaced. Use the previous example resource policy, which grants permissions for the following actions:
  + `CreateInboundIntegration` – Allows the source principal to create an inbound integration for data to be replicated from the source into the target data warehouse.
  + `AuthorizeInboundIntegration` – Allows Amazon Redshift to continuously validate that the target data warehouse can receive data replicated from the source ARN.
+ Use the [GetResourcePolicy](https://docs.aws.amazon.com/redshift/latest/APIReference/API_GetResourcePolicy.html) API operation is to view existing resource policies.
+ Use the [DeleteResourcePolicy](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DeleteResourcePolicy.html) API operation to remove a resource policy from the resource.

To update a resource policy, you can also use the [put-resource-policy](https://docs.aws.amazon.com/cli/latest/reference/redshift/put-resource-policy.html) AWS CLI command. For example, to put a resource policy on your Amazon Redshift namespace ARN for a DynamoDB source, run a AWS CLI command similar to the following.

```
aws redshift put-resource-policy \
--policy file://rs-rp.json \
--resource-arn "arn:aws:redshift-serverless:us-east-1:123456789012:namespace/cc4ffe56-ad2c-4fd1-a5a2-f29124a56433"
```

Where `rs-rp.json` contains:

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
                "Service": "redshift.amazonaws.com"
            },
            "Action": "redshift:AuthorizeInboundIntegration",
            "Resource": "arn:aws:redshift-serverless:us-east-1:123456789012:namespace/cc4ffe56-ad2c-4fd1-a5a2-f29124a56433",
            "Condition": {
                "StringEquals": {
                    "aws:SourceArn": "arn:aws:dynamodb:us-east-1:123456789012:table/test_ddb"
                }
            }
        },
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::123456789012:root"
            },
            "Action": "redshift:CreateInboundIntegration",
            "Resource": "arn:aws:redshift-serverless:us-east-1:123456789012:namespace/cc4ffe56-ad2c-4fd1-a5a2-f29124a56433"
        }
    ]
}
```

------