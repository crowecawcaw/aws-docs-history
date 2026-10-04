

# Update a brand profile from a registration
<a name="nx-features-brand-profiles-sync-update-bp"></a>

Import brand attributes from an existing registration into a brand profile you already have. The registration must be in the `COMPLETE` status. Attributes are imported asynchronously; choose how conflicts are resolved when the profile already has a matching attribute.

------
#### [ AWS Management Console ]

**To update a brand profile from a registration using the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. Open the brand profile detail page and choose the **Attributes** tab, then choose **Import from registration**.

1. On **Import attributes from registration**, for **Registration** choose a registration (only registrations with status `COMPLETE` are listed). Leave **Smart match** enabled.

1. For **On attribute conflict**, choose **Replace** (overwrite the existing value) or **Preserve** (keep the existing value).

1. Choose **Submit**.

------
#### [ AWS CLI ]

**To update a brand profile from a registration using the AWS CLI**
+ At the command line, enter the following command:

  ```
  $ aws endusermessaging update-brand-profile-from-registration \
  > --brand-profile-id {{bp-gkma20fagojtpys0e}} \
  > --registration-id {{reg-abc123}} \
  > --on-attribute-conflict {{REPLACE}}
  ```

  In the preceding command, make the following changes:
  + Replace the brand profile ID and registration ID placeholders.
  + Set **--on-attribute-conflict** to `REPLACE` or `PRESERVE`.

------

This operation runs asynchronously and returns a job ID for each registration. Track the job on the **Jobs** tab of the brand profile, or with the **GetJob** operation (see [Track brand profile jobs](nx-features-brand-profiles-sync-jobs.md)).