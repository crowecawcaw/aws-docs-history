# Deployment considerations

Be sure to launch _Customizations for AWS Control Tower_ (CfCT)
in the same account and Region where your AWS Control Tower landing zone is deployed; that is, you
must deploy it in the AWS Control Tower management account in your AWS Control Tower home Region. By default,
CfCT creates and runs the landing zone configuration package by setting up a configuration
pipeline in that account and Region.

## Prepare for deployment

You have some options when you prepare your CloudFormation template for initial deployment. You
can choose the configuration source, and you can allow for manual approval of pipeline
deployments. The next two sections explain more about these options.

### Choose your configuration source

By default, the template creates an Amazon Simple Storage Service (Amazon S3) bucket to store the sample
configuration package as a `.zip` file called
`_custom-control-tower-configuration.zip`. The Amazon S3 bucket is
version controlled, and you can update the configuration package as needed. For
information about updating the configuration package, refer to [Using Amazon S3 as the Configuration Source](cfct-s3-source.md "cfct-s3-source.md").

###### Remember to remove the underscore

The sample configuration package filename begins with an underscore (\_) so
that AWS CodePipeline is not initiated automatically. When you have finished
customizing the configuration package, be sure to upload the
`custom-control-tower-configuration.zip` without the underscore
(\_) in order to begin the deployment in AWS CodePipeline.

If you have an existing AWS CodeCommit Git repository, you can change the storage location of the configuration package from the Amazon S3
bucket to an AWS CodeCommit Git repository. To do so, select the `CodeCommit`
option in the CloudFormation parameter.

###### To zip, or not to zip?

When you're using the default S3 bucket, be sure that the configuration
package is available as a `.zip` file. If you're using the
AWS CodeCommit repository, be sure to place the configuration package in the
repository without zipping the files. For information about creating and storing
the configuration package in AWS CodeCommit, see [CfCT customization guide](cfct-customizations-dev-guide.md "cfct-customizations-dev-guide.md").

You can use the sample configuration package to create your own custom
configuration source. When you are ready to deploy your custom configurations,
manually upload the configuration package, either to the Amazon S3 bucket or to the
AWS CodeCommit repository. The pipeline begins automatically when you upload the
configuration file.

### Choose your pipeline

configuration approval parameters

The AWS CloudFormation template provides the option to approve the deployment of
configuration changes manually. By default, manual approval is not enabled. For more
information, refer to [Step 1. Launch the stack](step1.md "step1.md").

When manual approval is enabled, the configuration pipeline validates the
customizations made to the AWS Control Tower file manifest and templates, then it pauses the
process until manual approval is granted. After approval, the deployment proceeds to
run the remaining pipeline stages, as needed, to implement the _Customizations for AWS Control Tower_ (CfCT)
functionality.

You can use the manual approval parameter to keep the customizations for the
AWS Control Tower configuration from running, by rejecting the first attempt to run through
the pipeline. This parameter also allows you to validate customizations for the
AWS Control Tower configuration changes manually, as a final control before
implementation.

## To update Customizations for AWS Control Tower

If you have previously deployed CfCT, you must update the CloudFormation stack to get the
latest version of the CfCT framework. For details, refer to [Update the Stack](update-stack.md "update-stack.md").
