

# Step 3: Set up a phone pool (optional)
<a name="nx-rcs-gsu-pool"></a>

For RCS, the sending identity is your AWS RCS Agent, so you can send RCS messages directly to the agent without a phone pool. A phone pool is optional for RCS and is used to enable SMS fallback: you create a pool that contains your AWS RCS Agent together with one or more SMS phone numbers, so that AWS End User Messaging automatically falls back to SMS when RCS delivery is not possible. For more information about creating and managing phone pools, see [Phone pools](nx-features-phone-pools.md). For how fallback works and how to configure it, see [Resiliency](nx-rcs-scale-fallback.md).

To create a pool from the console or the AWS CLI, choose the tab that matches how you want to work.

------
#### [ Console ]

**To create a pool for SMS fallback (console)**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. In the navigation pane, under **Configurations**, choose **Phone pools**, and then choose **Create phone pool**.

1. For **Pool name**, enter a name. For the first origination identity, choose your AWS RCS Agent, then choose **Create phone pool**.

1. Open the pool and choose **Add originator to pool**, then add one or more SMS phone numbers to use for fallback. Every identity you add must have the same settings as the first identity in the pool.

------
#### [ AWS CLI ]

Use the [create-pool](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/create-pool.html) command, passing your AWS RCS Agent as {{originationIdentity}}. To add the SMS numbers for fallback, use [associate-origination-identity](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/associate-origination-identity.html).

```
$ aws pinpoint-sms-voice-v2 create-pool \
> --origination-identity {{rcsAgentId}} \
> --iso-country-code {{XX}} \
> --message-type {{TRANSACTIONAL}}
```

To add an SMS number to the pool for fallback, use [associate-origination-identity](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/associate-origination-identity.html). Replace {{poolId}} with the pool and {{originationIdentity}} with the SMS number to add.

```
$ aws pinpoint-sms-voice-v2 associate-origination-identity \
> --pool-id {{poolId}} \
> --origination-identity {{originationIdentity}} \
> --iso-country-code {{XX}}
```

**Important**  
Every identity you add to a pool must have the same settings as the first identity you used to create the pool.

------