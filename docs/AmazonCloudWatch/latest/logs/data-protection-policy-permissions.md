

# IAM permissions required to create or work with a data protection policy
<a name="data-protection-policy-permissions"></a>

To be able to work with data protection policies for log groups, you must have certain permissions as shown in the following tables. The permissions are different for account-wide data protection policies and for data protection policies that apply to a single log group.

## Permissions required for account-level data protection policies
<a name="data-protection-policy-permissions-accountlevel"></a>

**Note**  
If you are performing any of these operations inside a Lambda function, the Lambda execution role and permissions boundary must also include the following permissions.



- ** **Create a data protection policy with no audit destinations** **
  - **IAM permission needed:** `logs:PutAccountPolicy` / **Resource:** `*`
  - **IAM permission needed:** `logs:PutDataProtectionPolicy` / **Resource:** `*`

- ** **Create a data protection policy with CloudWatch Logs as an audit destination** **
  - **IAM permission needed:** `logs:PutAccountPolicy` / **Resource:** `*`
  - **IAM permission needed:** `logs:PutDataProtectionPolicy` / **Resource:** `*`
  - **IAM permission needed:** `logs:CreateLogDelivery` / **Resource:** `*`
  - **IAM permission needed:** `logs:PutResourcePolicy` / **Resource:** `*`
  - **IAM permission needed:** `logs:DescribeResourcePolicies` / **Resource:** `*`
  - **IAM permission needed:** `logs:DescribeLogGroups` / **Resource:** `*`

- ** **Create a data protection policy with Firehose as an audit destination** **
  - **IAM permission needed:** `logs:PutAccountPolicy` / **Resource:** `*`
  - **IAM permission needed:** `logs:PutDataProtectionPolicy` / **Resource:** `*`
  - **IAM permission needed:** `logs:CreateLogDelivery` / **Resource:** `*`
  - **IAM permission needed:** `firehose:TagDeliveryStream` / **Resource:** `arn:aws:logs:::deliverystream/{{YOUR_DELIVERY_STREAM}}`

- ** **Create a data protection policy with Amazon S3 as an audit destination** **
  - **IAM permission needed:** `logs:PutAccountPolicy` / **Resource:** `*`
  - **IAM permission needed:** `logs:PutDataProtectionPolicy` / **Resource:** `*`
  - **IAM permission needed:** `logs:CreateLogDelivery` / **Resource:** `*`
  - **IAM permission needed:** `s3:GetBucketPolicy` / **Resource:** `arn:aws:s3:::{{YOUR_BUCKET}}`
  - **IAM permission needed:** `s3:PutBucketPolicy` / **Resource:** `arn:aws:s3:::{{YOUR_BUCKET}}`

- ** **Unmask masked log events in a specified log group** **
  - **IAM permission needed:** `logs:Unmask`
  - **Resource:** `arn:aws:logs:::log-group:*`

- ** **View an existing data protection policy** **
  - **IAM permission needed:** `logs:GetDataProtectionPolicy`
  - **Resource:** `*`

- ** **Delete a data protection policy** **
  - **IAM permission needed:** `logs:DeleteAccountPolicy` / **Resource:** `*`
  - **IAM permission needed:** `logs:DeleteDataProtectionPolicy` / **Resource:** `*`



If any data protection audit logs are already being sent to a destination, then other policies that send logs to the same destination only need the `logs:PutDataProtectionPolicy` and `logs:CreateLogDelivery` permissions.

## Permissions required for data protection policies for a single log group
<a name="data-protection-policy-permissions-loggroup"></a>

**Note**  
If you are performing any of these operations inside a Lambda function, the Lambda execution role and permissions boundary must also include the following permissions.


| Operation | IAM permission needed | Resource | 
| --- | --- | --- | 
| Create a data protection policy with no audit destinations | `logs:PutDataProtectionPolicy` | `arn:aws:logs:::log-group:{{YOUR_LOG_GROUP}}:*` | 
| Create a data protection policy with CloudWatch Logs as an audit destination | `logs:PutDataProtectionPolicy`<br />`logs:CreateLogDelivery`<br />`logs:PutResourcePolicy`<br />`logs:DescribeResourcePolicies`<br />`logs:DescribeLogGroups` | `arn:aws:logs:::log-group:{{YOUR_LOG_GROUP}}:*`<br />`*`<br />`*`<br />`*`<br />`*` | 
| Create a data protection policy with Firehose as an audit destination | `logs:PutDataProtectionPolicy`<br />`logs:CreateLogDelivery`<br />`firehose:TagDeliveryStream` | `arn:aws:logs:::log-group:{{YOUR_LOG_GROUP}}:*`<br />`*`<br />`arn:aws:logs:::deliverystream/{{YOUR_DELIVERY_STREAM}}` | 
| Create a data protection policy with Amazon S3 as an audit destination | `logs:PutDataProtectionPolicy`<br />`logs:CreateLogDelivery`<br />`s3:GetBucketPolicy`<br />`s3:PutBucketPolicy` | `arn:aws:logs:::log-group:{{YOUR_LOG_GROUP}}:*`<br />`*`<br />`arn:aws:s3:::{{YOUR_BUCKET}}`<br />`arn:aws:s3:::{{YOUR_BUCKET}}` | 
| Unmask masked log events | `logs:Unmask` | `arn:aws:logs:::log-group:{{YOUR_LOG_GROUP}}:*` | 
| View an existing data protection policy | `logs:GetDataProtectionPolicy` | `arn:aws:logs:::log-group:{{YOUR_LOG_GROUP}}:*` | 
| Delete a data protection policy | `logs:DeleteDataProtectionPolicy` | `arn:aws:logs:::log-group:{{YOUR_LOG_GROUP}}:*` | 

If any data protection audit logs are already being sent to a destination, then other policies that send logs to the same destination only need the `logs:PutDataProtectionPolicy` and `logs:CreateLogDelivery` permissions.

## Sample data protection policy
<a name="data-protection-policy-sample"></a>

The following sample policy allows a user to create, view, and delete data protection policies that can sending audit findings to all three types of audit destinations. It does not permit the user to view unmasked data.

------
#### [ JSON ]

****  

```
 
    {
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowLogDeliveryConfiguration",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogDelivery",
                "logs:PutResourcePolicy",
                "logs:DescribeLogGroups",
                "logs:DescribeResourcePolicies"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowDataProtectionAndBucketConfiguration",
            "Effect": "Allow",
            "Action": [
                "logs:GetDataProtectionPolicy",
                "logs:DeleteDataProtectionPolicy",
                "logs:PutDataProtectionPolicy",
                "s3:PutBucketPolicy",
                "firehose:TagDeliveryStream",
                "s3:GetBucketPolicy"
            ],
            "Resource": [
            "arn:aws:firehose:{{us-east-1}}:{{111122223333}}:deliverystream/{{delivery-stream-name}}",
            "arn:aws:s3:::{{amzn-s3-demo-destination-bucket}}",
            "arn:aws:logs:{{us-east-1}}:{{111122223333}}:log-group:{{log-group-name}}:*"
            ]
        }
    ]
}
```

------