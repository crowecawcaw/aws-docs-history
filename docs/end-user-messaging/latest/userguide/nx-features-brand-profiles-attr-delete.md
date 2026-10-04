

# Delete a brand profile attribute
<a name="nx-features-brand-profiles-attr-delete"></a>

Delete an attribute you no longer need from a brand profile.

------
#### [ AWS Management Console ]

**To delete a brand profile attribute using the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. Open the brand profile detail page and choose the **Attributes** tab.

1. Select the attribute, choose the delete action, and confirm.

------
#### [ AWS CLI ]

**To delete a brand profile attribute using the AWS CLI**
+ At the command line, enter the following command:

  ```
  $ aws endusermessaging delete-brand-profile-attribute \
  > --brand-profile-id {{bp-gkma20fagojtpys0e}} \
  > --attribute-name {{"Company Name"}}
  ```

  Replace the placeholders with the ID or ARN of the brand profile and the name of the attribute to delete.

------