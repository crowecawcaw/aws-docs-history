# Managing Fleet Scaling Using the Amazon WorkSpaces Applications Console

You can set up and manage fleet scaling by using the WorkSpaces Applications console in either of the
following two ways: During fleet creation, or any time, by using the
**Fleets** tab. Two default scaling policies are associated with
newly created fleets after launch. You can edit these policies on the **Scaling
Policies** tab in the WorkSpaces Applications console. For more information, see [Create a Fleet in Amazon WorkSpaces Applications](set-up-stacks-fleets-create.md "set-up-stacks-fleets-create.md").

For user environments that vary in number, define scaling policies to control how
scaling responds to demand. If you expect a fixed number of users or have other reasons
for disabling scaling, you can set your fleet with a fixed number of instances ro user
sessions.

###### To set a fleet scaling policy using the console

1. Open the WorkSpaces Applications console at
   [https://console.aws.amazon.com/appstream2/home](https://console.aws.amazon.com/appstream2/home "https://console.aws.amazon.com/appstream2/home").
2. In the navigation pane, choose **Fleets**.
3. Select the fleet and then choose **Scaling Policies**.
4. Edit existing policies by choosing the edit icon next to each value. Set the
   desired values in the edit field and choose **Update**. The
   policy changes go into effect within a few minutes.
5. Add (create) new policies using the **Add Policy** link. Set
   the desired values in the edit field and choose **Create**. The
   new policy goes into effect within a few minutes.
   You can use the **Fleet Usage** tab to monitor the effects of your
   scaling policy changes. The following is an example usage graph of scaling activity when
   five users connect to the fleet and then disconnect. This example is from a fleet using
   the following scaling policy values:

- Minimum Capacity = 10
- Maximum Capacity = 50
- Scale Out = Add 5 instances (for single session fleets) or user sessions (for
  multi-session fleets) if Capacity Utilization > 75%
- Scale In = Remove 6 instances (for single session fleets) or user sessions
  (for multi-session fleets) if Capacity Utilization < 25%

###### Note

The above policy is applicable in both single-session and multi-session
scenarios. In a single session scenario, 5 new instances will be launched
during a scale out event, and 4 instances will be reclaimed during the scale
down event. In a multi-session scenario, with the maximum sessions per
instance = 4, the scale out event will trigger a launch of roundup (add 5
user sessions/ maximum sessions per instance 4) = 2 instances. During a
scale in event, services will reclaim roundup (remove 6 user
sessions/maximum sessions per instance 4) = 2 instances. Instances with
running user sessions will not be reclaimed. Only instances with no user
sessions running will be reclaimed.

###### To set a fixed capacity fleet using the console

1. Open the WorkSpaces Applications console at
   [https://console.aws.amazon.com/appstream2/home](https://console.aws.amazon.com/appstream2/home "https://console.aws.amazon.com/appstream2/home").
2. In the navigation pane, choose **Fleets**.
3. Select the fleet.
4. For **Scaling Policies**, remove all policies associated with
   the fleet.
5. For **Fleet Details**, edit the fleet to set
   **Desired Capacity**.
   The fixed fleet has constant capacity based on the value that you specified as
   **Desired Capacity**. Note that a fixed fleet has the desired
   number of instances available at all times and the fleet must be stopped to stop billing
   costs for that fleet.
