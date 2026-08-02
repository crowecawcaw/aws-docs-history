# Managing an active service period

Active service periods impact both parties Billing Transfer management experience in Billing and Cost Management console. Partners can view and manage active service periods through AWS Partner Central channel management.

Active service periods require the specified advance notice (14, 30, or 60 days) before either party can make billing transfer changes. Both parties retain the ability to make changes to Billing Transfer via the AWS Billing console, however the notice period determines the allowed effective date for any Billing Transfer change.

For example, if a 60-day notice period is in place and a user attempts to withdraw from Billing Transfer on January 1, they would only be able to elect to withdraw effective March 1 or later. This provides the counterparty sufficient notice to manage billing changes before they go into effect.

## Replacing service periods

Partners may need to replace an existing active service period with new terms to accommodate changing business requirements or contract renewals. The replacement process ensures continuous governance of the billing transfer relationship while updating the service period parameters.

### When to replace a service period

Partners may want to replace a service period to adjust the minimum notice period duration (for example, changing from 30 to 60 days) to accommodate changing business requirements or contract renewals.

### Replacement process

1. **Partner initiates replacement** – Channel Partners access the active service period through AWS Partner Central channel relationship management and select the option to replace the service period. Partners specify the new minimum notice period duration (14, 30, or 60 days) and can include optional context explaining the reason for replacement.
2. **Customer notification** – A new service period channel handshake is automatically created and the end-customer's AWS management account receives an email notification with a unique link to review the proposed replacement terms.
3. **Customer review and response** – An authorized user from the customer's AWS management account must:

   - Access the replacement request using the provided link
   - Sign in to the AWS Console to review the new service period terms and partner's explanation
   - Accept or reject the replacement request

4. **Seamless transition** – When the customer accepts the replacement handshake:

   - The previous service period ends immediately
   - The new service period becomes active with the updated terms
   - The billing transfer relationship continues uninterrupted under the new service period governance
   - Both parties receive confirmation notifications

### Important considerations

- If the customer rejects the replacement request, the original service period continues under its existing terms
- Only one pending service period handshake can exist at a time for each relationship
- Replacement requests expire after 30 days if not accepted by the customer
- The replacement history is maintained in the relationship record for audit purposes
- Replacing a service period does not affect the underlying billing transfer relationship
