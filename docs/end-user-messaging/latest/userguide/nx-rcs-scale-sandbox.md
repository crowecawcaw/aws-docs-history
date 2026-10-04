

# Move out of the sandbox
<a name="nx-rcs-scale-sandbox"></a>

Every new AWS RCS Agent starts in a testing state. In the testing state you can send RCS messages only to devices that you have added as testers, which lets you validate your integration before you reach real recipients. To send to any recipient, you move the agent out of testing by submitting a country launch registration for each country where you want to send, and waiting for carrier approval. This topic explains the testing state and the path to production.

**Topics**
+ [The testing state](#nx-rcs-scale-sandbox-testing)
+ [Add test devices](#nx-rcs-scale-sandbox-testers)
+ [Launch in production](#nx-rcs-scale-sandbox-launch)

## The testing state
<a name="nx-rcs-scale-sandbox-testing"></a>

When you create an AWS RCS Agent, you submit a testing registration at the same time. The testing registration creates an RCS for Business ID, also called a testing agent, that you use to send messages while you build and validate your integration. A testing agent is typically approved within minutes. While your agent is in the testing state, the following limits apply:
+ You can send only to phone numbers that you have added as test devices and that have accepted the tester invitation.
+ All RCS content types are available for testing, including text, rich cards, carousels, and suggested actions, so you can validate your full experience.

For the steps to create an agent and submit the testing registration, see [How to get set up](nx-rcs-get-set-up.md).

## Add test devices
<a name="nx-rcs-scale-sandbox-testers"></a>

Before you can receive messages from a testing agent, you add each phone as a test device and accept the tester invitation on that device. You can add a test device from the console on the agent's **Testing** tab under **RBM tester management**, or with the `CreateVerifiedDestinationNumber` operation using the `--rcs-agent-id` parameter.

After you add a test device, AWS End User Messaging sends a tester invitation to the phone number from an RCS agent named **RBM Tester Management**. The invitation contains two buttons, **Make me a tester** and **No thanks**. Choose **Make me a tester** to complete verification. The invitation is not sent immediately after you add the device. For the complete steps, see [How to get set up](nx-rcs-get-set-up.md).

## Launch in production
<a name="nx-rcs-scale-sandbox-launch"></a>

To send RCS messages to any recipient, rather than only to test devices, submit a country launch registration for each country where you want to send. Each country has its own registration form and requirements, and each carrier in that country reviews your agent independently, so approval timelines vary by country and carrier. When a country launch is approved, you can send to any recipient on an approved carrier in that country. For the supported countries and the per-country requirements, see [Country support](nx-rcs-scale-country.md).