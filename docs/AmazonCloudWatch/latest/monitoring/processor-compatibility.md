

# Processor compatibility and restrictions
<a name="processor-compatibility"></a>General processor rules

Maximum count  
A pipeline can have at most 20 processors.

Parser placement  
Parser processors (OCSF, CSV, Grok, and so on), if used, must be the first processor in a pipeline.

Unique processors  
The following processors can appear only once per pipeline:  
+ `add_entries`
+ `copy_values`


| Processor Type | CloudWatch Logs Source | S3 Source | API-based Sources | 
| --- | --- | --- | --- | 
| OCSF | Must be first processor | Must be first processor | Must be first processor | 
| parse\_vpc | Must be first processor | Not applicable | Not applicable | 
| parse\_route53 | Must be first processor | Not applicable | Not applicable | 
| parse\_rds | Must be first processor | Not applicable | Not applicable | 
| parse\_json | Must be first processor | Must be first processor | Must be first processor | 
| grok | Must be first processor | Must be first processor | Must be first processor | 
| csv | Must be first processor | Not compatible | Not compatible | 
| key\_value | Must be first processor | Must be first processor | Must be first processor | 
| add\_entries | Must be first processor | Must be first processor | Must be first processor | 
| copy\_values | Must be first processor | Must be first processor | Must be first processor | 
| String processors (lowercase, uppercase, trim) | Must be first processor | Must be first processor | Must be first processor | 
| Field processors (move\_keys, rename\_keys) | Must be first processor | Must be first processor | Must be first processor | 
| Data transformation (date, flatten) | Must be first processor | Must be first processor | Must be first processor | 

**Compatibility definitions**  

Must be first processor  
When used, must be the first processor in the pipeline configuration

Not compatible  
Cannot be used with this source type

Not applicable  
Processor is not relevant for this source type

## Processor-specific restrictions
<a name="processor-specific-restrictions"></a>

The following table describes processor restrictions by source type.


| Processor | Source Type | Restrictions | 
| --- | --- | --- | 
| OCSF | CloudWatch Logs with CloudTrail |  +  Only allowed when `data_source_name` is `aws_cloudtrail` <br />+  Must use CloudTrail-specific schema version <br />+  Cannot be combined with other processors   | 
| OCSF | API-based Sources |  +  Must use source-specific schema (for example, microsoft\_office365\_management\_activity for Office 365) <br />+  Requires specific mapping version for each source type <br />+  Must be first processor in pipeline   | 
| parse\_vpc | CloudWatch Logs |  +  Only valid for VPC Flow Logs <br />+  Must be first processor <br />+  Input must contain raw VPC Flow Log format   | 
| parse\_route53 | CloudWatch Logs |  +  Only valid for Route 53 Resolver Query Logs <br />+  Must be first processor <br />+  Input must contain Route 53 Resolver query log format   | 
| parse\_rds | CloudWatch Logs |  +  Only valid when `data_source_name` is `amazon_rds` <br />+  Must be first processor <br />+  Takes no parameters; the log type is inferred from the pipeline's `data_source_type`   | 
| add\_entries | All Sources |  +  Maximum one instance per pipeline <br />+  Key names must be valid according to field naming rules   | 
| copy\_values | All Sources |  +  Maximum one instance per pipeline <br />+  Source fields must exist in the event   | 

**Important**  
When using processors with restrictions:  
Always validate your pipeline configuration using the `ValidateTelemetryPipelineConfiguration` API before deployment
Test the pipeline with sample data using the `TestTelemetryPipeline` API to make sure proper processing
Monitor pipeline metrics after deployment to make sure events are being processed as expected