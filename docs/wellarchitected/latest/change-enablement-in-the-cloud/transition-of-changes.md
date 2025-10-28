# Transition of changes

After approval of a release using the change enablement process and
following the appropriate project management, release, and
deployment management steps, deploying the release causes you to
validate and test your change. Guidance on transitioning changes is
also provided in the
[Operational
Excellence Pillar](../operational-excellence-pillar/welcome.md "../operational-excellence-pillar/welcome.md") of the AWS Well-Architected Framework.

In this stage, you should determine the scope of service validation
and testing within the AWS Cloud. This is best illustrated by understanding the
[AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") for security. The validation and
testing of a service should be limited to the areas in this diagram
that are in scope for the customer. However, it is critical that
operations have an operational understanding of any managed services
before acceptance into service. In addition, AWS informs customers
of a change that is being made in their area of responsibility.
However, due to the abstraction from the underlying hardware in the
cloud, these changes typically do not impact customer business
operations.

Automation, integration, and deployment tools in the AWS Cloud allow
the business to make small, frequent changes that reduce business
risk and introduce business value at an increased rate. The
introduction of the cloud should not change the process of service
validation and testing, but the rate of change leads to an increased
capacity for validation and testing that may require changes to the
implementation of the process and the focus of the stakeholders.

Changes introduce business value. It is important that each release
meets customer expectations and that IT operations teams can support
this new added business value. The criteria for assessing this value
in the cloud should not change from what already exists in your
legacy process, but the organization must be prepared for an
increase in release volume and adapt the implementation of these
processes by introducing automation.

A new service requires consent from the customer that the new
service meets agreed service-level requirements. The current best
practices of tracking your current service-level objectives (SLOs)
and tracking service level agreement (SLA) breaches still apply.
This can be done by a third-party monitoring service for external
facing services. For internal services, you must track this with
monitoring and metrics on the primary business function of the
services. For example, if a certain business transaction is not
performing per the SLA, the monitoring of this performance metric
should notify the workload owner of the breach proactively. If this
occurs because of a recent change, it's possible to reverse the
change with automation. Separate service-level requirements may
exist for different aspects of a service, and additional dimensions
may be required as metrics to indicate which aspect is being
measured. Indeed, during a change deployment, monitoring can drive
an automated rollback if a change would violate an SLA.

Operations must be able to support a new release or service before
they make it available to the customer. With the correct tools and
process defined, you can design automation that creates
documentation, provision runbooks, and build predefined patching
plans. This process can be made robust by using cloud services that
ensure that only use pre-approved services can be deployed. An
example of this is
[Service Catalog](https://aws.amazon.com/servicecatalog/ "https://aws.amazon.com/servicecatalog/").

The focus of a test manager should be to automate service acceptance
testing as much as possible. The cloud can make it easier with a
wide variety of tools that are available for both validation and
testing.

Amazon CloudWatch provides you with data and actionable insights to
monitor your applications running on AWS or on-premises, respond to
system-wide performance changes, and display a unified view of
operational health. As you deploy changes, you can set alarms,
visualize logs and metrics side-by-side, take automated actions,
troubleshoot issues, and discover insights to keep your applications
running smoothly. For more information, see
[Amazon CloudWatch](https://aws.amazon.com/pm/cloudwatch/ "https://aws.amazon.com/pm/cloudwatch/").

CloudWatch provides different features, including dashboards,
synthetic monitoring, CloudWatch Application Insights, and X-Ray,
which can be used during and after transitioning a release into
production to ensure that actionable alarms are present to prevent
or remediate against service degradation or failure.

Providing easy access to metrics, logs, and dashboards to monitor
the health of an application helps teams to resolve problem faster
and reduce business risk, while implementing changes.
