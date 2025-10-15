# Monitor the progress of a stack
 update

You can monitor the progress of a stack update by viewing the stack's events. The stack's
 **Events** tab displays each major step in the creation and update of the
 stack sorted by the time of each event with latest events on top. For more information, see
 [Monitor stack progress](monitor-stack-progress.md "monitor-stack-progress.md").

###### Topics

* [Events generated
 during a successful stack update](#using-cfn-updating-stacks-monitor-stack-update-events "#using-cfn-updating-stacks-monitor-stack-update-events")
* [Events generated
 when a resource update fails](#using-cfn-updating-stacks-monitor-stack-update-failure "#using-cfn-updating-stacks-monitor-stack-update-failure")

## Events generated
 during a successful stack update


The start of the stack update process is marked with an `UPDATE_IN_PROGRESS` event for the
 stack:



```

2011-09-30 09:35 PDT AWS::CloudFormation::Stack `MyStack` UPDATE_IN_PROGRESS 
```

Next are events that mark the beginning and completion of the update of each resource
 that was changed in the update template. For example, updating an [AWS::RDS::DBInstance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html") resource named `MyDB` would result in the following
 entries:



```

2011-09-30 09:35 PDT AWS::RDS::DBInstance MyDB UPDATE_COMPLETE
2011-09-30 09:35 PDT AWS::RDS::DBInstance MyDB UPDATE_IN_PROGRESS 
```

The `UPDATE_IN_PROGRESS` event is logged when CloudFormation reports that it has begun to
 update the resource. The `UPDATE_COMPLETE` event is logged when the resource is successfully
 created.


When CloudFormation has successfully updated the stack, you will see the following
 event:



```

2011-09-30 09:35 PDT AWS::CloudFormation::Stack `MyStack` UPDATE_COMPLETE 
```

###### Important

During stack update operations, if CloudFormation needs to replace an existing resource,
 it first creates a new resource and then deletes the old resource. However, there may be
 cases where CloudFormation can't delete the old resource (for example, if the user doesn't
 have permissions to delete a resource of a given type).

CloudFormation makes three attempts at deleting the old resource. If CloudFormation can't
 delete the old resource, it removes the old resource from the stack and continues
 updating the stack. When the stack update is complete, CloudFormation issues an
 `UPDATE_COMPLETE` stack event, but includes a `StatusReason`
 that states that one or more resources couldn't be deleted. CloudFormation also issues a
 `DELETE_FAILED` event for the specific resource, with a corresponding
 `StatusReason` providing more detail on why CloudFormation failed to delete
 the resource.

The old resource still exists and will continue to incur charges, but is no longer
 accessible through CloudFormation. To delete the old resource, access the old resource
 directly using the console or API for the underlying service.

This is also true for resources that you have removed from the stack template, and so
 will be deleted from the stack during the stack update.


## Events generated
 when a resource update fails


If an update of a resource fails, CloudFormation reports an `UPDATE_FAILED` event
 that includes a reason for the failure. For example, if your update template specified a
 property change that's not supported by the resource such as reducing the size of
 `AllocatedStorage` for an [AWS::RDS::DBInstance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html") resource, you would see events like these:



```

2011-09-30 09:36 PDT AWS::RDS::DBInstance MyDB UPDATE_FAILED Size cannot be less than current size; requested: 5; current: 10
2011-09-30 09:35 PDT AWS::RDS::DBInstance MyDB UPDATE_IN_PROGRESS 
```

If a resource update fails, CloudFormation rolls back any resources that it has updated
 during the upgrade to their configurations before the update. Here is an example of the
 events you would see during an update rollback:



```

2011-09-30 09:38 PDT AWS::CloudFormation::Stack `MyStack` UPDATE_ROLLBACK_COMPLETE
2011-09-30 09:38 PDT AWS::RDS::DBInstance MyDB UPDATE_COMPLETE
2011-09-30 09:37 PDT AWS::RDS::DBInstance MyDB UPDATE_IN_PROGRESS
2011-09-30 09:37 PDT AWS::CloudFormation::Stack `MyStack` UPDATE_ROLLBACK_IN_PROGRESS The following resource(s) failed to update: [MyDB] 
```
