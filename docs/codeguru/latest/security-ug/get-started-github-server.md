On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# Integrate with GitHub Enterprise Server

Complete the following steps to integrate CodeGuru Security with GitHub Enterprise Server.

## Step 1: Prerequisites

Complete the following prerequisites before continuing with the integration steps.

- Enable GitHub Actions on your enterprise server. For more information, see [Enabling GitHub Actions for GitHub Enterprise Server](https://docs.github.com/en/enterprise-server@3.10/admin/github-actions/enabling-github-actions-for-github-enterprise-server "https://docs.github.com/en/enterprise-server@3.10/admin/github-actions/enabling-github-actions-for-github-enterprise-server") in the GitHub Enterprise
  Server Docs.
- Configure self-hosted runners to run workflows. For more information, see [Getting started with self-hosted runners for your enterprise](https://docs.github.com/en/enterprise-server@3.10/admin/github-actions/getting-started-with-github-actions-for-your-enterprise/getting-started-with-self-hosted-runners-for-your-enterprise "https://docs.github.com/en/enterprise-server@3.10/admin/github-actions/getting-started-with-github-actions-for-your-enterprise/getting-started-with-self-hosted-runners-for-your-enterprise") in the GitHub
  Enterprise Server Docs.
- Grant your enterprise server access to the following AWS GitHub actions: [aws-actions/configure-aws-credentials](https://github.com/aws-actions/configure-aws-credentials "https://github.com/aws-actions/configure-aws-credentials") and [aws-actions/codeguru-security](https://github.com/aws-actions/codeguru-security "https://github.com/aws-actions/codeguru-security"). For more information, see [Managing access to actions from GitHub.com](https://docs.github.com/en/enterprise-server@3.10/admin/github-actions/managing-access-to-actions-from-githubcom "https://docs.github.com/en/enterprise-server@3.10/admin/github-actions/managing-access-to-actions-from-githubcom") in the GitHub Enterprise Server Docs.
- (Optional) To view findings in GitHub, enable code scanning for your enterprise instance
  in order to upload static analysis results. For more information, see [Code scanning](https://docs.github.com/en/enterprise-server@3.10/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning "https://docs.github.com/en/enterprise-server@3.10/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning") in the GitHub Enterprise Server Docs.

## Step 2: Create an IAM role

To allow CodeGuru Security to integrate with GitHub, create an IAM role with sufficient
permissions. You can create an AWS CloudFormation stack that sets up a role for you, or manually
configure a role.

To manually configure an IAM role for GitHub, see [Configuring OpenID Connect in Amazon Web Services](https://docs.github.com/en/enterprise-server@3.10/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services "https://docs.github.com/en/enterprise-server@3.10/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services") in the GitHub Docs. You can attach
the AWS managed policy [AmazonCodeGuruSecurityScanAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonCodeGuruSecurityScanAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonCodeGuruSecurityScanAccess") to configure your role with the minimum
necessary permissions to integrate with GitHub.

If you have already configured a role to use CodeGuru Security with the GitHub repository you want
to scan, you can skip to step 2.

###### Create a role with a CloudFormation stack

Complete the following steps to create a CloudFormation stack that sets up an IAM role with
the necessary permissions attached to integrate with GitHub.

1. Open the **Integrations** page in the
   [CodeGuru Security
   console](https://console.aws.amazon.com/codeguru/security/integrations "https://console.aws.amazon.com/codeguru/security/integrations") and choose **Integrate with GitHub**.
2. For **Step 1: Create an IAM role**, choose
   **Use CloudFormation template**. Then choose
   **Open template in CloudFormation** to be redirected to the
   Create stack page in the CloudFormation console.
3. For **Stack name**, enter a unique name for your stack.
4. For **Parameters**, for **Hostname**,
   enter the hostname of your GitHub Enterprise Server instance. For **Repository**, enter the name of the repository you want to scan.
5. Check the box to acknowledge that AWS CloudFormation might create IAM resources with custom
   names. This allows CloudFormation to create a role for you.
6. Choose **Create stack**. CloudFormation creates a role called
   `CodeGuruSecurityGitHubEnterpriseServerAccessRole`. Continue to the next
   step.

## Step 3: Create a custom workflow in

GitHub

Complete the following steps to create a custom workflow for your repository that includes
steps and actions to run CodeGuru Security scans. The following workflow will initiate security scans
every time you push code to the `main` branch of the repository you are integrating
with. If CodeGuru Security detects a critical finding, the pipeline build will fail.

1. Log in to your [GitHub account](https://github.com/ "https://github.com/").
2. Open the repository that you want to scan.
3. Choose the **Actions** tab.
4. Choose **New workflow**.
5. Choose **set up a workflow yourself**.
6. Paste the following code into the `.github/workflow/main.yml` file editor in
   GitHub. You can modify the events defined in this file based on your use case.

Replace `accountID` with the AWS account ID of the account
that is assuming the role and `region` with the region where you are
running scans. If you manually configured a role, replace
`CodeGuruSecurityGitHubEnterpriseServerAccessRole` with the name of
the role you created to integrate with GitHub.

If you want to add code quality findings to your scan, add `analysis_type :
 All` in the `CodeGuru Security` step below `fail_on_severity :
 Critical`.

```
name: CodeGuru Security Example
on:
  push:
    branches:
      - 'main'

permissions:
  id-token: write
  # for writing security events
  security-events: write
  # only required for workflows in private repositories
  actions: read
  contents: read

jobs:
  build:
    runs-on: self-hosted
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3
        with:
          fetch-depth: 0

      - name: Configure aws credentials
        uses: aws-actions/configure-aws-credentials@v2
        with:
          role-to-assume: arn:aws:iam::`accountID`:role/`CodeGuruSecurityGitHubEnterpriseServerAccessRole`
          aws-region: `region`
          role-session-name: GitHubActionScript

      - name: CodeGuru Security
        uses: aws-actions/codeguru-security@v1
        with:
          source_path: .
          aws_region: `region`
          fail_on_severity: Critical
      - name: Print Findings
        run: |
          ls -l
          cat codeguru-security-results.sarif.json

      # Note: Code scanning feature needs to be enabled for this repository.
      # https://docs.github.com/en/enterprise-server@3.10/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/configuring-default-setup-for-code-scanning
      - name: Upload result
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: codeguru-security-results.sarif.json

```

7. Commit your changes.

## Step 4: Run scans and address findings

After creating the workflow, CodeGuru Security will scan your repository based on the events that
you have defined in the workflow file. If you used the code from the previous step or otherwise
configured your workflow to initiate scans on code commits, CodeGuru Security will automatically scan
your code whenever you push to the specified branch.

If you enabled code scanning in GitHub, you can view findings by going to the
**Security** tab of your repository, and then choosing **Code
scanning** in the left navigation bar. You can also view scans and findings in the
CodeGuru Security console.

To address findings, update your code based on the suggested remediations, and then push
your changes to the branch where you created the workflow. CodeGuru Security will scan the updated code
based on the events that you have defined in the workflow file, and you can check that the
vulnerabilities were remediated.
