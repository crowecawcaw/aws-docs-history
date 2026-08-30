# Run code security scans from your IDE

Run code security scans directly from your IDE using Kiro or Claude Code. The IDE integration lets you scan your local source code for security vulnerabilities, run differential scans on only changed code, and perform threat model reviews on design documents — all without leaving your development environment. Findings appear alongside your code with remediation guidance, and you can apply automated fixes directly from the IDE.

## How IDE integration works

The IDE integration uses the AWS Security Agent MCP (Model Context Protocol) server to connect your IDE to the AWS Security Agent service:

1. The MCP server packages your source code into a ZIP archive.
2. The archive is uploaded to an S3 bucket that the server auto-provisions in your AWS account.
3. The server calls the AWS Security Agent API to start a scan.
4. AWS Security Agent analyzes the code for security vulnerabilities and compliance with your organization’s security requirements.
5. Findings are returned to the IDE with code locations, descriptions, severity ratings, and remediation suggestions.

The MCP server handles all orchestration — Agent Space provisioning, S3 bucket creation, IAM role setup, code packaging, and scan polling — so you only need AWS credentials configured locally.

###### Note

The only prerequisite is AWS credentials configured in your local environment (for example, through `aws configure`, AWS SSO, or environment variables). The MCP server auto-provisions the Agent Space, IAM service role, and S3 bucket on first use.

## Prerequisites

Before you begin, ensure you have:

- AWS credentials configured locally with the following permissions:

  - `iam:CreateRole`, `iam:PutRolePolicy` (for one-time setup of the service role)
  - `s3:CreateBucket`, `s3:PutObject`, `s3:PutPublicAccessBlock`, `s3:PutLifecycleConfiguration`
  - `securityagent:CreateAgentSpace`, `securityagent:UpdateAgentSpace`, `securityagent:ListAgentSpaces`, `securityagent:BatchGetAgentSpaces`
  - `securityagent:CreateCodeReview`, `securityagent:StartCodeReviewJob`, `securityagent:BatchGetCodeReviewJobs`
  - `securityagent:ListFindings`, `securityagent:BatchGetFindings`
  - `securityagent:StartCodeRemediation` (for automated fixes)
  - `sts:GetCallerIdentity`

- [uv](https://docs.astral.sh/uv/getting-started/installation/ "https://docs.astral.sh/uv/getting-started/installation/") installed (Python package runner)
- Python 3.10 or later
- One of the following IDEs:

  - [Kiro](https://kiro.dev "https://kiro.dev") (install the AWS Security Agent Power)
  - Claude Code (install the AWS Security Agent plugin)

## Install the MCP server

### Kiro

Install the **AWS Security Agent** Power from the Kiro marketplace. The Power bundles the MCP server configuration, steering instructions, and lifecycle hooks for automatic security scan suggestions.

Alternatively, configure the MCP server manually in your project’s `.kiro/mcp.json`:

```
{
  "mcpServers": {
    "security-agent": {
      "command": "uvx",
      "args": ["awslabs.security-agent-mcp-server@latest"],
      "env": {
        "AWS_PROFILE": "default",
        "AWS_REGION": "us-east-1",
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    }
  }
}
```

### Claude Code

Install the AWS Security Agent plugin, which provides skills for setup, full scans, diff scans, threat model reviews, and remediation.

Configure the MCP server in your project’s `.mcp.json`:

```
{
  "mcpServers": {
    "awslabs.security-agent-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.security-agent-mcp-server@latest"],
      "env": {
        "AWS_PROFILE": "default",
        "AWS_REGION": "us-east-1",
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    }
  }
}
```

###### Tip

You can also run the MCP server via Docker if you prefer not to install Python locally. See the [MCP server documentation](https://github.com/awslabs/mcp "https://github.com/awslabs/mcp") for Docker configuration.

## First-time setup

On first use, the MCP server automatically provisions the required AWS resources:

| Resource         | Name convention                           | Purpose                                                        |
| ---------------- | ----------------------------------------- | -------------------------------------------------------------- |
| Agent Space      | User-chosen or auto-created               | Container for scans, reviews, and penetration tests            |
| IAM service role | `SecurityAgentScanRole`                   | Assumed by `securityagent.amazonaws.com` to read uploaded code |
| S3 bucket        | `security-agent-scans-{account}-{region}` | Stores zipped source code (30-day auto-expiry lifecycle)       |

To trigger setup explicitly, ask your IDE:

```
Set up the security agent
```

The setup verifies your AWS credentials, creates or reuses an Agent Space, provisions the IAM role and S3 bucket, and confirms readiness. If you already have Agent Spaces from the AWS Management Console, the setup shows them and asks which one to use.

###### Note

Setup runs automatically on your first scan if not already configured. You don’t need to run it separately.

## Run a full security scan

Scan your entire project for security vulnerabilities:

```
Scan this project for security issues
```

The IDE:

1. Archives your source code (excluding `.git`, `node_modules`, build artifacts, and other non-essential directories)
2. Uploads the archive to S3
3. Starts a full code review job
4. Polls for completion (typically around 1 hour)
5. Presents findings grouped by severity

### Scan progress

Full scans typically take around 1 hour depending on codebase size. The IDE checks progress every 5 minutes and notifies you when results are ready. You can ask for status at any time:

```
How's the scan going?
```

## Run a differential scan

For faster feedback during development, scan only the code that changed since a git ref:

```
Scan my changes against main for security issues
```

By default, if you don’t specify a base ref, the scan compares your uncommitted changes against `HEAD`. You can explicitly specify a different base:

```
Diff scan my uncommitted changes
```

Differential scans upload both the full repository context and the git diff patch, then run analysis focused only on the changed lines. Results typically arrive in 5–15 minutes.

For more information about the S3 diff scan API, see [Run a differential code scan with S3](run-diff-scan-s3.md "run-diff-scan-s3.md").

## Run a threat model review

Analyze design documents for security-posture changes using STRIDE methodology:

```
Run a threat model review on my spec
```

The IDE identifies your `requirements.md` and `design.md` files (typically under `.kiro/specs/`), uploads them alongside your source code, and runs a threat model analysis. Results identify:

- Security threats categorized by STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege)
- Severity ratings for each threat
- Impact on specific assets in your codebase
- Recommendations for mitigation

###### Tip

Run a threat model review before generating implementation tasks from a spec. This catches security design issues before code is written.

## Review findings

When a scan completes, findings appear in your IDE grouped by severity:

```
🟣 CRITICAL: SQL Injection in user-service.ts
   File: src/api/user-service.ts:45
   User input flows directly into SQL query without parameterization

🔴 HIGH: Hardcoded credentials in config.ts
   File: src/config/database.ts:12
   Database password stored in source code
```

A detailed report is also written to `.security-agent/findings-{scan_id}.md` with full information for each finding including risk type, confidence score, code locations, and remediation code.

To view findings from a previous scan:

```
Show my security findings
```

## Apply automated fixes

After reviewing findings, apply automated remediation:

```
Fix the security findings
```

The IDE works through findings top-down by severity (Critical → High → Medium → Low), applying code fixes using the remediation guidance from each finding. After all fixes are applied, it automatically runs a verification diff scan to confirm the issues are resolved.

You can also fix individual findings:

```
Fix the SQL injection in user-service.ts
```

###### Important

Always review automated fixes before committing. Verify that fixes don’t break existing functionality or introduce regressions.

## Automatic scan suggestions (Kiro)

When using the Kiro Power, AWS Security Agent can automatically suggest diff scans after you make security-sensitive code changes. The Power installs a hook that evaluates each completed coding turn and suggests a scan when changes affect:

- Authentication or authorization logic
- Cryptography or secrets handling
- Input validation or data sanitization
- Network requests or external integrations
- Security configuration (CORS, headers, session handling)

You can opt out of automatic suggestions at any time by deleting `.kiro/hooks/security-diff-scan-suggester.kiro.hook`.

## Available scan types

| Scan type    | Duration      | Use case                                 | Command                                       |
| ------------ | ------------- | ---------------------------------------- | --------------------------------------------- |
| Full scan    | Around 1 hour | Comprehensive review of entire codebase  | "Scan my project for security issues"         |
| Diff scan    | 5–15 minutes  | Changed code only (pre-commit, pre-PR)   | "Scan my changes" or "Diff scan against main" |
| Threat model | 5–30 minutes  | Design docs (requirements.md, design.md) | "Run a threat model review on my spec"        |

## Environment variables

| Variable            | Description                                        | Default         |
| ------------------- | -------------------------------------------------- | --------------- |
| `AWS_REGION`        | AWS region for SecurityAgent API calls             | `us-east-1`     |
| `AWS_PROFILE`       | AWS credential profile name                        | Default profile |
| `FASTMCP_LOG_LEVEL` | MCP server log level (DEBUG, INFO, WARNING, ERROR) | `WARNING`       |

## Troubleshooting

### "Not configured. Run setup first."

Your `.security-agent/config.json` is missing or the Agent Space no longer exists. Ask the IDE to run setup:

```
Set up the security agent
```

### Scan fails with AccessDenied

Ensure your AWS credentials have the required IAM permissions listed in the Prerequisites section. The most common missing permission is `iam:CreateRole` (needed only for first-time setup).

### Scan times out or takes too long

- Full scans on large codebases can take more than 1 hour
- Use differential scans for iterative development — they complete in minutes
- Check that your source archive doesn’t include unnecessary directories (the MCP server excludes common patterns automatically)

### Empty diff — no changes to scan

If you run a diff scan with no uncommitted changes, the MCP server reports "No changes vs HEAD" and does not start a scan. Commit or stage your changes first, or specify a different base ref.

## Quotas and limits

- Maximum source archive size: 2 GB
- S3 bucket lifecycle: uploaded code auto-deleted after 30 days

## Next steps

After running your first IDE security scan:

- Enable pull request code review comments for automated GitHub integration (see [Enable pull request code review for GitHub repositories](enable-code-review.md "enable-code-review.md"))
- Configure security requirements for organization-specific policy validation (see [Manage security requirements](security-requirements.md "security-requirements.md"))
- Run periodic full scans to catch issues across your entire codebase (see [Create a code review](perform-code-review-scan.md "perform-code-review-scan.md"))
- Use threat model reviews on new feature specs before implementation
