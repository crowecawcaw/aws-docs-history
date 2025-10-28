# Send a test message for Apple Messages for Business to test integration

with Amazon Connect

After onboarding to the Apple Messages for Business account, use the following steps to send a test message
to make sure the integration is set up properly.

## Step 1: Add internal testers to your Messages for Business

account

1. Sign in to [Apple Business
   Register](https://register.apple.com/ "https://register.apple.com/").
2. Choose **Messages for Business Accounts** and select the account to add
   testers.
3. Scroll down the page to **Account Testing**.
4. Add the Apple IDs of your internal testers.
5. When your list is complete and you are ready to begin testing, choose
   **Send to new testers** to send an instructional email
   to your testers.

An instructional email containing a link to your Messages for Business conversation is sent to the
Apple ID email address of each tester. If a tester does not receive the email, then
recheck that their email address is provided in the Account Testing section. It's
most likely that the email address is incorrect or it's not an Apple ID. For
security reasons, Apple cannot verify Apple ID email addresses.

## Step 2: Test sending and receiving

messages

When your testers get the instructional email, they will need to activate the link
in it. After doing this, they can send messages to your agents, who can then reply
from the Contact Control Panel (CCP).

Note the following:

1. Design a test to trigger all of your Apple Messages for Business features.
2. You should observe that messages sent from an iOS device arrive to your
   test business. Employees testing from your support agent desktop should be
   able to respond to these test messages.
3. Your testers may notice your brand colors are not visible in the Messages
   header. Brand color is not available while your account is in test mode. The
   colors for your brand will display correctly after your account goes online.
4. If you send the testing link to someone whose email is not listed in the
   Account Testing section, they will not be able to send messages.
5. If you provide a Redirect Page URL and your testers try to enter Messages for Business from
   an unsupported device, they will land either on a default or redirected
   page. You can set your Redirect Page URL in the **Unsupported
   Devices** section at the bottom of your Messages for Business account
   page.

###### To begin testing

1. Check that your testers are using a device with a supported iOS: iOS 11.3
   and later, or macOS 10.13.4.
2. Ask your testers to doing the following:
   1. Use their supported devices to find the email sent to them.
   2. Open the email from the supported device, and then choose the
      link. It takes them to a Messages for Business conversation in the Messages
      app.

## Troubleshoot

If you encounter any issues when sending a test message, follow these steps:

1.  Confirm that you’ve allowlisted your email address/Apple ID as a tester in
    your Messages for Business account.
2.  Confirm the following settings on your Apple device:
    - Go to **Settings** >
      **Messages** and check that
      **iMessage** is enabled.
    - Go to **Settings** >
      **Messages** > **Send &
      Receive** and check that the AppleID is correct and
      messages are allowed to receive.

3.  Check that you're using a supported iOS. Apple devices running iOS 11.3
    and later or macOS 10.13.4 and later support Messages for Business.
4.  When you selected Amazon Connect as your MSP in your Apple Account, did you select
    **Amazon Connect** from the dropdown? Or did you enter
    the following URL:

        * https://messagingintegrations.connect.amazonaws.com/applebusinesschat

    If you entered the URL, doublecheck for typos.

5.  Confirm your Apple business account is **Online** in the
    [Apple Business
    Register](https://register.apple.com/ "https://register.apple.com/"). If the account is in a pending state, then select
    **Send for review**. This needs to be repeated after
    making additional Apple ID allow-listing changes or other Apple business
    account configuration changes.
