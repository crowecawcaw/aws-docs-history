# Tutorial: Create the IAM execution role

If your account doesn't already have an IAM execution role, use the following steps to create
the role.

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**.
3. Choose **Create role**.
4. For **Trusted entity type**, choose**AWS service**.
5. For **Service or use case**, choose **Elastic Container
   Service**. Then choose **Elastic Container Service Task**
   again.
6. Choose **Next**.
7. For **Permissions policies**, search for
   **AmazonECSTaskExecutionRolePolicy**.
8. Choose the check box to the left of the
   **AmazonECSTaskExecutionRolePolicy** policy, and then choose
   **Next**.
9. For **Role Name**, enter `ecsTaskExecutionRole` and then
   choose **Create role**.
