

# Step 3: Request your own numbers (optional)
<a name="nx-notify-get-set-up-dedicated"></a>

By default, Notify sends messages using AWS-managed origination identities, so you do not need to provision any phone numbers. Complete this step only if you want to send from your own dedicated numbers. You request one or more phone numbers, add them to a phone pool, and associate the pool with your Notify configuration. When a pool is associated, Notify checks the pool for a customer-owned identity that supports the destination country first, and falls back to AWS-managed identities if none is found.

Using your own pool lets you send from dedicated short codes or toll-free numbers for specific countries, and any opt-out lists on the pool are respected. For some countries, AWS does not provide managed identities, so you must associate a pool with customer-owned numbers to send to those countries.

**To send from your own dedicated numbers**

1. Request one or more phone numbers for the countries you send to. For the number types available per country and the request steps, see [Phone numbers](nx-features-phone-numbers.md).

1. Create a phone pool and add your numbers to it. Every number you add to a pool must have the same settings as the first number used to create the pool. For example, if the first number has two-way messaging enabled, every other number you add must also have two-way messaging enabled. For more information, see [Phone pools](nx-features-phone-pools.md).

1. Associate the pool with your Notify configuration by choosing **Edit** on the configuration and selecting the pool, or by setting the associated pool with the `update-notify-configuration` command.