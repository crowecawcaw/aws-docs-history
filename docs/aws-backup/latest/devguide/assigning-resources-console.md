# Assign resources using the AWS Backup

console

###### To navigate to the **Assign resources** page:

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. Choose **Backup plans**.
3. Choose **Create Backup plan**.
4. Select any template in the **Choose template** dropdown list, then
   choose **Create plan**.
5. Type in a **Backup plan name**.
6. Choose **Create plan**.
7. Choose **Assign resources**.

###### To begin your resource assignment, in the **General**

section:

1. Type in a **Resource assignment name**.
2. Choose the **Default role** or **Choose an IAM
   role**.

###### Note

If you choose an IAM role, verify that it has permission to back up all the
resources you are about assign. If your role encounters a resource that it doesn't
have permission to back up, your backup plan will fail.
To assign your resources, in the **Assign resources** section, choose
one of the two options under **Define resource selection**:

- **Include all resource types**. This option configures your backup
  plan to protect all current and future AWS Backup-supported resources assigned to your backup
  plan. Use this option to quickly and easily protect your data estate.

When you choose this option, you can optionally **Refine selection using
tags** as the next step.

- **Include specific resource types**. When you choose this option,
  you must **Select specific resource types** with the following
  steps:

      1. Using the **Select resource types** dropdown menu, assign one
       or more resource types.


      Once you finish, AWS Backup presents you the list of resource types you selected and
       its default setting, which is to protect all resources for each selected resource
       type.
      2. Optionally, if you want to exclude specific resources from a resource type you
       selected:



      	1. Use the **Choose resources** dropdown menu and deselect the
      	 default option.
      	2. Select the specific resources to assign to your backup plan.
      3. Optionally, you can **Exclude specific resource IDs from the selected
       resource types**. Use this option if you want to exclude one or a few
       resources out of many, because doing so might be faster than selecting many
       resources during the previous step. You must include a resource type before you can
       exclude resources from that resource type. Exclude a resource ID using the following
       steps:



      	1. Under **Exclude specific resource IDs from the selected resource
      	 types**, choose one or more of the resource types that you included
      	 using **Select resource types**.
      	2. For each resource type, use the **Choose resources** menu
      	 to select one or more resources to exclude.

  In addition to your previous choices, you can make even more granular selections using
  the optional **Refine selection using tags** feature. This feature allows
  you to refine your current selection to include a subset of your resources using
  tags.

Tags are key-value pairs that you can assign to specific resources to help you identify,
organize, and filter your resources. Tags are case sensitive. For more information about
tags, see [Tagging
your AWS resources](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md").

When you refine your selection using two or more tags, the effect is an AND condition.
For example, if you refine your selection using two tags, `env: prod` and
`role: application`, you only assign resources with BOTH tags to your backup
plan.

###### To refine your selection using tags:

1. Under **Refine selection using tags**, choose a
   **Key** from the list.
2. Choose a **Condition for value** from the list.
   - _Value_ refers to the next input, the value of your key-value
     pair.
   - **Condition** can be `Equals`,
     `Contains`, `Begins with`, or `Ends with`, or their
     inverse: `Does not equal`, `Does not contain`, `Does not
begin with`, or `Does not end with`.

3. Choose a **Value** from the list.
4. To further refine using another tag, choose **Add tag**.
