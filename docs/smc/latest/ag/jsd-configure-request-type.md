# Configuring project

request type groups

The AWS request type must be in a group for users to be able to
access it in Jira Service Management. Enabling Jira projects, as
described in [Configuring Connector
Settings (Jira Project Enablement and Request Type)](jsd-configure-connector.md "jsd-configure-connector.md"), makes AWS product
request types available, but Jira Service Management users won't see
the request type until you add it to a **Request Type
Group**.

###### To configure request types

1. In the AWS Service Management Connector for Jira Service
   Management, go to the **Connector settings**
   page.
2. In the **Projects** section, choose
   **add the AWS request type**.
3. Choose **Add existing request type** in the
   upper right-hand corner.
4. Choose **Request AWS product** from the
   available request type.
5. Choose **Edit Groups** for the
   **Request AWS product** request type.
6. On the **Edit groups** form, choose
   **General**, then choose
   **Save**.

###### Note

When you create a custom **Request AWS
Product** request type for the Connector for Jira Service
Management, you do not need to edit to the **Request AWS
Product** request type. You can add a request type to an
existing group. If you don't have a group, create a new group and
add the request type to it.
