# Create a code review

Create code reviews in the AWS Security Agent web application to scan your source code repositories and S3 sources for security vulnerabilities. Code reviews perform comprehensive static analysis across your entire codebase, identifying security issues and providing remediation guidance.

Unlike pull request-based code review which analyzes individual code changes (see [Review code security findings in pull requests](review-code-findings-github.md "review-code-findings-github.md")), on-demand code reviews scan your full source code to identify security vulnerabilities and validate compliance with your organization’s security requirements.

In this procedure, you’ll create a code review by selecting source code inputs, configuring permissions, and running the review.

## Prerequisites

Before you begin, ensure you have:

- Access to the AWS Security Agent web application
- At least one connected GitHub repository or S3 bucket in your Agent Space

###### Tip

If you already have GitHub repositories connected to your Agent Space, code review is ready to use — no additional setup is required. Choose **Start in web app** from the **Code review** card on your Agent Space page, or launch the web application directly.

If you need to connect additional sources or configure S3 buckets, see [Enable code review](enable-code-review-scan.md "enable-code-review-scan.md").

## Access the code reviews page

Navigate to the code reviews section in the web application.

1. Log in to the AWS Security Agent web application.
2. In the left sidebar, choose **Code reviews**.
3. You see a list of existing code reviews with their source information, last run status, and findings summary.

## Create a code review

Set up a new code review by configuring its source code inputs and permissions.

1. On the **Code reviews** page, choose **Create code review**.

### Configure code review details

Provide a title and select the source code to review.

1. In the **Title** field, enter a descriptive name for your code review.

###### Tip

Use a name that identifies the application, repository, or scope of the review. For example, "billing-service-security-review" or "infrastructure-code-audit". 2. In the **Sources** section, select the source code inputs for this review. Choose from two tabs:

#### GitHub repositories

Select from repositories connected to your Agent Space.

1. Choose the **GitHub repositories** tab.
2. In the **Integrated repositories** table, select the checkbox next to each repository you want to include in the review.
3. Use the search field to find specific repositories by name.

###### Note

Only repositories connected to your Agent Space through the code review configuration appear here. To add more repositories, choose **Manage in your Admin console** or ask your administrator to update the Agent Space configuration.

###### Tip

When you select a repository, you can specify a branch. By default, the service uses the primary branch. To use a different branch, enter the branch name in the field next to the repository.

#### S3 sources

Select ZIP files from the S3 buckets connected to your Agent Space. Your Agent Space administrator configures which S3 buckets are available. Any ZIP file stored in one of those buckets can be used as a source for a code review.

1. Choose the **S3 sources** tab.
2. Enter the S3 URI of each ZIP file you want to include in the review. You can add up to 30 S3 sources.

###### Note

S3 sources must be ZIP files stored in S3 buckets that are connected to your Agent Space. To make additional buckets available, see [Enable code review](enable-code-review-scan.md "enable-code-review-scan.md").

### Configure permissions

Select the IAM service role and optional CloudWatch log group for this code review.

1. In the **Permissions** section, locate the **Service role** dropdown.
2. Select the IAM role from your configured service roles.

###### Note

The service role must have permissions to access your source code in S3 and write to CloudWatch logs, and any other AWS resources needed for the code review. Service roles are configured during code review setup in the AWS Management Console. 3. (Optional) In the **CloudWatch log group** dropdown, select a log group to store code review execution logs.

###### Note

If you don’t select a log group, AWS Security Agent creates a default log group for storing code review logs.

### Configure automatic code remediation

Enable automatic remediation to have AWS Security Agent generate code fixes for all findings as soon as the review completes.

1. In the **Automatic code remediation** section, select the **Enable automatic code remediation** checkbox.

How AWS Security Agent delivers the fix depends on the source:

- **Private GitHub repositories** – AWS Security Agent submits a pull request with the fix to the repository.
- **Public GitHub repositories** – To avoid disclosing the vulnerability before it’s fixed, AWS Security Agent does not open a pull request. Instead, it attaches a suggested diff to the finding that you can download from the web application and apply privately.
- **S3 sources** – Code remediation is not available. Review the finding details and apply fixes manually.

###### Important

Remediation pull requests submitted to private repositories are visible to everyone with read access. Review the changes before merging. Automatic code remediation is only available when GitHub repositories are selected as a source.

###### Note

When disabled, you can still manually trigger code remediation for individual GitHub-sourced findings after the review completes.

### Configure simulated validation

Enable simulated validation to dynamically confirm whether discovered vulnerabilities are exploitable in a running application.

1. In the **Simulated validation** section, select the **Enable simulated validation** checkbox.

When enabled, AWS Security Agent provisions a simulated environment after static analysis completes. It onboards your source code, starts services inside the environment, and attempts to exploit vulnerabilities found during the scan. Findings are then updated with a validation status indicating whether the vulnerability was successfully exploited.

###### Note

Simulated validation is currently available for self-contained dockerizable applications only. When multiple repositories are selected as sources, simulated validation is not available.

###### Important

Simulated validation adds processing time to your code review run. The validation step provisions an environment and runs exploitation attempts. This typically takes 1–3 hours depending on the number of findings and application complexity.

#### Allowed network destinations

The simulated environment has outbound network access restricted to a predefined allowlist. Your application can reach the following domains during validation:

The following table lists the allowed domains and their purposes.

| Domain                                                                                | Purpose                         |
| ------------------------------------------------------------------------------------- | ------------------------------- |
| `.amazonaws.com`, `.aws.amazon.com`                                                   | AWS services                    |
| `.public.ecr.aws`                                                                     | Amazon ECR Public               |
| `.docker.com`, `.docker.io`                                                           | Docker Hub                      |
| `.github.com`, `.githubusercontent.com`                                               | GitHub                          |
| `.gitlab.com`                                                                         | GitLab                          |
| `.npmjs.com`, `.npmjs.org`                                                            | npm registry                    |
| `.pypi.org`, `.pypi.python.org`, `.pythonhosted.org`                                  | Python Package Index            |
| `.crates.io`, `.rustup.rs`                                                            | Rust packages                   |
| `.maven.org`, `.gradle.org`                                                           | Java/Gradle packages            |
| `.nuget.org`                                                                          | .NET packages                   |
| `.rubygems.org`, `.ruby-lang.org`                                                     | Ruby packages                   |
| `.golang.org`, `.pkg.go.dev`, `.goproxy.io`                                           | Go packages                     |
| `.nodejs.org`, `.yarnpkg.com`                                                         | Node.js                         |
| `.alpinelinux.org`, `.debian.org`, `.ubuntu.com`, `.centos.org`, `.fedoraproject.org` | Linux distribution repositories |
| `.cloudfront.net`                                                                     | CloudFront distributions        |
| `.google.com`, `.googleapis.com`                                                      | Google APIs                     |
| `.microsoft.com`, `.visualstudio.com`                                                 | Microsoft services              |
| `.sourceforge.net`, `.bitbucket.org`                                                  | Source hosting                  |

###### Note

If your application requires network access to domains not on this list, the connection will be blocked by the network firewall. Applications that depend on external APIs or services not listed above may not start correctly in the simulated environment.

### Create the code review

1. Review your configuration to ensure accuracy.
2. Choose **Create code review**.

You are redirected to the code review detail page where you can start a review run.

## Run a code review

After creating a code review, start a run to begin the analysis.

1. On the code review detail page, choose **Start review**.
2. AWS Security Agent begins analyzing your source code.

You can also start a review from the **Code reviews** list page by choosing **Start review** next to the code review you want to run.

## Monitor a code review run

Track the progress of your code review as it executes.

### Review run phases

A code review run progresses through the following phases, displayed as a progress indicator:

1. **Preflight** – AWS Security Agent validates access to your source code and sets up the testing environment. The preflight checks include:

   - Service infrastructure setup
   - S3 source access validation
   - Setup testing environment

2. **Static analysis** – AWS Security Agent scans your source code for security vulnerabilities and requirement violations.
3. **Simulated validation** (optional) – If simulated validation is enabled, AWS Security Agent provisions a simulated environment and deploys your application. It then attempts to exploit the vulnerabilities discovered during static analysis. This step confirms whether findings are exploitable in the target runtime. This phase only appears when you enable simulated validation during code review creation.
4. **Finalizing** – AWS Security Agent compiles findings and generates the results summary.

### View run details

On the run detail page, navigate between tabs to monitor progress:

- **Code review run** – View the run summary including run ID, creation time, status, duration, task hours, severity level breakdown, and risk types chart.
- **Preflight** – View the preflight check progress and status of each validation step.
- **Code review logs** – View the tasks AWS Security Agent identified and conducted during the review, with detailed task logs for each step.
- **Simulated validation** – When simulated validation is enabled, view the provisioning status, validation tasks for individual findings, and their results.
- **Findings** – View security findings after the review completes (see [Review findings from a code review](review-code-scan-findings.md "review-code-scan-findings.md")).

### Run history

Each code review maintains a history of all runs. On the code review detail page:

- The **Latest run** section shows the most recent run with its start time, status, duration, and ID.
- The **All runs** table lists all previous runs with their start time, status, duration, findings summary, and ID.
- Choose **Monitor run** to view the details of the latest active run.
- Choose any run’s start time link to view its full details.

## Next steps

After running a code review:

- Review security findings and their remediation guidance (see [Review findings from a code review](review-code-scan-findings.md "review-code-scan-findings.md"))
- Remediate findings through automated pull requests or manual fixes (see [Remediate code review findings](remediate-code-scan-findings.md "remediate-code-scan-findings.md"))
- Run additional reviews after implementing fixes to verify remediation
- Adjust your code review configuration or sources as your codebase evolves
