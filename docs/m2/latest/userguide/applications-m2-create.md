AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Create an AWS Mainframe Modernization application

Use the AWS Mainframe Modernization console to create an AWS Mainframe Modernization application. Creating an application allows
you to perform tasks with the migrated mainframe workload.

These instructions assume that you have completed the steps in [Set up for AWS Mainframe Modernization](setting-up.md "setting-up.md").

## Create an application

###### To create an application

1. Open the AWS Mainframe Modernization console at [https://console.aws.amazon.com/m2/](https://console.aws.amazon.com/m2/ "https://console.aws.amazon.com/m2/").
2. In the AWS Region selector, choose the Region where you want to create the
   application.
3. On the **Applications** page, choose **Create
   application**.
4. On the **Specify basic information** page, in the **Name and
   description** section, enter a name for the application.
5. (Optional) In the **Application description** field, enter a description
   for the application. This description can help you and other users identify the purpose of the
   application.
6. In the **Engine type** section, choose **Blu Age** for
   automated refactoring, or **Micro Focus (Rocket)** for replatforming.
7. In the **KMS key** section, choose **Customize encryption
   settings** if you want to use a customer managed AWS KMS key. For more information,
   see [Data encryption at rest for AWS Mainframe Modernization service](data-protection.md#encryption-rest "data-protection.md#encryption-rest").

###### Note

By default, AWS Mainframe Modernization encrypts your data with a AWS KMS key that AWS Mainframe Modernization owns and manages for you.
However, you can choose to use a customer managed AWS KMS key. 8. (Optional) Choose an AWS KMS key by name or Amazon Resource Name (ARN), or choose
**Create an AWS KMS key** to go to the AWS KMS console and create a new AWS KMS
key. 9. (Optional) In the **Tags** section, choose **Add new
tag** to add one or more application tags to your application. An application tag is
a custom attribute label that helps you organize and manage your AWS resources). 10. Choose **Next**. 11. In the **Resources and configurations** section, use the inline editor
to enter the application definition. Alternatively, choose **Use an application
definition JSON file in an Amazon S3 bucket** and provide the location of the
application definition that you want to use. For more information, see [AWS Blu Age application definition
sample](applications-m2-definition.md#applications-m2-definition-ba "applications-m2-definition.md#applications-m2-definition-ba") or
[Rocket Software (formerly Micro Focus) application
definition](applications-m2-definition.md#applications-m2-definition-mf "applications-m2-definition.md#applications-m2-definition-mf"). 12. Choose **Next**. 13. On the **Review and create** page, review the information that you
entered, and then choose **Create application**.
