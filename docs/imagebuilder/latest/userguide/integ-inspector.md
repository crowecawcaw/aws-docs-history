

# Amazon Inspector integration in Image Builder
<a name="integ-inspector"></a>

Image Builder integrates with Amazon Inspector to scan the images that you build for software vulnerabilities. Amazon Inspector is a paid service.

Image Builder supports the following scan types. An AMI image or AMI pipeline uses one scan type, and you can't combine the two AMI scan types.
+ **Test instance scan** (`TEST_INSTANCE_CVE`) – For AMI images. Amazon Inspector scans the test instance that Image Builder launches during the test stage, and Image Builder saves a copy of the findings with your image. You can view the findings on the **Security findings** pages of the Image Builder console, or with the **ListImageScanFindings** API action. This scan type requires that Amazon Inspector is activated for your account. It's the default scan type for AMI images.
+ **On-demand AMI scan** (`ON_DEMAND_AMI_CVE`) – For AMI images. Amazon Inspector scans the output AMI that the build creates. This scan type doesn't require Amazon Inspector activation. You can set a scan result condition that fails the image if the AMI has findings that are more severe than you allow. You can view the results for the AMI on the Amazon EC2 console. For more information, see [Scan output AMIs with on-demand AMI scans](#integ-inspector-ami-scan).
+ **Container image scan** – For container images. Amazon Inspector scans a copy of your container image that Image Builder pushes to Amazon ECR, and Image Builder saves a copy of the findings with your image. The findings appear in the same places as test instance scan findings. This scan type requires that Amazon Inspector is activated for Amazon ECR in your account.

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

**Configure security scans**  
For test instance scans and container image scans, Image Builder saves a copy of the findings with your image so that you can investigate and remediate them after the build. Amazon Inspector scans either the test instance or the copy of your container image that Image Builder pushes to Amazon ECR. Image Builder terminates the test instance after the test stage. For on-demand AMI scans, Amazon Inspector scans the output AMI, and Image Builder doesn't save a copy of the findings.

To choose the scan type for your pipeline in the console, see [Configure security scans for Image Builder images in the AWS Management Console](image-security-findings.md#image-config-security-scans).

**Amazon Inspector activation required for test instance and container image scans**  
Test instance scans and container image scans require that Amazon Inspector is activated for your account in the AWS Region where you build your image: for Amazon EC2 (`ec2`) resources for test instance scans of AMI images, or for Amazon ECR (`ecr`) resources for container images. When a **CreateImage**, **CreateImagePipeline**, or **UpdateImagePipeline** request enables one of these scans, Image Builder checks the activation before it accepts the request. The request fails with `ResourceDependencyException` if Amazon Inspector isn't activated for the required resource type, or with `UnsupportedOperationException` if Amazon Inspector isn't available in the Region. For more information, see [Getting started tutorial: Activating Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/getting_started_tutorial.html) in the *Amazon Inspector User Guide*.  
Because Image Builder doesn't repeat the check when it runs an existing pipeline, later builds save no security findings if you deactivate Amazon Inspector for your account after you create a pipeline that has scanning enabled. For the scan status that Image Builder reports in this case, see [Image scan status and failure reasons](image-security-findings.md#image-scan-status-failure-reasons).  
On-demand AMI scans don't require Amazon Inspector activation, and Image Builder doesn't check the activation for them.

**Choose the scanning configuration for your recipe type**  
The `ecrConfiguration` field applies only to container images. For AMI images, set `imageScanningEnabled` to `true` and omit `ecrConfiguration`. To choose the scan type for an AMI image, set `imageScanningTypes`. For all scanning fields and the error that Image Builder returns if you specify `ecrConfiguration` for an AMI image, see [Create custom images with Image Builder](create-images.md). For how Amazon Inspector scans Amazon EC2 instances, see [Scanning Amazon EC2 instances with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/scanning-ec2.html) in the *Amazon Inspector User Guide*.

**Prerequisites for container image scanning**  
For a container recipe, Image Builder checks the following before it accepts the request.
+ **Amazon Inspector must be activated for Amazon ECR** – For instructions, see [Activating a scan type](https://docs.aws.amazon.com/inspector/latest/user/activate-scans.html) in the *Amazon Inspector User Guide*.
+ **A repository that you name must already exist** – If you set `repositoryName`, the Amazon ECR repository must already exist in the same account and Region, or the request fails with `ResourceNotFoundException`.
+ **A repository that you name must not use `MANUAL` scan frequency** – If the repository uses a `MANUAL` scan frequency, the request fails with `ResourceDependencyException`. Use scan on push or continuous scanning.

If you omit `repositoryName`, Image Builder uses the default repository `image-builder-image-scanning-repository` and creates it if it doesn't exist. To learn when Image Builder removes the image that it pushes, see [Create custom images with Image Builder](create-images.md).

**Review security findings**  
In the Image Builder console, you can view security findings for all of your Image Builder resources in one place. You can see all findings on the **Security findings** page in the **Security Overview** section, or you can group your findings by vulnerability, by image pipeline, or by image. The console defaults to display all security findings. The summary panel for the **All security findings** option shows the number of findings that you have for each severity level. For more information, see [Manage security findings for Image Builder images in the AWS Management Console](image-security-findings.md#image-manage-security-findings).

These pages show findings from test instance scans and container image scans. They don't show the results of on-demand AMI scans. For where to find those results, see [View on-demand AMI scan results](#integ-inspector-ami-scan-results).

To learn more about Amazon Inspector vulnerability findings, see [Understanding Amazon Inspector findings](https://docs.aws.amazon.com/inspector/latest/user/findings-understanding.html) in the *Amazon Inspector User Guide*.

Image Builder encrypts the findings snapshot for an image at rest with a KMS key that Image Builder owns.

## Scan output AMIs with on-demand AMI scans
<a name="integ-inspector-ami-scan"></a>

With an on-demand AMI scan, Amazon Inspector scans the output AMI that your build creates, instead of the test instance. You don't have to activate Amazon Inspector for your account. You can also set a scan result condition, so that the image fails if the AMI has findings that are more severe than you allow.

To request an on-demand AMI scan, set `imageScanningEnabled` to `true` and set `imageScanningTypes` to `ON_DEMAND_AMI_CVE` in the image scanning configuration. You can do this in **CreateImage**, **CreateImagePipeline**, and **UpdateImagePipeline** requests. For the fields, see [Create custom images with Image Builder](create-images.md). To configure a pipeline in the console, see [Configure security scans for Image Builder images in the AWS Management Console](image-security-findings.md#image-config-security-scans). For a AWS CLI example, see [Create an AMI image pipeline from the AWS CLI](cli-create-image-pipeline.md).

For more information about how Amazon Inspector scans machine images, see [Running on-demand machine image scans with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/machine-image-on-demand.html) in the *Amazon Inspector User Guide*.

**How on-demand AMI scans work**  
When you request `ON_DEMAND_AMI_CVE`, Image Builder adds the AWS managed `test-ami-scan` workflow to the image, unless you already list it. Image Builder adds it when you create an image and on each pipeline run. The workflow starts an Amazon Inspector scan of the output AMI. For the workflow steps, parameters, and run order, see [AMI scan managed workflow (test-ami-scan)](manage-image-workflows.md#managed-workflow-test-ami-scan).

What happens after the scan starts depends on whether you set a scan result condition:
+ **With a scan result condition** – Image Builder waits for Amazon Inspector to finish the scan, and then checks the results against your condition. If the AMI has a finding that's more severe than the condition allows, the image fails.
+ **Without a scan result condition** – Image Builder starts the scan but doesn't wait for it. The build continues, and Image Builder can distribute the image. The scan results appear in Amazon EC2 later.

**Pricing**  
Amazon Inspector charges for each successful on-demand scan. For more information, see [Amazon Inspector pricing](https://aws.amazon.com/inspector/pricing/).

To troubleshoot an image that fails because of an on-demand AMI scan, see [On-demand AMI scan fails the image](troubleshooting.md#ts-ami-scan-fails).

### Scan result conditions
<a name="integ-inspector-ami-scan-condition"></a>

Use a scan result condition to prevent Image Builder from distributing an AMI that doesn't meet your security criteria. The condition sets the highest finding severity that the output AMI can have. If the scan reports a finding with a higher severity, the image fails in the test stage, and Image Builder doesn't distribute the AMI. Specify the condition in the `scanResultCondition` field. You can use it only with `ON_DEMAND_AMI_CVE`. The condition has the following fields:
+ **maximumSeverityLabel** (string) – Required. The most severe finding that the image can have. Valid values are `INFORMATIONAL`, `LOW`, `MEDIUM`, and `HIGH`. If the AMI has a finding that's more severe, the image fails. A counted `CRITICAL` finding always fails the image.
+ **fixAvailable** (boolean) – Set to `true` to count only findings that have a fix available. Set to `false` to count every finding, including findings that have no fix available. The default is `true`.

### View on-demand AMI scan results
<a name="integ-inspector-ami-scan-results"></a>

Image Builder doesn't save on-demand AMI scan results with the image. To view the results, use the AMI ID from the output resources of the image, and do one of the following:
+ In the Amazon EC2 console, view the scan results for the AMI.
+ Call the Amazon EC2 [GetImageFindings](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetImageFindings.html) API action.

On-demand AMI scan results don't appear on the **Security findings** pages in the Image Builder console. The **ListImageScanFindings** and **ListImageScanFindingAggregations** API actions don't return them. Image Builder also doesn't set the `scanState` of the image, because `scanState` refers to test instance scans.

Amazon Inspector delivers on-demand scan findings through Amazon EventBridge, not in the Amazon Inspector console.

### Permissions for on-demand AMI scans
<a name="integ-inspector-ami-scan-permissions"></a>

On-demand AMI scans don't require an execution role. If you don't specify an execution role for the image (`executionRole`), Image Builder runs the `test-ami-scan` workflow with its service-linked role, `AWSServiceRoleForImageBuilder`. The service-linked role includes the permissions that the scan needs.

If you specify an execution role, Image Builder runs the workflow with that role. For example, you specify an execution role when you attach custom image workflows. The execution role must trust the Image Builder service principal and have the permissions for the scan. To grant the scan permissions, use one of the following options:
+ **AWS managed policy (recommended)** – Attach the EC2ImageBuilderExecutionPolicy AWS managed policy to the role. The policy includes the permissions for on-demand AMI scans. For more information, see [EC2ImageBuilderExecutionPolicy policy](security-iam-awsmanpol.md#sec-iam-manpol-EC2ImageBuilderExecutionPolicy).
+ **Custom policy** – Add the permissions in the following list to the role.

A custom execution role needs the following permissions for on-demand AMI scans:
+ `inspector2:StartOnDemandScan`, `inspector2:GetOnDemandScanStatus`, and `inspector2:ListOnDemandScans`, on the resource `arn:aws:inspector2:*:*:*`.
+ `iam:CreateServiceLinkedRole` on the resource `arn:aws:iam::*:role/*`, with the condition that `iam:AWSServiceName` is one of `ami.inspector2.amazonaws.com`, `inspector2.amazonaws.com`, or `agentless.inspector2.amazonaws.com`.
+ `ec2:DescribeImages`, which Image Builder uses to read the scan results when it checks a scan result condition.

The following example policy grants these permissions:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "inspector2:StartOnDemandScan",
                "inspector2:GetOnDemandScanStatus",
                "inspector2:ListOnDemandScans"
            ],
            "Resource": "arn:aws:inspector2:*:*:*"
        },
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "arn:aws:iam::*:role/*",
            "Condition": {
                "StringEquals": {
                    "iam:AWSServiceName": [
                        "agentless.inspector2.amazonaws.com",
                        "ami.inspector2.amazonaws.com",
                        "inspector2.amazonaws.com"
                    ]
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": "ec2:DescribeImages",
            "Resource": "*"
        }
    ]
}
```

This example covers only the permissions for the scan. The execution role also needs the permissions that Image Builder uses for the rest of the image build. For information about how to assign an execution role, see [Specify the IAM service role that Image Builder uses to run workflow actions](pipeline-workflows.md#pipeline-workflow-service-role).

If your execution role doesn't have a required permission, the `StartAmiScan` workflow step fails with an access-denied error.

### Requirements and limitations for on-demand AMI scans
<a name="integ-inspector-ami-scan-limits"></a>

On-demand AMI scans have the following requirements and limitations:
+ **AMI image recipes only** – The request must specify an `imageRecipeArn`. Image Builder rejects `ON_DEMAND_AMI_CVE` for a request that specifies a `containerRecipeArn`.
+ **Scanning must be turned on** – To use `imageScanningTypes` or `scanResultCondition`, you must set `imageScanningEnabled` to `true`.
+ **Execution role permissions** – If you specify an execution role, the role must have the permissions for the scan. If you don't specify one, Image Builder uses its service-linked role, which includes these permissions. For more information, see [Permissions for on-demand AMI scans](#integ-inspector-ami-scan-permissions).
+ **One scan type** – `imageScanningTypes` takes exactly one value. You can't combine `TEST_INSTANCE_CVE` and `ON_DEMAND_AMI_CVE`.
+ **Image tests must be turned on** – If you set `imageTestsEnabled` to `false`, the request fails with an `InvalidParameterCombinationException`.
+ **The scan targets the parent AMI if you skip the build** – If you specify `workflows` without a build workflow, Image Builder doesn't create a new AMI, and the scan targets the parent AMI of the recipe. Amazon Inspector scans only AMIs that your account owns, so your account must own the parent AMI.
+ **The scan workflow must stop on failure when you set a condition** – If you list the `test-ami-scan` workflow with `onFailure` set to `CONTINUE` and also set a `scanResultCondition`, Image Builder rejects the request.
+ **Supported operating systems** – Amazon Inspector must support the operating system of the AMI. For supported operating systems, see [Running on-demand machine image scans with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/machine-image-on-demand.html) in the *Amazon Inspector User Guide*.
+ **Console restrictions** – In the Image Builder console, you can't skip the test stage while **On-demand AMI scan** is selected. You also can't skip the build stage when your account doesn't own the parent image of the recipe, because Amazon Inspector can't scan it. For example, your account doesn't own an AWS Marketplace image or an Amazon managed image.