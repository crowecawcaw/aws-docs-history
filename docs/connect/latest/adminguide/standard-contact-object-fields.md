

# Customer Profiles standard contact object fields
<a name="standard-contact-object-fields"></a>

The standard contact object stores a customer's contact methods—phone numbers and email addresses—with history retained. Each version of a contact method is stored as a separate record, so a changed phone number doesn't overwrite the previous one. Register the built-in template with `PutProfileObjectType` using the template ID `_contact`, or create a custom object type whose fields target `_contact.*` and whose key carries the `CONTACT`, `PROFILE`, and `UNIQUE` standard identifiers.

The following table lists all the fields in the Customer Profiles standard contact object. All fields are of type `String`.


**Contact**  

| Standard contact field | Type | Description | 
| --- | --- | --- | 
| Contact | String | The contact value itself: a phone number or an email address. Part of the unique key. | 
| ChannelType | String | The kind of contact method, for example Home, Business, Mobile, or Land. Part of the unique key. | 
| Type | String | The purpose or context of the contact method, for example Profile, Booking, Subscription, or Payment. Part of the unique key. | 
| EffectiveDate | String | The date this version of the contact method became effective. Part of the unique key. This value is compared as text and is never parsed, so use one format for every record—ISO 8601 (YYYY-MM-DD) is recommended. A new EffectiveDate creates a new record instead of overwriting the previous one. | 
| ChannelCode | String | The channel of the contact value, for example Phone or Email. | 
| PhoneCountryCode | String | Dialing country code for phone contacts, for example 1 or 44. Empty for email contacts. | 
| IsVerified | String | Whether the contact method has been verified. Stored and returned as text, not a JSON boolean: send the string true or false and compare it as a string on read. Other values are stored as sent and are not normalized. | 
| OptIn | String | Whether the customer has opted in to communication on this contact method. Stored and returned as text, not a JSON boolean, following the same rule as IsVerified. | 
| LastUpdated | String | Timestamp of the last update in the source system. | 
| OrganizationId | String | Identifier of the organization or business unit that owns the contact record. | 


**Standard Index Fields**  

| Standard index name | Standard contact record fields | 
| --- | --- | 
| \_contactId | Contact, ChannelType, Type, EffectiveDate | 

The `_contactId` key carries the `CONTACT`, `PROFILE`, and `UNIQUE` standard identifiers. All four key fields (Contact, ChannelType, Type, and EffectiveDate) are required on every `_contact` object; an object missing any of them is rejected. By default, a profile can hold up to 250 `_contact` objects.

To read contact data, use `ListProfileObjects` with `ObjectTypeName` `_contact` to return the full contact history of a profile, `SearchProfiles` with `KeyName` `_contactId` to find the profile that owns a contact record, or `GetProfile`, which reports `_contactId` in `FoundByItems`.