# Run a differential code scan with S3

Run a differential (diff) code scan to analyze only the changed lines in your source code, rather than performing a full repository scan. Differential scans are faster than full scans and produce findings targeted to specific code changes, making them ideal for pre-merge validation in development workflows.

Unlike pull request-based code review which is triggered automatically by third-party source control provider events (see [Review code security findings in pull requests](review-code-findings-github.md "review-code-findings-github.md")), differential scans are initiated programmatically through the AWS Security Agent API or SDK. You upload a unified diff file to S3 and reference it when starting a code review job.

## How differential scans work

A differential scan analyzes your code changes in the full context of your repository. When you create a code review resource with your source code uploaded to S3, the differential scan uses the complete repository as context while focusing findings specifically on the changed lines in your diff. This enables the scan to identify security issues that arise from how your changes interact with existing code — such as broken authentication flows, insecure data handling across modules, or changes that expose existing vulnerabilities.

The scan process:
. You upload a unified diff file (the output of `git diff`) to an S3 bucket connected to your Agent Space.
. You call the `StartCodeReviewJob` API with a `diffSource` parameter pointing to the S3 location of your diff.
. AWS Security Agent analyzes only the changed code in the diff for security vulnerabilities and compliance with your organization’s security requirements.
. Findings are scoped to the changed lines, with severity ratings, code locations, and remediation guidance.

## Prerequisites

Before you begin, ensure you have:

- An Agent Space with code review enabled (see [Enable code review](enable-code-review-scan.md "enable-code-review-scan.md"))
- A code review resource already created for the target repository, with the full source code uploaded to the S3 bucket connected to your Agent Space. The full repository provides context that enables deeper analysis of how your changes interact with existing code. See [Create a code review](perform-code-review-scan.md "perform-code-review-scan.md") for instructions on creating a code review and uploading source code.
- An S3 bucket connected to your Agent Space
- IAM permissions to upload to the S3 bucket and call `securityagent:StartCodeReviewJob`
- A unified diff file generated from your code changes (for example, the output of `git diff main..feature-branch`)

###### Tip

For the most accurate results, ensure your code review resource has the latest version of your full source code uploaded to S3. The diff scan uses this full repository as context to understand your application architecture, data flows, and existing security controls when analyzing the changed lines.

## Step 1: Generate a diff file

Generate a unified diff that represents the code changes you want to scan.

```
git diff main..feature-branch > changes.diff
```

Alternatively, generate a diff for staged changes:

```
git diff --cached > changes.diff
```

###### Tip

The diff file should be in standard unified diff format. AWS Security Agent parses the file paths and changed lines from the diff headers to scope its analysis.

## Step 2: Upload the diff to S3

Upload the diff file to an S3 bucket that is connected to your Agent Space.

```
aws s3 cp changes.diff s3://my-security-agent-bucket/diffs/changes.diff
```

###### Important

The S3 bucket must be one that is already connected to your Agent Space. The IAM service role associated with your Agent Space must have read access to this location. See [Enable code review](enable-code-review-scan.md "enable-code-review-scan.md") for instructions on connecting S3 buckets.

## Step 3: Start a differential code review job

Call the `StartCodeReviewJob` API with the `diffSource` parameter to initiate a differential scan.

### Using the AWS CLI

```
aws securityagent start-code-review-job \
  --agent-space-id "your-agent-space-id" \
  --code-review-id "your-code-review-id" \
  --diff-source '{"s3Uri": "s3://my-security-agent-bucket/diffs/changes.diff"}'
```

### Using the AWS SDK (Python)

```
import boto3

client = boto3.client('securityagent')

response = client.start_code_review_job(
    agentSpaceId='your-agent-space-id',
    codeReviewId='your-code-review-id',
    diffSource={
        's3Uri': 's3://my-security-agent-bucket/diffs/changes.diff'
    }
)

print(f"Job started: {response['codeReviewJobId']}")
```

### Using the AWS SDK (JavaScript/TypeScript)

```
import { SecurityAgentClient, StartCodeReviewJobCommand } from '@aws-sdk/client-securityagent';

const client = new SecurityAgentClient({ region: 'us-east-1' });

const response = await client.send(new StartCodeReviewJobCommand({
  agentSpaceId: 'your-agent-space-id',
  codeReviewId: 'your-code-review-id',
  diffSource: {
    s3Uri: 's3://my-security-agent-bucket/diffs/changes.diff',
  },
}));

console.log(`Job started: ${response.codeReviewJobId}`);
```

The API returns immediately with a `codeReviewJobId` and `status` of `IN_PROGRESS`.

## Step 4: Monitor the scan

Poll the code review job status until it completes.

```
aws securityagent get-code-review-job \
  --agent-space-id "your-agent-space-id" \
  --code-review-id "your-code-review-id" \
  --code-review-job-id "the-job-id"
```

The job progresses through the same phases as a full code review: Preflight → Static analysis → Finalizing. Differential scans typically complete faster than full scans because they analyze fewer lines of code.

## Step 5: Review findings

After the job completes, list findings for the code review job.

```
aws securityagent list-findings \
  --agent-space-id "your-agent-space-id" \
  --code-review-id "your-code-review-id" \
  --code-review-job-id "the-job-id"
```

Each finding includes:

- A description of the security issue
- The severity level (Critical, High, Medium, or Low)
- Code locations referencing specific lines in the diff
- Risk reasoning explaining the potential impact
- Remediation guidance

For more information about understanding and acting on findings, see [Review findings from a code review](review-code-scan-findings.md "review-code-scan-findings.md").

## Quotas and limits

- Maximum number of changed files in a diff: 3,000 files or 5 MB total diff size
- Findings are capped at 30 per scan, prioritized by severity (Critical > High > Medium > Low)

## Next steps

After running a differential scan:

- Review findings and apply remediation guidance (see [Review findings from a code review](review-code-scan-findings.md "review-code-scan-findings.md"))
- Enable pull request comments for automated code review on every pull request (see [Enable pull request code review for GitHub repositories](enable-code-review.md "enable-code-review.md"))
- Run a full code review periodically to catch issues outside of individual changes (see [Create a code review](perform-code-review-scan.md "perform-code-review-scan.md"))
- Use the IDE integration to run differential scans directly from your development environment (see [Run code security scans from your IDE](code-review-ide-integration.md "code-review-ide-integration.md"))
