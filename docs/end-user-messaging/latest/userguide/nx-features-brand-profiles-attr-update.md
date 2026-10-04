

# Update a brand profile attribute
<a name="nx-features-brand-profiles-attr-update"></a>

Update an attribute to change its value, category, or description. For image and document attributes, upload new binary content to replace the stored file.

------
#### [ AWS Management Console ]

**To update a brand profile attribute using the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. Open the brand profile detail page and choose the **Attributes** tab.

1. Select the attribute and choose **Edit**. Change the value, category, or description, then save.

------
#### [ AWS CLI ]

**To update a brand profile attribute using the AWS CLI**
+ At the command line, enter the following command:

  ```
  $ aws endusermessaging update-brand-profile-attribute \
  > --brand-profile-id {{bp-gkma20fagojtpys0e}} \
  > --attribute-name {{"Company Name"}} \
  > --attribute-value {{"Example Corporation"}}
  ```

  In the preceding command, make the following changes:
  + Replace the brand profile ID and attribute name placeholders.
  + For a text attribute, set **--attribute-value**. For an image or document attribute, set **--attachment-body** with the new content. You can also update **--category** and **--description**.

------