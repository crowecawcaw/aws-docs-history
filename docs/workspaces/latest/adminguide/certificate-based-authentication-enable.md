# Enable Certificate-based

Authentication

Complete the following steps to enable certificate-based authentication.

###### To enable certificate-based authentication

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. Choose **Directories** in the navigation pane.
3. Choose the **Pools directories** tab.
4. Choose the directory you want to configure.
5. Choose **Edit** in the
   **Authentication** section of the page.
6. Choose **Edit Certificate-Based Authentication** in the
   **Certificate-Based Authentication** section of the
   page.
7. Choose **Enable Certificate-Based
   Authentication**.
8. Choose the certificate in the **AWS Certificate Manager (ACM) Private
   Certificate Authority (CA)** drop-down.

To appear in the drop-down, you should store the private CA in the same
AWS account and AWS Region. You must also tag the private CA with a key
named `euc-private-ca`. 9. Configure directory log in fallback. With Fallback, users can log in with
their AD domain password if certificate-based authentication is
unsuccessful. This is recommended only in cases where users know their
domain passwords. When fallback is turned off, a session can disconnect the
user if a lock screen or Windows log off occurs. If fallback is turned on,
the session prompts the user for their AD domain password. 10. Choose **Save**.
Certificate-based authentication is now enabled. When users authenticate with SAML
2.0 to an WorkSpaces Pools directory using the domain-joined WorkSpaces, they will no longer
receive a prompt for the domain password. Users will see a **Connecting with
certificate-based authentication** message when connecting to a session
enabled for certificate-based authentication.
