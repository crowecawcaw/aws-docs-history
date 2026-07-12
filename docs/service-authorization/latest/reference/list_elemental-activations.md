# Actions, resources, and condition keys for AWS Elemental Appliances and Software Activation Service

AWS Elemental Appliances and Software Activation Service (service prefix: `elemental-activations`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md").
- View a list of the [API operations available for
  this service](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/elemental-activations/elemental-activations.json "https://servicereference.us-east-1.amazonaws.com/v1/elemental-activations/elemental-activations.json") for this service.

###### Topics

- [Actions defined by AWS Elemental Appliances and Software Activation Service](#list_elemental-activations-actions-as-permissions "#list_elemental-activations-actions-as-permissions")
- [Permission-only actions for AWS Elemental Appliances and Software Activation Service](#list_elemental-activations-permission-only-actions "#list_elemental-activations-permission-only-actions")
- [Resource types defined by AWS Elemental Appliances and Software Activation Service](#list_elemental-activations-resources-for-iam-policies "#list_elemental-activations-resources-for-iam-policies")
- [Condition keys for AWS Elemental Appliances and Software Activation Service](#list_elemental-activations-policy-keys "#list_elemental-activations-policy-keys")

## Actions defined by AWS Elemental Appliances and Software Activation Service

AWS Elemental Appliances and Software Activation Service has no API operations that can be used in the
`Actions` element of an IAM policy statement.

## Permission-only actions for AWS Elemental Appliances and Software Activation Service

The following actions are defined by AWS Elemental Appliances and Software Activation Service but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                                   | Description                                                                                                                   | Resource types (\*required) | Condition keys | Access level |
| ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [CompleteAccountRegistration](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md")      | Grants permission to complete the process of registering customer account for AWS Elemental Appliances and Software Purchases |                             |                | Write        |
| [CompleteFileUpload](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md")               | Grants permission to complete the process of uploading a Software file for AWS Elemental Appliances and Software Purchases    |                             |                | Write        |
| [ConfirmAccount](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md")                   | Grants permission to confirm asset ownership                                                                                  |                             |                | Write        |
| [DownloadKickstart](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md")                | Grants permission to download the kickstart files for AWS Elemental Appliances and Software purchases                         |                             |                | Read         |
| [DownloadSoftware](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md")                 | Grants permission to download the Software files for AWS Elemental Appliances and Software Purchases                          |                             |                | Read         |
| [GenerateLicense](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md")                  | Grants permission to generate a software license for an AWS Elemental Appliances and Software purchase                        |                             |                | Write        |
| [GenerateLicenses](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md")                 | Grants permission to generate Software Licenses for AWS Elemental Appliances and Software Purchases                           |                             |                | Write        |
| [GetArtifactGroupSoftwareVersions](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md") | Grants permission to describe the software version of an artifact group                                                       |                             |                | Read         |
| [GetAsset](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md")                         | Grants permission to describe an asset                                                                                        |                             |                | Read         |
| [GetAssets](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md")                        | Grants permission to describe assets associated to the requesting account                                                     |                             |                | Read         |
| [GetProductAdvisories](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md")             | Grants permission to get all product advisories                                                                               |                             |                | Read         |
| [GetSoftwareVersions](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md")              | Grants permission to describe available software versions                                                                     |                             |                | Read         |
| [StartFileUpload](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md")                  | Grants permission to start the process of uploading a Software file for AWS Elemental Appliances and Software Purchases       |                             |                | Write        |

## Resource types defined by AWS Elemental Appliances and Software Activation Service

AWS Elemental Appliances and Software Activation Service does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Elemental Appliances and Software Activation Service

AWS Elemental Appliances and Software Activation Service has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
