

# Attach a claimed or ported phone number to a flow in Connect Customer
<a name="associate-claimed-ported-phone-number-to-flow"></a>

After you publish a flow, you can attach a [claimed](get-connect-number.md) or [ported](port-phone-number.md) phone number to it. When a contact calls the phone number that you associate with a flow, they are connected to that flow.

**To associate a claimed or ported phone number with a published flow**

1. Log in to your Connect Customer instance (https://{{instance name}}.my.connect.aws/) with an Admin account or a user account that has **Phone number - Edit** permissions in it's [security profile](connect-security-profiles.md). (To find the name of your instance, see [Find your Connect Customer instance ID or ARN](find-instance-arn.md).)

1. On the navigation menu, choose **Channels**, **Phone numbers**.

1. Locate the phone number to associate with the flow in the list. Choose the phone number to open the **Edit Phone number** page. The following image shows a sample phone number that you would choose.  
![A sample phone number on the Phone number page.](http://docs.aws.amazon.com/connect/latest/adminguide/images/choose-on-phone-number.png)

1. On the **Edit Phone number** page, do the following:

   1. (Optional) Edit the description for the phone number.

   1. For **Flow / IVR**, select the flow. Note that only published flows are included in this list.

   1. Choose **Save**.