# Remediate code review findings

After reviewing security findings from a code review, you can use AWS Security Agent to generate code fixes for findings in GitHub repository sources. For private repositories, AWS Security Agent opens a pull request with the proposed fix. For public repositories, AWS Security Agent attaches a downloadable diff to the finding that you can apply locally. Findings from S3 sources must be remediated manually.

## Prerequisites

Before you begin, ensure you have:

- A completed code review run with findings
- GitHub repositories connected as a source for the code review
- Access to the AWS Security Agent web application
- Familiarity with your application’s architecture and security requirements

## How code remediation works

When you trigger code remediation for a finding, AWS Security Agent analyzes the finding and its code locations, then generates a code fix. How the fix is delivered depends on the source:

- **Private GitHub repositories** – AWS Security Agent submits a pull request to the relevant repository. The pull request includes a description of the security issue and the changes made.
- **Public GitHub repositories** – AWS Security Agent attaches a suggested diff to the finding so the vulnerability isn’t disclosed before it’s fixed. You can download the diff from the web application and apply it locally with `git apply /path/to/code_remediation_changes.diff`.
- **S3 sources** – Code remediation is not available. Use the finding’s description, code locations, and risk reasoning to apply fixes manually.

###### Important

Pull requests created by AWS Security Agent are visible to all users who have read access to the repository. Review the changes before merging to ensure they align with your application’s requirements.

## Automatic code remediation

If you enabled **automatic code remediation** when creating the code review, AWS Security Agent generates fixes for all eligible findings as soon as the review completes. You don’t need to take any additional action — pull requests appear in your connected private GitHub repositories, and diffs appear on findings from public GitHub repositories, as the run finalizes.

## Manual code remediation

If automatic code remediation is disabled, you can trigger remediation for individual findings from GitHub sources.

1. Navigate to the **Findings** tab of a completed code review run.
2. Select the finding you want to remediate.
3. In the finding detail panel, choose **Remediate code**.
4. AWS Security Agent generates a code fix and either submits a pull request to the repository or attaches a downloadable diff to the finding, depending on the repository’s visibility.

## Review remediation pull requests

After AWS Security Agent submits a remediation pull request to a private GitHub repository:

1. Navigate to your GitHub repository.
2. Locate the pull request created by AWS Security Agent.
3. Review the changes, including:

   - The description explaining the security finding and fix
   - The code changes addressing the vulnerability
   - Any relevant context about the remediation approach

4. Merge the pull request if the fix is appropriate, or close it and implement an alternative solution.

###### Tip

After merging remediation pull requests, start a new code review run to verify that the fixes resolve the findings and don’t introduce new security issues.

## Apply remediation diffs

For findings from public GitHub repositories, apply the downloadable diff locally.

1. In the finding detail panel, download the diff from the **Code remediation** section.
2. In your local clone of the repository, run `git apply /path/to/code_remediation_changes.diff`.
3. Review the applied changes, test them against your application, and commit them through your normal development workflow.

## Limitations

- Code remediation is only available for findings from GitHub repository sources. Findings from S3 sources must be remediated manually.
- AWS Security Agent generates fixes based on its analysis of the vulnerability. Review all changes before merging or committing them to ensure they’re appropriate for your application.
- Some complex findings may require manual intervention beyond the automated fix.

## Next steps

After remediating findings:

- Review and merge pull requests in your GitHub repositories, or commit applied diffs through your normal workflow
- Run a new code review to verify fixes and check for remaining issues
- Resolve findings in the web application after confirming remediation
- Adjust your code review sources or settings as needed (see [Enable code review](enable-code-review-scan.md "enable-code-review-scan.md"))
