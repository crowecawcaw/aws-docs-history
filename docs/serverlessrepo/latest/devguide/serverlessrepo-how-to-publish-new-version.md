# Publishing a New Version of

an Existing Application

This section shows you how to publish a new version of an existing application to the
AWS Serverless Application Repository by using the AWS SAM CLI or the AWS Management Console. For instructions on publishing a new
application, see [How to Publish Applications](serverlessrepo-how-to-publish.md "serverlessrepo-how-to-publish.md").

## Publishing a New

Version of an Existing Application (AWS CLI)

The easiest way to publish a new version of an existing application is to use a
set of AWS SAM CLI commands. For more information, see [Publishing an Application Using the AWS SAM CLI](../../../serverless-application-model/latest/developerguide/serverless-sam-template-publishing-applications.md "../../../serverless-application-model/latest/developerguide/serverless-sam-template-publishing-applications.md") in the
_AWS Serverless Application Model (AWS SAM) Developer Guide_.

## Publishing a New

Version of an Existing Application (Console)

To publish a new version of an application that you have previously published,
follow these steps:

1. Open the [AWS Serverless Application Repository
   console](https://console.aws.amazon.com/serverlessrepo/home "https://console.aws.amazon.com/serverlessrepo/home").
2. In the navigation pane, choose **My Applications** to
   bring up the list of applications that you've created.
3. Choose the application that you want to publish a new version for.
4. Choose **Publish new version**.
5. In **Versions**, enter the following application
   information:

| Property             | Required | Description                                                                                                                                                                                                                                    |
| -------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Semantic version** | TRUE     | The semantic version of the application. For more<br>information, see the [Semantic Versioning website](https://semver.org/ "https://semver.org/").<br>You must provide a value for this property in order to<br>make your application public. |
| **Source code Url**  | FALSE    | A link to a public repository for the source code of your<br>application.                                                                                                                                                                      |
| **SAM template**     | TRUE     | A valid AWS Serverless Application Model (AWS SAM) template that defines the<br>AWS resources that are used.                                                                                                                                   |

6. Choose **Publish version**.
