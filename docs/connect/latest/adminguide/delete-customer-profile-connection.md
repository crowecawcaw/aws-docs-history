# Delete Customer Profiles or stop

integrations

###### Note

Deleting mappings will only delete objects and data associated with that
specific mapping. If there are multiple objects associated with a profile, then
deleting a specific mapping may not clear the profile data. If you want to
delete specific data, then you would delete the mapping, but your profiles may
still exist if they contain data from other mappings. This could result in
additional charges for the existing profiles. You can delete a domain and all
data from Customer Profiles, including all profiles, by using the [Amazon Connect console](delete-customer-profiles-domain.md "delete-customer-profiles-domain.md")
or the [DeleteDomain](../../../customerprofiles/latest/APIReference/API_DeleteDomain.md "../../../customerprofiles/latest/APIReference/API_DeleteDomain.md") API.

**Console method**

- If at any time you want to stop the ingestion of customer profile data,
  choose the integration/mapping and then choose
  **Delete**.
- To delete the integrations, customer profiles, and all the customer
  profile data, you can delete your customer profiles domain in the Amazon Connect console. For more information, see [Delete an Amazon Connect Customer Profiles domain](delete-customer-profiles-domain.md "delete-customer-profiles-domain.md").
  **API method**

- To delete customer profiles data for a specific integration, use the
  `DeleteProfileObjectType` API.
- To delete the integrations, customer profiles, and all the customer
  profile data, use the `DeleteDomain` API.
  To re-enable the ingestion of customer profile data, go through the setup steps
  again.
