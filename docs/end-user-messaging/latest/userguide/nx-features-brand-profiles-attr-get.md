

# Get a brand profile attribute
<a name="nx-features-brand-profiles-attr-get"></a>

View a single attribute to see its value, type, category, and (for image and document attributes) a download URL for the stored file.

------
#### [ AWS Management Console ]

**To get a brand profile attribute using the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. Open the brand profile detail page and choose the **Attributes** tab.

1. Choose an attribute in the table to view its **Value**, **Type**, **Category**, and description.

------
#### [ AWS CLI ]

**To get a brand profile attribute using the AWS CLI**
+ At the command line, enter the following command:

  ```
  $ aws endusermessaging get-brand-profile-attribute \
  > --brand-profile-id {{bp-gkma20fagojtpys0e}} \
  > --attribute-name {{"Company Name"}}
  ```

  Replace the placeholders with the ID or ARN of the brand profile and the attribute name. For `IMAGE` and `DOCUMENT` attributes, the response includes a `mediaDownloadUrl`.

------