

# Publishing a New Version of an Existing Application
<a name="serverlessrepo-how-to-publish-new-version"></a>

This section shows you how to publish a new version of an existing application to the AWS Serverless Application Repository by using the AWS SAM CLI or the AWS Management Console. For instructions on publishing a new application, see [How to Publish Applications](serverlessrepo-how-to-publish.md).

## Publishing a New Version of an Existing Application (AWS CLI)
<a name="serverlessrepo-how-to-publish-new-version-cli"></a>

The easiest way to publish a new version of an existing application is to use a set of AWS SAM CLI commands. For more information, see [Publishing an Application Using the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-template-publishing-applications.html) in the *AWS Serverless Application Model (AWS SAM) Developer Guide*.

## Publishing a New Version of an Existing Application (Console)
<a name="serverlessrepo-how-to-publish-new-version-console"></a>

To publish a new version of an application that you have previously published, follow these steps:

1. Open the [AWS Serverless Application Repository console](https://console.aws.amazon.com/serverlessrepo/home).

1. In the navigation pane, choose **My Applications** to bring up the list of applications that you've created.

1. Choose the application that you want to publish a new version for.

1. Choose **Publish new version**.

1. In **Versions**, enter the following application information:


<table>
<thead>
  <tr><th>Property</th><th>Required</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><b>Semantic version</b></td><td>TRUE</td><td>The semantic version of the application. For more information, see the <a href="https://semver.org/">Semantic Versioning website</a>.<br />You must provide a value for this property in order to make your application public.</td></tr>
  <tr><td><b>Source code Url</b></td><td>FALSE</td><td>A link to a public repository for the source code of your application.</td></tr>
  <tr><td><b>SAM template</b></td><td>TRUE</td><td>A valid AWS Serverless Application Model (AWS SAM) template that defines the AWS resources that are used.</td></tr>
</tbody>
</table>


1. Choose **Publish version**.