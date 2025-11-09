# Generate templates from existing resources with IaC

generator

With the CloudFormation infrastructure as code generator (IaC generator), you can generate a
template using AWS resources provisioned in your account that are not already managed by
CloudFormation.

The following are benefits of the IaC generator:

- Bring entire applications under CloudFormation management or migrate them into an
  AWS CDK app.
- Generate templates without having to describe a resource property by property and
  then translate that into JSON or YAML syntax.
- Use the template to replicate resources in a new account or Region.
  The IaC generation process consists of the following steps:

1. Scan resources – The first step is to start
   a scan of your resources. This scan is region-wide and expires after 30 days. During
   this time, you can create multiple templates from the same scan.
2. Create your template – To create the
   template, you have two options:
   - Create a new template from scratch and add the scanned resources and
     related resources to it.
   - Use an existing CloudFormation stack as a starting point and add the scanned
     resources and related resources to its template.

3. Import resources – Use your template to
   import the resources as a CloudFormation stack or migrate them into an AWS CDK app.
   The IaC generator feature is available in all commercial Regions and supports many common
   AWS resource types. For a full list of supported resources, see [Resource type
   support](resource-import-supported-resources.md "resource-import-supported-resources.md").

###### Topics

- [Considerations](#iac-generator-considerations "#iac-generator-considerations")
- [IAM permissions required for scanning
  resources](#iac-generator-permissions "#iac-generator-permissions")
- [Commonly used commands for
  template generation, management, and deletion](#iac-generator-commonly-used-commands "#iac-generator-commonly-used-commands")
- [Migrate a template to the AWS CDK](#iac-generator-cdk-migrate "#iac-generator-cdk-migrate")
- [Start a resource scan with
  CloudFormation IaC generator](iac-generator-start-resource-scan.md "iac-generator-start-resource-scan.md")
- [View the scan summary in the CloudFormation
  console](generate-IaC-view-scan-summary.md "generate-IaC-view-scan-summary.md")
- [Create a
  CloudFormation template from resources scanned with IaC generator](iac-generator-create-template-from-scanned-resources.md "iac-generator-create-template-from-scanned-resources.md")
- [Create a CloudFormation
  stack from scanned resources](iac-generator-create-stack-from-scanned-resources.md "iac-generator-create-stack-from-scanned-resources.md")
- [Resolve write-only properties](generate-IaC-write-only-properties.md "generate-IaC-write-only-properties.md")

## Considerations

You can generate JSON or YAML templates for AWS resources that you have read access
to. The templates for the IaC generator capability models cloud resources reliably and
quickly without having to describe a resource property by property.

The following table lists the quotas available for the IaC generation feature.

| Name                                                                   | Full scan | Partial scan |
| ---------------------------------------------------------------------- | --------- | ------------ |
| Maximum number of resources that can be processed in a scan            | 100,000   | 100,000      |
| Number of scans per day (for scans with less than 10,000<br>resources) | 10        | 10           |
| Number of scans per day (for scans with more than 10,000<br>resources) | 1         | 1            |
| Concurrent number of templates generating per account                  | 5         | 5            |
| Concurrent number of resources modeled for one template<br>generation  | 5         | 5            |
| Total number of resources that can be modeled in one<br>template       | 500       | 500          |
| Maximum number of generated templates per account                      | 1,000     | 1,000        |

###### Important

IaC generator only supports AWS resources that are supported by Cloud Control API in your
Region. For more information, see [Resource type
support](resource-import-supported-resources.md "resource-import-supported-resources.md").

## IAM permissions required for scanning

resources

To scan resources with IaC generator, your IAM principal (user, role, or group) must
have:

- CloudFormation scanning permissions
- Read permissions for target AWS services

The scan scope is limited to resources you have read access to. Missing permissions
won't cause scan failure but will exclude those resources.

For an example IAM policy that grants scanning and template management permissions,
see [Allow all IaC generator
operations](security_iam_id-based-policy-examples.md#iam-policy-example-for-iac-generator "security_iam_id-based-policy-examples.md#iam-policy-example-for-iac-generator").

## Commonly used commands for

template generation, management, and deletion

The commonly used commands for working with IaC generator include:

- [start-resource-scan](../../../cli/latest/reference/cloudformation/start-resource-scan.md "../../../cli/latest/reference/cloudformation/start-resource-scan.md") to start a scan of the resources in the account
  in an AWS Region.
- [describe-resource-scan](../../../cli/latest/reference/cloudformation/describe-resource-scan.md "../../../cli/latest/reference/cloudformation/describe-resource-scan.md") to monitor the progress of a resource scan.
- [list-resource-scans](../../../cli/latest/reference/cloudformation/list-resource-scans.md "../../../cli/latest/reference/cloudformation/list-resource-scans.md") to list the resource scans in an
  AWS Region.
- [list-resource-scan-resources](../../../cli/latest/reference/cloudformation/list-resource-scan-resources.md "../../../cli/latest/reference/cloudformation/list-resource-scan-resources.md") to list the resources found during the
  resource scan.
- [list-resource-scan-related-resources](../../../cli/latest/reference/cloudformation/list-resource-scan-related-resources.md "../../../cli/latest/reference/cloudformation/list-resource-scan-related-resources.md") to list the resources related
  to your scanned resources.
- [create-generated-template](../../../cli/latest/reference/cloudformation/create-generated-template.md "../../../cli/latest/reference/cloudformation/create-generated-template.md") to generate a CloudFormation template from a
  set of scanned resources.
- [update-generated-template](../../../cli/latest/reference/cloudformation/update-generated-template.md "../../../cli/latest/reference/cloudformation/update-generated-template.md") to update the generated template.
- [describe-generated-template](../../../cli/latest/reference/cloudformation/describe-generated-template.md "../../../cli/latest/reference/cloudformation/describe-generated-template.md") to return information about a generated
  template.
- [list-generated-templates](../../../cli/latest/reference/cloudformation/list-generated-templates.md "../../../cli/latest/reference/cloudformation/list-generated-templates.md") to list all generated templates in your
  account and current Region.
- [delete-generated-template](../../../cli/latest/reference/cloudformation/delete-generated-template.md "../../../cli/latest/reference/cloudformation/delete-generated-template.md") to delete a generated template.

## Migrate a template to the AWS CDK

The AWS Cloud Development Kit (AWS CDK) is an open-source software development framework that you can use to
develop, manage, and deploy CloudFormation resources using popular programming
languages.

The AWS CDK CLI provides an integration with IaC generator. Use the AWS CDK CLI `cdk
 migrate` command to convert the CloudFormation template and create a new CDK app
that contains your resources. Then, you can use the AWS CDK to manage your resources and
deploy to CloudFormation.

For more information, see [Migrate to AWS CDK](../../../cdk/v2/guide/migrate.md "../../../cdk/v2/guide/migrate.md") in the _AWS Cloud Development Kit (AWS CDK) Developer Guide_.
