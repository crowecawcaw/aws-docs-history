# Grouping resources in an Application

Component

When the application is imported into AWS Resilience Hub along with its resources, AWS Resilience Hub
makes its best effort to group related resources into the same AppComponent when you
import your application, but the grouping might not always be 100 percent accurate. Some
resources are blocked for manual grouping and will be grouped automatically when
applicable because these services have strict dependencies that require specific
grouping configurations. For a complete list of services that are blocked for manual
grouping, see [Blocked services for manual
grouping](blocked-services-for-manual-grouping.md "blocked-services-for-manual-grouping.md").

AWS Resilience Hub performs the following activities after your application and its resources
are successfully imported:

- Scans your resources to check if they can be re-grouped into new AppComponents
  to improve the assessment accuracy.
- If AWS Resilience Hub identifies resources that can be re-grouped into new
  AppComponents, it displays the same as recommendations and allows you to either
  accept or reject the same. In AWS Resilience Hub, the confidence level assigned to a
  grouping recommendation indicates the degree of certainty with which the
  resources should be grouped together based on their attributes and metadata. A
  **High** confidence level indicates that AWS Resilience Hub has a
  confidence level of 90% or above that the resources in that group are related
  and should be grouped together. A **Medium** confidence level
  indicates that AWS Resilience Hub has a confidence level between 70% and 90% that the
  resources in that group are related and should be grouped together.

###### Note

AWS Resilience Hub requires the correct grouping so that it can compute estimated
workload RTO and estimated workload RPO to generate recommendations.

The following are examples of correct groupings:

- Group primary databases and replicas under a single AppComponent.
- Group Amazon EC2 instances that run the same application under a single
  AppComponent.
- Group Amazon ECS services in one Region and failover Amazon ECS services in another
  Region under a single AppComponent.
  For more information about reviewing and including resource grouping recommendations
  by AWS Resilience Hub, see the following topics:

- [AWS Resilience Hub resource grouping
  recommendations](grouping-recommendation.md "grouping-recommendation.md")
- [Manually grouping resources into an
  AppComponent](AppComponent-manual-grouping.md "AppComponent-manual-grouping.md")
