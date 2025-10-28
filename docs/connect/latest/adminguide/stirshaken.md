# Stir/Shaken attestation in Amazon Connect

Amazon Connect supports STIR/SHAKEN attestation for outbound calls to help prevent caller
ID spoofing.

When originating calls from United States direct-inward-dial (DID) or
toll-free numbers to North American Numbering Plan (NANP) destinations (+1 prefix),
Amazon Connect signs calls with STIR/SHAKEN headers indicating the level of
attestation.

###### Contents

- [What is STIR/SHAKEN?](#what-is-stirshaken "#what-is-stirshaken")
- [Amazon Connect attestation
  levels](#attestation-levels "#attestation-levels")
- [Requirements for A-level
  attestation](#attestation-level-a "#attestation-level-a")
- [Requirements for B-level
  attestation](#attestation-level-b "#attestation-level-b")
- [Examples of C-level
  attestation](#examples-c-attestation "#examples-c-attestation")
- [Important things to know](#important-attestation "#important-attestation")

## What is STIR/SHAKEN?

The STIR/SHAKEN framework is designed to combat fraudulent caller ID spoofing in
telephony networks. It consists of two components:

- STIR (Secure Telephone Identity Revisited): The underlying protocol suite
  that enables cryptographic signing and verification of calling
  numbers.
- SHAKEN (Signature-based Handling of Asserted Information Using toKENs):
  Guidelines for implementing these protocols across networks.

For more information about STIR/SHAKEN, see
[Combating Spoofed Robocalls with Caller ID Authentication](https://www.fcc.gov/call-authentication "https://www.fcc.gov/call-authentication")
on the Federal Communications Commission (FCC) website.

## Amazon Connect attestation levels

Amazon Connect assigns one of three attestation levels when signing outbound
calls:

- A-level (Full) - Amazon Connect has:
  - Authenticated the calling party
  - Confirmed their authorization to use the calling number

- B-level (Partial) - Amazon Connect has:
  - Authenticated the calling party
  - Cannot verify their authorization to use the number

- C-level (Gateway) - Amazon Connect has:
  - Originated the call
  - Cannot verify the calling party's identity
  - Cannot verify legitimate use of the number

## Requirements for A-level

attestation

Your calls receive A-level attestation if you are subject to AWS Service Terms
or are a customer of an authorized AWS Solution Provider/Distribution Seller AND
any of these conditions are met:

- Number claimed through Amazon Connect portal/API.
- Number ported into Amazon Connect.
- Third-party number mapped to your account with validated
  documentation.

## Requirements for B-level

attestation

Your calls receive B-level attestation if:

- You have been notified that additional information is needed to maintain
  A-level attestation.
- We have NOT notified you that we have successfully validated the information you provided.

## Examples of calls that receive C-level

attestation

All calls that don't receive A- or B-level attestation receive C-level attestation.

Following are examples of calls that receive C-level attestation:

- Calls made by customers using unauthorized solution providers.
- Calls made
  in violation of AWS Services Terms (for example, call deflection).
- Cases where we
  have notified you that additional information is required and we have not received the requested attestation
  documentation by the specified date.

## Important things to know

- While Amazon Connect provides STIR/SHAKEN headers to carriers,
  attestation may not be preserved end-to-end due to legacy equipment in
  some carrier networks that cannot transmit these headers.
- Carriers may use attestation levels as part of their process of determining whether they deliver calls in their network.
- To maintain the highest levels of attestation for your calls, Amazon Connect may ask you for additional information.
  In the notification email we send to you, we will state when you need to reply with the requested information.
  Any delays in providing us the information may impact the attestation level of your calls and as a result,
  may impact the success of your call delivery.
