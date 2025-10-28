# Cross-account permission cascading

When you share data across AWS accounts using LF-Tag policies, AWS Lake Formation enables permission cascading through two primary delegation mechanisms.
These mechanisms allow consumer account administrators to grant access to users and roles without requiring the producer account to manage individual permissions for each consumer.

- **Delegation with identical LF-Tag policies** –
  When the LF-Tag policy is exactly the same as the LF-Tag policy used by the producer account
  to share resources with the consumer account, principals can cascade permissions using the
  grantable permissions (`PermissionsWithGrantOption`). This allows the principal
  in the consumer account to grant the same permissions to other principals within their
  account.
- **Alternative delegation using `DESCRIBE`
  permissions** – Principals in the consumer account can cascade permissions
  without requiring grantable permissions (`PermissionsWithGrantOption`) if they
  have DESCRIBE permissions on tag-value pairs. This approach only works when producer and
  consumer accounts have different permissions policies.
  Understanding these delegation mechanisms is important for proper cross-account data
  sharing and security management. They determine how permissions flow from data owners to
  consumers.

###### Topics

- [Permission cascading rules](permission-cascading-rules.md "permission-cascading-rules.md")
- [Prerequisites](prerequisites.md "prerequisites.md")
- [Cascading cross-account permissions](cascade-cross-account-permission-procedures.md "cascade-cross-account-permission-procedures.md")
- [Rule priority behavior](permission-cascading-rule-priority-behavior.md "permission-cascading-rule-priority-behavior.md")
- [Best practices](permission-cascading-best-practices.md "permission-cascading-best-practices.md")
- [Troubleshooting](permission-cascading-troubleshooting.md "permission-cascading-troubleshooting.md")
