

# Create a code review
<a name="perform-code-review-scan"></a>

Create code reviews in the AWS Security Agent web application to scan your source code repositories and S3 sources for security vulnerabilities. Code reviews perform comprehensive static analysis across your entire codebase, identifying security issues and providing remediation guidance.

Unlike pull request-based code review which analyzes individual code changes (see [Review code security findings in pull requests](review-code-findings-github.md)), on-demand code reviews scan your full source code to identify security vulnerabilities and validate compliance with your organization’s security requirements.

In this procedure, you’ll create a code review by selecting source code inputs, configuring permissions, and running the review.

## Prerequisites
<a name="_prerequisites"></a>

Before you begin, ensure you have:
+ Access to the AWS Security Agent web application
+ At least one connected GitHub repository or S3 bucket in your Agent Space

**Tip**  
If you already have GitHub repositories connected to your Agent Space, code review is ready to use — no additional setup is required. Choose **Start in web app** from the **Code review** card on your Agent Space page, or launch the web application directly.  
If you need to connect additional sources or configure S3 buckets, see [Enable code review](enable-code-review-scan.md).

## Access the code reviews page
<a name="_access_the_code_reviews_page"></a>

Navigate to the code reviews section in the web application.

1. Log in to the AWS Security Agent web application.

1. In the left sidebar, choose **Code reviews**.

1. You see a list of existing code reviews with their source information, last run status, and findings summary.

## Create a code review
<a name="_create_a_code_review"></a>

Set up a new code review by configuring its source code inputs and permissions.

1. On the **Code reviews** page, choose **Create code review**.

### Configure code review details
<a name="_configure_code_review_details"></a>

Provide a title and select the source code to review.

1. In the **Title** field, enter a descriptive name for your code review.
**Tip**  
Use a name that identifies the application, repository, or scope of the review. For example, "billing-service-security-review" or "infrastructure-code-audit".

1. In the **Sources** section, select the source code inputs for this review. Choose from two tabs:

#### GitHub repositories
<a name="_github_repositories"></a>

Select from repositories connected to your Agent Space.

1. Choose the **GitHub repositories** tab.

1. In the **Integrated repositories** table, select the checkbox next to each repository you want to include in the review.

1. Use the search field to find specific repositories by name.

**Note**  
Only repositories connected to your Agent Space through the code review configuration appear here. To add more repositories, choose **Manage in your Admin console** or ask your administrator to update the Agent Space configuration.

**Tip**  
When you select a repository, you can specify a branch. By default, the service uses the primary branch. To use a different branch, enter the branch name in the field next to the repository.

#### S3 sources
<a name="_s3_sources"></a>

Select ZIP files from the S3 buckets connected to your Agent Space. Your Agent Space administrator configures which S3 buckets are available. Any ZIP file stored in one of those buckets can be used as a source for a code review.

1. Choose the **S3 sources** tab.

1. Enter the S3 URI of each ZIP file you want to include in the review. You can add up to 30 S3 sources.

**Note**  
S3 sources must be ZIP files stored in S3 buckets that are connected to your Agent Space. To make additional buckets available, see [Enable code review](enable-code-review-scan.md).

### Configure permissions
<a name="_configure_permissions"></a>

Select the IAM service role and optional CloudWatch log group for this code review.

1. In the **Permissions** section, locate the **Service role** dropdown.

1. Select the IAM role from your configured service roles.
**Note**  
The service role must have permissions to access your source code in S3 and write to CloudWatch logs, and any other AWS resources needed for the code review. Service roles are configured during code review setup in the AWS Management Console.

1. (Optional) In the **CloudWatch log group** dropdown, select a log group to store code review execution logs.
**Note**  
If you don’t select a log group, AWS Security Agent creates a default log group for storing code review logs.

### Configure automatic code remediation
<a name="_configure_automatic_code_remediation"></a>

Enable automatic remediation to have AWS Security Agent generate code fixes for all findings as soon as the review completes.

1. In the **Automatic code remediation** section, select the **Enable automatic code remediation** checkbox.

How AWS Security Agent delivers the fix depends on the source:
+  **Connected private repository** – AWS Security Agent submits a pull request (or a merge request, for GitLab) with the fix.
+  **Public repository** – To avoid disclosing the vulnerability before it’s fixed, AWS Security Agent does not open a pull request. Delivery varies by provider — for example, public GitHub repositories receive a downloadable diff you can apply privately; see the provider’s connection topic.
+  **Amazon S3 sources** – AWS Security Agent attaches a downloadable code diff to the finding (there’s no connected repository to open a pull request against). Download it from the web application and apply it locally.

**Important**  
Everyone with read access to the private repository can see the remediation pull request. Review the changes before merging.

**Note**  
When automatic code remediation is disabled, you can still trigger it manually for individual findings. This works for findings from a connected repository or an Amazon S3 source.

### Configure simulated validation
<a name="_configure_simulated_validation"></a>

Enable simulated validation to dynamically confirm whether discovered vulnerabilities are exploitable in a running application.

1. In the **Simulated validation** section, select the **Enable simulated validation** checkbox.

When enabled, AWS Security Agent provisions a simulated environment after static analysis completes. It onboards your source code, starts services inside the environment, and attempts to exploit vulnerabilities found during the scan. Findings are then updated with a validation status indicating whether the vulnerability was successfully exploited.

**Note**  
Simulated validation is currently available for self-contained dockerizable applications only. When multiple repositories are selected as sources, simulated validation is not available.

**Important**  
Simulated validation adds processing time to your code review run. The validation step provisions an environment and runs exploitation attempts. This typically takes 1–3 hours depending on the number of findings and application complexity.

#### Allowed network destinations
<a name="_allowed_network_destinations"></a>

The simulated environment has outbound network access restricted to a predefined allowlist. Your application can reach the following domains during validation:

The following table lists the allowed domains and their purposes.


| Domain | Purpose | 
| --- | --- | 
|  `.amazonaws.com`, `.aws.amazon.com`  | AWS services | 
|  `.public.ecr.aws`  | Amazon ECR Public | 
|  `.docker.com`, `.docker.io`  | Docker Hub | 
|  `.github.com`, `.githubusercontent.com`  | GitHub | 
|  `.gitlab.com`  | GitLab | 
|  `.npmjs.com`, `.npmjs.org`  | npm registry | 
|  `.pypi.org`, `.pypi.python.org`, `.pythonhosted.org`  | Python Package Index | 
|  `.crates.io`, `.rustup.rs`  | Rust packages | 
|  `.maven.org`, `.gradle.org`  | Java/Gradle packages | 
|  `.nuget.org`  | .NET packages | 
|  `.rubygems.org`, `.ruby-lang.org`  | Ruby packages | 
|  `.golang.org`, `.pkg.go.dev`, `.goproxy.io`  | Go packages | 
|  `.nodejs.org`, `.yarnpkg.com`  | Node.js | 
|  `.alpinelinux.org`, `.debian.org`, `.ubuntu.com`, `.centos.org`, `.fedoraproject.org`  | Linux distribution repositories | 
|  `.cloudfront.net`  | CloudFront distributions | 
|  `.google.com`, `.googleapis.com`  | Google APIs | 
|  `.microsoft.com`, `.visualstudio.com`  | Microsoft services | 
|  `.sourceforge.net`, `.bitbucket.org`  | Source hosting | 

**Note**  
If your application requires network access to domains not on this list, the connection will be blocked by the network firewall. Applications that depend on external APIs or services not listed above may not start correctly in the simulated environment.

### Create the code review
<a name="_create_the_code_review"></a>

1. Review your configuration to ensure accuracy.

1. Choose **Create code review**.

You are redirected to the code review detail page where you can start a review run.

## Run a code review
<a name="_run_a_code_review"></a>

After creating a code review, start a run to begin the analysis.

1. On the code review detail page, choose **Start review**.

1. AWS Security Agent begins analyzing your source code.

You can also start a review from the **Code reviews** list page by choosing **Start review** next to the code review you want to run.

## Monitor a code review run
<a name="_monitor_a_code_review_run"></a>

Track the progress of your code review as it executes.

### Review run phases
<a name="_review_run_phases"></a>

A code review run progresses through the following phases, displayed as a progress indicator:

1.  **Preflight** – AWS Security Agent validates access to your source code and sets up the testing environment. The preflight checks include:
   + Service infrastructure setup
   + S3 source access validation
   + Setup testing environment

1.  **Static analysis** – AWS Security Agent scans your source code for security vulnerabilities and requirement violations.

1.  **Simulated validation** (optional) – If simulated validation is enabled, AWS Security Agent provisions a simulated environment and deploys your application. It then attempts to exploit the vulnerabilities discovered during static analysis. This step confirms whether findings are exploitable in the target runtime. This phase only appears when you enable simulated validation during code review creation.

1.  **Finalizing** – AWS Security Agent compiles findings and generates the results summary.

### View run details
<a name="_view_run_details"></a>

On the run detail page, navigate between tabs to monitor progress:
+  **Code review run** – View the run summary including run ID, creation time, status, duration, task hours, severity level breakdown, and risk types chart.
+  **Preflight** – View the preflight check progress and status of each validation step.
+  **Code review logs** – View the tasks AWS Security Agent identified and conducted during the review, with detailed task logs for each step.
+  **Simulated validation** – When simulated validation is enabled, view the provisioning status, validation tasks for individual findings, and their results.
+  **Findings** – View security findings after the review completes (see [Review findings from a code review](review-code-scan-findings.md)).

### Run history
<a name="_run_history"></a>

Each code review maintains a history of all runs. On the code review detail page:
+ The **Latest run** section shows the most recent run with its start time, status, duration, and ID.
+ The **All runs** table lists all previous runs with their start time, status, duration, findings summary, and ID.
+ Choose **Monitor run** to view the details of the latest active run.
+ Choose any run’s start time link to view its full details.

## Next steps
<a name="_next_steps"></a>

After running a code review:
+ Review security findings and their remediation guidance (see [Review findings from a code review](review-code-scan-findings.md))
+ Remediate findings through automated pull requests or manual fixes (see [Remediate code review findings](remediate-code-scan-findings.md))
+ Run additional reviews after implementing fixes to verify remediation
+ Adjust your code review configuration or sources as your codebase evolves