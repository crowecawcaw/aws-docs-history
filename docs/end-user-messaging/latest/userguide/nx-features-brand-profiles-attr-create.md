

# Create brand profile attributes
<a name="nx-features-brand-profiles-attr-create"></a>

Attributes hold your brand identity information — company details, addresses, compliance documents, and logos — as key/value pairs on the brand profile. Each attribute has a type of `TEXT`, `IMAGE`, or `DOCUMENT`. You can add up to 10 attributes in a single request. For `IMAGE` and `DOCUMENT` attributes, provide the file content directly or reference a file in Amazon S3, and AWS End User Messaging returns a download URL.

------
#### [ AWS Management Console ]

**To add brand profile attributes using the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. Choose the brand profile **Name** to open its detail page, then choose the **Attributes** tab and choose **Add attribute**.

1. In the **Add attribute** dialog, choose how to add the attribute:
   + **Use a suggested attribute** — pick a **Category**, then a suggested **Attribute name**. The matching type is set for you.
   + **Create a custom attribute** — enter your own **Attribute name** (up to 256 characters), choose the **Type** (**Text**, **Image**, or **Document**), and optionally a **Category**.

1. For a **Text** attribute, enter the **Value** (up to 4,096 characters). For an **Image** or **Document** attribute, upload the file.

1. Choose **Add attribute**.

------
#### [ AWS CLI ]

**To add brand profile attributes using the AWS CLI**
+ At the command line, enter the following command:

  ```
  $ aws endusermessaging create-brand-profile-attributes \
  > --brand-profile-id {{bp-gkma20fagojtpys0e}} \
  > --attributes '[{"attributeName":"Company Name","attributeType":"TEXT","attributeValue":"Example Corp","category":"BUSINESS_IDENTITY"}]'
  ```

  In the preceding command, make the following changes:
  + Replace {{bp-gkma20fagojtpys0e}} with the ID or ARN of the brand profile.
  + If you set `category`, it must be one of the following values: `BUSINESS_IDENTITY`, `BUSINESS_ADDRESS`, `BUSINESS_CONTACT`, `MESSAGING_USE_CASE`, `OPT_IN_CONSENT`, `MESSAGE_CONTENT`, `COMPLIANCE_KEYWORDS`, `TERMS_AND_POLICY`, `BRAND_DISPLAY`, `SUPPORTING_DOCUMENT`, or `OTHER`. Any other value returns a `ValidationException`.
  + In **--attributes**, provide 1–10 attribute objects. Each object sets `attributeName`, `attributeType` (`TEXT`, `IMAGE`, or `DOCUMENT`), and either `attributeValue` or `attachmentBody`, plus an optional `category` and `description`. For a `TEXT` attribute, set `attributeValue` to the text value. For an `IMAGE` or `DOCUMENT` attribute, either provide the file content as base64 in `attachmentBody` or set `attributeValue` to an Amazon S3 URL (`s3://{{bucket}}/{{key}}`) that points to the file.

------