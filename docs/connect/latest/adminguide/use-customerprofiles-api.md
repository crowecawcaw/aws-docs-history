# Use the Amazon Connect Customer Profiles API

For information about how to programmatically manage domains and profiles, see the
[Amazon Connect Customer Profiles API Reference](../../../customerprofiles/latest/APIReference/Welcome.md "../../../customerprofiles/latest/APIReference/Welcome.md").

## ListObjectTypeAttributeValues API

The ListObjectTypeAttributeValues API provides access to the most recent distinct values for any specified attribute, making it valuable for real-time data validation and consistency checks within your object types. This API works across domain, supporting both custom and standard object types. The API accepts the object type name, attribute name, and domain name as input parameters and returns values up to the storage limit of approximately 350KB.

**Note:**

- We store up to 350KB of attribute values per field, prioritizing the most recent values first. Once this limit is reached, older values will be automatically removed to make space for new entries.

## GetObjectTypeAttributeValues API

The GetObjectTypeAttributeValues API delivers statistical insights about attributes within a specific object type, but is exclusively available for domains with Data store enabled. This API performs daily calculations to provide statistical information about your attribute values, helping you understand patterns and trends in your data. The statistical calculations are performed once per day, providing a consistent snapshot of your attribute data characteristics.

**Note:**

- You'll receive null values in two scenarios:
  - During the first period after enabling data vault (unless a calculation cycle occurs, which happens once daily).
  - For attributes that don't contain numeric values.

We recommend using the CustomerProfileJS open source library when integrating Customer
Profiles into your own agent application. For more information, see the
CustomerProfilesJS repo on [Github](https://github.com/amazon-connect/amazon-connect-customer-profiles "https://github.com/amazon-connect/amazon-connect-customer-profiles").

For more information about how to integrate your existing apps with Amazon Connect use [Amazon Connect Streams](https://github.com/aws/amazon-connect-streams "https://github.com/aws/amazon-connect-streams"). You can
embed the Contact Control Panel (CCP) components into your app.
