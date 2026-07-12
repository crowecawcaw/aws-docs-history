The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Using the AWS Partner Central Channel API

AWS Partner Central Channel APIs enable you to programmatically manage your authorized AWS reselling business. These APIs allow AWS Solution Providers, AWS Distributors, and AWS Distribution Sellers to:

- Report AWS management accounts used for resale programs to Partner Central
- Send invitations to AWS accounts to accept partner associations
- Create relationships required to onboard resold end customer AWS accounts and apply partner discounts
  With AWS Partner Central Channel APIs, you can build custom automation to:

- Onboard new partner-owned AWS accounts to APN resale programs
- Onboard new end customer accounts to resale programs
- Accelerate customer onboarding and discount qualification

## Working with Program Management Accounts (PMAs)

A Program Management Account (PMA) associates your AWS management account with your Channel Program registration. Program management accounts are activated self-service using channel handshakes. When you create and activate a PMA, channel program benefits and discounts are applied to all invoices delivered to the associated AWS management account. Use these APIs to report and manage AWS accounts that handle reselling and Channel Discounts:

- `CreateProgramManagementAccount`: Add new accounts for customer billing management
- `UpdateProgramManagementAccount`: Modify existing accounts
- `DeleteProgramManagementAccount`: Remove accounts from resale programs
- `ListProgramManagementAccounts`: View existing accounts and their status

## Working with channel handshakes

Channel handshakes enable secure, mutual consent for critical channel management operations. AWS Partner Central uses channel handshakes to verify consent from AWS management accounts for three distinct purposes: activating Program Management Accounts (PMAs), establishing service periods, and terminating service periods early. There are three types:

- `PROGRAM_MANAGEMENT_ACCOUNT`: Program Management Account handshakes verify consent when activating PMAs to apply channel program benefits
- `START_SERVICE_PERIOD`: Service period creation handshakes establish mutual agreements for billing transfer commitments with minimum notice periods or fixed terms
- `REVOKE_SERVICE_PERIOD`: Service period termination handshakes enable early termination of active service periods when both parties consent. All handshake types require acceptance from the target AWS management account to take effect.

Use these APIs to manage channel handshakes for PMA activation and service period management:

- `CreateChannelHandshake`: Create handshakes for PMA invitations, service period establishment, or service period termination
- `AcceptChannelHandshake`: Accept handshakes from target AWS accounts (can be used by partners or customers depending on handshake type)
- `RejectChannelHandshake`: Reject handshakes from target AWS accounts
- `CancelChannelHandshake`: Cancel pending handshakes before they are accepted, rejected, or expired
- `ListChannelHandshakes`: Track and view handshakes with filtering by type and status

## Working with channel relationships

Relationships enable you to manage end customers, internal organizations, or downstream sellers. Each relationship includes:

- The AWS management account of the associated AWS organization
- Required AWS Partner Network metadata for channel discount qualification

When you create a relationship, all usage from the associated AWS organization receives the related Channel Program benefits. Use these APIs to report sellers and end customers:

- `CreateRelationship`: Onboard new end customer, distribution-seller, or internal AWS accounts
- `GetRelationship`: View specific relationship details
- `ListRelationships`: View all relationships
- `UpdateRelationship`: Modify existing relationships
- `DeleteRelationship`: Remove relationships
