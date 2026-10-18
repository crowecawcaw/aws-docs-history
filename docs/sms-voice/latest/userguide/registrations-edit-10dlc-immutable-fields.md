

# Immutable 10DLC campaign fields
<a name="registrations-edit-10dlc-immutable-fields"></a>

Certain 10DLC campaign fields are permanently locked by The Campaign Registry (TCR) after initial submission. These fields cannot be modified regardless of whether the campaign is approved, denied, or in a **Requires Updates** state. If you attempt to change one of these fields during resubmission, the update is rejected with the following error:

```
"Cannot update registration: If you wish to modify certain 10DLC campaign
fields, or edit an already approved 10DLC campaign, you must instead create
a new 10DLC campaign registration."
```

The following 10DLC campaign fields cannot be changed after submission:
+ **Use case type** – The campaign use case category (for example, 2FA, marketing, or customer care).
+ **Sub-use cases** – Any sub-use case categories associated with the campaign.
+ **Opt-in message** – The message sent to subscribers when they opt in to the campaign.
+ **Opt-out message** – The message sent to subscribers when they opt out of the campaign.
+ **Help message** – The message sent to subscribers when they send a HELP keyword.

If you need to change any of these fields, you must delete the existing 10DLC campaign registration and create a new one with the correct values. For more information, see [Editing or deleting a 10DLC campaign](registrations-10dlc-modify-campaign.html).

**Important**  
Verify that use case type, sub-use cases, and subscriber message fields are correct before submitting your 10DLC campaign registration. These fields are enforced by TCR and cannot be modified by AWS after submission.