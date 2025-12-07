# Implement preventative controls for Lambda with AWS Config

It is essential to ensure compliance in your serverless
applications as early in the development process as possible. In this topic, we cover how to
implement preventative controls using [AWS Config](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md"). This allows you to implement compliance checks earlier in the development process
and enables you to implement the same controls in your CI/CD pipelines. This also standardizes
your controls in a centrally managed repository of rules so that you can apply your controls
consistently across your AWS accounts.

For example, suppose your compliance administrators defined a requirement to ensure that all Lambda functions include AWS X-Ray tracing. With AWS Config's proactive mode, you can run compliance checks on your Lambda function resources before deployment, reducing the risk of deploying improperly configured Lambda functions and saving developers time by giving them faster feedback on infrastructure as code templates.
The following is a visualization of the flow for preventative controls with AWS Config:

![CloudFormation requests must pass AWS Config rules before provisioning.](images/governance-config-1.png)

Consider a requirement that all Lambda functions must have tracing enabled. In response, the
platform team identifies the need for a specific AWS Config rule to run proactively across all
accounts. This rule flags any Lambda function that lacks a configured X-Ray tracing configuration
as a non-compliant resource. The team develops a rule, packages it in a
[conformance
pack](../../../config/latest/developerguide/conformance-packs.md "../../../config/latest/developerguide/conformance-packs.md"), and deploys the conformance pack across all AWS accounts to ensure that all accounts
in the organization uniformly apply these controls. You can write the rule in AWS CloudFormation Guard
2.x.x syntax, which takes the following form:

```
rule name when condition { assertion }
```

The following is a sample Guard rule that checks to ensure Lambda functions has tracing
enabled:

```
rule lambda_tracing_check {
  when configuration.tracingConfig exists {
      configuration.tracingConfig.mode == "Active"
  }
}
```

The platform team takes further action by mandating that every AWS CloudFormation deployment invokes a
pre-create/update
[hook](../../../cloudformation-cli/latest/userguide/hooks-structure.md "../../../cloudformation-cli/latest/userguide/hooks-structure.md").
They assume full responsibility for developing this hook and configuring the pipeline,
strengthening the centralized control of compliance rules and sustaining their consistent
application across all deployments. To develop, package, and register a hook, see
[Developing AWS CloudFormation Hooks](../../../cloudformation-cli/latest/hooks-userguide/hooks-develop.md "../../../cloudformation-cli/latest/hooks-userguide/hooks-develop.md") in the CloudFormation Command Line Interface (CFN-CLI) documentation.
You can use the [CloudFormation CLI](../../../cloudformation-cli/latest/userguide/initiating-hooks-project-python.md "../../../cloudformation-cli/latest/userguide/initiating-hooks-project-python.md") to create the hook project:

```
cfn init
```

This command asks you for some basic information about your hook project and creates a project
with following files in it:

```
README.md
`<hook-name>`.json
rpdk.log
src/handler.py
template.yml
hook-role.yaml
```

As a hook developer, you need to add the desired target resource type in the
`<hook-name>.json` configuration file. In the
configuration below, a hook is configured to execute before any Lambda function is created using
CloudFormation. You can add similar handlers for `preUpdate` and `preDelete` actions as well.

```
    "handlers": {
        "preCreate": {
            "targetNames": [
                "AWS::Lambda::Function"
            ],
            "permissions": []
        }
    }
```

You also need to ensure that the CloudFormation hook has appropriate permissions to call the AWS Config APIs. You can do that by updating the role definition file named
`hook-role.yaml`. The role definition file has the following trust policy by
default, which allows CloudFormation to assume the role.

```
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - hooks.cloudformation.amazonaws.com
                - resources.cloudformation.amazonaws.com
```

To allow this hook to call config APIs, you must add following permissions to the Policy statement.
Then you submit the hook project using the `cfn submit` command, where
CloudFormation creates a role for you with the required permissions.

```
      Policies:
        - PolicyName: HookTypePolicy
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action:
                  - "config:Describe*"
                  - "config:Get*"
                  - "config:List*"
                  - "config:SelectResourceConfig"
                Resource: "*
```

Next, you need to write a Lambda function in a `src/handler.py` file. Within this
file, you find methods named `preCreate`, `preUpdate`, and `preDelete` already created when you
initiated the project. You aim to write a common, reusable function that calls the AWS Config
`StartResourceEvaluation` API in proactive mode using the AWS SDK for Python (Boto3). This API call takes resource properties as input and evaluates the resource against the
rule definition.

```
def validate_lambda_tracing_config(resource_type, function_properties: MutableMapping[str, Any]) -> ProgressEvent:
  LOG.info("Fetching proactive data")
  config_client = boto3.client('config')
  resource_specs = {
      'ResourceId': 'MyFunction',
      'ResourceType': resource_type,
      'ResourceConfiguration': json.dumps(function_properties),
      'ResourceConfigurationSchemaType': 'CFN_RESOURCE_SCHEMA'
  }
  LOG.info("Resource Specifications:", resource_specs)
  eval_response = config_client.start_resource_evaluation(EvaluationMode='PROACTIVE', ResourceDetails=resource_specs, EvaluationTimeout=60)
  ResourceEvaluationId = eval_response.ResourceEvaluationId
  compliance_response = config_client.get_compliance_details_by_resource(ResourceEvaluationId=ResourceEvaluationId)
  LOG.info("Compliance Verification:", compliance_response.EvaluationResults[0].ComplianceType)
  if "NON_COMPLIANT" == compliance_response.EvaluationResults[0].ComplianceType:
      return ProgressEvent(status=OperationStatus.FAILED, message="Lambda function found with no tracing enabled : FAILED", errorCode=HandlerErrorCode.NonCompliant)
  else:
      return ProgressEvent(status=OperationStatus.SUCCESS, message="Lambda function found with tracing enabled : PASS.")
```

Now you can call the common function from the handler for the pre-create hook. Here's an example of the
handler:

```
@hook.handler(HookInvocationPoint.CREATE_PRE_PROVISION)
def pre_create_handler(
        session: Optional[SessionProxy],
        request: HookHandlerRequest,
        callback_context: MutableMapping[str, Any],
        type_configuration: TypeConfigurationModel
) -> ProgressEvent:
    LOG.info("Starting execution of the hook")
    target_name = request.hookContext.targetName
    LOG.info("Target Name:", target_name)
    if "AWS::Lambda::Function" == target_name:
        return validate_lambda_tracing_config(target_name,
            request.hookContext.targetModel.get("resourceProperties")
        )
    else:
        raise exceptions.InvalidRequest(f"Unknown target type: {target_name}")
```

After this step you can register the hook and configure it to listen to all AWS Lambda function
creation events.

A developer prepares the infrastructure as code (IaC) template for a serverless microservice using
Lambda. This preparation includes adherence to internal standards, followed by locally testing
and committing the template to the repository. Here's an example IaC template:

```
  MyLambdaFunction:
  Type: 'AWS::Lambda::Function'
  Properties:
    Handler: index.handler
    Role: !GetAtt LambdaExecutionRole.Arn
    FunctionName: MyLambdaFunction
    Code:
      ZipFile: |
        import json

        def handler(event, context):
            return {
                'statusCode': 200,
                'body': json.dumps('Hello World!')
            }
    Runtime: python3.14
    TracingConfig:
        Mode: PassThrough
    MemorySize: 256
    Timeout: 10
```

As part of the CI/CD process, when the CloudFormation template is deployed, the CloudFormation
service invokes the pre-create/update hook right before provisioning
`AWS::Lambda::Function` resource type. The hook utilizes AWS Config rules running
in proactive mode to verify that the Lambda function configuration includes the mandated tracing
configuration. The response from the hook determines the next step. If compliant, the hook signals
success, and CloudFormation proceeds to provision the resources. If not, the CloudFormation stack
deployment fails, the pipeline comes to an immediate halt, and the system records the details for
subsequent review. Compliance notifications are sent to the relevant stakeholders.

You can find the hook success/fail information in the CloudFormation console:

![Hook success/fail information in the CloudFormation console](images/governance-config-2.png)

If you have logs enabled for your CloudFormation hook, you can capture the hook evaluation result.
Here is a sample log for a hook with a failed status, indicating that the Lambda function does not
have X-Ray enabled:

![Sample log for a hook with a failed status](images/governance-config-3.png)

If the developer chooses to change the IaC to update `TracingConfig Mode` value
to `Active` and redeploy, the hook executes successfully and the stack proceeds
with creating the Lambda resource.

![CloudFormation console shows successful resource deployment](images/governance-config-4.png)

In this way, you can implement preventative controls with AWS Config in proactive mode when
developing and deploying serverless resources in your AWS accounts. By integrating AWS Config
rules into the CI/CD pipeline, you can identify and optionally block non-compliant resource
deployments, such as Lambda functions that lack an active tracing configuration. This ensures that
only resources that comply with the latest governance policies are deployed into your AWS environments.
