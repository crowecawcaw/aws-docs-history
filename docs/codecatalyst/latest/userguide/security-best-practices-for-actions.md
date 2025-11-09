Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Best practices for workflow actions in Amazon CodeCatalyst

There are a number of security best practices to consider as you develop your workflows in
CodeCatalyst. The following are general guidelines and don’t represent a complete security solution.
Because these best practices might not be appropriate or sufficient for your environment, treat
them as helpful considerations rather than prescriptions.

###### Topics

- [Sensitive information](#sensitive-info "#sensitive-info")
- [Licensing terms](#licensing-terms "#licensing-terms")
- [Untrusted code](#untrusted-code "#untrusted-code")
- [GitHub Actions](#github-actions "#github-actions")

## Sensitive information

Do not embed sensitive information in your YAML. Rather than embedding credentials, keys, or
tokens in your YAML, we recommend you use CodeCatalyst secrets. Secrets provide an easy way to store
and reference sensitive information from within your YAML.

## Licensing terms

Make sure to pay attention to the licensing terms of the action you choose to use.

## Untrusted code

Actions are generally self-contained, single purpose modules that can be shared across a
project, space, or the broader community. Using code from others can be a great
convenience and efficiency gain, but also introduces a new threat vector. Review the following
sections to ensure you’re following best practices to keep your CI/CD workflows secure.

## GitHub Actions

GitHub Actions are open source, built and maintained by the community. We follow the [shared responsibility
model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") and consider GitHub Actions source code as customer data for which you are
responsible. GitHub Actions can be granted access to secrets, repository tokens, source code,
account links, and your compute time. Make sure you are confident in the trustworthiness and
security of the GitHub Actions you plan to run.

More specific guidance and security best practices for GitHub Actions:

- [Security hardening](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions "https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions")
- [Preventing pwn requests](https://securitylab.github.com/research/github-actions-preventing-pwn-requests/ "https://securitylab.github.com/research/github-actions-preventing-pwn-requests/")
- [Untrusted input](https://securitylab.github.com/research/github-actions-untrusted-input/ "https://securitylab.github.com/research/github-actions-untrusted-input/")
- [How to trust your building blocks](https://securitylab.github.com/research/github-actions-building-blocks/ "https://securitylab.github.com/research/github-actions-building-blocks/")
