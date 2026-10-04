

# Create a brand profile
<a name="nx-features-brand-profiles-create"></a>

A brand profile is a lightweight container that stores your business identity as a set of attributes. When you create a brand profile you choose how to populate it: start from scratch and add attributes yourself, or import from an existing registration and let AWS End User Messaging pre-fill the attributes for you. A new brand profile starts with a standard set of default attributes and is created with a status of `ACTIVE`. After you create it, add your company information, addresses, compliance documents, and logos with the attribute operations.

------
#### [ AWS Management Console ]

**To create a brand profile using the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, choose **Brand profiles**.

1. On the **Brand profiles** page, choose **Create brand profile**.

1. In the **Source** section, choose **Start from scratch** to create an empty brand profile and fill in its attributes yourself.
**Note**  
To pre-fill the brand profile from an existing registration instead, choose **Import from registration**. For more information, see [Create a brand profile from a registration](nx-features-brand-profiles-sync-create-bp.md).

1. In the **Brand profile details** section, for **Name** enter a name for the brand profile. The name can be up to 64 characters and can contain letters, numbers, spaces, underscores, and hyphens.

1. (Optional) Expand **Tags** and choose **Add new tag** to add a key/value pair. You can add up to 50 tags.

1. Choose **Create brand profile**.

------
#### [ AWS CLI ]

**To create a brand profile using the AWS CLI**

1. At the command line, enter the following command:

   ```
   $ aws endusermessaging create-brand-profile \
   > --brand-profile-name {{MyBrandProfile}}
   ```

   In the preceding command, make the following changes:
   + Replace {{MyBrandProfile}} with a name for the brand profile. The name can be 1–64 characters and can contain letters, numbers, spaces, underscores, and hyphens.

   To protect the brand profile from being deleted, add **--deletion-protection-enabled**. To apply tags, add **--tags key={{KeyName}},value={{Value}}**.

1. The response includes the brand profile ID, ARN, status, and the number of default attributes that were created:

   ```
   {
       "brandProfileId": "bp-gkma20fagojtpys0e",
       "brandProfileArn": "arn:aws:end-user-messaging:us-east-1:123456789012:brand-profile/bp-gkma20fagojtpys0e",
       "brandProfileName": "MyBrandProfile",
       "status": "ACTIVE",
       "attributesCreated": 12,
       "deletionProtectionEnabled": false
   }
   ```

------

After you create the brand profile, add your brand identity information with the attribute operations (see [Create brand profile attributes](nx-features-brand-profiles-attr-create.md)), or seed attributes from a registration type with the registration helper. To reuse the profile across senders, sync it to your registrations (see [Syncing brand profiles with registrations](nx-features-brand-profiles-sync.md)).