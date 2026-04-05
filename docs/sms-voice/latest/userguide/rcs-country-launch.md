# Launching RCS in countries

After you have tested your RCS messaging integration using a testing agent, the
next step is to launch your AWS RCS Agent in one or more countries. Each country
launch creates a separate RCS for Business ID that is approved
for each carrier in that country. AWS End User Messaging supports RCS country launches in the
United States and Canada.

The country launch process follows this path: you create an AWS RCS Agent,
submit a testing registration to get a testing agent, and then submit one or more
country launch registrations. Each country launch registration goes through a
separate approval process for each carrier in that country.

###### Note

The AWS End User Messaging console presents AWS RCS Agent creation and testing registration
as a single guided workflow. API users can create the AWS RCS Agent
separately and could technically skip the testing registration, but we strongly
recommend completing testing before submitting country launch registrations.

For an overview of how
the AWS RCS Agent relates to RCS for Business IDs, see
[What is RCS?](rcs-overview.md "rcs-overview.md"). For details on creating
and managing your AWS RCS Agent, see
[Managing RCS agents](rcs-agents.md "rcs-agents.md").

###### Topics

- [Testing registration](#rcs-country-launch-testing-registration "#rcs-country-launch-testing-registration")
- [Testing agent as a template for country launches](#rcs-country-launch-template "#rcs-country-launch-template")
- [Launching in the United States](#rcs-country-launch-us "#rcs-country-launch-us")
- [Launching in Canada](#rcs-country-launch-ca "#rcs-country-launch-ca")
- [Use case selection](#rcs-country-launch-use-cases "#rcs-country-launch-use-cases")
- [Registration state management](#rcs-country-launch-registration-states "#rcs-country-launch-registration-states")
- [Per-carrier launch status](#rcs-country-launch-carrier-status "#rcs-country-launch-carrier-status")
- [Carrier approval timelines](#rcs-country-launch-timelines "#rcs-country-launch-timelines")
- [Common registration issues and troubleshooting](#rcs-country-launch-troubleshooting "#rcs-country-launch-troubleshooting")

## Testing registration

Before you can submit a country launch registration, you must first complete a
testing registration for your AWS RCS Agent. The testing registration creates a
testing agent (an RCS for Business ID) that you can use to validate your
integration before going to production.

For step-by-step instructions on creating an AWS RCS Agent and completing the
testing registration, see
[Getting started with RCS](rcs-getting-started.md "rcs-getting-started.md"). For
details on managing test devices and sending test messages, see
[Testing RCS messages](rcs-testing.md "rcs-testing.md").

###### Important

Testing messages are charged at standard RCS rates.

## Testing agent as a template for country launches

###### Important

The testing agent serves as the template for all your country launch
registrations. The brand configuration you set during testing registration
is what gets pre-populated into each country launch form. Take time to get
your testing agent configuration right before submitting country
launches.

When you submit a country launch registration, the AWS End User Messaging console
auto-populates the registration form with the brand configuration from your
testing agent. This includes your brand name, logo, banner image, brand color,
description, and website URL.

You can customize fields for each country launch. For example, you
might adjust the consumer-facing agent name, logo, banner image, or contact
information to match local requirements. Countries can have different brand
assets. The testing agent provides the starting point, but each country
launch can be customized independently.

## Launching in the United States

To launch your AWS RCS Agent in the United States, submit a country launch
registration using the `US_RCS_LAUNCH` registration type. The US
launch registration requires additional information beyond what you provided
for the testing registration.

### US registration requirements

The US launch registration requires the following information:

- **Brand information** —
  Auto-populated from your testing agent configuration. You can
  review and adjust the brand name, description, website URL, and
  contact information.
- **Use case selection** —
  Select the use case category for your RCS messaging. Available
  categories include OTP (one-time passwords), Transactional,
  Promotional, and Multi-use.
- **Screen recording** —
  You must provide a screen recording that demonstrates your
  RCS messaging experience. The recording should show the end-user
  experience of receiving and interacting with your RCS messages.
  This is a requirement specific to the US launch.
- **Privacy policy and terms of service**
  — URLs to your privacy policy and terms of service pages.

###### Important

The screen recording requirement is specific to the US launch
registration. You must provide a recording that clearly demonstrates
your RCS messaging use case. Registrations submitted without a valid
screen recording are rejected.

## Launching in Canada

To launch your AWS RCS Agent in Canada, submit a country launch registration
using the `CA_RCS_LAUNCH` registration type. The Canada launch
registration has different form field requirements than the US launch.

### Canada registration requirements

The Canada launch registration requires the following information:

- **Brand information** —
  Auto-populated from your testing agent configuration. You can
  review and adjust the brand name, description, website URL, and
  contact information for the Canadian market.
- **Use case selection** —
  Select the use case category for your RCS messaging. Available
  categories include OTP (one-time passwords), Transactional,
  Promotional, and Multi-use.
- **Privacy policy and terms of service**
  — URLs to your privacy policy and terms of service pages.

###### Note

The Canada launch registration does not require a screen recording.
The form field requirements differ from the US launch registration.
Review the registration form carefully to ensure all required fields
are completed for the Canadian market.

## Use case selection

When you submit a country launch registration, you must select a use case
category that describes how you intend to use RCS messaging. The use case
category is reviewed by carriers as part of the approval process. The following
use case categories are available:

###### Important

Use case examples must be provided for your agent to be launched.
Select the appropriate use case, as this determines your agent's
configuration and capabilities. Incorrect selection may result in delays
or issues with deployment.

**OTP (one-time password)**

Used for account authentication or secure transaction
confirmation.

**Not permitted:** product updates,
offers, or promotions.

**Transactional**

Send notifications and updates related to customer's
products or services (for example, alerts, confirmations, account
updates).

**Not permitted:** offers,
promotions, discounts, or upgrades.

**Promotional**

Used for offers, promotions, and marketing messages to increase
sales, including reminders for incomplete transactions.

**Not permitted:** OTPs, 2FA, or
urgent transactional notifications.

**Multi-use**

Used when messaging includes both transactional and promotional
messages (for example, sending a purchase confirmation followed by
a related offer).

**Not permitted:** OTP/2FA, password
resets, or purely transactional or purely promotional use.

## Registration state management

Country launch registrations go through a multi-stage approval process. You
can track the progress of your registration using two sets of states: registration
states and registration version states.

### Registration states

The registration state tracks the overall status of your country launch
registration:

**CREATED**

The registration has been created but not yet submitted. You
can edit the registration form fields in this state.

**SUBMITTED**

The registration has been submitted and is awaiting
review.

**REVIEWING**

The registration is being reviewed by the carriers. You
cannot modify the registration while it is in this
state.

**COMPLETE**

The registration has been approved and the country launch
agent (RCS for Business ID) is active. Your AWS RCS Agent can
send messages in this country.

**REQUIRES_UPDATES**

The registration requires changes before it can be approved.
Review the feedback provided, update the required fields, and
resubmit the registration.

**CLOSED**

The registration has been closed. The associated resources
have been removed.

**DELETED**

The registration has been deleted.

### Registration version states

Each registration can have multiple versions. The version state tracks the
status of a specific version of the registration:

**DRAFT**

The version is being prepared and has not been submitted.
You can edit the form fields in this state.

**SUBMITTED**

The version has been submitted for review.

**REVIEWING**

The version is being reviewed by the carriers.

**APPROVED**

The version has been approved. The country launch agent is
active for this country.

**DENIED**

The version has been denied. Review the feedback and submit
a new version with the required changes.

**REVOKED**

A previously approved version has been revoked. The country
launch agent is no longer active.

**ARCHIVED**

The version has been archived. It is no longer the active
version but is retained for historical reference.

**DISCARDED**

The version has been discarded before submission.

## Per-carrier launch status

After you submit a country launch registration, each carrier in that country
independently reviews and approves your AWS RCS Agent. You can track the approval
status at both the individual carrier level and the country aggregate level.

### Carrier states

Each carrier in a country has one of the following approval states:

**PENDING**

The carrier is reviewing your agent. No action is required
from you.

**ACTIVE**

The carrier has approved your agent. Your AWS RCS Agent can
send RCS messages to recipients on this carrier's
network.

**REJECTED**

The carrier has rejected your agent. Review the rejection
reason and submit a new registration version with the required
changes.

### Country aggregate states

The country-level aggregate state summarizes the carrier approval status
across all carriers in a country:

**PENDING**

All carriers in the country are still reviewing your agent.
No carriers have approved or rejected the agent yet.

**PARTIAL**

At least one carrier has approved your agent, but not all
carriers have completed their review. Your AWS RCS Agent can
send messages to recipients on approved carriers.

**ACTIVE**

All carriers in the country have approved your agent. Your
AWS RCS Agent has full reach in this country.

**REJECTED**

All carriers in the country have rejected your agent.

Your AWS RCS Agent can send messages in a country as soon as at least one
carrier in that country has approved the agent. You do not need to wait for all
carriers to approve before you can start sending RCS messages. When a recipient
is on a carrier that has not yet approved your agent, AWS End User Messaging automatically
falls back to SMS if you are using pool-based or account-level sending. As
additional carriers approve your agent, your RCS reach in that country
increases.

To view the per-carrier launch status for your AWS RCS Agent, use the
`DescribeRcsAgentCountryLaunchStatus` API or navigate to the
**Country launch status** tab on the agent details
page in the AWS End User Messaging console.

## Carrier approval timelines

Carrier approval for RCS country launches is a multi-step process that involves
review by each carrier in the target country. Approval timelines vary depending
on the carrier and the completeness of your registration.

For both the United States and Canada, expect the carrier approval process to
take several months from the time you submit your country launch registration.
The timeline includes the initial review, any required updates, and the
per-carrier rollout.

To help ensure a smooth approval process:

- Complete all required registration fields accurately before
  submitting.
- For US launches, provide a clear and complete screen recording that
  demonstrates your RCS messaging use case.
- Respond promptly to any REQUIRES_UPDATES feedback from the review
  process.
- Ensure your privacy policy and terms of service URLs are accessible
  and up to date.

## Common registration issues and troubleshooting

The following sections describe common issues that you might encounter during
the country launch registration process and how to resolve them.

### Registration requires updates

If your registration enters the REQUIRES_UPDATES state, review the
feedback provided in the registration details. Common reasons include:

- Incomplete or inaccurate brand information.
- Missing or invalid screen recording (US launches only).
- Privacy policy or terms of service URLs that are inaccessible or
  do not meet requirements.
- Use case description that does not clearly explain your intended
  messaging purpose.

Update the required fields and resubmit the registration. The registration
returns to the SUBMITTED state and is reviewed again.

### Carrier rejected the agent

If a carrier rejects your AWS RCS Agent, review the rejection reason
provided in the carrier status details. Common rejection reasons
include:

- Brand assets that do not meet the carrier's quality
  standards.
- Use case that does not comply with the carrier's messaging
  policies.
- Insufficient information about the business or messaging
  purpose.

Address the rejection feedback and submit a new registration version. Note
that a rejection by one carrier does not affect the approval status with
other carriers in the same country.

### Registration in review for an extended period

Carrier approval timelines for the United States and Canada are typically
several months. If your registration has been in the REVIEWING state for
longer than expected:

- Verify that your registration does not have a REQUIRES_UPDATES
  status that you may have missed.
- Check the per-carrier status using the
  `DescribeRcsAgentCountryLaunchStatus` API to see if
  some carriers have already approved while others are still
  reviewing.
- Contact AWS Support if you need assistance with a registration
  that has been in review for an unusually long time.

### Registration denial reasons

When a registration is denied, AWS End User Messaging provides a denial reason that
explains why the registration was not approved. The following table lists
all RCS registration denial reasons and the recommended action for each.

| RCS registration denial reasons      | Denial reason                                                                                                                                          | Description                                                                                                                                                                                                                                                                   | Recommended action |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `REQUIRES_OFFLINE_REVIEW`            | This registration requires manual offline review.                                                                                                      | Create a support case in the AWS Support Center.<br>Choose the RCS Agent assistance category and include your<br>registration ID. See<br>[Get more information through Support for registration issues](registrations-request-support.md "registrations-request-support.md"). |
| `CANNOT_UPDATE_REGISTRATION`         | Certain RCS agent fields cannot be modified on an<br>existing registration.                                                                            | Create a new testing registration with the corrected<br>fields.                                                                                                                                                                                                               |
| `IMAGE_URL_INACCESSIBLE`             | The image URL provided is not publicly<br>accessible.                                                                                                  | Provide a URL that can be accessed without<br>authentication. Update the registration and<br>resubmit.                                                                                                                                                                        |
| `IMAGE_FORMAT_INVALID`               | The image must be in JPEG or PNG format.                                                                                                               | Upload an image in the correct format and<br>resubmit.                                                                                                                                                                                                                        |
| `IMAGE_RESOLUTION_INVALID`           | The image does not meet the required resolution. The<br>logo must be 224 x 224 pixels and the banner must be<br>1440 x 448 pixels.                     | Resize the image to the required dimensions and<br>resubmit.                                                                                                                                                                                                                  |
| `IMAGE_SIZE_EXCEEDED`                | The image file size exceeds the allowed limit. The<br>logo must not exceed 50 KB and the banner must not<br>exceed 200 KB.                             | Reduce the file size and resubmit.                                                                                                                                                                                                                                            |
| `ACCENT_COLOR_CONTRAST_INSUFFICIENT` | The accent color must have a contrast ratio of at<br>least 4.5:1 relative to white.                                                                    | Choose a darker accent color that meets the contrast<br>requirement and resubmit.                                                                                                                                                                                             |
| `PRIVACY_POLICY_INACCESSIBLE`        | The privacy policy URL provided is inaccessible or<br>invalid.                                                                                         | Provide a publicly accessible privacy policy URL and<br>resubmit.                                                                                                                                                                                                             |
| `TERMS_AND_CONDITIONS_INACCESSIBLE`  | The terms and conditions URL provided is inaccessible<br>or invalid.                                                                                   | Provide a publicly accessible terms and conditions URL<br>and resubmit.                                                                                                                                                                                                       |
| `CONTACT_DETAILS_MISSING`            | At least one contact method (phone, email, or website)<br>is required in the agent profile, and each contact value<br>must have a corresponding label. | Add at least one contact method to your agent profile.<br>Ensure each contact value has a corresponding label (for<br>example, if you provide a phone number, also provide a<br>phone label). Update the registration and resubmit.                                           |

For denial reasons that require AWS Support assistance, create a
support case in the [AWS
Support Center](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase"). Include your AWS RCS Agent ID and registration ID
in the case description.
