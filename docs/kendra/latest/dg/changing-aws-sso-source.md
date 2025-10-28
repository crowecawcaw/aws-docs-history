# Changing your IAM Identity Center identity source

###### Warning

Changing your identity source in IAM Identity Center **Settings** might affect
the preservation of user and group information. To do this safely, it is recommended
you review [Considerations for changing your identity source](../../../singlesignon/latest/userguide/manage-your-identity-source-considerations.md "../../../singlesignon/latest/userguide/manage-your-identity-source-considerations.md"). When you change your
identity source, a new identity source ID is generated. Check you are using the
correct ID before you set the mode to `AWS_SSO` in [UserGroupResolutionConfiguration](../APIReference/API_UserGroupResolutionConfiguration.md "../APIReference/API_UserGroupResolutionConfiguration.md").

###### To change your IAM Identity Center identity source

1. Open the [IAM Identity Center>
   console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. Choose **Settings**.
3. On the **Settings** page, under **Identity
   source**, choose **Change**.
4. On the **Change identity source** page, select your preferred
   identity source, and then choose **Next**.
