

# RevisionWeights
<a name="sam-property-webfunction-revisionweights"></a>

Specifies how a Web Function endpoint splits traffic across revisions. Use this property when `AutoDeploymentMode` is `Disabled`, for example to run a canary or blue/green deployment.

`RevisionWeights` is a map. Each key is a revision ID, and each value is the percentage of traffic to route to that revision. The following rules apply:
+ Specify at most two revisions.
+ Each weight is an integer from 1 to 100, and the weights must add up to 100.
+ Individual weights can be intrinsic functions, but the map itself can't be an intrinsic function.

*Type*: Map

*CloudFormation compatibility*: This property is similar to the `[RevisionWeights](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-webfunctionendpoint.html#cfn-lambda-webfunctionendpoint-revisionweights)` property of an `AWS::Lambda::WebFunctionEndpoint` resource. AWS SAM converts the map into a list of objects, each with a `RevisionId` and a `Weight`.

## Syntax
<a name="sam-property-webfunction-revisionweights-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-webfunction-revisionweights-syntax.yaml"></a>

```
{{revision-id}}: {{Integer}}
{{revision-id}}: {{Integer}}
```

## Examples
<a name="sam-property-webfunction-revisionweights-examples"></a>

### Canary split
<a name="sam-property-webfunction-revisionweights-example-canary"></a>

The following example sends 90% of traffic to `rev-abc123` and 10% to `rev-def456`.

```
AutoDeploymentMode: Disabled
RevisionWeights:
  rev-abc123: 90
  rev-def456: 10
```

AWS SAM transforms this into the following endpoint property:

```
RevisionWeights:
  - RevisionId: rev-abc123
    Weight: 90
  - RevisionId: rev-def456
    Weight: 10
```