# Scaling Concepts for Amazon WorkSpaces Applications

WorkSpaces Applications scaling is provided by Application Auto Scaling. For more information, see the [Application Auto Scaling API Reference](../../../autoscaling/application/APIReference.md "../../../autoscaling/application/APIReference.md").

For step-by-step guidance for working with WorkSpaces Applications Fleet Auto Scaling, see [Scaling Your Desktop Application Streams with Amazon AppStream 2.0](https://aws.amazon.com/blogs/compute/scaling-your-desktop-application-streams-with-amazon-appstream-2-0/ "https://aws.amazon.com/blogs/compute/scaling-your-desktop-application-streams-with-amazon-appstream-2-0/") in the
_AWS Compute Blog_.

To use Fleet Auto Scaling effectively, you must understand the following terms and
concepts.

**Multi-session vs. Single-session**

In a single-session scenario, each user session has its own dedicated
instance. In a multi-session mode, more than one user session can be
provisioned on an instance. Fleet capacity and auto scaling policies must be
configured in terms of user sessions, and the service will calculate and
launch the required number of instances.

**Minimum Capacity/Minimum User Sessions for fleet**

The minimum number of instances (for single session fleets) or user
sessions (for multi-session fleets). The number of instances (for single
session fleets) or user sessions (for multi-session fleets) can't be below
this value, and scaling policies will not scale your fleet below this value.
For example, in a single-session scenario, if you set the minimum capacity
for a fleet to 2, your fleet will never have less than 2 instances.
Similarly, in a multi-session scenario, with the maximum number of sessions
on an instance set to 5, if you set the minimum capacity for a fleet to 12,
your fleet will never have less than roundup (12/5) = 3 instances.

**Maximum Capacity/Maximum User Sessions for fleet**

The maximum number of instances (for single session fleets) or user
sessions (for multi-session fleets). The number of instances (for single
session fleets) or user sessions (for multi-session fleets) can't be above
this value, and scaling policies will not scale your fleet above this value.
For example, in a single-session scenario, if you set the maximum capacity
for a fleet to 10, your fleet will never have more than 10 instances.
Similarly, in a multi-session scenario, with maximum number of sessions on
an instance set to 5, if you set the maximum capacity for a fleet to 52,
your fleet will never have more than roundup (52/5) = 11 instances.

**Desired Capacity**

The total number of instances (for single session fleets) or user sessions
(for multi-session fleets) that are either running or pending. This value
represents the total number of concurrent streaming sessions that your fleet
can support in a steady state. To set the value for **Desired
Capacity**, edit **Fleet Details**. We do not
recommend changing the **Desired Capacity** value manually
when you use **Scaling Policies**.

If the value of **Desired Capacity** is set below the
value of **Minimum Capacity** and a scale-out activity is
triggered, Application Auto Scaling scales the **Desired
Capacity** value up to the value of **Minimum
Capacity** and then continues to scale out as required, based
on the scaling policy. However, in this case, a scale-in activity does not
adjust **Desired Capacity**, because it is already below
the **Minimum Capacity** value.

If the value of **Desired Capacity** is set above the
value of **Maximum Capacity** and a scale-in activity is
triggered, Application Auto Scaling scales the **Desired
Capacity** value down to the value of **Maximum
Capacity** and then continues to scale in as required, based on
the scaling policy. However, in this case, a scale-out activity does not
adjust **Desired Capacity**, because it is already above
the **Maximum Capacity** value.

**Scaling Policy Action**

The action that scaling policies perform on your fleet when the
**Scaling Policy Condition** is met. You can choose an
action based on **% capacity** or **number of
instance(s)** (for single session fleets) or **user
sessions** (for multi-session fleets). For example, if
**Current Capacity** is 4 and **Scaling Policy
Action** is set to "Add 25% capacity", **Desired
Capacity** is increased will be set to 5 when **Scaling
Policy Condition** is met.

**Scaling Policy Condition**

The condition that triggers the action set in **Scaling Policy
Action**. This condition includes a scaling policy metric, a
comparison operator, and a threshold. For example, to scale a fleet if the
utilization of the fleet is greater than 50%, your scaling policy condition
should be "If Capacity Utilization > 50%".

**Scaling Policy Metric**

Your scaling policy is based on this metric. The following metrics are
available for scaling policies:

**Capacity Utilization**

The percentage of instances in a fleet that are being used.
You can use this metric to scale your fleet based on usage of
the fleet. For example, **Scaling Policy
Condition**: "If Capacity Utilization < 25%"
perform **Scaling Policy Action**: "Remove 25 %
capacity".

**Available Capacity**

The number of instances (for single session fleets) or user
sessions (for multi-session fleets) in your fleet that are
available for users. You can use this metric to maintain a
buffer in your capacity available for users to start streaming
sessions. For example, **Scaling Policy
Condition**: "If Available Capacity < 5" perform
**Scaling Policy Action**: "Add 5
instance(s) (for single session fleets) or user session(s) (for
multi-session fleets)".

**Insufficient Capacity Error**

The number of session requests rejected due to lack of
capacity. You can use this metric to provision new instances for
users who can't start streaming sessions due to lack of
capacity. For example, **Scaling Policy
Condition**: "If Insufficient Capacity Error >
0" perform **Scaling Policy Action**: "Add 1
instance(s) (fr single session fleets) or user session(s) (for
multi-session fleets)".
