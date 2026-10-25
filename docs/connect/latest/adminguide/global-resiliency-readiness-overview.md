

# View your resiliency readiness in Connect Customer Global Resiliency
<a name="global-resiliency-readiness-overview"></a>

Connect Customer Global Resiliency (ACGR) gives you a single view of your overall resiliency readiness status on the **Global Resiliency** page in the admin website. For example, you can confirm your instance is ready before a Region switch, so you can spot and resolve synchronization or configuration issues ahead of time.

## Enable the Global Resiliency permission
<a name="enable-global-resiliency-permission"></a>

To view this page, enable the **View** permission under **Global Resiliency** for the appropriate security profile.

1. Open the admin website at `https://{{instance_name}}.my.connect.aws/` using an Admin account.

1. On the navigation bar, choose **Security profiles**. On the **Manage security profiles** page, choose a security profile (for example, **Admin**), and then choose **Edit**.

1. On the **Edit security profile** page, choose **Global Resiliency - View**, and then choose **Save**.

![The Global Resiliency permission group in the Edit security profile page, with the View permission for the Failover Readiness Dashboard selected.](https://docs.aws.amazon.com/connect/latest/adminguide/images/acgr-readiness-security-profile-permission.png)


**Note**  
This permission applies only to instances that have Connect Customer Global Resiliency enabled.

After you enable the permission, a **Global Resiliency** option appears in the admin website navigation.

![The Global Resiliency option in the admin website navigation bar.](https://docs.aws.amazon.com/connect/latest/adminguide/images/acgr-readiness-navigation.png)


## Overall status widget
<a name="global-resiliency-overall-status"></a>

The **Overall status** widget summarizes the readiness of your ACGR instance as a single indicator. When there are no resource synchronization or configuration errors, it shows **Good**. When the service detects any configuration or synchronization errors, this changes to **Needs attention**. You can navigate to the Resource Synchronization widget to identify the Connect Customer resources that need you to take action.

**Note**  
The status shows **Checking status** while the service gathers details. It shows **Undetermined** when the service cannot fetch a response from a backend API call.

![The Overall status widget showing a Needs attention Global Resiliency readiness status, with source Region and replica Region details and their initial replication status.](https://docs.aws.amazon.com/connect/latest/adminguide/images/acgr-readiness-overall-status.png)


## Resource Synchronization
<a name="global-resiliency-resource-synchronization"></a>

Use the **Resource synchronization** widget to confirm which resources ACGR is replicating and which resource types are currently in sync. When a sync issue occurs, the widget shows the error. Choose **View details** to see the steps required to resolve it.

![The Resource Synchronization widget listing resource types such as Phone numbers, Agents, Hours of operation, and Queues, with their pending sync counts and sync status.](https://docs.aws.amazon.com/connect/latest/adminguide/images/acgr-readiness-resource-synchronization.png)


The **Pending sync** column shows how many resources are still waiting to replicate in each Region, shown as source/replica. A resource appears under the Region where it is still waiting to replicate. A resource you create or update in the source Region appears under the replica Region until Connect Customer finishes replicating the change. The reverse is true for a resource you create or update in the replica Region. For example, if the column shows 0/25, the source Region has 0 resources waiting and the replica Region has 25 resources to sync. Both Regions display the same value regardless of which Region you view the status in.

Most changes replicate within seconds, so this column typically reads 0/0. The count rises when you create or update a large number of resources at once. For example, creating a batch of queues in the source Region shows the pending count under the replica Region, and it decreases as Connect Customer works through the replication. A change that does not replicate on the first attempt is picked up on a following attempt. The replication service periodically checks whether the replication action is complete and completes it without any action from you. Allow up to 15 minutes for the column to reflect a change in either direction, both when a resource starts waiting and after you resolve an issue.

The **Sync status** section shows the error, and **View details** shows the specific configuration with the issue and the action you need to take. For example, the widget may surface phone numbers or users that are not associated with a traffic distribution group. In this case, choose **View details** for the resource type, then open the **Not assigned to Traffic Distribution Group** tab. Select the listed users and phone numbers, and associate them with a specific traffic distribution group. ACGR requires this association so that flows connect to phone numbers in the replica and agents can move across Regions during a Region switch.

The following table lists the error types that the Resource synchronization widget surfaces.


| Error type | Action needed | 
| --- | --- | 
| Duplicate resource name | Navigate to the Region listed in the Region to delete column. Use the List API to identify the resource with the duplicate name, then use the Delete API to delete the duplicate resource. After the resource is deleted, the ACGR replication service automatically syncs the resource. No additional action is needed. | 
| Validation constraints mismatch | Navigate to the User Management page on the admin website in the source or the replica instance, and update the Desk Phone Number to the correct format. No additional action is needed. | 
| Unassigned phone numbers | We recommend associating all phone numbers with a traffic distribution group (TDG). Choose View details on the Resource Synchronization tab to view the list of phone numbers that are associated with the instance, select all, and choose a TDG to associate the phone numbers. | 
| Unassigned users | Select the users listed in View details, and assign the users to a specific traffic distribution group. This allows users to move across Regions during a Region switch without manual action. | 
| Widget load issues | There was an issue rendering the resource synchronization information. Refresh the page. | 
| Resource replication available through ACGR, but not enabled in your instance | ACGR supports replication of this resource type, but it is not enabled for your instance. Contact AWS Support to enable replication. | 

**Note**  
The Resource synchronization widget refreshes automatically every 120 seconds.

Resource synchronization status is also available through the API. Use `ListReplicationFindings` to retrieve the synchronization status. For more information, see the [Connect Customer API Reference](https://docs.aws.amazon.com/connect/latest/APIReference/Welcome.html).

## Traffic Distribution Groups
<a name="global-resiliency-traffic-distribution-groups"></a>

The page includes a **Traffic Distribution Groups** widget that shows all traffic distribution group (TDG) configurations in your ACGR instance, alongside the current agent and telephony distribution status for each TDG. It also shows the last Region switch time so you can monitor your readiness cadence.

**Important**  
You cannot create or modify a traffic distribution group configuration in this widget. Update your traffic distribution group through the [UpdateTrafficDistribution](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateTrafficDistribution.html) API.

![The Traffic Distribution Groups widget showing TDG names, status, agent and telephony traffic distribution, sign-in and channels distribution, and the last failover time.](https://docs.aws.amazon.com/connect/latest/adminguide/images/acgr-readiness-traffic-distribution-groups.png)
