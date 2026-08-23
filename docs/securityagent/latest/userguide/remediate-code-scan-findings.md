# Remediate code review findings

After reviewing security findings from a code review, you can use AWS Security Agent to generate code fixes. Supported sources include connected third-party source code providers (such as GitHub, GitLab, or Bitbucket) and Amazon S3. For a connected private repository, AWS Security Agent opens a pull request (or a merge request, for GitLab) with the proposed fix. For Amazon S3 sources, it attaches a downloadable code diff that you can apply locally. For the list of supported providers and how to connect them, see [How integrations work with Agent Spaces](about-integrations.md "about-integrations.md").

## Prerequisites

Before you begin, ensure you have:

- A completed code review run with findings
- A source for the code review — a connected source code repository (see [How integrations work with Agent Spaces](about-integrations.md "about-integrations.md")) or source code uploaded to Amazon S3
- Access to the AWS Security Agent web application
- Familiarity with your application’s architecture and security requirements

## How code remediation works

When you trigger code remediation for a finding, AWS Security Agent analyzes the finding and its code locations, then generates a code fix. How the fix is delivered depends on the source:

- **Connected private repository** – AWS Security Agent opens a pull request (or a merge request, for GitLab) on the repository. It includes a description of the security issue and the changes made. This applies to the source code providers you’ve connected — see [How integrations work with Agent Spaces](about-integrations.md "about-integrations.md").
- **Amazon S3 source** – AWS Security Agent attaches a suggested code diff to the finding. Because there’s no connected repository to open a pull request against, download the code diff from the web application and apply it locally with `git apply /path/to/code_remediation_changes.diff`.
- **Public repository** – To avoid disclosing the vulnerability before it’s fixed, AWS Security Agent doesn’t open a pull request. Delivery depends on the provider. For example, public GitHub repositories receive a downloadable code diff. Automated remediation isn’t available for public GitLab or Bitbucket repositories. See the provider’s connection topic for details.

###### Important

Pull requests created by AWS Security Agent are visible to all users who have read access to the repository. Review the changes before merging to ensure they align with your application’s requirements.

## Automatic code remediation

If you enabled **automatic code remediation** when creating the code review, AWS Security Agent generates fixes for all eligible findings as soon as the review completes. You don’t need to take any additional action. AWS Security Agent delivers each fix the same way as an on-demand fix, using the delivery methods described earlier in this topic.

Automatic code remediation covers both connected source code repositories and Amazon S3 sources.

## Manual code remediation

You can trigger remediation for an individual finding on demand, whether its source is a connected repository or an Amazon S3 upload. Use this when automatic code remediation is disabled, or to remediate a specific finding.

1. Navigate to the **Findings** tab of a completed code review run.
2. Select the finding you want to remediate.
3. In the finding detail panel, choose **Remediate code**.
4. AWS Security Agent generates a code fix and delivers it based on the source: a pull request or merge request for a connected private repository, or a downloadable code diff for an Amazon S3 source.

## Review remediation pull requests

After AWS Security Agent submits a remediation pull request (or merge request) to a connected private repository:

1. Navigate to the repository on your source code provider.
2. Locate the pull request (or merge request) created by AWS Security Agent.
3. Review the changes, including:

   - The description explaining the security finding and fix
   - The code changes addressing the vulnerability
   - Any relevant context about the remediation approach

4. Merge the pull request if the fix is appropriate, or close it and implement an alternative solution.

###### Tip

After merging remediation pull requests, start a new code review run to verify that the fixes resolve the findings and don’t introduce new security issues.

## Apply remediation diffs

For findings delivered as a downloadable code diff (Amazon S3 sources, and public repositories where supported), apply the diff locally.

1. In the finding detail panel, download the code diff from the **Code remediation** section.
2. In your local copy of the source code, run `git apply /path/to/code_remediation_changes.diff`.
3. Review the applied changes, test them against your application, and commit them through your normal development workflow.

## Limitations

- Code remediation is available for findings from connected source code repositories and Amazon S3 sources, both automatically and on demand. For public repositories, availability varies by provider — see [How integrations work with Agent Spaces](about-integrations.md "about-integrations.md") and the provider’s connection topic.
- AWS Security Agent generates fixes based on its analysis of the vulnerability. Review all changes before merging or committing them to ensure they’re appropriate for your application.
- Some complex findings may require manual intervention beyond the automated fix.

## Next steps

After remediating findings:

- Review and merge pull requests (or merge requests) in your connected repositories, or commit applied diffs through your normal workflow
- Run a new code review to verify fixes and check for remaining issues
- Resolve findings in the web application after confirming remediation
- Adjust your code review sources or settings as needed (see [Enable code review](enable-code-review-scan.md "enable-code-review-scan.md"))
