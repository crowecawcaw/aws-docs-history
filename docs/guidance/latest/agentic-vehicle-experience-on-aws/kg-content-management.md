

# Managing KB content without code redeployment
<a name="kg-content-management"></a>

## Content-as-config principle
<a name="kg-content-as-config"></a>

The most impactful operational property of the AVX grounding architecture is that reference content is fully decoupled from agent code. All automotive reference material lives in an ADP-hosted S3 content store backed by the Bedrock Knowledge Base, and the agent retrieves it at request time via Bedrock Retrieve. Adding or updating a document requires no code change and no runtime redeployment:

1. Upload the new or revised document to the Knowledge Base S3 bucket under the appropriate source-category prefix.

1. Trigger a Bedrock Knowledge Base sync job (either manually or via an S3 event notification wired to a sync Lambda).

1. Verify the sync completes without errors and that the document is retrievable.

This separation of content lifecycle from agent lifecycle is the operational property that makes AVX manageable at scale. Recall bulletins are issued on regulatory timelines, TSBs are revised frequently, and tenant service policies change with contract cycles — none of these events requires an engineering deployment.

## Document ingestion workflow
<a name="kg-sync-workflow"></a>

The recommended workflow for adding or updating KB content is:

1.  **Prepare the document** — DTC guides, TSBs, and recall notices are typically sourced from vendor feeds (NHTSA, OEM technical portal) or generated from structured ADP records. Format as Markdown for text-heavy reference content; PDF parsing is supported for scanned or pre-formatted documents.

1.  **Attach a metadata sidecar** — alongside each document, upload a JSON sidecar file (same key with a `.metadata.json` suffix) declaring the `source_category`, applicable persona roles, and tenant scope. Without a sidecar, documents default to `shared` with no source-category filter, which causes them to surface in unintended persona contexts.

1.  **Upload to S3** — copy the document and its sidecar to the correct prefix within the Knowledge Base S3 bucket. The prefix hierarchy by source category enables targeted audits: `dtc-guides/`, `tsb-recall/`, `owner-manuals/`, `service-policy/`, `parts-catalog/`, `charging-narrative/`. Using consistent prefixes also simplifies IAM prefix-based access policies for tenant-specific content uploads.

1.  **Trigger KB sync** — invoke the Bedrock `StartIngestionJob` API (or use the AWS Console Knowledge Base data source sync button) against the data source. The sync is incremental: only new or modified objects are re-embedded. For large bulk loads (initial population or major corpus refresh), schedule the sync during off-peak hours to avoid embedding-model throughput limits.

1.  **Verify retrieval** — after the sync completes, run a smoke-test Retrieve call with a query and filter that should match the new document. Confirm that the document appears in the top-k results. The `scripts/smoke-test-kb-retrieve.py` utility in the AVX repository supports parameterized retrieval smoke tests against any `source_category` and query pair.

1.  **Document the update** — record the document name, source category, date, and ingestion job ID in the team’s KB content log. This log is the audit trail for content changes and enables root-cause analysis when a citation surfaces unexpected content.

## Index refresh latency
<a name="kg-indexing-note"></a>

Bedrock Knowledge Base ingestion jobs are asynchronous. After the `StartIngestionJob` API returns `COMPLETE`, allow a short delay before the new content appears in Retrieve results. Run post-ingestion verification queries after the job reaches `COMPLETE`, and retry a query that misses new content once before treating it as a failure.

## Access control for content updates
<a name="kg-access-control"></a>

Content operators (teams responsible for keeping DTC guides, TSBs, and recalls current) should have S3 `PutObject` permission on the Knowledge Base bucket prefix corresponding to their content scope, but should not have IAM permissions to modify the vector index, the Bedrock Knowledge Base configuration, or the CDK stacks. The recommended pattern:
+ A content-operator IAM role with `s3:PutObject` and `s3:GetObject` on the specific S3 prefixes, plus `bedrock:StartIngestionJob` on the specific Knowledge Base ARN.
+ A separate infrastructure-operator IAM role for CDK stack changes, vector index management, and Knowledge Base configuration.
+ Tenants that manage their own overlay content are granted the content-operator permissions scoped to their tenant prefix (`s3:PutObject` on `tenant-content/<tenant-id>/`).

This separation ensures that content updates — which should be high-frequency and low-risk — never require the blast-radius permissions of an infrastructure deployment.