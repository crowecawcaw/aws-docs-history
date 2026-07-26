# Review code security findings in pull requests

After enabling code review for pull requests for your repositories, AWS Security Agent automatically analyzes pull requests and posts security findings directly in your source control provider. This allows developers to address security issues within their normal workflow without leaving the pull request.

###### Note

This page applies to GitHub pull requests, GitLab merge requests, and Bitbucket pull requests. The experience is similar across all providers.

## How code review works in pull requests

When you submit a pull request (or merge request in GitLab) in a repository with code review enabled, AWS Security Agent automatically begins analysis.

1. **Pull request analysis trigger** - Code review is triggered when a pull request is marked as "Ready for review" in repositories where you’ve enabled the code review capability. Draft pull requests are not analyzed.
2. **Analysis acknowledgment** - When AWS Security Agent begins analyzing your pull request, it posts an initial comment: "AWS Security Agent is analyzing your code…​" This lets you know the analysis has started and is in progress.
3. **Review completion** - After analysis completes, AWS Security Agent posts a review to your pull request with the results. All security findings are batched together in a single review to keep your pull request organized and minimize notifications.

## Understanding code review results

AWS Security Agent provides different types of results depending on what it finds during analysis.

### When security issues are found

If AWS Security Agent identifies security issues in your code changes, it posts a review that includes:

- **Summary** - A high-level overview of all security findings, describing the types of issues identified and their potential impact
- **Individual findings** - Detailed security findings appear as threaded comments under the main review, with each finding including:

  - Description of the security issue
  - Location in your code where the issue was found
  - Remediation guidance explaining how to address the issue
  - Relevant context based on your code review settings (security requirement violations, common vulnerabilities, or both)

###### Note

The types of security issues analyzed depend on your code review settings. If you configured security requirement validation, findings will reference your organization’s custom security requirements. If you configured security vulnerability findings, findings will identify common security vulnerabilities. For more information about code review settings, see [Enable pull request code review for GitHub repositories](enable-code-review.md "enable-code-review.md").

### When no security issues are found

If AWS Security Agent completes analysis and finds no security issues in your code changes, it posts a comment: "No issues identified." This confirms the review finished successfully and your code changes did not trigger any security findings based on your configured code review settings.

## Responding to security findings

After reviewing the security findings posted by AWS Security Agent, you can take action directly in your source control provider.

- **Address findings** - Update your code based on the remediation guidance provided in the findings, then push new commits to the pull request. AWS Security Agent will analyze the updated code.
- **Resolve conversations** - After addressing a security finding, mark the conversation as resolved to track your progress.

###### Tip

Each finding includes specific remediation guidance tailored to the security issue identified. Review this guidance carefully to understand the security risk and how to address it effectively.

## Filtering code review findings

You can customize how AWS Security Agent analyzes your code by adding a `filtering.md` file to your repository. This file allows you to reduce false positives by providing context about your codebase and excluding files or folders from analysis.

### Creating the filtering file

Create a file named `filtering.md` in the `.awssecurityagent` directory at the root of your repository:

```
.awssecurityagent/filtering.md
```

AWS Security Agent reads this file from the main branch of your repository (for example, `main` or `mainline`) when analyzing pull requests.

### File structure

The `filtering.md` file uses standard Markdown formatting with specific sections that AWS Security Agent recognizes. The file must include a `Code Review` heading followed by one or both of the following sections: `IgnorePatterns` and `ContextHints` (no space).

The following example shows the complete structure of a `filtering.md` file:

```
# filtering.md

## Code Review

### IgnorePatterns

**/*.md

/myapp/src/**/*.snap

/myapp/config/README

### ContextHints

- The backend is a trusted system and won't return non-standard protocols.
- URL is generated from server with presigned token, so no SSRF security vulnerabilities.
- AppSec has verified that we are allowed to use cache with an eviction policy.
```

### Ignore patterns

The `IgnorePatterns` section specifies files and folders that AWS Security Agent should skip during code review. Use `glob patterns` to define which paths to exclude from analysis.

Format requirements:

- Each pattern must be on its own line.
- Separate each pattern with an empty line between them. This ensures the file renders correctly when viewed in GitHub or code review tools.
- Patterns follow the standard glob format. For example, `**/*.md` matches all markdown files, and `/myapp/src/**/*.snap` matches all `.snap` files inside the `/myapp/src/` folder at the root.
- We support upto 1000 ignore patterns in this section.

### Context hints

The `ContextHints` section provides additional context about your codebase that helps AWS Security Agent make more accurate assessments. Use context hints to explain architectural decisions, security exceptions,
or other information that might affect how findings are interpreted.

Format requirements:

- Each hint must start with a dash (`-`) followed by a space.
- Write each hint as a single line of free-form text limited to 500 characters.
- Each hint should describe one specific piece of context about your codebase.
- We support upto 20 context hints in this section.

Context hints are applied after AWS Security Agent completes its initial analysis, helping to filter findings that don’t apply to your specific use case.

## Next steps

After reviewing code security findings:

- Update your code based on remediation guidance
- Push new commits to trigger re-analysis of your changes
- Adjust code review settings if needed (see [Enable pull request code review for GitHub repositories](enable-code-review.md "enable-code-review.md"))
- Review your organization’s security requirements to understand validation criteria
- Consider penetration testing for comprehensive security validation of deployed applications
