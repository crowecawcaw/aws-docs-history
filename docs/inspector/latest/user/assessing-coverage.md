# Assessing Amazon Inspector coverage of your AWS environment

You can assess Amazon Inspector coverage of your AWS environment from the **Account management** screen in the Amazon Inspector console, which shows details and statistics about the status of Amazon Inspector scans for your accounts and resources.

###### Note

If you're the delegated administrator for an organization, you can view details and statistics for all the accounts in the organization.

The following procedure describes how to assess coverage of your Amazon Inspector environment.

###### To assess Amazon Inspector coverage of your AWS environment

1. Sign in using your credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. From the navigation pane, choose **Account management**.
3. To review coverage, choose one of the following tabs:
   - Choose **Accounts** to review account-level coverage.
   - Choose **Instances** to review coverage for Amazon Elastic Compute Cloud (Amazon EC2) instances.
   - Choose **Container repositories** to review coverage of Amazon Elastic Container Registry (Amazon ECR) repositories.
   - Choose **Container images** to review coverage for Amazon ECR container images.
   - Choose **Lambda functions** to review coverage for Lambda functions.

The following topics describe the information each of these tabs provide.

###### Topics

- [Assessing account-level coverage](#viewing-coverage-accounts "#viewing-coverage-accounts")
- [Assessing coverage of Amazon EC2
  instances](#viewing-coverage-instances "#viewing-coverage-instances")
- [Assessing coverage of Amazon ECR
  repositories](#viewing-coverage-repositories "#viewing-coverage-repositories")
- [Assessing coverage of Amazon ECR container
  images](#viewing-coverage-images "#viewing-coverage-images")
- [Assessing coverage of AWS Lambda functions](#viewing-coverage-lambdas "#viewing-coverage-lambdas")

## Assessing account-level coverage

If your account is not part of an organization or is not the delegated Amazon Inspector
administrator account for an organization, the **Accounts** tab
provides information about your account and the status of resource scanning for your
account. On this tab, you can activate or deactivate scanning for all or only specific types
of resources for your account. For more information, see [Automated scan types in Amazon Inspector](scanning-resources.md "scanning-resources.md").

If your account is the delegated Amazon Inspector administrator account for an organization, the
**Accounts** tab provides automatic activation settings for
accounts in your organization, and it lists all the accounts in your organization. For
each account, the list indicates whether Amazon Inspector is activated for the account and, if so,
the resource scanning types that are activated for the account. As the delegated
administrator, you can use this tab to change the automatic activation settings for your
organization. You can also activate or deactivate specific types of resource scanning for
individual member accounts. For more information, see [Activating Amazon Inspector scans for member accounts](adding-member-accounts.md "adding-member-accounts.md").

## Assessing coverage of Amazon EC2

instances

The **Instances** tab shows Amazon EC2 instances in your AWS
environment. The lists are organized into groups on the following tabs:

- **All** – Shows all the instances in your environment.
  The **Status** column indicates the current scanning status for
  an instance.
- **Scanning** – Shows all the instances that Amazon Inspector
  is actively monitoring and scanning in your environment.
- **Not scanning** – Shows all the instances that Amazon Inspector
  is not monitoring and scanning in your environment. The
  **Reason** column indicates why Amazon Inspector is not monitoring and
  scanning an instance.

An EC2 instance can appear on the **Not scanning** tab for any of
several reasons. Amazon Inspector uses AWS Systems Manager (SSM) and the SSM Agent to
automatically monitor and scan your EC2 instances for vulnerabilities. If an instance
does not have the SSM Agent running, does not have an AWS Identity and Access Management (IAM) role
that supports Systems Manager, or is not running a supported operating system or
architecture, Amazon Inspector cannot monitor and scan the instance. For more information,
see [Amazon EC2 instance scanning](scanning-ec2.md "scanning-ec2.md").

On each tab, the **Account** column specifies the AWS account that
owns an instance.

**EC2 instance tags** – This column shows you the tags associated with the instance
and can be
used
to determine if your instance has been excluded from scans by tags.

**Operating system** – This column shows you the operating system type,
which can be `WINDOWS`, `MAC`,
`LINUX`,
or `UNKNOWN`.

**Monitored using** – This column shows whether Amazon Inspector is using the [agent-based](scanning-ec2.md#agent-based "scanning-ec2.md#agent-based") or [agentless](scanning-ec2.md#agentless "scanning-ec2.md#agentless")
scan method on this instance.

**Last scanned** – This column shows you when Amazon Inspector last checked that
resource for vulnerabilities. The frequency that Amazon Inspector performs scans depends on the
scan method
it's
using to scan the instance.

To review additional details about an EC2 instance, choose the link in the
**EC2 instance** column. Amazon Inspector then displays details about the instance
and current findings for the instance. To review the details of a finding, choose the
link in the **Title** column. For information about these details, see
[Viewing details for your Amazon Inspector findings](findings-understanding-details.md "findings-understanding-details.md").

### Scanning status values for Amazon EC2 instances

For an Amazon Elastic Compute Cloud (Amazon EC2) instance, the possible **Status** values
are:

- **Actively monitoring** – Amazon Inspector is continuously monitoring
  and scanning the instance.
- **Agentless instance storage limit exceeded** – Amazon Inspector uses this status when the combined size of all volumes attached to an instance is greater than 1200 GB, or an instance has more than 8 volumes attached to it.
- **Agentless instance collection time limit exceeded** – Amazon Inspector times out while trying to run an agentless scan on an instance.
- **EC2 instance stopped** – Amazon Inspector paused scanning
  for the instance because the instance is in a stopped state. Any existing
  findings will persist until the instance is terminated. If the instance is
  restarted, Amazon Inspector will automatically resume scanning for the instance.
- **Internal error** – An internal error occurred
  when Amazon Inspector attempted to scan the instance. Amazon Inspector will automatically address
  the error and resume scanning as soon as possible.
- **No inventory** – Amazon Inspector couldn’t find the
  software application inventory to scan for the instance. The Amazon Inspector
  associations for the instance might have been deleted or they might have
  failed to run.

To remediate this issue, use AWS Systems Manager to ensure that the
`InspectorInventoryCollection-do-not-delete` association
exists and its association status is successful. In addition, use AWS Systems Manager
Fleet Manager to verify the software application inventory for the
instance.

- **Pending disable** – Amazon Inspector has stopped scanning
  the instance. The instance is being disabled, pending completion of clean-up
  tasks.
- **Pending initial scan** – Amazon Inspector has queued the
  instance for an initial scan.
- **Resource terminated** – The instance was
  terminated. Amazon Inspector is currently cleaning up existing findings and coverage
  data for the instance.
- **Stale inventory** – Amazon Inspector wasn’t able to collect
  an updated software application inventory that was captured within the past
  7 days for the instance.

To remediate this issue, use AWS Systems Manager to ensure that the required Amazon Inspector
associations exist and are running for the instance. In addition, use
AWS Systems Manager Fleet Manager to verify the software application inventory for the
instance.

- **Unmanaged EC2 instance** – Amazon Inspector isn’t
  monitoring or scanning the instance. The instance isn’t managed by
  AWS Systems Manager.

To remediate this issue, you can use the [AWSSupport-TroubleshootManagedInstance
runbook](../../../systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshoot-managed-instance.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshoot-managed-instance.md") provided by AWS Systems Manager Automation. After you
configure AWS Systems Manager to manage the instance, Amazon Inspector will automatically begin
to continuously monitor and scan the instance.

- **Unsupported OS** – Amazon Inspector isn’t monitoring or
  scanning the instance. The instance uses an operating system or architecture
  that Amazon Inspector doesn’t support. For a list of operating systems that Amazon Inspector
  supports, see [Amazon EC2
  instances status values](supported.md#supported-os-ec2 "supported.md#supported-os-ec2").
- **Actively monitoring with partial errors** – This status means that EC2 scanning is active, but there are errors associated with [Amazon Inspector deep inspection for Linux-based Amazon EC2 instances](deep-inspection.md "deep-inspection.md"). The possible deep inspections errors are:
  - **Deep inspection package collection limit exceeded** – The instance
    has exceeded the 5000 package limit for Amazon Inspector deep inspection.
    To resume deep inspection for this instance, you can try to adjust
    the custom paths associated with the account.
  - **Deep inspection daily ssm inventory limit exceeded** – The SSM agent
    couldn't send inventory to Amazon Inspector because the SSM quota for
    _Inventory data collected per instance per
    day_ has already been reached for this instance. For
    more information, see [Amazon EC2 Systems Manager endpoints and
    quotas](../../../general/latest/gr/ssm.md "../../../general/latest/gr/ssm.md").
  - **Deep inspection collection time limit exceeded** – Amazon Inspector failed to extract the package inventory because the package collection time exceeding the maximum threshold of 15 minutes.
  - **Deep inspection has no inventory** – The [Amazon Inspector SSM plugin](inspector-ssm-plugin.md "inspector-ssm-plugin.md")hasn't yet
    been able to collect an inventory of packages for this instance.
    This is usually the result of a pending scan, however, if this
    status persists after 6 hours, use Amazon EC2 Systems Manager to ensure that the
    required Amazon Inspector associations exist and are running for the instance.

For details about configuring the scanning settings for an EC2 instance, see [Amazon EC2 instance scanning](scanning-ec2.md "scanning-ec2.md").

## Assessing coverage of Amazon ECR

repositories

The **Repositories** tab shows Amazon ECR repositories in your AWS
environment. The lists are organized into groups on the following tabs:

- **All** – Shows all the repositories in your
  environment. The **Status** column indicates the current
  scanning status for a repository.
- **Activated** – Shows all the repositories that
  Amazon Inspector is configured to monitor and scan in your environment. The
  **Status** column indicates the current scanning status for
  a repository.
- **Not activated** – Shows all the repositories that
  Amazon Inspector is not monitoring and scanning in your environment. The
  **Reason** column indicates why Amazon Inspector is not monitoring and
  scanning a repository.

On each tab, the **Account** column specifies the AWS account that
owns a repository.

To review additional details about a repository, choose the repository’s name. Amazon Inspector
then displays a list of container images in the repository and details for each image.
The details include the image tag, image digest, and scanning status. They also include
key finding statistics, such as the number of **Critical** findings for
the image. To drill down and review supporting data for finding statistics, choose the
image tag for the image.

###### Note

Amazon ECR images without continuous scanning are not included in coverage widgets.

### Scanning status values for Amazon ECR repositories

For an Amazon Elastic Container Registry (Amazon ECR) repository, the possible
**Status** values are:

- **Activated (Continuous)** – For a repository, Amazon Inspector is continuously monitoring images in this repository. The enhanced scanning setting for the repository is set to continuous scanning. Amazon Inspector initially scans new images when they are pushed and rescans images if a new CVE relevant to that image is published. Amazon Inspector will continue to be monitor images in this repository for the [Amazon ECR re-scan duration](scanning_resources_configure_duration_setting_ecr.md "scanning_resources_configure_duration_setting_ecr.md") you configure.
- **Activated (On push)** – Amazon Inspector
  automatically scans individual container images in the repository when a new
  image is pushed. Enhanced scanning is activated for the repository and set to
  scan on push.
- **Access denied** – Amazon Inspector isn’t allowed to access
  the repository or any container images in the repository.

To remediate this issue, ensure that AWS Identity and Access Management (IAM) policies for the
repository allow Amazon Inspector to access the repository.

- **Deactivated (Manual)** – Amazon Inspector isn’t monitoring or
  scanning any container images in the repository. The Amazon ECR scanning setting
  for the repository is set to basic, manual scanning.

To start scanning images in the repository with Amazon Inspector, change the scanning
setting for the repository to enhanced scanning, and then choose whether to
scan images continuously or only when a new image is pushed.

- **Activated (On push)** – Amazon Inspector
  automatically scans individual container images in the repository when a new
  image is pushed. The enhanced scanning setting for the repository is set to
  scan on push.
- **Internal error** – An internal error occurred
  when Amazon Inspector attempted to scan the repository. Amazon Inspector will
  automatically address the error and resume scanning as soon as
  possible.

For details about configuring the scanning settings for repositories [Amazon ECR container image scanning](scanning-ecr.md "scanning-ecr.md").

## Assessing coverage of Amazon ECR container

images

The **Images** tab shows Amazon ECR container images in your AWS
environment. The lists are organized into groups on the following tabs:

- **All** – Shows all the container images in your
  environment. The **Status** column indicates the current
  scanning status for an image.
- **Scanning** – Shows all the container images that
  Amazon Inspector is configured to monitor and scan in your environment. The
  **Status** column indicates the current scanning status for
  an image.
- **Not scanning** – Shows all the container images that
  Amazon Inspector is not monitoring and scanning in your environment. The
  **Reason** column indicates why Amazon Inspector is not monitoring and
  scanning an image.

A container image can appear on the **Not activated** tab for
any of several reasons. The image might be stored in a repository that Amazon Inspector
scans are not activated for, or Amazon ECR filtering rules prevent that repository from
being scanned. Or the image has not been pushed or pulled within the number of days your configured for the **ECR re-scan duration**. For more
information, see [Configuring the Amazon ECR re-scan duration](scanning_resources_configure_duration_setting_ecr.md "scanning_resources_configure_duration_setting_ecr.md").

On each tab, the **Repository name** column specifies the name of the
repository that stores a container image. The **Account** column
specifies the AWS account that owns the repository. The **Last
scanned** column shows you when Amazon Inspector last checked that resource for
vulnerabilities. This can include checks when there is an update to finding metadata,
when there is an update to the application inventory of the resource, or when a rescan
is done in response to a new CVE. For more information, see [Scan behaviors for Amazon ECR scanning](scanning-ecr.md#ecr-scan-behavior "scanning-ecr.md#ecr-scan-behavior").

To review additional details about a container image, choose the link in the
**ECR container image** column. Amazon Inspector then displays details about
the image and current findings for the image. To review the details of a finding, choose
the link in the **Title** column. For information about these details,
see [Viewing details for your Amazon Inspector findings](findings-understanding-details.md "findings-understanding-details.md").

### Scanning status values for Amazon ECR container

images

For an Amazon Elastic Container Registry container image, the possible
**Status** values are:

- **Actively monitoring (Continuous)** –
  Amazon Inspector is continuously monitoring and the
  image and new scans are performed on it whenever a new relevant CVE is published. The Amazon ECR rescan duration for the image is refreshed whenever the image is pushed or pulled. Enhanced scanning is enabled for the repository that stores the
  image, and the enhanced scanning setting for the repository is set to
  continuous scanning.
- **Activated (On push)** – Amazon Inspector automatically scans the image each time a new
  image is pushed. Enhanced scanning is activated for the repository that stores
  the image, and the enhanced scanning setting for the repository is set to
  scan on push.
- **Internal error** – An internal error occurred
  when Amazon Inspector attempted to scan the container image. Amazon Inspector will
  automatically address the error and resume scanning as soon as
  possible.
- **Pending initial scan** – Amazon Inspector has queued the image for
  an initial scan.
- **Scan eligibility expired (Continuous)** – Amazon Inspector suspended
  scanning for the image. The image hasn’t been updated within the duration
  that you specified for automated re-scans of images in the repository. You can push or pull the image to resume scanning.
- **Scan eligibility expired (On push)** – Amazon Inspector suspended
  scanning for the image. The image hasn’t been updated within the duration
  that you specified for automated re-scans of images in the repository. You can push the image to resume scanning.
- **Scan frequency manual (Manual)** – Amazon Inspector doesn’t scan the Amazon ECR container image. The Amazon ECR scanning setting for the
  repository that stores image is set to basic, manual scanning. To start scanning the image
  automatically with Amazon Inspector, change the repository setting to enhanced scanning, and then
  choose whether to scan images continuously or only when a new image is
  pushed.
- **Unsupported OS** – Amazon Inspector isn’t monitoring or scanning the
  image. The image is based on an operating system that Amazon Inspector doesn't support,
  or it uses a media type that Amazon Inspector doesn’t support.

For a list of operating systems that Amazon Inspector supports, see [Supported operating systems: Amazon ECR scanning with Amazon Inspector](supported.md#supported-os-ecr "supported.md#supported-os-ecr"). For
a list of media types that Amazon Inspector supports, see [Supported media types](scanning-ecr.md#ecr-supported-media "scanning-ecr.md#ecr-supported-media").

For details about configuring the scanning settings for repositories and images,
see [Amazon ECR container image scanning](scanning-ecr.md "scanning-ecr.md").

## Assessing coverage of AWS Lambda functions

The **Lambda** tab shows Lambda functions in your AWS environment. This page two tables, one that shows function coverage details for Lambda standard scanning and another for Lambda code scanning. You can group functions based on the following tabs:

- **All** – Shows all the Lambda functions in your environment.
  The **Status** column indicates the current scanning status for
  a Lambda function.
- **Scanning** – Shows the Lambda functions that Amazon Inspector is
  configured to scan. The **Status** column indicates the current
  scanning status for each Lambda function.
- **Not scanning** – Shows the Lambda functions that Amazon Inspector is
  not configured to scan. The **Reason** column indicates why
  Amazon Inspector is not monitoring and scanning a function.

A Lambda function can appear on the **Not scanning** tab for several
reasons. The Lambda function might belong to an account that hasn't been added to Amazon Inspector
or filtering rules prevent this function from being scanned. For more
information, see [Lambda function scanning](scanning-lambda.md "scanning-lambda.md").

On each tab, the **Function name** column specifies the name of the
Lambda function. The **Account** column specifies the AWS account that owns
the function. **Runtime** specifies the function's runtime. The
**Status** column indicates the current scanning status for each
Lambda function. **Resource tags** shows the tags that have been applied to
the function. The **Last scanned** column shows you when Amazon Inspector last
checked that resource for vulnerabilities. This can include checks when there is an
update to finding metadata, when there is an update to the application inventory of the
resource, or when a rescan is done in response to a new CVE. For more information, see
[Scan behaviors for Lambda function scanning](scanning-lambda.md#lambda-scan-behavior "scanning-lambda.md#lambda-scan-behavior").

### Scanning status values for AWS Lambda functions

For a Lambda function, the possible **Status** values are:

- **Actively monitoring** – Amazon Inspector is continuously monitoring
  and scanning Lambda functions. Continuous scanning includes an initial scan
  of new functions when they are pushed to the repository and automated
  re-scans of functions when they are updated or when new
  Common Vulnerabilities and Exposures (CVEs) are released.
- **Excluded by tag**– Amazon Inspector isn’t scanning this function because it has been excluded from scans by tags.
- **Scan eligibility expired**– Amazon Inspector is not monitoring this function because it has been 90 days or more since it was last invoked or updated.
- **Internal error**–An internal error occurred when
  Amazon Inspector attempted to scan the function. Amazon Inspector will automatically address the
  error and resume scanning as soon as possible.
- **Pending initial scan**– Amazon Inspector has queued the
  function for an initial scan.
- **Unsupported**– The Lambda function has an unsupported
  runtime.
