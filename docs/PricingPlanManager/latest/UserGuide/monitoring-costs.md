# Monitoring and Managing Costs

## AWS Cost Explorer

Flat-rate plans appear in Cost Explorer as charge line items.

**Example Cost Explorer Display**

```
Service                        Service total    November 2025
CloudFront Flat-Rate Plans     $15.00           $15.00
```

### Available Filtering Options

- Group by Dimension: Service, Linked Account, Region, Usage Type
- Service Filter: Select "CloudFront Flat-Rate Plans" from "Choose services" dropdown
- Linked Account Filter: Filter by specific AWS accounts
- Region Filter: Filter by AWS regions
- Date Range: Customizable with Monthly/Daily granularity
- Export: Download as CSV for analysis

## Cost Allocation Tags

### Tag Applicability

For flat-rate plans, only tags applied to the primary billable resource will appear in billing reports. Tags on associated resources that are included in the flat-rate plan do not generate separate charges and therefore do not appear in flat-rate plan billing reports.

### Tagging Strategy

```
Cost Center: CC-12345
Department: Marketing
Project: Website-Redesign
Environment: Production
Application: CustomerPortal
Owner: jane.doe@example.com
```

### Activation Steps

1. Apply tags to resources with flat-rate plans
2. Activate cost allocation tags in Billing and Cost Management console
3. Wait 24 hours for tags to appear in Cost Explorer
4. Create filtered views by tag values

## AWS Cost and Usage Reports (CUR)

###### Note

Flat-rate plans appear in CUR as charge line items only. No usage metrics (requests, data transfer, etc.) are available in CUR for flat-rate plans.

### Configuration

1. Enable CUR in Billing and Cost Management console
2. Configure S3 bucket for report delivery
3. Include resource IDs and tags
4. Set daily granularity
5. Enable report versioning

### Example Queries

**Monthly flat-rate charges (example: CloudFront)**

```
 SELECT
  DATE_TRUNC('month', line_item_usage_start_date) AS month,
  line_item_usage_account_id,
  line_item_usage_account_name,
  SUM(line_item_unblended_cost) AS total_cost
FROM cur_table
WHERE line_item_product_code = 'CloudFrontPlans'
GROUP BY month, line_item_usage_account_id, line_item_usage_account_name
ORDER BY month, total_cost DESC;
```

**Charges by plan tier**

```
 SELECT
  line_item_usage_type AS plan_tier,
  line_item_line_item_description AS plan_description,
  COUNT(DISTINCT line_item_resource_id) AS plan_count,
  SUM(line_item_usage_amount) AS total_usage_count,
  SUM(line_item_unblended_cost) AS total_cost
FROM cur_table
WHERE line_item_product_code = '<service_code>'
GROUP BY plan_tier, plan_description
ORDER BY total_cost DESC;
```

**Resource-level charges**

```
 SELECT
  line_item_resource_id,
  line_item_usage_type AS plan_tier,
  line_item_line_item_description AS plan_description,
  SUM(line_item_usage_amount) AS usage_count,
  SUM(line_item_unblended_cost) AS total_cost
FROM cur_table
WHERE line_item_product_code = '<service_code>'
GROUP BY line_item_resource_id, plan_tier, plan_description
ORDER BY total_cost DESC;
```

**Department-level charges (requires cost allocation tags)**

```
 SELECT
  resource_tags_user_department AS department,
  line_item_usage_type AS plan_tier,
  COUNT(DISTINCT line_item_resource_id) AS resource_count,
  SUM(line_item_unblended_cost) AS total_cost
FROM cur_table
WHERE line_item_product_code = '<service_code>'
  AND resource_tags_user_department IS NOT NULL
GROUP BY department, plan_tier
ORDER BY department, total_cost DESC;
```

###### Note

Replace `<service_code>` with the appropriate service code for your flat-rate plan (e.g., `CloudFrontPlans` for CloudFront). The `line_item_resource_id` represents the primary billable resource. Tags applied to this resource will appear in CUR reports. Tags on associated resources included in the flat-rate plan will not appear.
