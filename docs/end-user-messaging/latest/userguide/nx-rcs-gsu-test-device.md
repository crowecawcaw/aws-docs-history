

# Step 2: Add a test device
<a name="nx-rcs-gsu-test-device"></a>

After your testing registration is approved, add your phone as a test device so you can receive RCS messages from your testing agent.

**Note**  
After you add a test device, the tester invitation is not sent immediately. The system delays activation for at least 120 seconds, and it can take up to 20 minutes for the invitation to arrive. The console shows an approximate activation time. You do not need to wait before adding the device – the system handles the delay automatically.

------
#### [ Console ]

**To add a test device**

1. In the AWS End User Messaging console, navigate to your AWS RCS Agent and choose the **Testing** tab.

1. Choose the **RBM tester management** sub-tab.

1. Choose **Add RBM tester**.

1. Enter the phone number of your test device in E.164 format (for example, `+12065550100`).

1. Choose **Send verification code**.

------
#### [ AWS CLI ]

Use the `CreateVerifiedDestinationNumber` API with the `--rcs-agent-id` parameter to register a test device for your AWS RCS Agent:

```
aws pinpoint-sms-voice-v2 create-verified-destination-number \
    --destination-phone-number +12065550100 \
    --rcs-agent-id rcs-a1b2c3d4
```

------

After you add the test device, AWS End User Messaging sends a tester invitation to the phone number. The invitation comes from an RCS agent called **RBM Tester Management** and contains two buttons to accept or decline: **Make me a tester** and **Decline**. The recipient must tap **Make me a tester** to complete verification.

**Note**  
On iOS devices (iPhone with iOS 18 or later), the tester invitation may appear in the **Unknown Senders** folder in the Messages app rather than the main inbox. If you don't see the invitation, check the Unknown Senders folder.