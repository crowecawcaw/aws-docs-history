# Accessing data

Using ADK APIs, you can access data that is set on the actions. Here is some of the
data you can access.

###### Topics

- [Environment variables](#env-variables "#env-variables")
- [Action inputs](#action-inputs "#action-inputs")
- [Secrets](#action-secrets "#action-secrets")
- [Application URLs](#action-urls "#action-urls")

## Environment variables

CodeCatalyst sets environment variables available at the action runtime. An action can be configured with input
variables and pre-defined variables that can be accessed by the action. The variables can be accessed for auditing
purposes, metrics, access tokens, and other information. The following ADK API can be used to get both input
variables and pre-defined variables: `code.getEnvironmentVariable('variableName');`. For more information, see
[ADK
Core's getEnvironmentVariable details](https://aws.github.io/actions-dev-kit/functions/_aws_codecatalyst_adk_core.getEnvironmentVariable.html "https://aws.github.io/actions-dev-kit/functions/_aws_codecatalyst_adk_core.getEnvironmentVariable.html").

```
Identifier: my_org/my_action
   Configuration:
      MyEnvironment: 'MY_PROJECT'
```

```
const projectName = core.getEnvironmentVariable('MyEnvironment')
```

## Action inputs

Action inputs are values passed into an action at runtime. These inputs are defined in the action definition file
(`action.yml`) and can be used to specify parameters. You can access and configure the action inputs
in order to customize the behavior of the action based on a specific use case. The following ADK API can be used
to get the action inputs: `core.getInput(`${inputName}`)`. For more information, see
[ADK
Core's getInput details](https://aws.github.io/actions-dev-kit/functions/_aws_codecatalyst_adk_core.getInput.html "https://aws.github.io/actions-dev-kit/functions/_aws_codecatalyst_adk_core.getInput.html").

```
Identifier: my_org/my_action
   Configuration:
      MyInput: 'MY_ACTION_INPUT'
```

```
const actionInput = core.getInput('MyInput')
```

## Secrets

Sensitive data like authentication credentials and other values can be stored and protected in secrets with CodeCatalyst.
You can then reference the secrets in your workflow definition file. For more information, see
[Working
with secrets](../userguide/workflows-secrets.md "../userguide/workflows-secrets.md").

In the following workflow, the value of the `core.getInput(`${StackName}`)` secret is assigned to the
`StackName` action input at runtime. For more information, see
[ADK
Core's getInput details](https://aws.github.io/actions-dev-kit/functions/_aws_codecatalyst_adk_core.getInput.html "https://aws.github.io/actions-dev-kit/functions/_aws_codecatalyst_adk_core.getInput.html").

```
Actions:
  ACTIONNAME:
    Identifier: aws/cdk-deploy@v2
    Environment:
      Name: codecatalyst-cdk-deploy-environment
      Connections:
        - Name: codecatalyst-account-connection
          Role: codecatalyst-cdk-deploy-role
    Inputs:
      Sources:
        - WorkflowSource
    Configuration:
      StackName: ${Secrets.MY_SECRET_STACK_NAME}
      Region: ${Secrets.MY_REGION}
```

```
const stackName = core.getInput('StackName')
```

```
const region = core.getInput('Region')
```

## Application URLs

Your workflow that deploys an application can display a URL in the workflow diagram. The clickable URL in the CodeCatalyst console can
help to quickly verify your application. For more information, see
[Surfacing
the URL of the deployed application](../userguide/deploy-consumption-surface-app-url.md "../userguide/deploy-consumption-surface-app-url.md").

You can also configure action source code with an output variable to get a URL link for your application. In the following code, the URL
is first defined so the variable holds the URL you want to set as the output value. The output variable is named `AppUrl` in
`code.setOutput('AppUrl, url);` with the value of the `url` variable. The output variable can then be accessed in a workflow.
For more information, see [Working with
variables](../userguide/workflows-working-with-variables.md "../userguide/workflows-working-with-variables.md").

```
const url = "https://mycompany.myapp.com";
```

```
core.setOutput('AppUrl', url);
```
