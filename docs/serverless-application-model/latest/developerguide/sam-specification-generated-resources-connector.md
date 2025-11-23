# CloudFormation resources generated when

you specify AWS::Serverless::Connector

###### Note

When you define connectors through the embedded `Connectors` property, it is first transformed
into an `AWS::Serverless::Connector` resource before generating these resources.

When you specify an `AWS::Serverless::Connector` resource in an AWS SAM template,
AWS SAM generates the following AWS CloudFormation resources as needed.

**`AWS::IAM::ManagedPolicy`**

_`LogicalId`:_``<connector‑LogicalId>`Policy`

_Referenceable property:_ N/A (To reference this CloudFormation resource, you
must use the `LogicalId`.)

**`AWS::SNS::TopicPolicy`**

_`LogicalId`:_``<connector‑LogicalId>`TopicPolicy`

_Referenceable property:_ N/A (To reference this CloudFormation resource, you
must use the `LogicalId`.)

**`AWS::SQS::QueuePolicy`**

_`LogicalId`:_``<connector‑LogicalId>`QueuePolicy`

_Referenceable property:_ N/A (To reference this CloudFormation resource, you
must use the `LogicalId`.)

**`AWS::Lambda::Permission`**

_`LogicalId`:_`<connector‑LogicalId>`<permission>`LambdaPermission`

`<permission>` is a permission specified by the `Permissions` property. For example, `Write`.

_Referenceable property:_ N/A (To reference this CloudFormation resource, you
must use the `LogicalId`.)
