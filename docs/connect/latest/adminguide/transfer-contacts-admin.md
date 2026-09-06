

# Transfer in progress contacts to a quick connect agent or a queue in Connect Customer
<a name="transfer-contacts-admin"></a>

On the **Contact details** page of an in-progress contact, you can transfer a contact to a quick connect agent or queue. This capability supports task, email, or chat contacts.

To transfer contacts programmatically, use the [TransferContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_TransferContact.html).

## Required permissions
<a name="transfer-contacts-permissions"></a>

1. Enable one of the following permissions to view contacts on the **Contact search** and **Contact details** pages:

   1. **Contact search - View**: Allows a user to view all contacts 

   1. **View my contacts - View**: Allows agents to view contacts that they themselves had handled

1. **Restrict contact access** (Optional): Restrict a user's access to contacts on the **Contact search** and **Contact details** pages within their own hierarchy group or any hierarchy groups below them. For more information about these permissions, see [Manage who can search for contacts and access detailed information](contact-search.md#required-permissions-search-contacts).

1. **Transfer Contact**: Enables a user to transfer contacts on the **Analytics & Optimization** pages. The following image shows the **Contact Actions - Transfer Contact** permission.  
![The Contact details page, contact transferred successfully.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contact-details-contact-transfer-permissions.png)

## How to transfer a task, email, or chat contact
<a name="howto-transfer-inprogress-contacts"></a>

1. Log in to Connect Customer with a user account that has [permissions to access contact records](contact-search.md#required-permissions-search-contacts).

1. In Connect Customer choose **Analytics and optimization**, **Contact search**.

1. Search for an in-progress task or email contact to transfer:

   1. Select the **Contact status** filter and set it to **In progress**, as shown in the following image.   
![The Contact search page, task filter, contact status filter.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contact-details-contact-transfer-filters.png)

   1. Set the **Channel** filter to **Tasks**, **Email**, or **Chat** to view only task, email, or chat contacts. 

   1. Choose the task, email, or chat contact to view its details.

1. On the **Contact details** page for the task, email, or chat contact, choose **Actions**, **Transfer**.  
![The Contact details page, contact transferred successfully.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contact-details-contact-transfer-action.png)

1. Select an agent or queue from a list of your quick connects and choose **Transfer**.

1. When the contact is transferred successfully, the page automatically refreshes with the **Next contact** link to the contact created as a result of the transfer. The following image shows the location of the **Next contact** link.  
![The Contact details page, contact transferred successfully.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contact-details-contact-transferred.png)