

# Planned lifecycle events for AWS Health
<a name="aws-health-planned-lifecycle-events"></a>

Learn about planned lifecycle events for AWS Health.

**Topics**
+ [What are planned lifecycle events?](#what-are-planned-lifecycle-events)
+ [What should I expect when I receive a planned lifecycle event notification?](#planned-lifecycle-event-notifications)
+ [Shared responsibility model for resilience](#shared-responsibility-model)
+ [Accessing planned lifecycle events](#accessing-planned-lifecycle-events)

## What are planned lifecycle events?
<a name="what-are-planned-lifecycle-events"></a>

AWS Health communicates important changes that can affect the availability of your applications. In the AWS shared responsibility model, AWS takes action to keep the underlying hardware and infrastructure that supports your resources up to date and secure. However, some changes require customer action or coordination in order to avoid impact to your applications. AWS Health notifies you in advance of important changes such as:
+ Open source software end of support - Some AWS services run open source versions of software. If the open source community ends support for software versions, then AWS informs you when you need to take action to upgrade and avoid impact to your applications.
  + [Amazon RDS for MySQL engine version end of support](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Concepts.VersionMgmt.html)
  + [Amazon EKS Kubernetes version end of support](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html#kubernetes-release-calendar)
+ Changes that affect AWS-owned resources that might require your action.
  + [Amazon RDS Certificate Authority certificates expiration](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL-certificate-rotation.html).
**Note**  
All notifications that fit this criteria will be reported through AWS Health as Planned Lifecycle Events.
+ **Dynamic resource burndown and improved metadata**: From the time you receive the notification through the lifespan of the AWS Health event, your affected resources are associated with the AWS Health event as affected entities with a specific entity status. Affected resources are specified in ARN format, where applicable. If your affected resource(s) require customer action, then they are listed with a “PENDING” status. If your affected resource(s) had the requisite action performed or the resources were deleted, then the status is updated to “RESOLVED”.
**Note**  
Resource state updates are performed asynchronously and periodically and can have a delay of up to 72 hours in rare occasions.
In the exceptions where dynamic updates are not provided, rather than resources having a “PENDING” or “RESOLVED” status, resources will not be assigned any status.
Resource status updates are not supported in the AWS GovCloud (US) and China Regions. 

## What should I expect when I receive a planned lifecycle event notification?
<a name="planned-lifecycle-event-notifications"></a>

The AWS Health experience for planned lifecycle events helps your teams learn about upcoming lifecycle changes and track action completion.

**Type category:** Scheduled change

**Event type code**: AWS\_{SERVICE}\_PLANNED\_LIFECYCLE\_EVENT

**Event start time:** Event start time is the soonest date at which your resources are affected by the change.

**Event end time:** Event end time is the date that the change finishes across all AWS resources. Note that end time is not always specified. It is important to treat the start time as the change date. 

**Note**  
Organizations can expect to receive a single event ARN for every planned lifecycle event grouped by Region where there are affected resources. But they might receive multiple ARNs if the organization has a large number of affected AWS accounts or resources.

**Early visibility into planned lifecycle events:** Planned lifecycle events are designed to have a minimum lead time of 180 days for major versions/changes and 90 days for minor versions/changes, where possible.

**Dynamic resource burndown and improved metadata:** From the time you receive the notification through the lifespan of the AWS Health event, your affected resources are associated with the AWS Health event as [affected entities](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedEntities.html) with a specific entity status. Affected resources are specified in ARN format, where applicable. If your affected resource(s) require customer action, then they are listed with a “PENDING” status. If your affected resource(s) had the requisite action performed or the resources were deleted, then the status is updated to “RESOLVED”.

**Note**  
AWS Health notifications provide status updates over time where possible, except for the AWS GovCloud (US) and China Regions.
Resource state updates are performed asynchronously and periodically and can have a delay of up to 72 hours in rare occasions.

![Amazon EKS planned lifecycle event example showing event details and timeline](http://docs.aws.amazon.com/health/latest/ug/images/eks-example-ple.png)


**After the planned event date passes:**

1. If applicable, the service might implement the described change to your resource any time after the start date of the event.

1. If you resolve all resources prior to the end of support date, then your AWS Health event changes to the status `Closed`.

1. If you have outstanding resources after the change date that aren't resolved, then the AWS Health event remains open for 4 years after the event start or end date (whichever is later). After this time, the AWS Health event is deleted.

## Shared responsibility model for resilience
<a name="shared-responsibility-model"></a>

Security and compliance are shared responsibilities between AWS and the customer. Depending on the services deployed, this shared model can help relieve the customer’s operational burden. This is because AWS operates, manages, and controls the components from the host operating system and virtualization layer down to the physical security of the facilities in which the service operates. The customer assumes responsibility and management of the guest operating system (including updates and security patches) and other associated application software, in addition to the configuration of the security group firewall provided by AWS. For more information, see [Shared responsibility model](https://docs.aws.amazon.com/whitepapers/latest/aws-risk-and-compliance/shared-responsibility-model.html).

![Shared responsibility model](http://docs.aws.amazon.com/health/latest/ug/images/responsibility-model.png)


## Accessing planned lifecycle events
<a name="accessing-planned-lifecycle-events"></a>

Planned lifecycle events can be accessed and monitored using several channels:
+ [Use Amazon EventBridge](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html)
+ [Use the AWS Health dashboard](https://docs.aws.amazon.com/health/latest/ug/getting-started-health-dashboard.html)
  + [Calendar view](https://docs.aws.amazon.com/health/latest/ug/aws-health-account-views.html#calendar-view)
  + [Affected resources view](https://docs.aws.amazon.com/health/latest/ug/aws-health-account-views.html#affected-resouces-view)
+ [Use the AWS Health API](https://docs.aws.amazon.com/health/latest/ug/health-api.html)