# Manage directory registrations

Console

###### To manage directory registrations using the console

Directory registrations for connectors can be managed from the top level of the
AWS Private CA Connector for Active Directory console. This topic walks through the available management
options.

1.  Sign in to your AWS account and open the AWS Private CA Connector for Active Directory console at
    `https://console.aws.amazon.com/pca-connector-ad/home`.
2.  In the left navigation area, choose **Directory registrations**.
3.  The **Directory registrations** page displays a table of
    registered directories with the following fields:

        * **Directory ID** – The unique ID of the
         directory
        * **Directory name** – The directory domain site
         name
        * **Directory type**
        * **Registered** – The status of the registration.
         Supported values are CREATING | ACTIVE | DELETING | FAILED.
        * **Directory status** – The status of the
         directory

    Use can use **Register directory** to create a new registration.

4.  You can select one of the listed registrations in order to manage it. This enables
    the **View registration details** and **Deregister
    directory** buttons. The **View registration details**
    button opens the details page for the registration.
5.  The **Directory registration details** pane displays the
    following information:
    - **Directory domain site name**
    - **Directory ID** – The unique ID of the directory.
      Choosing the link takes you to the AWS Directory Service console.
    - **Directory type**
    - **Status** – Status of the directory
    - **Directory registration ARN** – The Amazon
      resource name of the directory registration
    - **Additional status information**

6.  In the **Connectors and service principal name (SPNs)** pane, you
    can manage SPNs for the connector. For more information, see [View connector details](ad-spn.md "ad-spn.md").
7.  In the **Tags – optional** pane, you can apply and
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

API

**To manage directory registrations using the API**

**Create**: [CreateDirectoryRegistration](../../../pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.md "../../../pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.md") action in the AWS Private CA Connector for Active Directory API.

**Retrieve**: [GetDirectoryRegistration](../../../pca-connector-ad/latest/APIReference/API_GetDirectoryRegistration.md "../../../pca-connector-ad/latest/APIReference/API_GetDirectoryRegistration.md") action in the AWS Private CA Connector for Active Directory API.

**List**: [ListDirectoryRegistrations](../../../pca-connector-ad/latest/APIReference/API_ListDirectoryRegistrations.md "../../../pca-connector-ad/latest/APIReference/API_ListDirectoryRegistrations.md") action in the AWS Private CA Connector for Active Directory API.

**Delete**: [DeleteDirectoryRegistration](../../../pca-connector-ad/latest/APIReference/API_DeleteDirectoryRegistration.md "../../../pca-connector-ad/latest/APIReference/API_DeleteDirectoryRegistration.md") action in the AWS Private CA Connector for Active Directory API.

CLI

**To manage directory registrations using the CLI**

**Create**: Use the [create-directory-registration](../../../cli/latest/reference/pca-connector-ad/create-directory-registration.md "../../../cli/latest/reference/pca-connector-ad/create-directory-registration.md") command in the AWS Private CA Connector for Active Directory section of
the AWS CLI.

**Retrieve**: [get-directory-registration](../../../cli/latest/reference/pca-connector-ad/get-directory-registratio.md "../../../cli/latest/reference/pca-connector-ad/get-directory-registratio.md") command in the AWS Private CA Connector for Active Directory section of the
AWS CLI.

**List**: [list-directory-registrations](../../../cli/latest/reference/pca-connector-ad/list-directory-registratios.md "../../../cli/latest/reference/pca-connector-ad/list-directory-registratios.md") command in the AWS Private CA Connector for Active Directory section of
the AWS CLI.

**Delete**: [delete-directory-registration](../../../cli/latest/reference/pca-connector-ad/delete-directory-registratio.md "../../../cli/latest/reference/pca-connector-ad/delete-directory-registratio.md") command in the AWS Private CA Connector for Active Directory section of
the AWS CLI.
