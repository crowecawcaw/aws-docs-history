# Change enablement in the cloud

All changes should be delivering business value. The change
enablement practice should focus on optimizing business risk,
maximizing productivity, and minimizing wasted effort and cost. The
AWS Cloud enhances a change enablement practice by:

- Minimizing the possibility of human error with workflow
  automation and integration
- Allowing the creation of identical environments for improved
  predictable and testable outcomes
- Removing the requirement to submit changes to scale
  infrastructure to meet business demand
- Automatically recovering from failure and rolling back failed
  changes
- Blue/green and other deployment techniques

Automation reduces the business risk associated with a change and
increases business agility, which delivers more business value.
Ultimately, this is why we make changes to applications and
infrastructure. Agile and DevOps ways of working are also designed
to deliver business value more quickly. However, to achieve these
outcomes, key areas of your change enablement process may need to be
updated.

AWS supports the evolution of your process.
[AWS Systems Manager Change Manager](../../../whitepapers/latest/aws-systems-manager-operational-capabilities/change-management.md "../../../whitepapers/latest/aws-systems-manager-operational-capabilities/change-management.md") is an AWS product
for requesting, approving, implementing, and reporting on
operational changes to your application and infrastructure. If you
use

[AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/"),
you can manage changes from a single delegated administrator account
across multiple AWS accounts and across AWS Regions. Alternatively,
using a local account, you can manage changes within a VPC. Use
Change Manager for managing changes to both AWS resources and
on-premises resources.

In an AWS architecture, you can isolate applications within a single
VPC, which helps you reduce the scope when making changes and
decentralize the authority for change approval. This isolation is
not possible with on-premises infrastructure solutions.
Decentralizing change authority through enforced automation
increases velocity as desired. Customers should follow
Well-Architected Best Practices when architecting their workloads to
optimize operational capabilities.

## Managing configuration items in the cloud

On AWS, you can manage cloud configuration items in
[AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/") when processing changes more efficiently and
accurately. For example, if an application suffers a fault in a
traditional IT environment where application updates and operating
system patches are installed or deployed on a server, an engineer
may be tasked to investigate and either apply a fix or deploy a
new server. Either of these tasks requires an emergency change and
could impact the business for an amount of time.

The cloud enables automation that is initiated by a set of
configured conditions. For example,
[AWS Auto Scaling groups](https://aws.amazon.com/autoscaling/ "https://aws.amazon.com/autoscaling/") (ASG) can create additional EC2 instances as
needed. You can use an ASG to automate the update of system
patches by allowing the ASG to deploy each patched EC2. In this
example, the manageable resource, the ASG, is recognized as the
configuration item, not the EC2 instances that are created.
Furthermore, if you use a health check to detect a failure within
an ASG, the ASG replaces affected items automatically from the
designated image. This represents how cloud technology removes the
requirement to have change control under certain pre-defined
conditions. The automation provisions additional resources to meet
demand, reduces human error and configuration drift, and minimizes
business risk while reducing the time to recover.

In a traditional environment, the addition of servers requires
approval using a standard or normal change record. In the
best-case scenario, work was done to increase capacity. In the
worst-case scenario, the business was impacted and put at risk by
the business processes required to introduce additional capacity,
and it may not have been possible to meet the business demand in
the required amount of time.

According to the traditional definition of a change (the addition,
modification, replacement, or removal of a configuration item), a
change record would be necessary when an ASG deploys an EC2
instance. As a result, it may help to redefine what items should
be considered configuration items.

As a rule of thumb in the cloud, any resource that is
auto-deployed without human triggering, should not be subject to a
change ticket, nor should it be considered a configuration item
that requires you to manage change. In the previous example, the
servers themselves are not configuration items when they are in an
Auto Scaling group because they are transient and initiated by a
non-human process. The Auto Scaling group and the image used to
create the servers should be considered configuration items. When
changes are made to these items and configurations are incorrect,
the business can be exposed to risk.

To manage configuration items in the AWS Cloud, use
[AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/") to assess, audit and evaluate the configuration of
AWS resources allowing you to monitor and record AWS resource
configurations. With AWS Config, you can track the relationships
between resources and review resource dependencies prior to making
changes. Once a change occurs, you can quickly review the history
of the resource's configuration and determine what the resource's
configuration looked like at any point in the past. AWS Config
provides you with information to assess how a change to a resource
configuration affects your other resources, which minimizes the
impact of change-related incidents. If you still maintain a CMDB
within your ITSM platform, you can also use the
[AWS Service Management Connector](https://aws.amazon.com/service-management-connector/ "https://aws.amazon.com/service-management-connector/") to synchronize configuration
items between AWS Config and your CMDB.

You can use
[AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") change sets to preview how proposed changes
to a stack might affect your running resources. For example, you
can use change sets to check whether your changes would delete or
replace any critical resources. When you decide to deploy the
change set, AWS CloudFormation automatically makes the changes.

## Automation of change models

Regardless of whether a deployment is an application, a patch, or
a configuration change, an optimized cloud configuration can
automate the deployment process through an unchanged
pipeline.
You can use cloud and software development pipelines to model
change more specifically by defining repetitive end-to-end change
types. These change models help you pre-plan for the level of
business risk when you deploy a specific change.

| ITIL®4 Change Enablement Practice<br>Guide, PeopleCert+                                      |
| -------------------------------------------------------------------------------------------- |
| A Change Model is a repeatable approach to the management of a<br>particular type of change. |

The concept of a standard change can be confused with a change
model. Standard changes are typically defined generically as low
risk and well-documented. A change model is defined specifically
and is managed the same way each time it is deployed, often via a
development pipeline. Change models may have some level of risk,
but these risks are mitigated through automated governance.

Pipeline deployment capabilities foster repeatability and
consistency across multiple environments and types of changes, as
well as automation of software testing, compliance testing,
security testing, and functional testing. With cloud technologies,
you can programmatically model each type of change through its
entire pipeline workflow and enforce change control policies. With
this capability, there is no longer a need to model generic
changes based on the level of risk. You can now model specific
changes based on how their pipeline has mitigated risk. Once
certified, the pipeline is free to deploy these changes on-demand
because the automation enforces internal approvals. Although this
does not verify that no adverse impacts happen, it optimizes your
risk by embedding change policies into the pipeline workflow. A
change cannot be automatically deployed unless the workflow
completes all required steps. This includes the automated creation
and population of a change record in your ITSM system.

For example, if an automated security test is approved for
deployment, the security review during the change approval process
can be reduced or even removed in the appropriate circumstances.
Repeatability and consistency throughout the lifecycle of a
workload and its deployment reduces the potential time delay and
the burden required by the examination of changes by the Change
Approval Board. The focus should be on how changes are delivered
(through the pipeline) and the automation of tests that reduce
required scrutiny by the approval board, both of which are prone
to human error.

[AWS CodePipeline](https://aws.amazon.com/codepipeline/ "https://aws.amazon.com/codepipeline/") and

[Amazon CodeCatalyst](https://aws.amazon.com/codecatalyst/ "https://aws.amazon.com/codecatalyst/") help you to automate your software release
process and speed up the release of new features to your users.
AWS CodePipeline helps you iterate on feedback more quickly. When
you automate your build, test, and release process, you can test
each code change and catch bugs while they are small and simple to
fix. Amazon CodeCatalyst helps you set up a new project from
pre-configured blueprints. These two services work together to
help you increase velocity.

EC2 Image Builder reduces the effort of keeping images up-to-date
and secure by providing a simple graphical interface, built-in
automation, and AWS-provided security settings. With Image
Builder, there are no manual steps for updating an image, nor do
you have to build your own automation pipeline. Creating a
[golden
image](https://opensource.com/article/19/7/what-golden-image "https://opensource.com/article/19/7/what-golden-image") using EC2 Image Builder reduces the risk
of non-compliant images being used, as well as improving security,
consistency, and compliance. For more information, see
[EC2 Image Builder](https://aws.amazon.com/image-builder/ "https://aws.amazon.com/image-builder/").

Use AWS Systems Manager to automate operational tasks to help make
your teams efficient. With automated approval workflows and
runbooks with rich text descriptions, you reduce human error and
simplify maintenance and deployment tasks on AWS resources. You
can use predefined automation runbooks or build your own to share
for common operational tasks, such as stopping and restarting an
EC2 instance. Systems Manager also has built-in safety controls
that roll out new changes and automatically halt and rollback the
change if errors occur. For more information, see
[AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/").

[AWS Systems Manager Change Manager](../../../systems-manager/latest/userguide/change-manager.md "../../../systems-manager/latest/userguide/change-manager.md"), a subset of the Systems
Manager product, provides organizations the ability to automate
repeatable operational changes to applications and infrastructure.
You can use Change Manager to create automated runbooks using
CloudFormation code.

We recommend a change model certification process to ensure that
an entire end-to-end pipeline workflow adheres to the requirements
of your change control policy and mitigates business risk, while
delivering desired business value. The change enablement practice
should define clear criteria necessary for certification of each
pipeline that desires to have automated continuous deployment
permission.

It is worth noting that from an ITIL perspective, when automating
a change model, you are integrating three practices into one value
stream: release management, change enablement, and deployment
management.

## Automated testing and rollback

A change model that has automated testing and rollback creates the
confidence for continuous deployment. Enable these capabilities
for workloads that require automated change models. Without
automated testing and failback capabilities, an automated change
model may require you to manually pause the pipeline to gain
approval for deployment. This may be acceptable for some
workloads, and it highlights another benefit of using the cloud to
isolate application workloads. By isolating workloads inside their
own account or VPC, we can reduce the overall scope of a change,
allowing the workload owner to approve it, even if the changes
cannot be automatically deployed.

## Remediation from failure

An automated change model that uses deployment capabilities, such
as blue/green, should still not be approved without considering
the consequences of a failure. A backout plan should be a
requirement in the change model. In the event of a failure,
automated backout can be initiated manually or automatically based
on pre-conditions and status monitoring. Although not always
possible with every type of change, the requirement should be that
changes are reversible where possible. The application's
architecture influences the ability to make changes reversible.
Not every change can be easily reversed, but this should be the
goal to mitigate any business impact in the case of failure.

As discussed, deployments in the AWS Cloud that use an automated
pipeline allow changes to be redeployed quickly and safely,
helping minimize risk and reduce business impact. In certain
scenarios, it may not be possible to backout changes or redeploy,
in which case the organization may need to invoke an incident
management process or a business continuity plan to resolve the
failed deployment in production. For more detail, see
[Ensuring
Rollback Safety During Deployments](https://aws.amazon.com/builders-library/ensuring-rollback-safety-during-deployments/ "https://aws.amazon.com/builders-library/ensuring-rollback-safety-during-deployments/"). Track metrics for the
number of successful vs. reversed changes, not to place blame on
individuals, but to reveal continuous improvement opportunities.

For your most critical applications, use continuous data
protection in the cloud to provide sub-second recovery point
objectives (RPOs) and recovery time objectives (RTOs) in minutes.
For more detail, see
[AWS Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/ "https://aws.amazon.com/disaster-recovery/"). Crucially, where it's
not possible to back out changes, the AWS Cloud provides methods
to reduce business risk and impact of a failed change by
simplifying the redeployment or initiation of disaster recovery
plans.

Modern deployment methods in the cloud allow for fast or instant
rollback. For example, with blue/green deployments, you can make a
change to a workload by deploying an identical copy (green) of the
live environment (blue) with the configuration change. Users are
then switched to the new environment (green) while the old live
environment (blue) remains available, but idle. For more
information, see
[Blue/Green
deployments](../../../whitepapers/latest/overview-deployment-options/bluegreen-deployments.md "../../../whitepapers/latest/overview-deployment-options/bluegreen-deployments.md"). In this scenario, if a failure is
discovered, users can be redirected back to the blue environment,
and the business impact can be reduced. It is also possible to
combine this approach with a
[canary
release](https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.canary-deployment.en.html "https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.canary-deployment.en.html") method. With this approach, you can redirect a
subset of users to the new deployment, assess its efficacy, and
gradually increase the number of users on the new deployment until
all users are using the new deployment.

There are other considerations when choosing a method of
deployment, but the key is to use automated methods in your
pipeline to enforce requirements.

Amazon CodeCatalyst is a unified software development service for
development teams to quickly build, deliver and scale applications
on AWS while adhering to organization-specific best practices.
Developers can automate development tasks and innovate faster with
generative AI capabilities, and spend less time setting up project
tools, managing CI/CD pipelines, provisioning and configuring
various development environments or coordinating with team
members. IT Leaders can codify organizational best practices at
scale via application blueprints to ensure compliance across teams
with scale. For more information, see
[Amazon CodeCatalyst](https://aws.amazon.com/codecatalyst/ "https://aws.amazon.com/codecatalyst/").

AWS CloudFormation monitors the state of your application during
stack creation and updating and rollbacks that operation if the
application breaches the threshold of the alarms you've specified.
For each
[rollback](../../../AWSCloudFormation/latest/UserGuide/using-cfn-rollback-triggers.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-rollback-triggers.md")
you create, you specify the CloudWatch alarm that AWS CloudFormation monitors. AWS CloudFormation monitors the specified
alarms during the stack create or update operation and for the
specified amount of time after it deploys the resources. If any of
the alarms is set off during the stack operation or the monitoring
period, AWS CloudFormation rollbacks the entire stack operation.
For more information, see
[AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/").

[AWS AppConfig](https://aws.amazon.com/systems-manager/features/appconfig/ "https://aws.amazon.com/systems-manager/features/appconfig/")
supports best practices by rolling out
configuration changes at once or over a period. It monitors the
change over a time that customers define. If you configure alarms
in Amazon CloudWatch, AWS AppConfig can automatically rollback
configuration changes if those alarms are initiated. For more
information, see
[AWS AppConfig](https://aws.amazon.com/systems-manager/features/appconfig/ "https://aws.amazon.com/systems-manager/features/appconfig/").

## Adapting your change enablement practice to the cloud

The AWS Cloud facilitates several main adaptations:

1. The ability to automate deployment with deployment techniques
   that mitigate risk
2. The ability to automate rollback when those deployments fail
3. The automation of change ticket creation from data available
   in the pipeline, allowing developers to perform all the
   required steps in their pipeline tool

Because the risk and impact to the business of a failed change can
be reduced by these aspects, you can make frequent changes with
confidence in the deployment and rollback plans. As a result, your
process may also require an update for the acceptance of rolling
back changes.

If failed changes have a lower impact due to the speed and
consistency of roll back, activating rollbacks is now part of the
normal process. This is true when you remediate the issue and push
it through the same automated pipelines to deliver the original
intended business value of the change.

With these considerations in mind, if automation, pipelines, and
deployment methods are in place, it is now possible to reconsider
the approach to standard changes. A standard change is where there
is a defined event to initiate the change request. In addition, in
a standard change, actions are documented and proven, authority is
given in advance (or pre-authorized), and the risk is usually low.
If the automation, testing, and deployment strategies are put in
place, it results in a scenario where large, infrequent, and risky
changes are transformed in to small, frequent, and low-risk
changes. In this scenario, each standard change evolves to its
individual type or model that is specific to its deployable
component in production.

By understanding the risk-reduction strategies in the AWS Cloud,
and by re-architecting workloads to isolate adjacent workloads and
other infrastructure resources, it is possible, and it may even be
necessary to widen the scope of a standard change to include
deployments that would have previously been considered normal due
to their associated risks associated in traditional IT
environments. You increase volume and velocity of change while
reducing additional risk.

As changes become more frequent with agile methodologies and
automation, there is a risk that the process becomes overburdened
with normal changes. Higher velocity can lead to delaying changes
due to bandwidth or resource constraints, causing important
details to be missed. Both scenarios introduce business risk that
change enablement aims to optimize. In an environment of small,
frequent changes, standard (automated) changes become the new
standard. You should then give proper scrutiny to normal changes,
which helps you reduce business risk and deliver on desired
business outcomes.

Smaller changes also enable increase in frequency. By changing
frequently, you improve your organization's capability, which
minimizes business disruption (ITIL® 4: High-Velocity IT,
PeopleCert+). This alone can positively impact business value and
operational metrics expected from your move to AWS.
