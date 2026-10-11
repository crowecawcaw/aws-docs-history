

# Cross-account grant model
<a name="sec-cross-account-grants"></a>

When AVX and ADP are deployed in separate AWS accounts — the production topology — data access from AVX to ADP crosses an account boundary. The agent layer holds no long-lived credentials into the ADP account; access is governed by two grant mechanisms and is fully auditable via CloudTrail data events.

See [Building on CMS and ADP](building-on-cms-and-adp.md) for the infrastructure wiring (CDK context variables, Lake Formation share configuration, and KB resource policy provisioning). This section covers the security posture of that model.

## Lake Formation cross-account data access
<a name="sec-lake-formation-grants"></a>

ADP’s tabular data products — vehicle identity, service records, OTA campaigns, and others — reside in the ADP account’s Glue catalog, backed by an S3-based Iceberg data lake with server-side encryption (SSE-KMS). AVX accesses this data through cross-account Lake Formation grants:

1. The ADP CDK stack creates a Lake Formation resource link and grants AVX’s AgentCore execution role `lakeformation:GetDataAccess` on the targeted databases. The grant is expressed as a wildcard over the databases in scope, scoped explicitly by database name — not by account-wide wildcard.

1. AVX’s Athena workgroup (`cvx-{stage}-analytics`) uses Lake Formation-issued temporary session credentials to read S3 objects in the ADP data lake. No permanent cross-account IAM role with S3 permissions is required; credentials are issued per-query with a bounded TTL.

1. Athena query results are written to an AVX-owned S3 bucket (`cvx-{stage}-athena-results- {region}`), not to the ADP account’s storage. The ADP account’s data lake objects are never copied or retained by AVX beyond the in-flight query.

To add a new ADP database to the cross-account share, the ADP CDK stack is updated with the database name and a new Lake Formation grant is created. No change is required on the AVX side beyond updating the Athena query to reference the new database.

## Bedrock Knowledge Base resource policy
<a name="sec-bedrock-kb-resource-policy"></a>

The ADP-hosted vehicle Knowledge Base is accessed cross-account via a Bedrock KB resource policy that explicitly enumerates the AVX role ARN(s) permitted to call `bedrock-agent-runtime:Retrieve`:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCVXRetrieve",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::<cvx-account-id>:role/<cvx-agentcore-exec-role>"
      },
      "Action": "bedrock:Retrieve",
      "Resource": "arn:aws:bedrock:<region>:<adp-account-id>:knowledge-base/<kb-id>"
    }
  ]
}
```

Replace `<cvx-account-id>`, `<adp-account-id>`, `<region>`, `<kb-id>`, and `<cvx-agentcore-exec-role>` with your deployment’s values. The resource policy is the only trust mechanism: the AVX role does not need an inline policy granting `bedrock:Retrieve` on the ADP resource — the resource policy alone is sufficient for cross-account Retrieve access.

In the single-account, two-region staging topology (AVX us-west-2, ADP us-east-1), the same resource-policy pattern applies, scoped by IAM role rather than account ID. The code path for both topologies is identical; only the ARN account fields differ.

## CloudTrail data-event audit
<a name="sec-cloudtrail-data-events"></a>

All data-plane access from AVX to ADP is logged by AWS CloudTrail data events in both accounts:
+  **ADP account:** S3 data events on the data lake bucket record every object GET issued by Lake Formation-credentialed Athena queries, including the IAM principal ARN, source IP address, and query timestamp.
+  **ADP account:** Bedrock data events record every `Retrieve` call against the KB, including the calling principal, KB ID, and request timestamp.
+  **AVX account:** Athena query-execution events record the query text, workgroup, and result location for every cross-account data pull.

Together, these three event streams provide a complete audit trail: who queried what data, when, and on behalf of which AVX session. CloudTrail data events should be delivered to a dedicated audit S3 bucket with Object Lock enabled and a minimum 90-day retention policy.