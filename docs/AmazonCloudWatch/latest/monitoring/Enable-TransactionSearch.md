

# Enable transaction search
<a name="Enable-TransactionSearch"></a>

You can enable [Transaction Search](CloudWatch-Transaction-Search.md) through the console or by using an API. Transaction search is configured for the entire account and switches all spans ingestion through X-Ray into cost effective collection mode using [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/). By default you will also index 1% of ingested spans for free as trace summary for analysis, which is typically sufficient given you already have full end-to-end trace visibility on all ingested spans through Transaction Search.

## Prerequisites
<a name="Enable-TransactionSearch-prerequisites"></a>

 Before you can enable Transaction Search, you must create a role with the following permissions. 

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "TransactionSearchXRayPermissions",
      "Effect": "Allow",
      "Action": [
        "xray:GetTraceSegmentDestination",
        "xray:UpdateTraceSegmentDestination",
        "xray:GetIndexingRules",
        "xray:UpdateIndexingRule"
      ],
      "Resource": "*"
    },
    {
      "Sid": "TransactionSearchLogGroupPermissions",
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutRetentionPolicy"
      ],
      "Resource": [
        "arn:aws:logs:*:*:log-group:/aws/application-signals/data:*",
        "arn:aws:logs:*:*:log-group:aws/spans:*"
      ]
    },
    {
      "Sid": "TransactionSearchLogsPermissions",
      "Effect": "Allow",
      "Action": [
        "logs:PutResourcePolicy",
        "logs:DescribeResourcePolicies"
      ],
      "Resource": "*"
    },
    {
      "Sid": "TransactionSearchApplicationSignalsPermissions",
      "Effect": "Allow",
      "Action": [
        "application-signals:StartDiscovery"
      ],
      "Resource": "*"
    },
    {
      "Sid": "CloudWatchApplicationSignalsCreateServiceLinkedRolePermissions",
      "Effect": "Allow",
      "Action": "iam:CreateServiceLinkedRole",
      "Resource": "arn:aws:iam::*:role/aws-service-role/application-signals.cloudwatch.amazonaws.com/AWSServiceRoleForCloudWatchApplicationSignals",
      "Condition": {
        "StringLike": {
          "iam:AWSServiceName": "application-signals.cloudwatch.amazonaws.com"
        }
      }
    },
    {
      "Sid": "CloudWatchApplicationSignalsGetRolePermissions",
      "Effect": "Allow",
      "Action": "iam:GetRole",
      "Resource": "arn:aws:iam::*:role/aws-service-role/application-signals.cloudwatch.amazonaws.com/AWSServiceRoleForCloudWatchApplicationSignals"
    },
    {
      "Sid": "CloudWatchApplicationSignalsCloudTrailPermissions",
      "Effect": "Allow",
      "Action": [
        "cloudtrail:CreateServiceLinkedChannel"
      ],
      "Resource": "arn:aws:cloudtrail:*:*:channel/aws-service-channel/application-signals/*"
    }
  ]
}
```

------

**Note**  
If you encrypt spans with a customer managed AWS KMS key, the role also needs the `kms:DescribeKey` permission for the key. If your role uses the `CloudWatchFullAccessV2` managed policy, it already has this permission. For an example policy and the key requirements, see [Encrypting spans with a customer managed key](#Enable-TransactionSearch-kms).

**Note**  
 To use Transaction Search and other CloudWatch features, add the [CloudWatchReadOnlyAccess policy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchReadOnlyAccess.html) to your role. For information about how to create a role, see [IAM role creation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html). 

## Encrypting spans with a customer managed key
<a name="Enable-TransactionSearch-kms"></a>

By default, CloudWatch Logs encrypts the `aws/spans` log group that stores your spans. To use your own key instead, choose a customer managed AWS KMS key when you enable Transaction Search. X-Ray applies the key only when it creates the `aws/spans` log group.

The key must meet the following requirements:
+ It's a symmetric encryption key in the same account and Region as the log group. Specify the key ARN. Key IDs and alias ARNs aren't supported.
+ The key policy allows CloudWatch Logs to use the key. For more information about key policies for CloudWatch Logs, see [Encrypt log data in CloudWatch Logs using AWS KMS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html).
+ The role that enables Transaction Search has the `kms:DescribeKey` permission for the key. If the `aws/spans` log group already exists, you also need the `logs:AssociateKmsKey` permission for it.

The following example JSON policy grants the `kms:DescribeKey` permission for one key. Add it to the role that enables Transaction Search:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "TransactionSearchKmsDescribeKey",
            "Effect": "Allow",
            "Action": "kms:DescribeKey",
            "Resource": "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}"
        }
    ]
}
```

In the example, make the following replacements:
+ Replace `{{us-east-1}}` with the Region of your key.
+ Replace `{{111122223333}}` with your account ID.
+ Replace `{{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}` with the ID of your key.

If the `aws/spans` log group already exists, X-Ray doesn't apply the key. In the console, CloudWatch applies your key to the existing log group in CloudWatch Logs instead.

If you use the API or CloudFormation, a request that includes a key fails, and X-Ray makes no changes. Instead, enable Transaction Search without a key, and then associate your key with the existing log group in CloudWatch Logs. Your key encrypts only spans that CloudWatch Logs ingests after you associate it.

The key applies only to the `aws/spans` log group. To encrypt the `/aws/application-signals/data` log group, create it with your key before you enable Transaction Search.

## Enabling Transaction Search in the console
<a name="CloudWatch-Transaction-Search-EnableConsole"></a>

 The following procedure describes how to enable Transaction Search in the console. 

**To enable Transaction Search in the CloudWatch console**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1.  From the navigation pane, under **Application Signals**, choose **Transaction Search**. 

1.  Choose **Enable Transaction Search**. 

1.  Select the box to ingest spans as structured logs, and enter a percentage of spans to be indexed. You can index spans at 1% for free and change the percentage later based on your requirements. 

1. (Optional) Select **Customize encryption settings (advanced)**, and then choose a customer managed key to encrypt the `aws/spans` log group with your own key. For more information about the key requirements, see [Encrypting spans with a customer managed key](#Enable-TransactionSearch-kms).

## Enabling Transaction Search using an API
<a name="CloudWatch-Transaction-Search-EnableAPI"></a>

 The following procedure describes how to enable Transaction Search using an API. 

### Step 1. Create a policy that grants access to ingest spans in CloudWatch Logs
<a name="w2aac25c21c15c13b5"></a>

 When using the AWS CLI or SDK to enable Transaction Search, you must configure permissions using a resource-based policy with [`PutResourcePolicy`](https://docs.aws.amazon.com/xray/latest/api/API_PutResourcePolicy.html). 

**Example policy**  
 The following example policy allows X-Ray to send traces to CloudWatch Logs 

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "TransactionSearchXRayAccess",
            "Effect": "Allow",
            "Principal": {
                "Service": "xray.amazonaws.com"
            },
            "Action": "logs:PutLogEvents",
            "Resource": [
                "arn:aws:logs:{{us-east-1}}:{{123456789012}}:log-group:aws/spans:*",
                "arn:aws:logs:{{us-east-1}}:{{123456789012}}:log-group:/aws/application-signals/data:*"
            ],
            "Condition": {
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:xray:{{us-east-1}}:{{123456789012}}:*"
                },
                "StringEquals": {
                    "aws:SourceAccount": "{{123456789012}}"
                }
            }
        }
    ]
}
```

------

**Example command**  
 The following example shows how to format your AWS CLI command with `PutResourcePolicy`. 

```
aws logs put-resource-policy --policy-name MyResourcePolicy --policy-document '{ "Version": "2012-10-17",		 	 	  "Statement": [ { "Sid": "TransactionSearchXRayAccess", "Effect": "Allow", "Principal": { "Service": "xray.amazonaws.com" }, "Action": "logs:PutLogEvents", "Resource": [ "arn:partition:logs:region:account-id:log-group:aws/spans:*", "arn:partition:logs:region:account-id:log-group:/aws/application-signals/data:*" ], "Condition": { "ArnLike": { "aws:SourceArn": "arn:partition:xray:region:account-id:*" }, "StringEquals": { "aws:SourceAccount": "account-id" } } } ]}'
```

### Step 2. Configure the destination of trace segments
<a name="w2aac25c21c15c13b7"></a>

 Configure the ingestion of spans with [`UpdateTraceSegmentDestination`](https://docs.aws.amazon.com/xray/latest/api/API_UpdateTraceSegmentDestination.html). 

**Example command**  
 The following example shows how to format your AWS CLI command with `UpdateTraceSegmentDestination`. 

```
aws xray update-trace-segment-destination --destination CloudWatchLogs
```

To encrypt the `aws/spans` log group with your own key, add the key ARN in `CloudWatchLogsConfiguration`. For more information about the key requirements, see [Encrypting spans with a customer managed key](#Enable-TransactionSearch-kms). In the following example, replace the key ARN with the ARN of your key.

```
aws xray update-trace-segment-destination --destination CloudWatchLogs --cloud-watch-logs-configuration '{"SpansLogGroupKmsKeyId": "arn:{{partition}}:kms:{{region}}:{{account-id}}:key/{{key-id}}"}'
```

### Step 3. Configure the amount of spans to index
<a name="w2aac25c21c15c13b9"></a>

 Configure your desired sampling percentage with [`UpdateIndexingRule`](https://docs.aws.amazon.com/xray/latest/api/API_UpdateIndexingRule.html) 

**Example command**  
 The following example shows how to format your AWS CLI command with `UpdateIndexingRule`. 

```
aws xray update-indexing-rule --name "Default" --rule '{"Probabilistic": {"DesiredSamplingPercentage": number}}'
```

**Note**  
 After you enable Transaction Search, it can take 10 minutes for spans to become available for search and analysis. 

### Step 4. Verify spans are available for search and analysis
<a name="w2aac25c21c15c13c11"></a>

 To verify spans are available for search and analysis, use [`GetTraceSegmentDestination`](https://docs.aws.amazon.com/xray/latest/api/API_GetTraceSegmentDestination.html). 

**Example commands**  
 The following example shows how to format your AWS CLI command with `GetTraceSegmentDestination`. 

```
aws xray get-trace-segment-destination
```

**Example response**  
 The following example shows the response you can expect when Transaction Search is active. 

```
{
    "Destination": "CloudWatchLogs",
    "Status": "ACTIVE"
}
```

If you used a customer managed key, the following command shows which key encrypts the `aws/spans` log group.

```
aws logs describe-log-groups --log-group-name-prefix aws/spans --query 'logGroups[].kmsKeyId'
```