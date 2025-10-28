# Network service descriptor template

Defines a network service descriptor (NSD) template.

## Syntax

```
tosca_definitions_version: tnb_simple_yaml_1_0

vnfds:
  - descriptor_id: String
    namespace: String

topology_template:

  inputs:
    SampleInputParameter:
      type: String
      description: "Sample parameter description"
      default: "DefaultSampleValue"

  node_templates:
    SampleNode1: tosca.nodes.AWS.NS
```

## Using defined parameters

When you want to dynamically pass a parameter, such as the CIDR block for the VPC node,
you can use the `{ get_input: `input-parameter-name` }`
syntax and define the parameters in the NSD template. Then reuse the parameter across the
same NSD template.

The following example shows how to define and use parameters:

```
tosca_definitions_version: tnb_simple_yaml_1_0

topology_template:

  inputs:
    cidr_block:
      type: String
      description: "CIDR Block for VPC"
      default: "10.0.0.0/24"

  node_templates:
    ExampleSingleClusterNS:
      type: tosca.nodes.AWS.NS
      properties:
        descriptor_id: "`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"
         .....

    ExampleVPC:
      type: tosca.nodes.AWS.Networking.VPC
      properties:
        cidr_block: { get_input: cidr_block }
```

## VNFD import

`descriptor_id`

The UUID of the descriptor.

Required: Yes

Type: String

Pattern:
`[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

`namespace`

The unique name.

Required: Yes

Type: String

## Topology template

`node_templates`

The possible TOSCA AWS nodes are:

- [AWS.NS](node-ns.md "node-ns.md")
- [AWS.Compute.EKS](node-eks.md "node-eks.md")
- [AWS.Compute.EKS.AuthRole](node-eks-authrole.md "node-eks-authrole.md")
- [AWS.Compute.EKSManagedNode](node-eks-managed-node.md "node-eks-managed-node.md")
- [AWS.Compute.EKSSelfManagedNode](node-eks-self-managed.md "node-eks-self-managed.md")
- [AWS.Compute.PlacementGroup](node-compute-placement-group.md "node-compute-placement-group.md")
- [AWS.Compute.UserData](node-compute-user-data.md "node-compute-user-data.md")
- [AWS.Networking.SecurityGroup](node-networking-security-group.md "node-networking-security-group.md")
- [AWS.Networking.SecurityGroupEgressRule](node-networking-security-group-egress-rule.md "node-networking-security-group-egress-rule.md")
- [AWS.Networking.SecurityGroupIngressRule](node-networking-security-group-ingress-rule.md "node-networking-security-group-ingress-rule.md")
- [AWS.Resource.Import](node-resource-import.md "node-resource-import.md")
- [AWS.Networking.ENI](node-eni.md "node-eni.md")
- [AWS.HookExecution](node-hook-execution.md "node-hook-execution.md")
- [AWS.Networking.InternetGateway](node-internet-gateway.md "node-internet-gateway.md")
- [AWS.Networking.RouteTable](node-route-table.md "node-route-table.md")
- [AWS.Networking.Subnet](node-subnet.md "node-subnet.md")
- [AWS.Deployment.VNFDeployment](node-vnf-deployment.md "node-vnf-deployment.md")
- [AWS.Networking.VPC](node-vpc.md "node-vpc.md")
- [AWS.Networking.NATGateway](node-nat-gateway.md "node-nat-gateway.md")
- [AWS.Networking.Route](node-route.md "node-route.md")
