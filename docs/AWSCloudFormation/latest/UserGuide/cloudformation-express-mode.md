

# Deploy AWS CloudFormation stacks faster with express mode
<a name="cloudformation-express-mode"></a>

With CloudFormation express mode, you can complete stack operations as soon as CloudFormation applies the resource configuration, without waiting for resources to fully stabilize. Use express mode to create, update, and delete stacks significantly faster during iterative development workflows.

Express mode works with all existing CloudFormation templates. You don't need to make any template changes to use express mode.

**Topics**
+ [When to use express mode](#express-mode-when-to-use)
+ [How express mode works](#express-mode-how-it-works)
+ [How CloudFormation handles dependencies in express mode](#express-mode-dependencies)
+ [Getting started with express mode](#express-mode-getting-started)
+ [Rollback behavior with express mode](#express-mode-rollback)
+ [Express mode and nested stacks](#express-mode-nested-stacks)
+ [Resource readiness considerations](#express-mode-resource-readiness)
+ [Unsupported features and limitations](#express-mode-unsupported)
+ [Comparison with AWS CDK hotswap deployments](#express-mode-comparison-cdk-hotswap)
+ [Related resources](#express-mode-related-resources)

## When to use express mode
<a name="express-mode-when-to-use"></a>

Use express mode for development and iteration workflows where speed is more important than waiting for full resource stabilization. Use express mode when:
+ You iterate on template changes during development.
+ You want faster feedback on whether your resource configurations are valid.
+ You don't need to wait for resources to be fully operational before proceeding.

For production deployments where you need to verify that resources are fully stabilized and operational before considering the deployment complete, use the default deployment mode.

## How express mode works
<a name="express-mode-how-it-works"></a>

In the default deployment mode, CloudFormation waits for each resource to reach a fully stabilized state before reporting the resource as complete. For example, when creating an Amazon EC2 instance, CloudFormation waits until the instance is in the `running` state.

In express mode, CloudFormation typically considers a resource operation complete as soon as the API call to create, update, or delete the resource succeeds. In most cases, CloudFormation does not wait for the resource to reach its final operational state.

This means that after an express mode stack operation completes:
+ Resources might still be initializing or propagating changes.
+ Resources might not yet be ready to serve traffic or accept connections.
+ Delete operations might still be in progress.

## How CloudFormation handles dependencies in express mode
<a name="express-mode-dependencies"></a>

Express mode respects resource dependencies defined in your template. If a resource references another resource's ID or attribute (via `Ref` or `Fn::GetAtt`), CloudFormation confirms the referenced resource's configuration is applied before starting the dependent resource. If a dependent resource encounters a transient failure because a referenced resource isn't ready, CloudFormation retries the operation.

Resources that have no dependencies on each other can proceed in parallel.

Express mode does not change the dependency ordering of your resources. It changes when the stack operation reports complete.

## Getting started with express mode
<a name="express-mode-getting-started"></a>

You can use express mode with the AWS Command Line Interface (AWS CLI), the AWS Cloud Development Kit (AWS CDK) (AWS CDK), the CloudFormation console, and change sets. The following sections describe how to enable express mode with each method.

### Using express mode with the AWS CLI
<a name="express-mode-cli"></a>

To use express mode with the AWS CLI, add the `--deployment-config` parameter to your stack operation commands.

**Create a stack with express mode**  
The following command creates a stack using express mode:

```
aws cloudformation create-stack --stack-name {{my-stack}} \
    --template-body {{file://my-template.yaml}} \
    --deployment-config '{"mode": "EXPRESS"}'
```

**Update a stack with express mode**  
The following command updates a stack using express mode:

```
aws cloudformation update-stack --stack-name {{my-stack}} \
    --template-body {{file://my-template.yaml}} \
    --deployment-config '{"mode": "EXPRESS"}'
```

**Delete a stack with express mode**  
The following command deletes a stack using express mode:

```
aws cloudformation delete-stack --stack-name {{my-stack}} \
    --deployment-config '{"mode": "EXPRESS"}'
```

### Using express mode with the AWS CDK
<a name="express-mode-cdk"></a>

To use express mode with the AWS Cloud Development Kit (AWS CDK) (AWS CDK), use the `--express` flag with the `cdk deploy` command:

```
cdk deploy --express
```

### Using express mode with AWS SAM
<a name="express-mode-sam"></a>

To use express mode with the AWS SAM CLI, add the `--express` flag to your deploy or sync commands:

```
sam deploy --express
```

```
sam sync --express
```

To persist the setting in your project configuration, use `--save-params`:

```
sam deploy --express --save-params
```

This saves `express = true` to your `samconfig.toml` file so subsequent deployments use Express mode automatically.

When express mode is enabled, the AWS SAM CLI passes the deployment configuration to CloudFormation. The `--disable-rollback` flag controls rollback behavior within the deployment configuration.

### Using express mode with the console
<a name="express-mode-console"></a>

When creating or updating a stack in the CloudFormation console, you can enable express mode in the **Configure stack options** step. Under **Deployment options**, select **Express** for the deployment mode.

### Using express mode with change sets
<a name="express-mode-change-sets"></a>

You can use express mode with change sets by specifying the deployment configuration when creating the change set:

```
aws cloudformation create-change-set --stack-name {{my-stack}} \
    --change-set-name {{my-change-set}} \
    --template-body {{file://my-template.yaml}} \
    --deployment-config '{"mode": "EXPRESS"}'
```

When you execute the change set, CloudFormation applies the express mode deployment configuration specified during change set creation.

## Rollback behavior with express mode
<a name="express-mode-rollback"></a>

When you use express mode, CloudFormation disables rollback by default. If a resource operation fails, CloudFormation does not automatically roll back the changes.

To re-enable rollback when using express mode, set `disableRollback` to `false` in the `--deployment-config` parameter:

```
aws cloudformation create-stack --stack-name {{my-stack}} \
    --template-body {{file://my-template.yaml}} \
    --deployment-config '{"mode": "EXPRESS", "disableRollback": false}'
```

## Express mode and nested stacks
<a name="express-mode-nested-stacks"></a>

When you use express mode on a parent stack, the setting propagates to all nested stacks in the hierarchy. You don't need to specify express mode for each nested stack separately. All resources in the root stack and its nested stacks complete as soon as their configuration is applied.

## Resource readiness considerations
<a name="express-mode-resource-readiness"></a>

Express mode completes resource operations before resources reach a fully stabilized state, so any resource might require additional time to become fully ready to serve traffic or complete multi-region propagation. The following table illustrates the kinds of resource behavior you can expect, using examples across different resource types. These examples are illustrative and don't represent a complete list of supported resources.


| Resource type | Operation | Readiness behavior | 
| --- | --- | --- | 
| Amazon CloudFront distribution | Create/Update | Distribution might take several minutes to deploy globally after configuration is applied. | 
| Amazon EC2 instance | Create | Instance might still be initializing (running user data scripts, status checks) after the stack operation completes. | 
| AWS Lambda function | Delete | Function resources might still be cleaning up after the delete operation reports complete. | 
| Amazon Elastic Container Service (Amazon ECS) service | Create/Update | Service tasks might still be starting or reaching a steady state after the stack operation completes. | 

## Unsupported features and limitations
<a name="express-mode-unsupported"></a>

The following features and services are not supported with express mode:

CloudFormation StackSets  
CloudFormation does not support express mode with StackSets operations.

The following resources have specific behavior with express mode:

Custom resources  
Custom resources (including `AWS::CloudFormation::CustomResource` and `Custom::*` resources) follow their default behavior. CloudFormation waits for the custom resource to send a response signal before considering the operation complete, even in express mode. To prevent a slow or stuck custom resource from delaying fast iteration workflows, set a maximum wait time with the `ServiceTimeout` property. For more information, see [Response timeout](template-custom-resources.md#response-timeout).

## Comparison with AWS CDK hotswap deployments
<a name="express-mode-comparison-cdk-hotswap"></a>

The following table compares express mode with AWS CDK hotswap deployments.


| Feature | Express mode | AWS CDK hotswap | 
| --- | --- | --- | 
| Deployment mechanism | Uses CloudFormation for all resource operations | Bypasses CloudFormation and calls service APIs directly | 
| Template compatibility | Works with all existing CloudFormation templates | Supports a limited set of resource types | 
| Stack state | Stack state remains consistent with template | Stack state might drift from template | 
| Rollback support | Supports rollback (disabled by default) | No rollback support | 
| Resource coverage | All CloudFormation resource types | Limited resource types (AWS Lambda, Amazon ECS, AWS Step Functions, and others) | 
| Recommended use | Development and iteration workflows | Development workflows with supported resources only | 

## Related resources
<a name="express-mode-related-resources"></a>
+ [Choose how to handle failures when provisioning resources](stack-failure-options.md)
+ [Nested stacks](using-cfn-nested-stacks.md)
+ [Update stacks using change sets](using-cfn-updating-stacks-changesets.md)
+ [CreateStack](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStack.html) in the *AWS CloudFormation API Reference*