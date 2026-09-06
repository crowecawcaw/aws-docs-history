

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Working with Partner Profile
<a name="working-with-partner-profile"></a>

## Profile management
<a name="profile-management"></a>

Partners manage profiles containing company details (name, description, website, logo) with public/private visibility control, asynchronous validation, and status tracking allowing one update at a time.

1. **Profile Information** – Partner profiles must include essential company details such as display name, description, website URL, logo, IndustrySegments and PrimarySolutionType.

1. **Multilingual Support** – Partner profiles support multiple languages. Each localized version of the profile contains an attribute for locale.

1. **Profile Visibility Control** – Partners can configure their profile visibility (public or private).

1. **Profile Storage** – Profile information will be stored within the partner account object.

1. **Profile Status Management** – Profile updates are validated asynchronously before publishing. Partners can check the latest profile updating status (IN\_PROGRESS, SUCCEED, FAILED and CANCELLED). Only approved profiles become publicly visible.

1. **Request Concurrency Control** – Only one profile update request is allowed at a time. If a profile update is already in progress, customers must explicitly cancel the ongoing update via the CancelPartnerProfileUpdateTask API before initiating a new one.

1. **Cancellation of Update Tasks** – Partners can cancel an in-progress profile update by calling the CancelPartnerProfileUpdateTask API. Cancellation is only allowed while the update is in the IN\_PROGRESS status and must be completed before starting a new update.

### API Summary
<a name="profile-api-summary"></a>

1. **StartPutProfileTask API:** This API accepts partner profile updates and performs basic synchronous input validation.

1. **GetProfileUpdateTask API:** This API allows Partners to fetch the current profile update status. It is intended to be used after customer start a profile update via StartPutPartnerProfile API, enabling Partners to check whether their request is IN\_PROGRESS, FAILED, SUCCEEDED or CANCELLED.

1. **CancelProfileTask API:** Allows a partner to explicitly cancel a profile update task that is currently in the IN\_PROGRESS status. This includes both auto-vetting and manual review phases. Canceling a request enables the partner to initiate a new profile update without waiting for the current vetting process to complete.

1. **PutProfileVisibility API:** By calling this API, partners can control the visibility of a profile regardless of locale. This allows partners to make profiles public or private without modifying the content.

1. **GetProfileVisibility API:** By calling the UpdatePartnerProfileVisibility API, partners can control the visibility of a profile regardless of locale. This allows partners to make profiles public or private without modifying the content.