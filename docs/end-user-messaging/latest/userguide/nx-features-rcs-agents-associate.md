

# Associate a registration with an agent
<a name="nx-features-rcs-agents-associate"></a>

An AWS RCS Agent is gated by a registration. After you create the agent and create a registration (a testing registration or a country launch registration), you associate the registration with the agent so that AWS End User Messaging can review and approve it.

**To associate a registration with an agent using the AWS CLI**

1. Create the registration. For a testing agent, use the testing registration type.

   ```
   $ aws pinpoint-sms-voice-v2 create-registration \
   > --registration-type {{TEST_RCS_LAUNCH_REGISTRATION}}
   ```

   Save the registration ID from the response.

1. Associate the registration with the agent, replacing {{registrationId}} and {{rcs-agentId}} with your values.

   ```
   $ aws pinpoint-sms-voice-v2 create-registration-association \
   > --registration-id {{registrationId}} \
   > --resource-id {{rcs-agentId}}
   ```

1. Populate the registration fields, submit the registration version, and poll the registration and agent status until the testing agent status is `ACTIVE`. For the full setup walkthrough, see [How to get set up](nx-rcs-get-set-up.md).