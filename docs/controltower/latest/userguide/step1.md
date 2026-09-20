

# Step 1. Launch the stack
<a name="step1"></a>

The CloudFormation template in this section deploys *Customizations for AWS Control Tower* (CfCT) in your account.

**Note**  
You are responsible for the cost of the AWS services used while you run CfCT. For more details, see [Cost](cost.md).

1. To launch *Customizations for AWS Control Tower*, [download the template from GitHub](  https://github.com/aws-solutions/aws-control-tower-customizations/blob/main/customizations-for-aws-control-tower.template) and then launch it from [AWS CloudFormation](https://console.aws.amazon.com/cloudformation/home?region=us-east-1).

1. The template launches in the US East (N. Virginia) Region by default. To launch CfCT in a different AWS Region, use the Region selector in the console navigation bar.
**Note**  
CfCT must be launched in the same Region and account where you deployed your AWS Control Tower landing zone, which is your home Region.

1. On the **Create stack** page, verify that the correct template URL shows in the ** URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your CfCT stack.

1. Under **Parameters**, review the following parameters and modify them in the template, if necessary.


<table>
<thead>
  <tr><th colspan="3">Pipeline Configuration</th><th></th><th></th><th></th><th></th><th></th><th></th></tr>
  <tr><th>Parameter</th><th>Default</th><th>Description</th><th></th><th></th><th></th><th></th><th></th><th></th></tr>
  <tr><th colspan="3">AWS CodeCommit Setup</th><th></th><th></th><th></th><th></th><th></th><th></th></tr>
  <tr><th>Parameter</th><th>Default</th><th>Description</th><th></th><th></th><th></th><th></th><th></th><th></th></tr>
  <tr><th colspan="3">CloudFormation StackSets Configuration</th><th></th><th></th><th></th><th></th><th></th><th></th></tr>
  <tr><th>Parameter</th><th>Default</th><th>Description</th><th></th><th></th><th></th><th></th><th></th><th></th></tr>
</thead>
<tbody>
  <tr><td><b>Pipeline Approval Stage</b></td><td><code>No</code></td><td>Choose whether to change the pipeline configuration from the default automated approval stage to a manual approval stage. For more information, see <a href="cfct-customizations-dev-guide.md">CfCT customization guide</a>.</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td><b>Pipeline Approval Email Address</b></td><td>&lt;Optional Input&gt;</td><td>The email address for approval notifications. To use this parameter, you must set the <b>Pipeline Approval Stage</b> parameter to <code>Yes</code>.</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td><b>AWS CodePipeline Source</b></td><td><code>Amazon S3</code></td><td>The source for AWS CodePipeline to help you select where to store and configure the CfCT customizations.</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td><b>Existing CodeCommit Repository?</b></td><td><code>No</code></td><td>Choose whether to use an existing CodeCommit Git repository. If you choose <code>Yes</code>, you must set the <b>CodePipeline Source</b> parameter to <code>AWS CodeCommit</code>.</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td><b>CodeCommit Repository Name</b></td><td><code>custom-control-tower-configuration</code></td><td>If you provide the name of an existing Git repository, you must set the <b>Existing CodeCommit Repository?</b> parameter to <code>Yes</code> and enter the exact name of that repository.</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td><b>CodeCommit Branch Name</b></td><td><code>main</code></td><td>The Git branch where the customization package is stored. To use this parameter, you must set the <b>CodePipeline Source</b> parameter to <code>AWS CodeCommit</code>.</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td><b>Region Concurrency Type</b></td><td><code>PARALLEL</code></td><td>Select the concurrency type of deploying StackSets operations in Regions. This setting is applicable for create, update, and delete workflows. Other allowed value is <code>SEQUENTIAL</code>.</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td><b>Max Concurrent Percentage</b></td><td><code>100</code></td><td>The maximum percentage of accounts in which to perform this operation at one time. The max allowed value is 100. For more information, refer to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-ops-options">Stack Set operation options</a>. </td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td><b>Failure Tolerance Percentage</b></td><td><code>10</code></td><td>The percentage of accounts, per Region, for which this stack operation can fail before AWS CloudFormation stops the operation in that Region. The minimum allowed value is 0 and max allowed value is 100. For more information, refer to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-ops-options">Stack Set operation options</a>.</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
</tbody>
</table>


1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Be sure to check the box acknowledging that the template will create AWS Identity and Access Management (IAM) resources.

1. Choose **Create stack** to deploy the stack.

   You can view the status of the stack in the CloudFormation console in the **Status** column. You should see a status of **CREATE\_COMPLETE** in approximately 15 minutes.