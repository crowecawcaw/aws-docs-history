# AOSSEC02-BP01 Set up audit logging for OpenSearch Service domains that

use fine-grained access control

Turn on audit logging for OpenSearch Service domains using fine-grained
access control, enhancing security monitoring and compliance.

**Level of risk exposed if this best practice
is not established:** High

**Desired outcome:** Audit logs are
enabled on OpenSearch Service domains with fine-grained access control
enabled.

**Benefits of establishing this best
practice:**

- **Improved security monitoring:**
  Enabling audit logs on OpenSearch Service domains with fine-grained
  access control enabled allows for improved security monitoring
  and tracking of user activity.
- **Enhanced compliance:** By
  customizing the audit log settings to meet specific needs,
  organizations can enhance compliance with regulatory
  requirements by maintaining a detailed record of user actions
  and activities within their OpenSearch clusters.

## Implementation guidance

If your OpenSearch Service domain uses fine-grained access
control, you can enable audit logs for your data. Audit logs are
highly customizable and let you track user activity on your
OpenSearch clusters, including authentication success and
failures, requests to OpenSearch, index changes, and incoming
search queries. The default configuration tracks a popular set of
user actions, but we recommend tailoring the settings to your
exact needs.

For details on how to enable audit logs for your OpenSearch Service domain, see [AOSOPS03-BP04](aosops03-bp04.md "aosops03-bp04.md").

## Resources

- [Monitoring
  audit logs in Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/audit-logs.md "../../../opensearch-service/latest/developerguide/audit-logs.md")
