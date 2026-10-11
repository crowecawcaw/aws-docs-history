

# Source-category filtering
<a name="kg-source-category"></a>

## Why filtering matters
<a name="kg-why-filtering"></a>

The ADP Knowledge Base can hold content for every tenant, every persona, and every document type in a single vector index. Without filtering, a Bedrock Retrieve call against the full index could surface a fleet operator’s proprietary service-level agreement in response to a consumer-facing query, or could include recall bulletins irrelevant to the vehicle type in question. Two hazards result:
+  **Confidentiality violation** — tenant-confidential content leaks across persona boundaries.
+  **Relevance degradation** — the supervisor receives off-target passages in its grounding context, and the quality of the synthesized answer drops.

Metadata filtering eliminates both hazards without requiring separate indexes or separate inference calls. Each document in the Knowledge Base is ingested with a metadata sidecar that tags it with one or more `source_category` values, an optional `persona_id` allowlist, and optionally a `tenant_id`. The Bedrock Retrieve call from the `knowledge()` tool includes a filter expression that restricts the retrieved passages to those whose metadata matches the current persona and tenant.

## Source categories in use
<a name="kg-source-categories"></a>

The current KB content is organized into the following source categories:


| source\_category | Content type | Typical consumer personas | 
| --- | --- | --- | 
|  `dtc_guide`  | Diagnostic Trouble Code (DTC) reference guides — fault definition, probable causes, severity, recommended action, safety classification, and repair procedures for common OBD codes. | Technician, Service Advisor | 
|  `tsb_recall`  | Technical Service Bulletins (TSBs) and NHTSA recall notices — defect description, affected vehicle population, remedy procedure, parts required, compliance timeline. | Service Advisor, Technician, Fleet Driver (recall awareness) | 
|  `owner_manual`  | Owner and operator manual content — instrument panel indicators, fluid specifications, maintenance schedules, towing and payload ratings, EV charging guidance. | Vehicle Owner, Consumer, Fleet Driver | 
|  `service_policy`  | Tenant service policy documents — authorization levels, warranty claim procedures, parts approval thresholds, escalation rules, SLA definitions. | Service Advisor (tenant-scoped) | 
|  `parts_catalog`  | ADP Parts Catalog narratives — OEM part numbers, list prices, fleet pricing, stock availability, interchange references, installation notes. | Technician, Service Advisor | 
|  `charging_narrative`  | EV charging session summaries and charging policy guidance — rate optimization, charger compatibility, range estimation, charging infrastructure SOPs. | Consumer, Fleet Driver (EV), Vehicle Owner | 

A metadata sidecar file accompanying each document declares the applicable categories:

```
{
  "source_category": ["dtc_guide"],
  "applicable_personas": ["technician", "service_advisor"],
  "document_type": "dtc_reference",
  "applicable_makes": ["generic"]
}
```

The `knowledge()` tool constructs the Bedrock Retrieve filter based on the current persona’s allowed source categories:

```
filter_expression = {
    "orAll": [
        {"equals": {"key": "source_category", "value": cat}}
        for cat in persona_allowed_categories
    ]
}
```

This means a Fleet Driver session never receives passages from `service_policy` documents (which may contain tenant-confidential authorization rules), and a Technician session retrieves `dtc_guide` and `parts_catalog` content without surfacing `charging_narrative` passages that are irrelevant to a workshop context.

## Per-turn and per-document filtering
<a name="kg-per-turn-filter"></a>

Filtering applies at two levels:
+  **Per-turn persona filter** — as described above, every Retrieve call applies the current persona’s allowed-category filter. This is the primary tenant and persona isolation mechanism.
+  **Per-document tenant filter** — content that is specific to a single tenant (for example, a fleet operator’s proprietary service SLA document, or an OEM’s brand-specific recall coverage extension) is tagged at ingestion with a `tenant_id` metadata attribute. The Retrieve filter combines the category filter with a tenant equality check: `tenant_id == current_tenant OR tenant_id == "shared"`. Cross-tenant content tagged `shared` is accessible to all tenants; tenant-specific documents are accessible only to that tenant’s sessions.