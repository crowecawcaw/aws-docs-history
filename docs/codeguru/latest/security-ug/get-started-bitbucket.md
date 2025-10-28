On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# Integrate with Bitbucket

The following steps show how to integrate Amazon CodeGuru Security into your Bitbucket pipeline. After you
complete the setup, CodeGuru Security will scan your repository whenever you push to the
`main` branch, or you can customize the workflow to your organization's needs. After
a scan completes, you will be able to see findings on the Findings page in the CodeGuru Security
console.

You can also complete these steps on the **Integrations** page in the [CodeGuru Security console](https://console.aws.amazon.com/codeguru/security/integrations "https://console.aws.amazon.com/codeguru/security/integrations"). Choose
**Integrate with Bitbucket** to get started.

## Step 1: Create an IAM role

To allow CodeGuru Security to integrate with Bitbucket, create an IAM role with sufficient
permissions. You can create an AWS CloudFormation stack that sets up a role for you, or manually configure
a role.

To manually configure an IAM role for Bitbucket, see [Deploy on AWS using Bitbucket Pipelines OpenID Connect](https://support.atlassian.com/bitbucket-cloud/docs/deploy-on-aws-using-bitbucket-pipelines-openid-connect/ "https://support.atlassian.com/bitbucket-cloud/docs/deploy-on-aws-using-bitbucket-pipelines-openid-connect/") in the Bitbucket Support
documentation. You can attach the AWS managed policy [AmazonCodeGuruSecurityScanAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonCodeGuruSecurityScanAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonCodeGuruSecurityScanAccess") to configure your role with the minimum necessary
permissions to integrate with Bitbucket.

If you have already configured a role to use CodeGuru Security with the Bitbucket repository you want
to scan, you can skip to step 2.

###### Create a role with a CloudFormation stack

Complete the following steps to create a CloudFormation stack that sets up an IAM role with
the necessary permissions attached to integrate with Bitbucket.

1. Open the **Integrations** page in the
   [CodeGuru Security
   console](https://console.aws.amazon.com/codeguru/security/integrations "https://console.aws.amazon.com/codeguru/security/integrations") and choose **Integrate with Bitbucket**.
2. For **Step 1: Create an IAM role**, choose
   **Use CloudFormation template**. Then choose
   **Open template in CloudFormation** to be redirected to the
   Create stack page in the CloudFormation console.
3. For **Stack name**, enter a unique name for your stack.
4. For **Parameters**, for **Audience**, enter the
   Audience of the repository you want to scan. For **ProviderUrl**, enter the
   Identity provider URL of the repository you want to scan.

These values can be found in your Bitbucket account under **Repository
settings**. Go to **Pipelines: OpenID Connect** and then
**Identity provider**. 5. Check the box to acknowledge that AWS CloudFormation might create IAM resources with custom
names. This allows CloudFormation to create a role for you. 6. Choose **Create stack**. CloudFormation creates a role called
`CodeGuruSecurityBitbucketAccessRole`. Continue to the next step.

## Step 2: Configure Bitbucket pipelines

Complete the following steps to update your Bitbucket pipeline to include steps and actions
to run CodeGuru Security scans. The following pipeline will initiate security scans every time you push
code to the `main` branch of the repository you are integrating with. If CodeGuru Security
detects a critical finding, the pipeline build will fail.

1. Log in to your [Bitbucket account](https://bitbucket.org/ "https://bitbucket.org/").
2. Open the repository that you want to scan.
3. Choose the **Source** tab.
4. If you don't have a pipeline YAML file yet, choose **Add file** and name
   it `bitbucket-pipelines.yml`.

If you have already set up a pipeline YAML file, choose **Edit**. 5. Paste the following code into the `bitbucket-pipelines.yml` file editor in
Bitbucket. You can modify the events defined in this file based on your use case.

Replace `accountID` with the AWS account ID of the account
that is assuming the role and `region` with the region where you are
running scans. If you manually configured a role, replace
`CodeGuruSecurityBitbucketAccessRole` with the name of the role you
created to integrate with Bitbucket.

If you want to add code quality findings to your scan, add `--analysis_type
 All` to the `python` script line after `--fail_on_severity
 Critical`.

```
pipelines:
  branches:
    master:
    - step:
        image: public.ecr.aws/l6c8c5q3/codegurusecurity-actions-public:latest
        oidc: true
        script:
          - export AWS_ROLE_ARN=arn:aws:iam::`accountID`:role/`CodeGuruSecurityBitbucketAccessRole`
          - export AWS_WEB_IDENTITY_TOKEN_FILE=$(pwd)/web-identity-token
          - echo $BITBUCKET_STEP_OIDC_TOKEN > $(pwd)/web-identity-token
          - python /usr/app/codeguru/command.py --source_path . --aws_region `region` --scan_name CGS-Bitbucket-$BITBUCKET_REPO_SLUG --fail_on_severity Critical
          - cat codeguru-security-results.sarif.json

```

6. Choose **Commit** to commit your changes.

## Step 3: Run scans and address findings

After updating the pipeline, CodeGuru Security will scan your code based on the events that you
have defined in the YAML file. If you configured your pipeline to initiate scans on code
commits, CodeGuru Security will automatically scan your code whenever you push to the specified
branch.

You can view your findings in the CodeGuru Security console. To address findings, update your code
based on the suggested remediations, and then push your changes. CodeGuru Security will scan the updated
code based on the events that you have defined in the YAML file, and you can check that the
vulnerabilities were remediated.
