

# Force agent logout

You can use Force agent logout to sign out agents directly from the [Queue and agent performance dashboard](queue-performance-dashboard.md). This is useful when agents forget to sign out at the end of their shift or become unresponsive.

## Prerequisites
<a name="force-agent-logout-prerequisites"></a>

Before you can sign out agents from the dashboard, complete the following steps:
+ Ensure you have the **Analytics and Optimization**, **Force Logout** permission enabled in your security profile. For more information, see [Analytics and Optimization](security-profile-list.md#analytics-list).
+ Ensure you have access to dashboards. For more information, see [Get started](dashboards.md#how-to-access-dashboards).

## Sign out an agent from the dashboard
<a name="sign-out-agent-from-dashboard"></a>

**Irreversible action**  
Signing out an agent ends the agent's session entirely. The agent is removed from all queues and is no longer tracked as an active agent.

1. Open the **Queue and agent performance** dashboard.

1. Navigate to the **Current agent performance** widget. Ensure the widget is grouped by agent.

1. Locate the agent you want to sign out. Choose the three-dot menu next to the agent's name, and then choose **Sign out**.

1. Review the confirmation dialog, which shows the agent's current activity.

1. Choose **Sign out** to confirm, or choose **Cancel**.

1. Review the result:
   + If the sign-out succeeds, a success banner displays on the widget and dismisses automatically after five seconds.
   + If the sign-out fails, an error banner displays on the widget. Try the operation again.

## Things to know
<a name="force-agent-logout-things-to-know"></a>
+ You cannot sign out an agent who is currently handling an active contact.
+ After a successful sign-out, an agent with no active sessions is removed from the widget in near real time.
+ Users with the **Analytics and Optimization** - **Force Logout** permission still see Offline agents on the dashboard, so they can sign those agents out.
+ When an agent logs in and stays Offline, the **Agent duration** metric shows the time since their last login until they change their status in the Contact Control Panel (CCP).
+ For Connect Customer Global Resiliency (ACGR) without global routing, the sign-out applies to the current Region only and does not carry over to the other Region, the same as other dashboard actions which are Regional. With ACGR with global routing, the agent is signed out of both Regions.