

# Troubleshoot Image Builder issues
<a name="troubleshooting"></a>

EC2 Image Builder integrates with AWS services for monitoring and troubleshooting to help you troubleshoot image build issues. Image Builder tracks and displays the progress for each step in the image building process. Additionally, Image Builder can export logs to an Amazon S3 location that you provide.

For advanced troubleshooting, you can run predefined commands and scripts using [AWS Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html).

**Tip**  
You can use the Troubleshoot feature, powered by AWS DevOps Agent, to diagnose failed builds and get AI-powered root cause analysis with remediation steps. For more information, see [Troubleshoot failed builds with AI - Preview](devops-agent-troubleshooting.md).

**Topics**
+ [Troubleshoot pipeline builds](#troubleshooting-pipelines)
+ [Find the cause of a failed image build with failure context](image-failure-context.md)
+ [Troubleshooting scenarios](#image-builder-troubleshooting-scenarios)
+ [Troubleshoot failed builds with AI - Preview](devops-agent-troubleshooting.md)
+ [Troubleshoot builds with an AI coding agent](agent-toolkit-skill.md)

## Troubleshoot pipeline builds
<a name="troubleshooting-pipelines"></a>

If an Image Builder pipeline build fails, Image Builder returns an error message that describes the failure. Image Builder also returns a `workflow execution ID` in the failure message, such as the one in the following example output:

```
Workflow Execution ID: '{{wf-12345abc-6789-0123-abc4-567890123abc}}' failed with reason: …
```

A failed image also carries structured failure context that names the workflow step, component step, or distribution AWS Region that caused the failure. For more information, see [Find the cause of a failed image build with failure context](image-failure-context.md).

Image Builder arranges and directs image build actions through a series of steps that are defined for the runtime stages in its standard image creation process. The build and test stages of the process each have an associated workflow. When Image Builder runs a workflow to build or test a new image, it generates a workflow metadata resource that keeps track of runtime details.

Container images have an additional workflow that runs during distribution.

**Research details for runtime instance failures for your workflow**  
To troubleshoot a runtime failure for your workflow, you can call the [GetWorkflowExecution](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetWorkflowExecution.html) and [ListWorkflowStepExecutions](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListWorkflowStepExecutions.html) API actions with your `workflow execution ID`.

**Review workflow runtime logs**
+ **Amazon CloudWatch Logs**

  Image Builder publishes detailed workflow execution logs to the following Image Builder CloudWatch Logs group and stream:

  With CloudWatch Logs, you can search log data with filter patterns. For more information, see [Search log data using filter patterns](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/SearchDataFilterPattern.html) in the *Amazon CloudWatch Logs User Guide*.
+ **AWS CloudTrail**

  All build activity is also logged in CloudTrail if it's activated in your account. You can filter CloudTrail events by the source `imagebuilder.amazonaws.com`. Alternatively, you can search for the Amazon EC2 instance ID that is returned in the execution log to see more details about the pipeline execution.
+ **Amazon Simple Storage Service (S3)**

  If you've specified an S3 bucket name and key prefix in your infrastructure configuration, the workflow step runtime log path follows this pattern:

  ```
  S3://{{S3BucketName}}/{{KeyPrefix}}/{{ImageName}}/{{ImageVersion}}/{{ImageBuildVersion}}/{{WorkflowExecutionId}}/{{StepName}}
  ```

  The logs that you send to your S3 bucket show the steps and error messages for activity on the EC2 instance during the image build process. The logs include log outputs from the component manager, the definitions of the components that were run, and the detailed output (in JSON) of all of the steps taken on the instance. If you encounter an issue, you should review these files, starting with `application.log`, to diagnose the cause of the problem on the instance.

By default, Image Builder shuts down the Amazon EC2 build or test instance that is running when the pipeline fails. You can change the instance settings for the infrastructure configuration resource that your pipeline uses, to retain your build or test instance for troubleshooting.

To change the instance settings in the console, you must clear the **Terminate instance on failure** check box located in the **Troubleshooting settings** section of your infrastructure configuration resource.

You can also change the instance settings with the **update-infrastructure-configuration** command in the AWS CLI. Set the `terminateInstanceOnFailure` value to `false` in the JSON file that the command references with the `--cli-input-json` parameter. For details, see [Update an infrastructure configuration](update-infra-config.md).

**Tip**  
For information about a sample that deploys a build that fails on purpose, with a walkthrough that shows where each failure class leaves evidence, see the [debugging sample](https://github.com/aws-samples/amazon-ec2-image-builder-samples/tree/HEAD/debugging) on GitHub. For more information, see [Explore Image Builder sample projects on GitHub](sample-projects.md).

## Troubleshooting scenarios
<a name="image-builder-troubleshooting-scenarios"></a>

This section lists the following detailed troubleshooting scenarios:
+ [Access denied – status code 403](#ts-access-denied)
+ [Build fails when the build or test instance isn't reachable through Systems Manager](#ts-timeout-ssm-agent)
+ [Windows secondary disk is offline at launch](#ts-win-disk-offline)
+ [Build fails with CIS hardened base image](#ts-cis-base)
+ [Enhanced image metadata collection fails (Systems Manager inventory association)](#ts-ssm-mult-inventory)
+ [On-demand AMI scan fails the image](#ts-ami-scan-fails)

To see the details of a scenario, choose the scenario title to expand it. You can have multiple titles expanded at the same time.

### Access denied – status code 403
<a name="ts-access-denied"></a>

#### Description
<a name="ts-access-denied-descr"></a>

The pipeline build fails with "https response error StatusCode: 403" in the failure message, followed by an "api error AccessDenied" or "api error AccessDeniedException" clause.

Older image builds might report this failure as "AccessDenied: Access Denied status code: 403".

#### Cause
<a name="ts-access-denied-cause"></a>

Possible causes include:
+ The instance profile does not have the required [permissions](set-up-ib-env.md#image-builder-IAM-prereq) to access APIs or component resources.
+ The instance profile role is missing permissions that are required for logging to Amazon S3. Most commonly, this occurs when the instance profile role does not have **PutObject** permissions for your S3 buckets.

#### Solution
<a name="ts-access-denied-solution"></a>

Depending on the cause, this issue can be resolved as follows:
+ **Instance profile is missing managed policies** – Add the missing policies to your instance profile role. Then run the pipeline again.
+ **Instance profile is missing write permissions for S3 bucket** – Add a policy to your instance profile role that grants **PutObject** permissions to write to your S3 bucket. Then run the pipeline again.

### Build fails when the build or test instance isn't reachable through Systems Manager
<a name="ts-timeout-ssm-agent"></a>

#### Description
<a name="ts-timeout-ssm-agent-descr"></a>

The pipeline build fails with a message like "An error occurred (InvalidInstanceId) when calling the SendCommand operation: Instances [[i-1234567890abcdef0]] not in a valid state for account 111122223333 in workflow step LaunchBuildInstance". When Image Builder can determine why the instance never became reachable, the failure message also includes a diagnosis. For example: "The instance never registered with Systems Manager - check that the instance profile role has AmazonSSMManagedInstanceCore and that the instance can reach SSM endpoints. For user data overrides, instances you provide, and Windows images, also confirm SSM Agent is running."

Older image builds might report this failure as "Step timed out while step is verifying the Systems Manager Agent availability on the target instance(s)".

#### Cause
<a name="ts-timeout-ssm-agent-cause"></a>

Possible causes include:
+ The instance that was launched to perform the build operations and to run components was not able to access the Systems Manager endpoint.
+ The instance profile does not have the required [permissions](set-up-ib-env.md#image-builder-IAM-prereq).

#### Solution
<a name="ts-timeout-ssm-agent-solution"></a>

Depending on the possible cause, this issue can be resolved as follows:
+ **Access issue, private subnet** – If you are building in a private subnet, make sure that you have set up PrivateLink endpoints for Systems Manager, Image Builder, and, if you want logging, Amazon S3/CloudWatch. For more information about setting up PrivateLink endpoints, see [Access AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html).
+ **Missing permissions** – Add the following managed policies to the IAM role that's associated with your instance profile:
  + EC2InstanceProfileForImageBuilder
  + EC2InstanceProfileForImageBuilderECRContainerBuilds
  + AmazonSSMManagedInstanceCore

  For more information about the permissions that Image Builder requires, see [IAM prerequisites](set-up-ib-env.md#image-builder-IAM-prereq).

### Windows secondary disk is offline at launch
<a name="ts-win-disk-offline"></a>

#### Description
<a name="ts-win-disk-offline-descr"></a>

When the instance type used to build an Image Builder Windows AMI does not match the instance type that is used to launch from the AMI, an issue can occur where non-root volumes are offline at launch. This primarily happens when the build instance is using a newer architecture than the launch instance.

The following example demonstrates what happens when an Image Builder AMI is built on an EC2 Nitro instance type and launched on an EC2 Xen instance:

**Build instance type**: m5.large (Nitro)

**Launch instance type**: t2.medium (Xen)

```
PS C:\Users\Administrator> get-disk
Number  Friendly Name  Serial Number         Health Status  Operational Status  Total Size  Partition Style
------  -------------  -------------         -------------  ------------------  ----------  ---------------
0       AWS PVDISK     vol0abc12d34e567f8a9  Healthy        Online                   30 GB  MBR
1       AWS PVDISK     vol1bcd23e45f678a9b0  Healthy        Offline                   8 GB  MBR
```

#### Cause
<a name="ts-win-disk-offline-cause"></a>

Because of Windows default settings, newly discovered disks are not automatically brought online and formatted. When the instance type is changed on EC2, Windows treats this as new disks being discovered. This is because of the underlying driver change.

#### Solution
<a name="ts-win-disk-offline-solution"></a>

We recommend that you use the same system of instance types when building your Windows AMI that you intend to launch from. Do not include instance types that are built on different systems in your infrastructure configuration. If any of the instance types you specify use the Nitro system, then they should all use the Nitro system.

For more information about instances that are built on the Nitro system, see [Instances built on the Nitro System](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#ec2-nitro-instances) in the *Amazon EC2 User Guide*.

### Build fails with CIS hardened base image
<a name="ts-cis-base"></a>

#### Description
<a name="ts-cis-base-descr"></a>

You are using a CIS hardened base image and the build fails.

#### Cause
<a name="ts-cis-base-cause"></a>

When the `/tmp` directory is classified as `noexec`, it can cause Image Builder to fail.

#### Solution
<a name="ts-cis-base-solution"></a>

Choose a different location for your working directory in the `workingDirectory` field of the image recipe. For more information, see the [ImageRecipe](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImageRecipe.html) data type description.

### Enhanced image metadata collection fails (Systems Manager inventory association)
<a name="ts-ssm-mult-inventory"></a>

#### Description
<a name="ts-ssm-mult-inventory-descr"></a>

The pipeline build fails with a message like "The Systems Manager association this step created failed (ssm:DescribeAssociationExecutions: Failed, association a1b2c3d4-5678-90ab-cdef-EXAMPLE11111) in workflow step InventoryCollection".

Older image builds might report this failure as "ssm:DescribeAssociationExecutions returned terminal state Failed in workflow step InventoryCollection", or as a failure in the `AssertInventoryCollection` step of a Systems Manager Automation.

#### Cause
<a name="ts-ssm-mult-inventory-cause"></a>

You or your organization might have created a Systems Manager State Manager association that collects inventory information for EC2 instances. If enhanced image metadata collection is enabled for your Image Builder pipeline (this is the default), Image Builder attempts to create a new inventory association for the build instance. However, Systems Manager does not allow multiple inventory associations for managed instances, so the association that Image Builder creates fails to run. This results in a failed pipeline build.

#### Solution
<a name="ts-ssm-mult-inventory-solution"></a>

To resolve this issue, turn off enhanced image metadata collection, using one of the following methods:
+ Update your image pipeline in the console, to clear the **Enable enhanced metadata collection** check box. Save your changes and run a pipeline build.

  For more information about updating your AMI image pipeline using the EC2 Image Builder console, see [Update AMI image pipelines in the console](update-image-pipeline-console.md). For more information about updating your container image pipeline using the EC2 Image Builder console, see [Update a container image pipeline in the console](update-container-pipeline-console.md).
+ You can also update your image pipeline with the **update-image-pipeline** command in the AWS CLI. To do this, include the `EnhancedImageMetadataEnabled` property in your JSON file, set to `false`. The following example shows the property set to `false`.

  ```
  {
      "name": "{{MyWindows2019Pipeline}}",
      "description": "{{Builds Windows 2019 Images}}",
      "enhancedImageMetadataEnabled": {{false}},
      "imageRecipeArn": "arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:image-recipe/{{my-example-recipe}}/2020.12.03",
      "infrastructureConfigurationArn": "arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:infrastructure-configuration/{{my-example-infrastructure-configuration}}",
      "distributionConfigurationArn": "arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:distribution-configuration/{{my-example-distribution-configuration}}",
      "imageTestsConfiguration": {
          "imageTestsEnabled": true,
          "timeoutMinutes": 60
      },
      "schedule": {
          "scheduleExpression": "cron(0 0 * * SUN *)",
          "pipelineExecutionStartCondition": "EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE"
      },
      "status": "ENABLED"
  }
  ```

To prevent this from happening for new pipelines, clear the **Enable enhanced metadata collection** check box when you create a new pipeline using the EC2 Image Builder console, or set the value of the `EnhancedImageMetadataEnabled` property in your JSON file to `false` when you create your pipeline using the AWS CLI.

### On-demand AMI scan fails the image
<a name="ts-ami-scan-fails"></a>

#### Description
<a name="ts-ami-scan-fails-descr"></a>

An image that requests an on-demand AMI scan fails in the test stage. The failure message names the workflow step of the `test-ami-scan` workflow that failed: the `StartAmiScan`, `WaitForAmiScan`, or `EvaluateScanResultCondition` workflow step.

#### Cause
<a name="ts-ami-scan-fails-cause"></a>

The image can fail for one of the following reasons:
+ **Access denied** – The execution role that you specified doesn't have the permissions that the scan needs, so the `StartAmiScan` workflow step fails with an access-denied error. For example, the role isn't allowed to call `inspector2:StartOnDemandScan`, or `iam:CreateServiceLinkedRole` for `ami.inspector2.amazonaws.com`.
+ **The scan wait timed out** – In the `WaitForAmiScan` workflow step, Amazon Inspector didn't finish the scan within the wait time. The scan might still be running.
+ **Amazon Inspector couldn't scan the AMI** – In the `WaitForAmiScan` workflow step, Amazon Inspector reports that the scan failed. The failure message includes the reason code in parentheses.
+ **The scan results weren't available** – In the `EvaluateScanResultCondition` workflow step, Amazon EC2 didn't have the Amazon Inspector scan results for the AMI within 15 minutes. Image Builder couldn't check the results against the scan result condition.
+ **The AMI breached the scan result condition** – In the `EvaluateScanResultCondition` workflow step, the most severe finding exceeds `maximumSeverityLabel`. If `fixAvailable` is `true`, Image Builder counts only findings that have a fix available. The failure message names the severity and the AMI ID.

#### Solution
<a name="ts-ami-scan-fails-solution"></a>

When you retry a failed image or run the pipeline again, Image Builder starts a new scan. Before you retry, fix the cause:
+ **Access denied** – Attach the EC2ImageBuilderExecutionPolicy AWS managed policy to your execution role, or add the missing permissions to the role. If the image doesn't need an execution role for other features, such as custom image workflows, you can omit the execution role. Image Builder then runs the scan with its service-linked role. For the permissions, see [Permissions for on-demand AMI scans](integ-inspector.md#integ-inspector-ami-scan-permissions).
+ **The scan wait timed out** – Retry the image, or increase the `WaitForAmiScanTimeoutSeconds` parameter of the `test-ami-scan` workflow, up to 43,500 seconds. If the scan keeps timing out, contact Support. For the parameter, see [AMI scan managed workflow (test-ami-scan)](manage-image-workflows.md#managed-workflow-test-ami-scan).
+ **Amazon Inspector couldn't scan the AMI** – Use the reason code in the failure message:
  + `UNSUPPORTED_OS` – Amazon Inspector doesn't support the operating system of the AMI. For supported operating systems, see [Running on-demand machine image scans with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/machine-image-on-demand.html) in the *Amazon Inspector User Guide*.
  + `ACCESS_DENIED` – Amazon Inspector couldn't access the AMI, or the KMS key that encrypts it. Check the Amazon Inspector service-linked roles and the key policy. Also check that the key isn't in another account, and doesn't have the `InspectorEc2Exclusion` tag.
  + `RESOURCE_TERMINATED` – The AMI or one of its snapshots no longer existed when Amazon Inspector tried to finish the scan. Keep the AMI and its snapshots until the scan finishes.
  + `STORAGE_LIMIT_EXCEEDED` – The AMI exceeds the Amazon Inspector per-AMI scan quota of 8 snapshots or 1,200 GiB. Reduce the number or size of the snapshots.
  + `EXTRACTION_COLLECTION_TIME_LIMIT_EXCEEDED` – The Amazon Inspector scan timed out. Retry the image.
  + `INTERNAL_ERROR` – Retry the image.
+ **The scan results weren't available** – Retry the image. If the problem continues, contact Support.
+ **The AMI breached the scan result condition** – To review the findings, call the Amazon EC2 [GetImageFindings](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetImageFindings.html) API action with the AMI ID from the failure message. Remediate the findings, for example, by updating your components or the parent image. Alternatively, change the scan result condition. For more information, see [Scan result conditions](integ-inspector.md#integ-inspector-ami-scan-condition).