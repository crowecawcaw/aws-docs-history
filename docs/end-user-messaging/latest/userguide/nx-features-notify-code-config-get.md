

# Get a notify code configuration
<a name="nx-features-notify-code-config-get"></a>

View a single notify code configuration to see its passcode policy, channel templates, deletion protection setting, and identifiers.

------
#### [ AWS Management Console ]

**To get a notify code configuration using the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Notify**, choose **Code configurations**.

1. Choose the configuration **Name** to open its detail page.

1. On the **Configuration details** and **Settings** areas, review the ID, ARN, code type, length, validity, maximum attempts, deletion protection, and the per-channel templates.

------
#### [ AWS CLI ]

**To get a notify code configuration using the AWS CLI**
+ At the command line, enter the following command:

  ```
  $ aws endusermessaging get-notify-code-configuration \
  > --notify-code-configuration {{cc-3bnvvqhwq05xr3fkj}}
  ```

  Replace {{cc-3bnvvqhwq05xr3fkj}} with the ID or ARN of the notify code configuration.

------