

# Per-tenant knowledge bases and shared content
<a name="kg-per-tenant-kb"></a>

## Shared cross-tenant content
<a name="kg-shared-layer"></a>

Some automotive content is genuinely shared across all tenants and personas. These documents are ingested once into the shared layer of the Knowledge Base and tagged `tenant_id=shared`:
+  **NHTSA recall bulletins** — federal recall notices have no tenant affiliation. Every tenant benefits from recall awareness, and the remedy information is publicly published.
+  **VSS (Vehicle Signal Specification) catalog** — the VSS signal tree and unit definitions are a vendor-neutral standard used to interpret telemetry field names.
+  **Generic DTC guides** — many OBD-II codes are defined by SAE standards and apply regardless of make or model. Generic DTC guides are shared; OEM-specific trouble codes with proprietary fault trees are ingested under the relevant tenant.
+  **Generic owner manual sections** — content about instrument panel warning lights, universal safety guidance, and standard maintenance intervals for common drivetrains does not vary by tenant and can be shared.

## Tenant-specific content isolation
<a name="kg-tenant-layer"></a>

Content that belongs to a single tenant is ingested with `tenant_id` set to that tenant’s identifier and is never returned to another tenant’s Retrieve calls. Examples of tenant-specific content include:
+  **Proprietary service policies** — a fleet operator’s internal authorization thresholds, tiered SLA terms, or branded warranty extensions that are not disclosed to other operators.
+  **Brand-specific recall extensions** — OEM-specific recall remedy procedures that go beyond the NHTSA minimum.
+  **Tenant-branded owner content** — custom driver guides, operator handbooks, or vehicle-configuration-specific manuals produced by the tenant.
+  **Technician-level FSBs** — field service bulletins produced by the tenant’s technical operations team, not published through NHTSA’s public channel.

The tenant isolation boundary is enforced at two independent layers: the Bedrock Retrieve metadata filter (so that the query result set never includes cross-tenant documents) and the IAM resource policy on the Bedrock Knowledge Base (so that only authorized AVX execution roles can call Retrieve at all). The IAM layer is the hard boundary; the metadata filter is the relevance layer. Neither alone is sufficient.

## Overlay pattern for tenant content
<a name="kg-overlay-pattern"></a>

Tenants that have modest proprietary content volumes do not require a separate Knowledge Base. The recommended approach is a **shared-plus-overlay** model:

1. A shared Knowledge Base (backed by a single vector index) holds all cross-tenant content tagged `tenant_id=shared`.

1. Tenant-specific documents are ingested into the same index tagged with the tenant’s identifier.

1. Retrieve calls apply the combined filter: `(source_category IN allowed_categories) AND (tenant_id == current_tenant OR tenant_id == "shared")`.

1. Tenants with very high proprietary content volumes, or tenants whose content must be isolated at the infrastructure level (for contractual or regulatory reasons), can be served from a dedicated Knowledge Base referenced in the tenant config.

The tenant config record (managed in DynamoDB) carries the `knowledgeBaseId` for the tenant’s overlay knowledge base, if any. When the config specifies an overlay KB ID, the `knowledge()` tool issues Retrieve calls to both the shared KB and the overlay KB in parallel, merging the result sets with overlay hits preferred when they are higher-ranked. The shared KB ARN is set at CDK context time as `<adp-knowledge-base-id>`; the overlay KB ARN is tenant-configurable without a code or infrastructure change.