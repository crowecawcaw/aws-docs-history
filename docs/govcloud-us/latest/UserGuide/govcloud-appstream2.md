

# Amazon WorkSpaces Applications in AWS GovCloud (US)
<a name="govcloud-appstream2"></a>

Amazon AppStream 2.0 is a fully managed application streaming service that provides users with instant access to their desktop applications from anywhere. AppStream 2.0 manages the AWS resources required to host and run your applications, scales automatically, and provides access to your users on demand. AppStream 2.0 provides users access to the applications they need on the device of their choice, with a responsive, fluid user experience that is indistinguishable from natively installed applications.

## How Amazon WorkSpaces Applications differs
<a name="how_amazon_shared_aas2_differs"></a>

The following differences apply to Amazon WorkSpaces Applications:
+ The Graphics Design and Graphics Pro instance types are not available in the AWS GovCloud (US-East) Region.
+ The Windows Server 2012 image is not available in the AWS GovCloud (US-East) Region.
+ Copying WorkSpaces Applications images from the AWS GovCloud (US) Regions to other AWS Regions is not available.
+ The WorkSpaces Applications user pool is not available.
+ The following CloudFormation resources are not available in AWS GovCloud (US):
  +  [AWS::AppStream::User](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-user.html) 
  +  [AWS::AppStream::StackUserAssociation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackuserassociation.html) 
+ The following AppStream 2.0 API actions are not available in AWS GovCloud (US):
  +  [BatchAssociateUserStack](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_BatchAssociateUserStack.html) 
  +  [BatchDisassociateUserStack](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_BatchDisassociateUserStack.html) 
  +  [DescribeUserStackAssociations](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeUserStackAssociations.html), when USERPOOL is specified for the AuthenticationType parameter. USERPOOL is the only supported value for this parameter.
  +  [CreateUser](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateUser.html) 
  +  [DeleteUser](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DeleteUser.html) 
  +  [DescribeUsers](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeUsers.html) 
  +  [DisableUser](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DisableUser.html) 
  +  [EnableUser](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_EnableUser.html) 

## Documentation
<a name="govcloud-aas2-docs"></a>
+  [Amazon AppStream 2.0 documentation](https://docs.aws.amazon.com/appstream2) 
+  [Configure the Relay State of Your Federation](https://docs.aws.amazon.com/appstream2/latest/developerguide/external-identity-providers-setting-up-saml.html#external-identity-providers-relay-state) 

## Export-controlled content
<a name="govcloud-appstream-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+  Amazon AppStream 2.0 metadata is not permitted to contain export-controlled data. This metadata includes all configuration data that you enter when creating and maintaining WorkSpaces Applications image builders, images, fleets, and stacks.
+ Do not enter export-controlled data in the following console fields or when using the WorkSpaces Applications API actions or AWS Command Line Interface (AWS CLI) commands:
  + Names and descriptions for Amazon AppStream 2.0 image builders, images, fleets and stacks.
  + Resource tags.
  + If importing export-controlled images, do not use pre-signed URLs for the CLI argument.