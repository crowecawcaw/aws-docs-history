# View CloudFormation stack events

You can view stack events to monitor the progress and status of your stack and
resources in the stack. Stack events help you understand when resources are being
created, updated, or deleted, and whether the stack deployment is proceeding as
expected.

###### Topics

- [View stack events (console)](#view-stack-events-console "#view-stack-events-console")
- [View stack events (AWS CLI)](#view-stack-events-cli "#view-stack-events-cli")
- [Stack status
  codes](#cfn-console-view-stack-data-resources-status-codes "#cfn-console-view-stack-data-resources-status-codes")

## View stack events (console)

###### To view stack events

1. Open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose the AWS Region
   you created the stack in.
3. On the **Stacks** page of the CloudFormation console, select
   the stack name. CloudFormation displays the stack details for the selected
   stack.
4. Choose the **Events** tab to view the stack events
   CloudFormation has generated for your stack.

CloudFormation automatically refreshes the stack events every minute. Additionally,
CloudFormation displays the **New events available** badge when new
stack events occur. Choose the refresh icon to load these events into the list. By
viewing stack creation events, you can understand the sequence of events that lead
to your stack's creation (or failure, if you are debugging your stack).

While your stack is being created, it's listed on the **Stacks**
page with a status of `CREATE_IN_PROGRESS`. After your stack has been
successfully created, its status changes to `CREATE_COMPLETE`.

For more information, see [Understand CloudFormation stack creation
events](stack-resource-configuration-complete.md "stack-resource-configuration-complete.md") and [Monitor the progress of a stack
update](using-cfn-updating-stacks-monitor-stack.md "using-cfn-updating-stacks-monitor-stack.md").

## View stack events (AWS CLI)

Alternatively, you can use the [describe-stack-events](../../../cli/latest/reference/cloudformation/describe-stack-events.md "../../../cli/latest/reference/cloudformation/describe-stack-events.md") command while the stack is being created to view
events as they're reported.

The following **describe-stack-events** command describes the
`my-stack` stack events.

```
aws cloudformation describe-stack-events --stack-name `my-stack`
```

The following is an example response.

```
{
    "StackEvents": [
        {
            "StackId": "arn:aws:cloudformation:`aws-region`:123456789012:stack/my-stack/64726230-7edf-11f0-8a36-06453a64f325",
            "EventId": "7b755820-7edf-11f0-ab15-0673b09f3847",
            "StackName": "my-stack",
            "LogicalResourceId": "my-stack",
            "PhysicalResourceId": "arn:aws:cloudformation:`aws-region`:123456789012:stack/my-stack/64726230-7edf-11f0-8a36-06453a64f325",
            "ResourceType": "AWS::CloudFormation::Stack",
            "Timestamp": "2025-08-21T22:37:56.243000+00:00",
            "ResourceStatus": "CREATE_COMPLETE",
            "ClientRequestToken": "`token`"
        },
        {
            "StackId": "arn:aws:cloudformation:`aws-region`:123456789012:stack/my-stack/64726230-7edf-11f0-8a36-06453a64f325",
            "EventId": "WebServer-CREATE_COMPLETE-2025-08-21T22:37:54.356Z",
            "StackName": "my-stack",
            "LogicalResourceId": "WebServer",
            "PhysicalResourceId": "i-099df76cb31b866a9",
            "ResourceType": "AWS::EC2::Instance",
            "Timestamp": "2025-08-21T22:37:54.356000+00:00",
            "ResourceStatus": "CREATE_COMPLETE",
            "ResourceProperties": "{\"UserData\":\"IyEvYmluL2Jhc2gKeXVtIGluc3RhbGwgLXkgYXdzLWNmbi1ib290c3RyYXAKL29wdC9hd3MvYmluL2Nmbi1pbml0IC12IC0tc3RhY2sgc2Rmc2RhZnNhZHNka2wgLS1yZXNvdXJjZSBXZWJTZXJ2ZXIgLS1yZWdpb24gdXMtd2VzdC0yCg==\",\"ImageId\":\"ami-0bbc328167dee8f3c\",\"InstanceType\":\"t2.micro\",\"SecurityGroupIds\":[\"my-stack-WebServerSecurityGroup-n8A43bQT1ty2\"],\"Tags\":[{\"Value\":\"Bootstrap Tutorial Web Server\",\"Key\":\"Name\"}]}",
            "ClientRequestToken": "`token`"
        },
        {
            "StackId": "arn:aws:cloudformation:`aws-region`:123456789012:stack/my-stack/64726230-7edf-11f0-8a36-06453a64f325",
            "EventId": "WebServer-CREATE_IN_PROGRESS-2025-08-21T22:37:31.226Z",
            "StackName": "my-stack",
            "LogicalResourceId": "WebServer",
            "PhysicalResourceId": "i-099df76cb31b866a9",
            "ResourceType": "AWS::EC2::Instance",
            "Timestamp": "2025-08-21T22:37:31.226000+00:00",
            "ResourceStatus": "CREATE_IN_PROGRESS",
            "ResourceStatusReason": "Resource creation Initiated",
            "ResourceProperties": "{\"UserData\":\"IyEvYmluL2Jhc2gKeXVtIGluc3RhbGwgLXkgYXdzLWNmbi1ib290c3RyYXAKL29wdC9hd3MvYmluL2Nmbi1pbml0IC12IC0tc3RhY2sgc2Rmc2RhZnNhZHNka2wgLS1yZXNvdXJjZSBXZWJTZXJ2ZXIgLS1yZWdpb24gdXMtd2VzdC0yCg==\",\"ImageId\":\"ami-0bbc328167dee8f3c\",\"InstanceType\":\"t2.micro\",\"SecurityGroupIds\":[\"my-stack-WebServerSecurityGroup-n8A43bQT1ty2\"],\"Tags\":[{\"Value\":\"Bootstrap Tutorial Web Server\",\"Key\":\"Name\"}]}",
            "ClientRequestToken": "`token`"
        },
        {
            "StackId": "arn:aws:cloudformation:`aws-region`:123456789012:stack/my-stack/64726230-7edf-11f0-8a36-06453a64f325",
            "EventId": "WebServer-CREATE_IN_PROGRESS-2025-08-21T22:37:29.210Z",
            "StackName": "my-stack",
            "LogicalResourceId": "WebServer",
            "PhysicalResourceId": "",
            "ResourceType": "AWS::EC2::Instance",
            "Timestamp": "2025-08-21T22:37:29.210000+00:00",
            "ResourceStatus": "CREATE_IN_PROGRESS",
            "ResourceProperties": "{\"UserData\":\"IyEvYmluL2Jhc2gKeXVtIGluc3RhbGwgLXkgYXdzLWNmbi1ib290c3RyYXAKL29wdC9hd3MvYmluL2Nmbi1pbml0IC12IC0tc3RhY2sgc2Rmc2RhZnNhZHNka2wgLS1yZXNvdXJjZSBXZWJTZXJ2ZXIgLS1yZWdpb24gdXMtd2VzdC0yCg==\",\"ImageId\":\"ami-0bbc328167dee8f3c\",\"InstanceType\":\"t2.micro\",\"SecurityGroupIds\":[\"my-stack-WebServerSecurityGroup-n8A43bQT1ty2\"],\"Tags\":[{\"Value\":\"Bootstrap Tutorial Web Server\",\"Key\":\"Name\"}]}",
            "ClientRequestToken": "`token`"
        },
        {
            "StackId": "arn:aws:cloudformation:`aws-region`:123456789012:stack/my-stack/64726230-7edf-11f0-8a36-06453a64f325",
            "EventId": "WebServerSecurityGroup-CREATE_COMPLETE-2025-08-21T22:37:28.803Z",
            "StackName": "my-stack",
            "LogicalResourceId": "WebServerSecurityGroup",
            "PhysicalResourceId": "my-stack-WebServerSecurityGroup-n8A43bQT1ty2",
            "ResourceType": "AWS::EC2::SecurityGroup",
            "Timestamp": "2025-08-21T22:37:28.803000+00:00",
            "ResourceStatus": "CREATE_COMPLETE",
            "ResourceProperties": "{\"GroupDescription\":\"Allow HTTP access from my IP address\",\"SecurityGroupIngress\":[{\"CidrIp\":\"0.0.0.0/0\",\"Description\":\"HTTP\",\"FromPort\":\"80\",\"ToPort\":\"80\",\"IpProtocol\":\"tcp\"}]}",
            "ClientRequestToken": "`token`"
        },
        {
            "StackId": "arn:aws:cloudformation:`aws-region`:123456789012:stack/my-stack/64726230-7edf-11f0-8a36-06453a64f325",
            "EventId": "WebServerSecurityGroup-CREATE_IN_PROGRESS-2025-08-21T22:37:22.626Z",
            "StackName": "my-stack",
            "LogicalResourceId": "WebServerSecurityGroup",
            "PhysicalResourceId": "my-stack-WebServerSecurityGroup-n8A43bQT1ty2",
            "ResourceType": "AWS::EC2::SecurityGroup",
            "Timestamp": "2025-08-21T22:37:22.626000+00:00",
            "ResourceStatus": "CREATE_IN_PROGRESS",
            "ResourceStatusReason": "Resource creation Initiated",
            "ResourceProperties": "{\"GroupDescription\":\"Allow HTTP access from my IP address\",\"SecurityGroupIngress\":[{\"CidrIp\":\"0.0.0.0/0\",\"Description\":\"HTTP\",\"FromPort\":\"80\",\"ToPort\":\"80\",\"IpProtocol\":\"tcp\"}]}",
            "ClientRequestToken": "`token`"
        },
        {
            "StackId": "arn:aws:cloudformation:`aws-region`:123456789012:stack/my-stack/64726230-7edf-11f0-8a36-06453a64f325",
            "EventId": "WebServerSecurityGroup-CREATE_IN_PROGRESS-2025-08-21T22:37:20.186Z",
            "StackName": "my-stack",
            "LogicalResourceId": "WebServerSecurityGroup",
            "PhysicalResourceId": "",
            "ResourceType": "AWS::EC2::SecurityGroup",
            "Timestamp": "2025-08-21T22:37:20.186000+00:00",
            "ResourceStatus": "CREATE_IN_PROGRESS",
            "ResourceProperties": "{\"GroupDescription\":\"Allow HTTP access from my IP address\",\"SecurityGroupIngress\":[{\"CidrIp\":\"0.0.0.0/0\",\"Description\":\"HTTP\",\"FromPort\":\"80\",\"ToPort\":\"80\",\"IpProtocol\":\"tcp\"}]}",
            "ClientRequestToken": "`token`"
        },
        {
            "StackId": "arn:aws:cloudformation:`aws-region`:123456789012:stack/my-stack/64726230-7edf-11f0-8a36-06453a64f325",
            "EventId": "64740fe0-7edf-11f0-8a36-06453a64f325",
            "StackName": "my-stack",
            "LogicalResourceId": "my-stack",
            "PhysicalResourceId": "arn:aws:cloudformation:`aws-region`:123456789012:stack/my-stack/64726230-7edf-11f0-8a36-06453a64f325",
            "ResourceType": "AWS::CloudFormation::Stack",
            "Timestamp": "2025-08-21T22:37:17.819000+00:00",
            "ResourceStatus": "CREATE_IN_PROGRESS",
            "ResourceStatusReason": "User Initiated",
            "ClientRequestToken": "`token`"
        }
    ]
}
```

The most recent events are reported first. The following table describe the fields
returned by the **describe-stack-events** command:

| Field                  | Description                                                                                                                                                                                     |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------------------ | ----------------- | --------------- | ------------------------ | -------------------- | ----------------- | ------------------------ | ------------------------------ | ---------------------------- | --------------------------------- | ------------------------ | ----------------------- | --------------------- | -------------------------- | --------------------- | ----------------------------------------- | ------------------- | ------------------------ | -------------------------- | -------------------------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `EventId`              | Event identifier.                                                                                                                                                                               |
| `StackName`            | Name of the stack that the event corresponds to.                                                                                                                                                |
| `StackId`              | Identifier of the stack that the event corresponds to.                                                                                                                                          |
| `LogicalResourceId`    | Logical identifier of the resource.                                                                                                                                                             |
| `PhysicalResourceId`   | Physical identifier of the resource.                                                                                                                                                            |
| `ResourceProperties`   | Properties of the resource.                                                                                                                                                                     |
| `ResourceType`         | Type of the resource.                                                                                                                                                                           |
| `Timestamp`            | Time when the event occurred.                                                                                                                                                                   |
| `ResourceStatus`       | The status of the resource, which can be one of the following<br>status codes: `CREATE_COMPLETE`                                                                                                | <br>`CREATE_FAILED` | `CREATE_IN_PROGRESS`<br> | `DELETE_COMPLETE` | `DELETE_FAILED` | <br>`DELETE_IN_PROGRESS` | <br>`DELETE_SKIPPED` | `IMPORT_COMPLETE` | <br>`IMPORT_IN_PROGRESS` | <br>`IMPORT_ROLLBACK_COMPLETE` | <br>`IMPORT_ROLLBACK_FAILED` | <br>`IMPORT_ROLLBACK_IN_PROGRESS` | <br>`REVIEW_IN_PROGRESS` | <br>`ROLLBACK_COMPLETE` | <br>`ROLLBACK_FAILED` | <br>`ROLLBACK_IN_PROGRESS` | <br>`UPDATE_COMPLETE` | <br>`UPDATE_COMPLETE_CLEANUP_IN_PROGRESS` | <br>`UPDATE_FAILED` | `UPDATE_IN_PROGRESS`<br> | `UPDATE_ROLLBACK_COMPLETE` | <br>`UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS` | <br>`UPDATE_ROLLBACK_FAILED` | <br>`UPDATE_ROLLBACK_IN_PROGRESS`<br>The `DELETE_SKIPPED` status applies to resources<br>with a deletion policy attribute of retain. |
| `DetailedStatus`       | The detailed status of the stack. If<br>`CONFIGURATION_COMPLETE` is present, the stack<br>resources configuration phase has completed and the<br>stabilization of the resources is in progress. |
| `ResourceStatusReason` | More information on the status.                                                                                                                                                                 |

## Stack status

codes

The following table describes stack status codes:

| Stack status and optional detailed status      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `CREATE_COMPLETE`                              | Successful creation of one or more stacks.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `CREATE_IN_PROGRESS`                           | Ongoing creation of one or more stacks.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `CREATE_FAILED`                                | Unsuccessful creation of one or more stacks. View the stack events to see any associated error messages.<br>Possible reasons for a failed creation include insufficient permissions to work with all resources in the stack,<br>parameter values rejected by an AWS service, or a timeout during resource creation.                                                                                                                                                                              |
| `DELETE_COMPLETE`                              | Successful deletion of one or more stacks. Deleted stacks are retained and viewable for 90 days.                                                                                                                                                                                                                                                                                                                                                                                                 |
| `DELETE_FAILED`                                | Unsuccessful deletion of one or more stacks. Because the delete failed, you might have some resources that<br>are still running; however, you can't work with or update the stack. Delete the stack again or view the stack<br>events to see any associated error messages.                                                                                                                                                                                                                      |
| `DELETE_IN_PROGRESS`                           | Ongoing removal of one or more stacks.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `REVIEW_IN_PROGRESS`                           | Ongoing creation of one or more stacks with an expected `StackId` but without any templates or resources.ImportantA stack with this status code counts against the [maximum possible<br>number of stacks](cloudformation-limits.md "cloudformation-limits.md").                                                                                                                                                                                                                                  |
| `ROLLBACK_COMPLETE`                            | Successful removal of one or more stacks after a failed stack creation or after an explicitly canceled stack<br>creation. The stack returns to the previous working state. Any resources that were created during the create stack<br>operation are deleted.<br>This status exists only after a failed stack creation. It signifies that all operations from the partially<br>created stack have been appropriately cleaned up. When in this state, only a delete operation can be<br>performed. |
| `ROLLBACK_FAILED`                              | Unsuccessful removal of one or more stacks after a failed stack creation or after an explicitly canceled<br>stack creation. Delete the stack or view the stack events to see any associated error messages.                                                                                                                                                                                                                                                                                      |
| `ROLLBACK_IN_PROGRESS`                         | Ongoing removal of one or more stacks after a failed stack creation or after an explicitly canceled stack<br>creation.                                                                                                                                                                                                                                                                                                                                                                           |
| `UPDATE_COMPLETE`                              | Successful update of one or more stacks.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `UPDATE_COMPLETE_CLEANUP_IN_PROGRESS`          | Ongoing removal of old resources for one or more stacks after a successful stack update. For stack updates<br>that require resources to be replaced, CloudFormation creates the new resources first and then deletes the old<br>resources to help reduce any interruptions with your stack. In this state, the stack has been updated and is<br>usable, but CloudFormation is still deleting the old resources.                                                                                  |
| `UPDATE_FAILED`                                | Unsuccessful update of one or more stacks. View the stack events to see any associated error<br>messages.                                                                                                                                                                                                                                                                                                                                                                                        |
| `UPDATE_IN_PROGRESS`                           | Ongoing update of one or more stacks.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `UPDATE_ROLLBACK_COMPLETE`                     | Successful return of one or more stacks to a previous working state after a failed stack update.                                                                                                                                                                                                                                                                                                                                                                                                 |
| `UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS` | Ongoing removal of new resources for one or more stacks after a failed stack update. In this state, the stack<br>has been rolled back to its previous working state and is usable, but CloudFormation is still deleting any new<br>resources it created during the stack update.                                                                                                                                                                                                                 |
| `UPDATE_ROLLBACK_FAILED`                       | Unsuccessful return of one or more stacks to a previous working state after a failed stack update. When in<br>this state, you can delete the stack or [continue<br>rollback](using-cfn-updating-stacks-continueupdaterollback.md "using-cfn-updating-stacks-continueupdaterollback.md"). You might need to fix errors before your stack can return to a working state. Or, you can<br>contact Support to restore the stack to a usable state.                                                    |
| `UPDATE_ROLLBACK_IN_PROGRESS`                  | Ongoing return of one or more stacks to the previous working state after failed stack update.                                                                                                                                                                                                                                                                                                                                                                                                    |
| `IMPORT_IN_PROGRESS`                           | The import operation is currently in progress.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `IMPORT_COMPLETE`                              | The import operation successfully completed for all resources in the stack that support `resource<br>import`.                                                                                                                                                                                                                                                                                                                                                                                    |
| `IMPORT_ROLLBACK_IN_PROGRESS`                  | Import will roll back to the previous template configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `IMPORT_ROLLBACK_FAILED`                       | The import rollback operation failed for at least one resource in the stack. Results will be available for<br>the resources CloudFormation successfully imported.                                                                                                                                                                                                                                                                                                                                |
| `IMPORT_ROLLBACK_COMPLETE`                     | Import successfully rolled back to the previous template configuration.                                                                                                                                                                                                                                                                                                                                                                                                                          |
