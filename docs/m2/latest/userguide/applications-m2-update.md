AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Update an AWS Mainframe Modernization application

Use the AWS Mainframe Modernization console to update an AWS Mainframe Modernization application. Updating an application creates
a new version of the application.

These instructions assume that you have completed the steps in [Set up for AWS Mainframe Modernization](setting-up.md "setting-up.md").

## Update an application

An AWS Mainframe Modernization application can have multiple versions, each with its own application definition.
To update an application, provide a new application definition. This creates a new version of
the application.

###### To update an application

1. Open the AWS Mainframe Modernization console at [https://console.aws.amazon.com/m2/](https://console.aws.amazon.com/m2/ "https://console.aws.amazon.com/m2/").
2. In the AWS Region selector, choose the Region where the application that you want to
   update was created.
3. On the **Applications** page, choose the application that you want to
   update.
4. On the application details page, in the **Current definition** section,
   choose **Edit** to update the current application definition.
5. On the **Update application** page, use the inline editor to update the
   current application definition.

Alternatively, choose **Use an application definition JSON file in an Amazon S3
bucket** and provide the location of the application definition that you want to
use. For more information, see [AWS Blu Age application definition
sample](applications-m2-definition.md#applications-m2-definition-ba "applications-m2-definition.md#applications-m2-definition-ba") or [Rocket Software (formerly Micro Focus) application
definition](applications-m2-definition.md#applications-m2-definition-mf "applications-m2-definition.md#applications-m2-definition-mf"). 6. When you're finished updating the application definition, choose
**Update**.

###### Note

After you update the application, you must deploy it again. For more information, see
[Deploy an AWS Mainframe Modernization application](applications-m2-deploy.md "applications-m2-deploy.md").
