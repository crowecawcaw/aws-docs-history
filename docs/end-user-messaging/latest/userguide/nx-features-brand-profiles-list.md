

# List brand profiles
<a name="nx-features-brand-profiles-list"></a>

List all of the brand profiles in your account and AWS Region. Each entry includes the profile name, ID, status, and creation date.

------
#### [ AWS Management Console ]

**To list brand profiles using the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, choose **Brand profiles**.

1. The **Brand profiles** page lists every brand profile in the current AWS Region, with its **Name**, **Brand profile ID**, **Status**, and **Creation date**. Use **Find brand profiles** to filter the list.

------
#### [ AWS CLI ]

**To list brand profiles using the AWS CLI**
+ At the command line, enter the following command:

  ```
  $ aws endusermessaging list-brand-profiles
  ```

  To page through large result sets, use **--max-results** and the **--next-token** value returned in the response.

------