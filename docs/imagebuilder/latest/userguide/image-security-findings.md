

# Manage security findings for Image Builder images
<a name="image-security-findings"></a>

Image Builder integrates with Amazon Inspector to scan the images that you build for software vulnerabilities. Amazon Inspector is a paid service.

Image Builder supports the following scan types. An AMI image or AMI pipeline uses one scan type, and you can't combine the two AMI scan types.
+ **Test instance scan** (`TEST_INSTANCE_CVE`) – For AMI images. Amazon Inspector scans the test instance that Image Builder launches during the test stage, and Image Builder saves a copy of the findings with your image. You can view the findings on the **Security findings** pages of the Image Builder console, or with the **ListImageScanFindings** API action. This scan type requires that Amazon Inspector is activated for your account. It's the default scan type for AMI images.
+ **On-demand AMI scan** (`ON_DEMAND_AMI_CVE`) – For AMI images. Amazon Inspector scans the output AMI that the build creates. This scan type doesn't require Amazon Inspector activation. You can set a scan result condition that fails the image if the AMI has findings that are more severe than you allow. You can view the results for the AMI on the Amazon EC2 console. For more information, see [Scan output AMIs with on-demand AMI scans](integ-inspector.md#integ-inspector-ami-scan).
+ **Container image scan** – For container images. Amazon Inspector scans a copy of your container image that Image Builder pushes to Amazon ECR, and Image Builder saves a copy of the findings with your image. The findings appear in the same places as test instance scan findings. This scan type requires that Amazon Inspector is activated for Amazon ECR in your account.

The information in this topic about findings management, retention, and scan status applies to test instance scans and container image scans, because Image Builder saves the findings for these scan types. For the results of an on-demand AMI scan, see [View on-demand AMI scan results](integ-inspector.md#integ-inspector-ami-scan-results).

When Amazon Inspector discovers vulnerabilities in your software, it takes the following actions:
+ Sends an event to Amazon EventBridge for each finding.
+ Rates the severity of the finding. The severity rating categorizes vulnerabilities to help you prioritize your findings, and includes the following values:
  + Untriaged
  + Informational
  + Low
  + Medium
  + High
  + Critical
+ Provides information about the finding, and links to additional resources for more detail.
+ Offers remediation guidance to help you resolve the issues that generated the finding.

## Configure security scans for Image Builder images in the AWS Management Console
<a name="image-config-security-scans"></a>

For test instance scans and container image scans, Image Builder saves a copy of the findings with your image so that you can investigate and remediate them after the build. Amazon Inspector scans either the test instance or the copy of your container image that Image Builder pushes to Amazon ECR. Image Builder terminates the test instance after the test stage. For on-demand AMI scans, Amazon Inspector scans the output AMI, and Image Builder doesn't save a copy of the findings.

In the AWS Management Console, you choose the scan type in the settings of an image pipeline. The console doesn't offer scan settings for images that you create outside a pipeline. To configure scanning with the AWS CLI or the Image Builder API, see the image scanning settings in [Create custom images with Image Builder](create-images.md), and the pipeline examples in [Create an AMI image pipeline from the AWS CLI](cli-create-image-pipeline.md).

**Step 1: Activate Amazon Inspector security scans for your account**  
Test instance scans and container image scans require that Amazon Inspector is activated for your account. On-demand AMI scans don't. If you use only on-demand AMI scans, skip to Step 2. To activate Amazon Inspector from the Image Builder console, follow these steps:

1. Open the EC2 Image Builder console at [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/).

1. Choose **Security scanning settings** from the navigation pane.

   The **Security scanning settings** page shows whether **EC2 security scanning** and **ECR security scanning** are enabled for your account.

1. Choose **Launch Amazon Inspector** to open the Amazon Inspector account management page.

1. Select your account, and then choose **Enable** for the type of scanning that you want to activate.
**Note**  
Amazon Inspector incurs charges. For more information, see [Amazon Inspector pricing](https://aws.amazon.com/inspector/pricing/).

If your pipeline uses test instance scans, Image Builder takes a snapshot of the findings for your test instance when it creates a new image. This way, you can access the findings after Image Builder terminates the test instance.

**Finding retention**  
Image Builder keeps the findings snapshot until you delete the image build version. For more information, see [Delete an image](delete-resources.md#delete-resources-image).

**Step 2: Choose the scan type for your pipeline**  
To choose the scan type when you create or edit a pipeline, follow these steps:

1. Open the EC2 Image Builder console at [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/).

1. Choose **Image pipelines** from the navigation pane.

1. Do one of the following:
   + To create a pipeline, choose **Create image pipeline**.
   + To update a pipeline, select the checkbox next to the pipeline name, and then choose **Edit pipeline** from the **Actions** menu.

1. In the **Advanced settings** section, choose the scan type:
   + For an AMI image recipe, for **EC2 image scanning**, choose **Instance scan** or **On-demand AMI scan**. To turn off scanning, choose **Disabled**. **Instance scan** is available only when Amazon Inspector is activated for Amazon EC2 in your account.
   + For a container recipe, for **ECR container scanning**, choose **Enabled**. This setting is available only when Amazon Inspector is activated for Amazon ECR in your account.

1. If you chose **On-demand AMI scan**, set the following options:
   + For **Maximum allowed severity**, choose the most severe finding that the image can have: **High**, **Medium**, **Low**, or **Informational**. If the AMI has a more severe finding, the image fails. A critical finding always fails the image. The exception is a critical finding that has no fix available when you count only findings that have a fix. To scan without failing the image, choose **Any severity (don't fail the build)**, which is the default. With this choice, the pipeline has no scan result condition.
   + (Optional) To also count findings that don't have a fix available, clear the **Ignore findings that don't have a fix available yet** checkbox. The console selects this checkbox by default and shows it when you choose a severity other than **Any severity (don't fail the build)**.
   + (Optional) In the **Test** section, for the `test-ami-scan` workflow, enter a value for `WaitForAmiScanTimeoutSeconds`. For the valid values, see [AMI scan managed workflow (test-ami-scan)](manage-image-workflows.md#managed-workflow-test-ami-scan).

1. Choose **Create pipeline**, or **Save changes**.

An on-demand AMI scan doesn't require an execution role. When you create or edit the pipeline, you can choose an IAM role that Image Builder uses to run workflow actions. If you do, the role must have the permissions for the scan. For more information, see [Specify the IAM service role that Image Builder uses to run workflow actions](pipeline-workflows.md#pipeline-workflow-service-role). For the permissions that the role needs, see [Permissions for on-demand AMI scans](integ-inspector.md#integ-inspector-ami-scan-permissions).

When you choose **On-demand AMI scan**, the **Test** section shows the AWS managed `test-ami-scan` workflow as a locked row labeled **Required for AMI scan**. You can't select this workflow yourself. If you change **EC2 image scanning** to another value, the console removes the workflow. For more information about how the scan works, see [Scan output AMIs with on-demand AMI scans](integ-inspector.md#integ-inspector-ami-scan).

**Console restrictions for on-demand AMI scans**  
While **On-demand AMI scan** is selected, you can't skip the test workflows. You also can't skip the build workflow when your account doesn't own the parent image of the recipe, because Amazon Inspector can't scan it. For example, your account doesn't own an AWS Marketplace image or an Amazon managed image. The **On-demand AMI scan** option isn't offered for container recipes.

The **Image pipelines** page also has **Enable security findings** and **Disable security findings** actions. **Enable security findings** sets the pipeline to scan without a scan type, which uses a test instance scan for an AMI pipeline. **Disable security findings** turns off scanning. Both actions replace an on-demand AMI scan configuration, and remove the `test-ami-scan` workflow from the pipeline.

Turning off scanning for a pipeline doesn't deactivate Amazon Inspector scanning for your account. To deactivate Amazon Inspector scanning, see [Deactivating Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/deactivating-best-practices.html) in the *Amazon Inspector User Guide*.

## Manage security findings for Image Builder images in the AWS Management Console
<a name="image-manage-security-findings"></a>

**Package vulnerability findings only**  
Image Builder saves only package vulnerability findings from Amazon Inspector. For more information, see [Understanding Amazon Inspector findings](https://docs.aws.amazon.com/inspector/latest/user/findings-understanding.html) in the *Amazon Inspector User Guide*.

The **Security findings** pages show the findings that Image Builder saves from test instance scans and container image scans.

The **Security findings** list pages display high-level information about the findings for your resources, with views based on several different filters that you can apply. Each view includes the following options at the top to change your view:
+ **All security findings** – This is the default view if you choose **Security findings** page from the navigation pane in the Image Builder console.
+ **By vulnerability** – This view shows a high-level list of all of the image resources in your account that have findings. The **Finding ID** is linked to more detailed information about the finding. This information appears on a panel that opens on the right side of the page. The panel includes the following information:
  + A detailed description of the finding.
  + A **Finding details** tab. This tab includes a finding overview, affected packages, summary remediation advice, vulnerability details, and related vulnerabilities. The **Vulnerability ID** links to detailed vulnerability information in the National Vulnerability Database.
  + A **Score breakdown** tab. This tab includes a side-by-side comparison of the CVSS and Amazon Inspector scores so that you can see where Amazon Inspector has modified a score, if applicable.
+ **By image pipeline** – This view shows the number of findings for each image pipeline in your account. Image Builder displays counts for medium severity and higher findings, plus a total for all findings. All data in the list is linked, as follows:
  + The **Image pipeline name** column links to the detail page for the specified image pipeline.
  + The severity level column links open the **All security findings** view, filtered by the associated image pipeline name and severity level.

  You can also use search criteria to refine your results.
+ **By image** – This view shows the number of findings for each image build in your account. Image Builder displays counts for medium severity and higher findings, plus a total for all findings. All data in the list is linked, as follows:
  + The **Image name** column links to the image detail page for the specified image build. For more information, see [View image resource details](view-image-details.md).
  + The severity level column links open the **All security findings** view, filtered by the associated image build name and severity level.

  You can also use search criteria to refine your results.

Image Builder shows the following details in the **Findings** list section of the default **All security findings** view.

**Severity**  
The severity level of the CVE finding. Values are as follows:  
+ Untriaged
+ Informational
+ Low
+ Medium
+ High
+ Critical

**Finding ID**  
The unique identifier for the CVE finding that Amazon Inspector detected for your image when it scanned the test instance or the container image. The ID is linked to the **Security findings > By vulnerability** page.

**Image ARN**  
The Amazon Resource Name (ARN) for the image with the finding specified in the **Finding ID** column.

**Pipeline**  
The pipeline that built the image specified in the **Image ARN** column.

**Description**  
A short description of the finding.

**Inspector score**  
The score that Amazon Inspector assigned for the CVE finding.

**Remediation**  
Links to details about the recommended course of action to remediate the finding.

**Published date**  
The date and time when this vulnerability was first added to the vendor's database.

## Image scan status and failure reasons
<a name="image-scan-status-failure-reasons"></a>

This section applies to test instance scans and container image scans. For an image that fails because of an on-demand AMI scan, see [On-demand AMI scan fails the image](troubleshooting.md#ts-ami-scan-fails).

Amazon Inspector, not Image Builder, runs the scan. For a test instance scan or a container image scan, the `CollectImageScanFindings` step in your test workflow polls Amazon Inspector for the scan status of the test instance for an AMI-based image, or of the Amazon ECR container that Image Builder pushes to the scanning repository for a container-based image. Polling continues until the scan reaches a terminal state or the wait time ends. If the scan succeeds, Image Builder saves a one-time snapshot of the findings.

Image Builder treats the following Amazon Inspector reasons as terminal. When Amazon Inspector returns one, Image Builder stops polling, sets the image scan status to `FAILED`, and records the reason unchanged. For all reasons, see the [ScanStatus](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ScanStatus.html) data type in the *Amazon Inspector API Reference*.

`ACCESS_DENIED`  
**Cause** – A resource access policy restricts Amazon Inspector (not Image Builder) access to the scanned resource.  
**Resolution** – Update the IAM or resource policy that denies Amazon Inspector access, then build a new image.

`INTERNAL_ERROR`  
**Cause** – Amazon Inspector encountered an internal error for the scanned resource.  
**Resolution** – Build a new image to scan again.

`UNSUPPORTED_OS`  
**Cause** – Amazon Inspector doesn't support the operating system, architecture, or image manifest type of the scanned resource.  
**Resolution** – Build from a parent image that Amazon Inspector supports. For the list of supported operating systems, see [Supported operating systems and programming languages for Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/supported.html) in the *Amazon Inspector User Guide*.

If the scan doesn't reach a terminal state in time, Image Builder sets the image scan status to `FAILED` with the reason `UNKNOWN`. By default, Image Builder waits 15 minutes for the scan. If the `CollectImageScanFindings` step sets `timeoutSeconds`, that value limits the whole step instead, including the wait for the scan. When the default wait ends, Image Builder also writes a message to the image's log group in CloudWatch Logs that says the image scan didn't finish. For the log group names, see [Monitor Image Builder logs with Amazon CloudWatch Logs](monitor-cwlogs.md).

The scan also ends this way in the following cases, because Amazon Inspector reports no coverage for the resource:
+ Amazon Inspector isn't activated for your account when the build runs.
+ The scanned resource is terminated before the scan completes.

**Failed scans can't be repeated**  
After a scan fails, Image Builder can't scan the same image again, even if the `CollectImageScanFindings` step has a `retry` attribute. To scan again, build a new image.