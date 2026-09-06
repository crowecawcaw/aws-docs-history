

# Tutorial: Create the IAM execution role
<a name="create-execution-role"></a>

If your account doesn't already have an IAM execution role, use the following steps to create the role.

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**. 

1. Choose **Create role**. 

1. For **Trusted entity type**, choose** AWS service**.

1. For **Service or use case**, choose **Elastic Container Service**. Then choose **Elastic Container Service Task** again.

1. Choose **Next**.

1. For **Permissions policies**, search for **AmazonECSTaskExecutionRolePolicy**.

1. Choose the check box to the left of the **AmazonECSTaskExecutionRolePolicy** policy, and then choose **Next**.

1. For **Role Name**, enter `ecsTaskExecutionRole` and then choose **Create role**.