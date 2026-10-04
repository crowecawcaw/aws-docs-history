

# Update a brand profile
<a name="nx-features-brand-profiles-update"></a>

Update a brand profile to change its name or its deletion protection setting. To change the brand identity information stored on the profile, update its attributes instead (see [Update a brand profile attribute](nx-features-brand-profiles-attr-update.md)).

------
#### [ AWS Management Console ]

**To update a brand profile using the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, choose **Brand profiles**.

1. Choose the brand profile **Name** to open its detail page.

1. Choose **Actions**, and then choose the edit option to change the name. To change deletion protection, use the **Deletion protection** tab and choose **Edit settings**.

------
#### [ AWS CLI ]

**To update a brand profile using the AWS CLI**
+ At the command line, enter the following command:

  ```
  $ aws endusermessaging update-brand-profile \
  > --brand-profile-id {{bp-gkma20fagojtpys0e}} \
  > --brand-profile-name {{MyRenamedProfile}}
  ```

  In the preceding command, make the following changes:
  + Replace {{bp-gkma20fagojtpys0e}} with the ID or ARN of the brand profile.
  + Replace {{MyRenamedProfile}} with the new name.

  To change deletion protection, add **--deletion-protection-enabled** or **--no-deletion-protection-enabled**.

------