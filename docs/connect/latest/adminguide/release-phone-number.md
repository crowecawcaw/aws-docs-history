

# Release a phone number from Connect Customer back to inventory
<a name="release-phone-number"></a>

If you want a different phone number, or have extra numbers that you aren't using, you can release them back to inventory. You can do this using the Connect Customer console, or programmatically by using the [ReleasePhoneNumber](https://docs.aws.amazon.com/connect/latest/APIReference/API_ReleasePhoneNumber.html) API.

When a phone number is released from your Connect Customer instance:
+ You will no longer be charged for it.
+ You cannot reclaim the phone number.
+ Connect Customer reserves the right to allow it to be claimed by another customer.

**Tip**  
If you want to close your Connect Customer account, do these steps for all of your phone numbers. This will make sure you aren't billed if people erroneously call numbers that you've claimed, and initiate your flows. You might also want to [delete your instances.](delete-connect-instance.md) 

**To release a phone number**

1. Log in to Connect Customer admin website with an Admin account or a user account that has **Phone numbers - Release** security profile permission. 

1. On the navigation menu, choose **Channels**, **Phone numbers**. This option appears only if you have the **Phone numbers - View** permission in your security profile.

1. Choose the phone number you want to release, and then choose **Release**. This option appears only if you have the **Phone numbers - Release** permission in your security profile.

If the phone number is associated with a flow, that flow will be deactivated until another number is associated with it.

When customers call the phone number you have released, they will get a message that it is not a working phone number. 

**To use the ReleasePhoneNumber API**
+ Releasing a number by using the [ReleasePhoneNumber](https://docs.aws.amazon.com/connect/latest/APIReference/API_ReleasePhoneNumber.html) API puts the number in a cool down period for up to 180 days. The phone number cannot be searched for or claimed until after the cool down period ends.
**Note**  
You will not be billed for the phone number during the 180-day cool down period.

## Avoid being blocked from claiming or releasing too many numbers
<a name="avoid-being-blocked-releasing"></a>

If you plan to claim and release numbers frequently, contact us for a service quota exception. Otherwise, it's possible you will be blocked from claiming and releasing any more numbers until up to 180 days past the oldest number released has expired.

By default you can claim and release up to 200% of your maximum number of active phone numbers. If you claim and release phone numbers using the UI or API during a rolling 180 day cycle that exceeds 200% of your phone number service level quota, you will be blocked from claiming any more numbers until 180 days past the oldest number released has expired. 

For example, if you already have 99 claimed numbers and a service level quota of 99 phone numbers, and in any 180 day period you release 99, claim 99, and then release 99, you will have exceeded the 200% limit. At that point you are blocked from claiming any more numbers until you open an AWS support ticket.