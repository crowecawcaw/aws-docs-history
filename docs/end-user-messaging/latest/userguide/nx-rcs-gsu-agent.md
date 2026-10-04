

# Step 1: Create an AWS RCS test agent
<a name="nx-rcs-gsu-agent"></a>

The first step is to create an AWS RCS Agent and submit a testing registration. The testing registration creates an RCS for Business ID (testing agent) that you can use to send messages to registered test devices without carrier approval.

------
#### [ Console ]

**To create an AWS RCS Agent and submit a testing registration**

1. Open the [AWS End User Messaging console](https://console.aws.amazon.com/sms-voice/home).

1. In the navigation pane, under **Configurations**, choose **RCS agents**.

1. Choose **Create RCS Agent**. This creates an AWS RCS Agent and then immediately guides you through creating a testing registration in a single workflow.

1. The next screen shows an introduction to RCS and explains the setup process. Review the information and choose **Next** to continue.

1. On the **Agent details** page, set the following:
   + **Friendly name** – A console-only label for your AWS RCS Agent. This is an internal name for your reference (stored as a tag) and is not the name displayed on recipients' phones. The friendly name is not available through the API.
   + **Deletion protection** – (Optional) Enable to prevent accidental deletion of the agent.
   + **Tags** – (Optional) Add tags to organize and identify your agent.

1. In the **Brand information** section of the same page, enter the following:
   + **Display name** – The brand name that recipients see alongside your RCS messages.
   + **Description** – A brief description of your brand or business.
   + **Use case** – Select the primary use case for your RCS messaging (for example, transactional notifications, marketing, or customer support).

1. In the **Brand assets** section of the same page, upload the following:
   + **Logo** – 224 x 224 pixels, PNG with transparency, under 50 KB.
   + **Banner image** – 1440 x 448 pixels, PNG or JPEG, under 200 KB.
   + **Brand color** – A hex color code (for example, `#1A73E8`) with a minimum contrast ratio of 4.5:1 against a white background.
**Important**  
Some brand assets cannot be changed after the agent is submitted for registration. Prepare your final brand assets before creating the agent. If you want to experiment first, you can quickly create a test agent using this flow, then create a fresh AWS RCS Agent with finalized brand assets later.

1. On the **Compliance keywords** page, configure your keywords and auto-response messages.

1. On the **Review** page, verify all your settings.

1. Choose **Validate and submit** to create the AWS RCS Agent and submit the testing registration.

**Note**  
You have successfully created an AWS RCS Agent and submitted a testing registration. Your testing agent is typically approved within minutes. Now enable test messaging to your device.

------
#### [ AWS CLI ]

You can also create an AWS RCS Agent using the AWS CLI. First, create the agent, then submit a testing registration.

Create the AWS RCS Agent:

```
aws pinpoint-sms-voice-v2 create-rcs-agent \
    --deletion-protection-enabled
```

Submit a testing registration for the agent. Use the `CreateRegistration` API with the registration type for RCS testing. You can use the `DescribeRegistrationFieldDefinitions` API to programmatically retrieve all available registration form fields before submitting. Provide your brand assets, description, and contact details as part of the registration form fields.

------