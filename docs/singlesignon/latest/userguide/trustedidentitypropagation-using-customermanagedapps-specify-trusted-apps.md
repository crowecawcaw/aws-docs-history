# Specify trusted applications

After you [set up your customer managed application](customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2.md "customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2.md"), you must specify one or
more trusted AWS services, or trusted applications, for identity propagation.
Specify an AWS service that has data that users of your customer managed
applications need to access. When your users sign in to your customer managed
application, that application will pass your users' identity to the trusted
application.

Use the following procedure to select a service, and then specify individual
applications to trust for that service.

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. Choose **Applications**.
3. Choose the **Customer managed** tab.
4. In the **Customer managed applications** list, select
   the OAuth 2.0 application that you want to initiate requests for access.
   This is the application that your users sign in to.
5. On the **Details page**, under **Trusted
   applications for identity propagation**, choose
   **Specify trusted applications**.
6. Under **Setup type**, select **Individual
   applications and specify access**, and then choose
   **Next**.
7. On the **Select service** page, choose the AWS
   service that has applications that your customer managed application can
   trust for identity propagation, and then choose
   **Next**.

The service that you select defines the applications that can be
trusted. You'll select applications in the next step. 8. On the **Select applications** page, choose
**Individual applications**, select the check box
for each application that can receive requests for access, and then
choose **Next**. 9. On the **Configure access** page, under
**Configuration method**, do either of the
following:

    * **Select access per application** –
     Select this option to configure different access levels for each
     application. Choose the application for which you want to
     configure the access level, and then choose **Edit
     access**. In **Level of access to
     apply**, change the access levels as needed, and
     then choose **Save changes**.
    * **Apply same level of access to all
     applications** – Select this option if you
     do not need to configure access levels on a per-application
     basis.

10. Choose **Next**.
11. On the **Review configuration** page, review the
    choices that you made. To make changes, choose the configuration section
    that you want, choose **Edit access**, and then make
    the required changes.
12. After you are finished, choose **Trust
    applications**.
