

# VNFD template
<a name="vnfd-template"></a>

Defines a virtual network function descriptor (VNFD) template.

## Syntax
<a name="vnfd-syntax"></a>

```
tosca_definitions_version: tnb_simple_yaml_1_0

topology_template:

  inputs:
    SampleInputParameter:
      type: String
      description: "Sample parameter description"
      default: "DefaultSampleValue"

  node\_templates:
    SampleNode1: tosca.nodes.AWS.VNF
```

## Topology template
<a name="vnfd-topology-template"></a>

 `node_templates`    
The TOSCA AWS Nodes. The possible nodes are:  
+ [AWS.VNF](node-vnf.md)
+ [AWS.Artifacts.Helm](node-helm.md)