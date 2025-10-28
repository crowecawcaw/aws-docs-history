# Editing an

OpsItem

The **OpsItem details** section includes information about an OpsItem,

including the description, title, source, OpsItem ID, and the status.
You can edit a
single OpsItem or you can select multiple OpsItems and edit the
following fields:
**Status**, **Priority**,

**Severity**, **Category**.

When Amazon EventBridge creates an OpsItem, it populates the **Title**,
**Source**, and **Description** fields. You
can edit the **Title** and **Description** fields,
but you can't edit the **Source** field.

###### Note

The console supports most markdown formatting in the OpsItem description
field. For more information, see [Using Markdown in the
Console](../../../awsconsolehelpdocs/latest/gsg/aws-markdown.md "../../../awsconsolehelpdocs/latest/gsg/aws-markdown.md") in the _Getting Started with the AWS Management Console Getting Started
Guide._

Generally, you can edit the following configurable data for an OpsItem:

- Title – Name of the OpsItem. The source
  creates the title of the OpsItem.
- Description – Information about this
  OpsItem including (if applicable) steps for reproducing the issue.
- Status – Status of an OpsItem. For a
  list of valid status values, see [OpsItem Status](../APIReference/API_OpsItem.md#systemsmanager-Type-OpsItem-Status "../APIReference/API_OpsItem.md#systemsmanager-Type-OpsItem-Status") in the _AWS Systems Manager API Reference_.
- Priority – Priority of an OpsItem can
  be between 1 and 5. We recommend that your organization determine what each
  priority level means and a corresponding service level agreement for each
  level.
- Severity – Severity of an OpsItem can
  be between 1 to 4, where 1 is critical, 2 is high, 3 is medium, and 4 is
  low.
- Category – Category of an OpsItem can
  be availability, cost, performance, recovery, or security.
- Notifications – When you edit an
  OpsItem, you can specify the Amazon Resource Name (ARN) of an Amazon Simple Notification Service topic
  in the **Notifications** field. By specifying an ARN, you
  ensure that all stakeholders receive a notification when the OpsItem is edited,
  including a status change. For more information, see the [_Amazon Simple Notification Service Developer Guide_](../../../sns/latest/dg.md "../../../sns/latest/dg.md").

###### Important

The Amazon SNS topic must exist in the same AWS Region as the OpsItem. If
the topic and the OpsItem are in different Regions, the system returns an
error.
OpsCenter has bidirectional integration with AWS Security Hub. When you update an OpsItem
status and severity related to a security finding, those changes are automatically
sent to Security Hub to ensure you always see the latest and correct information.

When an OpsItem is created from a Security Hub finding, Security Hub metadata is automatically
added to the operational data field of the OpsItem. If this metadata is deleted, the
bidirectional updates no longer function.

###### To edit OpsItem details

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **OpsCenter**.
3. Choose an OpsItem ID to open the details page or choose multiple OpsItems. If
   you choose multiple OpsItems, you can only edit the status, priority, severity,
   or category. If you edit multiple OpsItems, OpsCenter updates and saves your
   changes as soon as you choose the new status, priority, severity, or
   category.
4. In the **OpsItem details** section, choose
   **Edit**.
5. Edit the details of the OpsItem according to the requirements and guidelines
   specified by your organization.
6. When you're finished, choose **Save**.
