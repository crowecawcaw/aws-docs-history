# Reviewing resiliency recommendations

Resiliency recommendations evaluate Application Components and recommend how to
optimize by estimated workload RTO and estimated workload RPO, costs, and minimal
changes.

With AWS Resilience Hub, you can optimize resiliency using one of the following recommended
options in **Why you should choose this
option**:

###### Note

- AWS Resilience Hub provides up to three AWS Resilience Hub recommended options.
- If you set Regional RTO and RPO targets, AWS Resilience Hub displays **Optimize for Region RTO/RPO** in the
  recommended options. If Regional RTO and RPO targets are not set,
  **Optimize for Availability Zone (AZ)
  RTO/RPO** is displayed. For more information about setting
  Regional RTO/RPO targets while creating resiliency policies, see [Creating resiliency policies](create-policy.md "create-policy.md") .
- Estimated workload RTO and estimated workload RPO values for the
  applications and their configurations are determined by considering the
  amount of data and individual AppComponents. However, these values are
  only estimates. You should use your own testing (such as AWS Fault Injection Service) to
  test your application for actual recovery times.
  **Optimize for Availability Zone RTO/RPO**

The lowest possible estimated workload recovery times (RTO/RPO) during an
Availability Zone (AZ) disruption. If your configuration can't be changed
sufficiently to meet the RTO and RPO targets, you're informed about the lowest
estimated workload AZ recovery times to get your configuration close to the
possibility of meeting the policy.

**Optimize for Region RTO/RPO**

The lowest possible estimated workload recovery times (RTO/RPO) during a Regional
disruption. If your configuration can't be changed sufficiently to meet the RTO and
RPO targets, you're informed about the lowest estimated workload Region recovery
times to get your configuration close to the possibility of meeting the
policy.

**Optimize for cost**

The lowest cost that you can incur and still meet your resiliency policy. If your
configuration can't be changed sufficiently to meet the optimization goals, you're
informed about the lowest cost that you can incur to get your configuration close to
the possibility of meeting the policy.

**Optimize for minimal changes**

The minimum changes required to achieve your policy targets. If your configuration
can't be changed sufficiently to meet the optimization goals, you're informed about
the recommended changes that can get your configuration close to the possibility of
meeting the policy.

The following items are included in the optimization category breakdowns:

- **Description**

Describes the configurations suggested by AWS Resilience Hub.

- **Changes**

A list of text changes that describe the necessary tasks to switch to the
suggested configuration.

- **Base cost**

The estimated cost associated with the recommended changes.

###### Note

**Base cost** can vary based on the usage and it does
not include any discounts or offers from Enterprise Discount Program
(EDP).

- **Estimated Workload RTO and RPO**

The estimated workload RTO and estimated workload RPO after
changes.
AWS Resilience Hub evaluates whether an Application Component (AppComponent) can comply with
a resiliency policy. If the AppComponent does not comply with a resiliency policy
and AWS Resilience Hub cannot make any recommendations to facilitate compliance, it might be
because the recovery time for the selected AppComponent cannot be met within the
constraints of the AppComponent. Examples of AppComponent constraints include
resource type, storage size, or resource configuration.

To facilitate the compliance of the AppComponent with the resiliency policy,
change the resource type of the AppComponent or update the resiliency policy to
align with what the resource can deliver.
