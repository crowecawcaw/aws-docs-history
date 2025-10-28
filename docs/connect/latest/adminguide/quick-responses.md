# Add quick responses for use with chat and email contacts in

Amazon Connect

This topic explains how to add a quick response by using the Amazon Connect admin website. For the APIs used to
create and manage quick responses programmatically, see [APIs to create and manage quick responses](#apis-quick-responses "#apis-quick-responses").

###### To add responses

1. Log in to the Amazon Connect admin website at https://_instance
   name_.my.connect.aws/. Use an **Admin** account, or an
   account assigned to a security profile that has \*\*Content Management - Quick responses

- Create\*\* permission.

2. On the navigation bar, choose **Content
   Management**, then **Quick responses**.

![Menu showing "Content Management" and "Quick responses."](images/agent-application-1.png) 3. On the **Quick responses** page, choose **Add
response**.

###### Note

If the **Add response** button isn't available, sign in with an account
that has the admin security profile, or ask another admin for help. 4. On the **Add response** page, choose whether the response is for chat,
email, or both channels. 5. On the **Add response** page, enter a name, description, and shortcut key
for the quick response. You must enter a unique name and shortcut key because agents will
search on those values. 6. Open the **Routing profiles** list and select one or more profiles. You
can select a maximum of 20 profiles, or choose **All**. Only the agents
assigned to a given profile can see the quick responses associated with that profile. 7. (Optional) Choose **Activate: Make this response visible for agents** if
you want agents to see and search for the response. 8. In the **Content** section, enter the response, then choose
**Save**.

###### Note

If you configured user-defined attributes in the flow block, those attributes, such as
customer name, appear when an [agent searches for a response in
CCP](search-qr-ccp.md "search-qr-ccp.md"). For more information, see [Set contact
attributes](set-contact-attributes.md "set-contact-attributes.md").

## APIs to create and manage quick responses

Use the following APIs to create and manage quick responses programmatically:

- [CreateQuickResponse](../APIReference/API_amazon-q-connect_CreateQuickResponse.md "../APIReference/API_amazon-q-connect_CreateQuickResponse.md")
- [UpdateQuickResponse](../APIReference/API_amazon-q-connect_UpdateQuickResponse.md "../APIReference/API_amazon-q-connect_UpdateQuickResponse.md")
- [DeleteQuickResponse](../APIReference/API_amazon-q-connect_DeleteQuickResponse.md "../APIReference/API_amazon-q-connect_DeleteQuickResponse.md")
- [GetQuickResponse](../APIReference/API_amazon-q-connect_GetQuickResponse.md "../APIReference/API_amazon-q-connect_GetQuickResponse.md")
- [ListQuickResponses](../APIReference/API_amazon-q-connect_ListQuickResponses.md "../APIReference/API_amazon-q-connect_ListQuickResponses.md")
- [SearchQuickResponses](../APIReference/API_amazon-q-connect_SearchQuickResponses.md "../APIReference/API_amazon-q-connect_SearchQuickResponses.md")
- [UpdateQuickResponse](../APIReference/API_amazon-q-connect_UpdateQuickResponse.md "../APIReference/API_amazon-q-connect_UpdateQuickResponse.md")
