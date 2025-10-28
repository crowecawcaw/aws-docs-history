AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Troubleshooting Systems Manager automation documents in

AWS Toolkit

###### I saved my automation document in AWS Toolkit, but I don’t see it in the

AWS Management Console.

Saving an automation document in AWS Toolkit doesn't publish the automation document to
AWS. For more information about publishing your Automation document, see [Publishing a Systems Manager automation document](systems-manager-automation-docs.md#systems-manager-publish "systems-manager-automation-docs.md#systems-manager-publish").

###### Publishing my automation document failed with a permissions error.

Make sure your AWS credentials profile has the necessary permissions to publish
Automation documents. For an example permissions policy, see [IAM permissions for Systems Manager Automation
documents](systems-manager-automation-docs.md#systems-manager-permissions "systems-manager-automation-docs.md#systems-manager-permissions").

###### I published my automation document to AWS, but I don’t see it in the

AWS Explorer pane.

Make sure that you’ve published the document to the same AWS Region you’re browsing in
the AWS Explorer pane.

###### I’ve deleted my automation document, but I’m still being billed for the resources it

created.

Deleting an automation document doesn’t delete the resources it created or modified. You
can identify the AWS resources that you’ve created from the [AWS Billing Management
Console](https://console.aws.amazon.com/billing/home "https://console.aws.amazon.com/billing/home"), explore your charges, and choose what resources to delete from
there.
