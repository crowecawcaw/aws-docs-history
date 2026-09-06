

# ManagedResourceTags
<a name="sam-property-capacityprovider-managedresourcetags"></a>

Applies explicit tags to the Amazon Elastic Compute Cloud instances and other resources that the capacity provider provisions and manages on your behalf.

**Note**  
The `ManagedResourceTags` property controls tagging of the Amazon EC2 instances and other resources that Lambda manages for the capacity provider. This property differs from the [PropagateTags](sam-resource-capacityprovider.md#sam-capacityprovider-propagatetags) property, which specifies whether AWS SAM propagates the [Tags](sam-resource-capacityprovider.md#sam-capacityprovider-tags) property to the CloudFormation resources that AWS SAM generates from your template.

## Syntax
<a name="sam-property-capacityprovider-managedresourcetags-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-capacityprovider-managedresourcetags-syntax.yaml"></a>

```
[Tags](#sam-capacityprovider-managedresourcetags-tags): {{Map}}
```

## Properties
<a name="sam-property-capacityprovider-managedresourcetags-properties"></a>

The following properties are supported for `ManagedResourceTags`.

 `Tags`   <a name="sam-capacityprovider-managedresourcetags-tags"></a>
A map of key-value pairs to apply to the Amazon EC2 instances and other resources that the capacity provider manages.  
*Type*: Map  
*Required*: No  
*CloudFormation compatibility*: AWS SAM uses this property to construct the `[PropagateTags](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-capacityprovider.html#cfn-lambda-capacityprovider-propagatetags)` property of an `AWS::Lambda::CapacityProvider` resource. AWS SAM sets `Mode` to `Explicit` and converts the key-value pairs to a list of Tag objects in `ExplicitTags`. 

## Examples
<a name="sam-property-capacityprovider-managedresourcetags-examples"></a>

### Apply explicit tags to managed resources
<a name="sam-property-capacityprovider-managedresourcetags-examples-explicit"></a>

The following example applies an explicit set of tags to the Amazon EC2 instances that the capacity provider manages.

```
ManagedResourceTags:
  Tags:
    CostCenter: {{cc-1234}}
    Environment: {{Production}}
```