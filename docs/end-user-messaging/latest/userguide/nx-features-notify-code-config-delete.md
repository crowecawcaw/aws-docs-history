

# Delete a notify code configuration
<a name="nx-features-notify-code-config-delete"></a>

Delete a notify code configuration you no longer need. Verifications that are already in progress are unaffected because their policy was captured at send time. If deletion protection is enabled, turn it off before you delete.

------
#### [ AWS Management Console ]

**To delete a notify code configuration using the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Notify**, choose **Code configurations**.

1. Select the option button next to the configuration, or open its detail page.

1. Choose **Delete** and confirm.
**Note**  
If deletion protection is enabled, the delete fails until you disable it on the **Deletion protection** tab.

------
#### [ AWS CLI ]

**To delete a notify code configuration using the AWS CLI**
+ At the command line, enter the following command:

  ```
  $ aws endusermessaging delete-notify-code-configuration \
  > --notify-code-configuration {{cc-3bnvvqhwq05xr3fkj}}
  ```

  Replace {{cc-3bnvvqhwq05xr3fkj}} with the ID or ARN of the configuration. The request fails if deletion protection is enabled.

------