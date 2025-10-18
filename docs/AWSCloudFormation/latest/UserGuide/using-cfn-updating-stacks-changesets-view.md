# View a change set for a CloudFormation stack

After you create a change set, you can view the proposed changes before executing them.
 You can use the CloudFormation console, AWS CLI, or CloudFormation API to view change sets. The
 CloudFormation console provides a summary of the changes and a detailed list of changes in JSON
 format. The AWS CLI and AWS CloudFormation API return a detailed list of changes in JSON format.


View a change set (console)
###### To view a change set

1. Open the AWS CloudFormation console at
 [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose your AWS Region.
3. On the **Stacks** page, choose the name of the stack that
 contains the change set that you want to view.
4. In the navigation pane, choose **Change Sets** to view a list
 of the stack's change sets.
5. Choose the name of the change set that you want to view.


The CloudFormation console directs you to the change set's details page, where you
 can see the time the change set was created, its status, the input used to generate
 the change set, and a summary of the changes.


In the **Changes** section, each row represents a resource that
 CloudFormation will add, modify, or remove.




	* **Add** – CloudFormation creates a resource
	 when you add a resource to the stack's template.
	* **Modify** – CloudFormation modifies a
	 resource when you change the properties of a resource in the stack's
	 template.
	* **Remove** – CloudFormation deletes a
	 resource when you delete a resource from the stack's template.
###### Note

A modification can cause the resource to be interrupted or replaced
 (recreated). For more information about resource update behaviors, see [Understand update behaviors of stack
 resources](using-cfn-updating-stacks-update-behaviors.md "using-cfn-updating-stacks-update-behaviors.md").


To focus on specific changes, use the filter view. For example, filter for a
 specific resource type, such as `AWS::EC2::Instance`. To filter for a
 specific resource, specify its logical or physical ID, such as
 `myWebServer` or `i-123abcd4`.
6. In the **Changes** section, choose **View
 details** in the **Property-level changes** column to
 view property value changes made to your resource.
7. The CloudFormation console directs you to the property-level changes page for a
 resource, where you can see the template configuration of the resource before
 executing a change set and what the template configuration will look like after
 executing the change set.


The **Property-level changes** section table shows the
 **Path**, **Change type**, **Before
 value**, and **After value** for impacted properties. In
 the table, choose the checkbox for each change you want to highlight in the
 **Before** and **After** views of your template
 to see what changes will be made at the property-level.




	* **Add** – Added properties are
	 highlighted green.
	* **Modify** – Modified properties are
	 highlighted blue.
	* **Remove** – Removed properties are
	 highlighted red.


View a change set for nested stack (console)
###### To view a change set for nested stacks (console)

1. Open the AWS CloudFormation console at
 [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose your AWS Region.
3. On the **Stacks** page, choose the name of the stack that
 contains the change set that you want to view.
4. In the navigation pane, choose **Change sets** to view a list
 of the stack's change sets.
5. Choose the name of the change set that you want to view.


The CloudFormation console directs you to the change set's details page, where you
 can see the time the change set was created, its status, the input used to generate
 the change set, and a summary of the changes.


In the **Changes** section, each row represents a resource that
 CloudFormation will add, modify, remove, or show the status of dynamic.




	* **Add** – CloudFormation creates a resource
	 when you add a resource to the stack's template.
	* **Modify** – CloudFormation modifies a
	 resource when you change the properties of a resource in the stack's
	 template.
	* **Remove** – CloudFormation deletes a
	 resource when you delete a resource from the stack's template.
	* **Dynamic** – CloudFormation can't determine
	 the exact resource change action from the nested stack's template.
###### Note

A modification can cause the resource to be interrupted or replaced
 (recreated). For more information about resource update behaviors, see [Understand update behaviors of stack
 resources](using-cfn-updating-stacks-update-behaviors.md "using-cfn-updating-stacks-update-behaviors.md").


To focus on specific changes, use the filter view. For example, filter for a
 specific resource type, such as `AWS::CloudFormation::Stack`.
 To filter for a specific resource, specify its logical or physical ID, such as
 `DeadLetterQueue` or
 `NestedStack`.
6. In the **Changes** section, choose **View nested change
 set** of the nested change set you want to view.


The CloudFormation console directs you to the nested change set's details page. You
 can choose **Go to root change set** to view the root change set
 or, you can choose **View parent change set** to view the parent
 change set. For more information see, [Change sets for nested stacks](change-sets-for-nested-stacks.md "change-sets-for-nested-stacks.md").


###### Note

CloudFormation property-level change sets does not resolve cross-stack references 
 when you create change sets for nested stacks. Change sets can mark resources in 
 a child stack for conditional replacement if they reference the output of a parent 
 stack, and the parent stack has been modified


###### To view a change set (AWS CLI)

1. To get the ID of the change set, run the [change-sets](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-change-sets.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-change-sets.html") command.


Specify the name of the stack that has the change set that you want to view, as
 shown in the following example:



```
aws cloudformation list-change-sets --stack-name `MyStack`
```

CloudFormation returns a list of change sets, similar to the following:



```
{
    "Summaries": [
        {
            "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/MyStack/1a2345b6-0000-00a0-a123-00abc0abc000",
            "Status": "CREATE_COMPLETE",
            "ChangeSetName": "SampleChangeSet",
            "CreationTime": "2020-11-18T20:44:05.889Z",
            "StackName": "MyStack",
            "ChangeSetId": "arn:aws:cloudformation:us-east-1:123456789012:changeSet/SampleChangeSet/1a2345b6-0000-00a0-a123-00abc0abc000"
        },
        {
            "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/MyStack/1a2345b6-0000-00a0-a123-00abc0abc000",
            "Status": "CREATE_COMPLETE",
            "ChangeSetName": "SampleChangeSet-conditional",
            "CreationTime": "2020-11-18T21:15:56.398Z",
            "StackName": "MyStack",
            "ChangeSetId": "arn:aws:cloudformation:us-east-1:123456789012:changeSet/SampleChangeSet-conditional/1a2345b6-0000-00a0-a123-00abc0abc000"
        },
        {
            "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/MyStack/1a2345b6-0000-00a0-a123-00abc0abc000",
            "Status": "CREATE_COMPLETE",
            "ChangeSetName": "SampleChangeSet-replacement",
            "CreationTime": "2020-11-18T21:03:37.706Z",
            "StackName": "MyStack",
            "ChangeSetId": "arn:aws:cloudformation:us-east-1:123456789012:changeSet/SampleChangeSet-replacement/1a2345b6-0000-00a0-a123-00abc0abc000"
        }
    ]
}
```
2. Run the [describe-change-set](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-change-set.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-change-set.html") command, specifying the ID of the change
 set that you want to view. For example:



```
aws cloudformation describe-change-set \
  --change-set-name `arn:aws:cloudformation:us-east-1:123456789012:changeSet/SampleChangeSet/1a2345b6-0000-00a0-a123-00abc0abc000`
```

CloudFormation returns information about the specified change set.



```
{
    "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/MyStack/1a2345b6-0000-00a0-a123-00abc0abc000",
    "Status": "CREATE_COMPLETE",
    "ChangeSetName": "SampleChangeSet-direct",
    "Parameters": [
        {
            "ParameterValue": "testing",
            "ParameterKey": "Purpose"
        },
        {
            "ParameterValue": "ellioty-useast1",
            "ParameterKey": "KeyPairName"
        },
        {
            "ParameterValue": "t2.micro",
            "ParameterKey": "InstanceType"
        }
    ],
    "Changes": [
        {
            "ResourceChange": {
                "ResourceType": "AWS::EC2::Instance",
                "PhysicalResourceId": "i-1abc23d4",
                "Details": [
                    {
                        "ChangeSource": "DirectModification",
                        "Evaluation": "Static",
                        "Target": {
                            "Attribute": "Tags",
                            "RequiresRecreation": "Never"
                        }
                    }
                ],
                "Action": "Modify",
                "Scope": [
                    "Tags"
                ],
                "LogicalResourceId": "MyEC2Instance",
                "Replacement": "False"
            },
            "Type": "Resource"
        }
    ],
    "CreationTime": "2020-11-18T23:35:25.813Z",
    "Capabilities": [],
    "StackName": "MyStack",
    "NotificationARNs": [],
    "ChangeSetId": "arn:aws:cloudformation:us-east-1:123456789012:changeSet/SampleChangeSet-direct/9edde307-960d-4e6e-ad66-b09ea2f20255"
}
```

Use `--include-property-values` with **describe-change-set**
 to list the property-level changes.


The `Changes` key lists changes to resources. If you were to execute this
 change set, CloudFormation would update the tags of the `i-1abc23d4` EC2 instance.
 For a description of each field, see the [`Change`](../APIReference/API_Change.md "../APIReference/API_Change.md") data type in the
 *AWS CloudFormation API Reference*.


For additional examples of change sets, see [Example change sets for CloudFormation stacks](using-cfn-updating-stacks-changesets-samples.md "using-cfn-updating-stacks-changesets-samples.md").
###### To view property-level changes in a change set
 (AWS CLI)

* The following command lists the property-level changes related to a change set for a
 `AWS::EC2::NetworkInterface` resource that will remove the
 `Ipv4Prefixes` property, modifies the `Description` for the
 resource, and adds a `Tag`:



```
aws cloudformation describe-change-set --include-property-values \
  --change-set-name `arn:aws:cloudformation:us-east-1:123456789012:changeSet/ExampleChangeSet/9f7b541b-126b-44f7-998e-932174557841`
```

The following is example output.



```
"ChangeSetName": "ExampleChangeSet",
    "ChangeSetId": "arn:aws:cloudformation:us-east-1:803642222207:changeSet/ExampleChangeSet/9f7b541b-126b-44f7-998e-932174557841",
    "StackId": "arn:aws:cloudformation:us-east-1:803642222207:stack/ExampleStack/ab664180-f686-11ee-9e29-12cd92393671",
    "StackName": "ExampleStack",
    "Description": null,
    "Parameters": null,
    "CreationTime": "2024-04-09T18:04:59.935000+00:00",
    "ExecutionStatus": "AVAILABLE",
    "Status": "CREATE_COMPLETE",
    "StatusReason": null,
    "NotificationARNs": [],
    "RollbackConfiguration": {
        "RollbackTriggers": []
    },
    "Capabilities": [],
    "Tags": null,
    "ParentChangeSetId": null,
    "IncludeNestedStacks": true,
    "RootChangeSetId": null,
    "OnStackFailure": null,
 {
    "Changes": [
        {
            "Type": "Resource",
            "ResourceChange": {
                "Action": "Modify",
                "LogicalResourceId": "EC2NetworkInterface00eni067fd35b649a05b7100Tpyls",
                "PhysicalResourceId": "eni-067fd35b649a05b71",
                "ResourceType": "AWS::EC2::NetworkInterface",
                "Replacement": "False",
                "Scope": [
                    "Properties",
                    "Tags"
                ],
                "Details": [
                    {
                        "Target": {
                            "Attribute": "Properties",
                            "Name": "Ipv4Prefixes",
                            "RequiresRecreation": "Never",
                            "Path": "/Properties/Ipv4Prefixes",
                            "BeforeValue": "[]",
                            "AttributeChangeType": "Remove"
                        },
                        "Evaluation": "Static",
                        "ChangeSource": "DirectModification"
                    },
                    {
                        "Target": {
                            "Attribute": "Properties",
                            "Name": "Description",
                            "RequiresRecreation": "Never",
                            "Path": "/Properties/Description",
                            "BeforeValue": "",
                            "AfterValue": "Description",
                            "AttributeChangeType": "Modify"
                        },
                        "Evaluation": "Static",
                        "ChangeSource": "DirectModification"
                    },
                    {
                        "Target": {
                            "Attribute": "Tags",
                            "RequiresRecreation": "Never",
                            "Path": "/Properties/Tags/0",
                            "AfterValue": "{\"Key\":\"Test\",\"Value\":\"Test\"}",
                            "AttributeChangeType": "Add"
                        },
                        "Evaluation": "Static",
                        "ChangeSource": "DirectModification"
                    }
                ],
                "BeforeContext": "{\"Properties\":{\"Description\":\"\",\"PrivateIpAddress\":\"172.31.76.2\",\"PrivateIpAddresses\":[{\"PrivateIpAddress\":\"172.31.76.2\",\"Primary\":\"true\"}],\"SecondaryPrivateIpAddressCount\":\"0\",\"Ipv6PrefixCount\":\"0\",\"Ipv4Prefixes\":[],\"Ipv4PrefixCount\":\"0\",\"GroupSet\":[\"sg-05a45689b1059e82d\"],\"Ipv6Prefixes\":[],\"SubnetId\":\"subnet-455e8969\",\"SourceDestCheck\":\"true\",\"InterfaceType\":\"interface\",\"Tags\":[]},\"UpdateReplacePolicy\":\"Retain\",\"DeletionPolicy\":\"Retain\"}",
                "AfterContext": "{\"Properties\":{\"Description\":\"Description\",\"PrivateIpAddress\":\"172.31.76.2\",\"PrivateIpAddresses\":[{\"PrivateIpAddress\":\"172.31.76.2\",\"Primary\":\"true\"}],\"SecondaryPrivateIpAddressCount\":\"0\",\"Ipv6PrefixCount\":\"0\",\"Ipv4PrefixCount\":\"0\",\"GroupSet\":[\"sg-05a45689b1059e82d\"],\"Ipv6Prefixes\":[],\"SubnetId\":\"subnet-455e8969\",\"SourceDestCheck\":\"true\",\"InterfaceType\":\"interface\",\"Tags\":[{\"Value\":\"Test\",\"Key\":\"Test\"}]},\"UpdateReplacePolicy\":\"Retain\",\"DeletionPolicy\":\"Retain\"}"
            }
        }
    ],
    "ChangeSetName": "ExampleChangeSet",
    "ChangeSetId": "arn:aws:cloudformation:us-east-1:123456789012:changeSet/ExampleChangeSet/9f7b541b-126b-44f7-998e-932174557841",
    "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/ExampleStack/ab664180-f686-11ee-9e29-12cd92393671",
```
