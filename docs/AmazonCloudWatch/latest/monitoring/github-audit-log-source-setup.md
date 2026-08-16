# Source configuration for GitHub Audit Log

###### Note

Important: GitHub Enterprise accounts are required to use this connector. GitHub Personal or Organization accounts are not supported.

## Integrating with GitHub

Amazon Telemetry Pipelines enables you to collect audit logs from GitHub Enterprise Cloud. GitHub Enterprise is an enterprise-grade software development platform designed for the complex workflows of modern development. GitHub Enterprise Cloud is the cloud-based solution of GitHub Enterprise, hosted on GitHub's servers.

## Authenticating with GitHub

To read the audit logs, pipeline needs to authenticate with your GitHub account. For Enterprise [scope](https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin/audit-log?apiVersion=2022-11-28#get-the-audit-log-for-an-enterprise "https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin/audit-log?apiVersion=2022-11-28#get-the-audit-log-for-an-enterprise") , you can use Personal Access Token and for Organization [scope](https://docs.github.com/en/enterprise-cloud@latest/rest/orgs/orgs?apiVersion=2022-11-28#get-the-audit-log-for-an-organization "https://docs.github.com/en/enterprise-cloud@latest/rest/orgs/orgs?apiVersion=2022-11-28#get-the-audit-log-for-an-organization") , you can either use Personal Access Token or GitHub App.

**Generate the token to authenticate as Personal Access Token:**

- Sign in to [GitHub](https://github.com/dashboard "https://github.com/dashboard") using credentials for the GitHub account
- The authenticated user must be an enterprise admin to use this endpoint
- Open the GitHub Personal access tokens (classic) page, locate the Generate new token (classic) and then follow the GitHub procedure to generate a token with `read:audit_log` scope and No expiration
- Store this new token in a secret in the AWS Secrets Manager under the key `personal_access_token`

**Generate the private key to authenticate as GitHub App:**

- Sign in to [GitHub](https://github.com/dashboard "https://github.com/dashboard") using credentials for the GitHub account
- Make sure the GitHub App has the "Administration" organization [permissions](https://docs.github.com/en/enterprise-cloud@latest/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app "https://docs.github.com/en/enterprise-cloud@latest/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app") (read) permission
- Follow the instructions in [Managing private keys for GitHub Apps](https://docs.github.com/en/enterprise-cloud@latest/apps/creating-github-apps/authenticating-with-a-github-app/managing-private-keys-for-github-apps "https://docs.github.com/en/enterprise-cloud@latest/apps/creating-github-apps/authenticating-with-a-github-app/managing-private-keys-for-github-apps") and generate the private key
- Store this private key in a secret in the AWS Secrets Manager under the key `private_key` and the GitHub App name under the key `app_id`

## Configuring the CloudWatch Pipeline

When configuring the pipeline to read audit logs from GitHub Enterprise Cloud, choose GitHub Audit Logs as the data source. Select the Source Type as Enterprise or Organization based on the scope of your integration and fill in the required information like Enterprise or Organization name according to the selected scope. After you create the pipeline, data will be available in the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports OCSF schema version v1.5.0 and the [GitHub actions](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/security-log-events "https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/security-log-events") that maps to Account Change (3001), API Activity (6003) and Entity Management (3004).

**Account Change** contains the following actions:

- org.enable\_two\_factor\_requirement
- org.disable\_two\_factor\_requirement
- two\_factor\_authentication.add\_factor
- two\_factor\_authentication.enabled
- two\_factor\_authentication.disabled
- two\_factor\_authentication.remove\_factor
- org.disable\_saml
- org.enable\_saml
- personal\_access\_token.access\_restriction\_disabled
- personal\_access\_token.access\_restriction\_enabled
- personal\_access\_token.expiration\_limit\_set
- personal\_access\_token.expiration\_limit\_unset

**API Activity** contains the following actions:

- repository\_secret\_scanning\_custom\_pa....create
- repository\_secret\_scanning\_custom\_pa....update
- repository\_secret\_scanning\_custom\_pa....delete
- repository\_secret\_scanning\_custom\_pa....publish
- repository\_secret\_scanning\_custom\_p....enabled
- repository\_secret\_scanning\_custom\_p....disabled
- repository\_secret\_scanning\_non\_provi....enabled
- repository\_secret\_scanning\_non\_provi....disabled
- repository\_secret\_scanning\_generic\_s....enabled
- repository\_secret\_scanning\_generic\_s....disabled
- business\_secret\_scanning\_custom\_pattern.create
- business\_secret\_scanning\_custom\_pattern.update
- business\_secret\_scanning\_custom\_pattern.delete
- business\_secret\_scanning\_custom\_pattern.publish
- business\_secret\_scanning\_custom\_patt....enabled
- business\_secret\_scanning\_custom\_patt....disabled
- business\_secret\_scanning\_generic\_secrets.enabled
- business\_secret\_scanning\_generic\_secrets.disabled
- business\_secret\_scanning\_non\_provide....enabled
- business\_secret\_scanning\_non\_provide....disabled
- org\_secret\_scanning\_non\_provider\_patt....enabled
- org\_secret\_scanning\_non\_provider\_patt....disabled
- org\_secret\_scanning\_generic\_secrets.enabled
- org\_secret\_scanning\_generic\_secrets.disabled
- org\_secret\_scanning\_custom\_pattern.create
- org\_secret\_scanning\_custom\_pattern.update
- org\_secret\_scanning\_custom\_pattern.delete
- org\_secret\_scanning\_custom\_pattern.publish

[Show moreShow less](# "#")
**Entity Management** contains the following actions:

- oauth\_application.destroy
- oauth\_application.generate\_client\_secret
- oauth\_application.remove\_client\_secret
- oauth\_application.revoke\_all\_tokens
- oauth\_application.revoke\_tokens
- oauth\_application.transfer
- personal\_access\_token.auto\_approve\_grant\_requests\_enabled
- personal\_access\_token.auto\_approve\_grant\_requests\_disabled
- ip\_allow\_list.disable
- ip\_allow\_list.enable\_for\_installed\_apps
- ip\_allow\_list.disable\_for\_installed\_apps
- ip\_allow\_list\_entry.create
- ip\_allow\_list\_entry.update
- ip\_allow\_list\_entry.destroy
- repository\_secret\_scanning.disable
- repository\_secret\_scanning\_automatic....disabled
- repository\_secret\_scanning\_push\_prot....disable
- repository\_secret\_scanning\_push\_prot....enable
- oauth\_application.create
- oauth\_application.reset\_secret
- auto\_approve\_personal\_access\_token\_req....enabled
- auto\_approve\_personal\_access\_token\_req....disabled
- ip\_allow\_list.enable
- ip\_allow\_list.disable\_user\_level\_enforcement
- ip\_allow\_list.enable\_user\_level\_enforcement
- repository\_secret\_scanning.enable
- repository\_secret\_scanning\_automatic....enabled
- repository\_secret\_scanning\_push\_prot....enable
- repository\_secret\_scanning\_push\_prot....add
- repository\_secret\_scanning\_push\_prot....remove
- repository\_secret\_scanning\_push\_prot....disable
- secret\_scanning.enable
- secret\_scanning.disable
- secret\_scanning\_new\_repos.enable
- org\_secret\_scanning\_automatic\_validi....enabled
- org\_secret\_scanning\_automatic\_validi....disabled
- org\_secret\_scanning\_push\_protection\_b....add
- org\_secret\_scanning\_push\_protection\_b....remove
- org\_secret\_scanning\_push\_protection\_b....disable
- org\_secret\_scanning\_push\_protection\_b....enable
- business\_secret\_scanning\_automatic\_va....enabled
- business\_secret\_scanning\_automatic\_va....disabled
- business\_secret\_scanning\_push\_protection.enable
- business\_secret\_scanning\_push\_protection.disable
- business\_secret\_scanning\_push\_protection.enabled\_for\_new\_repos
- business\_secret\_scanning\_push\_protection.disabled\_for\_new\_repos
- business\_secret\_scanning\_push\_prote....enable
- business\_secret\_scanning\_push\_prote....update
- business\_secret\_scanning\_push\_prote....disable

[Show moreShow less](# "#")
