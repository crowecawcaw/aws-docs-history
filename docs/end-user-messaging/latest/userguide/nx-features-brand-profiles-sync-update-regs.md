

# Update registrations from a brand profile
<a name="nx-features-brand-profiles-sync-update-regs"></a>

Update registrations that are already associated with a brand profile so they pick up the profile's current attribute values. Choose how conflicts are resolved when a registration field already has a value.

------
#### [ AWS Management Console ]

**To update registrations from a brand profile using the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. Open the brand profile detail page, choose **Actions**, and start a job.

1. On **Choose job type**, choose **Registration**, then **Next**.

1. On **Configure job**, for **Registration source** choose **Update existing registrations**. Select the registrations to update (up to 10). For **Attribute conflict resolution**, choose **Replace** (overwrite with the profile value) or **Preserve** (keep the existing value).

1. Choose **Next**, review, and choose **Create**.

------
#### [ AWS CLI ]

**To update registrations from a brand profile using the AWS CLI**
+ At the command line, enter the following command:

  ```
  $ aws endusermessaging update-registrations-from-brand-profile \
  > --brand-profile-id {{bp-gkma20fagojtpys0e}} \
  > --registration-ids {{reg-abc123}} \
  > --on-attribute-conflict {{REPLACE}}
  ```

  In the preceding command, make the following changes:
  + Replace the brand profile ID placeholder.
  + In **--registration-ids**, list 1–10 registrations to update.
  + Set **--on-attribute-conflict** to `REPLACE` or `PRESERVE`.

------

This operation runs asynchronously and returns a job ID for each registration. Track the job on the **Jobs** tab of the brand profile, or with the **GetJob** operation (see [Track brand profile jobs](nx-features-brand-profiles-sync-jobs.md)).