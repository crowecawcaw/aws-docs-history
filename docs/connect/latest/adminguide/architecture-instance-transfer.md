# Instance to instance transfer

You can build your contact center within a single Amazon Connect instance. However, managing
multiple lines of business in one instance complicates access control. Instance transfer
lets you maintain the benefits of Amazon Connect while allowing individual business units to
run and control their own contact centers.

Instance transfer enables you to centralize IVR functions in one instance. After customers
select their options, you transfer calls to individual Amazon Connect instances. This allows
independent management of each business unit while maintaining isolation of access controls
but eliminates the cost of the telephony between the two systems.

## How it works

Instance transfer uses our routing AI to identify the telephone number being called.
If the number belongs to your Amazon Connect account, the call transfers across the AWS Backbone
to the Amazon Connect instance that owns the number, removing the telephony transfer costs for
both instances.

**Instance transfers require:**

- Unlimited AI
- Amazon Connect Telephony using DID, Toll-Free, Shared Cost numbers only
- Direct ownership relationship within an AWS Organization (To enable AWS
  wide transfers, open a support case with AWS Support.)

**Instance transfers are not supported:**

- Outside of an AWS Organization with no direct ownership relationship
- A-La Carte (Classic) Instances

## Passing data between instances

Instance transfer within the AWS network preserves contact attributes for
transferred calls. To pass context between instances:

1. Set context attributes on the original call leg, capturing whatever data you
   wish to pass.
2. When the call reaches the next instance, the second instance should then
   retrieve the information about the original by using a Lambda call using [DescribeContact](../APIReference/API_DescribeContact.md "../APIReference/API_DescribeContact.md")
   API passing in the original contact ID. The contact ID is retrievable from the `connect:CrossInstanceInfo` segment attributes. More information on how to
   determine the ID can be found [here](troubleshoot-instance-transfer.md#locate-instance-transfer-information "troubleshoot-instance-transfer.md#locate-instance-transfer-information").

## Service availability

Instance transfer is available in all AWS regions where Amazon Connect is offered, except
AWS GovCloud (US-West) and Africa (Cape Town).

## Transfers cost considerations

Instance transfer of calls between instances within the same AWS Region is covered
by the existing cost structure for Amazon Connect and Contact Centre Telecom, allowing you to run
segmented or globally distributed follow the sun models without additional telephony
transfer costs.
