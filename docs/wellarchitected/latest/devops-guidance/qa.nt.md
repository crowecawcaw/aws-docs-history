# [QA.NT.1] Evaluate code quality through static testing

**Category:** FOUNDATIONAL

Static testing is a proactive method of assessing the quality of code without needing
to run it. It can be used to test application source code, as well as other design
artifacts, documentation, and infrastructure as code (IaC) files. Static testing allows
teams to spot misconfigurations, security vulnerabilities, or non-compliance with
organizational standards in these components before they get applied in a real environment.

Static testing should be available to developers on-demand in local environments, as
well as automatically run in automated pipelines. Use static testing to run automated code
reviews and detect defects early on to provide fast feedback to developers. This feedback
enables developers to fix and remove bugs before deployment, which is much easier and cost
effective than fixing them after deployment.

Use specialized static analysis tools tailored to the type of
code you are using. For example, tools
like [AWS CloudFormation Guard](../../../cfn-guard/latest/ug/what-is-guard.md "../../../cfn-guard/latest/ug/what-is-guard.md") and
[cfn-lint](https://github.com/aws-cloudformation/cfn-lint "https://github.com/aws-cloudformation/cfn-lint")
are designed to catch issues in
[AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") templates. These tools can be configured
to detect issues like insecure permissions, enforcing tagging
standards, or misconfigurations that could make infrastructure
vulnerable. Keep your static analysis tools updated and
regularly review their findings to adapt to changing
infrastructure security and compliance best practices.

**Related information:**

- [What
  is Amazon CodeGuru Reviewer?](../../../codeguru/latest/reviewer-ug/welcome.md "../../../codeguru/latest/reviewer-ug/welcome.md")
- [Checkov](https://www.checkov.io/ "https://www.checkov.io/")
