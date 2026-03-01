# Enable Certificate-based Authentication

Complete the following steps to enable certificate-based authentication.

###### To enable certificate-based authentication

1. Open the WorkSpaces Applications console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. In the navigation pane, choose **Directory Configs**.
   Select the directory config you want to configure, and choose
   **Edit**.
3. Choose **Enable Certificate-Based
   Authentication.**
4. Confirm that your private CA ARN is associated in the list. To appear in
   the list, you should store the private CA in the same AWS account and
   AWS Region. You must also tag the private CA with a key named
   `euc-private-ca`.
5. Configure directory log in fallback. With Fallback, users can log in with
   their AD domain password if certificate-based authentication is
   unsuccessful. This is recommended only in cases where users know their
   domain passwords. When fallback is turned off, a session can disconnect the
   user if a lock screen or Windows log off occurs. If fallback is turned on,
   the session prompts the user for their AD domain password.
6. Choose **Save Changes**.
7. Certificate-based authentication is now enabled. When users authenticate
   with SAML 2.0 to an WorkSpaces Applications stack using the domain-joined fleet from the
   WorkSpaces Applications web client or the client for Windows (version 1.1.1099 and later),
   they will no longer receive a prompt for the domain password. Users will see
   a “Connecting with certificate-based authentication...” message when
   connecting to a session enabled for certificate-based authentication.
