# View connector template details

Use the following procedures to view the configuration details of a connector template
using the console, command line, or API for AWS Private CA Connector for Active Directory

Console

###### To view details for a connector template using the console

1.  Sign in to your AWS account and open the AWS Private CA Connector for Active Directory console at
    `https://console.aws.amazon.com/pca-connector-ad/home`.
2.  Choose a connector from the **Connectors for Active
    Directory** list and then choose **View
    details**.
3.  On the connector details page, review the information in the
    **Templates** section, and select the template that you
    wish to inspect. Then choose **View details**.
4.  On the details page, the **Template details** pane displays
    the following information about the template:

        * **Template name**
        * **Template ID**
        * **Template status**
        * **Template schema version**
        * **Template version**
        * **Template ARN**
        * **Certificate type**
        * **Auto-enrollment turned on**
        * **Validity period**
        * **Renewal period**
        * **Subject name requirements**
        * **Subject alternative name requirements**
        * **Certificate request and enrollment settings**
        * **Cryptography provider category**
        * **Key algorithm**
        * **Minimum key size (bits)**
        * **Hash algorithm**
        * **Cryptography providers**
        * **Key usage extension settings**

    From this pane, you can also perform the following actions using the
    **Edit**, **Delete**, and
    **Actions** buttons.

        * **Edit**
        * **Delete**
        * **Manage groups and permissions** – For more
         information, see [Configure groups and permissions](create-ad-template.md#create-ad-template-console-12 "create-ad-template.md#create-ad-template-console-12").
        * **Manage superseded templates** – For more
         information, see [Review
         and create](create-ad-template.md#create-ad-template-console-15 "create-ad-template.md#create-ad-template-console-15").
        * **Manage tags** – For more information, see
         [Tagging Connector for AD resources](ad-tags.md "ad-tags.md").
        * **Re-enroll all certificate holders** – This
         setting allows the major version of a template to be increased
         automatically. All members of Active Directory groups that are allowed
         to enroll with a template will receive a new certificate issued using
         that template. For more information, see the  [UpdateTemplate](../../../pca-connector-ad/latest/APIReference/API_UpdateTemplate.md "../../../pca-connector-ad/latest/APIReference/API_UpdateTemplate.md") API.

5.  The lower pane displays a row of tabs allowing changes to the configuration of
    the template.
    - **Groups and permissions** – View and manage
      permissions for Active Directory groups to enroll certificates using
      this template. For more information, see [Configure groups and permissions](create-ad-template.md#create-ad-template-console-12 "create-ad-template.md#create-ad-template-console-12")
    - **Application policies** – View and manage
      template application policies. For more information, see [Assign
      application policies](create-ad-template.md#create-ad-template-console-9 "create-ad-template.md#create-ad-template-console-9").
    - **Superseded templates** – View and manage
      superseded templates. For more information, see [Review
      and create](create-ad-template.md#create-ad-template-console-15 "create-ad-template.md#create-ad-template-console-15").
    - **Tag*optional***
      – View and manage tagging on this template. For more information,
      see [Tagging Connector for AD resources](ad-tags.md "ad-tags.md").

API
**To list your connectors using the API**

Use the [GetTemplate](../../../pca-connector-ad/latest/APIReference/API_GetTemplate.md "../../../pca-connector-ad/latest/APIReference/API_GetTemplate.md") action in the AWS Private CA Connector for Active Directory API.

CLI
**To list your connectors using the AWS CLI**

Use the [get-template](../../../cli/latest/reference/pca-connector-ad/get-template.md "../../../cli/latest/reference/pca-connector-ad/get-template.md") command in the AWS Private CA Connector for Active Directory section of the
AWS CLI.
