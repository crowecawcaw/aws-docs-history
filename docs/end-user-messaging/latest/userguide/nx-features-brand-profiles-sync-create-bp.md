

# Create a brand profile from a registration
<a name="nx-features-brand-profiles-sync-create-bp"></a>

Create a new brand profile whose attributes are imported from an existing registration. This is the **Import from registration** path when you create a brand profile. With smart match enabled, an AI model maps the registration fields onto brand profile attributes.

------
#### [ AWS Management Console ]

**To create a brand profile from a registration using the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, choose **Brand profiles**.

1. Choose **Create brand profile**. In the **Source** section, choose **Import from registration**.

1. For **Name**, enter a name for the new profile. For **Registration**, choose the registration whose details will populate the profile. Leave **Smart match** enabled to map the fields with AI.

1. Choose **Create brand profile**.

------
#### [ AWS CLI ]

**To create a brand profile from a registration using the AWS CLI**
+ At the command line, enter the following command:

  ```
  $ aws endusermessaging create-brand-profile-from-registration \
  > --brand-profile-name {{MyBrandProfile}} \
  > --registration-id {{reg-abc123}}
  ```

  In the preceding command, make the following changes:
  + Replace {{MyBrandProfile}} with a name for the new profile.
  + Replace {{reg-abc123}} with the ID or ARN of the registration to import from.

  Smart match is on by default; add **--no-smart-match** to turn it off. Apply tags with **--tags**.

------

This operation runs asynchronously and returns a job ID for each registration. Track the job on the **Jobs** tab of the brand profile, or with the **GetJob** operation (see [Track brand profile jobs](nx-features-brand-profiles-sync-jobs.md)).