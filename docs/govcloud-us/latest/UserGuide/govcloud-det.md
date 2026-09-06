

# Amazon Detective in AWS GovCloud (US)
<a name="govcloud-det"></a>

Amazon Detective makes it easy to analyze, investigate, and quickly identify the root cause of security findings or suspicious activities. Detective automatically collects log data from your AWS resources. It then uses machine learning, statistical analysis, and graph theory to help you visualize and conduct faster and more efficient security investigations.

## Region availability
<a name="region-availability"></a>

Amazon Detective is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-East) 
+  AWS GovCloud (US-West) 

## How Amazon Detective differs
<a name="feature-diffs"></a>
+ In GovCloud Regions, Detective does not validate the email address for member accounts, and does not send invitation emails to member accounts.
+ When accounts are terminated in AWS, Detective cannot automatically remove them from the behavior graph.

## Documentation
<a name="documentation"></a>
+  [Detective documentation](https://docs.aws.amazon.com/detective/latest/adminguide/what-is-detective.html) 

## Export-controlled content
<a name="itar-boundary"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ This service can generate metadata from customer-defined configurations. This metadata includes all configuration data in console fields, descriptions, resource names, and tagging information. AWS suggests customers do not enter export-controlled information in those fields.