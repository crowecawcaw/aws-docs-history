# Step 7: Delete the AWS resources created for this

tutorial

In the final step of [Getting Started Using
Amazon MSK](getting-started.md "getting-started.md"), you delete the MSK cluster and the client machine
that you created for this tutorial.

###### To delete the resources using the AWS Management Console

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/](https://console.aws.amazon.com/msk/ "https://console.aws.amazon.com/msk/").
2. Choose the name of your cluster. For example,
   **MSKTutorialCluster**.
3. Choose **Actions**, then choose
   **Delete**.
4. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
5. Choose the instance that you created for your client machine, for example,
   `MSKTutorialClient`.
6. Choose **Instance state**, then choose **Terminate
   instance**.

###### To delete the IAM policy and role

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. On the navigation pane, choose **Roles**.
3. In the search box, enter the name of the IAM role that you created for this tutorial.
4. Choose the role. Then choose **Delete role**, and confirm the deletion.
5. On the navigation pane, choose **Policies**.
6. In the search box, enter the name of the policy that you created for this tutorial.
7. Choose the policy to open its summary page. On the policy's **Summary** page, choose **Delete policy**.
8. Choose **Delete**.
