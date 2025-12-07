# Enable code review capability for a GitHub repository

Configure AWS Security Agent to automatically review pull requests in your connected GitHub repositories. Code review analyzes code changes against your organizational security requirements and common security vulnerabilities for consistent enforcement.

AWS Security Agent automatically comments on pull requests with security findings and remediation guidance, helping developers address issues directly in their GitHub workflow.

In this procedure, you’ll connect repositories to your Agent Space, select which repositories have code review enabled, configure code review settings, and activate the capability.

## Prerequisites

Before you begin, ensure you have:

- Installed and authorized the AWS Security Agent GitHub App for your GitHub organization (see [Connect AWS Security Agent to GitHub repositories](connect-github.md "connect-github.md"))
- Appropriate permissions to configure code review settings for your Agent Space
- (Optional) At least one custom security requirement enabled if you plan to use security requirement validation (see [Manage security requirements](security-requirements.md "security-requirements.md"))

## Step 1: Access the code review configuration

Navigate to the code review configuration for your Agent Space.

1. In the AWS Security Agent console, select your Agent Space.
2. Choose **Enable code review** from the capabilities menu.

## Step 2: Connect repositories to your Agent Space

Select which repositories from your authorized GitHub organization or user account to connect to this Agent Space.

1. From the list select the registered **GitHub organization or user** that you authorized.

###### Note

If you registered multiple GitHub organizations or users, you can select one and connect repositories. 2. Select repositories to connect:

    * Browse the list of available repositories
    * Select the checkbox next to each repository you want to connect

3. Click **Add repositories** to connect the selected repositories to your Agent Space.
4. The connected repositories will appear in your Agent Space’s repository list.

## Step 3: Select repositories for code review

Review your connected GitHub repositories and enable code review for the repositories you want AWS Security Agent to monitor.

1. In the **Connected GitHub repositories** section, you’ll see a list of all repositories connected to your Agent Space.
2. Review the repository list and identify which repositories should have code review enabled.

###### Note

Code review is only available for private repositories. 3. For each repository you want to enable:

    * Locate the repository in the table
    * Toggle the **Enable** switch in the **Code review** column to the on position


    ###### Tip

    You can use the search field to quickly find specific repositories by name.

## Step 4: Configure code review settings

Configure the types of security issues AWS Security Agent analyzes in pull requests. This setting applies to all repositories with code review enabled in this Agent Space and can be modified at any time.

1. In the **Code review settings** section, select one of the following options:
   - **Security requirement validation** – Validate whether code changes comply with the custom security requirements you’ve enabled. This is the default setting.
   - **Security vulnerability findings** – Identify common security vulnerabilities in code changes.
   - **Security requirements and vulnerability findings** – Analyze code changes for both compliance with your organization’s custom security requirements and common security vulnerabilities.

###### Note

When security requirement validation is enabled, AWS Security Agent only checks code changes against your enabled custom security requirements, not AWS managed requirements. Custom security requirements are organization-specific policies you define and enable. If you enable security requirement validation but do not have at least one custom security requirement enabled, AWS Security Agent will not perform code reviews. For more information about security requirements, see [Manage security requirements](security-requirements.md "security-requirements.md").

## Step 5: Enable code review

After selecting your repositories and configuring your settings, activate code review capability for your Agent Space.

1. Review your repository selections and code review settings to ensure accuracy.
2. Click **Enable** at the bottom of the page.
3. AWS Security Agent will activate code review for the selected repositories with your configured settings.

###### Note

You can modify code review settings and which repositories have code review enabled at any time by returning to this configuration page.

## Next steps

After enabling code review:

- AWS Security Agent will automatically analyze pull requests in enabled repositories based on your configured code review settings
- Security findings will be posted as comments on pull requests with specific remediation guidance
- Review and respond to security findings as they are discovered
- Adjust code review settings or which repositories have code review enabled as your needs change
