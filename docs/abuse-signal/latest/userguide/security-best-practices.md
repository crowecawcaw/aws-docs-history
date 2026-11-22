

# Security best practices for AWS Abuse Signal API

Use the following practices to protect the credentials and systems that you use to submit reports.

## Preventative controls
<a name="security-best-practices-preventative"></a>
+  **Apply least-privilege IAM** – Grant only the abuse: actions each identity needs. Prefer IAM roles with short-lived credentials over long-lived access keys. For more information, see [Identity and access management for AWS Abuse Signal API](security-iam.md).
+  **Require MFA** – Turn on multi-factor authentication (MFA) for identities that can submit or track reports.
+  **Keep your client current** – Keep your SDK and signing client up to date. Don’t disable certificate verification or pin to deprecated TLS versions.
+  **Include only the information that AWS needs to process your report** – Don’t include passwords, access keys or other credentials in any field. Never include images or video of child sexual abuse material in a report.
+  **Use AWS PrivateLink** – Reach the API privately from your VPC. For more information, see [Regions and endpoints](regions-endpoints.md).

## Detective controls
<a name="security-best-practices-detective"></a>
+  **Log API activity with AWS CloudTrail** – CloudTrail records all abuse: API calls, including who called the API, from where, and when.
+  **Monitor your submission pipeline** – Watch for unexpected increases in validation failure responses (HTTP 400 or 422) or throttling responses (HTTP 429). These can indicate misconfiguration or misuse of your credentials.
+  **Review IAM access periodically** – Use IAM last-accessed data and credential reports to remove unused abuse: permissions and stale credentials.