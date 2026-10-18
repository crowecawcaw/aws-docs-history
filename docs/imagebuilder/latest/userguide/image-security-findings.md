

# Manage security findings for Image Builder images
<a name="image-security-findings"></a>

When you activate security scanning with Amazon Inspector, it continuously scans machine images and running instances in your account for operating system and programming language vulnerabilities. If activated, security scanning is automatic, and Image Builder can save a snapshot of the findings from your test instance when you create a new image. Amazon Inspector is a paid service.

When Amazon Inspector discovers vulnerabilities in your software, it takes the following actions:
+ Notifies you that there was a finding.
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

If you've activated Amazon Inspector for your account, Amazon Inspector automatically scans the EC2 instances that Image Builder launches to build and test a new image. Those instances have a short lifespan during the build and test process, and their findings would normally expire as soon as those instances shut down. To help you investigate and remediate findings for your new image, Image Builder can optionally save any findings that Amazon Inspector identified on your test instance during the build process as a snapshot.

**Step 1: Activate Amazon Inspector security scans for your account**  
To activate Amazon Inspector security scans for your account from the Image Builder console, follow these steps:

1. Open the EC2 Image Builder console at [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/).

1. Choose **Security scanning settings** from the navigation pane. This opens the **Security scanning** dialog box.

   The dialog box displays the scanning status for your account. If Amazon Inspector is already activated for your account, the status shows **Enabled**.

1. Follow steps 1 and 2 of the instructions to activate Amazon Inspector scanning.
**Note**  
Amazon Inspector incurs charges. For more information, see [Amazon Inspector pricing](https://aws.amazon.com/inspector/pricing/).

If you've activated scanning for your pipeline, Image Builder takes a snapshot of the findings for your test instance when you create a new image. This way, you can access the findings after Image Builder terminates the test instance.

**Finding retention**  
Image Builder keeps the findings snapshot until you delete the image build version. For more information, see [Delete an image](delete-resources.md#delete-resources-image).

**Step 2: Configure your pipeline to save snapshots for vulnerability findings**  
To configure vulnerability finding snapshots for your pipeline, perform the following steps:

1. Open the EC2 Image Builder console at [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/).

1. Choose **Image pipelines** from the navigation pane.

1. Pick one of the following methods to specify pipeline details:

**Create a new pipeline**

   1. From the **Image pipelines** page, choose **Create image pipeline**. This opens the **Specify pipeline details** page in the pipeline wizard.

**Update an existing pipeline**

   1. From the **Image pipelines** page, choose the **Pipeline name** link for the pipeline that you want to update. This opens the pipeline detail page.
**Note**  
Alternatively, you can select the check box next to the name of the pipeline that you want to update, and then choose **View details**.

   1. From the pipeline details page, select **Edit pipeline** from the **Action** menu. This takes you to the **Edit pipeline** page.

1. In the **General** section from the pipeline wizard or the **Edit pipeline** page, select the **Enable security scan** check box.
**Note**  
If you want to turn off the snapshots later, you can edit your pipeline to clear the check box. This doesn't deactivate Amazon Inspector scanning for your account. To deactivate Amazon Inspector scanning, see [Deactivating Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/deactivating-best-practices.html) in the *Amazon Inspector User Guide*.

## Manage security findings for Image Builder images in the AWS Management Console
<a name="image-manage-security-findings"></a>

**Package vulnerability findings only**  
Image Builder saves only package vulnerability findings from Amazon Inspector. For more information, see [Understanding Amazon Inspector findings](https://docs.aws.amazon.com/inspector/latest/user/findings-understanding.html) in the *Amazon Inspector User Guide*.

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
The unique identifier for the CVE finding that Amazon Inspector detected for your image when it scanned the test instance. The ID is linked to the **Security findings > By vulnerability** page.

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

Amazon Inspector, not Image Builder, runs the scan. When you enable scanning, the `CollectImageScanFindings` step in your test workflow polls Amazon Inspector for the scan status of the test instance for an AMI-based image, or of the Amazon ECR container that Image Builder pushes to the scanning repository for a container-based image. Polling continues until the scan reaches a terminal state or the wait time ends. If the scan succeeds, Image Builder saves a one-time snapshot of the findings.

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