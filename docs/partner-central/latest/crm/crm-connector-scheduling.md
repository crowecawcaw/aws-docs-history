# Creating synchronization schedules

###### Note

The topics in this section assume you've completed the prerequisites for an AWS Partner Central integration, an AWS Marketplace integration, or both.
For more information, refer to [Integration prerequisites](crm-integration-setting-up.md "crm-integration-setting-up.md")
and [Getting started](crm-integration-getting-started.md "crm-integration-getting-started.md") earlier in this guide.

You can create inbound and outbound synchronization schedules between Salesforce and
AWS Partner Central. The steps in the following sections explain how.

###### Topics

- [Prerequisites](#scheduling-prerequisites "#scheduling-prerequisites")
- [Creating a schedule](#creating-a-schedule "#creating-a-schedule")
- [Deactivating a scheduled job](#deactivating-a-scheduled-job "#deactivating-a-scheduled-job")
- [Viewing all schedules](#viewing-all-schedules "#viewing-all-schedules")

## Prerequisites

Ensure that you complete the following before creating a synchronization schedule:

- [Map](crm-connector-mapping.md "crm-connector-mapping.md") all required fields on at least
  one object, opportunity, or lead.
- Create a [system integration user](#system-integration-user "#system-integration-user") in
  Salesforce.

### Creating a system integration user

Before you can create a synchronization schedule, you must use Salesforce to create
a system integration user with APN integration permissions. To create synchronization
schedules, you must sign in to Salesforce as the system integration user. Creating a
schedule without APN integration user permissions can break the APN integration.

###### To create a system integration user

1. Sign in to your Salesforce organization as a system administrator.
2. Create a user in your Salesforce organization. Assign a profile to the user with
   access to the required objects in your Salesforce organization. For more
   information, refer to [Add a
   single user](https://help.salesforce.com/s/articleView?id=sf.adding_new_users.htm "https://help.salesforce.com/s/articleView?id=sf.adding_new_users.htm").
3. Assign the user the **APN Integration User** permissions set.
   For more information, refer to [Assign permission set to users](https://help.salesforce.com/s/articleView?id=sf.assign_permission_set_to_user.htm "https://help.salesforce.com/s/articleView?id=sf.assign_permission_set_to_user.htm").

## Creating a schedule

After completing the [prerequisites](#scheduling-prerequisites "#scheduling-prerequisites"),
you can create synchronization schedules between Salesforce and APN.

###### To create a synchronization schedule with APN

1. Sign in to Salesforce as a user with system integration user permissions.
2. On the **Schedules** tab, choose **New**.
3. Choose the objects to schedule. You can set up schedules for leads and
   opportunities, or for a single object.
4. Choose the schedule frequency, from a minimum of every five minutes to a maximum
   of once a day.
5. Choose **Schedule**.

###### Note

- Only one schedule per object can be active at one time. Creating a new schedule
  for the same object deactivates the existing schedule.
- To disable the inbound integration when creating a schedule, choose
  **Disable Inbound Integration, Schedule**.
- Creating a schedule without APN integration user permissions can break the APN
  integration.

## Deactivating a scheduled job

1. On the **Scheduling** page, choose **Deactivate All
   Jobs** to turn off any active schedules.
2. Proceed through the confirmation screen to deactivate the synchronization
   schedule.

## Viewing all schedules

From the **Schedules** tab, use the list view filters to toggle
between **Active**, **Inactive**, and **All
synchronization** schedules.
