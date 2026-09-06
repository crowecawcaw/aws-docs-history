

# AWS Resource Access Manager in AWS GovCloud (US)
<a name="govcloud-ram"></a>

AWS Resource Access Manager (RAM) is a service that enables you to easily and securely share AWS resources with any AWS account or within your AWS Organization. You can share AWS Transit Gateways, Subnets, AWS License Manager configurations, and Amazon Route 53 Resolver rules resources with RAM. Many organizations use multiple accounts to create administrative or billing isolation, and to limit the impact of errors. RAM eliminates the need to create duplicate resources in multiple accounts, reducing the operational overhead of managing those resources in every single account you own. You can create resources centrally in a multi-account environment, and use RAM to share those resources across accounts in three simple steps: create a Resource Share, specify resources, and specify accounts. RAM is available to you at no additional charge.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How AWS Resource Access Manager differs
<a name="govcloud-ram-diffs"></a>

The following differences apply to AWS Resource Access Manager:
+ Sharing of Amazon Aurora DB clusters is not available.
+ Sharing of AWS CodeBuild projects is not available.
+ Sharing AWS CodeBuild Report groups is not available.
+ Sharing of AWS App Mesh Meshes is not available.

## Documentation
<a name="govcloud-ram-docs"></a>
+  [AWS Resource Access Manager documentation](https://docs.aws.amazon.com/ram) 

## Export-controlled content
<a name="govcloud-ram-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ Resource Share name cannot contain export-controlled data.