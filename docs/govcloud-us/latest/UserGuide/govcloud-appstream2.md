# Amazon AppStream 2.0 in AWS GovCloud (US)

Amazon AppStream 2.0 is a fully managed application streaming service that provides users with instant access to their desktop applications from anywhere. AppStream 2.0 manages the AWS resources required to host and run your applications, scales automatically, and provides access to your users on demand. AppStream 2.0 provides users access to the applications they need on the device of their choice, with a responsive, fluid user experience that is indistinguishable from natively installed applications.

## How Amazon AppStream 2.0 differs for AWS GovCloud (US)

- The Graphics Design and Graphics Pro instance types are not supported in the AWS GovCloud (US-East) Region.
- The Windows Server 2012 image is not supported in the AWS GovCloud (US-East) Region.
- Copying AppStream 2.0 images from the AWS GovCloud (US) Regions to other AWS Regions is not supported.
- The AppStream 2.0 user pool is not supported.
- The following CloudFormation resources are not available in AWS GovCloud (US):
  - [AWS::AppStream::User](../../../AWSCloudFormation/latest/UserGuide/aws-resource-appstream-user.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-appstream-user.md")
  - [AWS::AppStream::StackUserAssociation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackuserassociation.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackuserassociation.md")

- The following AppStream 2.0 API actions are not supported in AWS GovCloud (US):
  - [BatchAssociateUserStack](../../../appstream2/latest/APIReference/API_BatchAssociateUserStack.md "../../../appstream2/latest/APIReference/API_BatchAssociateUserStack.md")

  - [BatchDisassociateUserStack](../../../appstream2/latest/APIReference/API_BatchDisassociateUserStack.md "../../../appstream2/latest/APIReference/API_BatchDisassociateUserStack.md")

  - [DescribeUserStackAssociations](../../../appstream2/latest/APIReference/API_DescribeUserStackAssociations.md "../../../appstream2/latest/APIReference/API_DescribeUserStackAssociations.md"), when USERPOOL is specified for the AuthenticationType parameter. USERPOOL is the only supported value for this parameter.

  - [CreateUser](../../../appstream2/latest/APIReference/API_CreateUser.md "../../../appstream2/latest/APIReference/API_CreateUser.md")

  - [DeleteUser](../../../appstream2/latest/APIReference/API_DeleteUser.md "../../../appstream2/latest/APIReference/API_DeleteUser.md")

  - [DescribeUsers](../../../appstream2/latest/APIReference/API_DescribeUsers.md "../../../appstream2/latest/APIReference/API_DescribeUsers.md")

  - [DisableUser](../../../appstream2/latest/APIReference/API_DisableUser.md "../../../appstream2/latest/APIReference/API_DisableUser.md")

  - [EnableUser](../../../appstream2/latest/APIReference/API_EnableUser.md "../../../appstream2/latest/APIReference/API_EnableUser.md")

## Documentation for Amazon AppStream 2.0

[Amazon AppStream 2.0 documentation](../../../appstream2.md "../../../appstream2.md").

[Configure the Relay State of Your Federation](../../../appstream2/latest/developerguide/external-identity-providers-setting-up-saml.md#external-identity-providers-relay-state "../../../appstream2/latest/developerguide/external-identity-providers-setting-up-saml.md#external-identity-providers-relay-state").

[Instance type pricing and availability by region can be found here.](https://aws.amazon.com/appstream2/pricing/ "https://aws.amazon.com/appstream2/pricing/")

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Amazon AppStream 2.0 metadata is not permitted to contain export-controlled data. This
  metadata includes all configuration data that you enter when creating and
  maintaining AppStream 2.0 image builders, images, fleets, and stacks.
- Do not enter export-controlled data in
  the following console fields or when using the AppStream 2.0 API actions or AWS Command Line Interface
  (AWS CLI) commands:
  - Names and descriptions for Amazon AppStream 2.0 image builders, images, fleets
    and stacks.
  - Resource tags.
  - If importing export-controlled images, do not use pre-signed URLs for
    the CLI argument.
