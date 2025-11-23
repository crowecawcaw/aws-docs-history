# View image resource details

On the image details page in the Image Builder console, you can view details for a specific image
resource that you own. You can also use commands or actions with the Image Builder API, SDKs, or
AWS CLI to get image details.

For more information about resources that another AWS account shared with you
through a AWS Resource Access Manager (AWS RAM) resource share, see
[Access AWS resources shared
with you](../../../ram/latest/userguide/working-with-shared.md "../../../ram/latest/userguide/working-with-shared.md") in the _AWS RAM User Guide_.

###### Contents

- [View image details in the Image Builder console](#view-image-details-console "#view-image-details-console")
- [Get image policy details from the AWS CLI](#cli-get-image-policy-details "#cli-get-image-policy-details")

## View image details in the Image Builder console

The image detail page in the Image Builder console includes a summary section, with
additional information grouped into tabs. The page heading is the
name and build version of the recipe that created the image. If a tab doesn't apply
to your image, the tab is inactive and doesn't display data.

###### Console detail sections and tabs

- [Summary section](#view-image-details-console-summary "#view-image-details-console-summary")
- [Output resources tab](#view-image-details-console-output-tab "#view-image-details-console-output-tab")
- [Infrastructure configuration
  tab](#view-image-details-console-infra-tab "#view-image-details-console-infra-tab")
- [Distribution
  settings tab](#view-image-details-console-distrib-tab "#view-image-details-console-distrib-tab")
- [Workflow
  tab](#view-image-details-console-workflow-tab "#view-image-details-console-workflow-tab")
- [Security findings
  tab](#view-image-details-console-findings-tab "#view-image-details-console-findings-tab")
- [Tags
  tab](#view-image-details-console-tags-tab "#view-image-details-console-tags-tab")

### Summary section

The summary section spans the width of the page and includes the following details. These
details are always displayed.

**Recipe**

The recipe name and version that doesn't include the build
version. For example, if the build version is
`sample-linux-recipe | 1.0.1/2`, the recipe is
`sample-linux-recipe | 1.0.1`, and the build version
is `2`.

**Date created**

The date and time when Image Builder created the image build version.

**Image status**

The current status of the image build version.
Status can relate to the image build or disposition. For example,
during the build process, you might see a status of `Building` or
`Distributing`. For disposition of the image, you might see a status
of `Deprecated` or `Deleted`.

**Reason for failure**

The reason for the image status.
The Image Builder console only displays the reason when the build fails
(**Image status** equals `Failed`).

### Output resources tab

The **Output resources** tab lists output and distribution details for the
image resource that is currently displayed. The information that Image Builder displays
depends on the type of recipe that the pipeline used to create the image, as
follows.

###### Image recipe

- **Region** – The distribution Region for the
  output Amazon Machine Image (AMI) that is specified in the
  **Image** column.
- **Image** – The ID of the AMI that Image Builder
  distributed to the destination. This ID is linked to the **Amazon
  Machine Images (AMIs)** page in the Amazon EC2 console.

###### Note

Image Builder creates the AMI after it creates the output image resource, and
before it distributes the AMI to the destination.

- **Name** – The name of the AMI that Image Builder
  distributed to the destination.
- **Description** – The optional description from
  the image recipe that the pipeline used to create the output image
  resource.
- **Account** – The AWS account that owns the
  currently displayed Image Builder image resource.

###### Container recipe

Image Builder displays the following details for output created from a container
recipe.

- **Region** – The distribution Region for the
  container image that is specified in the **Image URI**
  column.
- **Image URI** – The URI of the output container
  image that Image Builder distributed to the ECR repository in the destination
  Region.

###### Note

Image Builder displays one row per destination. The output image always has at least
one entry for distribution to the account that created the image. Additional
destinations can include distributions across Regions, AWS accounts, or
AWS Organizations. For more information, see [Manage Image Builder distribution settings](manage-distribution-settings.md "manage-distribution-settings.md").

### Infrastructure configuration

tab

The **Infrastructure configuration** tab displays the Amazon EC2 infrastructure
settings that Image Builder used to build and test the image that is currently displayed.
Image Builder always displays the name of the infrastructure configuration resource
(**Configuration name**) and its Amazon Resource Name
(**ARN**). If your infrastructure configuration sets the
values, additional infrastructure details can include the following

- Instance types
- An instance profile
- Network infrastructure
- Security group settings
- An Amazon S3 location where Image Builder stores application logs
- An Amazon EC2 key pair for troubleshooting
- An Amazon SNS topic for event notifications

For more information, see [Manage Image Builder infrastructure configuration](manage-infra-config.md "manage-infra-config.md").

### Distribution

settings tab

The **Distribution settings** tab displays settings that
Image Builder used to distribute your output images. Image Builder always displays the name of
the distribution configuration resource (**Configuration name**)
and its Amazon Resource Name (**ARN**). Additional
distribution details depend on the type of recipe that the Image Builder pipeline
used to create the image, as follows:

###### Image recipe

If your distribution configuration resource sets the values, additional distribution
details can include the following,:

- **Region** – The distribution Region for the
  output Amazon Machine Image (AMI).
- **Output AMI name** – The name of the AMI that
  Image Builder distributed to the destination.
- **Encryption (KMS key)** – If configured, the
  AWS KMS key that Image Builder uses to encrypt the image for distribution to the
  target Region.
- **Target accounts for distribution** – If you
  configured cross-account distribution, this column displays a
  comma-separated list of AWS accounts to share the output image with in the
  target Region.
- **Principals with shared permission** – A
  comma-separated list of the AWS principals that have permission to launch
  your image, for example, AWS accounts or groups, AWS Organizations or
  organizational units (OUs).

###### Note

When you grant permission for other principals to launch your image,
you still own the image. AWS bills your account for all of the
instances that Amazon EC2 launches from your image.

- **Target accounts for faster launch configuration**
  – The AWS accounts where EC2 Fast Launch distributes pre-provisioned
  snapshots for launch.
- **Associated license configurations** – The License Manager
  license configuration ARNs that are associated with the AMI in the specified
  Region.
- **Launch template configuration** – Identifies an Amazon EC2
  launch template to use for a specific account.
- **Set launch template default version** – Sets the
  specified Amazon EC2 launch template as the default launch template for the specified
  AWS account.

###### Container recipe

Container distributions always include the following details:

- **Region** – The distribution Region for the
  container image specified in the **Image URI**
  column.
- **Image URI** – The URI of the output container
  image that Image Builder distributed to the Amazon ECR repository in the destination
  Region.

###### Note

Image Builder displays one row per destination. The output image always has at least
one entry for distribution to the account that created the image. Additional
destinations can include distributions across Regions, AWS accounts, or
AWS Organizations. For more information, see [Manage Image Builder distribution settings](manage-distribution-settings.md "manage-distribution-settings.md").

### Workflow

tab

Workflows define the sequence of steps that Image Builder performs
when it creates a new image. All images have build, test, and distribution workflows. The **Workflow** tab displays
the applicable workflows that Image Builder ran for your image.

###### Filter workflow types

Image Builder initially displays the build or import workflow summary and workflow steps
by default. However, the **Workflow** filter shows all of the workflows
that are in progress or completed for your image. To view a different workflow, select
from the list.

Image workflows that produce AMI output can have build, import, or test workflows.
Container workflows that produce container output can have build, test, or distribution
workflows.

###### Note

If the workflow hasn't started yet, it doesn't appear in the list.
For example, if your image build that has both build and test workflows
configured has just started, the build workflow is the only workflow type
that appears in the list. When the test workflow begins, Image Builder adds it to
the list.

Following the **Workflow** filter, the selected workflow
shows a runtime summary that includes the following details for every
workflow type:

**Workflow status**

The current runtime status for this workflow. Values can include
the following:

- Pending
- Skipped
- Running
- Completed
- Failed
- Rollback-in-progress
- Rollback-completed

**Execution ID**

A unique identifier that Image Builder assigns to keep track of
runtime resources each time it runs a workflow.

**Start**

The timestamp when the runtime instance of this workflow
started.

**End**

The timestamp when this runtime instance of the workflow
finished.

**Total steps**

The total number of steps in the workflow. This should
equal the sum of the step counts for steps that succeeded,
were skipped, and failed.

**Steps succeeded**

A runtime count for the number of steps in the workflow
that ran successfully.

**Steps failed**

A runtime count for the number of steps in the workflow
that failed.

**Steps skipped**

A runtime count for the number of steps in the workflow
that were skipped.

The details in the following list report the current status for all
of the steps in this runtime instance of the workflow. Image Builder displays
the same details for all image types.

**Step #**

A number that represents the order in which Image Builder runs
the workflow steps.

**Step ID**

A unique identifier for the workflow step, assigned
at runtime.

**Step status**

The current runtime status of the specified workflow
step.

**Rollback status**

The current rollback status if this runtime instance
of the workflow failed.

**Step name**

The name of the specified workflow step.

**Start**

The timestamp when the specified step for this runtime instance
of the workflow started.

**End**

The timestamp when the specified step for this runtime instance
of the workflow finished.

### Security findings

tab

If you've activated scanning, the **Security findings** tab displays
Common Vulnerabilities and Exposures (CVE) findings. Amazon Inspector identified these findings
on the test instance that Image Builder launched to create your new image. To ensure that
Image Builder captures findings for your image, you must configure scanning as
follows:

1. Activate Amazon Inspector scans for your account. For more information, see
   [Getting started with
   Amazon Inspector](../../../inspector/v1/userguide/inspector_getting-started.md "../../../inspector/v1/userguide/inspector_getting-started.md") in the
   _Amazon Inspector User Guide_.
2. Activate security findings for the pipeline that creates this image. When you activate
   security findings for your pipeline, Image Builder saves a snapshot of the findings
   before it terminates the test instance. For more information, see [Configure security scans for Image Builder images in the AWS Management Console](image-security-findings.md#image-config-security-scans "image-security-findings.md#image-config-security-scans")

The **Security findings** tab includes the following details
for each vulnerability that Amazon Inspector identified for your image.

**Severity**

The severity level of the CVE finding. Values are as follows:

- Untriaged
- Informational
- Low
- Medium
- High
- Critical

**Finding ID**

The unique identifier for the CVE finding that Amazon Inspector detected
for your image when it scanned the test instance. The ID is linked
to the **Security findings > By vulnerability** page.
For more information, see
[Manage security findings for Image Builder images in the AWS Management Console](image-security-findings.md#image-manage-security-findings "image-security-findings.md#image-manage-security-findings").

**Source**

The source of the vulnerability information for the CVE finding.

**Age**

The number of days since the finding was first observed for
your image.

**Inspector score**

The score that Amazon Inspector assigned for the CVE finding.

### Tags

tab

The **Tags** tab displays any tags that you have
defined for your image.

## Get image policy details from the AWS CLI

The following example shows how to get the details of an image policy with its Amazon
Resource Name (ARN).

```
aws imagebuilder get-image-policy --image-arn arn:aws:imagebuilder:`us-west-2`:`123456789012:image`/`example-image`/2019.12.02
```
