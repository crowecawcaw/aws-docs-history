The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Working with Partner Verification

## Managing Partner Verification

Partner verification is a mandatory prerequisite for partner account registration. Before partners can create a partner account, they must complete business verification and identity verification processes. These verifications validate that the business is legally registered and confirm the identity of the person registering the AWS account.

Partners can utilize the available verification APIs to initiate and monitor verification processes:

### During Verification

1. **Business Verification Initiation** – Partners initiate business verification by calling the `StartVerification` API with business registration details including legal name, registration ID, country code, and jurisdiction of incorporation.
2. **Identity Verification Initiation** – Partners initiate identity verification by calling the `StartVerification` API with registrant information. The API returns a secure completion URL where the registrant completes the identity verification workflow using government-issued identification.
3. **Verification Status Monitoring** – Partners use the `GetVerification` API to retrieve the current status and details of verification processes. The API returns verification type, status, timestamps, and verification-specific details.
4. **Verification Completion** – Both business verification and identity verification must reach `SUCCEEDED` status before partners can proceed to partner account creation. Failed or expired verifications must be resolved before account registration.

### Post Verification

1. **Partner Account Creation** – After successful verification, partners proceed to create their partner account using the `CreatePartner` API described in the Partner Account documentation.
2. **Verification Record Retrieval** – Partners can retrieve verification details at any time using the `GetVerification` API with the verification ID returned during initiation.

### API Summary

1. **`StartVerification` API:** Partners initiate verification processes by calling the `StartVerification` API. For business verification, the API validates business registration details. For identity verification, the API generates a time-limited completion URL for the registrant to complete identity verification.
2. **`GetVerification` API:** After initiating verification, partners use the `GetVerification` API to retrieve verification status and details. The API returns current status, timestamps, and verification-specific information.
