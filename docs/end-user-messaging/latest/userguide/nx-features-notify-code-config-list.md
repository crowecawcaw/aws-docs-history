

# List notify code configurations
<a name="nx-features-notify-code-config-list"></a>

List the notify code configurations in your account and AWS Region. Each entry shows the name, ID, code type, code length, and creation date.

------
#### [ AWS Management Console ]

**To list notify code configurations using the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Notify**, choose **Code configurations**.

1. The **Code configurations** page lists every configuration with its **Name**, **Code configuration ID**, **Code type**, **Code length**, and **Creation date**. Use **Find code configurations** to filter.

------
#### [ AWS CLI ]

**To list notify code configurations using the AWS CLI**
+ At the command line, enter the following command:

  ```
  $ aws endusermessaging list-notify-code-configurations
  ```

  Use **--max-results** and **--next-token** to page through results.

------