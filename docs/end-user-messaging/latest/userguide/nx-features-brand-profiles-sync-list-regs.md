

# List registrations from a brand profile
<a name="nx-features-brand-profiles-sync-list-regs"></a>

List the registrations that are associated with a brand profile. Each entry shows the registration ID, registration type, whether smart match was used, and when the association was created.

------
#### [ AWS Management Console ]

**To list registrations from a brand profile using the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. Open the brand profile detail page and choose the **Associated registrations** tab.

1. The **Associated registrations** table lists each associated registration with its **Registration ID**, **Registration type**, **Smart match used**, and **Created** date.

------
#### [ AWS CLI ]

**To list registrations from a brand profile using the AWS CLI**
+ At the command line, enter the following command:

  ```
  $ aws endusermessaging list-registrations-from-brand-profile \
  > --brand-profile-id {{bp-gkma20fagojtpys0e}}
  ```

  Replace {{bp-gkma20fagojtpys0e}} with the ID or ARN of the brand profile. Use **--max-results** and **--next-token** to page through results.

------