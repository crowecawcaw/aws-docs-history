# Use case selection and pre-submission checklist

Your declared use case (OTP, Transactional, Promotional, or Multi-use) must
align with ALL other elements of your registration.

## Alignment requirements

| Element           | Must match use case                                  |
| ----------------- | ---------------------------------------------------- |
| Agent description | Describes the same message types as your use case    |
| Sample messages   | Examples match the declared use case category        |
| Launch video      | Demonstrates messages matching the declared use case |
| Opt-in flow       | Consent language covers the declared message types   |

## Choosing the right use case

- **One-time password (OTP)** —
  Used for account authentication or secure transaction confirmation.
  Not permitted: product updates, offers, or promotions.
- **Transactional** — Used to
  send notifications and updates related to a customer's products or
  services (for example, alerts, confirmations, account updates). Not
  permitted: offers, promotions, discounts, or upgrades.
- **Promotional** — Used for
  offers, promotions, and marketing messages to increase sales, including
  reminders for incomplete transactions. Not permitted: OTPs, 2FA, or
  urgent transactional notifications.
- **Multi-use** — Used when
  messaging includes both transactional and promotional messages (for
  example, sending a purchase confirmation followed by a related offer).
  Not permitted: OTP/2FA, password resets, or purely
  transactional-only or purely promotional-only use. You must demonstrate
  both message types in your video and description.

###### Note

When in doubt between Transactional and Multi-use: if you will EVER
send a promotional message (offer, discount, upsell), choose Multi-use.
But ensure your video and description reflect both message types.

## Common misalignment denials

| Declared use case | Issue                                      | How to fix                                                                  |
| ----------------- | ------------------------------------------ | --------------------------------------------------------------------------- |
| Multi-use         | Video only shows transactional messages    | Add promotional message examples to the video                               |
| Transactional     | Sample message is promotional ("20% off!") | Change sample to a transactional message (order<br>confirmation, alert)     |
| Multi-use         | Description only mentions notifications    | Update description to mention both transactional and<br>promotional content |
| OTP               | Campaign description mentions marketing    | Change use case to Multi-use, or remove marketing<br>references             |

## Phone number format

Phone numbers in your registration (company phone, brand contact mobile)
must be in valid international format.

- Use E.164 format: country code with + prefix, followed by
  digits only.
- No spaces, dashes, parentheses, or other formatting
  characters.
- Example: `+12125551234` (US),
  `+14165550100` (CA)

## Pre-submission checklist

Before submitting your country launch registration, verify:

- **Agent description** clearly
  states message types (transactional, promotional, or both) and is under
  100 characters
- **Launch video** shows: sample
  message, HELP response with contact info, STOP response with brand
  name
- **Launch video URL** is publicly
  accessible (test in incognito browser)
- **Video content** matches your
  declared use case (multi-use = show both types)
- **CTA/opt-in page** includes:
  brand name, HELP/STOP instructions, frequency, rates, T&C link,
  privacy link
- **Opt-in confirmation message**
  includes your brand name
- **Privacy policy URL** is
  accessible and covers messaging
- **Terms of service URL** is
  accessible and includes messaging terms
- **Phone numbers** are in E.164
  format (+12125551234)
- **Brand contact email** uses the
  end-brand's domain (ISVs: provide a contact at the end-brand's
  organization)
- **Use case selection** aligns
  with description, video, and sample messages
- **All URLs** tested in incognito
  browser (no auth, no geo-blocking)
