

# Amazon Comprehend Medical in AWS GovCloud (US)
<a name="govcloud-cmpm"></a>

Amazon Comprehend Medical detects useful information in unstructured clinical text. As much as 75 percent of all health record data is found in unstructured text such as physician’s notes, discharge summaries, test results, and case notes. Amazon Comprehend Medical uses Natural Language Processing (NLP) models to sort through enormous quantities of data for valuable information gained through advances in machine learning.

 Amazon Comprehend Medical is currently available in AWS GovCloud (US-West).

## How Amazon Comprehend Medical differs
<a name="how_shared_cmpmlong_differs"></a>

The following differences apply to Amazon Comprehend Medical:

Differences in Quotas/Limits:


| Resource | Default | 
| --- | --- | 
| Transactions per second (TPS) for the `DetectEntities-v2` and `DetectEntities` operations | 2 | 
| Transactions per second (TPS) for the `DetectPHI` operation | 5 | 
| Transactions per second (TPS) for the `StartEntitiesDetectionV2Job`, `StartPHIDetectionJob`, `StopEntitiesDetectionV2Job`, `StopPHIDetectionJob`, `ListEntitiesDetectionV2Jobs`, `ListPHIDetectionJobs`, `DescribeEntitiesDetectionV2Job`, and `DescribePHIDetectionJob` operations | 2 | 

## Documentation
<a name="govcloud-cmpm-docs"></a>
+  [Amazon Comprehend Medical documentation](https://docs.aws.amazon.com/comprehend/latest/dg/comprehend-medical.html) 

## Export-controlled content
<a name="govcloud-cmpm-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ This service can generate metadata from customer-defined configurations. AWS suggests customers do not enter export-controlled information in console fields, descriptions, resource names, and tagging information.