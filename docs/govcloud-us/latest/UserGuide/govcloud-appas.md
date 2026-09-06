

# Application Auto Scaling in AWS GovCloud (US)
<a name="govcloud-appas"></a>

Application Auto Scaling is a web service for developers and system administrators who need a solution for automatically scaling their scalable resources for individual AWS services beyond Amazon EC2.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How Application Auto Scaling differs
<a name="govcloud-appas-diffs"></a>

The following differences apply to Application Auto Scaling:
+ Application Auto Scaling notifications are not currently supported in the AWS Health Dashboard.
+ The following resources are not currently supported for Application Auto Scaling in the AWS GovCloud (US-West) Region:
  +  Amazon Neptune clusters
  + Spot Fleet requests
  + Custom resources
+ The following resources are not currently supported for Application Auto Scaling in the AWS GovCloud (US-East) Region:
  +  Amazon Comprehend document classification and entity recognizer endpoints
  +  Amazon Neptune clusters
  +  SageMaker AI endpoint variants
  + Spot Fleet requests
  + Custom resources

## Documentation
<a name="govcloud-awsas-docs"></a>
+  [Amazon EC2 Auto Scaling in AWS GovCloud (US)](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-as.html) 
+  [AWS Auto Scaling documentation](https://docs.aws.amazon.com/documentation/autoscaling/) 

## Export-controlled content
<a name="govcloud-awsas-itar-2"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+  Auto Scaling is not permitted to contain export-controlled data.
+ For example, do not enter export-controlled data in the following fields:
  + Scaling policy names
  + Scaling policy configuration