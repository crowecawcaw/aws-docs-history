Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Automating your management tasks with AWS OpsHub

You can use AWS OpsHub to automate operational tasks that you perform frequently on
your Snowball Edge. You can create a task for reoccurring actions that you might want to
perform on resources, such as restarting virtual servers, stopping Amazon EC2-compatible instances, and
so on. You provide an automation document that safely performs operational tasks and
runs the operation on AWS resources in bulk. You can also schedule common IT workflows.

###### Note

Automating tasks is not supported on clusters.

To use tasks, the Amazon EC2 Systems Manager service must be started first. For more information, see [Activating Snowball Edge Device Management on a Snowball Edge](aws-sdm.md#enable-sdm "aws-sdm.md#enable-sdm").

###### Topics

- [Creating and starting a task with AWS OpsHub](#create-task "#create-task")
- [Viewing details of a task in AWS OpsHub](#view-task "#view-task")
- [Deleting a task in AWS OpsHub](#delete-task "#delete-task")

## Creating and starting a task with AWS OpsHub

When you create a task, you specify the types of resources that the task
should run on, and then provide a task document that contains the instructions that
run the task. The task document is either in YAML or JSON format. You then provide
the required parameters for the task and start the task.

###### To create a task

1. In the **Launch tasks** section of the dashboard, choose **Get
   started** to open the **Tasks** page. If you
   have created tasks, they appear under **Tasks**.
2. Choose **Create task** and provide details for the task.
3. For **Name**, enter a unique name for the task.

###### Tip

The name must be between 3 and 128 characters. Valid characters are
`a-z`, `A-Z`, `0-9`,
`.`, `_`, and `-`. 4. Optionally, you can choose a target type from the **Target type-optional**
list. This is the type of resource that you want the task to run on.

For example, you can specify `/AWS::EC2::Instance`
for the tasks to run on an Amazon EC2-compatible instance or `/` to run
on all resource types. 5. In the **Content** section, choose **YAML** or
**JSON**, and provide the script that performs the
task. You have two options, YAML or JSON format. For examples, see [Task examples in AWS OpsHub](#task-examples "#task-examples"). 6. Choose **Create**. The task that you created then appears
on the **Tasks** page.

###### To start a task

1. In the **Launch tasks** section of the dashboard, choose **Get
   started** to open the **Tasks** page. Your
   tasks appear under **Tasks**.
2. Choose your task to open the **Start task** page.
3. Choose **Simple execution** to run on targets.

Choose **Rate control** to run safely on multiple targets
and define concurrency and error thresholds. For this option, you provide
the additional target and error threshold information in the **Rate
control** section. 4. Provide the required input parameters, and choose **Start task**.

The status of the task is **Pending**, and changes to
**Success** when the task has run successfully.

### Task examples in AWS OpsHub

The following example restarts an Amazon EC2-compatible instance. It requires two input
parameters: `endpoint` and `instance ID`.

_YAML example_

```

description: Restart EC2 instance
schemaVersion: '0.3'
parameters:
  Endpoint:
    type: String
    description: (Required) EC2 Service Endpoint URL
  Id:
    type: String
    description: (Required) Instance Id
mainSteps:
  - name: restartInstance
    action: aws:executeScript
    description: Restart EC2 instance step
    inputs:
      Runtime: python3.7
      Handler: restart_instance
      InputPayload:
        Endpoint: "{{ Endpoint }}"
        Id: "{{ Id }}"
      TimeoutSeconds: 30
      Script: |-
        import boto3
        import time
        def restart_instance(payload, context):
            ec2_endpoint = payload['Endpoint']
            instance_id = payload['Id']
            ec2 = boto3.resource('ec2', endpoint_url=ec2_endpoint)
            instance = ec2.Instance(instance_id)
            if instance.state['Name'] != 'stopped':
                instance.stop()
                instance.wait_until_stopped()
            instance.start()
            instance.wait_until_running()
            return {'InstanceState': instance.state}
```

_JSON example_

```
{
  "description" : "Restart EC2 instance",
  "schemaVersion" : "0.3",
  "parameters" : {
    "Endpoint" : {
      "type" : "String",
      "description" : "(Required) EC2 Service Endpoint URL"
    },
    "Id" : {
      "type" : "String",
      "description" : "(Required) Instance Id"
    }
  },
  "mainSteps" : [ {
    "name" : "restartInstance",
    "action" : "aws:executeScript",
    "description" : "Restart EC2 instance step",
    "inputs" : {
      "Runtime" : "python3.7",
      "Handler" : "restart_instance",
      "InputPayload" : {
        "Endpoint" : "{{ Endpoint }}",
        "Id" : "{{ Id }}"
      },
      "TimeoutSeconds" : 30,
      "Script" : "import boto3\nimport time\ndef restart_instance(payload, context):\n
            ec2_endpoint = payload['Endpoint']\n    instance_id = payload['Id']\n
            ec2 = boto3.resource('ec2', endpoint_url=ec2_endpoint)\n
            instance = ec2.Instance(instance_id)\n
            if instance.state['Name'] != 'stopped':\n
            instance.stop()\n
            instance.wait_until_stopped()\n
            instance.start()\n
            instance.wait_until_running()\n
            return {'InstanceState': instance.state}"
    }
  } ]
}
```

## Viewing details of a task in AWS OpsHub

You can view details of a management task, such as the description and the
parameters that are required to run the task.

###### To view details of a task

1. In the **Launch tasks** section of the dashboard, choose **Get
   started** to open the **Tasks** page.
2. On the **Tasks** page, locate and choose the task that you want to see
   details of.
3. Choose **View details**, and choose one of the tabs to see the details. For
   example, the **Parameters** tab shows you the input
   parameters in the script.

## Deleting a task in AWS OpsHub

Follow these steps to delete a management task.

###### To delete a task

1. In the **Launch tasks** section of the dashboard,
   choose **Get started** to open the
   **Tasks** page.
2. Locate the task that you want to delete. Choose the task, and then choose
   **Delete**.
