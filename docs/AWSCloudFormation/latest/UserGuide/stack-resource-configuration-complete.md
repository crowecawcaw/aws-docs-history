# Understand CloudFormation stack creation
 events

During stack deployment, several events occur to create, configure, and validate the
 resources defined in the stack template. Understanding these events can help you optimize your
 stack creation process and streamline deployments.


* Resource creation events – When each resource
 starts the creation process, a **Status** of
 `CREATE_IN_PROGRESS` event is set. This event indicates that the resource is
 being provisioned.
* Eventual consistency check – A significant portion
 of the stack creation time is spent performing an eventual consistency check against the
 resources created by the stack. During this phase, the service performs internal consistency
 checks, ensuring the resource is fully operational and meets service stabilization criteria
 defined by each AWS service.
* Configuration complete event – When each resource
 has finished the eventual consistency check phase of the provisioning, a  **Detailed
 status** of `CONFIGURATION_COMPLETE` event is set.
* Resource creation complete event – After the
 resource has been created and configured as specified, and the configuration matches what is
 specified in the template, the **Status** of `CREATE_COMPLETE`
 event is set.
You can leverage the `CONFIGURATION_COMPLETE` event to streamline your stack
 creation process in scenarios where resource eventual consistency check is not required, such as
 validating a pre-production stack configuration or cross-stack provisioning. You can use this
 event in multiple ways. For example, you can use it as a visual signal to skip waiting for the
 resource or stack consistency check to finish. Or you could use it to create an automated
 mechanism using continuous integration and continuous delivery (CI/CD) to trigger additional
 actions.

###### Important

While leveraging the `CONFIGURATION_COMPLETE` event accelerates stack creation
 times, you should be aware of its trade-offs. First, it's only supported for a subset of
 resource type that support drift detection. For a list of resource types that support drift
 detection, see [Resource type
 support](resource-import-supported-resources.md "resource-import-supported-resources.md"). This approach may not be suitable for all
 scenarios, especially where resources require thorough eventual consistency checks to ensure
 full operational readiness across the cloud environment (for example, in production
 environments). We recommend carefully assessing your deployment requirements and the
 criticality of the consistency checks for each resource. Use the
 `CONFIGURATION_COMPLETE` event to optimize deployment speeds without compromising
 the integrity and reliability of your infrastructure. 

Because the `CONFIGURATION_COMPLETE` event is not guaranteed to be set, any
 scenarios that use it should be prepared to handle a `CREATE_COMPLETE` event when
 no `CONFIGURATION_COMPLETE` event was set.


![Diagram showing the sequence of events for resource creation and eventual consistency check in a stack.](images/configuration-complete.png)
When the stack deployment starts, both the `AWS::ECR::Repository` and
 `AWS::ECS::Cluster` resources start the creation process
 (`ResourceStatus` = `CREATE_IN_PROGRESS`. When the
 `AWS::ECR::Repository` resource type has started the eventual consistency check
 (`DetailedStatus` = `CONFIGURATION_COMPLETE`), then the
 `AWS::ECS::TaskDefinition` resource can start the creation process. Similarly, once
 the `AWS::ECS::TaskDefinition` resource begins the eventual consistency check, the
 `AWS::ECS::Service` resource start the creation process.


###### `CREATE_IN_PROGRESS` and `CREATE_COMPLETE` events


* [Stack]:
`CREATE_IN_PROGRESS`
* [Resource]: ECR Repository
 `CREATE_IN_PROGRESS`
* [Resource]: ECS Cluster
 `CREATE_IN_PROGRESS`
* [Resource]: ECR Repository
 `CREATE_IN_PROGRESS`, `CONFIGURATION_COMPLETE`
* [Resource]: ECS Task Definition
 `CREATE_IN_PROGRESS`
* [Resource]: ECS Cluster `CREATE_IN_PROGRESS`,
 `CONFIGURATION_COMPLETE`
* [Resource]: ECS Task Definition
 `CREATE_IN_PROGRESS`, `CONFIGURATION_COMPLETE`
* [Resource]: ECS Service
 `CREATE_IN_PROGRESS`
* [Resource]: ECR Repository
 `CREATE_COMPLETE`
* [Resource]: ECS Cluster
 `CREATE_COMPLETE`
* [Resource]: ECS Service `CREATE_IN_PROGRESS`,
 `CONFIGURATION_COMPLETE`
* [Stack]:
`CREATE_IN_PROGRESS`, `CONFIGURATION_COMPLETE`
* [Resource]: ECS Task Definition
 `CREATE_COMPLETE`
* [Resource]: ECS Service
 `CREATE_COMPLETE`
* [Stack]:
`CREATE_COMPLETE`
