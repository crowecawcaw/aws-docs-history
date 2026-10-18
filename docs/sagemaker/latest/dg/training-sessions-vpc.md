

# Configure a VPC for SageMaker AI training sessions
<a name="training-sessions-vpc"></a>

When you provide a `VpcConfig` in your `CreateTrainingSession` request, SageMaker AI training sessions place a proxy elastic network interface (ENI) in your VPC. All customer data traffic — including access to your Amazon S3 buckets for checkpoints and model artifacts — flows through this ENI. This keeps data within your VPC network boundary.

**Topics**
+ [Required VPC setup](#training-sessions-vpc-setup)
+ [IAM permissions](#training-sessions-vpc-iam)
+ [API configuration](#training-sessions-vpc-api)
+ [Restrict access to your VPC](#training-sessions-vpc-restrict)

## Required VPC setup
<a name="training-sessions-vpc-setup"></a>

**Subnets**

Provide at least two private subnets in different Availability Zones for redundancy. Up to 16 subnets are supported.

Enable DNS support and DNS hostnames on your VPC.

```
aws ec2 modify-vpc-attribute --vpc-id vpc-0abc123 \
    --enable-dns-support '{"Value": true}'
aws ec2 modify-vpc-attribute --vpc-id vpc-0abc123 \
    --enable-dns-hostnames '{"Value": true}'
```

The subnets do not need a NAT gateway or internet gateway because all AWS service traffic exits through VPC endpoints.

**Security group**

Create a security group with the following outbound rules. No inbound rules are required for the proxy ENI itself.

Scope the egress rules to your VPC CIDR, or to the private IP addresses or security group of your Amazon S3 interface endpoint ENIs. Don't scope them to the Amazon S3 managed prefix list (`pl-xxxxxxxx`). That list contains only the public IP ranges of Amazon S3, which apply to a gateway endpoint. In this setup, Amazon S3 traffic goes through the interface endpoint and resolves to private ENI IP addresses inside your VPC.


| Protocol | Port | Destination | Purpose | 
| --- | --- | --- | --- | 
| TCP | 443 | Your VPC CIDR, for example 10.0.0.0/16 | HTTPS to the Amazon S3 interface endpoint | 
| UDP | 53 | Your VPC CIDR, for example 10.0.0.0/16 | DNS resolution via the VPC resolver | 

Up to 5 security groups are supported.

The following example creates the security group and its egress rules. Replace `10.0.0.0/16` with your VPC CIDR.

```
SG_ID=$(aws ec2 create-security-group \
    --group-name training-session-proxy-sg \
    --description "Proxy ENI for SageMaker Training Sessions" \
    --vpc-id vpc-0abc123 \
    --query 'GroupId' --output text)

# Remove the default allow-all egress rule
aws ec2 revoke-security-group-egress --group-id ${SG_ID} \
    --ip-permissions '[{"IpProtocol": "-1", "IpRanges": [{"CidrIp": "0.0.0.0/0"}]}]'

# Allow HTTPS egress within the VPC
aws ec2 authorize-security-group-egress --group-id ${SG_ID} \
    --protocol tcp --port 443 --cidr 10.0.0.0/16

# Allow DNS egress within the VPC
aws ec2 authorize-security-group-egress --group-id ${SG_ID} \
    --protocol udp --port 53 --cidr 10.0.0.0/16
```

**VPC endpoints**

Create an Amazon S3 interface endpoint in your VPC so that the service can reach your Amazon S3 bucket without traversing the public internet. The service routes checkpoint reads and writes through a proxy network interface that uses your VPC's DNS resolver — an interface endpoint with Private DNS enabled is required so that Amazon S3 hostnames resolve to private IPs within your VPC.

**Why an interface endpoint (not a gateway endpoint)?** The service proxy sends Amazon S3 traffic to whatever IP your VPC's DNS resolver returns for the Amazon S3 hostname. With an interface endpoint and Private DNS enabled, that resolves to private ENI IPs reachable from any subnet, so routing works no matter which of your `VpcConfig.Subnets` the proxy ENI is placed in. A gateway endpoint is a valid, cheaper alternative, but it routes via an Amazon S3 prefix-list entry in the subnet's route table — so you would have to ensure that prefix-list route is present on the route table of every subnet you pass in `VpcConfig.Subnets`, since the service picks the subnet at runtime.


| Endpoint | Traffic routed | Service name | Type | 
| --- | --- | --- | --- | 
| Amazon S3 (required) | Checkpoints, model artifacts | com.amazonaws.{{region}}.s3 | Interface | 

Create a security group for the interface endpoint, then create the Amazon S3 interface endpoint with it. This is a separate security group from the proxy ENI group you created earlier.

**Important**  
Enable Private DNS on the endpoint. The service proxy uses your VPC's DNS resolver to reach Amazon S3. Without Private DNS, Amazon S3 hostnames don't resolve to private IP addresses, and checkpoint operations fail. The following command sets `--private-dns-enabled`.

```
ENDPOINT_SG_ID=$(aws ec2 create-security-group \
    --group-name training-session-endpoint-sg \
    --description "S3 interface endpoint for SageMaker Training Sessions" \
    --vpc-id vpc-0abc123 \
    --query 'GroupId' --output text)

aws ec2 create-vpc-endpoint \
    --vpc-id vpc-0abc123 \
    --service-name com.amazonaws.us-east-1.s3 \
    --vpc-endpoint-type Interface \
    --subnet-ids subnet-0abc123 subnet-0def456 \
    --security-group-ids ${ENDPOINT_SG_ID} \
    --private-dns-enabled
```

**Interface endpoint security group**

The Amazon S3 interface endpoint must have a security group that allows inbound TCP 443 from your VPC CIDR.

```
aws ec2 authorize-security-group-ingress --group-id ${ENDPOINT_SG_ID} \
    --protocol tcp --port 443 --cidr 10.0.0.0/16
```

## IAM permissions
<a name="training-sessions-vpc-iam"></a>

The execution role you pass as `RoleArn` to `CreateTrainingSession` must have Amazon EC2 permissions to manage the proxy ENI on your behalf. The `AmazonSageMakerTrainingSessionFullAccess` managed policy includes these permissions. If you use a custom execution role, add the following three policy statements.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EC2NetworkPermissions",
            "Effect": "Allow",
            "Action": [
                "ec2:CreateNetworkInterface",
                "ec2:CreateNetworkInterfacePermission",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeVpcs",
                "ec2:DescribeSubnets",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeDhcpOptions"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "EC2NetworkInterfaceTagPermissions",
            "Effect": "Allow",
            "Action": [
                "ec2:CreateTags"
            ],
            "Resource": "arn:aws:ec2:*:*:network-interface/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}",
                    "ec2:CreateAction": "CreateNetworkInterface"
                }
            }
        },
        {
            "Sid": "EC2NetworkInterfaceDeletePermissions",
            "Effect": "Allow",
            "Action": [
                "ec2:DeleteNetworkInterface",
                "ec2:DeleteNetworkInterfacePermission"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        }
    ]
}
```

## API configuration
<a name="training-sessions-vpc-api"></a>

Include the `VpcConfig` parameter in your `CreateTrainingSession` request. Specify up to 5 security group IDs and up to 16 subnet IDs.

```
{
    "VpcConfig": {
        "SecurityGroupIds": ["sg-0abc123def"],
        "Subnets": ["subnet-0abc123", "subnet-0def456"]
    }
}
```

Using the AWS CLI:

```
aws sagemaker create-training-session \
    --training-session-name my-session \
    --role-arn arn:aws:iam::111122223333:role/MySageMakerRole \
    --base-model-arn arn:aws:sagemaker:us-east-1:aws:hub-content/SageMakerPublicHub/Model/openai-reasoning-gpt-oss-20b \
    --vpc-config SecurityGroupIds=sg-0abc123def,Subnets=subnet-0abc123,subnet-0def456
```

You cannot modify `VpcConfig` after a session is created. To change the VPC configuration, create a new training session.

## Restrict access to your VPC
<a name="training-sessions-vpc-restrict"></a>

You can apply additional controls to harden your VPC configuration.

**Amazon S3 bucket policy**

To restrict Amazon S3 access to requests originating from your VPC endpoint only, add a deny statement with the `aws:SourceVpce` condition key. This prevents any Amazon S3 access that does not flow through your specific Amazon S3 interface endpoint — including direct access from the public internet or from other VPC endpoints. For more information, see [Using Amazon S3 bucket policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html).

```
{
    "Sid": "DenyAccessFromOutsideVpcEndpoint",
    "Effect": "Deny",
    "Principal": "*",
    "Action": "s3:*",
    "Resource": [
        "arn:aws:s3:::amzn-s3-demo-bucket",
        "arn:aws:s3:::amzn-s3-demo-bucket/*"
    ],
    "Condition": {
        "StringNotEquals": {
            "aws:SourceVpce": "vpce-0abc123def456"
        }
    }
}
```

**Note**  
Replace `vpce-0abc123def456` with the VPC endpoint ID of the Amazon S3 interface endpoint you created. To find it, run `aws ec2 describe-vpc-endpoints --filters Name=service-name,Values=com.amazonaws.{{region}}.s3 Name=vpc-id,Values=vpc-0abc123`. If you prefer to scope by VPC rather than a specific endpoint, use `aws:SourceVpc` with your VPC ID instead — both condition keys are available for interface endpoints.

**VPC endpoint policies**

You can attach a resource policy to your Amazon S3 interface endpoint to limit which actions and buckets are accessible through it. The following example restricts the endpoint to the specific Amazon S3 actions that training sessions require on your training bucket.

```
{
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket",
                "arn:aws:s3:::amzn-s3-demo-bucket/*"
            ]
        }
    ]
}
```

Any Amazon S3 request through this endpoint that targets a different bucket or uses a different action is denied by the endpoint policy, even if the requester's IAM policy would otherwise allow it.