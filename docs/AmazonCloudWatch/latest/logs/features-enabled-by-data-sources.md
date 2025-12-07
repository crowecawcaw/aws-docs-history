# Features enabled by data

sources

Data sources enable advanced log processing and analytics capabilities through field
discovery and consistent data structures.

- **Facets**: Facets are indexed log fields that
  provide interactive filtering and analysis without writing queries. CloudWatch Logs
  automatically creates facets for data source name and type, and you can create
  facet policies on discovered fields to accelerate troubleshooting. Facets
  display value distributions and counts in CloudWatch Logs Insights, making it easy to
  identify patterns through point-and-click exploration.
- **Pipelines**: Create transformation pipelines
  that apply to all logs from a specific data source name and type. This allows
  you to define consistent processing rules for logs from the same source.
- **Field discovery**: CloudWatch Logs automatically
  discovers fields and their data types for each data source name and type
  combination based on pipeline processors. For AWS managed logs, field
  structures are predefined. For application logs, we recommend maintaining
  consistent log formats to maximize compatibility with analytics tools such as
  Amazon S3 tables that require well-defined field structures.
  You can view the complete list of fields and their types for any data source using the
  `GetLogFields` API:

```
aws logs get-log-fields --data-source-name <name>  --data-source-type <type>
```

This field discovery and consistency enables advanced analytics and integrations, as
external tools can work with predictable field structures when processing your log
data.
