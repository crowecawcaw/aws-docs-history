On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# Integrate with AWS CodePipeline

The following steps show how to set up AWS CodePipeline with Amazon CodeGuru Security. After you set up, code
scans are automated and you can view findings on the Findings page in the CodeGuru Security
console.

You can also complete these steps on the **Integrations** page in the [CodeGuru Security console](https://console.aws.amazon.com/codeguru/security/integrations "https://console.aws.amazon.com/codeguru/security/integrations"). Choose
**Integrate with AWS CodePipeline** to get started.

## Step 1: Create CodeBuild project

Complete the following steps to create an AWS CloudFormation stack that sets up a CodeGuru Security CodeBuild
project. This authorizes CodeGuru Security to discover your repositories and run security scans
whenever you create a pull request.

1. Open the **Integrations** page in the
   [CodeGuru Security
   console](https://console.aws.amazon.com/codeguru/security/integrations "https://console.aws.amazon.com/codeguru/security/integrations") and choose **Integrate with AWS CodePipeline**.
2. For **Step 1: Create an IAM role**, choose
   **Open template in CloudFormation** to be redirected to the
   Create stack page in the CloudFormation console.
3. For **Stack name**, enter a unique name for your stack.
4. Check the box to acknowledge that AWS CloudFormation might create IAM resources with custom
   names. This allows CloudFormation to create a CodeGuru Security CodeBuild project.
5. Choose **Create stack**. Continue to the next step.

## Step 2: Add step to CodePipeline

Complete the following steps to add CodeGuru Security as a step in your CodePipeline.

1. Open the [AWS CodePipeline console](https://console.aws.amazon.com/codesuite/codepipeline/pipelines "https://console.aws.amazon.com/codesuite/codepipeline/pipelines").
2. Choose the pipeline you want to scan.
3. Choose **Edit**.
4. Choose **Add stage** and enter a stage name.
5. For the stage you just created, choose **Add action group**.
6. For Action provider, choose **CodeBuild**.
7. For Input artifacts, choose **SourceArtifact**.
8. For Project name, choose **CodeGuruSecurity**.
9. Choose **Done**.
10. Choose **Save**.

## Step 3: Run scans and address findings

After you add CodeGuru Security to your CodePipeline pipeline, CodeGuru Security will run scans
on every pipeline deployment. You can view scans and findings in the CodeGuru Security
console.

To address findings, update your code based on the suggested remediation, and then push
your changes to the pipeline where you added CodeGuru Security as a step. CodeGuru Security will automatically
scan the updated code and you can check that the vulnerabilities were remediated.
