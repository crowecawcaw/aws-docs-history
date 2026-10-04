

# Create registrations from a brand profile
<a name="nx-features-brand-profiles-sync-create-regs"></a>

Create one or more new registrations that are pre-filled from a brand profile. You choose the registration types and AWS End User Messaging starts a registration for each, mapping the profile's attributes onto the registration form fields. With smart match enabled, an AI model maps the fields semantically.

**Important**  
This operation creates draft registrations with the brand profile's attributes pre-filled, but it does not submit them. Review each registration, complete any remaining required fields, and submit it from the AWS End User Messaging console before it is processed.

------
#### [ AWS Management Console ]

**To create registrations from a brand profile using the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. Open the brand profile detail page, choose **Actions**, and start a job (the **Create job** wizard opens).

1. On **Choose job type**, choose **Registration**, then choose **Next**.

1. On **Configure job**, for **Registration source** choose **Create new registrations**. Choose the **Registration types** and a quantity for each (up to 10 registrations total). Leave **Smart match** enabled to let AI map the fields.

1. Choose **Next**, review, and choose **Create**.

------
#### [ AWS CLI ]

**To create registrations from a brand profile using the AWS CLI**
+ At the command line, enter the following command:

  ```
  $ aws endusermessaging create-registrations-from-brand-profile \
  > --brand-profile-id {{bp-gkma20fagojtpys0e}} \
  > --registration-types {{US_TOLL_FREE_REGISTRATION}}
  ```

  In the preceding command, make the following changes:
  + Replace {{bp-gkma20fagojtpys0e}} with the ID or ARN of the brand profile.
  + In **--registration-types**, list 1–10 registration types to create.

  Smart match is on by default; add **--no-smart-match** to turn it off. The response returns a job ID for each registration.

------

This operation runs asynchronously and returns a job ID for each registration. Track the job on the **Jobs** tab of the brand profile, or with the **GetJob** operation (see [Track brand profile jobs](nx-features-brand-profiles-sync-jobs.md)).