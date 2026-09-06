

# Enable outbound calls in your Connect Customer instance
<a name="enable-outbound-calls"></a>

Before your agents can make outbound calls to customers, you need to set up your Connect Customer instance for outbound communications.

1. Open the Connect Customer console at [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/).

1. On the instances page, choose the instance alias. The instance alias is also your **instance name**, which appears in your Connect Customer URL. The following image shows the **Connect Customer virtual contact center instances** page, with a box around the instance alias.  
![The Connect Customer virtual contact center instances page, the instance alias.](http://docs.aws.amazon.com/connect/latest/adminguide/images/instance.png)

1. In the navigation pane, choose **Telephony under Channels and communications**.

1. To enable outbound calling from your contact center, choose **Make outbound calls with Connect Customer**.

1. To enable outbound campaigns, choose **Enable outbound campaigns**.

1. By enabling early media audio, your agents can hear pre-connection audio such as busy signals, failure-to-connect errors, or other informational messages from telephony providers, when making outbound calls. Choose **Enable early media**.

1. Choose **Save**.

1. Ensure agents have the **Contact Control Panel (CCP) - Make outbound calls** permission in their security profile. For instructions, see [Assign a security profile for Connect Customer to a contact center user](assign-security-profile.md).

**Note**  
For a list of countries you can call **by default** based on the Region of your instance, see [Countries that call centers using Connect Customer can call by default](country-code-allow-list.md).  
For a list of all countries available for outbound calls based on the Region of your instance, see [Connect Customer pricing](https://aws.amazon.com/connect/pricing/). If a country is not available in your dropdown menu, open a ticket to add it to your allowlist. 