

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Working with Partner Verification
<a name="working-with-partner-verification"></a>

## Managing Partner Verification
<a name="managing-partner-verification"></a>

Partner verification is a mandatory prerequisite for partner account registration. Before partners can create a partner account, they must complete business verification and identity verification processes. These verifications validate that the business is legally registered and confirm the identity of the person registering the AWS account.

Partners can utilize the available verification APIs to initiate and monitor verification processes:

### During Verification
<a name="during-verification"></a>

1. **Business Verification Initiation** – Partners initiate business verification by calling the `StartVerification` API with business registration details including legal name, registration ID, country code, and jurisdiction of incorporation.

1. **Identity Verification Initiation** – Partners initiate identity verification by calling the `StartVerification` API with registrant information. The API returns a secure completion URL where the registrant completes the identity verification workflow using government-issued identification.

1. **Verification Status Monitoring** – Partners use the `GetVerification` API to retrieve the current status and details of verification processes. The API returns verification type, status, timestamps, and verification-specific details.

1. **Verification Completion** – Both business verification and identity verification must reach `SUCCEEDED` status before partners can proceed to partner account creation. Failed or expired verifications must be resolved before account registration.

### Post Verification
<a name="post-verification"></a>

1. **Partner Account Creation** – After successful verification, partners proceed to create their partner account using the `CreatePartner` API described in the Partner Account documentation.

1. **Verification Record Retrieval** – Partners can retrieve verification details at any time using the `GetVerification` API with the verification ID returned during initiation.

### API Summary
<a name="verification-api-summary"></a>

1. **`StartVerification` API:** Partners initiate verification processes by calling the `StartVerification` API. For business verification, the API validates business registration details. For identity verification, the API generates a time-limited completion URL for the registrant to complete identity verification.

1. **`GetVerification` API:** After initiating verification, partners use the `GetVerification` API to retrieve verification status and details. The API returns current status, timestamps, and verification-specific information.