

# Prerequisites
<a name="prerequisites"></a>

Make sure the following prerequisites are completed before installing the CloudWatch agent for the first time.

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

(Optional) If the agent is going to send logs to CloudWatch Logs and you want the agent to be able to set retention policies for these log groups, you need to add the `logs:PutRetentionPolicy` permission to the role.

### Create IAM user for on-premises servers
<a name="iam-user-onprem"></a>

If you're going to run the CloudWatch agent on on-premises servers, create an IAM user with the necessary permissions.

**Note**  
This scenario requires IAM users with programmatic access and long-term credentials, which presents a security risk. To help mitigate this risk, we recommend that you provide these users with only the permissions they require to perform the task and that you remove these users when they are no longer needed.

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Users** and then **Add users**.

1. Enter the user name for the new user. Select **Access key - Programmatic access** and choose **Next: Permissions**.

1. Choose **Attach existing policies directly**.

1. In the list of policies, select the check box next to **CloudWatchAgentServerPolicy**. If necessary, use the search box to find the policy. Choose **Next: Tags**.

1. (Optional) Create tags for the new IAM user. Choose **Next: Review**. Confirm that the correct policy is listed and choose **Create user**.

1. Next to the name of the new user, choose **Show**. Copy the access key and secret key to a file so that you can use them when installing the agent. Choose **Close**.

### Attach an IAM role to an Amazon EC2 instance
<a name="attach-iam-role"></a>

To enable the CloudWatch agent to send data from an Amazon EC2 instance, you must attach the IAM role you created to the instance.

For more information about attaching an IAM role to an instance, see [Attaching an IAM Role to an Instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/iam-roles-for-amazon-ec2.html#attach-iam-role) in the Amazon Elastic Compute Cloud User Guide.

### Allowing the CloudWatch agent to set log retention policy
<a name="CloudWatch-Agent-PutLogRetention"></a>

You can configure the CloudWatch agent to set the retention policy for log groups that it sends log events to. If you do this, you must grant the `logs:PutRetentionPolicy` to the IAM role or user that the agent uses. The agent uses an IAM role to run on Amazon EC2 instances, and uses an IAM user for on-premises servers.

**To grant log retention permissions to the agent's IAM role**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the left navigation pane, choose **Roles**.

1. In the search box, enter the beginning of the name of the CloudWatch agent's IAM role. You chose this name when you created the role. It might be named `CloudWatchAgentServerRole`.

   When you see the role, choose the name of the role.

1. In the **Permissions** tab, choose **Add permissions**, **Create inline policy**.

1. Choose the **JSON** tab and copy the following policy into the box, replacing the default JSON in the box:

------
#### [ JSON ]

****  

   ```
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

1. Choose **Review policy**.

1. For **Name**, enter **CloudWatchAgentPutLogsRetention** or something similar, and choose **Create policy**.

**To grant log retention permissions to the agent's IAM user**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the left navigation pane, choose **Users**.

1. In the search box, enter the beginning of the name of the CloudWatch agent's IAM user. You chose this name when you created the user.

   When you see the user, choose the name of the user.

1. In the **Permissions** tab, choose **Add inline policy**.

1. Choose the **JSON** tab and copy the following policy into the box, replacing the default JSON in the box:

------
#### [ JSON ]

****  

   ```
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

1. Choose **Review policy**.

1. For **Name**, enter **CloudWatchAgentPutLogsRetention** or something similar, and choose **Create policy**.

## Network requirements
<a name="network-requirements"></a>

**Note**  
When the server is in a public subnet make sure there is access to an internet gateway. When the server is in a private subnet, access is through the NAT gateways or VPC Endpoint. For more information about NAT gateways, see [https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html).

Your Amazon EC2 instances must have outbound internet access to send data to CloudWatch or CloudWatch Logs. For more information about how to configure internet access, see [Internet Gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) in the Amazon VPC User Guide.

### Using VPC endpoints
<a name="vpc-endpoints"></a>

If you're using a VPC and want to use CloudWatch agent without public internet access, you can configure VPC endpoints for CloudWatch and CloudWatch Logs.

The endpoints and ports to configure on your proxy are as follows:
+ If you're using the agent to collect metrics, you must add the CloudWatch endpoints for the appropriate Regions to the allow list. These endpoints are listed in [Amazon CloudWatch endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/cw_region.html).
+ If you're using the agent to collect logs, you must add the CloudWatch Logs endpoints for the appropriate Regions to the allow list. These endpoints are listed in [Amazon CloudWatch Logs endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/cwl_region.html).
+ If you're using Systems Manager to install the agent or Parameter Store to store your configuration file, you must add the Systems Manager endpoints for the appropriate Regions to the allow list. These endpoints are listed in [AWS Systems Manager endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html).