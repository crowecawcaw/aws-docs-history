# Managing resiliency policies

This section describes how to create resiliency policies for your applications. Setting
resiliency policies correctly enables you to understand your application's resiliency
posture. A resiliency policy contains information and objectives that you use to assess
whether your application is estimated to recover from a disruption type, such as software,
hardware, Availability Zone, or AWS Region. These policies do not change or affect an
actual application. Multiple applications can have the same resiliency policy.

When you create a resiliency policy, you define the target objectives: recovery time
objective (RTO) and recovery point objective (RPO). The objectives determine whether the
application meets the resiliency policy. Attach the policy to your application and run a
resiliency assessment. You can create different policies for the different types of
applications in your portfolio. For example, a real-time trading application would have a
different resiliency policy than a monthly reporting application.

###### Note

AWS Resilience Hub allows you to enter a value zero in the **RTO** and
**RPO** fields of your resiliency policy. But, while assessing your
application, the lowest possible assessment result is near zero. Hence, if you enter a
value zero in the **RTO** and **RPO** fields, the
estimated workload RTO and estimated workload RPO result will be near zero and the
**Compliance status** for your application will be set to
**Policy breached**.

The assessment evaluates your application configuration against the attached resiliency
policy. At the end of the process, AWS Resilience Hub provides an assessment of how your application
measures against the recovery targets in your resiliency policy.

You can create resiliency policies in Applications, and also in Resiliency policies. You
can access relevant details about your policies, and also modify and delete them.

AWS Resilience Hub uses your RTO and RPO targets to measure resiliency for these potential types of
disruptions:

- **Application** – Loss of a required software service
  or process.
- **Cloud infrastructure** – Loss of hardware, such as
  EC2 instances.
- **Cloud infrastructure Availability Zone (AZ)** – One
  or more Availability Zones are unavailable.
- **Cloud infrastructure Region** – One or more Regions
  are unavailable.
  AWS Resilience Hub enables you to create customized resiliency policies or use our recommended,
  open standard resiliency policies. When you create customized policies, name and describe
  your policy and choose the appropriate level or tier that defines your policy. These tiers
  include: Foundational IT core services, Mission critical, Critical, Important, and
  Non-critical.

Choose the tier that is appropriate for your class of application. For example, you might
classify a real-time trading system as critical, while you might classify a monthly
reporting application as non-critical. When you use our standard policies, you can choose a
resiliency policy with a preconfigured tier and values for the RTO and RPO targets by
disruption type. If necessary, you can change the tier and the RTO and RPO targets.

You can create resiliency policies in Resiliency policies, or when you describe a new
application.

## Accessing resiliency policy details

When you open a resiliency policy, you see important details about the policy. You can
also edit or delete the resiliency.

Resiliency policy details consist of two major views: **Summary** and **Tags**.

**Summary**

_Basic information_

Provides the following information about resiliency policy: Name, Description, Tier,
Cost Tier, and Date Created.

_Estimated workload RTO and estimated workload
RPO_

Shows the estimated workload RTO and estimated workload RPO disruption type associated
with this resiliency policy.

**Tags**

Use this view to manage, add, and delete tags internal to this application.

###### To edit resiliency policies in Resiliency policy details

1. In the left navigation menu, choose **Policies**.
2. In **Resiliency policies**, open a resiliency
   policy.
3. Choose **Edit**. Enter appropriate changes in
   **Basic Info**, and **RTO** and **RPO** fields. Then choose
   **Save changes**.

###### To edit resiliency policies in Resiliency policy

1. In the left navigation menu, choose **Policies**.
2. In **Resiliency policies**, choose a resiliency
   policy.
3. Choose **Actions**, and then select **Edit**.
4. Enter appropriate changes in **Basic Info**, and
   **RTO** and **RPO** fields. Then choose **Save
   changes**.

###### To delete resiliency policies in Resiliency policy details

1. In the left navigation menu, choose **Policies**.
2. In **Resiliency policies**, open a resiliency
   policy.
3. Choose **Delete**. Confirm your deletion, and
   then choose **Delete**.

###### To delete resiliency policies in Resiliency policy

1. In the left navigation menu, choose **Policies**.
2. In **Resiliency policies**, choose a resiliency
   policy.
3. Choose **Actions**, and then select **Delete**.
4. Confirm your deletion, and then choose **Delete**.
