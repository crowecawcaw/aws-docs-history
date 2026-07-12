The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Working with Partner Registration

## Partner Registration

Partners can register their account using their AWS account for Partner Engagement. Using the Create API, partners will provide required alliance lead information, accept APN terms, and provide a unique legal name.

### During Registration

1. **Synchronous Partner Entity Creation** – Customers initiate the partner registration process by calling the Create API, which performs input validation and creates the Partner Entity within the same request.
2. **Alliance Lead Information Requirement** – During partner registration, customer must provide alliance lead contact information for AWS Partner Network (APN) related communication.
3. **Terms & Conditions Enforcement** – Customers must accept the APN Terms and Conditions during registration. Acceptance is required to complete the registration and access any features. The terms apply to all APN program benefits and functionalities.
4. **Tag-On-Create Support** – As part of AWS Consistent Authorization Experience (CAE) and Tag-Based Authorization, customers are able to add tags at the time of partner entity creation.
5. **Legal Name-Based Validation** – Registration will enforce uniqueness based on partner legal name, ensuring no duplicate registrations under the same entity.

### Post Registration

1. **Tag Management Support** – After registration, partners are able to tag, un-tag, and list tags for an existing partner entity.
2. **Fetch Partner Entity** - After a partner entity is created, customers can use List API to retrieve the Partner ID and then use the Get API to fetch the details of a specific partner entity.

### API Summary

1. **CreatePartner API:** Customers initiate the partner registration process by calling the CreatePartner API, which performs input validation and creates the Partner Entity within the same request.
2. **ListPartners API:** After registration, customers can use the List API to retrieve list of partner entities.
3. **GetPartner API:** After registration, customers can use the Get API to retrieve details of a specific partner entity.
4. **PutAllianceLeadContact API:** Updates the primary alliance lead contact information. This operation allows partners to transfer primary alliance lead designation or modify contact details while maintaining organizational continuity.
5. **GetAllianceLeadContact API:** Updates the primary alliance lead contact information. This operation allows partners to transfer primary alliance lead designation or modify contact details while maintaining organizational continuity.
