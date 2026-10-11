

# Tenant isolation
<a name="sec-tenant-isolation"></a>

Authentication confirms who the caller is; tenant isolation ensures that each caller can access only the data belonging to their organization. AVX enforces isolation at three complementary layers.

## IAM condition keys
<a name="sec-iam-conditions"></a>

Every Lambda handler that reads or writes data carries a tenant-scoped IAM execution role. DynamoDB, Bedrock KB Retrieve, and AgentCore Memory calls are bounded by IAM condition keys that express the permitted tenant scope:

```
{
  "Condition": {
    "StringEquals": {
      "dynamodb:LeadingKeys": "${aws:PrincipalTag/tenantId}/<key>"
    }
  }
}
```

The `aws:PrincipalTag/tenantId` tag is set when the Lambda execution role is assumed; it is supplied from the validated Cognito claim and cannot be overridden by the caller. This means that even if a request somehow carries a manipulated tenant context in the request body, the IAM condition on the underlying API call will reject any attempt to read outside the principal’s permitted partition.

## DynamoDB partition-key prefixing
<a name="sec-dynamodb-partition-keys"></a>

All AVX DynamoDB tables use a composite partition key of the form `<tenantId>#<entityId>`. For example, a vehicle-state record for vehicle `V-001` in tenant `t-fleet-01` has the partition key `t-fleet-01#V-001`. A caller authenticated as tenant `t-rental-07` will never produce a GetItem or Query that resolves to a `t-fleet-01#*` key because the partition key is constructed server-side from the validated `custom:tenantId` claim, not from client-supplied input.

The prefix convention applies uniformly to: \* Vehicle state and live telemetry records \* Session and conversation state \* Booking and STAR ticket records \* Tenant-specific configuration overrides

## Per-tenant knowledge bases
<a name="sec-per-tenant-kbs"></a>

Knowledge base grounding is tenant-scoped in two ways:

1.  **Per-tenant Bedrock KB.** Each tenant’s corpus — service policies, brand-specific warranty terms, fleet SLA definitions, operator-supplied documentation — resides in a dedicated Bedrock Knowledge Base. The KB ID for a tenant is stored in the tenant config record and loaded at session start; no cross-tenant KB lookup is possible because the KB ARN is resolved from the tenant config, not from user input.

1.  **Shared cross-tenant KB with source-category filtering.** Cross-brand reference content (NHTSA recall bulletins, OBD-II DTC guides, NHTSA Vehicle Safety Standards) lives in a shared KB. The `source_category` metadata filter is set server-side on every Retrieve call so that a retrieval issued in a fleet-operator session cannot surface rental-policy content or vice versa.

For the cross-account grant model that backs KB access in multi-account deployments, see [Building on CMS and ADP](building-on-cms-and-adp.md).