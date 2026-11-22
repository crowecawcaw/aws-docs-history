

# Proactive troubleshooting for your WorkSpaces users (Preview)

**Important**  
Proactive troubleshooting for your WorkSpaces users is in preview release and is subject to change.

Proactive troubleshooting for your WorkSpaces users helps your users resolve common problems with their WorkSpaces sessions themselves, so they don't need to contact you for problems they can fix. WorkSpaces Advisor monitors each user's session in the WorkSpaces client: before they connect, while they're connected, and after a disconnect. When it detects a problem, it shows the user a plain-language explanation of the likely cause and what to do next. When the fix is outside the user's control, Advisor tells the user to contact you and gives them the problem and the likely cause to share, so you start from a diagnosis instead of a symptom.

**Note**  
You control this capability for each directory with the End User Advisor self-service permission. It's turned on by default.

During preview, this capability is available in the AWS Regions that support WorkSpaces Personal, except the AWS GovCloud (US) Regions, the China Regions, and the Saudi Arabia Region. There's no additional charge for it during preview.

## What your users see in the WorkSpaces client
<a name="workspaces-advisor-users-client"></a>

Your users see Advisor when End User Advisor is turned on for their directory and they use a supported client. Advisor shows the health of the user's session, so the user can tell whether the session is working normally, whether there's a problem that might affect it, or whether there's a problem affecting it now.

When there's a problem, Advisor shows the user a recommendation with:
+ **What's happening**: a short description of the problem
+ **What to do**: the recommended next step
+ **Why**: the likely cause, such as the user's computer, their network, or the WorkSpace

### Before the user connects
<a name="workspaces-advisor-users-before"></a>

Advisor explains problems that stop a user from connecting, such as:
+ A registration code that isn't valid
+ Sign-in problems, such as an incomplete single sign-on or a computer that isn't approved for your organization
+ A WorkSpace that's unavailable, for example during maintenance
+ A session that's taking longer than usual to start, for example because the WorkSpace is starting
+ A network that's offline or blocking the connection

### During a session
<a name="workspaces-advisor-users-during"></a>

If a session freezes or becomes slow, Advisor identifies whether the likely cause is the user's computer, their network, or the WorkSpace, and recommends a next step. For example:
+ The user's computer: high CPU or memory use. Advisor suggests closing apps and browser tabs the user doesn't need.
+ The network: a slow or unstable connection. Advisor suggests moving closer to the router or using a wired connection.
+ The WorkSpace: high CPU or memory use on the WorkSpace. Advisor names the apps using the most resources and suggests closing the ones the user doesn't need, restarting the WorkSpace, or changing its compute type.

### After a disconnect
<a name="workspaces-advisor-users-after"></a>

Advisor tells the user why the session ended, for example because they were inactive, the session was opened from another device, or the network disconnected, and how to reconnect.

### When a user needs your help
<a name="workspaces-advisor-users-help"></a>

Some problems need you to act, such as a computer that isn't approved for your organization or a WorkSpace that's unavailable. Advisor tells the user to contact you and shows them the problem and the likely cause, so they can include both in their request.

## Actions your users can take
<a name="workspaces-advisor-users-actions"></a>

Advisor recommends actions, and users decide whether to take them. Some recommendations let users restart the client directly. Where a recommended next step is a self-service action you've enabled for the directory, such as restarting their WorkSpace or changing its compute type or increasing its volume size, users can take it from the client. Users can't take self-service actions you haven't enabled.

For more information, see [Enable self-service WorkSpaces management capabilities for your users in WorkSpaces Personal](enable-user-self-service-workspace-management.md).

## Supported clients
<a name="workspaces-advisor-users-clients"></a>

Amazon WorkSpaces client for Windows, version 5.37 and later, with the new client experience.

## Turn End User Advisor on or off for a directory
<a name="workspaces-advisor-users-turn-on-off"></a>

End User Advisor is turned on by default for every directory. The setting applies to every WorkSpace and user registered to the directory. When you turn it off, your users don't see Advisor in the client. A change takes effect the next time a user connects; sessions already in progress aren't affected.

**To turn End User Advisor on or off (console)**

1. Open the [Amazon WorkSpaces console](https://console.aws.amazon.com/workspaces/v2/home).

1. In the navigation pane, choose **Directories**.

1. Choose the directory.

1. In the **Self-service permissions** section, choose **Edit**.

1. Select or clear **End User Advisor**.

1. Choose **Save**.

The **End User Advisor** column in the **Self-service permissions** section shows **Enabled** or **Disabled** for the directory.

To turn End User Advisor off (AWS CLI), run the following command:

```bash
aws workspaces modify-selfservice-permissions \
    --resource-id d-1234567890 \
    --selfservice-permissions EnableEndUserAdvisor=DISABLED
```

To turn it back on, set `EnableEndUserAdvisor=ENABLED`.

The setting applies to the whole directory. You can't turn it on or off for individual users, WorkSpaces, or bundles, and you can't choose which checks run.

## Preview limitations
<a name="workspaces-advisor-users-limits"></a>
+ Advisor shows recommendations in the WorkSpaces client only. It doesn't notify you when a user sees a recommendation.
+ Advisor recommends actions; users take them, either directly in the client or with the self-service actions you've enabled.
+ Recommendations are available in English, French, German, Italian, Japanese, Korean, Portuguese (Brazil), Spanish, Chinese (Simplified), and Chinese (Traditional).

For what data this capability uses, why, and how it's protected, see [Security for proactive troubleshooting for your WorkSpaces users](workspaces-advisor-security.md#workspaces-advisor-security-users).