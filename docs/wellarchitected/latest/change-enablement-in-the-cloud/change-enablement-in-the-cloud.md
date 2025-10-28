# Change Enablement in the Cloud

Publication date: **June 27, 2024** ([Document revisions](document-revisions.md "document-revisions.md"))

Like every business function, change management should provide the
capability for your organization to succeed. Just as every business
has a finance function to govern spending, change management is
essential for optimizing business risk. You can benefit from change
management if you have migrated to the cloud, have a hybrid
environment, or architected your workload natively in the cloud. An
effective change management process is agile and reduces time to
market while optimizing risk to your business. With an efficient
process, you can improve the quality and speed of delivery of all
changes for the business. An effective record of change should also
act as one of your first troubleshooting references if an incident
occurs.

Typically, businesses transitioning to the cloud expect to iterate
on products and deliver enhanced business value through an increased
volume of changes to their IT infrastructure and applications.
Current industry trends indicate that a high performing change
management process is comprised of increased frequency of
deployment, improved lead time for a change, and lower failure
rates. However, to achieve this, it also requires version control
and continuous delivery, as well as automated testing and deployment
capabilities. Research also suggests that peer-reviewed changes
within a team can achieve the same level of risk optimization as
using a change advisory board. This is important because it allows
organizations to decentralize change approval authority. (ITIL® 4:
High-Velocity IT, PeopleCert+)

By following the guidance in this paper, updating your processes
aligns with both the
[AWS
Cloud Adoption Framework (CAF)](https://aws.amazon.com/cloud-adoption-framework/ "https://aws.amazon.com/cloud-adoption-framework/") and the
[AWS
Well-Architected Operational Excellence](../operational-excellence-pillar/welcome.md "../operational-excellence-pillar/welcome.md") Framework, ensuring
adherence to best practices in governance when deploying changes to
your AWS environment.

## Introduction

In a cloud computing environment, new IT resources are readily
available. This reduces the time it takes to make resources
available to your developers, which leads to a dramatic increase in
agility for the organization. As a result, the cost and time it
takes to experiment and develop is significantly lower. For more
detail, see
[Six
advantages of cloud computing.](../../../whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.md "../../../whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.md")

The more successful an organization is at increasing its agility in
the cloud, the more difficult it can become to manage change.
Traditional processes can impede the volume and speed the cloud
enables. Business stakeholders may have become accustomed to longer
release cycles using
[waterfall](https://en.wikipedia.org/wiki/Waterfall_model "https://en.wikipedia.org/wiki/Waterfall_model")
methodologies, and challenges can arise from the transition to
working in a way that increases the frequency of software releases.
These challenges may result in increased stakeholder engagement, the
introduction of unnecessary gates that hinder development progress,
or unmanaged changes. Modernizing your change management process
will be necessary to overcome these challenges.

Make frequent, small, and reversible changes. Design workloads to
allow smaller components to be updated more frequently. Plan your
changes in smaller increments that can be reversed if they fail
(without an impact to business outcomes). Use this approach to
achieve the desired agility. AWS best practices and strategies for
designing and operating a cloud workload align with this approach. A
change process must continue to govern the deployment of a new
services, software, patches, and configuration changes.

In the cloud, you can enable automated governance with a complete
audit trail of the deployment steps. Due to automated deployment
capabilities, you can preserve agility by reducing the penalty if a
rollback of a failed change is required. To achieve cloud agility,
organizations must rollback changes that have adverse business
consequences, and automate this process where possible. The
automation should enforce change policies to occur within the
software development pipeline as regularly scheduled and unscheduled
changes continually flow. Different policies and procedures should
exist for emergency changes or changes that require manual processes
during deployment.
