

# Security best practices for AWS Network Security Manager
<a name="security-best-practices"></a>

The following best practices help you maintain a secure AWS Network Security Manager configuration.

## Preventative controls
<a name="security-best-practices-preventative"></a>
+ **Use IAM least privilege** -- Grant only the permissions required for each user or role to perform their AWS Network Security Manager tasks. Use IAM condition keys to restrict access to specific resources when possible.
+ **Use service-linked roles** -- AWS Network Security Manager uses service-linked roles to perform actions on your behalf. These roles have pre-defined permissions scoped to the minimum required access.
+ **Configure scopes carefully** -- Define scope configurations that target only the accounts and resource types that require protection. Overly broad scopes can lead to unintended enforcement.

## Detective controls
<a name="security-best-practices-detective"></a>
+ **Enable AWS CloudTrail logging** -- CloudTrail records all AWS Network Security Manager API calls. Review these logs to audit who made changes to your security configurations and when.
+ **Monitor synchronization status** -- Regularly check the synchronization status of your deployments to identify resources that are out of sync with your intended security posture.