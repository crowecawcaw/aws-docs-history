

# COST01-BP04 Keep up-to-date with new service releases

 Cloud providers release new services, features, and price reductions constantly. Each release can make part of your architecture cheaper to run, and each price cut can change a decision you made months ago. Staying current, through your own monitoring and through experts who track the cloud provider, turns these changes into recurring savings. 

 **Desired outcome:** 
+  You stay aware of new services, features, and price reductions that can lower the cost of running your workloads. 
+  You have a defined owner and cadence for reviewing releases and deciding which are worth adopting. 
+  You revisit deferred decisions when a relevant price reduction or new service changes their economics. 
+  Your teams draw on account teams, partners, and events to learn about cost-relevant changes. 

 **Common anti-patterns:** 
+  Keeping legacy designs out of habit, without checking whether a newer service would cost less. 
+  Leaving the architecture unchanged for long periods without evaluating new options. 
+  Ignoring release announcements and blog updates that describe cost-saving features. 
+  Overlooking price reductions that would change past build-or-buy and deferral decisions. 
+  Never engaging account teams, partners, or events that surface relevant changes. 

 **Benefits of establishing this best practice:** 
+  Cost efficiency improves continuously as new services and features replace costlier approaches. 
+  Access to newer capabilities keeps architectures aligned with current best practices. 
+  Price reductions translate into savings, because deferred decisions are revisited. 
+  Teams build a working understanding of the provider's direction and roadmap. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 The economics of a workload are not fixed at design time. A provider that ships features and cuts prices frequently keeps changing the cheapest way to run any workload. The risk is architectural inertia: a design that was cost-optimal at launch becomes more expensive as new functionality appear and go unadopted. 

 No team can evaluate every announcement, and not every new service is worth adopting. Adoption carries a cost in migration effort, testing, and retraining, which you weigh against the savings it promises. Separate monitoring from evaluation. Scan releases lightly but continuously. Then, on a cadence, deliberately evaluate the few changes that could materially reduce cost for your workloads. 

 Price reductions can change decisions retroactively. A build-or-buy analysis or a deferred migration might not have made sense at last year's prices. It can make sense now, with no change to the service itself. Treat a relevant price reduction as a prompt to reopen decisions you previously parked. 

 Announcement channels and blogs tell you what shipped. AWS account teams, solutions architects, and partners bring context on what is relevant to your workloads and how other organizations use it. That's often faster than reading every release yourself. Events and community meetups add peer experience. Assign this monitoring to a defined owner, often within a cloud center of excellence or cost-management function. Without a named owner, the work gets neglected. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Assign ownership and a review cadence:** Make one team or role responsible for monitoring new releases and price changes, and set a recurring cadence to evaluate them. Without a named owner, release monitoring lapses. 

1.  **Subscribe to announcement channels:** Follow [What's New with AWS](https://aws.amazon.com/new/) and the [AWS News Blog](https://aws.amazon.com/blogs/aws/) by RSS or email, and set your preferences on the [AWS communication preferences](https://aws.amazon.com/preferences/email/unsubscribe?languages=english) page. Add the [AWS Cost Management blog](https://aws.amazon.com/blogs/aws-cloud-financial-management/) for cost-specific guidance. 

1.  **Track price reductions and revisit deferred decisions:** Follow the [price-reduction category of the AWS News Blog](https://aws.amazon.com/blogs/aws/category/price-reduction/), and reopen any decisions you parked for cost reasons when a relevant reduction lands. 

1.  **Engage your account team and partners:** Schedule a regular cadence with your account manager, solutions architect, and support team to discuss industry trends and cost-relevant services. Include AWS Partners where they bring specialized expertise. 

1.  **Attend events and meetups:** Attend AWS summits, local meetups, and virtual events to hear how AWS experts and other customers apply new services to reduce cost. 

1.  **Evaluate and pilot promising services:** For the few releases that could materially cut cost, run a focused evaluation or pilot before committing, weighing migration and operating effort against expected savings. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST01-BP01 Establish cloud budgets and forecasts](cost01-bp01.md) 
+  [COST01-BP03 Track project lifecycle](cost01-bp03.md) 
+  [COST05-BP06 Perform continuous cost analysis](cost05-bp06.md) 
+  [COST07-BP01 Perform pricing model analysis](cost07-bp01.md) 

 **Related documents:** 
+  [AWS Cloud Financial Management](https://aws.amazon.com/aws-cost-management/) 
+  [What's New with AWS](https://aws.amazon.com/new/) 
+  [AWS News Blog](https://aws.amazon.com/blogs/aws/) 
+  [AWS News Blog – Price reductions](https://aws.amazon.com/blogs/aws/category/price-reduction/) 

 **Related examples:** 
+  [Improving your FinOps practice with real-time Slack notifications of AWS CFM announcements](https://aws.amazon.com/blogs/aws-cloud-financial-management/improving-your-finops-practice-with-real-time-slack-notifications-of-aws-cfm-announcements/) 

 **Related workshops:** 
+  [Cloud Intelligence Dashboards – AWS News feeds](https://catalog.workshops.aws/awscid/en-US/dashboards/advanced/aws-feeds) 