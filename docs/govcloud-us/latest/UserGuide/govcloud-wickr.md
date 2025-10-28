# AWS WickrGov in AWS GovCloud (US)

AWS WickrGov is an end-to-end encrypted service that helps organizations
collaborate across messaging, calling, file sharing, and screen sharing. Users of
AWS WickrGov can also federate with other AWS WickrGov users outside their
network.

## How AWS WickrGov differs for

AWS GovCloud (US)

- WickrGov is only available in the AWS GovCloud (US-West) Region.
- The AWS GovCloud (US) Federation allows communication between WickrGov
  networks in the AWS GovCloud (US-West) Region and commercial networks in other
  Regions.
- Client name will appear changed to AWS WickrGov and utilizes a new
  AWS WickrGov logo with blue background and white slashes.
- AWS WickrGov Desktop, Android, and iOS apps are tailored for AWS GovCloud (US)
  users. When AWS GovCloud (US) users engage in conversations with commercial users
  (Wickr Enterprise, AWS Wickr, Guest users), they will see the following
  unclassified warnings displayed:
  - A U tag in the room list. (U tag refers to unclassified)
  - An unclassified acknowledgment on the message screen in every
    conversation.
  - An unclassified banner on top of the conversation.

- AWS WickrGov offers a premium free trial option that allows up to 50 users and
  last for three months.

## Documentation for AWS WickrGov

[AWS WickrGov
documentation](../../../wickr/index.md "../../../wickr/index.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Email addresses of provisioned users within a network leave the AWS GovCloud (US)
  Regions in the normal course of service use. Do not enter export-controlled
  information into the email field when provisioning users.
- Network names are visible to the AWS WickrGov service team as part of
  normal service function. Do not enter export-controlled or sensitive information
  into the network name field when creating a network.
- When an AWS WickrGov network in AWS GovCloud (US) and an AWS Wickr
  network in an AWS commercial Region are federated, communications may be
  stored in either federated network’s data retention module if configured.
