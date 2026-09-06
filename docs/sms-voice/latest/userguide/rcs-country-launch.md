

# Launching RCS in countries
<a name="rcs-country-launch"></a>

After you have tested your RCS messaging integration using a testing agent, the next step is to launch your AWS RCS Agent in one or more countries. Each country launch creates a separate RCS for Business ID that is approved for each carrier in that country. AWS End User Messaging supports RCS country launches in 22 countries across North America, South America, Europe, and Asia Pacific.

The country launch process follows this path: you create an AWS RCS Agent, submit a testing registration to get a testing agent, and then submit one or more country launch registrations. Each country launch registration goes through a separate approval process for each carrier in that country. For the full list of supported countries, see [Supported countries for RCS](rcs-supported-countries.md).

**Note**  
The AWS End User Messaging console presents AWS RCS Agent creation and testing registration as a single guided workflow. API users can create the AWS RCS Agent separately and could technically skip the testing registration, but we strongly recommend completing testing before submitting country launch registrations.

For an overview of how the AWS RCS Agent relates to RCS for Business IDs, see [What is RCS?](rcs-overview.md). For details on creating and managing your AWS RCS Agent, see [Managing RCS agents](rcs-agents.md).

**Topics**
+ [Testing registration](#rcs-country-launch-testing-registration)
+ [Testing agent as a template for country launches](#rcs-country-launch-template)
+ [Use case selection](#rcs-country-launch-use-cases)
+ [Registration state management](#rcs-country-launch-registration-states)
+ [Per-carrier launch status](#rcs-country-launch-carrier-status)
+ [Carrier approval timelines](#rcs-country-launch-timelines)
+ [Common registration issues and troubleshooting](#rcs-country-launch-troubleshooting)
+ [Standard country launch registration](rcs-country-launch-standard.md)
+ [Launching RCS in Austria](rcs-country-launch-at.md)
+ [Launching RCS in Brazil](rcs-country-launch-br.md)
+ [Launching RCS in Canada](rcs-country-launch-ca.md)
+ [Launching RCS in France](rcs-country-launch-fr.md)
+ [Launching RCS in Germany](rcs-country-launch-de.md)
+ [Launching RCS in Mexico](rcs-country-launch-mx.md)
+ [Launching RCS in the Netherlands](rcs-country-launch-nl.md)
+ [Launching RCS in Peru](rcs-country-launch-pe.md)
+ [Launching RCS in Singapore](rcs-country-launch-sg.md)
+ [Launching RCS in Spain](rcs-country-launch-es.md)
+ [Launching RCS in the United Kingdom](rcs-country-launch-gb.md)
+ [Launching RCS in the United States](rcs-country-launch-us.md)
+ [RCS country launch compliance guide](rcs-country-launch-compliance.md)

## Testing registration
<a name="rcs-country-launch-testing-registration"></a>

Before you can submit a country launch registration, you must first complete a testing registration for your AWS RCS Agent. The testing registration creates a testing agent (an RCS for Business ID) that you can use to validate your integration before going to production.

For step-by-step instructions on creating an AWS RCS Agent and completing the testing registration, see [Getting started with RCS](rcs-getting-started.md). For details on managing test devices and sending test messages, see [Testing RCS messages](rcs-testing.md).

**Important**  
Testing messages are charged at standard RCS rates.

## Testing agent as a template for country launches
<a name="rcs-country-launch-template"></a>

**Important**  
The testing agent serves as the template for all your country launch registrations. The brand configuration you set during testing registration is what gets pre-populated into each country launch form. Take time to get your testing agent configuration right before submitting country launches.

When you submit a country launch registration, the AWS End User Messaging console auto-populates the registration form with the brand configuration from your testing agent. This includes your brand name, logo, banner image, brand color, description, and website URL.

You can customize fields for each country launch. For example, you might adjust the consumer-facing agent name, logo, banner image, or contact information to match local requirements. Countries can have different brand assets. The testing agent provides the starting point, but each country launch can be customized independently.

## Use case selection
<a name="rcs-country-launch-use-cases"></a>

When you submit a country launch registration, you must select a use case category that describes how you intend to use RCS messaging. The use case category is reviewed by carriers as part of the approval process. The following use case categories are available:

**Important**  
Use case examples must be provided for your agent to be launched. Select the appropriate use case, as this determines your agent's configuration and capabilities. Incorrect selection may result in delays or issues with deployment.

**OTP (one-time password)**  
Used for account authentication or secure transaction confirmation.  
**Not permitted:** product updates, offers, or promotions.

**Transactional**  
Send notifications and updates related to customer's products or services (for example, alerts, confirmations, account updates).  
**Not permitted:** offers, promotions, discounts, or upgrades.

**Promotional**  
Used for offers, promotions, and marketing messages to increase sales, including reminders for incomplete transactions.  
**Not permitted:** OTPs, 2FA, or urgent transactional notifications.

**Multi-use**  
Used when messaging includes both transactional and promotional messages (for example, sending a purchase confirmation followed by a related offer).  
**Not permitted:** OTP/2FA, password resets, or purely transactional or purely promotional use.

## Registration state management
<a name="rcs-country-launch-registration-states"></a>

Country launch registrations go through a multi-stage approval process. You can track the progress of your registration using two sets of states: registration states and registration version states.

### Registration states
<a name="rcs-country-launch-registration-states-registration"></a>

The registration state tracks the overall status of your country launch registration:

**CREATED**  
The registration has been created but not yet submitted. You can edit the registration form fields in this state.

**SUBMITTED**  
The registration has been submitted and is awaiting review.

**REVIEWING**  
The registration is being reviewed by the carriers. You cannot modify the registration while it is in this state.

**COMPLETE**  
The registration has been approved and the country launch agent (RCS for Business ID) is active. Your AWS RCS Agent can send messages in this country.

**REQUIRES\_UPDATES**  
The registration requires changes before it can be approved. Review the feedback provided, update the required fields, and resubmit the registration.

**CLOSED**  
The registration has been closed. The associated resources have been removed.

**DELETED**  
The registration has been deleted.

### Registration version states
<a name="rcs-country-launch-registration-states-version"></a>

Each registration can have multiple versions. The version state tracks the status of a specific version of the registration:

**DRAFT**  
The version is being prepared and has not been submitted. You can edit the form fields in this state.

**SUBMITTED**  
The version has been submitted for review.

**REVIEWING**  
The version is being reviewed by the carriers.

**APPROVED**  
The version has been approved. The country launch agent is active for this country.

**DENIED**  
The version has been denied. Review the feedback and submit a new version with the required changes.

**REVOKED**  
A previously approved version has been revoked. The country launch agent is no longer active.

**ARCHIVED**  
The version has been archived. It is no longer the active version but is retained for historical reference.

**DISCARDED**  
The version has been discarded before submission.

## Per-carrier launch status
<a name="rcs-country-launch-carrier-status"></a>

After you submit a country launch registration, each carrier in that country independently reviews and approves your AWS RCS Agent. You can track the approval status at both the individual carrier level and the country aggregate level.

### Carrier states
<a name="rcs-country-launch-carrier-status-carrier"></a>

Each carrier in a country has one of the following approval states:

**PENDING**  
The carrier is reviewing your agent. No action is required from you.

**ACTIVE**  
The carrier has approved your agent. Your AWS RCS Agent can send RCS messages to recipients on this carrier's network.

**REJECTED**  
The carrier has rejected your agent. Review the rejection reason and submit a new registration version with the required changes.

### Country aggregate states
<a name="rcs-country-launch-carrier-status-country"></a>

The country-level aggregate state summarizes the carrier approval status across all carriers in a country:

**PENDING**  
All carriers in the country are still reviewing your agent. No carriers have approved or rejected the agent yet.

**PARTIAL**  
At least one carrier has approved your agent, but not all carriers have completed their review. Your AWS RCS Agent can send messages to recipients on approved carriers.

**ACTIVE**  
All carriers in the country have approved your agent. Your AWS RCS Agent has full reach in this country.

**REJECTED**  
All carriers in the country have rejected your agent.

Your AWS RCS Agent can send messages in a country as soon as at least one carrier in that country has approved the agent. You do not need to wait for all carriers to approve before you can start sending RCS messages. When a recipient is on a carrier that has not yet approved your agent, AWS End User Messaging automatically falls back to SMS if you are using pool-based or account-level sending. As additional carriers approve your agent, your RCS reach in that country increases.

To view the per-carrier launch status for your AWS RCS Agent, use the `DescribeRcsAgentCountryLaunchStatus` API or navigate to the **Country launch status** tab on the agent details page in the AWS End User Messaging console.

## Carrier approval timelines
<a name="rcs-country-launch-timelines"></a>

Carrier approval for RCS country launches is a multi-step process that involves review by each carrier in the target country. Approval timelines vary depending on the carrier and the completeness of your registration.

Expect the carrier approval process to take several months from the time you submit your country launch registration. Timelines vary by country and carrier. The timeline includes the initial review, any required updates, the per-carrier rollout, and any out-of-band verification steps required by specific countries.

To help ensure a smooth approval process:
+ Complete all required registration fields accurately before submitting.
+ Provide a clear and complete screen recording that demonstrates your RCS messaging use case. See [Launch video requirements](rcs-compliance-video.md).
+ Respond promptly to any REQUIRES\_UPDATES feedback from the review process.
+ Ensure your privacy policy and terms of service URLs are accessible and up to date.

## Common registration issues and troubleshooting
<a name="rcs-country-launch-troubleshooting"></a>

The following sections describe common issues that you might encounter during the country launch registration process and how to resolve them. For detailed compliance requirements and how to avoid denials, see [RCS country launch compliance guide](rcs-country-launch-compliance.md).

### Registration requires updates
<a name="rcs-country-launch-troubleshoot-requires-updates"></a>

If your registration enters the REQUIRES\_UPDATES state, review the feedback provided in the registration details. Common reasons include:
+ Incomplete or inaccurate brand information.
+ Missing or invalid screen recording.
+ Privacy policy or terms of service URLs that are inaccessible or do not meet requirements.
+ Use case description that does not clearly explain your intended messaging purpose.

Update the required fields and resubmit the registration. The registration returns to the SUBMITTED state and is reviewed again.

### Carrier rejected the agent
<a name="rcs-country-launch-troubleshoot-rejected"></a>

If a carrier rejects your AWS RCS Agent, review the rejection reason provided in the carrier status details. Common rejection reasons include:
+ Brand assets that do not meet the carrier's quality standards.
+ Use case that does not comply with the carrier's messaging policies.
+ Insufficient information about the business or messaging purpose.

Address the rejection feedback and submit a new registration version. Note that a rejection by one carrier does not affect the approval status with other carriers in the same country.

### Registration in review for an extended period
<a name="rcs-country-launch-troubleshoot-long-review"></a>

Carrier approval timelines vary by country and can take several months. If your registration has been in the REVIEWING state for longer than expected:
+ Verify that your registration does not have a REQUIRES\_UPDATES status that you may have missed.
+ Check the per-carrier status using the `DescribeRcsAgentCountryLaunchStatus` API to see if some carriers have already approved while others are still reviewing.
+ Contact AWS Support if you need assistance with a registration that has been in review for an unusually long time.

### Registration denial reasons
<a name="rcs-country-launch-troubleshoot-denial-reasons"></a>

When a registration is denied, AWS End User Messaging provides a denial reason code that explains why the registration was not approved. For the complete list of denial reason codes with descriptions and recommended actions, see [RCS registration denial reasons](rcs-compliance-denial-reasons.md).

### API registration requirements not handled by the console
<a name="rcs-country-launch-troubleshoot-api-registration"></a>

The AWS End User Messaging console automatically populates registration fields from the previous version and manages agent associations. If you use the API to submit registrations, you must handle these steps yourself. The keyword-match validation applies to both the console and the API, but the console pre-fills values from your previous submission.

#### Keyword configuration must match the RCS agent
<a name="rcs-country-launch-troubleshoot-keyword-match"></a>

When you submit a country launch registration, the `complianceKeywords.stopResponse` and `complianceKeywords.helpResponse` field values must exactly match the STOP and HELP keyword responses that are currently configured on your RCS agent. If a custom keyword has been set on the agent and the registration values do not match, the registration is denied with `Invalid field value`. To avoid this, either leave the keyword response fields empty to keep the existing keyword configuration, or set them to the exact values already configured on the agent.

To view the current keyword configuration for your RCS agent, call `DescribeKeywords` using the RCS agent ID as the origination identity. To update a keyword before submitting the registration, call `PutKeyword` using the RCS agent ID as the origination identity.

#### Resubmitting a denied registration via the API
<a name="rcs-country-launch-troubleshoot-api-resubmission"></a>

After a registration is denied, you can create a new version and resubmit. When you use the API, calling `CreateRegistrationVersion` opens a blank version with no field values. You must call `PutRegistrationFieldValue` for every required field before calling `SubmitRegistrationVersion`. If any required fields are missing, the submission fails with `Missing required field`. The AWS End User Messaging console handles this automatically by re-populating the full form when you resubmit.

To identify which fields caused the denial, call `DescribeRegistrationFieldValues` on the denied version. The response includes a `DeniedReason` for each field that failed validation. You can then correct only the affected fields while ensuring all other required fields remain populated.

#### Associating an RCS agent before submission
<a name="rcs-country-launch-troubleshoot-agent-association"></a>

Before you can submit a country launch registration via the API, the registration must be associated with an RCS agent. Call `CreateRegistrationAssociation` to associate the registration with your RCS agent ID before calling `SubmitRegistrationVersion`. Without this association, the submission fails with `SUBMIT_REGISTRATION_VERSION_NOT_ALLOWED`. The AWS End User Messaging console creates this association automatically as part of the guided workflow.