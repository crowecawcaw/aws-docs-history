# Tutorial: Amazon Quick Suite and IAM identity

federation

|                                                                 |
| --------------------------------------------------------------- |
| \*_Applies<br>to:_<br>• Enterprise Edition and Standard Edition |

|                                                                                           |
| ----------------------------------------------------------------------------------------- |
| Intended audience:<br>Amazon Quick Suite Administrators and Amazon Quick Suite developers |

###### Note

IAM identity federation doesn't support syncing identity provider groups
with Amazon Quick Suite.

In the following tutorial, you can find a walkthrough for setting up the IdP Okta as a
federation service for Amazon Quick Suite. Although this tutorial shows the integration of
AWS Identity and Access Management (IAM) and Okta, you can also replicate this solution using your choice of
SAML 2.0 IdPs.

In the following procedure, you create an app in the Okta IdP using their "AWS Account Federation" shortcut. Okta describes this integration app as
follows:

"By federating Okta to Amazon Web Services (AWS) Identity and
Access Management (IAM) accounts, end users get single sign-on access to all their
assigned AWS roles with their Okta credentials. In each AWS account,
administrators set up federation and configure AWS roles to trust Okta.
When users sign in to AWS, they get Okta single sign-in experience to see
their assigned AWS roles. They can then select a desired role, which
defined their permissions for the duration of their authenticated session. Customers
with large numbers of AWS Accounts, check out the AWS
Single Sign-On app as an alternative." (https://www.okta.com/aws/)

###### To create an Okta app using Okta's "AWS Account

Federation" application shortcut

1. Sign in to your Okta dashboard. If you don't have one, create a free Okta
   Developer Edition account by using [this Amazon Quick Suite-branded
   URL](https://developer.okta.com/quickstart/ "https://developer.okta.com/quickstart/"). When you have activated your email, sign in to Okta.
2. On the Okta website, choose **<> Developer Console** at
   upper left, and then choose **Classic UI**.
3. Choose **Add Applications**, and choose **Add
   app**.
4. Enter `aws` for **Search**, and choose
   **AWS Account Federation** from the
   search results.
5. Choose **Add** to create an instance of this
   application.
6. For **Application label**, enter `AWS Account Federation - Amazon Quick Suite`.
7. Choose **Next**.
8. For **SAML 2.0**, **Default Relay State**,
   enter `https://quicksight.aws.amazon.com`.
9. Open the context (right-click) menu for **Identity Provider
   metadata**, and choose to save the file. Name the file
   `metadata.xml`. You need this file in the next procedure.

The contents of the file look similar to the following.

```
<md:EntityDescriptor xmlns:md="urn:oasis:names:tc:SAML:2.0:metadata" entityID="http://www.okta.com/exkffz2hATwiVft645d5">
    <md:IDPSSODescriptor WantAuthnRequestsSigned="false" protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
    <md:KeyDescriptor use="signing">
        <ds:KeyInfo xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
        <ds:X509Data>
            <ds:X509Certificate>
            MIIDpjCCAo6gAwIBAgIGAXVjA82hMA0GCSqGSIb3DQEBCwUAMIGTMQswCQYDVQQGEwJVUzETMBEG
            .
            .        (certificate content omitted)
            .
            QE/6cRdPQ6v/eaFpUL6Asd6q3sBeq+giRG4=
            </ds:X509Certificate>
        </ds:X509Data>
        </ds:KeyInfo>
    </md:KeyDescriptor>
    <md:NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</md:NameIDFormat>
    <md:NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:unspecified</md:NameIDFormat>
    <md:SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://dev-1054988.okta.com/app/amazon_aws/exkffz2hATwiVft645d5/sso/saml"/>
    <md:SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="https://dev-1054988.okta.com/app/amazon_aws/exkffz2hATwiVft645d5/sso/saml"/>
    </md:IDPSSODescriptor>
    </md:EntityDescriptor>
```

10. After you have the XML file saved, scroll to the bottom of the Okta page, and
    choose **Done**.
11. Keep this browser window open, if possible. You need it later in the
    tutorial.
    Next, you create an identity provider in your AWS account.

###### To create a SAML provider in AWS Identity and Access Management (IAM)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Identity providers**,
   **Create Provider**.
3. Enter the following settings:
   - **Provider Type** – Choose
     **SAML** from the list.
   - **Provider Name** – Enter
     `Okta`.
   - **Metadata Document** – Upload the XML file
     `manifest.xml` from the previous procedure.

4. Choose **Next Step**, **Create**.
5. Locate the IdP that you created and choose it to view the settings. Note the
   **Provider ARN**. You need this to finish the
   tutorial.
6. Verify that the identity provider is created with your settings. In IAM,
   choose **Identity providers**, **Okta** (the
   IdP you added), **Download metadata**. The file should be the
   one that you recently uploaded.
   Next, you create an IAM role to enable the SAML 2.0 federation to act as a trusted
   entity in your AWS account. For this step, you need to choose how you want to
   provision users in Amazon Amazon Quick Suite. You can do one of the following:

- Grant permission to the IAM role so that first-time visitors become
  Amazon Quick Suite users automatically.

###### To create an IAM role for a SAML 2.0 federation as a trusted entity

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**, **Create
   Role**.
3. For **Select type of trusted entity**, choose the card
   labeled **SAML 2.0 federation**.
4. For **SAML provider**, select the IdP that you created in the
   previous procedure, for example `Okta`.
5. Enable the option **Allow programmatic and AWS
   Management Console access**.
6. Choose **Next: Permissions**.
7. Paste the following policy into the editor.

In the policy editor, update the JSON with your provider's Amazon
Resource Name (ARN).

```
{
    "Version": "2012-10-17"		 	 	 ,
    "Statement": [
    {
        "Effect": "Allow",
        "Action": "sts:AssumeRoleWithSAML",
        "Resource": "arn:aws:iam::`111111111111`:saml-provider/`Okta`",
        "Condition": {
        "StringEquals": {
            "saml:aud": "https://signin.aws.amazon.com/saml"
        }
        }
    }
    ]
    }
```

8. Choose **Review policy**.
9. For **Name**, enter
   `QuicksightOktaFederatedPolicy`, and then choose
   **Create policy**.
10. Choose **Create policy**, **JSON** a second
    time.
11. Paste the following policy into the editor.

In the policy editor, update the JSON with your AWS account ID. It should be
the same account ID that you used in the previous policy in the provider
ARN.

```
{
    "Version": "2012-10-17"		 	 	 ,
    "Statement": [
        {
            "Action": [
                "quicksight:CreateReader"
            ],
            "Effect": "Allow",
            "Resource": [
                "arn:aws:quicksight::`111111111111`:user/${aws:userid}"
            ]
        }
    ]
    }
```

You can omit the AWS Region name in the ARN, as shown following.

```
arn:aws:quicksight**::**`111111111111`:user/$${aws:userid}
```

12. Choose **Review policy**.
13. For **Name**, enter
    `QuicksightCreateReader`, and then choose
    **Create policy**.
14. Refresh the list of policies by choosing the refresh icon at right.
15. For **Search**, enter
    `QuicksightOktaFederatedPolicy`. Choose the policy to
    enable it (

![](/images/quicksuite/latest/userguide/images/checkbox-on.png)

).

If you don't want to use automatic provisioning, you can skip the following
step.

To add a Amazon Quick Suite user, use [register-user](../../../quicksight/latest/APIReference/API_RegisterUser.md "../../../quicksight/latest/APIReference/API_RegisterUser.md"). To add a Amazon Quick Suite group, use [create-group](../../../quicksight/latest/APIReference/API_CreateGroup.md "../../../quicksight/latest/APIReference/API_CreateGroup.md"). To add users to the Amazon Quick Suite group, use [create-group-membership](../../../quicksight/latest/APIReference/API_CreateGroupMembership.md "../../../quicksight/latest/APIReference/API_CreateGroupMembership.md"). 16. (Optional) For **Search**, enter
`QuicksightCreateReader`. Choose the policy to enable
it (

![](/images/quicksuite/latest/userguide/images/checkbox-on.png)

).

Do this step if you want to provision Amazon Quick Suite users automatically, rather
than using the Amazon Quick Suite API.

The `QuicksightCreateReader` policy activates automatic
provisioning by allowing use of the `quicksight:CreateReader` action.
Doing this grants dashboard subscriber (reader-level) access to first-time
users. A Amazon Quick Suite administrator can later upgrade them from the Amazon Quick Suite
profile menu, **Manage Amazon Quick Suite**, **Manage
users**. 17. To continue attaching the IAM policy or policies, choose **Next:
Tags**. 18. Choose **Next: Review**. 19. For **Role name**, enter
`QuicksightOktaFederatedRole`, and choose
**Create role**. 20. Verify that you completed this successfully by taking these steps:

    1. Return to the main page of the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"). You
     can use your browser's **Back** button.
    2. Choose **Roles**.
    3. For **Search**, enter Okta. Choose
     **QuicksightOktaFederatedRole** from the search
     results.
    4. On the **Summary** page for the policy, examine the
     **Permissions** tab. Verify that the role has the
     policy or policies that you attached to it. It should have
     `QuicksightOktaFederatedPolicy`. If you chose to add the
     ability to create users, it should also have
     `QuicksightCreateReader`.
    5. Use the

     ![](/images/quicksuite/latest/userguide/images/caret-right-filled.png)

     icon to open each policy.
     Verify that the text matches what is shown in this procedure.
     Double-check that you added your own AWS account number in place of
     the example account number 111111111111.
    6. On the **Trust relationships** tab, verify that the
     **Trusted entities** field contains the ARN for the
     identity provider. You can double-check the ARN in the IAM console by
     opening **Identity providers**,
     **Okta**.
    7.

###### To create an access key for Okta

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Add a policy that allows Okta to display a list of IAM roles to the user. To
   do this, choose **Policy**, **Create policy**.
3. Choose **JSON**, then enter the following policy.

```
{
    "Version": "2012-10-17"		 	 	 ,
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "iam:ListRoles",
                "iam:ListAccountAliases"
            ],
            "Resource": "*"
        }
    ]
    }
```

4. Choose **Review Policy**.
5. For **Name**, enter
   `OktaListRolesPolicy`. Then choose **Create
   policy**.
6. Add a user so you can provide Okta with an access key.

In the navigation pane, choose **Users**, **Add
User**. 7. Use the following settings:

    * For **User name**, enter
     `OktaSSOUser`.
    * For **Access type**, enable **Programmatic
     access**.

8.  Choose **Next: Permissions**.
9.  Choose **Attach existing policies directly**.
10. For **Search**, enter
    `OktaListRolesPolicy`, and choose
    **OktaListRolesPolicy** from the search results.
11. Choose **Next: Tags**, and then choose **Next:
    Review**.
12. Choose **Create user**. Now you can get the access
    key.
13. Download the key file by choosing **Download .csv**. The file
    contains the same access key ID and secret access key that displays on this
    screen. However, because AWS doesn't display this information a
    second time, make sure to download the file.
14. Verify that you completed this step correctly by doing the following:

        1. Open the IAM console, and choose **Users**. Search
         for **OktaSSOUser**, and open it by choosing the
         username from the search results.
        2. On the **Permissions** tab, verify that the
         **OktaListRolesPolicy** is attached.
        3. Use the

         ![](/images/quicksuite/latest/userguide/images/caret-right-filled.png)

         icon to open the policy.
         Verify that the text matches what is shown in this procedure.
        4. On the **Security credentials** tab, you can check
         the access key, although you already downloaded it. You can return to
         this tab to create an access key when you need a new one.

    In the following procedure, you return to Okta to provide the access key. The access
    key works with your new security settings to allow AWS and the Okta IdP to work
    together.

###### To finish configuring the Okta application with AWS settings

1. Return to your Okta dashboard. If requested to do so, sign in. If the
   developer console is no longer open, choose **Admin** to reopen
   it.
2. If you have to reopen Okta, you can return to this section by following these
   steps:
   1. Sign in to Okta. Choose **Applications**.
   2. Choose **AWS Account Federation -
      Amazon Quick Suite**—the application that you created at
      the beginning of this tutorial.
   3. Choose the **Sign On** tab, between
      **General** and **Mobile**.

3. Scroll to **Advanced Sign-On Settings**.
4. For **Identity Provider ARN (Required only for SAML IAM
   federation)**, enter the provider ARN from the previous procedure,
   for example:

```
arn:aws:iam::`111122223333`:saml-provider/Okta
```

5. Choose **Done** or **Save**. The name of the
   button varies depending if you are creating or editing the application.
6. Choose the **Provisioning** tab, and at the lower part of the
   tab, choose **Configure API Integration**.
7. Turn on **Enable API integration** to display the
   settings.
8. For **Access Key** and **Secret Key**,
   provide the access key and secret key that you downloaded previously to a file
   named `OktaSSOUser``_credentials.csv`.
9. Choose **Test API Credentials**. Look above the
   **Enable API integration** setting for a message confirming
   that **AWS Account Federation was verified
   successfully**.
10. Choose **Save**.
11. Make sure that **To App** is highlighted at left, and choose
    **Edit** at right.
12. For **Create Users**, turn on the option
    **Enable**.
13. Choose **Save**.
14. On the **Assignments** tab, near
    **Provisioning** and **Import**, choose
    **Assign**.
15. Do one or more of the following to enable federated access:
    - To work with individual users, choose **Assign to
      People**.
    - To work with IAM groups, choose **Assign to
      Groups**. You can choose specific IAM groups or
      **Everyone (All users in your
      organization)**.

16. For each IAM user or group, do the following:
    1. Choose **Assign**, **Role**.
    2. Select **QuicksightOktaFederatedRole** from the list
       of IAM roles.
    3. For **SAML User Roles**, enable
       **QuicksightOktaFederatedRole**.

17. Choose **Save and Go Back**, and then choose
    **Done**.
18. Verify that you completed this step correctly by choosing the
    **People** or **Groups** filter at left,
    and checking the users or groups that you entered. If you can't complete
    this process because the role that you created doesn't appear in the list,
    return to the previous procedures to verify the settings.

###### To sign in to Amazon Quick Suite using Okta (IdP to service provider sign-in)

1. If you are using an Okta administrator account, switch to user mode.
2. Sign in to your Okta Applications dashboard with a user that has been granted
   federated access. You should see a new application with your label, for example
   **AWS Account Federation -
   Amazon Quick Suite**.
3. Choose the application icon to launch **AWS Account
   Federation - Amazon Quick Suite**.
   You can now manage identities using Okta and use federated access with
   Quick Suite.

The following procedure is an optional part of this tutorial. If you follow its steps,
you authorize Amazon Quick Suite to forward authorizations requests to the IdP on behalf of
your users. Using this method, users can sign in to Amazon Quick Suite with no need to sign in
using the IdP page first.

###### (Optional) To set up Amazon Quick Suite to send authentication requests to Okta

1. Open Amazon Quick Suite, and choose **Manage Amazon Quick Suite** from
   your profile menu.
2. Choose **Single sign-on (IAM federation)** from the
   navigation pane.
3. For **Configuration**, **IdP
   URL**, enter the URL that your IdP provides to authenticate users,
   for example
   https://dev-`1-----0`.okta.com/home/amazon_aws/`0oabababababaGQei5d5/282`.
   You can find this in your Okta app page, on the **General**
   tab, in **Embed Link**.
4. For **IdP URL**, enter `RelayState`.
5. Do one of the following:
   - To test signing in with your identity provider first, use the custom
     URL provided in **Test starting with your IdP**. You
     should arrive at the start page for Amazon Quick Suite, for example
     https://quicksight.aws.amazon.com/sn/start.
   - To test signing in with Amazon Quick Suite first, use the custom URL
     provided in **Test the end-to-end experience**. The
     `enable-sso` parameter is appended to the URL. If
     `enable-sso=1`, IAM federation attempts to
     authenticate. If `enable-sso=0`, Amazon Quick Suite doesn't send
     the authentication request, and you sign in to Amazon Quick Suite as
     before.

6. For **Status**, choose **ON**.
7. Choose **Save** to keep your settings.
   You can create a deep link to a Amazon Quick Suite dashboard to allow users to use IAM
   federation to connect directly to specific dashboards. To do this, you append the relay
   state flag and dashboard URL to the Okta single sign-on URL, as described
   following.

###### To create a deep link to a Amazon Quick Suite dashboard for single sign-on

1. Locate the Okta application’s single sign-on (IAM federation) URL in the
   `metadata.xml` file that you downloaded beginning of the
   tutorial. You can find the URL near the bottom of the file, in the element named
   `md:SingleSignOnService`. The attribute is named
   `Location` and the value ends with `/sso/saml`, as
   shown in the following example.

```
<md:SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="**https://dev-0000001.okta.com/app/amazon\_aws/abcdef2hATwiVft645d5/sso/saml**"/>
```

2. Take the value of the IAM federation URL and append
   `?RelayState=` followed by the URL of your Amazon Quick Suite
   dashboard. The `RelayState` parameter relays the state (the URL) that
   the user was in when they were redirected to the authentication URL.
3. To the new IAM federation with the relay state added, append the URL of your
   Amazon Quick Suite dashboard. The resulting URL should resemble the following.

```
https://dev-`1-----0`.okta.com/app/amazon_aws/`abcdef2hATwiVft645d5`/sso/saml**?RelayState=**https://us-west-2.quicksight.aws.amazon.com/sn/analyses/12a12a2a-121a-212a-121a-abcd12abc1ab
```

4. If the link you create doesn't open, check that you are using the most recent
   IAM federation URL from the `metadata.xml`. Also check that the
   username you use to sign in isn't assigned in more than one IAM federation
   Okta app.
