#  View an AWS Cloud WAN core network policy change set

View proposed changes to a policy before deploying those changes to become the new
 live policy.

A policy version is never implemented automatically. After creating a version of a
 policy, you can implement the policy version as your new **LIVE**
 policy.

###### To view a core policy version change set

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Core network**, and then
 choose **Policy versions**.
5. In the **Policy versions section**, choose the check box that
 you want to see policy changes for.
6. Choose **View or apply change set**. This creates a new
 version of the policy. The policy version is incremented by one from the last
 policy version.
7. The **Change set** page displays the
 **Type** of change being affected, for example, a core
 network segment, and the **Action** that's associated with that
 type, for example, adding a new segment.
8. In **New Values** and **Previous values**,
 choose **Details** to view the change in a JSON format.
9. In the **Compare** column, choose
 **Compare** to view a line-by-line comparison of the
 current live policy with the proposed policy change.
