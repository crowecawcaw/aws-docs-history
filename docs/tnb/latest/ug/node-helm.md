

# AWS.Artifacts.Helm

Defines an AWS Helm Node.

## Syntax
<a name="node-helm-syntax"></a>

```yaml
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

```yaml
SampleHelm:
  type: tosca.nodes.AWS.Artifacts.Helm
  properties:
    implementation: "./vnf-helm"
```