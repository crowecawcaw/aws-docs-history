# Understanding registration fields

Your country launch registration contains two categories of fields: fields
that become part of your agent's public profile visible to end users on their
device, and fields that are only seen by the carrier reviewer during the
approval process.

## Agent profile fields (visible to end users on device)

These fields are displayed to recipients in their messaging app. They
form your brand identity and are visible every time a user views your
agent's profile or receives a message from you.

| Field                | Where it appears                                                                   | Constraints                                  |
| -------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------- |
| **Display name**     | Shown as the sender name alongside messages and at the<br>top of the agent profile | 1-40 characters                              |
| **Description**      | Shown on the agent profile page in the messaging app                               | 1-100 characters                             |
| **Logo**             | Shown next to your messages and on the agent profile                               | 224x224 px, PNG with transparency, max 50 KB |
| **Banner image**     | Shown at the top of the agent profile (Android only)                               | 1440x448 px, PNG or JPEG, max 200 KB         |
| **Accent color**     | Used as highlight color in the messaging app UI                                    | Hex code, min 4.5:1 contrast ratio vs white  |
| **Contact phone**    | Shown on agent profile as a tappable contact option                                | E.164 format, with a label                   |
| **Contact email**    | Shown on agent profile as a tappable contact option                                | Valid email, with a label                    |
| **Contact website**  | Shown on agent profile as a tappable link                                          | Valid URL, with a label                      |
| **Privacy policy**   | Linked from the agent profile                                                      | Valid accessible URL, with a label           |
| **Terms of service** | Linked from the agent profile                                                      | Valid accessible URL, with a label           |

Because these fields are visible to end users, they must be accurate,
professional, and represent your brand correctly. Changes to some profile
fields (logo, display name) may require a new registration.

## Carrier review fields (not visible to end users)

These fields are submitted as part of the launch request and are reviewed
by carriers to verify your business identity and messaging compliance. End
users never see these fields.

| Field                                            | Purpose                                      | Notes                                                                                                                    |
| ------------------------------------------------ | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Company name, address, city,<br>region, zip**  | Business identity verification               | Must match official business records                                                                                     |
| **Company phone number**                         | Reviewer contact for verification            | E.164 format required                                                                                                    |
| **Tax code**                                     | Business identity verification               | Must match official records                                                                                              |
| **Industry**                                     | Risk assessment                              | Select from available options                                                                                            |
| **Brand contact person, email,<br>mobile, role** | Point of contact for the brand               | Email domain must match brand (see<br>[ISV and multi-brand registration](rcs-compliance-isv.md "rcs-compliance-isv.md")) |
| **Campaign description**                         | Explains what messages you will send         | Must align with declared use case                                                                                        |
| **Campaign example**                             | Sample message content                       | Must match declared use case type                                                                                        |
| **Opt-in details**                               | How users consent to receive messages        | Text description of your opt-in flow                                                                                     |
| **Opt-in URL**                                   | Where users opt in on your website           | Must be publicly accessible, on your domain                                                                              |
| **Opt-in example**                               | First message sent after opt-in              | Must include brand name                                                                                                  |
| **Opt-out details**                              | How users can stop messages                  | Text description of opt-out mechanism                                                                                    |
| **Opt-out example**                              | Message sent when user opts out              | Must include brand name, confirm no more messages                                                                        |
| **HELP example**                                 | Message sent when user sends HELP            | Must include customer care contact info                                                                                  |
| **Video URL**                                    | Screen recording of the messaging experience | Must be publicly accessible                                                                                              |
| **Estimated monthly volume**                     | Capacity planning                            | Informational, does not restrict sending                                                                                 |

## Why this matters

When writing your **agent description**
(100 chars max), remember that end users see it on their phone. It should
be clear and useful to a consumer, not written for a reviewer. However, it
must also satisfy the carrier reviewer's requirement to specify message
types.

When writing your **campaign description**
and **opt-in/opt-out details**, these are for
the reviewer only. Be thorough and explicit about your compliance
practices — the end user never sees these fields.
