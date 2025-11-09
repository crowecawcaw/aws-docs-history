AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Delete an AWS Mainframe Modernization application

You can delete an AWS Mainframe Modernization application from an environment using the AWS Mainframe Modernization console.

These instructions assume that you have completed the steps in [Set up for AWS Mainframe Modernization](setting-up.md "setting-up.md").

## Delete an application

If you need to delete an AWS Mainframe Modernization application, and it is running, make sure that you stop it
first. You can see the application status on the **Applications** page.

###### To delete an application

1. Open the AWS Mainframe Modernization console at [https://console.aws.amazon.com/m2/](https://console.aws.amazon.com/m2/ "https://console.aws.amazon.com/m2/").
2. In the AWS Region selector, choose the Region where the application that you want to
   delete from the environment was created.
3. On the **Applications** page, choose the application that you want to
   delete from the environment, and then choose **Actions**.
4. (Optional) If the status of the application is `Running`, choose
   **Stop application**.
5. Choose **Delete from environment**.

The delete process starts immediately.
