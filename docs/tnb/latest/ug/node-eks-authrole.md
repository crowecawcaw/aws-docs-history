# AWS.Compute.EKS.AuthRole

An AuthRole allows you to add IAM roles to the Amazon EKS cluster `aws-auth`
`ConfigMap` so that users can access the Amazon EKS cluster using an IAM role.

## Syntax

```
tosca.nodes.AWS.Compute.EKS.AuthRole:
  properties:
    role_mappings: List
      arn: String
      groups: List
  requirements:
    clusters: List
```

## Properties

`role_mappings`

List of mappings that define IAM roles that need to be added to the Amazon EKS
cluster `aws-auth`
`ConfigMap`.

`arn`

The ARN of the IAM role.

Required: Yes

Type: String

`groups`

Kubernetes groups to assign to the role defined in
`arn`.

Required: No

Type: List

## Requirements

`clusters`

An [AWS.Compute.EKS](node-eks.md "node-eks.md") node.

Required: Yes

Type: List

## Example

```
EKSAuthMapRoles:
    type: tosca.nodes.AWS.Compute.EKS.AuthRole
    properties:
        role_mappings:
        - arn: arn:aws:iam::${AWS::TNB::AccountId}:role/`TNBHookRole1`
          groups:
          - system:nodes
          - system:bootstrappers
        - arn: arn:aws:iam::${AWS::TNB::AccountId}:role/`TNBHookRole2`
          groups:
          - system:nodes
          - system:bootstrappers
    requirements:
         clusters:
         - `Free5GCEKS1`
         - `Free5GCEKS2`
```
