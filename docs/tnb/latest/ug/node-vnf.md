

# AWS.VNF
<a name="node-vnf"></a>

Defines an AWS virtual network function (VNF) node.

## Syntax
<a name="vnf-syntax"></a>

```
tosca.nodes.AWS.VNF:
  properties:
    descriptor\_id: String
    descriptor\_version: String
    descriptor\_name: String
    provider: String
  requirements:
    helm: String
```

## Properties
<a name="vnf-properties"></a>

 `descriptor_id`    
The UUID of the descriptor.  
Required: Yes  
Type: String  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 `descriptor_version`    
The version of the VNFD.  
Required: Yes  
Type: String  
Pattern: `^[0-9]{1,5}\\.[0-9]{1,5}\\.[0-9]{1,5}.*`

 `descriptor_name`    
The name of the descriptor.  
Required: Yes  
Type: String

 `provider`    
The author of the VNFD.  
Required: Yes  
Type: String

## Requirements
<a name="vnf-requirements"></a>

 `helm`    
The Helm directory defining container artifacts. This is a reference to [AWS.Artifacts.Helm](node-helm.md).   
Required: Yes  
Type: String

## Example
<a name="vnf-example"></a>

```
SampleVNF:
  type: tosca.nodes.AWS.VNF
  properties:
    descriptor_id: "{{6a792e0c-be2a-45fa-989e-5f89d94ca898}}"
    descriptor_version: "{{1.0.0}}"
    descriptor_name: "{{Test VNF Template}}"
    provider: "{{Operator}}"
  requirements:
    helm: SampleHelm
```