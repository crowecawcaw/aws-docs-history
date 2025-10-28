# Create a Region switch plan

You can create two different kinds of plans in Region switch: an active/active plan or an active/passive plan. When
you create a plan, specify the type that applies to how you want to manage failover.

- An _active/passive_ approach deploys two application replicas into two Regions, with traffic routed to
  the active Region only. You can activate the replica in the passive Region by executing the Region switch plan.
- An _active/active_ approach deploys two application replicas into two Regions, and both replicas are
  processing work or receiving traffic.

# To create a Region switch plan

1. From the Region switch console, choose **Create Region switch plan** with active/passive approach.
2. Provide the following details:
   - **Plan name** - Enter a descriptive name for your plan.
   - **Multi-Region approach** - Select **Active/passive** or
     **Active/active**. This
     approach means two application replicas are deployed into two Regions, with traffic routed into the active
     Region only. You can activate the replica in the passive Region by executing the Region switch plan.
     - Choose **active/passive** if you have deployed two application replicas
       into two Regions, with traffic routed to the active Region only. Then, you can activate the replica
       in the passive Region by executing the Region switch plan that specifies _Active/passive_.
     - Choose **Active/active** if you have deployed two application replicas
       into two Regions, and both replicas are processing work or receiving traffic.

   - **Primary and standby Regions** or **Regions** - Select the primary and standby Regions for
     your application. For an active/active deployment, select the Regions where the replicas are deployed.
   - **Recovery time objective (RTO)** - Enter your desired RTO. Region switch uses this to
     provide insight into how long Region switch plan executions take to complete in comparison to your desired RTO.
   - **IAM role** - Provide an IAM role for Region switch to use to execute
     the plan. For more information about permissions, see [Identity and Access Management for Region switch in ARC](security-iam-region-switch.md "security-iam-region-switch.md").
   - **Amazon CloudWatch alarm** - Provide an application health alarm that you've created
     with Amazon CloudWatch, to indicate the health of your application in each Region. Region switch uses these application
     health alarms to help determine the actual recovery time after you switch Regions to implement recovery.

   Before you add CloudWatch alarms to a Region switch plan, make sure that you have the correct IAM policy in place.
   For more information, see [CloudWatch alarms for application health permissions](security_iam_region_switch_cloudwatch.md "security_iam_region_switch_cloudwatch.md").
   - **Tags** - Optionally, add one or more tags to your plan.
