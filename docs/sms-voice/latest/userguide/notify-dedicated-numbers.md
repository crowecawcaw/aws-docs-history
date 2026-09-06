

# Using dedicated numbers with Notify
<a name="notify-dedicated-numbers"></a>

By default, Notify uses AWS-managed origination identities to send messages. You can optionally associate an existing phone pool with your Notify configuration to use your own dedicated phone numbers alongside AWS-managed identities.

**Note**  
For some countries, AWS does not provide managed origination identities. In these cases, you must associate your own phone pool with customer-owned numbers to send messages to those countries. Use the `ListNotifyCountries` API or the console Countries tab to check which countries require customer-owned identities.

## How hybrid routing works
<a name="notify-dedicated-numbers-routing"></a>

When you associate a phone pool with a Notify configuration, the system uses the following routing logic for each message:

1. Check the associated pool for a customer-owned origination identity that supports the destination country.

1. If a matching identity is found, use it to send the message.

1. If no matching identity is found (or no pool is associated), fall back to AWS-managed identities.

## Benefits of associating a pool
<a name="notify-dedicated-numbers-benefits"></a>
+ Use your own dedicated short codes or toll-free numbers for specific countries.
+ Existing opt-out lists on the pool are respected.

## Managing pool association
<a name="notify-dedicated-numbers-manage"></a>

------
#### [ Console ]

**Associate a pool**

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. Navigate to a Notify configuration and choose the **Use Dedicated Numbers** tab.

1. Choose **Associate pool**.

1. Select a pool from the table and choose **Associate pool**.

**Disassociate a pool**

1. On the **Use Dedicated Numbers** tab, choose **Disassociate pool**.

1. Type `confirm` in the confirmation field and choose **Disassociate pool**.

------
#### [ AWS CLI ]

Associate a pool:

```
aws pinpoint-sms-voice-v2 update-notify-configuration \
  --notify-configuration-id {{nc-1234567890abcdef0}} \
  --pool-id {{pool-1234567890abcdef0}}
```

Disassociate a pool:

```
aws pinpoint-sms-voice-v2 update-notify-configuration \
  --notify-configuration-id {{nc-1234567890abcdef0}} \
  --pool-id UNSET_DEFAULT_POOL_FOR_NOTIFY
```

------

**Note**  
The pool must exist in the same AWS account. You can change or remove the pool association at any time.