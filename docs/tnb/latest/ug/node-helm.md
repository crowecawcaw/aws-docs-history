# AWS.Artifacts.Helm

Defines an AWS Helm Node.

## Syntax

```
tosca.nodes.AWS.Artifacts.Helm:
  properties:
    implementation: String
```

## Properties

`implementation`

The local directory that contains the Helm chart within the CSAR
package.

Required: Yes

Type: String

## Example

```
SampleHelm:
  type: tosca.nodes.AWS.Artifacts.Helm
  properties:
    implementation: "./vnf-helm"
```
