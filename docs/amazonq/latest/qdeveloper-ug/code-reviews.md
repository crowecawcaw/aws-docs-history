# Reviewing code with Amazon Q Developer

Amazon Q Developer can review your codebase for security vulnerabilities and code quality issues
to improve the posture of your applications throughout the development cycle. You can review
an entire codebase, analyzing all files in your local project or workspace, or review a
single file. You can also enable auto reviews that assess your code as you write it.

Reviews are powered by both generative AI and rule-based automatic reasoning. [Amazon Q detectors](../../../codeguru/detector-library.md "../../../codeguru/detector-library.md"), informed
by years of AWS and Amazon.com security best practices, power the rule-based security and
quality reviews. As security policies are updated and detectors are added, reviews
automatically incorporate new detectors to ensure your code is compliant with the most
up-to-date policies.

For information on supported IDEs for this feature, see [Supported IDEs](q-in-IDE.md#supported-ides-features "q-in-IDE.md#supported-ides-features"). For information on supported languages, see
[Language support for code reviews](q-language-ide-support.md#code-reviews-language-support "q-language-ide-support.md#code-reviews-language-support").

###### Topics

- [How it works](#how-code-reviews-work "#how-code-reviews-work")
- [Types of code issues](#issue-types "#issue-types")
- [Quotas](#quotas "#quotas")
- [Starting a code review with Amazon Q Developer](start-review.md "start-review.md")
- [Addressing code issues with Amazon Q Developer](address-code-issues.md "address-code-issues.md")
- [Filtering code issues](filter-code-issues.md "filter-code-issues.md")
- [Code issue severity in Amazon Q Developer code reviews](code-issue-severity.md "code-issue-severity.md")

## How it works

During a code review, Amazon Q assesses both your custom code and third-party libraries
in your code. Before starting a code review, Amazon Q applies filtering to ensure that
only relevant code is reviewed. As part of the filtering process, Amazon Q excludes
unsupported languages, test code, and open source code.

Amazon Q can either review your recent code changes, or an entire file or project. To
initiate a review, you open your code folder in your IDE, and then ask Amazon Q to
review your code from the chat panel.

By default, if you simply ask Amazon Q to review your code, it will review only the
code changes in the active file in your IDE. Code changes are determined by the output
of the `git diff` command on your file. If there is no diff file is present, Amazon Q will
review the entire code file. If no file is open, it will search for any code changes in
the project to review.

Similarly, if you ask Amazon Q to review your entire project or workspace, it will
first attempt to review your code changes. If there is no diff file present, it will
review your entire codebase.

## Types of code issues

Amazon Q reviews your code for the following types of code issues:

- **SAST scanning — Detect security vulnerabilities
  in your source code.** Amazon Q identifies various security issues,
  such as resource leaks, SQL injection, and cross-site scripting.
- **Secrets detection — Prevent the exposure of
  sensitive or confidential information in your code.** Amazon Q
  reviews your code and text files for secrets such as hardcoded passwords,
  database connection strings, and usernames. Secrets findings include information
  about the unprotected secret and how to protect it.
- **IaC issues — Evaluate the security posture of
  your infrastructure files.** Amazon Q can review your infrastructure
  as code (IaC) code files to detect misconfiguration, compliance, and security
  issues.
- **Code quality issues — Ensure your code is meeting
  quality, maintainability, and efficiency standards.** Amazon Q
  generates code issues related to various quality issues, including but not
  limited to performance, machine learning rules, and AWS best practices.
- **Code deployment risks — Assess risks related to
  deploying code.** Amazon Q determines if there are any risks to deploying
  or releasing your code, including application performance and disruption to
  operations.
- **Software composition analysis (SCA) — Evaluate
  third-party code.** Amazon Q examines third-party components,
  libraries, frameworks, and dependencies integrated into your code, ensuring
  third-party code is secure and up to date.

For a complete list of the detectors Amazon Q uses to review your code, see the
[Amazon Q Detector
Library](../../../codeguru/detector-library.md "../../../codeguru/detector-library.md").

## Quotas

Amazon Q security scans maintain the following quotas:

- **Input artifact size** – The maximum size of all
  the files within an IDE project workspace, including third-party libraries,
  build JAR files, and temporary files.
- **Source code size** – The maximum size of the
  source code that Amazon Q scans after filtering all third-party libraries and
  unsupported files.

The following table describes the quotas maintained for auto scans and full project scans.

| Resource            | Auto reviews | File or project reviews |
| ------------------- | ------------ | ----------------------- |
| Input artifact size | 200 KB       | 500 MB                  |
| Source code size    | 200 KB       | 50 MB                   |
