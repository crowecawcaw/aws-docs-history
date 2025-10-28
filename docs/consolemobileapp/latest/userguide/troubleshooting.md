# Troubleshooting

In this section, you’ll find answers to some common questions and concerns.

## Which password managers are supported by the Console Mobile Application?

The AWS Console Mobile Application supports password managers that are integrated with the mobile operating systems maintained by Apple (iOS) and Google (Android). For example, iCloud Passwords and Keychain, Google Chrome Password Manager, and Samsung Pass.

## What hardware authenticators does the Console Mobile Application support for MFA?

The AWS Console Mobile Application supports all FIDO certified hardware authenticators, such as YubiKey, for MFA. For a complete list of FIDO certified hardware authenticators, see [Fido Certified Products](https://fidoalliance.org/certification/fido-certified-products/ "https://fidoalliance.org/certification/fido-certified-products/").

## Which software authenticators does the AWS Console Mobile Application support for MFA?

The AWS Console Mobile Application supports software authenticators such as Google Authenticator, Microsoft Authenticator, and LastPass Authenticator. The AWS Console Mobile Application for iOS can also auto-fill MFA codes using the time-based one-time password (TOTP) feature built in to the in-app Safari browser used during sign in. For more information, see [Multi-Factor Authentication (MFA) for IAM](https://aws.amazon.com/iam/features/mfa/ "https://aws.amazon.com/iam/features/mfa/").

## Can I use biometric authentication when signing into the AWS Console Mobile Application?

Yes. The mobile OS password managers that are supported by the AWS Console Mobile Application support the use of your mobile device’s biometric authentication technology. If your mobile device doesn’t support biometric verification, your password manager may let you use the PIN that you set on your mobile device to verify your identity instead. If you don’t have biometric verification or a device PIN enabled on your mobile device, then you can enter your AWS identity password to access your AWS resources within the AWS Console Mobile Application.

## What if my organization’s mobile device management policy doesn’t allow the use of password managers or auto-fill?

If your organization doesn’t allow the use of password managers or auto-fill, then must to sign in to your AWS identity in the AWS Console Mobile Application by entering your AWS identity’s password.

## How can I set and update my default identity?

If you only have one identity saved in the AWS Console Mobile Application, then it is automatically set as your default identity. If you save more than one identity in the AWS Console Mobile App, then you can modify your default identity from the Identities screen by choosing the **Actions** button in the upper right corner of the screen and then choosing the **Set a default identity** menu item. You can then set your default AWS identity by selecting its checkbox and choosing **Apply**. If you want to remove a default identity, unselect its checkbox and choose **Apply**.

## I lost my device, what should I do?

If you lose your device, we recommend deactivating the user signed into the Console Mobile Application. We also recommend performing a remote wipe on your device.

## Can I create resources within the app?

Currently, the only way to create resources from the app is to do so through the AWS CloudShell service using the AWS Command Line Interface (AWS CLI). Otherwise, you can view and sometimes modify resources within the app’s graphical user interface, but you can’t create resources through the graphical user interface.

## Which CloudWatch dashboards can I access in the Console Mobile App?

You can search and view all CloudWatch custom dashboards that your AWS identity has permissions to access. CloudWatch automatic dashboards aren’t currently supported in the AWS Console Mobile App.

## Why am I being asked to log in again?

A session in the Console Mobile Application lasts 12 hours. After your session expires, you may need to log in again.

## Can I leave feedback?

Yes. To leave feedback, open the app and choose the menu icon in the upper left, then choose **Feedback**. Add your comments, optionally include logs, and then choose **Submit**.

You can also provide feedback by [contacting us](mailto:aws-appstore@amazon.com "mailto:aws-appstore@amazon.com").
