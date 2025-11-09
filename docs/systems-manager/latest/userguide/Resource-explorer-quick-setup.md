AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Configure AWS Resource Explorer using

Quick Setup

With Quick Setup, a tool in AWS Systems Manager, you can quickly configure AWS Resource Explorer to search
and discover resources in your AWS account or across an entire AWS organization.
You can search for your resources using metadata like names, tags, and IDs.
AWS Resource Explorer provides fast responses to your search queries by using
_indexes_. Resource Explorer creates and maintains indexes using a
variety of data sources to gather information about resources in your AWS account.

Quick Setup for Resource Explorer automates the index configuration process. For more
information about AWS Resource Explorer, see [What is
AWS Resource Explorer?](../../../resource-explorer/latest/userguide/welcome.md "../../../resource-explorer/latest/userguide/welcome.md") in the AWS Resource Explorer User Guide.

During Quick Setup, Resource Explorer does the following:

- Creates an index in every AWS Region in your AWS account.
- Updates the index in the Region you specify to be the aggregator index for
  the account.
- Creates a default view in the aggregator index Region. This view has no
  filters so it returns all resources found in the index.
  **Minimum permissions**

To perform the steps in the following procedure, you must have the following
permissions:

- **Action**:
  `resource-explorer-2:*` – **Resource**: no specific resource (`*`)
- **Action**:
  `iam:CreateServiceLinkedRole` – **Resource**: no specific resource (`*`)

###### To configure Resource Explorer

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Quick Setup**.
3. On the **Resource Explorer** card, choose
   **Create**.
4. In the **Aggregator Index Region** section, choose which
   Region you want to contain the **aggregator index**. You
   should select the Region that is appropriate for the geographic location for
   your users.
5. (Optional) Select the **Replace existing aggregator indexes in
   Regions other than the one selected above**
   check box.
6. In the **Targets** section, choose the target
   **organization** or specific **Organizational
   Units (OUs)** containing the resources you want to discover.
7. In the **Regions** section, choose which
   **Regions** to include in the configuration.
8. Review the configuration summary, and then choose
   **Create**.
   On the **Resource Explorer** page, you can monitor the
   configuration status.
