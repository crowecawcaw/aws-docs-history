

# Prerequisites

Make sure the following prerequisites are completed before installing the CloudWatch agent for the first time.

## Required IAM permissions
<a name="CloudWatch-Agent-required-iam-permissions"></a>

The agent requires an AWS Identity and Access Management (IAM) role (for EC2) or user (for on-premises) with the correct permissions. Missing or incomplete permissions often cause the agent to start without publishing metrics or logs.

To grant the required permissions, do the following:
+ Attach `CloudWatchAgentServerPolicy` to the role or user on every instance that runs the agent. This policy grants permission to publish metrics, create and write log groups and streams, and read the Amazon EC2 Systems Manager (SSM) parameters used for agent configuration. The policy grants `ssm:GetParameter` only on parameters whose names begin with `AmazonCloudWatch-`, so store your agent configuration under a parameter name that uses that prefix.
+ For cross-account delivery, add an `sts:AssumeRole` statement that references the target account role. For more information about cross-account delivery, see [Sending metrics, logs, and traces to a different account](CloudWatch-Agent-common-scenarios.md#CloudWatch-Agent-send-to-different-AWS-account).

The following table maps common permission errors to their causes.


| Error | Likely cause | 
| --- | --- | 
| `AccessDeniedException` on `PutMetricData` or `PutLogEvents` | `CloudWatchAgentServerPolicy` is not attached to the instance role. | 
| `AccessDeniedException` on `GetParameter` | The Parameter Store parameter name does not begin with `AmazonCloudWatch-`. `CloudWatchAgentServerPolicy` grants `ssm:GetParameter` only on parameters with that prefix. | 

## Network requirements
<a name="CloudWatch-Agent-network-requirements"></a>

The CloudWatch agent sends data to AWS service endpoints over HTTPS (port 443). Your servers must be able to reach those endpoints through one of the following:
+ An internet gateway, for Amazon EC2 instances in a public subnet. For more information, see [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) in the *Amazon VPC User Guide*.
+ A NAT gateway, for Amazon EC2 instances in a private subnet. For more information, see [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) in the *Amazon VPC User Guide*.
+ Interface VPC endpoints, for Amazon EC2 instances without internet access. For more information, see the endpoint list in this section.
+ A proxy server. You specify the proxy in the agent's `common-config.toml` file.

**Note**  
If VPC Block Public Access is turned on for your account, instances in a public subnet can't reach the internet through an internet gateway, even if they have a public IP address. In ingress-only mode, only traffic through NAT gateways and egress-only internet gateways is allowed. Use a NAT gateway, VPC endpoints, or a Block Public Access exclusion. For more information, see [Block public access to VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html) in the *Amazon VPC User Guide*.

The agent must reach the following endpoints over HTTPS (TCP 443):
+ `monitoring.{{region}}.amazonaws.com`: for publishing metrics
+ `ec2.{{region}}.amazonaws.com`: for EC2 instance tag lookups used by the agent. If the agent can't reach this endpoint, the `fetch-config` command stops responding before the agent starts.
+ `logs.{{region}}.amazonaws.com`: for publishing logs

If you use AWS Systems Manager (Systems Manager) to install the agent or Parameter Store to hold its configuration, the agent must also reach the following endpoints. These match the SSM endpoints referenced in the installation section.
+ `ssm.{{region}}.amazonaws.com`
+ `ssmmessages.{{region}}.amazonaws.com`
+ `ec2messages.{{region}}.amazonaws.com`

You might also need these endpoints:
+ `xray.{{region}}.amazonaws.com`: to send traces, or to use Application Signals.
+ `s3.{{region}}.amazonaws.com`: to download the agent package and the `AWS-ConfigureAWSPackage` document. Create this as a gateway endpoint, not an interface endpoint.
+ `sts.{{region}}.amazonaws.com`: only if you use `role_arn` to send data to a different account.

In private subnets without a NAT gateway, create a Amazon Virtual Private Cloud (Amazon VPC) endpoint for each of these services. Create interface endpoints for all of the services except Amazon S3, and enable private DNS on each interface endpoint. Create a gateway endpoint for Amazon S3, which routes through a route table and does not use private DNS. To test connectivity before installing, run the following `curl` command:

```
curl -v https://monitoring.{{region}}.amazonaws.com
```

For more information about the installation procedure, see [Installing the CloudWatch agent](install-CloudWatch-Agent-on-EC2-Instance.md).

## IAM roles and users for CloudWatch agent
<a name="iam-setup"></a>

Access to AWS resources requires permissions. You create an IAM role, an IAM user, or both to grant permissions that the CloudWatch agent needs to write metrics to CloudWatch.

### Create an IAM role for Amazon EC2 instances
<a name="iam-role-ec2"></a>

If you're going to run the CloudWatch agent on Amazon EC2 instances, create an IAM role with the necessary permissions.

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**.

1. Choose **Create role**.

1. Under **Trusted entity type**, verify that **AWS service** is selected. For **Use case**, choose **EC2**. Choose **Next**.

1. In the list of policies, select the check box next to **CloudWatchAgentServerPolicy**. If necessary, use the search box to find the policy.

1. Choose **Next**.

1. For **Role name**, enter a name for the role, such as `CloudWatchAgentServerRole`. Choose **Create role**.

### Create IAM user for on-premises servers
<a name="iam-user-onprem"></a>

If you're going to run the CloudWatch agent on on-premises servers, create an IAM user with the necessary permissions.

**Note**  
This scenario requires IAM users with programmatic access and long-term credentials, which presents a security risk. To help mitigate this risk, we recommend that you provide these users with only the permissions they require to perform the task and that you remove these users when they are no longer needed.

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Users** and then **Create user**.

1. Enter the user name for the new user and choose **Next**.

1. Choose **Attach policies directly**.

1. In the list of policies, select the check box next to **CloudWatchAgentServerPolicy**. If necessary, use the search box to find the policy. Choose **Next**.

1. (Optional) Add tags for the new IAM user. Confirm that the correct policy is listed and choose **Create user**.

1. Choose the name of the new user, and then choose the **Security credentials** tab.

1. Under **Access keys**, choose **Create access key**. For **Use case**, choose **Application running outside AWS**, and then choose **Next**.

1. Choose **Create access key**. Copy the access key and secret access key and store them securely so that you can use them when installing the agent. Choose **Done**. For more information, see [Manage access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) in the *IAM User Guide*.

### Attach an IAM role to an Amazon EC2 instance
<a name="attach-iam-role"></a>

To enable the CloudWatch agent to send data from an Amazon EC2 instance, you must attach the IAM role you created to the instance.

For more information about attaching an IAM role to an instance, see [Attach an IAM role to an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/attach-iam-role.html) in the Amazon Elastic Compute Cloud User Guide.

### Allowing the CloudWatch agent to set log retention policy
<a name="CloudWatch-Agent-PutLogRetention"></a>

You can configure the CloudWatch agent to set the retention policy for log groups that it sends log events to. To do this, the IAM role or user that the agent uses must have the `logs:PutRetentionPolicy` permission. The **CloudWatchAgentServerPolicy** managed policy includes this permission, so you don't need to take any further action if you attached that policy.

If you use a custom policy instead of **CloudWatchAgentServerPolicy**, grant the permission with a policy like the following:

------
#### [ JSON ]

****  

```json
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "logs:PutRetentionPolicy",
      "Resource": "*"
    }
  ]
}
```

------