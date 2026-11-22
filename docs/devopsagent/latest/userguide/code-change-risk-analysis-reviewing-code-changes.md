

# Reviewing code changes

**Preview:** Code Change Risk Analysis is in preview and is subject to change.

Code Change Risk Analysis evaluates your code changes for cross-repository dependency risks, internal standards compliance, access-control correctness, and risks to your production environments. It can also perform automatic verification testing, which builds, runs, and tests your code changes in a verification environment that AWS DevOps Agent manages. For an overview of the capability, see [Code Change Risk Analysis](working-with-devops-agent-code-change-risk-analysis-index.md).

## Getting started
<a name="getting-started"></a>

To use Code Change Risk Analysis, complete the following setup steps.

### Step 1: Enable capabilities on your repositories
<a name="step-1-enable-capabilities-on-your-repositories"></a>

Code review and automated testing capabilities must be enabled on your connected GitHub or GitLab repositories before they can trigger.

The **Code Review and Automated Testing** section in your pipeline provider integration settings provides two per-repository capabilities:
+ **Auto trigger change review** — When enabled, DevOps Agent automatically runs Code Change Risk Analysis each time a pull request or merge request is opened or updated. Review findings appear as inline comments on the PR/MR.
+ **Automatic verification testing** — When enabled, DevOps Agent builds, runs, and tests your code changes in a managed verification environment during code reviews. This provides functional validation beyond static analysis. For more information, see [Automatic verification testing](#automatic-verification-testing).

You can enable or disable each capability independently per repository, allowing you to use change reviews without verification testing or vice versa.

**For GitHub:** Navigate to the **Code Review and Automated Testing** section in your GitHub integration settings and enable the capabilities for each repository. Both capabilities are enabled by default when you connect repositories. For detailed instructions, see [Configuring Code Review and Automated Testing](connecting-to-cicd-pipelines-connecting-github.md).

**For GitLab:** Navigate to the **Code Review and Automated Testing** section in your GitLab integration settings and enable the capabilities for your projects. For detailed instructions, see [Configuring Code Review and Automated Testing](connecting-to-cicd-pipelines-connecting-gitlab.md).

#### Controlling when automated reviews trigger
<a name="controlling-when-automated-reviews-trigger"></a>

By default, when **Auto trigger change review** is enabled, DevOps Agent runs Code Change Risk Analysis on every applicable pull request or merge request event, on any target branch. You can narrow this by adding trigger filters in the **Advanced settings** of the connection flow.

With trigger filters, you can scope automated reviews by:
+ **Target branches** (required) — One or more branch names or patterns (regular expressions). The review triggers only when the pull request or merge request's target (base) branch matches. For example, `main` limits reviews to changes targeting the `main` branch, and `release/.*` matches any branch under `release/`.
+ **Trigger events** (optional) — Limit the review to specific events, such as when a pull request or merge request becomes ready for review. Leave this empty to match all applicable events.

You combine these conditions into filter groups. Within a filter group, all conditions must match (AND). You can define multiple filter groups, and a review triggers when any group matches (OR). For example, you can review changes that become ready for review and that target `main` or any `release/*` branch. You can define up to 5 filter groups per repository or project, with up to 20 branch patterns per group.

Trigger filters aren't fixed at setup time — you can return to the connection at any time, choose **Edit**, and update the filters under **Advanced settings**.

For instructions on configuring trigger filters in GitHub, see [Advanced settings: trigger filters](connecting-to-cicd-pipelines-connecting-github.md). For instructions on configuring trigger filters in GitLab, see [Advanced settings: trigger filters](connecting-to-cicd-pipelines-connecting-gitlab.md).

### Step 2: Configure Release Management environments for private VPC access (optional)
<a name="step-2-configure-release-management-environments-for-private-vpc-access-optional"></a>

Code Change Risk Analysis can perform automatic verification testing by building, running, and testing your code changes in a verification environment (see [Automatic verification testing](#automatic-verification-testing)). If your code build process requires artifacts from internal systems — such as private image repositories (for example, Artifactory, Docker Hub Enterprise), internal build artifact stores, or dependent code repositories — you need to give the verification testing environment access to a VPC that can reach those service endpoints.

By default, the verification testing environment does not have network access to your internal systems. To enable access, create a Release Management environment in your Agent Space. The environment stores the private connection and runtime role that the verification testing environment uses to reach private resources. Then associate the environment with each GitHub repository or GitLab project that requires private access.

The verification testing environment creates and manages an elastic network interface (ENI) inside the VPC associated with the private connection. The runtime role provides the permissions required to create and manage the ENI.

**Note**  
** Integrating with VPCs in your account routes network traffic through your internal routes, following any network restrictions in place.

You can create an environment before connecting a repository or project, or create one from the GitHub or GitLab association flow.

1. Create a private connection that can reach the VPC, subnet, and security group for your internal build services. For instructions, see [Connecting to privately hosted tools](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md).

1. Open the AWS DevOps Agent console and navigate to your Agent Space.

1. Start creating the environment using one of the following options:
   + To create the environment before connecting a repository or project, choose the **Environments** tab, and then choose **Add environment**.
   + To create the environment while connecting a repository or project, choose the **Capabilities** tab and add or edit the GitHub or GitLab connection. In **Code Review and Automated Testing**, enable **Automatic verification testing**. Then open **Advanced settings**, expand the repository or project, and choose **Create environment** under **Verification environment**. The environment configuration opens in a new browser tab.

1. Enter an **Environment name** and select the **Private connection** that reaches your internal build services.

1. Under **Configure runtime role**, choose how to configure the IAM role for the environment. You can have the console create a role, select an existing role, or follow the instructions to create one manually. If you use an existing or manually created role, make sure that it trusts AWS DevOps Agent and has the `AIDevOpsReleaseManagementVPCPolicy` AWS managed policy attached.

1. Choose **Save** to create the environment.

After creating an environment, associate it with the GitHub repositories or GitLab projects that use automatic verification testing:

1. Return to the GitHub or GitLab connection. If you created the environment from the **Environments** tab, choose the **Capabilities** tab and add or edit the connection.

1. In **Code Review and Automated Testing**, enable **Automatic verification testing** for each repository or project that requires the environment.

1. Open **Advanced settings** and expand the repository or project. If you created the environment from the association flow, refresh the environment list.

1. For **Verification environment**, select the Release Management environment that contains the required private connection and runtime role.

1. Choose **Save**.

The **Verification environment** field is available only when **Automatic verification testing** is enabled. Each repository or project can use one environment. For provider-specific instructions, see [Connecting GitHub](connecting-to-cicd-pipelines-connecting-github.md) or [Connecting GitLab](connecting-to-cicd-pipelines-connecting-gitlab.md).

You can create multiple environments when repositories require access to different VPCs.

## Configuring review depth
<a name="configuring-review-depth"></a>

You can set the review depth for each branch in a repository. Each review runs at one of the following depths:


| Depth | Value | Description | 
| --- | --- | --- | 
| Static code analysis | static-analysis | Reviews the change without building or running it. Static reviews take less time and cost less, but they produce more false positives. | 
| Static code analysis with verification testing | verification-testing | Also builds, runs, and tests the change in a verification environment. These reviews produce fewer false positives, but they take longer and cost more. For more information, see [Automatic verification testing](#automatic-verification-testing). | 

To run reviews at verification testing depth, enable **Automatic verification testing** for the repository. Otherwise, reviews run static code analysis, and the report explains why.

When you request a review through AWS DevOps Agent chat or the AWS DevOps Agent Model Context Protocol (MCP) server, you can specify the review depth for that review. A depth in the request takes precedence over the repository's configuration file. For more information about the MCP server, see [Connecting to the DevOps Agent MCP server](connecting-to-devops-agent-remote-servers-connecting-to-the-devops-agent-mcp-server.md).

For pricing, see [AWS DevOps Agent pricing](https://aws.amazon.com/devops-agent/pricing/).

### Setting review depth by branch
<a name="setting-review-depth-by-branch"></a>

To set review depth by branch, add a `.aws-code-review.yaml` file to the root of your repository. The following example file runs verification testing on pull requests into `main` and static code analysis on all other pull requests:

```
version: 1
reviews:
  default:
    review_depth: static-analysis
  overrides:
    - when:
        target_branch: main
      review_depth: verification-testing
    - when:
        source_branch: "wip/**"
        target_branch: "staging/*"
      review_depth: static-analysis
```
+ `default` – The depth for reviews that no override matches.
+ `overrides` – A list of rules, checked in order. The first rule whose `when` conditions all match sets the depth.
+ `target_branch` and `source_branch` – A branch name or pattern, or a list of them. A list matches if any entry matches. Patterns follow [GitHub Actions branch filter syntax](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#filter-pattern-cheat-sheet) : `*` matches any characters except `/`, and `**` matches any characters. Negation with `!` isn't supported.
+ `version` (optional) – The file format version. The only supported value is `1`.

If you don't add a `.aws-code-review.yaml` file or specify a depth in your request, AWS DevOps Agent chooses the depth for each change.

#### Which copy of the file applies
<a name="which-copy-of-the-file-applies"></a>

For a pull request or merge request, AWS DevOps Agent reads `.aws-code-review.yaml` from the **target branch**. It doesn't read the file from the branch being merged. This has the following effects:
+ A pull request can't change the depth it is reviewed at. Changes to the file take effect after they merge into the target branch.
+ Each target branch needs its own copy of the file. For example, pull requests into `develop` use the file on `develop`, even if `main` has a different one.
+ You can keep the same file on every branch. Overrides on `target_branch` select the depth for each one.

For a review of a branch or commit that you request in chat, AWS DevOps Agent reads the file from the base branch if you name one. Otherwise, it reads the file from the reviewed branch or commit. Overrides on `target_branch` match only when you name a base branch.

When a review covers several repositories, the deepest depth that any repository requests applies.

If AWS DevOps Agent can't use the file, for example because it isn't valid YAML or sets an unsupported value, the review still runs. The agent chooses the depth and records the problem in the review's execution journal. If a rule has an unknown condition, the agent skips that rule and checks the remaining rules.

## Performing a code review
<a name="performing-a-code-review"></a>

You can request a code review on-demand through DevOps Agent chat:
+ "Review branch feature/payments on repo payment-service for release risks"
+ "Review commit abc123 on repo infrastructure for production risks"
+ "What release risks exist in the latest changes to repo order-service?"

The agent evaluates the specified scope — a branch, commit, or set of changes — and returns a report. The report includes:
+ **Recommended action** can be one of the following:
  + **BLOCK**: A critical risk was confirmed with high confidence or reproduced by testing. Resolve it before releasing.
  + **Deploy with Caution**: Actionable risks were found that do not meet the block threshold. Review them before releasing.
  + **Standard Deployment**: No actionable release risks were identified.
  + **Request Permissions**: The review could not complete because it lacked the access required to analyze the change. Grant the requested access and run the review again.
  + **Insufficient Data**: The review could not answer critical questions from the available change context. See the report's critical gaps for what was missing.
+ **Changes summary** — What was modified and the scope of impact
+ **Risk analysis** — Specific findings with affected code locations
+ **Recommendations** — Actionable steps to resolve each finding

Static code analysis reviews typically take about 5 minutes. Reviews that include verification testing typically take about 11 minutes. Review times depend on the size and complexity of the change.

## Automated code reviews
<a name="automated-code-reviews"></a>

Automated code reviews run without manual intervention. They can trigger in two contexts:

### Code reviews during code generation
<a name="code-reviews-during-code-generation"></a>

When using the Kiro Power or Claude Code plugin, the coding agent can request Code Change Risk Analysis as code is being generated. The review evaluates the in-progress changes against your policies and dependencies, surfacing findings directly in the IDE before the code is committed.

If issues are found, the coding agent is notified and can address them immediately — fixing policy violations, correcting over-permissioned IAM policies, or preparing dependent changes in other repositories.

### Code reviews in pull requests and merge requests
<a name="code-reviews-in-pull-requests-and-merge-requests"></a>

When automated PR/MR reviews are enabled, the agent reviews every new pull request and merge request in your connected repositories. Reviews trigger when:
+ A new PR/MR is opened
+ New commits are pushed to an existing PR/MR

By default, reviews trigger on all applicable events for all target branches. You can scope automated triggers to specific events (for example, only when a pull request or merge request becomes ready for review) and target branches by configuring trigger filters. For more information, see [Controlling when automated reviews trigger](#controlling-when-automated-reviews-trigger).

Findings appear as inline comments on the affected lines of code, with the overall assessment posted as a PR/MR comment. You can configure whether findings block merges (required status check) or are advisory only.

Each review posts a commit status named `aws-devops-agent/code-change-risk-analysis`. Reviews before November 17, 2026 posted `aws-devops-agent/release-readiness-review`; if you require that status check, update it to the new name. The status fails only when the recommended action is BLOCK; all other recommended actions pass. If a review fails, times out, or is canceled, the status passes and a comment asks you to review the change manually.

When you push new commits, the review focuses on what changed since the previous review and carries forward earlier findings that still apply. If the PR/MR was rebased onto a new base, the whole change is reviewed again. Findings that you already declined in a reply to an earlier comment on the same file, such as "won't fix" or "false positive", aren't posted again.

#### Public repository limitation
<a name="public-repository-limitation"></a>

Automated PR/MR code review triggers are only available for private repositories. DevOps Agent does not automatically review pull requests or merge requests on public repositories.

Because anyone can open a pull request against a public repository — including unknown external contributors — automatically triggering reviews on those PRs could consume resources without repository owner awareness or process untrusted content. Restricting automated triggers to private repositories ensures that only trusted collaborators initiate the review workflow.

If you use a public repository, you can still run Code Change Risk Analysis by requesting it through DevOps Agent chat or through coding agent integrations (Kiro Power, Claude Code plugin, or AWS Transform custom).

## Automatic verification testing
<a name="automatic-verification-testing"></a>

When a review that includes verification testing starts, DevOps Agent creates an AWS-managed verification environment and clones your code into it. The environment runs on dedicated compute resources with network restrictions that limit access to trusted services for build, artifact storage, and retrieval.

DevOps Agent reads your application's code and project files to determine the required build tools and dependencies, then installs them in the verification environment. After successfully building your application, the agent generates a testing plan and runs it to identify functional risks — such as edge cases that might result in failures or unexpected behavior.

**Important**  
** During verification testing, AWS DevOps Agent downloads the repositories that are referenced in your repository's README files and AGENTS.md files. To control which destinations the verification environment can reach, connect the verification environment to a VPC and control outbound traffic through your VPC routing. For instructions, see [Step 2: Configure Release Management environments for private VPC access (optional)](#step-2-configure-release-management-environments-for-private-vpc-access-optional).

Findings from verification testing are included in the final report alongside standards, dependency, and access-control findings.

You can use [agent instructions](about-aws-devops-agent-agent-instructions.md) (AGENTS.md) to tune how verification testing is performed — for example, specifying which test commands to run, what constitutes a passing build, or which parts of the application to exercise during verification.

### Reviewing verification test results
<a name="reviewing-verification-test-results"></a>

When a change has verification test results, you can review them in two places:
+ **In the console** — The change detail view includes a **Tests** tab whenever verification results exist. The tab lists the executed tests and their pass/fail outcomes, shown alongside the standards, dependency, and access-control findings so you can assess functional risk in context.
+ **From your source control** — If you review changes on a connected GitHub, GitLab, or Azure DevOps repository, the pull request or merge request comment also includes a **View test report** link. The link deep-links to the **Tests** tab for that change, so you can reach the results without leaving your code review workflow.

### Allowed network destinations
<a name="allowed-network-destinations"></a>

The verification testing environment has outbound network access restricted to a predefined allowlist. Your application can reach the following domains during validation:


| Domain | Purpose | 
| --- | --- | 
| .amazonaws.com, .aws.amazon.com | AWS services | 
| .public.ecr.aws | Amazon ECR Public | 
| .docker.com, .docker.io | Docker Hub | 
| .github.com, .githubusercontent.com | GitHub | 
| .gitlab.com | GitLab | 
| .npmjs.com, .npmjs.org | npm registry | 
| .pypi.org, .pypi.python.org, .pythonhosted.org | Python Package Index | 
| .crates.io, .rustup.rs | Rust packages | 
| .maven.org, .gradle.org | Java/Gradle packages | 
| .nuget.org | .NET packages | 
| .rubygems.org, .ruby-lang.org | Ruby packages | 
| .golang.org, .pkg.go.dev, .goproxy.io | Go packages | 
| .nodejs.org, .yarnpkg.com | Node.js | 
| .alpinelinux.org, .debian.org, .ubuntu.com, .centos.org, .fedoraproject.org | Linux distribution repositories | 
| .cloudfront.net | CloudFront distributions | 
| .google.com, .googleapis.com | Google APIs | 
| .microsoft.com, .visualstudio.com | Microsoft services | 
| .sourceforge.net, .bitbucket.org | Source hosting | 
| .prisma.sh | Prisma ORM | 
| get.helm.sh | Helm package manager | 
| .terraform.io | Terraform registry | 
| buf.build | Buf (Protobuf) | 
| .jitpack.io | JitPack (JVM packages) | 
| .scala-sbt.org | Scala SBT | 
| .sheetjs.com | SheetJS | 
| .confluent.io | Confluent (Kafka) | 
| .external-secrets.io | External Secrets Operator | 
| registry.npmmirror.com | npm mirror registry | 

**Note**  
** If your application requires network access to domains not on this list, connect your verification testing environment to a VPC. The environment then uses the routing and network firewall settings of your VPC, so you can allow access to the services that your application requires.

### Encrypting verification environments with a customer managed key
<a name="encrypting-verification-environments-with-a-customer-managed-key"></a>

Verification environments support customer managed keys in AWS Key Management Service (AWS KMS). For information about creating a customer managed key and setting its key policy, see [Encryption at rest for AWS DevOps Agent](aws-devops-agent-security-encryption-at-rest-for-devops-agent.md).

## Production context in code reviews
<a name="production-context-in-code-reviews"></a>

A code review uses read-only context from your running environment to assess how a change affects production. It doesn't need a separate setting. The agent uses the AWS accounts associated with your Agent Space and the custom Model Context Protocol (MCP) servers that you connect to it, and reads the following:
+ **AWS resources** – Reads Amazon CloudWatch metrics and alarms, and the configuration of resources in the AWS accounts associated with your Agent Space.
+ **Application topology** – Uses the resource [topology](about-aws-devops-agent-what-is-a-devops-agent-topology.md) of the AWS accounts associated with your Agent Space to find the resources that connect to the changed resource.
+ **MCP server tools** – Calls only allowlisted tools classified as `READ_ONLY` from the custom [MCP servers](configuring-integrations-and-knowledge-connecting-mcp-servers.md) that you connect.

The agent doesn't read log events, AWS Secrets Manager secret values, AWS Systems Manager parameter values, or application data such as Amazon S3 objects and Amazon DynamoDB items. It doesn't call operations that change resources. If your AWS Identity and Access Management (IAM) role denies a read, the review treats the check as unverifiable rather than as a finding.

## Repository content and external references
<a name="repository-content-and-external-references"></a>

During a Code Change Risk Analysis review, the agent reads content in your connected repositories. This includes code, README files, issues, and pull request or merge request comments. The agent might act on instructions or references that it finds in this content. During [automatic verification testing](#automatic-verification-testing), it might fetch referenced resources, such as external repositories or packages, from the [allowed network destinations](#allowed-network-destinations).

Repository content can contain malicious instructions that attempt to influence the agent. Connect only repositories that you trust.

To restrict outbound network access during automatic verification testing, use a Release Management environment connected to your own virtual private cloud (VPC). The verification testing environment's traffic then follows the routing and firewall rules in your VPC. For instructions on configuring Release Management environments for private VPC access, see [Step 2: Configure Release Management environments for private VPC access (optional)](#step-2-configure-release-management-environments-for-private-vpc-access-optional). You can also turn off automatic verification testing for a repository.

For more information about how security responsibilities are shared between AWS and you, see [Shared responsibility model](aws-devops-agent-security.md#shared-responsibility-model).

## Reviewing code review results
<a name="reviewing-code-review-results"></a>

Each code review produces a report accessible in the **Changes** page of the DevOps Agent web app. Reports include:
+ **Finding categories** — Policy violations, dependency risks, access-control issues, and test coverage gaps
+ **Severity levels** — Blocking (must fix before merge), Warning (should address), and Informational (awareness only)
+ **Execution journal** — The full trace of evaluation steps and tools used by the agent, providing transparency into how conclusions were reached

You can also ask follow-up questions in DevOps Agent chat: "Why did the review flag the IAM change in line 42?" or "What repositories depend on the API endpoint I modified?"

## Integrate with Kiro IDE and CLI
<a name="integrate-with-kiro-ide-and-cli"></a>

To use Code Change Risk Analysis in Kiro:

1. Install the [DevOps Agent Kiro Power](https://kiro.dev/launch/powers/add?name=aws-devops-agent) from the Kiro Power marketplace

1. The Power includes skills that instruct the coding agent when to request Code Change Risk Analysis — after significant code changes and before creating a PR

1. Findings surface directly in the IDE, and Kiro will offer to fix identified issues

From the Kiro CLI, you can also trigger reviews explicitly: the coding agent requests a review and incorporates findings into its workflow.

## Integrate with Claude Code
<a name="integrate-with-claude-code"></a>

To use Code Change Risk Analysis in Claude Code:

1. Install the [DevOps Agent Claude Code plugin](https://claude.com/plugins/aws-agents-for-devsecops) from the Claude Code plugin marketplace

1. The plugin connects Claude Code to your Agent Space and enables the coding agent to request Code Change Risk Analysis

1. During development, Claude Code can request a review of in-progress changes and address findings before committing

## Integrate with AWS Transform custom
<a name="integrate-with-aws-transform-custom"></a>

To use Code Change Risk Analysis in [AWS Transform custom](https://docs.aws.amazon.com/transform/latest/userguide/custom.html) :

1. Download the AWS DevOps Agent release readiness code review skill from the [AWS Transform custom samples repository](https://github.com/aws-samples/aws-transform-custom-samples/tree/main/client-side-skills/devops-agent-release-readiness-code-review) on GitHub.

1. Install the skill into your AWS Transform environment following the instructions in the repository README.

1. Once installed, the skill integrates with AWS Transform's code generation workflow. When Transform generates or modifies code, the skill requests a review of the proposed changes.

1. Review findings surface directly in the Transform output. If issues are identified, Transform can address them before finalizing the code change.

## Using code reviews in GitHub
<a name="using-code-reviews-in-github"></a>

Prerequisites: GitHub repository connected to your Agent Space with automated reviews enabled. For setup instructions, see [Configuring Code Review and Automated Testing](connecting-to-cicd-pipelines-connecting-github.md).
+ Reviews appear as inline comments on pull request diffs, with an overall status comment
+ Configure as a required status check to block merges when blocking findings exist

## Using code reviews in GitLab
<a name="using-code-reviews-in-gitlab"></a>

Prerequisites: GitLab project connected to your Agent Space with automated reviews enabled. For setup instructions, see [Configuring Code Review and Automated Testing](connecting-to-cicd-pipelines-connecting-gitlab.md).
+ Reviews appear as inline comments on merge request diffs, with an overall note
+ Blocking findings set the `aws-devops-agent/code-change-risk-analysis` commit status to failed

## Using code reviews in DevOps Agent chat
<a name="using-code-reviews-in-devops-agent-chat"></a>

From DevOps Agent chat, you can:
+ Request reviews of any branch, commit, or repository scope
+ Choose the review depth for a review: "Run a quick static review of branch feature/payments on repo payment-service" or "Review branch feature/payments on repo payment-service with verification testing." If you don't specify a depth, the review uses the repository's [review depth configuration](#configuring-review-depth).
+ Ask what the agent knows about your project's dependencies: "Which code bases interact with the service in the payments repo?"
+ Ask follow-up questions about specific findings
+ Request the agent generate a fix for an identified issue
+ View the dependency knowledge graph for your connected repositories

## Agentic safety guardrails
<a name="agentic-safety-guardrails"></a>

Code Change Risk Analysis includes built-in safety guardrails that prevent common unsafe agent behaviors. These guardrails are always active during the review process. Specific coverage and enforcement behavior may change as the feature evolves. While we aim to cover as many common unsafe behaviors as we can, some behaviors will not have corresponding guardrails in place.

### Credential exposure prevention
<a name="credential-exposure-prevention"></a>

The agent blocks any tool call where the tool input contains common credential patterns in plaintext, such as AWS keys, access tokens and private keys.

### Sensitive file exfiltration detection
<a name="sensitive-file-exfiltration-detection"></a>

The agent scans and blocks shell commands that combine access to sensitive file paths with network operations, preventing data exfiltration attempts.

### Mutative AWS operation blocking
<a name="mutative-aws-operation-blocking"></a>

The agent blocks any AWS API call that would modify your infrastructure. This prevents the review agent from making changes to your AWS environment during analysis. Read-only operations (describe, get, list) are permitted; mutative operations are blocked.

Read-only operations such as `describe_*`, `get_*`, and `list_*` are permitted.

### Sequential phase enforcement
<a name="sequential-phase-enforcement"></a>

Review phases must execute in sequence. This ensures systematic and thorough evaluation and prevents incomplete assessments from skipped steps.