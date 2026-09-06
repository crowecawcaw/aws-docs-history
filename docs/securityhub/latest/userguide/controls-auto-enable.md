

# Enabling new controls in enabled standards automatically
<a name="controls-auto-enable"></a>

AWS Security Hub CSPM regularly releases new controls and adds them to one or more standards. You can choose whether to automatically enable new controls in your enabled standards.

We recommend using Security Hub CSPM central configuration to automatically enable new security controls. You can create configuration policies that include a list of controls to be disabled across standards. All other controls, including newly released ones, are enabled by default. Alternatively, you can create policies that include a list of controls to be enabled across standards. All other controls, including newly released ones, are disabled by default. For more information, see [Understanding central configuration in Security Hub CSPM](central-configuration-intro.md).

Security Hub CSPM doesn't enable new controls when they are added to a standard that you haven't enabled.

The following instructions apply only if you don't use central configuration.

Choose your preferred access method, and follow the steps to automatically enable new controls in enabled standards.

**Note**  
When you automatically enable new controls using the following instructions, you can interact with the controls in the console and programmatically immediately after release. However, automatically enabled controls have a temporary default status of **Disabled**. It can take up to several days for Security Hub CSPM to process the control release and designate the control as **Enabled** in your account. During the processing period, you can manually enable or disable a control, and Security Hub CSPM will maintain that designation regardless of whether you have automatic control enablement turned on.

------
#### [ Security Hub CSPM console ]

**To automatically enable new controls**

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/).

1. In the navigation pane, choose **Settings**, and then choose the **General** tab.

1. Under **Controls**, choose **Edit**.

1. Turn on **Auto-enable new controls in enabled standards**.

1. Choose **Save**.

------
#### [ Security Hub CSPM API ]

**To automatically enable new controls**

1. Run [`UpdateSecurityHubConfiguration`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateSecurityHubConfiguration.html).

1. To automatically enable new controls for enabled standards, set `AutoEnableControls` to `true`. If you don't want to automatically enable new controls, set `AutoEnableControls` to false.

------
#### [ AWS CLI ]

**To automatically enable new controls**

1. Run the [`update-security-hub-configuration`](https://docs.aws.amazon.com/cli/latest/reference/securityhub/update-security-hub-configuration.html) command.

1. To automatically enable new controls for enabled standards, specify `--auto-enable-controls`. If you don't want to automatically enable new controls, specify `--no-auto-enable-controls`.

   ```
   aws securityhub update-security-hub-configuration --auto-enable-controls | --no-auto-enable-controls
   ```

   **Example command**

   ```
   aws securityhub update-security-hub-configuration --auto-enable-controls
   ```

------

If you don't automatically enable new controls, then you must enable them manually. For instructions, see [Enabling controls in Security Hub CSPM](securityhub-standards-enable-disable-controls.md).