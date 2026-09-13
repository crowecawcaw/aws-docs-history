

# Edit users in bulk in Amazon Connect Customer
<a name="edit-users-in-bulk"></a>

With bulk edit mode, you can quickly edit the attributes that are common across user records, such as routing profiles, security profiles, and tags.

**Tip**  
Although the service is processing a batch of bulk edits, you can continue working on the **User management** page, such as selecting more records to edit or delete, in bulk or individually. This is useful for quickly updating settings, such as routing profiles for groups of agents.

1. Sign in to Connect Customer with an Admin account, or an account assigned to a security profile that has **Users - Edit** permission.

1. In Connect Customer, on the left navigation menu, choose **Users**.

1. Select users from the table. You can select users in the following ways:
   + Select individual rows by choosing the checkbox next to each user. This adds to your existing selections.
   + Select all users on the current page by choosing the checkbox in the table header. This adds to your existing selections.
   + Select all users that match your search, regardless of page, by choosing **Select all**. Connect Customer asks you to confirm, and lists the applied filters. Depending on how many users match, you might experience a delay.  
![The Select all users dialog, showing the applied filters and the Start over and Add to previous buttons.](https://docs.aws.amazon.com/connect/latest/adminguide/images/user-cloudscape-selectall-confirmation.png)

   Your earlier selection might not be visible on the page — for example, after you save a bulk change, change your filters, or visit a user's detail page. In this case, Connect Customer asks what to do with it the next time you add users. Choose **Add to previous** to keep the earlier selection, or **Start over** to keep only your new selection. Choosing **Select all** when users are already selected offers these same two options.

   To manage your selections, choose **Actions**. From there you can add or remove users, or clear all selections. Your selections persist until you refresh the page.  
![The Actions dropdown showing selection management options.](https://docs.aws.amazon.com/connect/latest/adminguide/images/user-cloudscape-bulk-selection.png)
**Large selections**  
For large selections, work in batches to keep your browser running smoothly.
**Tip**  
To stop being asked to confirm each selection and each bulk save, see [Turn confirmation prompts on or off](#bulk-edit-confirmations).

1. Choose the **Actions** dropdown, and then choose the attribute you want to edit. You can edit the following attributes in bulk:
   + Routing profile
   + Security profiles
   + Phone configuration
   + Hierarchy
   + Tags
   + Contact handling
   + Proficiencies  
![The User management page with users selected and the Actions dropdown showing bulk edit options.](https://docs.aws.amazon.com/connect/latest/adminguide/images/user-cloudscape-bulk-actions.png)

1. Depending on the attribute, the edit experience differs:
   + **Replace settings**: For routing profile, security profile, and hierarchy, the new value replaces the previous settings. For more information, see [Replace settings](#bulk-edit-replace).
   + **Partial updates**: For proficiencies, contact handling, tags, and phone configuration, you can add, remove, or modify individual settings. For more information, see [Partial updates](#bulk-edit-partial).

1. Fill out the form. A banner tells you how many users the change applies to, and reports any selected users that it excludes because of access restrictions. Check the count, select **I understand and want to continue with these changes**, and then choose **Save**.
**Note**  
If the number of users changes before you save, the checkbox clears. Select it again to continue.

1. Although the batch update is running, you can continue working on the **User management** page, performing other create, edit, and delete tasks on user records.

## Replace settings
<a name="bulk-edit-replace"></a>

For routing profile, security profile, and hierarchy, the new value replaces the previous settings for all selected users.

The following image shows an example of bulk editing routing profiles.

![Acknowledgment checkbox and user-count banner in the Edit routing profile dialog.](https://docs.aws.amazon.com/connect/latest/adminguide/images/user-cloudscape-bulk-routing-profile-with-ack.png)


## Partial updates
<a name="bulk-edit-partial"></a>

For proficiencies, contact handling, tags, and phone configuration, you can choose whether to add, remove, or modify individual settings rather than replacing all values.

### Bulk edit proficiencies
<a name="bulk-edit-proficiencies"></a>

When you choose **Proficiencies** from the **Actions** dropdown, you can use two modes: Add or Remove.

For each mode, specify the attribute name and value from the predefined attributes configured for your instance (for example, `connect:AssignmentType`).

#### Add proficiencies
<a name="bulk-proficiencies-add"></a>

Use **Add** to add proficiency attributes to the selected users. If a user already has the attribute, the service updates the proficiency level to the new value.

**Tip**  
To set hundreds of proficiencies at once, use the CSV import and export options. Export saves proficiency settings for reuse on other users or instances.

1. Choose the **Add** tile (chosen by default).

1. Choose an attribute name and value from the dropdowns, and set the proficiency level.  
![Acknowledgment checkbox and user-count banner on the bulk edit proficiencies page, with the Add/Update tile selected.](https://docs.aws.amazon.com/connect/latest/adminguide/images/user-cloudscape-bulk-proficiencies-add-with-ack.png)

1. Choose **Save**.

#### Remove proficiencies
<a name="bulk-proficiencies-remove"></a>

Use **Remove** to remove the specified proficiency attributes from the selected users.

1. Choose the **Remove** tile.

1. Choose the attribute name and value to remove.  
![Acknowledgment checkbox and user-count banner on the bulk edit proficiencies page, with the Remove tile selected.](https://docs.aws.amazon.com/connect/latest/adminguide/images/user-cloudscape-bulk-proficiencies-remove-with-ack.png)

1. Choose **Save**.

## Turn confirmation prompts on or off
<a name="bulk-edit-confirmations"></a>

Connect Customer asks you to confirm bulk selections and bulk changes. If you make many bulk changes in a session, you can turn these prompts off to save clicks.

1. On the **User management** page, choose the settings (gear) icon above the table.

1. In the **Preferences** dialog, set the following options:
   + **Selection confirmation**: Whether Connect Customer asks you to keep or replace an earlier selection when you add more users to it.
   + **Save confirmation**: Whether Connect Customer asks you to confirm how many users a bulk change applies to before it's saved.

   Each option has three settings:
   + **On**: Connect Customer always asks. This is the default.
   + **Paused**: Connect Customer stops asking until you reload the page.
   + **Off**: Connect Customer stops asking until you turn the option back on.
**Note**  
**Select all** always asks you to confirm, even when **Selection confirmation** is paused or off.  
![The Preferences dialog, with Selection confirmation and Save confirmation each set to On.](https://docs.aws.amazon.com/connect/latest/adminguide/images/user-cloudscape-table-preference.png)

1. Choose **Confirm**.

## View bulk edit activity
<a name="bulk-edit-activity"></a>

After you perform a bulk edit, a banner shows the operation progress. You can track the progress and results, and manage operations from this banner or from the **Activity** page.

1. To view operation details, choose **View results** in the bulk operation banner.  
![The bulk operation banner with the View results button.](https://docs.aws.amazon.com/connect/latest/adminguide/images/user-cloudscape-bulk-activity-step1.png)

1. In the table header, choose **Stop** to stop the entire bulk operation. To stop an individual operation, in that operation's row choose **Stop**. The following image shows the Stop controls in the table header and next to individual rows.  
![The Activity page with Stop controls in the table header and next to individual rows.](https://docs.aws.amazon.com/connect/latest/adminguide/images/user-cloudscape-bulk-activity-step2.png)

1. To resume a stopped operation, choose **Resume**. When you navigate away from the **User management** page, the session ends. After the session ends, you cannot retry or resume operations.
**Page refresh clears retry options**  
Row actions and retry actions are not available after a hard refresh of the page. Complete any retries before refreshing.  
![The Activity page showing the option to resume stopped operations.](https://docs.aws.amazon.com/connect/latest/adminguide/images/user-cloudscape-bulk-activity-step3.png)

1. You can reselect users from a previous bulk operation. From the **Select rows** dropdown, choose **All**, **Failed**, **Stopped**, or **Succeeded**.  
![The Activity page with the Select rows dropdown showing all, failed, stopped, and succeeded options.](https://docs.aws.amazon.com/connect/latest/adminguide/images/user-cloudscape-bulk-activity-step4.png)

1. To view past activities, choose the **Activity** button.  
![The User management page with the Activity button in the table header.](https://docs.aws.amazon.com/connect/latest/adminguide/images/user-cloudscape-bulk-activity-step5.png)

1. Your browser stores activity data locally for 7 days. Storing many activities can slow browser performance. To free up space, delete activities manually. Deleting activity records does not affect user data or revert any changes.  
![The Activity page showing the option to delete activities.](https://docs.aws.amazon.com/connect/latest/adminguide/images/user-cloudscape-bulk-activity-step6.png)

## Before selecting users for bulk editing
<a name="before-bulk-editing"></a>

Use the search and filter options on the **User management** page to narrow down the user list before selecting users for bulk editing. You can filter by properties such as routing profile, security profile, or proficiencies. By default, filters use **Match all** (AND operator) to show users that match every filter condition. For security profile and tags filters, you can choose **Match any** (OR operator) to show users that match at least one condition.

![The User management page showing the filter panel with proficiency filters using Match all.](https://docs.aws.amazon.com/connect/latest/adminguide/images/user-cloudscape-filter-proficiency-and.png)


![The User management page showing security profile filters using Match any.](https://docs.aws.amazon.com/connect/latest/adminguide/images/user-cloudscape-filter-sp-or.png)


## Edit user settings programmatically
<a name="bulk-edit-users-programmatically"></a>

You can change the following values programmatically across selected users. The users are changed to the same value.


| Property | API | CLI | 
| --- | --- | --- | 
| Routing profiles |  [UpdateUserRoutingProfile](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateUserRoutingProfile.html)  | [update-user-routing-profiles](https://docs.aws.amazon.com/cli/latest/reference/connect/update-user-routing-profiles.html) | 
| Security profiles |  [UpdateUserSecurityProfiles](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateUserSecurityProfiles.html)  | [update-user-security-profiles](https://docs.aws.amazon.com/cli/latest/reference/connect/update-user-security-profiles.html) | 
| Tags | [TagResource](https://docs.aws.amazon.com/connect/latest/APIReference/API_TagResource.html)<br />[UntagResource](https://docs.aws.amazon.com/connect/latest/APIReference/API_UntagResource.html) | [tag-resource](https://docs.aws.amazon.com/cli/latest/reference/connect/tag-resource.html)<br />[untag-resource](https://docs.aws.amazon.com/cli/latest/reference/connect/untag-resource.html) | 
| User hierarchies |  [UpdateUserHierarchy](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateUserHierarchy.html)  | [update-user-hierarchy](https://docs.aws.amazon.com/cli/latest/reference/connect/update-user-hierarchy.html) | 
| User configuration |  [UpdateUserConfig](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateUserConfig.html)  | [update-user-config](https://docs.aws.amazon.com/cli/latest/reference/connect/update-user-config.html) | 

You can edit the following identity and contact information programmatically for an individual user: first name, last name, email address, mobile number, secondary email address. Use the following API or CLI:


| Property | API | CLI | 
| --- | --- | --- | 
| Identify and contact information |  [UpdateUserIdentityInfo](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateUserIdentityInfo.html)  | [update-user-identity-info](https://docs.aws.amazon.com/cli/latest/reference/connect/update-user-identity-info.html) | 