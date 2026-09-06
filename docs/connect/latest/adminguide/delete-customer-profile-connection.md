

# Delete Customer Profiles or stop integrations
<a name="delete-customer-profile-connection"></a>

**Note**  
Deleting mappings will only delete objects and data associated with that specific mapping. If there are multiple objects associated with a profile, then deleting a specific mapping might not clear the profile data. If you want to delete specific data, then you would delete the mapping, but your profiles might still exist if they contain data from other mappings. This could result in additional charges for the existing profiles. You can delete a domain and all data from Customer Profiles, including all profiles, by using the [Connect Customer console](delete-customer-profiles-domain.md) or the [DeleteDomain](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_DeleteDomain.html) API.

**Console method**
+ If at any time you want to stop the ingestion of customer profile data, choose the integration/mapping and then choose **Delete**.
+ To delete the integrations, customer profiles, and all the customer profile data, you can delete your customer profiles domain in the Connect Customer console. For more information, see [Delete a Connect Customer Customer Profiles domain](delete-customer-profiles-domain.md).

**API method**
+ To delete customer profiles data for a specific integration, use the `DeleteProfileObjectType` API.
+ To delete the integrations, customer profiles, and all the customer profile data, use the `DeleteDomain` API.

To re-enable the ingestion of customer profile data, go through the setup steps again. 