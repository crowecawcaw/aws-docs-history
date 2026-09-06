

# Managing a space
<a name="managing-spaces"></a>

You can perform the following actions for spaces.

**Topics**
+ [Viewing a list of spaces](#viewing-spaces)
+ [Editing a space](#editing-spaces)
+ [Adding knowledge to a space](#adding-resources-space)
+ [Viewing a list of content inside a space](#viewing-spaces-content)
+ [Using a space](#using-spaces)
+ [Sharing a space](#sharing-spaces)
+ [Deleting a space](#deleting-spaces)
+ [Removing knowledge from a space](#deleting-resources-space)
+ [Adding data from external sources into your space](#adding-external-data-sources)
+ [Adding application actions to a space](#adding-application-actions)

## Viewing a list of spaces
<a name="viewing-spaces"></a>

You can view a list of spaces created by—or shared with—you.

**To view a list of spaces**

1. Log in to the Amazon Quick console.

1. From the left navigation menu, select **Spaces**.

   You will see a list of spaces displayed. The list also displays the name, description, owner, and last modified date for each space. You can search for a space, and filter for recent spaces.

## Editing a space
<a name="editing-spaces"></a>

You can edit an Amazon Quick space. When you edit a space, you can perform the following actions:
+ Edit space description and space name
+ Add and delete any files and link or unlink any resources ( dashboards, topics, knowledge bases, and application actions) that you've added.

**To edit a space**

1. Log in to the Amazon Quick console.

1. From the left navigation menu, select **Spaces**.

1. In **Spaces**, select the space you want to edit.

1. Inside the space, do any of the following:

   1. To edit **Space name** or **Space description** , double click on the name or description field. Then, select the edit icon to update the description.

   1. In the **All knowledge** section, select **Add knowledge** to add new content.

   1. In **Amazon Quick resources** – Link and unlink resources as needed.

## Adding knowledge to a space
<a name="adding-resources-space"></a>

You can add knowledge—files and Amazon Quick resources—to a space after it's been created.

**To add knowledge to an existing space**

1. Log in to the Amazon Quick console.

1. From the left navigation menu, select **Spaces**, and then select your space from the list of spaces displayed.

1. Select **Add knowledge** to begin adding content to your space.

   From the dropdown menu, you can select from available resource types including **Dashboards**, **Topics**, **Knowledge bases**, **Actions**, and **File uploads**.
**Note**  
You can preview a resource before you choose to add it by clicking on its name. 

After you finish adding resources, **Space knowledge** displays a list of all resources and files added to your space.

## Viewing a list of content inside a space
<a name="viewing-spaces-content"></a>

You can view a list of content inside a space.

**To view a list of content within a space**

1. Log in to the Amazon Quick console.

1. From the left navigation menu, select **Spaces**.

1. Select the name of the space whose content you want to view from the list of spaces.

   On the space detail page, you will see the **Space knowledge** section displaying a list of files uploaded and resources linked to the space.

## Using a space
<a name="using-spaces"></a>

After you finish creating your space and adding knowledge to it, you can start interacting with it through agents. You can interact with an agent while in a space in the following ways:
+ Interact with a space using any agent
**Note**  
When you switch between spaces or open up a space during an on-going chat Amazon Quick detects your space and focuses your agent to it.
+ Interact with a specific knowledge source within a space using an agent

**To use an agent to chat with a space**

1. Log in to the Amazon Quick console.

1. Then, do one of the following:

   1. From the left navigation menu, select **Spaces**.

   1. In **Spaces**, select the space name.

   1. In the space that opens, start chatting with your data using the chat interface.

   1. Use the sparkle chat icon to open the chat interface.

   1. From the resource selector menu, select **All resources**, and then select **Choose a resource**.

   1. From the **Add a resource** menu, from **Spaces**, select the space you want to chat with. Then, start chatting.

## Sharing a space
<a name="sharing-spaces"></a>

You can share a space with any other Amazon Quick user. When you share a space with a user, you must also choose the permission levels that user has to the space—whether owner or viewer.

**To share a space**

1. Log in to the Amazon Quick console.

1. From the left navigation menu, select **Spaces**, and select the name of the space you want to share. The space should open.

1. From the top right corner of your space menu, select **Share**

1. In the **Share space** modal that opens, add the users and groups you want. Choose the permissions type for each user and group you add.

**Note**  
You can also share a space from the space home page. Locate the space you want to share, select the menu icon in the **Actions**, and then select **Share**. In the **Share space** modal that opens, add users and groups and set their permissions.

## Deleting a space
<a name="deleting-spaces"></a>

You can delete a Amazon Quick space. Deleting a space deletes all files associated with the space. Deleting a space unlinks assets associated with the space without deleting the assets. You can only delete a space you own.

**To delete a space**

1. Log in to the Amazon Quick console.

1. From the left navigation menu, select **Spaces**, and select the name of the space you want to share. The space should open.

1. From the top right corner of your space menu, select **Delete**, and then select **Delete** from the modal that opens.

**Note**  
You can also delete a space from the space home page. Locate the space you want to delete, select the menu icon in the **Actions**, and then select **Delete**. In the **Delete space** modal that opens, select **Delete**.

## Removing knowledge from a space
<a name="deleting-resources-space"></a>

You can remove knowledge (remove files and unlink assets) from a space. When you remove files, they are removed from the Amazon Quick index in which they are stored. When you remove an asset, it unlinks it from the space without deleting it from the Amazon Quick system.

**To remove knowledge from an existing space**

1. Log in to the Amazon Quick console.

1. From the left navigation menu, select **Spaces**, and then select your space from the list of spaces displayed.

1. In the **Space knowledge** section:

   1. In **Files uploaded** – From the **Actions** menu select **Delete**.

   1. In **Amazon Quick resources** – From the **Actions** menu select **Remove from this space**.

## Adding data from external sources into your space
<a name="adding-external-data-sources"></a>

You can pull in data from Google Drive, OneDrive, Confluence, SharePoint, web pages, and Amazon S3 into your spaces to expand the context of your chat and research agents.

**To add data from external sources**

1. Create a space and give it a name.

1. Select the **Knowledge bases** section in the space knowledge list.

1. Select **Add knowledge bases**.

1. In **All knowledge bases** you will see application data integrations that were created for you by others in your organization. You can select one to pull into your space, or create a new one.
**Note**  
To learn how to create a knowledge base, refer to [Working with integrations](https://docs.aws.amazon.com/quicksuite/latest/userguide/working-with-integrations.html).

## Adding application actions to a space
<a name="adding-application-actions"></a>

You can use application actions to read and write data to external SaaS applications and MCP servers from within a space. When you add actions to a space, only those actions will be considered when you select the space as your chat context.

**Note**  
Only authors can create connectors.

**To use actions in a space**

1. Create a space and give it a name.

1. Select the **Actions** section in the space knowledge list.

1. Select **Add action**.

1. Select **All actions**, and choose an action that others have created in your organization.

**Note**  
To learn how to create a connector, refer to [Working with integrations](https://docs.aws.amazon.com/quicksuite/latest/userguide/working-with-integrations.html).