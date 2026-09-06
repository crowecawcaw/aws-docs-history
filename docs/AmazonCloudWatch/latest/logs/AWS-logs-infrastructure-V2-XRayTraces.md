

# Traces sent to X-Ray
<a name="AWS-logs-infrastructure-V2-XRayTraces"></a>

**User permissions**

To enable sending traces to AWS X-Ray, you must be signed in with the following permissions.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ReadWriteAccessForLogDeliveryActions",
            "Effect": "Allow",
              "Action": [
                "logs:GetDelivery",
                "logs:GetDeliverySource",
                "logs:PutDeliveryDestination",
                "logs:GetDeliveryDestinationPolicy",
                "logs:DeleteDeliverySource",
                "logs:PutDeliveryDestinationPolicy",
                "logs:CreateDelivery",
                "logs:GetDeliveryDestination",
                "logs:PutDeliverySource",
                "logs:DeleteDeliveryDestination",
                "logs:DeleteDeliveryDestinationPolicy",
                "logs:DeleteDelivery",
                "logs:UpdateDeliveryConfiguration"
            ],
            "Resource": [
            "arn:aws:logs:{{us-east-1}}:{{111122223333}}:delivery:*",
            "arn:aws:logs:{{us-east-1}}:{{111122223333}}:delivery-source:*",
            "arn:aws:logs:{{us-east-1}}:{{111122223333}}:delivery-destination:*"
            ]
        },
        {
            "Sid": "ListAccessForLogDeliveryActions",
            "Effect": "Allow",
            "Action": [
                "logs:DescribeDeliveryDestinations",
                "logs:DescribeDeliverySources",
                "logs:DescribeDeliveries",
                "logs:DescribeConfigurationTemplates"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowUpdatesToResourcePolicyXRay",
            "Effect": "Allow",
            "Action": [
                "xray:PutResourcePolicy",
                "xray:ListResourcePolicies",
                "xray:GetTraceSegmentDestination"
            ],
            "Resource": "*"
        }
    ]
}
```

------

**X-Ray resource policy**

The destination account where the traces are being sent must have a resource policy that includes certain permissions. When the user setting up the tracing has `xray:PutResourcePolicy` and `xray:ListResourcePolicies` permissions in the account, AWS automatically creates the resource policy when you begin sending traces to X-Ray. The policy that is created depends on the source service :

**Amazon Bedrock AgentCore resources**  
AWS creates one resource policy per resource type. The policy uses wildcard patterns scoped to the account boundary, covering all resources of the same Amazon Bedrock AgentCore resource type in the account. For example, if a *Amazon Bedrock AgentCore Memory* resource is enabled for trace delivery, the policy covers all memory resources in that account — including any memory resources created in the future.    
****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AWSLogDeliveryWrite",
      "Effect": "Allow",
      "Principal": {
        "Service": "delivery.logs.amazonaws.com"
      },
      "Action": "xray:PutTraceSegments",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "123456789012"
        },
        "ForAllValues:ArnLike": {
          "logs:LogGeneratingResourceArns": "arn:aws:bedrock-agentcore:us-east-1:123456789012:memory/*"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:logs:us-east-1:123456789012:delivery-source:*"
        }
      }
    }
  ]
}
```

**Other AWS services**  
For other services that support trace delivery, AWS creates a resource policy scoped to the specific source resource.    
****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AWSLogDeliveryWrite",
      "Effect": "Allow",
      "Principal": {
        "Service": "delivery.logs.amazonaws.com"
      },
      "Action": "xray:PutTraceSegments",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "123456789012"
        },
        "ForAllValues:ArnLike": {
          "logs:LogGeneratingResourceArns": "arn:aws:bedrock:us-east-1:123456789012:knowledge-base/KnowledgeBaseId"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:logs:us-east-1:123456789012:delivery-source:xray-test"
        }
      }
    }
  ]
}
```

**Enable transaction search**

To enable sending traces to X-Ray, you must enable [transaction search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Enable-Lambda-TransactionSearch.html).