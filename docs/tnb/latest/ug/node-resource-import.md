

# AWS.Resource.Import
<a name="node-resource-import"></a>

You can import the following AWS resources into AWS TNB:
+ VPC
+ Subnet
+ Route Table
+ Internet Gateway
+ Security Group

## Syntax
<a name="node-resource-import-syntax"></a>

```
tosca.nodes.AWS.Resource.Import
  properties:
    resource\_type: String
    resource\_id: String
```

## Properties
<a name="node-resource-import-properties"></a>

 `resource_type`    
The resource type that is imported to AWS TNB.  
Required: No  
Type: List

 `resource_id`    
The resource ID that is imported to AWS TNB.  
Required: No  
Type: List

## Example
<a name="node-resource-import-example"></a>

```
SampleImportedVPC:
  type: tosca.nodes.AWS.Resource.Import
  properties:
    resource_type: "tosca.nodes.AWS.Networking.VPC"
    resource_id: "{{vpc-123456}}"
```