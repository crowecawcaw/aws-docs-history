On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# Integrate with GitLab

The following steps show how to integrate Amazon CodeGuru Security into your GitLab CI/CD workflow. After
you complete the setup, CodeGuru Security will scan your repository whenever you push to the
`main` branch, or you can customize the workflow to your organization's needs. After
a scan completes, you will be able to see findings in the **Vulnerability
report** page on GitLab and on the Findings page in the CodeGuru Security console.

You can also complete these steps on the **Integrations** page in the [CodeGuru Security console](https://console.aws.amazon.com/codeguru/security/integrations "https://console.aws.amazon.com/codeguru/security/integrations"). Choose
**Integrate with GitLab** to get started.

## Step 1: Create an IAM role

To allow CodeGuru Security to integrate with GitLab, create an IAM role with sufficient
permissions. You can create an AWS CloudFormation stack that sets up a role for you, or manually configure a role.

To manually configure an IAM role for GitLab, see
[Configure OpenID Connect in AWS
to retrieve temporary credentials](https://docs.gitlab.com/ee/ci/cloud_services/aws/ "https://docs.gitlab.com/ee/ci/cloud_services/aws/") in the GitLab Docs. You can attach
the AWS managed policy [AmazonCodeGuruSecurityScanAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonCodeGuruSecurityScanAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonCodeGuruSecurityScanAccess") to configure your role with the minimum
necessary permissions to integrate with GitLab.

If you have already configured a role to use CodeGuru Security with the GitLab repository you want
to scan, you can skip to step 2.

###### Create a role with a CloudFormation stack

Complete the following steps to create a CloudFormation stack that sets up an IAM role with
the necessary permissions attached to integrate with GitLab.

1. Open the **Integrations** page in the
   [CodeGuru Security
   console](https://console.aws.amazon.com/codeguru/security/integrations "https://console.aws.amazon.com/codeguru/security/integrations") and choose **Integrate with GitLab**.
2. For **Step 1: Create an IAM role**, choose
   **Use CloudFormation template**. Then choose
   **Open template in CloudFormation** to be redirected to the
   Create stack page in the CloudFormation console.
3. For **Stack name**, enter a unique name for your stack.
4. For **Parameters**, for **Group**, enter the name of
   the group that contains your project. For **Project**, enter the name of the
   project you want to scan.
5. Check the box to acknowledge that AWS CloudFormation might create IAM resources with custom
   names. This allows CloudFormation to create a role for you.
6. Choose **Create stack**. CloudFormation creates a role called
   `CodeGuruSecurityGitLabAccessRole`. Continue to the next step.

## Step 2: Configure your CI/CD workflow

Complete the following steps to configure your GitLab CI/CD workflow and to define the jobs
that make up your pipeline to run CodeGuru Security scans. This pipeline will initiate security scans
every time you push code to the `main` branch of the repository you are integrating
with. If CodeGuru Security detects a critical finding, the pipeline build will fail.

1. Log in to your [GitLab account](https://about.gitlab.com/ "https://about.gitlab.com/").
2. Open the project that you want to scan.
3. Choose the **Set up CI/CD**.
4. Choose **Configure pipeline**.
5. Paste the following code into the `.gitlab-ci.yml` file editor in GitLab. You can modify the events
   defined in this file based on your use case.

Replace `accountID` with the AWS account ID of the account that is
assuming the role and `region` with the region where you are running
scans. Replace `CodeGuruSecurityGitLabAccessRole` with the name of
the role you created to integrate with GitLab.

If you want to add code quality findings to your scan, add `--analysis_type
 All` to the `python` script line after `--fail_on_severity
 Critical`.

```
codeguru_security_example:
  image:
    name: public.ecr.aws/l6c8c5q3/codegurusecurity-actions-public:latest
    entrypoint: [""]
  variables:
    ROLE_ARN: arn:aws:iam::`accountID`:role/`CodeGuruSecurityGitLabAccessRole`
    AWS_PROFILE: oidc # used to get the credential. More detail: https://gitlab.com/guided-explorations/aws/configure-openid-connect-in-aws/-/tree/main
  id_tokens:
    MY_OIDC_TOKEN:
      aud: https://gitlab.com
  before_script:
    - mkdir -p ~/.aws
    - echo "${MY_OIDC_TOKEN}" > /tmp/web_identity_token
    - echo -e "[profile oidc]\nrole_arn=${ROLE_ARN}\nweb_identity_token_file=/tmp/web_identity_token" > ~/.aws/config
  script:
    - REPO_NAME="`basename -s .git $(echo $CI_REPOSITORY_URL | grep -oE "[^/]+$")`"
    - python /usr/app/codeguru/command.py --source_path "." --aws_region "`region`" --scan_name CGS-GitLab-$REPO_NAME --fail_on_severity Critical --output_file_format "sast"
    - cat codeguru-security-results.sast.json
  rules:
    - if: $CI_PIPELINE_SOURCE == "push" && $CI_COMMIT_BRANCH == "main"
      when: always
  artifacts:
    reports:
      sast: codeguru-security-results.sast.json

```

6. Choose **Commit changes** to commit your changes.

## Step 3: Run scans and address findings

After configuring the CI/CD workflow, CodeGuru Security scan your code based on the events that you
have defined in the file. If you configured your pipeline to initiate scans on code commits,
CodeGuru Security will automatically scan your code whenever you push to the specified branch.

To view your findings, choose **Secure** in the left
navigation bar of your project, and then choose **Vulnerability report**. You
can also view code scans and findings in the CodeGuru Security console.

To address findings, update your code based on the suggested remediations, and then push
your changes to the branch where you configured the workflow. CodeGuru Security will scan the updated
code based on the events that you have defined in the workflow file, and you can check that the
vulnerabilities were remediated.
