# Review code security findings in GitHub

After enabling code review for your repositories, AWS Security Agent automatically analyzes pull requests and posts security findings directly in GitHub. This allows developers to address security issues within their normal workflow without leaving the pull request.

## How code review works in GitHub

When you submit a pull request in a repository with code review enabled, AWS Security Agent automatically begins analysis.

1. **Pull request analysis trigger** - Code review is triggered when a pull request is marked as "Ready for review" in repositories where you’ve enabled the code review capability. Draft pull requests are not analyzed.
2. **Analysis acknowledgment** - When AWS Security Agent begins analyzing your pull request, it posts an initial comment: "AWS Security Agent is analyzing your code…​" This lets you know the analysis has started and is in progress.
3. **Review completion** - After analysis completes, AWS Security Agent posts a review to your pull request with the results. All security findings are batched together in a single review to keep your pull request organized and minimize notifications.

## Understanding code review results

AWS Security Agent provides different types of results depending on what it finds during analysis.

### When security issues are found

If AWS Security Agent identifies security issues in your code changes, it posts a review that includes:

- **Summary** - A high-level overview of all security findings at the top of the review, describing the types of issues identified and their potential impact
- **Individual findings** - Detailed security findings appear as threaded comments under the main review, with each finding including:
  - Description of the security issue
  - Location in your code where the issue was found
  - Remediation guidance explaining how to address the issue
  - Relevant context based on your code review settings (security requirement violations, common vulnerabilities, or both)

###### Note

The types of security issues analyzed depend on your code review settings. If you configured security requirement validation, findings will reference your organization’s custom security requirements. If you configured security vulnerability findings, findings will identify common security vulnerabilities. For more information about code review settings, see [Enable code review capability for a GitHub repository](enable-code-review.md "enable-code-review.md").

### When no security issues are found

If AWS Security Agent completes analysis and finds no security issues in your code changes, it posts a comment: "No issues identified." This confirms the review finished successfully and your code changes did not trigger any security findings based on your configured code review settings.

## Responding to security findings

After reviewing the security findings posted by AWS Security Agent, you can take action directly in GitHub.

- **Address findings** - Update your code based on the remediation guidance provided in the findings, then push new commits to the pull request. AWS Security Agent will analyze the updated code.
- **Resolve conversations** - After addressing a security finding, mark the conversation as resolved in GitHub to track your progress.

###### Tip

Each finding includes specific remediation guidance tailored to the security issue identified. Review this guidance carefully to understand the security risk and how to address it effectively.

## Next steps

After reviewing code security findings:

- Update your code based on remediation guidance
- Push new commits to trigger re-analysis of your changes
- Adjust code review settings if needed (see [Enable code review capability for a GitHub repository](enable-code-review.md "enable-code-review.md"))
- Review your organization’s security requirements to understand validation criteria
- Consider penetration testing for comprehensive security validation of deployed applications
