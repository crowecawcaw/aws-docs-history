On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# Secrets detection

CodeGuru Security integrates with AWS Secrets Manager to use a secrets detector that finds unprotected secrets
in your code and text files. Secrets detection is automatically enabled in scans, so you don't
need to turn it on.

The secrets detector searches for hardcoded passwords, database connection strings, user
names, and more. When an unprotected secret is found during a code scan, CodeGuru Security generates a
finding with a suggested remediation that tells you about the unprotected secret. To protect
secrets, you can store them in AWS Secrets Manager. For more information, see
[Move
hardcoded secrets to AWS Secrets Manager](../../../secretsmanager/latest/userguide/hardcoded.md "../../../secretsmanager/latest/userguide/hardcoded.md").

## Supported character types for secrets detection

CodeGuru Security can detect secrets in English. Valid characters include alphanumeric characters
and ASCII special characters.

## Supported file types for secrets detection

The secrets detector finds unprotected secrets the following file types with a maximum file
size of 100 KB.

- Class files (\*.class)
- Config files (\*.config, \*.cfg, \*.conf, \*.cnf, \*.cf)
- C# files (\*.cs)
- Environment files (\*.env)
- Go files (\*.go)
- HTML files (\*.html)
- Initialization files (\*.ini)
- Java files (\*.java)
- JavaScript files (\*.js, \*.mjs, \*.cjs)
- JSON files (\*.json)
- Jakarta Server Pages files (\*.jsp)
- Jupyter Notebook files (\*.ipynb)
- Key files (\*.key)
- Markdown files (\*.md)
- Privacy Enhanced Mail files (\*.pem)
- Properties files (\*.properties)
- Property List files (\*.plist)
- Python files (\*.py)
- reStructuredText files (\*.rst)
- Ruby files (\*.rb)
- Terraform files (\*.tf, \*.hcl)
- Text files (\*.txt, \*.text)
- TypeScript files (\*.ts)
- TOML files (\*.toml)
- XML files (\*.xml)
- YAML files (\*.yml, \*.yaml)

## Types of secrets detected by CodeGuru Security

CodeGuru Security detects unprotected usernames, passwords, RSA keys, and the
following secrets.

| Secrets detected by CodeGuru Security | Provider                                                                                                                                                                                    | Secrets detected |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| Amazon Web Services (AWS)             | • Amazon AWS Secret Access Key                                                                                                                                                              |
| Atlassian                             | • Atlassian API Token<br>• Atlassian JSON Web Token<br>• Bitbucket Server Personal Access Token                                                                                             |
| Databricks                            | • Databricks Access Token                                                                                                                                                                   |
| Datadog                               | • Datadog API Key<br>• Datadog App Key                                                                                                                                                      |
| GitHub                                | • GitHub Personal Access Token<br>• GitHub OAuth Access Token<br>• GitHub Refresh Token<br>• GitHub App Installation Access Token<br>• GitHub SSH Private Key                               |
| Intercom                              | • Intercom Access Token                                                                                                                                                                     |
| Mailchimp                             | • Mailchimp API Key                                                                                                                                                                         |
| Mailgun                               | • Mailgun API Key                                                                                                                                                                           |
| Salesforce                            | • Private Key                                                                                                                                                                               |
| SendGrid                              | • SendGrid API Key                                                                                                                                                                          |
| Shopify                               | • Shopify App Shared Secret<br>• Shopify Access Token<br>• Shopify Custom App Access Token<br>• Shopify Private App Password                                                                |
| Slack                                 | • Client ID<br>• Client Secret                                                                                                                                                              |
| Stripe                                | • Stripe API Key<br>• Stripe Live API Secret Key<br>• Stripe Test API Secret Key<br>• Stripe Live API Restricted Key<br>• Stripe Test API Restricted Key<br>• Stripe Webhook Signing Secret |
| Tableau                               | • Tableau Personal access token                                                                                                                                                             |
| Telegram                              | • Telegram Bot Token                                                                                                                                                                        |
| Twilio                                | • Twilio Account string identifier<br>• Twilio API Key                                                                                                                                      |
