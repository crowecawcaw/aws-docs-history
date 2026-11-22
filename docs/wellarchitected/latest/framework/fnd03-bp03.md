

# FND03-BP03 Establish centralized event monitoring and response

 AWS Health is the authoritative source of information about service events, scheduled changes, and account-specific notifications that affect your AWS resources. In a multi-account environment, these events arrive per account by default, so no single team has organization-wide visibility. This best practice covers aggregating AWS Health events across your organization into a central view, routing them through automation, and responding to them consistently. 

 **Desired outcome:** 
+  You aggregate AWS Health events from every account into a single organization-wide view through AWS Health organizational view. 
+  A delegated administrator account, rather than the management account, operates the central Health view so day-to-day access does not depend on management account credentials. 
+  AWS Health events flow to Amazon EventBridge in a central account, where rules route them to the teams and systems that own the affected resources. 
+  Planned lifecycle events (such as resource retirements and certificate expirations) and operational events trigger documented, and where appropriate automated, responses rather than being noticed after impact. 

 **Common anti-patterns:** 
+  Relying on each account owner to watch their own AWS Health Dashboard, so organization-wide events are seen inconsistently or missed entirely. 
+  Operating the central Health view only from the management account, which couples routine operational access to your highest-privilege account. 
+  Treating AWS Health events as informational email rather than routing them into ticketing, chat, and automation so they are acted on. 
+  Ignoring scheduled change events (resource retirements, maintenance, certificate expirations) until the change causes a disruption. 
+  Assuming Health events are retained indefinitely, when organizational events are available for only 90 days. 

 **Benefits of establishing this best practice:** 
+  Operational and scheduled events across all accounts are visible in one place instead of scattered across per-account dashboards. 
+  Events route automatically to the owners of the affected accounts and resources, reducing time to acknowledge and act. 
+  A delegated administrator keeps the central view out of the management account, supporting least privilege. 
+  Scheduled retirements and maintenance are handled before they cause disruption rather than after. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 AWS Health delivers two broad categories of information: unplanned operational events that describe service issues affecting your resources, and scheduled changes such as resource retirements, planned maintenance, and certificate expirations that require action before a deadline. In a single account, the AWS Health Dashboard is enough to see both. As the account count grows, per-account visibility fragments, and events like a production resource retirement or a security bulletin spanning many accounts can go unnoticed. 

 [AWS Health organizational view](https://docs.aws.amazon.com/health/latest/ug/aggregate-events.html) resolves this by aggregating Health events from every account in your AWS Organization into a single feed. After you enable it, the management account, or a [delegated administrator](https://docs.aws.amazon.com/health/latest/ug/aggregating-health-events.html) account, can see events across all accounts, filtered by Region, account, or service. Keep the management account out of the daily operational path and assign a delegated administrator, typically your central operations or observability account. Operational teams then see organization-wide Health events without management account access. The programmatic AWS Health API and organizational view require a Business, Enterprise On-Ramp, or Enterprise Support plan. 

 [AWS Health integrates with Amazon EventBridge](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html), and organizational view delivers events from all accounts to EventBridge in the management or delegated administrator account. EventBridge rules match on event type, service, or affected account and route to notification channels (Amazon SNS, chat), to your incident management or ITSM system, or to automation. Use the account and resource identifiers in the event payload with the ownership metadata from [FND01-BP02 Establish ownership for billing, security, and operations](fnd01-bp02.md) to route events to the owning team. 

 Automate responses to scheduled change events. An [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function invoked by an EventBridge rule can open a ticket for an EC2 instance retirement and tag the affected instance, or raise an alert well ahead of an ACM certificate expiration. Because organizational Health events are retained for only 90 days, capture the ones you need for audit or trend analysis into durable storage such as Amazon S3 through EventBridge. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Enable AWS Health organizational view:** From the management account, enable [organizational view](https://docs.aws.amazon.com/health/latest/ug/enable-organizational-view.html) so AWS Health aggregates events from all member accounts into a single feed. You can enable it through the AWS Health console, the AWS CLI, or the AWS Health API. Confirm your organization has a Business, Enterprise On-Ramp, or Enterprise Support plan, which the AWS Health API and organizational view require. 

1.  **Delegate a Health administrator account:** [Register a delegated administrator](https://docs.aws.amazon.com/health/latest/ug/aggregating-health-events.html) for AWS Health, typically your central operations or observability account, so operational teams access organization-wide Health events without using the management account. This keeps the management account restricted while giving teams the visibility they need. 

1.  **Route organizational Health events to EventBridge:** In the management or delegated administrator account, create an [Amazon EventBridge rule for the organizational Health event feed](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html) that captures events from all accounts. Deploy the rule through infrastructure as code so it is version-controlled and reproducible. 

1.  **Route events to owners and operational systems:** Add EventBridge targets that match on event type, service, and affected account, and route to [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) topics, your incident management or ITSM system, and team chat through [Amazon Q Developer in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html). Use the account and resource identifiers in the event payload together with the ownership metadata from [FND01-BP02 Establish ownership for billing, security, and operations](fnd01-bp02.md) so events reach the owning team rather than a shared inbox. 

1.  **Automate responses to scheduled change events:** For event categories that map to a known action, invoke an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function from an EventBridge rule to respond automatically, for example opening a ticket and tagging the resource for an EC2 instance retirement, or raising an early alert before an ACM certificate expires. Keep automated actions least-privilege and scoped to the specific event types they handle. 

1.  **Retain events beyond the 90-day window:** Because organizational Health events are retained for only 90 days, forward events through EventBridge to durable storage such as [Amazon S3](https://aws.amazon.com/s3/) for longer-term audit, reporting, and trend analysis. 

1.  **Incorporate Health events into operational processes:** Reference the central Health view and its automated notifications in your incident response and operational review processes, and build [runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html) for common event types (resource retirements, planned maintenance, certificate expirations) so responders act consistently. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND03-BP01 Define observability standards and policies](fnd03-bp01.md) 
+  [FND03-BP02 Establish central, cross-account observability capabilities](fnd03-bp02.md) 
+  [FND01-BP02 Establish ownership for billing, security, and operations](fnd01-bp02.md) 
+  [FND04-BP05 Establish service quota management](fnd04-bp05.md) 

 **Related documents:** 
+  [AWS Health documentation](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html) 
+  [Aggregating AWS Health events across accounts](https://docs.aws.amazon.com/health/latest/ug/aggregate-events.html) 
+  [Aggregating AWS Health events using organizational view and delegated administrator access](https://docs.aws.amazon.com/health/latest/ug/aggregating-health-events.html) 
+  [Monitoring AWS Health events with Amazon EventBridge](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html) 
+  [AWS Health and AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-health.html) 