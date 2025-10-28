# Enable outbound calls in your Amazon Connect

instance

Before your agents can make outbound calls to customers, you need to set up your Amazon Connect
instance for outbound communications.

1. Open the Amazon Connect console at
   [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/ "https://console.aws.amazon.com/connect/").
2. On the instances page, choose the instance alias. The instance alias is also
   your **instance name**, which appears in your Amazon Connect
   URL. The following image shows the **Amazon Connect virtual contact center instances** page, with a box
   around the instance alias.

![The Amazon Connect virtual contact center instances page, the instance alias.](images/instance.png) 3. In the navigation pane, choose **Telephony under Channels and
communications**. 4. To enable outbound calling from your contact center, choose **Make
outbound calls with Amazon Connect**. 5. To enable outbound campaigns, choose **Enable outbound campaigns**. 6. By enabling early media audio, your agents can hear pre-connection audio such
as busy signals, failure-to-connect errors, or other informational messages from
telephony providers, when making outbound calls. Choose **Enable early
media**. 7. Choose **Save**. 8. Ensure agents have the **Contact Control Panel (CCP) - Make outbound
calls** permission in their security profile. For instructions, see
[Assign a security profile for Amazon Connect to a
contact center user](assign-security-profile.md "assign-security-profile.md").

###### Note

For a list of countries you can call **by default**
based on the Region of your instance, see [Countries that call centers using Amazon Connect can
call by default](country-code-allow-list.md "country-code-allow-list.md").

For a list of all countries available for outbound calls based on the Region of
your instance, see [Amazon Connect
pricing](https://aws.amazon.com/connect/pricing/ "https://aws.amazon.com/connect/pricing/"). If a country is not available in your dropdown menu, open a
ticket to add it to your allowlist.
