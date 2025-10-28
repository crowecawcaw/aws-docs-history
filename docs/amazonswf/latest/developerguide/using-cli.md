# Using the AWS CLI with Amazon Simple Workflow Service

Many of the features of Amazon Simple Workflow Service can be accessed from the AWS CLI. The AWS CLI provides an alternative to using
Amazon SWF with the AWS Management Console or in some cases, to programming with the Amazon SWF API and the AWS Flow Framework.

For example, you can use the AWS CLI to register a new workflow type:

```
aws swf register-workflow-type --domain `MyDomain` --name `"MySimpleWorkflow"` --workflow-version `"v1"`
```

You can also list your registered workflow types:

```
aws swf list-workflow-types --domain `MyDomain` --registration-status `REGISTERED`
```

The following shows an example of the default output in JSON:

```
{
    "typeInfos": [
        {
            "status": "REGISTERED",
            "creationDate": 1377471607.752,
            "workflowType": {
                "version": "v1",
                "name": "MySimpleWorkflow"
            }
        },
        {
            "status": "REGISTERED",
            "creationDate": 1371454149.598,
            "description": "MyDomain subscribe workflow",
            "workflowType": {
                "version": "v3",
                "name": "subscribe"
            }
        }
    ]
}
```

The Amazon SWF commands in AWS CLI provide the ability to start and manage workflow executions, poll for activity tasks,
record task heartbeats, and more! For a complete list of Amazon SWF commands, with descriptions of the available arguments
and examples showing their use, see [Amazon SWF](../../../cli/latest/reference/swf/index.md "../../../cli/latest/reference/swf/index.md") commands in the _AWS CLI Command Reference_.

The AWS CLI commands follow the Amazon SWF API closely, so you can use the AWS CLI to learn about the
underlying Amazon SWF API. You can also use your existing API knowledge to prototype code or perform Amazon SWF actions on the
command line.

To learn more about the AWS CLI, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").
