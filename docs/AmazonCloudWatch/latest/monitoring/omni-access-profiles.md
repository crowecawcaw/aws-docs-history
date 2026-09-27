

# Access profiles
<a name="omni-access-profiles"></a>

An access profile is an identity for a resource that acts when no one is signed in. An alert, for example, evaluates its query on a schedule. The profile holds the permissions the resource uses at that time.

A profile is reusable. You create it once, grant it permissions, and choose which resources may assume it, so several alerts can share one profile instead of each carrying a copy of the same permissions.

**Note**  
Access profiles and permission levels solve different problems. A permission level governs a **person** and applies wherever they work. A profile governs a **resource** acting on its own. See [Control access to your space](omni-control-access-to-your-space.md).

**What an access profile contains**

Every profile has two halves:


| Half | What it answers | 
| --- | --- | 
| Permissions | What this profile is allowed to do: the grants it holds, and the integrations it can invoke. | 
| Who can assume | Which principals are allowed to act as this profile. In the console, you choose alerts: either every alert in the space or specific ones. | 

Neither half works alone. A profile with permissions that nothing is allowed to assume cannot be used. A profile that resources can assume but that has no permissions authorizes nothing. The console catches this when you create an alert, but a profile that loses its permissions later fails without an error. See the "Alerts and profiles" section of this page.

A profile belongs to one space, and its name must be unique within that space.

**System managed access profiles**

Creating a space also creates one system managed access profile:


| Profile | Purpose | 
| --- | --- | 
| DefaultAccessProfileForAsyncWorkflows | The identity the Omni agent uses when it investigates a Slack mention and no one is signed in. Only the space's Omni agent can assume it. It starts with no permissions, so Slack mention investigations cannot read your data until you grant it Viewer access. See [Connect Slack](omni-connect-slack.md). | 

A system managed profile is created with the space and maintained by the service. You cannot rename, edit, or delete it. You can still grant it permissions, the same way you grant any profile. Profiles that you create are customer managed, and you control them fully.

Create a profile for the resources that need one, scoped to the job it does. For example, an alert that reads one service's telemetry and posts to one Slack channel gets a profile that can do only that.

**Create an access profile**

1. In the console, open **Settings**, and under **Space** choose **Access Profiles**.

1. Choose **Create profile**.

1. Enter a **Name**. This is what you select from later, so name it for the job it does, such as `Read-only observability`. Add an optional **Description** and **Tags**.

1. Under **Permissions**, leave **Allow alerts that use this profile to read telemetry and send notifications** selected to give the profile the actions that alert evaluation needs. Clear it to start with an empty profile and grant permissions yourself.

1. Under **Who can assume**, choose which alerts may act as this profile. **Allow all alerts** is selected by default. Clear it to pick specific alerts.

1. Choose **Create profile**.

The profile appears in the list with its name and description. To show its ID as well, use the column settings. Open it to see whether *you* can assume it: the detail page reports **You are allowed to assume this access profile** or **You are not allowed to assume this access profile**.

**Grant a profile its permissions**

The **Permissions** checkbox on the create form gives a new profile the actions that alert evaluation needs. The console creates this grant for you with exactly these actions:
+ Query session and results: `cloudwatch:StartTelemetryQuerySession`, `cloudwatch:ListTelemetryQuerySessions`, `cloudwatch:StopTelemetryQuerySession`, `cloudwatch:StopTelemetryQuery`, `cloudwatch:GetTelemetryQueryResults`
+ Telemetry reads: `cloudwatch:GetRecords`, `cloudwatch:GetMetricData`, `cloudwatch:ListMetrics`
+ Notifications: `cloudwatch:InvokeIntegration`

For what each action allows, see [Custom grant actions](omni-custom-grant-actions.md).

To grant anything beyond that, grant it the way you grant a person access: open the profile and choose **Add grant**, or on the **Manage permissions** page add the profile as you would a member. See [Manage space members and permissions](omni-manage-space-members-and-permissions.md).

A profile's detail page lists every grant it holds in the same grants table as the **Manage permissions** page, and marks the grants the service created as system managed. Those cannot be edited or deleted.

Alerts themselves hold only one kind of grant. When you add a grant for an alert, or for **ALL** alerts, the form locks the grant to the single `cloudwatch:AssumeAccessProfile` action and asks you to pick the access profile it applies to. All of the alert's other permissions come from the profile it assumes.

Two limits apply to whatever you grant:
+ **A profile cannot administer the space.** Space administration is reserved for people. A resource acting as a profile can never add members, change permissions, or manage profiles, no matter how it is granted.
+ **The Omni Space Access role is the ceiling.** A profile can hold only permissions that the role also holds, and it never adds to them. Both layers apply together, exactly as they do for a member's permission level. The role is created during setup (see [Set up Omni](omni-set-up-omni.md)) and its policies are described in [Identity and access management for CloudWatch Omni](omni-identity-and-access-management-for-cloudwatch-omni.md).

A profile can hold **Viewer**, **Editor**, or **Custom** grants. **Space Admin** is not offered for a profile.

**Alerts and profiles**

Every alert carries a profile. When you create an alert in the console, the **Access profile** field is preselected to the profile in your space with the most grants. Change it if the alert should run with narrower access. The query preview on the create form runs with your own access. When the alert runs, it reads with the profile's access, so results can differ.

An alert evaluates its query *as* its profile. If alerts cannot assume the profile, or the profile cannot read the data the query names, the alert is not created and the console offers a **Manage access profiles** link. This check runs only when you create or update the alert. If the profile later loses read access to the data the query uses, the alert returns no rows and reports **no data** rather than an error.

Two conditions must hold:
+ **Both you and the alert must be allowed to assume the profile.** Open the profile to check your own access. Its page reports whether you are allowed to assume it. Leaving **Allow all alerts** selected covers the alert side. If you narrowed a profile to specific alerts, a new alert is not among them until you add it.
+ **The profile must be able to read the telemetry.** A profile that can invoke integrations but cannot read your data delivers nothing. Leaving the **Permissions** checkbox selected when you create the profile covers the telemetry reads and the notification call.

If an alert has reported no data since you created it, check the profile before you check the query. See [Alerts](omni-alerts.md).

**Review and manage a profile**

Open a profile from the list to see:
+ **Whether you can assume it.** You need this to set the profile on an alert.
+ **Description** and **Tags**.
+ **Its grants.** Every grant the profile holds, in the same table as **Manage permissions**, with its name, ID, permission level, and whether it is system managed. Open a grant to read its JSON, edit it, or delete it. **Add grant** adds one. A system managed grant is read-only.

The profile page does not list who can assume it. To see or change which alerts, users, or groups may act as a profile, open **Manage permissions**, choose the principal (for alerts, the **ALL** row or a specific alert), and review its `cloudwatch:AssumeAccessProfile` grants there.

On the detail page, **Edit access profile** changes the profile's name, description, and tags. From the list, **Actions** offers **Edit** and **Delete**. Deleting a profile does not check whether alerts still use it. An alert whose profile is deleted can no longer evaluate, so move those alerts to another profile or delete them first. A system managed profile cannot be edited or deleted. If you need different permissions for it, add or remove its grants instead.

**Next steps**
+ To understand how access to a space works, see [Control access to your space](omni-control-access-to-your-space.md).
+ To add members and set their permission levels, see [Manage space members and permissions](omni-manage-space-members-and-permissions.md).
+ To create an alert that uses a profile, see [Alerts](omni-alerts.md).
+ To connect the integrations a profile can invoke, see [Connect Slack](omni-connect-slack.md).