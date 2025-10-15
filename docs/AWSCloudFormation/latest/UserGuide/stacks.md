# Managing AWS resources as a single unit with AWS CloudFormation stacks

A stack is a collection of AWS resources that you can manage as a single unit. In other
 words, you can create, update, and delete a collection of resources by creating, updating, and
 deleting stacks.

Creating a stack involves deploying a CloudFormation template
 that specifies the resources and their configurations, which CloudFormation then provisions and
 configures.

Updating a stack involves making changes to the template or
 parameters. CloudFormation compares the changes you submit with the current state of your stack and
 updates only the changed resources. CloudFormation might interrupt resources or replace updated
 resources, depending on which properties you update. For more information about resource update
 behaviors, see [Understand update behaviors of stack
 resources](using-cfn-updating-stacks-update-behaviors.md "using-cfn-updating-stacks-update-behaviors.md").

CloudFormation provides two methods for updating stacks: 


* Change sets – With change sets, you can preview
 the changes CloudFormation will make to your stack, and then decide whether to apply those
 changes. Change sets are JSON-formatted documents that summarize the changes CloudFormation will
 make to a stack. Use change sets when you want to make sure that CloudFormation doesn't make
 unintentional changes or when you want to consider several options. For example, you can use
 a change set to verify that CloudFormation won't replace your stack's database instances during
 an update.
* Direct update – When you directly update a stack,
 you submit changes and CloudFormation immediately deploys them. Use direct updates when you want
 to quickly deploy your updates.
Deleting a stack deletes the resources associated with it. A
 stack, for instance, can include all the resources required to run a web application, such as a
 web server, a database, and networking rules. If you no longer require that web application, you
 can simply delete the stack, and all of its related resources are deleted.

###### Note

You are charged for the stack resources for the time they were operating (even if you
 deleted the stack right away).

CloudFormation ensures all stack resources are created or deleted as appropriate. Because
 CloudFormation treats the stack resources as a single unit, they must all be created or deleted
 successfully for the stack to be created or deleted. If a resource can't be created, CloudFormation
 rolls the stack back and automatically deletes any resources that were created. If a resource
 can't be deleted, any remaining resources are retained until the stack can be successfully
 deleted.

###### Topics

* [Interfaces for managing your stacks](#interfaces-for-managing-stacks "#interfaces-for-managing-stacks")
* [Create a stack from the CloudFormation console](cfn-console-create-stack.md "cfn-console-create-stack.md")
* [View stack information from the
 CloudFormation console](cfn-console-view-stack-data-resources.md "cfn-console-view-stack-data-resources.md")
* [Update your stack template](using-cfn-updating-stacks-get-template.md "using-cfn-updating-stacks-get-template.md")
* [Understand update behaviors of stack
 resources](using-cfn-updating-stacks-update-behaviors.md "using-cfn-updating-stacks-update-behaviors.md")
* [Update CloudFormation stacks using change
 sets](using-cfn-updating-stacks-changesets.md "using-cfn-updating-stacks-changesets.md")
* [Update stacks directly](using-cfn-updating-stacks-direct.md "using-cfn-updating-stacks-direct.md")
* [Cancel a stack update](using-cfn-stack-update-cancel.md "using-cfn-stack-update-cancel.md")
* [Delete a stack from the CloudFormation console](cfn-console-delete-stack.md "cfn-console-delete-stack.md")
* [Monitor stack progress](monitor-stack-progress.md "monitor-stack-progress.md")
* [Roll back your CloudFormation stack on alarm
 breach with rollback triggers](using-cfn-rollback-triggers.md "using-cfn-rollback-triggers.md")
* [Detect unmanaged configuration changes to stacks and
 resources with drift detection](using-cfn-stack-drift.md "using-cfn-stack-drift.md")
* [Import AWS resources into a CloudFormation stack](import-resources.md "import-resources.md")
* [Stack refactoring](stack-refactoring.md "stack-refactoring.md")
* [Resource type
 support](resource-import-supported-resources.md "resource-import-supported-resources.md")
* [Use quick-create links to
 create CloudFormation stacks](cfn-console-create-stacks-quick-create-links.md "cfn-console-create-stacks-quick-create-links.md")
* [Examples of CloudFormation stack operation commands for
 the AWS CLI and PowerShell](service_code_examples.md "service_code_examples.md")

## Interfaces for managing your stacks


You can manage your CloudFormation stacks using the following interfaces:



* CloudFormation console – Provides a web interface
 that you can use to access your stacks. You can access the CloudFormation console by signing
 into the AWS Management Console, using the search box on the navigation bar to search for
 **CloudFormation**, and then choosing **CloudFormation** from
 the search results.
* AWS Command Line Interface – Provides commands for a broad set of
 AWS services, including CloudFormation, and is supported on Windows, Mac, and Linux. For
 information about the CloudFormation commands, see [cloudformation](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/ "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/") in the
 *AWS CLI Command Reference*.
* AWS Tools for PowerShell – A set of PowerShell modules that
 are built on the functionality exposed by the SDK for .NET. The Tools for PowerShell enable you to script
 operations on your AWS resources from the PowerShell command line. You can find the
 cmdlets for CloudFormation in the [AWS Tools for PowerShell Cmdlet Reference](https://docs.aws.amazon.com/powershell/latest/reference/Index.html "https://docs.aws.amazon.com/powershell/latest/reference/Index.html").
* Query API – Provides low-level API actions that
 you call using HTTPS requests. If you make API calls in your application, you must write
 the code to handle low-level details, such as generating the hash to sign the request. For
 more information about the API actions for CloudFormation, see [Actions](../APIReference/API_Operations.md "../APIReference/API_Operations.md") in the
 *AWS CloudFormation API Reference*.
* AWS SDKs – Provides language-specific APIs and
 takes care of many of the connection details, such as calculating signatures, handling
 request retries, and error handling. For more information, see [Tools to Build on
 AWS](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/").
* AWS Cloud Development Kit (AWS CDK) – The AWS CDK is an
 open-source software development framework that allows you to define AWS infrastructure
 using familiar programming languages like TypeScript, Python, Java, and .NET. With the
 CDK, you can model your application resources and then provision them using CloudFormation
 directly from your integrated development environment (IDE). For more information, see
 [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/").
