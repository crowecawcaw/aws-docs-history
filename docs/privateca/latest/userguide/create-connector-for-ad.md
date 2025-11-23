# Creating a connector for Active Directory

Use the following procedures to create a connector using the console, command line, or API
for AWS Private CA Connector for Active Directory.

Console

###### To create a connector using the console

Sign in to your AWS account and open the AWS Private CA Connector for Active Directory console at
`https://console.aws.amazon.com/pca-connector-ad/home`.

1.  On the first-time service landing page or the **Connectors for Active
    Directory** page, choose **Create connector**.
2.  On the **Create Private CA Connector for Active Directory** page,
    provide information in the **Active Directory** section.
    - Under **Select your Active Directory type**, choose one
      of the two available types:
      - **AWS Directory Service for Microsoft Active Directory**
        – Specifies an Active Directory managed by Directory Service.
      - **On-premises Active Directory with AWS
        AD Connector**– Uses AD Connector to access
        an Active Directory that you host on-premises.

    - Under **Select your directory**, choose your directory
      from the list.

    Alternatively, you can choose **Create directory**, which
    opens the Directory Service console in a new window. When you finish creating a new
    directory, return to the AWS Private CA Connector for Active Directory console and refresh the list
    of directories. Your new directory should be available for selection.

    ###### Note

    When creating a directory, note that Connector for AD
    supports only the following directory types offered in the Directory Service
    console:

        + **AWS Managed Microsoft AD**
        + **AD Connector**

    - Under **Select security groups for VPC endpoint**, choose
      a security group from the list.

    Alternatively, you can choose **Create security group**,
    which opens the Amazon EC2 console to the **Create security
    group** page in a new window. When you finish creating a
    security group, return to the AWS Private CA Connector for Active Directory console and refresh the
    list of security groups. Your new security group should be available for
    selection.

3.  In the **IP address type** section, choose from
    the following options:
    - **IPv4** - Enables IPv4 connectivity to
      the service. Choose this option only if all subnets hosting your directory have IPv4 address ranges.
    - **Dualstack** - Enables both IPv4 and IPv6 connectivity to the service. Choose
      this option only if all subnets hosting your directory have both IPv4 and IPv6 address ranges.

4.  In the **Private certificate authority** section, choose a
    private CA from the list.

Alternatively, you can choose **Create Private CA**, which opens
the AWS Private CA console to the **Private certificate authorities**
page in a new window. When you finish creating a CA, return to the
AWS Private CA Connector for Active Directory console and refresh the list of CAs. Your new CA should be
available for selection. 5. In the **Tags – optional** pane, you can apply and
remove metadata on your AD resource. Tags are key-value string pairs where the
key must be unique to the resource and the value is optional. The pane displays any
existing tags for the resource in a table. The following actions are
supported.

    * Choose **Manage tags** to open the **Manage
     tags** page.
    * Choose Add new tag to create a tag. Fill in the
     **Key** field and, optionally, the
     **Value** field. Choose **Save
     changes** to apply the tag.
    * Choose the **Remove** button next to a tag to mark it
     for deletion, and choose **Save changes** to confirm.

6. After providing the required information and reviewing your choices, choose
   **Create connector**. This opens the **Connectors for
   Active Directory** details page where can view the progress of your
   connector as it is created.

After the process of creating a connector completes, assign it a service principal
name.

API
**To create a connector using the API**

To create a connector for Active Directory with the API, use the [CreateConnector](../../../pca-connector-ad/latest/APIReference/API_CreateConnector.md "../../../pca-connector-ad/latest/APIReference/API_CreateConnector.md") action in the AWS Private CA Connector for Active Directory API.

CLI
**To create a connector using the AWS CLI**

To create a connector for Active Directory with the CLI, use the [create-connector](../../../cli/latest/reference/pca-connector-ad/create-connector.md "../../../cli/latest/reference/pca-connector-ad/create-connector.md") command in the AWS Private CA Connector for Active Directory section of the
AWS CLI.
