# AOSOPS03-BP04 Enable audit logs for OpenSearch Service domains

using fine-grained access control

Turn on audit logging with access control to gain visibility into
domain operations, support issue resolution, and enhance security
and compliance.

**Level of risk exposed if this best practice
is not established:** Medium

**Desired outcome**: Achieve clear
visibility into your domain's operations, enabling quicker issue
resolution and better security and compliance.

**Benefits of establishing this best
practice:**

- Improved security and compliance
- Enhanced ability to monitor and audit user activity

## Implementation guidance

Audit logs help monitor user activity on your OpenSearch clusters,
capturing details such as authentication successes and failures,
OpenSearch requests, index modifications, and search queries.

### Implementation steps

Enabling audit logs for your domain involves a multi-step
process that includes:

- Enabling audit logs in your OpenSearch Service domain.
- Creating a CloudWatch Log group or choosing an existing one.
- Creating an access policy.
- Activating the audit logs in your OpenSearch Dashboards.

For a detailed step-by-step guide on enabling audit logs for
your OpenSearch Service Domain, see
[How
do I activate audit logs in OpenSearch Service](https://repost.aws/knowledge-center/opensearch-audit-logs "https://repost.aws/knowledge-center/opensearch-audit-logs") and
[Monitoring
audit logs in Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/audit-logs.md "../../../opensearch-service/latest/developerguide/audit-logs.md").

## Resources

- [Monitoring
  audit logs in Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/audit-logs.md "../../../opensearch-service/latest/developerguide/audit-logs.md")
