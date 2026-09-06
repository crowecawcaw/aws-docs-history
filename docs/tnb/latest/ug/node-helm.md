

# AWS.Artifacts.Helm
<a name="node-helm"></a>

Defines an AWS Helm Node.

## Syntax
<a name="node-helm-syntax"></a>

```
tosca.nodes.AWS.Artifacts.Helm:
  properties:
    implementation: String
```

## Properties
<a name="node-helm-properties"></a>

 `implementation`    
The local directory that contains the Helm chart within the CSAR package.  
Required: Yes  
Type: String

## Example
<a name="node-helm-example"></a>

```
SampleHelm:
  type: tosca.nodes.AWS.Artifacts.Helm
  properties:
    implementation: "./vnf-helm"
```