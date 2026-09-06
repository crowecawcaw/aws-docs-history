# Outbound calling restrictions in Connect Customer

This topic explains restrictions that are in place for outbound calling with Connect Customer.

###### Contents

- [Use of toll-free numbers outside the
  country of origin](#restriction1 "#restriction1")
- [Use of UIFN numbers for outbound
  dialing](#restriction2 "#restriction2")
- [Redirection of calls](#restriction3 "#restriction3")
- [International calling
  restrictions](#restriction4 "#restriction4")

## Use of toll-free numbers outside the country of origin

Connect Customer does not support the use of toll-free numbers for international
calling. International calls from toll-free numbers can be flagged as spam by
downstream providers, resulting in negative reputation scores. They can also
generate unexpected fees for call recipients.

## Use of UIFN numbers for outbound dialing

UIFN numbers are designed to be used for inbound calls only. They cannot be used
for outbound calling. If you attempt to use UIFN for outbound calling, the calls
will be blocked.

## Redirection of calls

If you are using Amazon Connect to redirect calls: If you are receiving calls with
Anonymous (withheld CLI), you must use a Connect Customer number for the transfer.

**Important:** Anonymous calls (calls without caller
ID) are increasingly blocked by carriers as anti-spam measures and might violate
telecommunications regulations in many countries. Always configure a valid caller ID
number from your Amazon Connect instance to ensure reliable call delivery.

See [Set up outbound caller ID in Connect Customer](queues-callerid.md "queues-callerid.md").

## International calling restrictions

Connect Customer has several restrictions on international calling. These are
based on requirements in the following specific jurisdictions.

### South Africa

South African mobile numbers available under the DID option are designed to be
national-only services and are not supported for international calling.

### China

Chinese carriers are increasingly blocking international routes into China
unilaterally. Connect Customer has taken steps to continue to support our
existing customers but require that all customers comply with additional
requirements for continued use. Starting October 14, 2023 all customers approved
to make international calls to China are required to follow these conditions.

#### Eligibility criteria

- **Unsupported use cases**

  - Short calls and alerting (less than 15 seconds).
  - High volume of calls, especially when done over a short
    period of time, using the same outbound caller ID (more than
    5 calls per minute).
  - Any form of cold calling.
  - Any calls to invalid phone numbers. All numbers called
    must be validated as accurate.
  - Repeated calls using the same FROM / TO numbers.
  - Attempts to call China FROM any number that has not been
    pre-approved.

- **Supported use cases**

  - Direct calls to known business entities. For example,
    calling a hotel or IT support function.
  - Calling users who attempted to engage with your business.
    For example, university placement schemes or product
    purchases.

#### Data required for setup

To request the ability to make international calls to Chinese telephone
numbers (+86), perform the following steps:

- You must provide an exact list of telephony numbers you will use
  to phone China.

  - The number must be a DID provided by Connect Customer.
    No other number is acceptable.
  - The number cannot be a DID provided by Hong Kong, Macau,
    Taiwan, or Singapore.

  ###### Note

  The preceding list might change at any time.

- Any number used to make international calls to Chinese telephone
  numbers must be able to called back. You must also implement a call
  back message that clearly states the name of the company that is
  associated with the phone number.
- You must provide a detailed description of your use case, and
  confirm that you meet the [eligibility
  criteria](#criteria-cr "#criteria-cr") described in this topic.

#### Consequences for violating the calling criteria for China

Connect Customer has a zero tolerance policy for international calling into China.
AWS will suspend your use of Connect Customer if you use the service for any of the
restricted use cases identified in this topic. It is essential that the
administrators of your Connect Customer service focus on ensuring the members of your
organization are aware of these restrictions, as ignorance of the rules is
not an acceptable reason for breach.

#### Service assurance

In the event of further incidents where Chinese carriers block major
international routes without prior warning and impact the ability to call
China, the exemptions in the [Connect Customer Service Level
Agreement](https://aws.amazon.com/connect/sla/ "https://aws.amazon.com/connect/sla/") will take effect.
