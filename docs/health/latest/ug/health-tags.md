

# Using tags with AWS Health events

AWS Health can include your resource and account tags in AWS Health events. When you turn on this feature and choose the tag keys that you want, AWS Health adds the matching tag key-value pairs to the affected entities of each event. You can see the tags in the AWS Health Dashboard, in AWS Health API responses, and in AWS Health events that are delivered through Amazon EventBridge.

## What is tag enrichment in AWS Health?
<a name="what-is-tag-enrichment"></a>

AWS Health events identify affected resources by Amazon Resource Name (ARN) and affected accounts by AWS account ID. These identifiers don't always tell you who owns a resource, which application it supports, or how critical it is. Many organizations store this context in tags.

With tag enrichment, AWS Health uses the ARN of each affected resource to look up the tag keys that you select and then returns the matching values with the event. In organizational view, AWS Health also returns the account tags that you define in AWS Organizations.

The following table shows where each tag type comes from and the views that include it.


| Tag type | Where it comes from | Account view | Organizational view | 
| --- | --- | --- | --- | 
| Resource tags | Tags on the affected AWS resource | Yes | Yes | 
| Account tags | Tags on member accounts in Organizations | No | Yes | 

Tag information is available through the following channels:
+ AWS Health Dashboard
+ AWS Health API
+ Amazon EventBridge (only for tag keys that you enable for EventBridge)

Tags aren't included in AWS Health email notifications.

## Use cases
<a name="tags-use-cases"></a>

You can use the tags in AWS Health events in the following ways.

**Route events to the right owner automatically**  
Use an `Owner`, `Team`, or cost center tag in an EventBridge rule or downstream workflow to send each event to the team that owns the affected resource. You don't have to build custom AWS Lambda functions or AWS Step Functions workflows that call tagging APIs to look up ownership.

**Prioritize by environment or criticality**  
Use an `Environment` or `Criticality` tag to separate production impact from development and test impact. For example, escalate only scheduled changes that affect resources tagged `Env=DevTest`.

**Track planned lifecycle events by application**  
Use an application tag, such as `AppId` or `aws:cloudformation:stack-name`, to see all resources in an application that are affected by a planned lifecycle event, such as a Lambda runtime deprecation or an Amazon EKS version upgrade. This helps you find outstanding actions across many accounts before a deadline.

**Enrich IT service management (ITSM) tickets**  
Pass tag values, such as an ITSM assignment group, to tools such as ServiceNow or Jira so that tickets created from AWS Health events can be assigned to the right group.