# ApiStateMachineAuth

Configures authorization at the event level, for a specific API, path, and method.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  ApiKeyRequired: `Boolean`
  AuthorizationScopes: `List`
  Authorizer: `String`
  ResourcePolicy: `ResourcePolicyStatement`

```

## Properties

`ApiKeyRequired`

Requires an API key for this API, path, and method.

_Type_: Boolean

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`AuthorizationScopes`

The authorization scopes to apply to this API, path, and method.

The scopes that you specify will override any scopes applied by the `DefaultAuthorizer` property if you have specified it.

_Type_: List

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`Authorizer`

The `Authorizer` for a specific state machine.

If you have specified a global authorizer for the API and want to make this state machine public, override the global authorizer by setting `Authorizer` to `NONE`.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`ResourcePolicy`

Configure the resource policy for this API and path.

_Type_: [ResourcePolicyStatement](sam-property-statemachine-resourcepolicystatement.md "sam-property-statemachine-resourcepolicystatement.md")

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

## Examples

### StateMachine-Auth

The following example specifies authorization at the state machine level.

#### YAML

```
Auth:
  ApiKeyRequired: true
  Authorizer: NONE

```
