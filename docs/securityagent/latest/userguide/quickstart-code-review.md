# Quickstart: Run a code review

This quickstart walks you through running your first code review with AWS Security Agent. AWS Security Agent scans your source code repositories for security vulnerabilities and compliance with your organization’s security requirements.

###### Note

You need access to the AWS Management Console to set up code review

## Step 1: Set up AWS Security Agent in the AWS console

If you haven’t already set up AWS Security Agent, complete the initial setup:

1. Navigate to [AWS Security Agent](https://console.aws.amazon.com/securityagent/ "https://console.aws.amazon.com/securityagent/") in the AWS Management Console.
2. Select **Set up AWS Security Agent**.
3. Create an Agent Space. An agent space can be used by multiple users and should be specific for every application you want to test. Enter a name and description for your first agent space. This name appears to users in the web application. The name should identify the application whose code you want to review.
4. Select **IAM-only access** under _User access configuration_.

   - This quickstart does not cover enabling single sign-on (SSO) with IAM Identity Center. This allows users to directly access the AWS Security Agent web application, from the AWS Console.
   - If you want to enable users without AWS Management Console Access to perform tasks such as starting a penetration test or design review, you should enable the IAM Identity Center integration.

5. Choose **Set up AWS Security Agent**.

###### Note

When you choose Set up, AWS Security Agent will create your Agent Space, and establish a web application where your users can carry out design reviews and penetration tests.

## Step 2: Enable and configure code review

###### Note

If you already have GitHub repositories or S3 buckets connected to your Agent Space (for example, through penetration testing setup), code review is already enabled. You can skip this step and go directly to the web application.

### Open the code review setup wizard

1. From the left sidebar, select **Agent Spaces** and then select your Agent Space.
2. Select **Enable code review** from the header or the **Code review** tab.

### Step 1: Connect integrations, repos, and buckets

1. **(If you don’t have a GitHub integration yet)** Create a GitHub registration. If you already have one, skip to the next step.

   1. In the **Connected integrations** section, choose **Add** and then **Create new registration**.
   2. Select **GitHub** and choose **Next**.
   3. Choose **Install and authorize**, then complete installation in GitHub:

      1. Select the GitHub user or organization that owns the repository you want to review.
      2. Select **All repositories** or **Only select repositories**.
      3. Choose **Install & Authorize** and complete GitHub authentication.

   4. Back in the AWS Management Console, enter a **Registration name** and confirm the **Account type** matches where you installed the GitHub App.
   5. Choose **Connect** to save the registration.

   For the full GitHub integration flow, see [Connect AWS Security Agent to GitHub repositories](connect-github.md "connect-github.md").

2. Connect GitHub repositories. In the **Connected integrations** section, choose **Add**, then select your GitHub registration. The two-step **Connect GitHub** wizard opens:

   1. On **Connect GitHub repositories**, select the repositories to include and choose **Next**.
   2. On **Manage capabilities**, toggle the following per repository:

      - **Code review comments** – Let AWS Security Agent post security findings as comments on pull requests in the repository.
      - **Automatic remediation** – Let users of the AWS Security Agent web application request pull requests that fix findings.

   3. Choose **Save** to return to the setup wizard.

3. (Optional) Connect S3 sources. In the **S3 buckets** section, choose **Add S3 resource** and enter the S3 URI for a bucket containing source code, or choose **Browse** to pick one.
4. Select your **Code review settings**. The default, **Security requirements and vulnerability findings**, analyzes code for both compliance with the security requirements you’ve enabled and common vulnerabilities.
5. Choose **Next**.

### Step 2: Optional configurations

1. Configure optional CloudWatch log groups and service access. The default service role is pre-configured with the required permissions.
2. Choose **Save**.

## Step 3: Create and run a code review

###### Note

You create and run code reviews only in the AWS Security Agent web application.

1. Select the **Web app** tab and then **Admin access** to launch the AWS Security Agent web application. Alternatively, if you have IAM Identity Center configured, log in directly.
2. In the left sidebar, choose **Code reviews**.
3. Choose **Create code review**.
4. Configure the code review:

   1. Enter a **Title** that identifies the scope of this review (for example, "billing-service-security-review").
   2. Under **Sources**, select the GitHub repositories or enter the S3 sources you want to scan.
   3. Select the **Service role** from your configured roles.
   4. (Optional) Select **Enable automatic code remediation** to have AWS Security Agent automatically submit pull requests with fixes for all findings.

5. Choose **Create code review**.
6. On the code review detail page, choose **Start review**.

## Step 4: Review code review findings

1. The code review typically takes 30–60 minutes depending on the size of your codebase.
2. Once complete, navigate to the completed run and select the **Findings** tab.
3. Review findings in the list-detail view:

   1. Select a finding from the left panel to view its details.
   2. Review the **Description**, **Code locations**, and **Risk reasoning** sections.
   3. Use **Remediate code** to generate a pull request with a fix, or review automatic remediation PRs if you enabled that option.
