

# End contacts from the Contact details page in Connect Customer
<a name="end-contacts-admin"></a>

On the **Contact details** page of an in-progress contact, you can end a contact. Ending a contact results in the contact being disconnected. If the contact was already connected to an agent, ending the contact starts After Contact Work (ACW) for the contact. 

To end contacts programmatically, use the [StopContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StopContact.html). 

## Important things to know
<a name="end-contacts-important"></a>
+ If you end a task contact after ACW is in progress, the contact is terminated. Voice and chat contacts that are in ACW state cannot be terminated by performing **End contact** action on the **Contact details** page.
+ You cannot end voice contacts when they are initiated using the following methods:
  + DISCONNECT
  + TRANSFER
  + QUEUE\_TRANSFER
+ You can end chat and task contacts regardless of how they were initiated.

## Required permissions
<a name="end-contacts-permissions"></a>

1. Enable one of the following permissions to view contacts on the **Contact search** and **Contact details** pages:

   1. **Contact search - View**: Allows a user to view all contacts. 

   1. **View my contacts - View**: Allows agents to view contacts that they themselves had handled.

1. **Restrict contact access** (Optional): Restrict a user's access to contacts on the **Contact search** and **Contact details** pages within their own hierarchy group or any hierarchy groups below them. For more information about these permissions, see [Manage who can search for contacts and access detailed information](contact-search.md#required-permissions-search-contacts).

1. **End Contact**: Enables a user to end contacts on the **Analytics & Optimization** pages. The following image shows the **Contact Actions - End contact** permission.  
![The end contact permission.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contact-details-contact-end-permissions.png)

## How to end an in-progress contact
<a name="howto-end-inprogress-contacts"></a>

1. Log in to Connect Customer with a user account that has [permissions to access contact records](contact-search.md#required-permissions-search-contacts). 

1. In Connect Customer choose **Analytics and optimization**, **Contact search**.

1. Select the **Contact status** filter and change the selected value to **In progress**. 

1. Choose an in-progress contact to view its details.

1. On the **Contact details** page choose **Actions**, **End**.  
![The contact details page, the end option.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contact-details-contact-end-action.png)

1. Confirm the action to end the contact by choosing **End**.

1. When the contact is ended successfully, the page automatically refreshes.