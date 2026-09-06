

# Enable code review
<a name="enable-code-review-scan"></a>

Configure your Agent Space to enable code review by connecting source code from GitHub repositories or S3 buckets. Code review analyzes your source code for security vulnerabilities and compliance with your organization’s custom security requirements.

Setting up code review configurations is an Agent Space-wide operation. The integrations and S3 buckets you connect are shared across capabilities, including code review and penetration testing.

After completing setup, users can create and run code reviews in the AWS Security Agent web application to scan repositories and S3 sources for security issues.

**Note**  
If you already have GitHub repositories connected to your Agent Space (for example, through penetration testing setup), code review is already enabled. You can skip this setup and go directly to the web application to create code reviews. See [Create a code review](perform-code-review-scan.md).

## Prerequisites
<a name="_prerequisites"></a>

Before you begin, ensure you have:
+ An Agent Space created in the AWS Management Console (see [Create an Agent Space](create-agent-space.md))
+ At least one of the following source code inputs:
  + A GitHub organization or user account with the AWS Security Agent GitHub App installed (see [Connect AWS Security Agent to GitHub repositories](connect-github.md))
  + An S3 bucket containing source code you want to review
+ Permissions to configure integrations for your Agent Space
+ (Optional) At least one security requirement enabled in a security requirement pack if you plan to use security requirement validation (see [Manage security requirements](security-requirements.md))

## Access the code review setup wizard
<a name="_access_the_code_review_setup_wizard"></a>

Navigate to the code review setup for your Agent Space.

1. In the AWS Security Agent console, select your Agent Space.

1. Choose **Enable code review** from one of the following locations:
   + The **Code review** card
   + The **Code review** tab, then choose **Enable code review** 

**Tip**  
If you would like AWS Security Agent to address code review feedback automatically, enable **Code remediation** as well. See [Enable users to start remediation of penetration test and code review findings](enable-remediate-findings.md) for details.

You are directed to the **Setup code review configurations** wizard.

## Step 1: Connect integrations, repos, and buckets
<a name="_step_1_connect_integrations_repos_and_buckets"></a>

In the first step of the wizard, connect your source code inputs and configure code review settings. You must add at least one GitHub repository or S3 bucket to proceed.

**Important**  
Integrations and S3 buckets configured here are shared across your Agent Space. Changes apply to both code review and penetration testing capabilities.

### Connect GitHub repositories
<a name="_connect_github_repositories"></a>

Add GitHub repositories from your authorized GitHub organizations or user accounts. Choosing **Add** opens the two-step **Connect GitHub** wizard, where you first select repositories and then configure what actions AWS Security Agent can take on each one.

1. In the **Connected integrations** section, choose **Add**.

1. Select the GitHub registration that contains the repositories you want to review.

1. On the **Connect GitHub repositories** step, select the checkbox for each repository you want to connect.

1. Choose **Next** to go to **Manage capabilities**.

**Note**  
Connected repositories are accessed read-only for code analysis during code review and penetration testing. You configure write actions such as posting review comments and opening remediation pull requests on the next step.

**Note**  
If you haven’t registered a GitHub integration yet, choose **Settings** to navigate to the Integrations page where you can authorize the AWS Security Agent GitHub App. For more information, see [Connect AWS Security Agent to GitHub repositories](connect-github.md).

### Configure GitHub repository capabilities
<a name="_configure_github_repository_capabilities"></a>

On the **Manage capabilities** step of the **Connect GitHub** wizard, choose what AWS Security Agent can do in each repository. **Code review comments** and **Code remediation** are set independently per repository.

1. For each repository, toggle **Code review comments** on to have AWS Security Agent post security findings as comments on pull requests.

1. For each repository, toggle **Code remediation** on to let AWS Security Agent fix findings. When enabled, web application users can request pull requests that fix findings, and pull request authors can comment `@AWS-Security-Agent fix all findings.` to have the agent address its review comments.

1. Choose **Save** to apply your selections and return to the code review setup wizard.

When **Code review comments** is enabled for a repository:
+ AWS Security Agent automatically analyzes pull requests when they are marked as "Ready for review". Draft pull requests are not analyzed.
+ Security findings are posted as review comments directly on the pull request with specific remediation guidance.
+ The analysis uses your configured code review settings (security vulnerabilities, custom requirements, or both).

**Note**  
Pull request comments are only available for private GitHub repositories.

When **Code remediation** is enabled for a repository, web application users can start remediation for both code review and penetration test findings on that repository, and AWS Security Agent delivers each fix as a pull request. For more information, see [Enable users to start remediation of penetration test and code review findings](enable-remediate-findings.md).

For more information about how pull request findings appear in GitHub and how to respond to them, see [Review code security findings in pull requests](review-code-findings-github.md).

### Add S3 buckets
<a name="_add_s3_buckets"></a>

Add S3 buckets containing source code or contextual resources for code review.

1. In the **S3 buckets** section, choose **Add S3 resource**.

1. Enter the S3 URI for the bucket or prefix containing your source code.

1. Choose **Add**.

**Note**  
You can add up to 10 S3 resources. S3 buckets are shared across capabilities including code review and penetration testing.

**Tip**  
You can add S3 buckets that contain source code, configuration files, infrastructure-as-code templates, or other artifacts you want AWS Security Agent to analyze for security issues.

### Configure code review settings
<a name="_configure_code_review_settings"></a>

Configure the types of security issues AWS Security Agent analyzes during code reviews. This setting applies to all repositories and sources with code review enabled in this Agent Space.

1. In the **Code review settings** section, select one of the following options:
   +  **Security requirement validation** – Validate whether code complies with the security requirements you’ve enabled in your security requirement packs.
   +  **Security vulnerability findings** – Identify common security vulnerabilities in code.
   +  **Security requirements and vulnerability findings** – Analyze code for both compliance with the security requirements you’ve enabled and common security vulnerabilities. This is the default setting.

**Note**  
When security requirement validation is enabled, AWS Security Agent checks code against the security requirements you’ve enabled in your security requirement packs. If you select security requirement validation but do not have at least one security requirement enabled, AWS Security Agent will not identify requirement-based findings. For more information about security requirements, see [Manage security requirements](security-requirements.md).

1. Choose **Next** to proceed to optional configurations.

## Step 2: Optional configurations
<a name="_step_2_optional_configurations"></a>

In the second step of the wizard, configure optional CloudWatch logging and service access settings for your code review environment.

### (Optional) Configure CloudWatch logs
<a name="_optional_configure_cloudwatch_logs"></a>

Configure CloudWatch log groups to capture and analyze application behavior during code review.

1. Expand the **CloudWatch logs** section.

1. In the **Log Groups** dropdown, select one or more existing CloudWatch log groups from your AWS account.

**Note**  
If you don’t select a log group, AWS Security Agent automatically creates a default log group to store code review execution logs.

### (Optional) Configure service access
<a name="_optional_configure_service_access"></a>

Configure the IAM service role that AWS Security Agent uses to access your AWS resources such as S3 buckets and CloudWatch logs for code review.

1. Expand the **Service access** section.

1. Select one of the following options:
   +  **Create default role** – AWS Security Agent automatically creates a new IAM role with the necessary permissions for code review.
   +  **Use an existing service role** – Select an existing IAM role from the dropdown menu.

1. If using the default role, enter a **Service role name**. The name must be unique across all roles in the account, use alphanumeric characters and `+=,.@-_` characters, and cannot include spaces.

**Note**  
The service role name has a maximum length of 64 characters. A service role is automatically created if you don’t select an existing role.

1. Choose **Save** to complete the setup.

## After setup
<a name="_after_setup"></a>

After completing the code review setup wizard:
+ The **Code review** card on your Agent Space page shows a **Ready** status.
+ Users can launch the web application and create code reviews to scan connected repositories and S3 sources.
+ You can modify your configuration at any time by choosing **Edit configuration** on the **Code review** tab.

## Edit code review configuration
<a name="_edit_code_review_configuration"></a>

To modify your code review configuration after initial setup:

1. Navigate to your Agent Space in the AWS Security Agent console.

1. Select the **Code review** tab.

1. Choose **Edit configuration**.

1. Update your integrations, S3 buckets, code review settings, CloudWatch logs, or service access as needed.

1. Choose **Save**.

## Next steps
<a name="_next_steps"></a>

After setting up code review configurations:
+ Launch the web application to create and run code reviews (see [Create a code review](perform-code-review-scan.md))
+ Connect additional GitHub repositories or S3 buckets as your codebase grows
+ Configure security requirement packs for organization-specific validation (see [Manage security requirements](security-requirements.md))
+ Review how pull request findings appear in GitHub (see [Review code security findings in pull requests](review-code-findings-github.md))