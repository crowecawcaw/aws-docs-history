

# Get a brand profile
<a name="nx-features-brand-profiles-get"></a>

View a single brand profile to see its name, ID, ARN, status, deletion protection setting, and timestamps.

------
#### [ AWS Management Console ]

**To get a brand profile using the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, choose **Brand profiles**.

1. In the **Brand profiles** table, choose the brand profile **Name** to open its detail page.

1. On the **Overview** tab, review the **Brand profile details**: name, brand profile ID, ARN, creation date, and status.

------
#### [ AWS CLI ]

**To get a brand profile using the AWS CLI**

1. At the command line, enter the following command:

   ```
   $ aws endusermessaging get-brand-profile \
   > --brand-profile-id {{bp-gkma20fagojtpys0e}}
   ```

   Replace {{bp-gkma20fagojtpys0e}} with the ID or ARN of the brand profile.

1. The response resembles the following:

   ```
   {
       "brandProfileId": "bp-gkma20fagojtpys0e",
       "brandProfileName": "MyBrandProfile",
       "brandProfileArn": "arn:aws:end-user-messaging:us-east-1:123456789012:brand-profile/bp-gkma20fagojtpys0e",
       "status": "ACTIVE",
       "deletionProtectionEnabled": false
   }
   ```

------