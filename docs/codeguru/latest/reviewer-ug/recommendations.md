Starting November 7, 2025, you will not be able to create new repository associations in Amazon CodeGuru Reviewer. If you would like to use the service, create repository associations prior to November 7, 2025. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](codeguru-reviewer-availability-change.md "codeguru-reviewer-availability-change.md").

# Recommendation types in CodeGuru Reviewer

Amazon CodeGuru Reviewer recommends various kinds of fixes in your Java and Python code. These
recommendations are based on common code scenarios and might not apply to all cases.

If you don't agree with a recommendation, you can [provide
feedback](provide-feedback.md "provide-feedback.md") in the CodeGuru Reviewer console or by commenting on the code in the pull requests.
Any positive or negative feedback can be used to help improve the performance of CodeGuru Reviewer so
that recommendations get better over time.

If you want to suppress recommendations from CodeGuru Reviewer, you can create and add to the root
directory of your repository an `aws-codeguru-reviewer.yml` file that lists files and
directories to exclude from analysis. For more information, see [Suppress
recommendations](recommendation-suppression.md "recommendation-suppression.md").

The following content describes the secrets detection functionality of CodeGuru Reviewer. For
information about the other recommendation types and the detectors that CodeGuru Reviewer uses, see the
[Amazon CodeGuru Reviewer Detector
Library](../../detector-library/index.md "../../detector-library/index.md").

## Secrets detection

CodeGuru Reviewer integrates with AWS Secrets Manager to use a secrets detector that finds unprotected
secrets in your code. Secrets detection is automatic, so you don't need to turn it on.

The secrets detector searches for hardcoded passwords, database connection strings,
user names, and more. When an unprotected secret is found during a code review, CodeGuru Reviewer
generates a recommendation and displays it with your code reviews. The recommendation
tells you about the unprotected secret. To immediately protect that secret, choose
**Protect your credential** in the code review. This opens the
Secrets Manager console to protect and manage the secret. For more information, see the [AWS Secrets Manager User Guide](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") and [View recommendations and provide
feedback](give-feedback-from-code-review-details.md "give-feedback-from-code-review-details.md").

###### Topics

- [Secrets detection supported file
  types](#secrets-file-extension-support "#secrets-file-extension-support")
- [Types of secrets detected by CodeGuru Reviewer](#secrets-found-types "#secrets-found-types")

### Secrets detection supported file

types

The secrets detector finds unprotected secrets the following file types with a
maximum file size of 100kb.

- Config files (\*.config, \*.cfg, \*.conf, \*.cnf, \*.cf)
- Environment files (\*.env)
- HTML files (\*.html)
- Initialization files (\*.ini)
- Java files (\*.java)
- JSON files (\*.json)
- Jupyter Notebook files (\*.ipynb)
- Key files (\*.key)
- Markdown files (\*.md)
- Privacy Enhanced Mail files (\*.pem)
- Property List files (\*.plist)
- Python files (\*.py)
- reStructuredText files (\*.rst)
- Text files (\*.txt, \*.text)
- TOML files (\*.toml)
- XML files (\*.xml)
- YAML files (\*.yml, \*.yaml)

### Types of secrets detected by CodeGuru Reviewer

Amazon CodeGuru Reviewer detects unprotected usernames, passwords, RSA keys, and the following
secrets.

| Secrets detected by CodeGuru Reviewer | Provider                                                                                                                                                                                             | Secrets detected |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| Amazon Web Services (AWS)             | <br>• Amazon AWS Secret Access Key                                                                                                                                                                   |
| Atlassian                             | <br>• Atlassian API Token <br>• Atlassian JSON Web Token <br>• Bitbucket Server Personal Access Token                                                                                                |
| Databricks                            | <br>• Databricks Access Token                                                                                                                                                                        |
| Datadog                               | <br>• Datadog API Key <br>• Datadog App Key                                                                                                                                                          |
| GitHub                                | <br>• GitHub Personal Access Token <br>• GitHub OAuth Access Token <br>• GitHub Refresh Token <br>• GitHub App Installation Access Token <br>• GitHub SSH Private Key                                |
| Intercom                              | <br>• Intercom Access Token                                                                                                                                                                          |
| Mailchimp                             | <br>• Mailchimp API Key                                                                                                                                                                              |
| Mailgun                               | <br>• Mailgun API Key                                                                                                                                                                                |
| Salesforce                            | <br>• Private Key                                                                                                                                                                                    |
| SendGrid                              | <br>• SendGrid API Key                                                                                                                                                                               |
| Shopify                               | <br>• Shopify App Shared Secret <br>• Shopify Access Token <br>• Shopify Custom App Access Token <br>• Shopify Private App Password                                                                  |
| Slack                                 | <br>• Client ID <br>• Client Secret                                                                                                                                                                  |
| Stripe                                | <br>• Stripe API Key <br>• Stripe Live API Secret Key <br>• Stripe Test API Secret Key <br>• Stripe Live API Restricted Key <br>• Stripe Test API Restricted Key <br>• Stripe Webhook Signing Secret |
| Tableau                               | <br>• Tableau Personal access token                                                                                                                                                                  |
| Telegram                              | <br>• Telegram Bot Token                                                                                                                                                                             |
| Twilio                                | <br>• Twilio Account string identifier <br>• Twilio API Key                                                                                                                                          |
