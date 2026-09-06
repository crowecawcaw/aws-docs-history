

# Update the task template on an in-progress contact in Connect Customer
<a name="update-template-contacts-admin"></a>

On the **Contact details** page of an in-progress task contact that is not assigned to an agent, you can update the task template associated with the contact. This is useful when a task was created without a template, or when the task needs a different template to represent updated task data.

To update the task template programmatically, use the [UpdateContactTaskTemplate](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateContactTaskTemplate.html) operation.

## Required permissions
<a name="update-template-contacts-permissions"></a>

1. Enable one of the following permissions to view contacts on the **Contact search** and **Contact details** pages:

   1. **Contact search - View**: Allows a user to view all contacts 

   1. **View my contacts - View**: Allows agents to view contacts that they themselves had handled

1. **Restrict contact access** (Optional): Restrict a user's access to contacts on the **Contact search** and **Contact details** pages within their own hierarchy group or any hierarchy groups below them. For more information about this permission, see [Manage who can search for contacts and access detailed information](contact-search.md#required-permissions-search-contacts).

1. **Update task template on contact**: Enables a user to update the task template on contacts from the **Contact details** page. The following image shows the **Contact Actions - Update task template on contact** permission.  
![The security profile permissions page, the Contact Actions section with Update task template on contact permission.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contact-details-update-template-permissions.png)

## How to update template on a task contact
<a name="howto-update-template-inprogress-contacts"></a>

1. Log in to Connect Customer with a user account that has [permissions to access contact records](contact-search.md#required-permissions-search-contacts).

1. In Connect Customer choose **Analytics and optimization**, **Contact search**.

1. Search for an in-progress task contact to update the template:

   1. Select the **Contact status** filter and set it to **In progress**, as shown in the following image.   
![The Contact search page, task filter, contact status filter.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contact-details-contact-transfer-filters.png)

   1. Set the **Channel** filter to **Tasks** to view only task contacts.

   1. Choose the task contact to view its details.

1. On the **Contact details** page for the task contact, choose **Actions**, **Update Template**.  
![The Contact details page, the Actions menu with Update Template option.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contact-details-update-template-action.png)

1. When the task template updates successfully, the page automatically refreshes to display the current task template in use.