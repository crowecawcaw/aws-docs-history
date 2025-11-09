AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Restart an AWS Mainframe Modernization runtime environment

Use the AWS Mainframe Modernization console to restart an AWS Mainframe Modernization runtime environment. When you restart a runtime
environment, the billing for the environment will be resumed.

## Restart a runtime environment

To restart an AWS Mainframe Modernization runtime environment, you follow similar steps as the stop environment
section.

###### To restart a runtime environment

1. Open the AWS Mainframe Modernization console at [https://console.aws.amazon.com/m2/](https://console.aws.amazon.com/m2/ "https://console.aws.amazon.com/m2/").
2. In the AWS Region selector, choose the Region where the environment that you want
   to restart was created.
3. On the **Environments** page, choose the environment that you want
   to restart.
4. On the details page for the environment, choose **Actions**, and
   then choose **Edit environment**.

###### Note

The desired capacity for standalone environment can only be updated to 1. To
restart a runtime environment, you can only choose to restart immediately. 5. On the **Edit environment page**, find **Resources
section**, and update the desired capacity from zero to the required
capacity. 6. Choose **Next**. 7. In **When to apply these changes**, choose
**Immediately**. Then choose **Update
environment**.

You see a message when the environment capacity is updated and the environment is
restarted.
