

# ReplicaRegions
<a name="sam-property-webfunction-replicaregions"></a>

Specifies the Regions that a `MultiRegion` or `PerRegion` Web Function endpoint replicates the function to. You can specify a list of Region codes and Region groups, or an object that includes Regions and optionally excludes some of them.

You can use the following Region groups anywhere you specify a Region:
+ `US`: `us-east-1`, `us-east-2`, `us-west-1`, `us-west-2`
+ `EU`: `eu-west-1`, `eu-west-2`, `eu-west-3`, `eu-central-1`, `eu-north-1`
+ `AP`: `ap-south-1`, `ap-northeast-1`, `ap-northeast-2`, `ap-northeast-3`, `ap-southeast-1`, `ap-southeast-2`
+ `CA`: `ca-central-1`
+ `SA`: `sa-east-1`
+ `SPARSE_GLOBAL`: one or two Regions per continent for global coverage with fewer Regions: `us-east-1`, `eu-west-1`, `eu-central-1`, `ap-northeast-1`, `ap-southeast-1`, `ap-southeast-2`, `sa-east-1`
+ `ALL_STANDARD`: every Region in the `US`, `EU`, `AP`, `CA`, and `SA` groups (17 Regions)

## Syntax
<a name="sam-property-webfunction-replicaregions-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-webfunction-replicaregions-syntax.yaml"></a>

```
[ExcludeRegions](#sam-webfunction-replicaregions-excluderegions): {{List}}
[IncludeRegions](#sam-webfunction-replicaregions-includeregions): {{List}}
```

## Properties
<a name="sam-property-webfunction-replicaregions-properties"></a>

 `ExcludeRegions`   <a name="sam-webfunction-replicaregions-excluderegions"></a>
A list of Region codes and Region groups to remove from `IncludeRegions`. You must also specify `IncludeRegions`. Entries can't be intrinsic functions, and you can't use `ExcludeRegions` when `IncludeRegions` contains intrinsic functions.  
*Type*: List  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `IncludeRegions`   <a name="sam-webfunction-replicaregions-includeregions"></a>
A list of Region codes and Region groups to replicate the function to. The list itself can't be an intrinsic function, but individual entries can.  
*Type*: List  
*Required*: No  
*CloudFormation compatibility*: This property is similar to the `[Regions](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-webfunctionendpoint.html#cfn-lambda-webfunctionendpoint-regions)` property of an `AWS::Lambda::WebFunctionEndpoint` resource. AWS SAM expands Region groups and removes any `ExcludeRegions` entries to produce the Region list. 

## Examples
<a name="sam-property-webfunction-replicaregions-examples"></a>

### List of Regions
<a name="sam-property-webfunction-replicaregions-example-list"></a>

The following example replicates the function to two Regions.

```
ReplicaRegions:
  - us-east-1
  - eu-west-1
```

### Region group with exclusions
<a name="sam-property-webfunction-replicaregions-example-exclude"></a>

The following example replicates the function to the US Regions except `us-west-1`.

```
ReplicaRegions:
  IncludeRegions:
    - US
  ExcludeRegions:
    - us-west-1
```