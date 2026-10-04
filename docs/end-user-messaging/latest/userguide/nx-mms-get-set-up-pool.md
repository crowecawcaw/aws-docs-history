

# Step 3: Set up a phone pool
<a name="nx-mms-get-set-up-pool"></a>

A phone pool is a container for the origination identities you send from. It groups identities that share the same settings, maps each message to an appropriate identity for the destination country, and fails over to another identity in the pool if one is unavailable. Using a pool is the recommended way to send, because you can send through a pool in every send API request, such as `SendTextMessage`, `SendMediaMessage`, `SendVoiceMessage`, and `SendRcsMessage`, and you can add or change origination identities later without changing your sending code.

You create a pool with a first origination identity, so Create the pool with the MMS-capable phone number from Step 1 as its first origination identity, and add more identities to the pool later. For more information about creating and managing phone pools, see [Phone pools](nx-features-phone-pools.md).

To create a pool from the console or the AWS CLI, choose the tab that matches how you want to work.

------
#### [ Console ]

**To create a pool (console)**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. In the navigation pane, under **Configurations**, choose **Phone pools**, and then choose **Create phone pool**.

1. For **Pool name**, enter a name. For the first origination identity, choose the phone number you requested in Step 1, then choose **Create phone pool**.

1. To add more numbers to the pool later, open the pool and choose **Add originator to pool**. Every number you add must have the same settings (such as two-way messaging) as the first number in the pool.

------
#### [ AWS CLI ]

Use the [create-pool](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/create-pool.html) command, passing the number from Step 1 as {{originationIdentity}}. To add more identities to an existing pool later, use [associate-origination-identity](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/associate-origination-identity.html).

```
$ aws pinpoint-sms-voice-v2 create-pool \
> --origination-identity {{originationIdentity}} \
> --iso-country-code {{XX}} \
> --message-type {{TRANSACTIONAL}}
```

To add another number to an existing pool, use [associate-origination-identity](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/associate-origination-identity.html). Replace {{poolId}} with the pool and {{originationIdentity}} with the number to add.

```
$ aws pinpoint-sms-voice-v2 associate-origination-identity \
> --pool-id {{poolId}} \
> --origination-identity {{originationIdentity}} \
> --iso-country-code {{XX}}
```

**Important**  
Every number you add to a pool must have the same settings as the first number you used to create the pool. For example, if the first number has two-way messaging enabled, every other number you add must also have two-way messaging enabled, or the association fails.

------