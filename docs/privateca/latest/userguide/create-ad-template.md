# Create a connector template

A template is a list of configurations for how the certificate should look once issued, and how the client should handle the certificates. The following procedures explain how to create a template.

Console

###### To create a template using the console

1.  Sign in to your AWS account and open the AWS Private CA Connector for Active Directory console at
    `https://console.aws.amazon.com/pca-connector-ad/home`.
2.  Choose a connector from the **Connectors for Active
    Directory** list and then choose **View
    details**.
3.  On the details page for the connector, find the **Templates** section and then choose **Create template**.
4.  On the **Create template** page, in the **Template
    creation method** section, choose one of the method options.
    - **Start from a predefined template** (default) –
      Choose from a list of predefined templates for AD applications:
      - **Code Signing**
      - **Computer**
      - **Domain Controller Authentication**
      - **EFS Recovery Agent**
      - **Enrollment Agent**
      - **Enrollment Agent (Computer)**
      - **IPSec**
      - **Kerberos Authentication**
      - **RAS and IAS Server**
      - **Smartcard Logon**
      - **Trust List Signing**
      - **User Signature**
      - **Workstation Authentication**

    - **Start from an existing template that you created**
      – Choose from a list of custom templates that you previously created.
    - **Start from a blank template** – Choose this
      option to begin creating a completely new template.

5.  In the **Certificate settings** section, define the following
    settings for certificates based on this template.
    - **Certificate type** – Specify whether to create
      **User** or **Computer**
      certificates.
    - **Auto-enrollment** – Choose whether to activate
      auto-enrollment for certificates based on this template.
    - **Validity period** – Specify a certificate
      validity period as an integer value of hours, days, weeks, months, or years.
      The minimum value is 2 hours.
    - **Renewal period** – Specify a certificate renewal
      period as an integer value of hours, days, weeks, months, or years. The
      renewal period must be no more than 75% of the validity period.
    - **Subject name** – Choose one or more options to
      be included in the subject name based on information contained in Active
      Directory.

    ###### Note

    At least one subject name or subject alternative name option must be
    specified.

        + **Common name**
        + **DNS as common name**
        + **Directory path**
        + **Email**

    - **Subject alternative name** – Choose one or more
      options to be included in the subject alternative name based on information
      contained in Active Directory.

    ###### Note

    At least one subject name or subject alternative name option must be
    specified.

        + **Directory GUID**
        + **DNS name**
        + **Domain DNS**
        + **Email**
        + **Service principal name (SPN)**
        + **User principal name (UPN)**

6.  In the **Certificate request handling and enrollment options**
    section, specify the purpose of certificates based on the template, choosing one of
    the following options.

        * **Signature**
        * **Encryption**
        * **Signature and encryption**
        * **Signature and smartcard logon**

    Next, choose which of the following features to activate. Options vary depending
    on the certificate purpose.

        * **Delete invalid certificates (do not archive)**
        * **Include symmetric algorithms**
        * **Exportable private key**

    Finally, choose a certificate enrollment option. Options vary depending on the
    certificate purpose.

        * **No user input required**
        * **Prompt user during enrollment**
        * **Prompt user during enrollment and require user input**

7.  In the **Application policies** section, choose all of the
    application policies that apply. The available policies are listed across several
    pages. Some policies may be preselected because of previous settings.
8.  In the **Custom application policies** section, you can add
    custom OIDs to the template, and specify whether application policy extensions are
    critical.
9.  In the **Cryptography settings** section, choose the following
    categories of cryptography settings for certificates based on this template.
10. In the **Groups and permissions** section, you can view the
    templates existing groups and permissions for enrollment, or you can choose the
    **Add new groups and permissions** button to add a new ones.
    The button opens a form requiring the following information:
    - **Display name**
    - **Security identifier** (SID)
    - **Enroll**, with options ALLOW | DENY | NOT SET
    - **Auto-enroll**, with options ALLOW | DENY | NOT
      SET

11. In the **Supersede templates** section, you can notify Active
    Directory that the current template supersedes one or more templates created in AD.
    Apply the superseding template by choosing **Add template from
    Active Directory to supersede** and specifying the common name of the
    superseding template.
12. In the **Tags – optional** pane, you can apply and
    remove metadata on your AD resource. Tags are key-value string pairs where the
    key must be unique to the resource and the value is optional. The pane displays any
    existing tags for the resource in a table. The following actions are
    supported.
    - Choose **Manage tags** to open the **Manage
      tags** page.
    - Choose Add new tag to create a tag. Fill in the
      **Key** field and, optionally, the
      **Value** field. Choose **Save
      changes** to apply the tag.
    - Choose the **Remove** button next to a tag to mark it
      for deletion, and choose **Save changes** to confirm.

13. After providing the required information and reviewing your choices, choose
    **Create template**. This opens **Template
    details**, where you can review the new template's settings, edit or
    delete the template, manage groups and permissions, manage superseded templates,
    manage tags, and set automatic re-enrollment for certificate holders.

API
**To create a connector template using the API**

Use the [CreateTemplate](../../../pca-connector-ad/latest/APIReference/API_CreateTemplate.md "../../../pca-connector-ad/latest/APIReference/API_CreateTemplate.md") action in the AWS Private CA Connector for Active Directory API.

CLI
**To create a connector template using the AWS CLI**

Use the [create-template](../../../cli/latest/reference/pca-connector-ad/create-template.md "../../../cli/latest/reference/pca-connector-ad/create-template.md") command in the AWS Private CA Connector for Active Directory section of the
AWS CLI.
