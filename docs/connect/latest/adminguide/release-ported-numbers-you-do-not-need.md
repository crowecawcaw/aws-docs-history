# Release numbers that

you ported to Amazon Connect that you no longer need

You do not have to keep phone numbers assigned to your Amazon Connect instance.

When a phone number is released from your Amazon Connect instance:

- You will no longer be charged for it.
- You cannot
  reclaim the phone number.
- Amazon Connect
  reserves the right to allow it to be claimed by another customer.

###### To release a phone number

1. Log in to Amazon Connect admin website with an Admin account or a user account that has **Phone numbers - Release** security profile permission.
2. On the navigation menu, choose **Channels**, **Phone
   numbers**. This option appears only if you have the **Phone numbers - View**
   permission in your
   security profile.
3. Choose the phone number you want to release, and then choose
   **Release**. This option appears only if you have the **Phone numbers - Release** permission in your
   security profile.
   If the phone number is associated with a flow, that flow will be deactivated
   until another number is associated with it.

When customers call the phone number you have released, they will get a message that it is
not a working phone number.
