# Add a phone number or sender ID to a phone pool

Follow these directions to add a phone number or sender ID to a phone pool. The configuration of every phone number or sender ID that you add to a pool has to match the
configuration of the phone pool. For example, if you create a pool and the first phone number added has two-way messaging enabled, the other phone numbers that you add to the pool must also have
two-way messaging enabled.

Add a phone number or sender ID to a pool (Console)
To add a phone number or sender ID to a pool using the AWS End User Messaging SMS console, follow
these steps:

###### Add a phone number or sender ID (Console)

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Configurations**,
   choose **Phone pools**.
3. On the **Phone Pools** page, choose the phone pool to
   add the origination identity to.
4. On the **Associated pool originators** tab, choose
   **Add originator**.
5. Choose one of the following options:
   - **Phone number** – If you choose this
     option, under the **Phone numbers available for
     association** section, do the following:
     - Choose a phone number to add to the phone pool.

   - **Sender ID** – If you
     choose this option, under the **Sender IDs available for
     association** section, do the following:
     - Choose a sender ID to add the phone pool.

6. Choose **Add originator to pool**.

Add a phone number or sender ID to a pool (AWS CLI)You can use the [associate-origination-identity](../../../cli/latest/reference/pinpoint-sms-voice-v2/associate-origination-identity.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/associate-origination-identity.md") CLI to add
phone numbers or sender IDs to an existing pool.

The configuration of every phone number or sender ID that you add to a pool has to match the
configuration of the first phone number or sender ID that you specified when you created the
pool. For example, if you create a pool that contains a phone number that has two-way messaging
enabled, the other numbers that you add to the pool must also have two-way messaging
enabled.

###### To add a phone number or sender ID to a pool using the AWS CLI

- At the command line, enter the following command:

```
`$` aws pinpoint-sms-voice-v2 associate-origination-identity \
`>` --pool-id `poolId` \
`>` --origination-identity `originationIdentity` \
`>` --iso-country-code `US`
```

In the preceding command, make the following changes:

    + Replace `poolId` with the ID or Amazon
     Resource Name (ARN) of the pool that you want to add the origination
     identity to.
    + Replace `originationIdentity` with the unique
     ID or Amazon Resource Name (ARN) of the phone number or sender ID that
     you want to add to the pool.
    + Replace `+12065550142` with the origination
     identity that you want to add to the pool. This value can be a short
     code, a phone number, or a sender ID.
    + Replace `US` with the two-letter ISO-3166
     alpha-2 code for the country of the origination identity.

List origination identities (AWS CLI)
You can use the [list-pool-origination-identities](../../../cli/latest/reference/pinpoint-sms-voice-v2/list-pool-origination-identities.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/list-pool-origination-identities.md") CLI to view information about all of the
origination identities that have been added to a specific pool.

###### To view a list of origination IDs in a pool using the AWS CLI

- At the command line, enter the following command:

```
`$` aws pinpoint-sms-voice-v2 list-pool-origination-identities \
`>` --pool-id `pool-78ec067f62f94d57bd3bab991example`
```

In the preceding command, replace `poolId` with the ID or Amazon
Resource Name (ARN) of the pool.
