# VNFD template

Defines a virtual network function descriptor (VNFD) template.

## Syntax

```
tosca_definitions_version: tnb_simple_yaml_1_0

topology_template:

  inputs:
    SampleInputParameter:
      type: String
      description: "Sample parameter description"
      default: "DefaultSampleValue"

  node_templates:
    SampleNode1: tosca.nodes.AWS.VNF
```

## Topology template

`node_templates`

The TOSCA AWS Nodes. The possible nodes are:

- [AWS.VNF](node-vnf.md "node-vnf.md")
- [AWS.Artifacts.Helm](node-helm.md "node-helm.md")
