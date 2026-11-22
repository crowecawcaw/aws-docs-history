

# Allow IAM users or groups to access Infrastructure Performance

Users who sign in to the AWS Management Console or AWS CLI must have permissions to access specific resources. You provide those permissions by using IAM, through policies.

The following procedure creates a policy that grants access to all Infrastructure Performance actions. To follow least-privilege best practices, include only the actions that your users need.

## Create an IAM policy
<a name="CloudWatch-InfrastructurePerformance-IAM-Create-Policy"></a>

Create a policy that provides users full access to Infrastructure Performance. Then attach the policy to a user or group.

**To create and attach an IAM policy using the console**

1. Open the [Policies page](https://console.aws.amazon.com/iam/home#/policies) of the IAM console.

1. In the content pane, choose **Create policy**.

1. In the policy editor, choose **JSON**, and then replace the contents with the following policy:

   ```json
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "ec2:DisableAwsNetworkPerformanceMetricSubscription",
                   "ec2:DescribeAwsNetworkPerformanceMetricSubscriptions",
                   "ec2:EnableAwsNetworkPerformanceMetricSubscription",
                   "ec2:GetAwsNetworkPerformanceData"
               ],
               "Resource": "*"
           }
       ]
   }
   ```

   This example policy grants access to all Infrastructure Performance actions. To follow least-privilege best practices, include only the actions that your users need. For example, for users who only view network performance data, include only `ec2:GetAwsNetworkPerformanceData` and `ec2:DescribeAwsNetworkPerformanceMetricSubscriptions`.

1. Choose **Next**.

1. On the **Review and create** page, for **Policy name**, enter a name, such as `NetworkPerformancePolicy`. Optionally, enter a description.

1. Review the permissions that the policy grants, and then choose **Create policy**.

1. Attach the new policy to your user or group.

   For information about attaching a policy to a user, see [Changing permissions for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html) in the *IAM User Guide*.

   For information about attaching a policy to a group, see [Attaching a policy to an IAM user group](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_attach-policy.html) in the *IAM User Guide*.