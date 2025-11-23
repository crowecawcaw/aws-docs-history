# Managing an active service period

Active service periods impact both parties Billing Transfer management experience in Billing and Cost Management console. Partners can view and manage active service periods through AWS Partner Central channel management.

- **Fixed-term commitments** prevent either party from modifying the billing transfer until the commitment period expires
- **Minimum notice periods** require the specified advance notice for any billing transfer changes

## Replacing service periods

Partners may need to replace an existing active service period with new terms to accommodate changing business requirements or contract renewals. The replacement process ensures continuous governance of the billing transfer relationship while updating the service period parameters.

### When to replace a service period

- Converting from a minimum notice period to a fixed-term commitment (or vice versa)
- Extending or modifying the duration of a fixed-term commitment
- Adjusting minimum notice period requirements (e.g., changing from 30 to 60 days)
- Renewing an expiring fixed-term commitment with updated terms

### Replacement process

1. **Partner initiates replacement** – Channel Partners access the active service period through AWS Partner Central channel relationship management and select the option to replace the service period. Partners specify the new service period terms (either updated minimum notice days or new start/end dates for fixed-term commitments) and can include optional context explaining the reason for replacement.
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
