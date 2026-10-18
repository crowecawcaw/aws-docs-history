

# Amazon Inspector integration in Image Builder
<a name="integ-inspector"></a>

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

**Configure security scans**  
If you've activated Amazon Inspector for your account, Amazon Inspector automatically scans the EC2 instances that Image Builder launches to build and test a new image. Those instances have a short lifespan during the build and test process, and their findings would normally expire as soon as those instances shut down. To help you investigate and remediate findings for your new image, Image Builder can optionally save any findings that Amazon Inspector identified on your test instance during the build process as a snapshot.

To configure security scans for your pipeline, see [Configure security scans for Image Builder images in the AWS Management Console](image-security-findings.md#image-config-security-scans).

**Amazon Inspector activation required**  
Image scanning requires that Amazon Inspector is activated for your account in the AWS Region where you build your image: for Amazon EC2 (`ec2`) resources for AMI images, or for Amazon ECR (`ecr`) resources for container images. When a **CreateImage**, **CreateImagePipeline**, or **UpdateImagePipeline** request enables scanning, Image Builder checks the activation before it accepts the request. The request fails with `ResourceDependencyException` if Amazon Inspector isn't activated for the required resource type, or with `UnsupportedOperationException` if Amazon Inspector isn't available in the Region. For more information, see [Getting started tutorial: Activating Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/getting_started_tutorial.html) in the *Amazon Inspector User Guide*.  
Because Image Builder doesn't repeat the check when it runs an existing pipeline, later builds save no security findings if you deactivate Amazon Inspector for your account after you create a pipeline that has scanning enabled. For the scan status that Image Builder reports in this case, see [Image scan status and failure reasons](image-security-findings.md#image-scan-status-failure-reasons).

**Choose the scanning configuration for your recipe type**  
The `ecrConfiguration` field applies only to container images. For AMI images, set `imageScanningEnabled` to `true` and omit `ecrConfiguration`. For all scanning fields and the error that Image Builder returns if you specify `ecrConfiguration` for an AMI image, see [Create custom images with Image Builder](create-images.md). For how Amazon Inspector scans Amazon EC2 instances, see [Scanning Amazon EC2 instances with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/scanning-ec2.html) in the *Amazon Inspector User Guide*.

**Prerequisites for container image scanning**  
For a container recipe, Image Builder checks the following before it accepts the request.
+ **Amazon Inspector must be activated for Amazon ECR** – For instructions, see [Activating a scan type](https://docs.aws.amazon.com/inspector/latest/user/activate-scans.html) in the *Amazon Inspector User Guide*.
+ **A repository that you name must already exist** – If you set `repositoryName`, the Amazon ECR repository must already exist in the same account and Region, or the request fails with `ResourceNotFoundException`.
+ **A repository that you name must not use `MANUAL` scan frequency** – If the repository uses a `MANUAL` scan frequency, the request fails with `ResourceDependencyException`. Use scan on push or continuous scanning.

If you omit `repositoryName`, Image Builder uses the default repository `image-builder-image-scanning-repository` and creates it if it doesn't exist. To learn when Image Builder removes the image that it pushes, see [Create custom images with Image Builder](create-images.md).

**Review security findings**  
In the Image Builder console, you can view security findings for all of your Image Builder resources in one place. You can see all findings on the **Security findings** page in the **Security Overview** section, or you can group your findings by vulnerability, by image pipeline, or by image. The console defaults to display all security findings. The summary panel for the **All security findings** option shows the number of findings that you have for each severity level. For more information, see [Manage security findings for Image Builder images in the AWS Management Console](image-security-findings.md#image-manage-security-findings).

To learn more about Amazon Inspector vulnerability findings, see [Understanding Amazon Inspector findings](https://docs.aws.amazon.com/inspector/latest/user/findings-understanding.html) in the *Amazon Inspector User Guide*.

Image Builder encrypts the findings snapshot for an image at rest with a KMS key that Image Builder owns.