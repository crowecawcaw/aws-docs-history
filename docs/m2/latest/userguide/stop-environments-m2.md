AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Stop an AWS Mainframe Modernization runtime environment

Use the AWS Mainframe Modernization console to stop an AWS Mainframe Modernization runtime environment. When you stop an environment the
current application deployments are retained and you won't be charged for the environment
until the environment is restarted.

These instructions assume that you have completed the steps in [Set up for AWS Mainframe Modernization](setting-up.md "setting-up.md").

## Stop a runtime environment

If you need to stop an AWS Mainframe Modernization runtime environment, you follow similar steps as the update
environment section.

Use the AWS Mainframe Modernization console to stop an AWS Mainframe Modernization runtime environment. When you stop an environment,
the current application deployments are retained and you won't be charged for the
environment until the environment is restarted.

###### Note

You must stop all applications before stopping environment.

###### To stop a runtime environment

1. Open the AWS Mainframe Modernization console at [https://console.aws.amazon.com/m2/](https://console.aws.amazon.com/m2/ "https://console.aws.amazon.com/m2/").
2. In the AWS Region selector, choose the Region where the environment that you want
   to stop was created.
3. On the **Environments** page, choose the environment that you want
   to stop.
4. On the details page for the environment, choose **Actions**, and
   then choose **Edit environment**.
5. On the **Edit environment page**, find **Resources
   section**, and update the desired capacity to zero.

###### Note

To stop an environment, you can only choose to stop immediately. 6. Choose **Next**. 7. In **When to apply these changes**, choose
**Immediately**. Then choose **Update
environment**.

You see a message when the environment capacity is updated.
