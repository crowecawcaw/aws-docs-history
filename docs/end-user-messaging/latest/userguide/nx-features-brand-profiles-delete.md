

# Delete a brand profile
<a name="nx-features-brand-profiles-delete"></a>

Delete a brand profile you no longer need. If deletion protection is enabled on the profile, turn it off before you delete (see [Update a brand profile](nx-features-brand-profiles-update.md)).

------
#### [ AWS Management Console ]

**To delete a brand profile using the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, choose **Brand profiles**.

1. Select the option button next to the brand profile you want to delete, or open its detail page.

1. Choose **Delete** and confirm.
**Note**  
If deletion protection is enabled, the delete fails until you disable it on the **Deletion protection** tab.

------
#### [ AWS CLI ]

**To delete a brand profile using the AWS CLI**
+ At the command line, enter the following command:

  ```
  $ aws endusermessaging delete-brand-profile \
  > --brand-profile-id {{bp-gkma20fagojtpys0e}}
  ```

  Replace {{bp-gkma20fagojtpys0e}} with the ID or ARN of the brand profile. The request fails if deletion protection is enabled.

------