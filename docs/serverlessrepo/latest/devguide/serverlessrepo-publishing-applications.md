# Publishing Applications

When you publish a serverless application to the AWS Serverless Application Repository, you make it available for
others to find and deploy.

You first define your application with an _AWS Serverless Application Model (AWS SAM)
template._ When you define your application, you must consider whether
consumers of your application will be required to acknowledge the application's
capabilities. For more information about using AWS SAM and acknowledging capabilities, see
[Using AWS SAM with the AWS Serverless Application Repository](using-aws-sam.md "using-aws-sam.md").

You can publish serverless applications by using the AWS Management Console, the AWS SAM command line
interface (AWS SAM CLI), or an AWS SDK. To learn more about the procedures for publishing
applications to the AWS Serverless Application Repository, see [How to Publish Applications](serverlessrepo-how-to-publish.md "serverlessrepo-how-to-publish.md").

When you publish your application, it's initially set to _private_,
which means that it's only available to the AWS account that created it. To share your
application with others, you must either set it to _privately shared_
(shared only with a specific set of AWS accounts), or _publicly shared_
(shared with everyone).

When you publish an application to the AWS Serverless Application Repository and set it to public, the service makes the
application available to consumers in all Regions. When a consumer deploys a public application to a
Region other than the Region in which the application was first published, the AWS Serverless Application Repository copies the
application’s deployment artifacts to an Amazon S3 bucket in the destination Region. It updates any
resources in the AWS SAM template that use those artifacts to instead reference the files in
the Amazon S3 bucket for the destination Region. Deployment artifacts can include Lambda function code,
API definition files, and so on.

###### Note

_Private_ and _privately shared_ applications
are only available in the AWS Region that they're created in. _Publicly
shared_ applications are available in all AWS Regions. To learn more about
sharing applications, see [AWS Serverless Application Repository
Application Policy Examples](security_iam_resource-based-policy-examples.md "security_iam_resource-based-policy-examples.md").

###### Topics

- [Using AWS SAM with the AWS Serverless Application Repository](using-aws-sam.md "using-aws-sam.md")
- [How to Publish Applications](serverlessrepo-how-to-publish.md "serverlessrepo-how-to-publish.md")
- [Verified Author Badge](serverlessrepo-verified-author.md "serverlessrepo-verified-author.md")
- [Sharing Lambda Layers](sharing-lambda-layers.md "sharing-lambda-layers.md")
