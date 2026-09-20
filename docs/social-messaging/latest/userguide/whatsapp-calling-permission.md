

# Check calling permission for a user
<a name="whatsapp-calling-permission"></a>

Before you call a user, check whether your business has permission to call them. Permission to call a user is granted by the user and is required by Meta. A permission can be permanent, or temporary with an expiration time. A user can also decline to grant permission. The permission status, the actions your business can take, and any limits on those actions are determined by Meta.

To check calling permission, use the `GetWhatsAppCallPermission` operation. Identify the user by their phone number, in E.164 format, or by their business-scoped user ID. The operation returns the current permission status, an optional expiration time for temporary permissions, and the list of calling actions that your business can take. It also returns any limits that apply to each action. A limit describes how many times an action is allowed within a time period. It also describes how much of that allowance you have used.

For more information about how call permission works and the values that Meta returns, see the [WhatsApp calling documentation](https://developers.facebook.com/docs/whatsapp/cloud-api/calling) from Meta.