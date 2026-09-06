

# Chaining IAM roles in Amazon Neptune
<a name="bulk-load-tutorial-chain-roles"></a>

**Important**  
The new bulk load cross-account feature introduced in [engine release 1.2.1.0.R3](engine-releases-1.2.1.0.R3.md) that takes advantage of chaining IAM roles may in some cases cause you to observe degraded bulk load performance. As a result, upgrades to engine releases that support this feature have been temporarily suspended until this problem is resolved.

When you attach a role to your cluster, your cluster can assume that role to gain access to data stored in Amazon S3. Starting with [engine release 1.2.1.0.R3](engine-releases-1.2.1.0.R3.md), if that role doesn't have access to all the resources you need, you can chain one or more additional roles that your cluster can assume to gain access to other resources. Each role in the chain assumes the next role in the chain, until your cluster has assumed the role at the end of chain.

To chain roles, you establish a trust relationship between them. For example, to chain `RoleB` onto `RoleA`, `RoleA` must have a permissions policy that allows it to assume `RoleB`, and `RoleB` must have a trust policy that allows it to pass its permissions back to `RoleA`. For more information, see [Using IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html).

The first role in a chain must be attached to the cluster that is loading data.

The first role, and each subsequent role that assumes the following role in the chain, must have:
+ A policy that includes a specific statement with the `Allow` effect on the `sts:AssumeRole` action.
+ The Amazon Resource Name (ARN) of the next role in a `Resource` element.

**Note**  
The target Amazon S3 bucket must be in the same AWS Region as the cluster.

## Cross-account access using chained roles
<a name="bulk-load-tutorial-chain-cross-account"></a>

You can grant cross-account access by chaining a role or roles that belong to another account. When your cluster temporarily assumes a role belonging to another account, it can gain access to resources there.

For example, suppose **Account A** wants to access data in an Amazon S3 bucket that belongs to **Account B**:
+ **Account A** creates an AWS service role for Neptune named `RoleA` and attaches it to a cluster.
+ **Account B** creates a role named `RoleB` that's authorized to access the data in an **Account B** bucket.
+ **Account A** attaches a permissions policy to `RoleA` that allows it to assume `RoleB`.
+ **Account B** attaches a trust policy to `RoleB` that allows it to pass its permissions back to `RoleA`.
+ To access the data in the **Account B** bucket, **Account A** runs a loader command using an `iamRoleArn` parameter that chains `RoleA` and `RoleB`. For the duration of the loader operation, `RoleA` then temporarily assumes `RoleB` to access the Amazon S3 bucket in **Account B**.

![Diagram illustrating cross-account access using chained roles](http://docs.aws.amazon.com/neptune/latest/userguide/images/cross-account-bulk-load.png)


For example, `RoleA` would have a trust policy that establishes a trust relationship with Neptune:

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
          "Service": "rds.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

------

`RoleA` would also have a permission policy that allows it to assume `RoleB`, which is owned by **Account B**:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "Stmt1487639602000",
            "Effect": "Allow",
            "Action": [
                "sts:AssumeRole"
            ],
            "Resource": "arn:aws:iam::{{111122223333}}:role/RoleB"
        }
    ]
}
```

------

Conversely, `RoleB` would have a trust policy to establish a trust relationship with `RoleA`:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:role/RoleA"
            }
        }
    ]
}
```

------

`RoleB` would also need permission to access data in the Amazon S3 bucket located in **Account B**.

## Creating an AWS Security Token Service (STS) VPC endpoint
<a name="bulk-load-tutorial-sts-endpoint"></a>

The Neptune loader requires a VPC endpoint for AWS STS when you are chaining IAM roles to privately access AWS STS APIs through private IP addresses. You can connect directly from an Amazon VPC to AWS STS through a VPC Endpoint in a secure and scalable manner. When you use an interface VPC endpoint, it provides a better security posture because you don't need to open outbound traffic firewalls. It also provides the other benefits of using Amazon VPC endpoints.

When using a VPC Endpoint, traffic to AWS STS does not transmit over the internet and never leaves the Amazon network. Your VPC is securely connected to AWS STS without availability risks or bandwidth constraints on your network traffic. For more information, see [Using AWS STS interface VPC endpoints](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_sts_vpce.html).

**To set up access for AWS Security Token Service (STS)**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoints**.

1. Choose **Create Endpoint**.

1. Choose the **Service Name**: `com.amazonaws.region.sts` for the Interface type endpoint.

1. Choose the **VPC** that contains your Neptune DB instance and EC2 instance.

1. Select the check box next to the subnet in which your EC2 instance is present. You can't select multiple subnets from the same Availability Zone.

1. For IP address type, choose from the following options:
   + **IPv4** – Assign IPv4 addresses to your endpoint network interfaces. This option is supported only if all selected subnets have IPv4 address ranges.
   + **IPv6** – Assign IPv6 addresses to your endpoint network interfaces. This option is supported only if all selected subnets are IPv6-only subnets.
   + **Dualstack** – Assign both IPv4 and IPv6 addresses to your endpoint network interfaces. This option is supported only if all selected subnets have both IPv4 and IPv6 address ranges.

1. For **Security groups**, select the security groups to associate with the endpoint network interfaces for the VPC endpoint. You would need to select all the security groups that is attached to your Neptune DB instance and EC2 instance.

1. For **Policy**, select **Full access** to allow all operations by all principals on all resources over the VPC endpoint. Otherwise, select **Custom** to attach a VPC endpoint policy that controls the permissions that principals have for performing actions on resources over the VPC endpoint. This option is available only if the service supports VPC endpoint policies. For more information, see [Endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html).

1. (*Optional*) To add a tag, choose **Add new tag** and enter the tag key and the tag value you want.

1. Choose **Create endpoint**.

For information about creating the endpoint, see [VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the Amazon VPC User Guide. Please note that Amazon STS VPC Endpoint is a required prerequisite for IAM role chaining.

Now that you have granted access to the AWS STS endpoint, you can prepare to load data. For information about supported formats, see [Load Data Formats](bulk-load-tutorial-format.md).

## Chaining roles within a loader command
<a name="bulk-load-tutorial-loader-chain"></a>

You can specify role chaining when you run a loader command by including a comma-separated list of role ARNs in the `iamRoleArn` parameter.

Although you'll mostly only need to have two roles in a chain, it is certainly possible to chain three or more together. For example, this loader command chains three roles:

------
#### [ AWS CLI ]

```
aws neptunedata start-loader-job \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --source "s3://{{(the target bucket name)}}/{{(the target date file name)}}" \
  --format "csv" \
  --iam-role-arn "arn:aws:iam::{{(Account A ID)}}:role/{{(RoleA)}},arn:aws:iam::{{(Account B ID)}}:role/{{(RoleB)}},arn:aws:iam::{{(Account C ID)}}:role/{{(RoleC)}}" \
  --s3-bucket-region "{{us-east-1}}"
```

For more information, see [start-loader-job](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/start-loader-job.html) in the AWS CLI Command Reference.

------
#### [ SDK ]

```
import boto3
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://{{your-neptune-endpoint}}:{{port}}',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

response = client.start_loader_job(
    source='s3://{{(the target bucket name)}}/{{(the target date file name)}}',
    format='csv',
    iamRoleArn='arn:aws:iam::{{(Account A ID)}}:role/{{(RoleA)}},arn:aws:iam::{{(Account B ID)}}:role/{{(RoleB)}},arn:aws:iam::{{(Account C ID)}}:role/{{(RoleC)}}',
    s3BucketRegion='{{us-east-1}}'
)

print(response)
```

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/loader \
  --region {{us-east-1}} \
  --service neptune-db \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{
        "source" : "s3://{{(the target bucket name)}}/{{(the target date file name)}}",
        "iamRoleArn" : "arn:aws:iam::{{(Account A ID)}}:role/{{(RoleA)}},arn:aws:iam::{{(Account B ID)}}:role/{{(RoleB)}},arn:aws:iam::{{(Account C ID)}}:role/{{(RoleC)}}",
        "format" : "csv",
        "region" : "us-east-1"
      }'
```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

```
curl -X POST https://{{your-neptune-endpoint}}:{{port}}/loader \
  -H 'Content-Type: application/json' \
  -d '{
        "source" : "s3://{{(the target bucket name)}}/{{(the target date file name)}}",
        "iamRoleArn" : "arn:aws:iam::{{(Account A ID)}}:role/{{(RoleA)}},arn:aws:iam::{{(Account B ID)}}:role/{{(RoleB)}},arn:aws:iam::{{(Account C ID)}}:role/{{(RoleC)}}",
        "format" : "csv",
        "region" : "us-east-1"
      }'
```

------