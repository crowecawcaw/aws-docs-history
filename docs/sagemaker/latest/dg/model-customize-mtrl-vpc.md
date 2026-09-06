

# Configure a VPC for multi-turn RL jobs
<a name="model-customize-mtrl-vpc"></a>

When you provide a `VpcConfig` in your multi-turn RL job configuration, Amazon SageMaker AI places a proxy elastic network interface (ENI) in your VPC. All customer data traffic — including access to your S3 buckets, agent invocations, and logging — flows through this ENI. This keeps data within your VPC network boundary.

**Subnets**

Provide two or more private subnets in different Availability Zones for redundancy. The subnets do not need a NAT gateway or internet access because all traffic exits through VPC endpoints.

**Security group**

Create a security group with the following outbound rules. No inbound rules are required.
+ Outbound TCP 443 to `0.0.0.0/0`
+ Outbound UDP 53 to `0.0.0.0/0`

**Note**  
For tighter security, you can restrict egress to the S3 managed prefix list and the private IP addresses of your interface endpoint ENIs instead of allowing `0.0.0.0/0`.

**VPC endpoints**

Create the following VPC endpoints so that traffic from the proxy ENI can reach AWS services without internet access.


| Endpoint | Traffic routed | Service name | Type | 
| --- | --- | --- | --- | 
| S3 (required) | Prompt data, job output, MLflow artifacts (GetObject, PutObject, ListBucket) | com.amazonaws.{{region}}.s3 | Gateway | 
| CloudWatch Logs (required) | Training container logs (PutLogEvents, CreateLogGroup, CreateLogStream) | com.amazonaws.{{region}}.logs | Interface | 
| Bedrock AgentCore (required if using Bedrock agent) | Agent invocations (InvokeAgentRuntime) | com.amazonaws.{{region}}.bedrock-agentcore | Interface | 
| Lambda (required if using Lambda agent) | Agent invocations via Lambda forwarder (Invoke) | com.amazonaws.{{region}}.lambda | Interface | 
| MLflow (required if using MLflow tracking) | Training metrics and traces (LogBatch, StartTrace, EndTrace) | aws.sagemaker.{{region}}.mlflow | Interface | 

**Note**  
Enable Private DNS on all interface endpoints.

**Interface endpoint security group**

All interface endpoints must share a security group with inbound TCP 443 from your VPC CIDR.

**IAM permissions**

The execution role must include EC2 permissions for ENI management. Add the following policy statement to the role.

```
[
    {
        "Effect": "Allow",
        "Action": [
            "ec2:CreateNetworkInterface",
            "ec2:CreateNetworkInterfacePermission",
            "ec2:DeleteNetworkInterface",
            "ec2:DeleteNetworkInterfacePermission",
            "ec2:DescribeNetworkInterfaces",
            "ec2:DescribeSubnets",
            "ec2:DescribeSecurityGroups",
            "ec2:DescribeVpcs"
        ],
        "Resource": "*"
    },
    {
        "Effect": "Allow",
        "Action": [
            "ec2:CreateTags"
        ],
        "Resource": "arn:aws:ec2:*:*:network-interface/*",
        "Condition": {
            "StringEquals": {
                "ec2:CreateAction": "CreateNetworkInterface"
            }
        }
    }
]
```

**API configuration**

Include the `VpcConfig` parameter in your multi-turn RL job request.

```
"VpcConfig": {
    "Subnets": ["subnet-0abc123", "subnet-0def456"],
    "SecurityGroupIds": ["sg-0abc123def"]
}
```

You can apply additional restrictions to further secure your VPC configuration.

**S3 bucket policy**

To restrict S3 access to your VPC only, add a deny policy with the `aws:SourceVpc` condition.

```
{
    "Sid": "DenyAccessFromOutsideVpc",
    "Effect": "Deny",
    "Principal": "*",
    "Action": "s3:*",
    "Resource": [
        "arn:aws:s3:::{{my-mtrl-bucket}}",
        "arn:aws:s3:::{{my-mtrl-bucket}}/*"
    ],
    "Condition": {
        "StringNotEquals": {
            "aws:SourceVpc": "{{vpc-0abc123def}}"
        }
    }
}
```

**Note**  
The `aws:SourceVpc` condition key is only populated when the request traverses an S3 Gateway Endpoint.

**VPC endpoint policies**

You can restrict interface endpoints to allow only the actions that multi-turn RL jobs need. The following example restricts a CloudWatch Logs endpoint to log groups with the `/aws/sagemaker/Job/` prefix.

```
{
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "logs:PutLogEvents",
                "logs:CreateLogGroup",
                "logs:CreateLogStream"
            ],
            "Resource": "arn:aws:logs:*:*:log-group:/aws/sagemaker/Job/*"
        }
    ]
}
```