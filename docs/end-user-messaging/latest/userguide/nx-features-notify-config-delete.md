

# Delete a Notify configuration
<a name="nx-features-notify-config-delete"></a>

Delete a Notify configuration you no longer need. If deletion protection is enabled, you must disable it before you can delete the configuration.

------
#### [ AWS Management Console ]

**To delete a Notify configuration using the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. Navigate to **Notify configurations**.

1. Select the configuration you want to delete.

1. Choose **Delete**, type **delete** in the confirmation field, and choose **Delete**.

------
#### [ AWS CLI ]

**To delete a Notify configuration using the AWS CLI**
+ At the command line, enter the following command:

  ```
  $ aws pinpoint-sms-voice-v2 delete-notify-configuration \
  > --notify-configuration-id {{nc-1234567890abcdef0}}
  ```

  Replace {{nc-1234567890abcdef0}} with the ID of the configuration. The request fails if deletion protection is enabled.

------