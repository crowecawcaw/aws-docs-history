

# Update a notify code configuration
<a name="nx-features-notify-code-config-update"></a>

Update a notify code configuration to change its passcode policy, channel templates, name, or deletion protection setting. The updated policy applies to new verifications; verifications already in progress keep the policy captured when they were sent.

------
#### [ AWS Management Console ]

**To update a notify code configuration using the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Notify**, choose **Code configurations**.

1. Choose the configuration **Name** to open its detail page, then choose **Edit**.

1. Change the passcode policy, channel templates, or name, then save. To change deletion protection, use the **Deletion protection** tab.

------
#### [ AWS CLI ]

**To update a notify code configuration using the AWS CLI**
+ At the command line, enter the following command:

  ```
  $ aws endusermessaging update-notify-code-configuration \
  > --notify-code-configuration {{cc-3bnvvqhwq05xr3fkj}} \
  > --code-configuration-parameters codeLength=8,validityPeriodMinutes=15
  ```

  In the preceding command, make the following changes:
  + Replace {{cc-3bnvvqhwq05xr3fkj}} with the ID or ARN of the configuration.
  + Set the policy fields in **--code-configuration-parameters** and channel templates in **--channel-parameters** that you want to change.

------