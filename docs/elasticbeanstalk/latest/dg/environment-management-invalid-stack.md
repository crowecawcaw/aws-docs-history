# Recovering your Elastic Beanstalk environment from an invalid state

This topic provides some background information and resources that explain how to troubleshoot an Elastic Beanstalk environment in an invalid state.

## Addressing the error

Standard operations on an environment in an invalid state will not complete successfully. The failed operation will return an error that includes the
following text:

```
The stack ``stack_id`` associated with environment ``environment-ID`` is in ``stack-status`` state.
```

To troubleshoot and resolve this error, see the Knowledge Center article [Why is my Elastic Beanstalk environment in the invalid state?](https://repost.aws/knowledge-center/elastic-beanstalk-invalid-state "https://repost.aws/knowledge-center/elastic-beanstalk-invalid-state").

###### Note

Prior to [December 16, 2024](../relnotes/release-2024-12-16-release-notes.md "../relnotes/release-2024-12-16-release-notes.md"), the
failing operation returned the following error instead: `Environment is in an invalid state for this operation. Must be ready.` In this case
you had to contact AWS Support to reset the environment status after you completed the corrective actions.

Today you must still resolve the stack issues following the instructions in the referenced [Knowledge Center article](https://repost.aws/knowledge-center/elastic-beanstalk-invalid-state "https://repost.aws/knowledge-center/elastic-beanstalk-invalid-state"). However, once you successfully complete
the corrective actions, Elastic Beanstalk automatically updates the environment's status from invalid to available, and you can resume the standard operations on
your environment without further delay.

## Why the error occurs

When you deploy an application in Elastic Beanstalk, the service creates an underlying AWS CloudFormation stack. Elastic Beanstalk calls the CloudFormation service to launch the resources in
your environment and propagate configuration changes.

If Elastic Beanstalk performs an operation on an environment without having access to a required resource, the environment’s underlying CloudFormation stack can enter
a failed state. Other issues can also lead to this state, although permission issues are the primary cause. As a result of the stack’s failed state, CloudFormation
blocks Elastic Beanstalk operation requests from performing further stack updates, causing the failure of Elastic Beanstalk operations, such as UpdateEnvironment and
RetrieveEnvironmentInfo.

At this point you must first correct the root cause of the underlying issue to remedy the CloudFormation stack. The Elastic Beanstalk service then detects the
CloudFormation stack status change and follows through to reset your environment to an available status. At this point further operations can complete
successfully.

Permission issues typically cause this effect on the CloudFormation stack and the Elastic Beanstalk environment, although out-of-band changes can also cause
issues.

###### Important

To avoid disruption to your environment, we strongly recommend that you only initiate operations to manage and configure your environment from the
Elastic Beanstalk service. Modification of resources by using the console, CLI commands, or SDK of a service other than Elastic Beanstalk is an out-of-band change, which causes
_resource drift_. Resource drift affects the status of the CloudFormation stack, which in turn causes the Elastic Beanstalk environment to enter
into an invalid state.

For more information about resource drift, see [What is drift?](../../../AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.md#what-is-drift "../../../AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.md#what-is-drift") in the
_AWS CloudFormation User Guide_.
