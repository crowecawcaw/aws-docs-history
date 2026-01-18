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
- Ensure the GitHub App has the "Administration" organization [permissions](https://docs.github.com/en/enterprise-cloud@latest/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app "https://docs.github.com/en/enterprise-cloud@latest/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app") (read) permission
- Follow the instructions in [Managing private keys for GitHub Apps](https://docs.github.com/en/enterprise-cloud@latest/apps/creating-github-apps/authenticating-with-a-github-app/managing-private-keys-for-github-apps "https://docs.github.com/en/enterprise-cloud@latest/apps/creating-github-apps/authenticating-with-a-github-app/managing-private-keys-for-github-apps") and generate the private key
- Store this private key in a secret in the AWS Secrets Manager under the key `private_key` and the GitHub App name under the key `app_id`

## Configuring the CloudWatch Pipeline

When configuring the pipeline to read audit logs from GitHub Enterprise Cloud, choose GitHub Audit Logs as the data source. Select the Source Type as Enterprise or Organization based on the scope of your integration and fill in the required information like Enterprise or Organization name according to the selected scope. Once you create the pipeline, data will be available in the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports OCSF schema version v1.5.0 and the [GitHub actions](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/security-log-events "https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/security-log-events") that maps to Account Change (3001), API Activity (6003) and Entity Management (3004).

**Account Change** contains the following actions:

- org.enable_two_factor_requirement
- org.disable_two_factor_requirement
- two_factor_authentication.add_factor
- two_factor_authentication.enabled
- two_factor_authentication.disabled
- two_factor_authentication.remove_factor
- org.disable_saml
- org.enable_saml
- personal_access_token.access_restriction_disabled
- personal_access_token.access_restriction_enabled
- personal_access_token.expiration_limit_set
- personal_access_token.expiration_limit_unset

**API Activity** contains the following actions:

- repository_secret_scanning_custom_pa....create
- repository_secret_scanning_custom_pa....update
- repository_secret_scanning_custom_pa....delete
- repository_secret_scanning_custom_pa....publish
- repository_secret_scanning_custom_p....enabled
- repository_secret_scanning_custom_p....disabled
- repository_secret_scanning_non_provi....enabled
- repository_secret_scanning_non_provi....disabled
- repository_secret_scanning_generic_s....enabled
- repository_secret_scanning_generic_s....disabled
- business_secret_scanning_custom_pattern.create
- business_secret_scanning_custom_pattern.update
- business_secret_scanning_custom_pattern.delete
- business_secret_scanning_custom_pattern.publish
- business_secret_scanning_custom_patt....enabled
- business_secret_scanning_custom_patt....disabled
- business_secret_scanning_generic_secrets.enabled
- business_secret_scanning_generic_secrets.disabled
- business_secret_scanning_non_provide....enabled
- business_secret_scanning_non_provide....disabled
- org_secret_scanning_non_provider_patt....enabled
- org_secret_scanning_non_provider_patt....disabled
- org_secret_scanning_generic_secrets.enabled
- org_secret_scanning_generic_secrets.disabled
- org_secret_scanning_custom_pattern.create
- org_secret_scanning_custom_pattern.update
- org_secret_scanning_custom_pattern.delete
- org_secret_scanning_custom_pattern.publish

[Show moreShow less](# "#")
**Entity Management** contains the following actions:

- oauth_application.destroy
- oauth_application.generate_client_secret
- oauth_application.remove_client_secret
- oauth_application.revoke_all_tokens
- oauth_application.revoke_tokens
- oauth_application.transfer
- personal_access_token.auto_approve_grant_requests_enabled
- personal_access_token.auto_approve_grant_requests_disabled
- ip_allow_list.disable
- ip_allow_list.enable_for_installed_apps
- ip_allow_list.disable_for_installed_apps
- ip_allow_list_entry.create
- ip_allow_list_entry.update
- ip_allow_list_entry.destroy
- repository_secret_scanning.disable
- repository_secret_scanning_automatic....disabled
- repository_secret_scanning_push_prot....disable
- repository_secret_scanning_push_prot....enable
- oauth_application.create
- oauth_application.reset_secret
- auto_approve_personal_access_token_req....enabled
- auto_approve_personal_access_token_req....disabled
- ip_allow_list.enable
- ip_allow_list.disable_user_level_enforcement
- ip_allow_list.enable_user_level_enforcement
- repository_secret_scanning.enable
- repository_secret_scanning_automatic....enabled
- repository_secret_scanning_push_prot....enable
- repository_secret_scanning_push_prot....add
- repository_secret_scanning_push_prot....remove
- repository_secret_scanning_push_prot....disable
- secret_scanning.enable
- secret_scanning.disable
- secret_scanning_new_repos.enable
- org_secret_scanning_automatic_validi....enabled
- org_secret_scanning_automatic_validi....disabled
- org_secret_scanning_push_protection_b....add
- org_secret_scanning_push_protection_b....remove
- org_secret_scanning_push_protection_b....disable
- org_secret_scanning_push_protection_b....enable
- business_secret_scanning_automatic_va....enabled
- business_secret_scanning_automatic_va....disabled
- business_secret_scanning_push_protection.enable
- business_secret_scanning_push_protection.disable
- business_secret_scanning_push_protection.enabled_for_new_repos
- business_secret_scanning_push_protection.disabled_for_new_repos
- business_secret_scanning_push_prote....enable
- business_secret_scanning_push_prote....update
- business_secret_scanning_push_prote....disable

[Show moreShow less](# "#")
