

# List brand profile attributes
<a name="nx-features-brand-profiles-attr-list"></a>

List every attribute on a brand profile. Each entry includes the attribute name, type, category, and when it was last updated.

------
#### [ AWS Management Console ]

**To list brand profile attributes using the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. Open the brand profile detail page and choose the **Attributes** tab.

1. The **Attributes** table lists every attribute on the profile with its name, category, description, and last-updated time. Use **Find attributes** to filter.

------
#### [ AWS CLI ]

**To list brand profile attributes using the AWS CLI**
+ At the command line, enter the following command:

  ```
  $ aws endusermessaging list-brand-profile-attributes \
  > --brand-profile-id {{bp-gkma20fagojtpys0e}}
  ```

  Replace {{bp-gkma20fagojtpys0e}} with the ID or ARN of the brand profile. Use **--max-results** and **--next-token** to page through results.

------