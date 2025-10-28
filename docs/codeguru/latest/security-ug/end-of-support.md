On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# End of support for CodeGuru Security

On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the CodeGuru Security console, service
resources, or documentation.

Code analysis capabilities are available through other AWS services. This page explains the
ways you can use other services to review your code for security and quality issues.

## Run code reviews with Amazon Q Developer

Amazon Q Developer includes code review capabilities such as static code analysis for security
vulnerabilities and best practices (SAST), secrets exposure detection, dependency vulnerability
detection (SCA), and code quality issue detection.

You can review code with the IDE plugin, or in your GitHub and GitLab Duo repositories. For
more information on reviewing code in the IDE, see [Reviewing code
with Amazon Q Developer](../../../amazonq/latest/qdeveloper-ug/code-reviews.md "../../../amazonq/latest/qdeveloper-ug/code-reviews.md") in the _Amazon Q Developer User Guide_. For more information on reviewing code in GitHub, see
[Reviewing
code in GitHub](../../../amazonq/latest/qdeveloper-ug/github-code-reviews.md "../../../amazonq/latest/qdeveloper-ug/github-code-reviews.md"). For more information on reviewing for in GitLab Duo, see
[GitLab
quick actions](../../../amazonq/latest/qdeveloper-ug/gitlab-concepts.md#gitlab-concepts-quick-actions "../../../amazonq/latest/qdeveloper-ug/gitlab-concepts.md#gitlab-concepts-quick-actions").

## Run code scans with Amazon Inspector

Amazon Inspector automatically discovers code repositories in GitHub and GitLab and scans
them for software vulnerabilities and unintended network exposure.

For more information about scanning your code with Amazon Inspector, see [Amazon Inspector Code Security](../../../inspector/latest/user/code-security-assessments.md "../../../inspector/latest/user/code-security-assessments.md") in the
_Amazon Inspector User Guide_

## What happens to my existing code scans?

When the CodeGuru Security service is no longer supported, you will lose access to all historical
code review data. You cannot migrate existing scans or findings to other AWS code
review services. In applicable integrations, download any code scan findings that you want to
save.

To generate new code findings your source code, you can run a review on your code using the
options described on this page.
