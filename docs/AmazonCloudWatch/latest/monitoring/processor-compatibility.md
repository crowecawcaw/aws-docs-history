# Processor compatibility and restrictions

###### General processor rules

Maximum count

A pipeline can have at most 20 processors.

Parser placement

Parser processors (OCSF, CSV, Grok, etc.), if used, must be the first processor in a
pipeline.

Unique processors

The following processors can appear only once per pipeline:

- `add_entries`
- `copy_values`

| Processor Type                                 | CloudWatch Logs Source  | S3 Source               | API-based Sources       |
| ---------------------------------------------- | ----------------------- | ----------------------- | ----------------------- |
| OCSF                                           | Must be first processor | Must be first processor | Must be first processor |
| parse_vpc                                      | Must be first processor | Not applicable          | Not applicable          |
| parse_route53                                  | Must be first processor | Not applicable          | Not applicable          |
| parse_json                                     | Must be first processor | Must be first processor | Must be first processor |
| grok                                           | Must be first processor | Must be first processor | Must be first processor |
| csv                                            | Must be first processor | Not compatible          | Not compatible          |
| key_value                                      | Must be first processor | Must be first processor | Must be first processor |
| add_entries                                    | Must be first processor | Must be first processor | Must be first processor |
| copy_values                                    | Must be first processor | Must be first processor | Must be first processor |
| String processors (lowercase, uppercase, trim) | Must be first processor | Must be first processor | Must be first processor |
| Field processors (move_keys, rename_keys)      | Must be first processor | Must be first processor | Must be first processor |
| Data transformation (date, flatten)            | Must be first processor | Must be first processor | Must be first processor |

###### Compatibility definitions

Must be first processor

When used, must be the first processor in the pipeline
configuration

Not compatible

Cannot be used with this source type

Not applicable

Processor is not relevant for this source type

## Processor-specific restrictions

| Processor restrictions by source type | Processor                       | Source Type                                                                                                                                                                                                    | Restrictions |
| ------------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| OCSF                                  | CloudWatch Logs with CloudTrail | • Only allowed when `data_source_name` is<br>`aws_cloudtrail`<br>• Must use CloudTrail-specific schema version<br>• Cannot be combined with other processors                                                   |
| OCSF                                  | API-based Sources               | • Must use source-specific schema (e.g.,<br>microsoft_office365_management_activity for Office<br>365)<br>• Requires specific mapping version for each source<br>type<br>• Must be first processor in pipeline |
| parse_vpc                             | CloudWatch Logs                 | • Only valid for VPC Flow Logs<br>• Must be first processor<br>• Input must contain raw VPC Flow Log<br>format                                                                                                 |
| parse_route53                         | CloudWatch Logs                 | • Only valid for Route 53 Resolver Query Logs<br>• Must be first processor<br>• Input must contain Route 53 Resolver query log<br>format                                                                       |
| add_entries                           | All Sources                     | • Maximum one instance per pipeline<br>• Key names must be valid according to field naming<br>rules                                                                                                            |
| copy_values                           | All Sources                     | • Maximum one instance per pipeline<br>• Source fields must exist in the event                                                                                                                                 |

###### Important

When using processors with restrictions:

- Always validate your pipeline configuration using the
  `ValidateTelemetryPipelineConfiguration` API before
  deployment
- Test the pipeline with sample data using the
  `TestTelemetryPipeline` API to ensure proper
  processing
- Monitor pipeline metrics after deployment to ensure events are being
  processed as expected
