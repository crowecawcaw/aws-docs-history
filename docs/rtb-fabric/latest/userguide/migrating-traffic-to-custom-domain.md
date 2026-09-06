

# Migrating traffic to inbound external links with custom domains
<a name="migrating-traffic-to-custom-domain"></a>

This section describes how to migrate existing bid-request traffic from your current endpoint infrastructure to RTB Fabric inbound external links with custom domains. The migration uses DNS-based traffic routing, requires zero application changes on either the demand-side or supply-side, and supports incremental cutover with instant rollback.

## Migration overview
<a name="migration-overview"></a>

Inbound external links with custom domains migration is DNS-based. You update the CNAME record for your public bid endpoint so that it resolves to your regional RTB Fabric Gateway endpoint instead of your existing origin. Because RTB Fabric preserves the request path, query string, and all HTTP headers exactly as received, neither your bidder application nor your upstream partners require any changes.

The migration sequence is:

1. Provision your inbound external links with custom domains configuration (TLS certificate if using HTTPS, routing rules, link association). See Getting started with inbound external links with custom domains.

1. Lower the DNS TTL on your existing CNAME record.

1. Create weighted DNS records to split traffic between your existing endpoint and the RTB Fabric Gateway.

1. Incrementally shift traffic to RTB Fabric by adjusting record weights.

1. After full cutover, remove the legacy weighted record and restore your preferred TTL.

**Important**  
RTB Fabric inbound external links with custom domains operates over HTTP/1.1 upstream only. If your existing endpoint serves HTTP/2 traffic, confirm that your supply-side partners can negotiate HTTP/1.1 before migrating. See Quotas and constraints for the full list of unsupported features.

## Pre-migration checklist
<a name="pre-migration-checklist"></a>

Complete the following steps before changing any DNS records:

1. **(HTTPS only) Verify certificate resolution.** If you use HTTPS, confirm that the TLS certificate associated with your gateway resolves correctly for every hostname you intend to migrate. Use `openssl s_client` against the gateway endpoint to verify SNI-based selection:

   ```
   openssl s_client -connect <gateway-endpoint>:443 -servername east-bid.example.com </dev/null 2>&1 | openssl x509 -noout -subject -ext subjectAltName
   ```

1. **Verify routing rules.** Send test requests directly to the gateway endpoint with the appropriate `Host` header and confirm that each request routes to the correct link ID. Use `https://` and port `443` for HTTPS, or `http://` and port `80` for HTTP:

   ```
   curl -v --resolve east-bid.example.com:443:<gateway-ip> https://east-bid.example.com/bid?supplier_id=7
   ```

1. **Lower DNS TTL.** Reduce the TTL on your existing CNAME record to a low value (60-120 seconds) at least 24 hours before the migration window. This ensures that when you change the record, DNS caches expire quickly, giving you faster rollback capability.

   ```
   east-bid.example.com. 60 IN CNAME legacy-origin.example.com.
   ```

1. **Document the current CNAME target.** Record the existing CNAME target so you can restore it immediately if rollback is needed.

**Note**  
The 24-hour lead time for TTL lowering accounts for the previous TTL's expiration across global DNS caches. If your existing TTL is already 300 seconds or lower, a shorter lead time is acceptable.

## Gradual cutover with Route 53 weighted routing
<a name="gradual-cutover-route53"></a>

Use Amazon Route 53 weighted routing records to incrementally shift traffic from your legacy endpoint to the RTB Fabric Gateway. Weighted routing distributes DNS responses proportionally across records based on their assigned weights.

### Step 1: Create the initial weighted record set
<a name="step1-create-weighted-records"></a>

Create two weighted CNAME records for your bid endpoint domain. Assign the majority of traffic to your existing origin.


| Record name | Type | Weight | Value | Set ID | 
| --- | --- | --- | --- | --- | 
| east-bid.example.com | CNAME | 90 | legacy-origin.example.com | legacy | 
| east-bid.example.com | CNAME | 10 | <gateway-id>.<account-id>.gateway.rtbfabric.<region>.amazonaws.com | rtbfabric | 

At this point, approximately 10% of DNS resolutions direct traffic to RTB Fabric.

### Step 2: Monitor and validate
<a name="step2-monitor-validate"></a>

Monitor the following for the initial traffic slice:
+ **Bid response latency** — Compare p50/p99 latency between RTB Fabric and legacy paths using Amazon CloudWatch metrics.
+ **Bid response rates** — Confirm no increase in timeouts or error responses.
+ **(HTTPS only) TLS handshake success** — Verify zero certificate-related failures in your gateway logs.
+ **Routing accuracy** — Confirm requests arrive at the expected link ID by inspecting bid logs.

Allow the initial slice to run for a minimum of one full traffic cycle (typically 1-4 hours depending on your traffic patterns).

### Step 3: Increase traffic incrementally
<a name="step3-increase-traffic"></a>

If metrics are healthy, increase the RTB Fabric weight in stages:


| Stage | Legacy weight | RTB Fabric weight | Approximate RTB Fabric traffic | 
| --- | --- | --- | --- | 
| Initial | 90 | 10 | 10% | 
| Stage 2 | 50 | 50 | 50% | 
| Stage 3 | 20 | 80 | 80% | 
| Full cutover | 0 | 100 | 100% | 

Update the Route 53 record weights for each stage:

```
aws route53 change-resource-record-sets --hosted-zone-id <zone-id> --change-batch '{
  "Changes": [{
    "Action": "UPSERT",
    "ResourceRecordSet": {
      "Name": "east-bid.example.com",
      "Type": "CNAME",
      "SetIdentifier": "rtbfabric",
      "Weight": 50,
      "TTL": 60,
      "ResourceRecords": [{"Value": "<gateway-id>.<account-id>.gateway.rtbfabric.<region>.amazonaws.com"}]
    }
  }, {
    "Action": "UPSERT",
    "ResourceRecordSet": {
      "Name": "east-bid.example.com",
      "Type": "CNAME",
      "SetIdentifier": "legacy",
      "Weight": 50,
      "TTL": 60,
      "ResourceRecords": [{"Value": "legacy-origin.example.com"}]
    }
  }]
}'
```

**Note**  
Weighted routing distributes traffic based on DNS resolution, not per-request. Individual DNS resolvers cache the returned record for the duration of the TTL. Actual traffic distribution may not precisely match the configured weights at any given moment, but converges over time.

### Step 4: Complete the cutover
<a name="step4-complete-cutover"></a>

After validating at 100% traffic on RTB Fabric, remove the legacy weighted record and convert back to a standard CNAME:

```
east-bid.example.com. 300 IN CNAME <gateway-id>.<account-id>.gateway.rtbfabric.<region>.amazonaws.com.
```

Restore the TTL to your standard value (for example, 300 seconds).

## Rollback procedures
<a name="rollback-procedures"></a>

Rollback at any stage consists of redirecting DNS back to the legacy origin.

### During weighted routing (partial cutover)
<a name="rollback-during-weighted"></a>

Set the RTB Fabric record weight to 0 and the legacy record weight to 100:

```
aws route53 change-resource-record-sets --hosted-zone-id <zone-id> --change-batch '{
  "Changes": [{
    "Action": "UPSERT",
    "ResourceRecordSet": {
      "Name": "east-bid.example.com",
      "Type": "CNAME",
      "SetIdentifier": "rtbfabric",
      "Weight": 0,
      "TTL": 60,
      "ResourceRecords": [{"Value": "<gateway-id>.<account-id>.gateway.rtbfabric.<region>.amazonaws.com"}]
    }
  }, {
    "Action": "UPSERT",
    "ResourceRecordSet": {
      "Name": "east-bid.example.com",
      "Type": "CNAME",
      "SetIdentifier": "legacy",
      "Weight": 100,
      "TTL": 60,
      "ResourceRecords": [{"Value": "legacy-origin.example.com"}]
    }
  }]
}'
```

### After full cutover
<a name="rollback-after-cutover"></a>

Replace the CNAME target with the legacy origin:

```
east-bid.example.com. 60 IN CNAME legacy-origin.example.com.
```

**Warning**  
Rollback is bounded by DNS TTL propagation. If you did not lower the TTL before migration, cached DNS entries may continue directing traffic to RTB Fabric for the duration of the original TTL. Always lower the TTL to 60-120 seconds before starting migration and keep it low until you are confident in the cutover.

**Rollback does not require any changes to:**
+ Your RTB Fabric gateway configuration
+ Routing rules or certificate associations
+ Your bidder application
+ Supply-side partner integrations

The RTB Fabric configuration remains in place and can be reused when you retry migration.

## Multi-region migration
<a name="multi-region-migration"></a>

For customers operating in multiple AWS Regions, migrate each region independently. Each region has its own gateway endpoint, certificate configuration, and routing rules.

1. Complete the full migration lifecycle (provision, validate, cutover) in one region first.

1. Use that region as a reference for monitoring thresholds.

1. Proceed with subsequent regions, applying the same weighted routing approach per region.

Create region-specific CNAME records pointing to each region's gateway:


| Record | Target | 
| --- | --- | 
| us-east-bid.example.com | <gateway-id>.<account-id>.gateway.rtbfabric.us-east-1.amazonaws.com | 
| eu-west-bid.example.com | <gateway-id>.<account-id>.gateway.rtbfabric.eu-west-1.amazonaws.com | 

**Note**  
Gateway endpoints, certificates, and routing rules are scoped to a single region. Changes to one region's configuration do not affect other regions.