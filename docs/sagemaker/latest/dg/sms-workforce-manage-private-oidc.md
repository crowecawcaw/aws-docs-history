# Manage a Private Workforce (OIDC

IdP)

Once you've created a private workforce using your OpenID Connect (OIDC) Identity Provider (IdP), you can manage your workers
using your IdP. For example, you can add, remove, and group workers directly through your
IdP.

To add workers to an Amazon SageMaker Ground Truth (Ground Truth) labeling job or Amazon Augmented AI (Amazon A2I) human review
task, you create work teams using 1-10 IdP groups and assign that work team to the job or
task. You assign a work team to a job or task by specifing that work team when you create a
labeling job (Ground Truth) or a human review workflow (Amazon A2I).

You can only assign one team to each labeling job or human review workflow. You can use
the same team to create multiple labeling jobs or human review tasks. You can also create
multiple work teams to work on different labeling jobs or human review tasks.

## Prerequisites

To create and manage private work teams using your OIDC IdP groups, first you must
create a workforce using the SageMaker API operation [`CreateWorkforce`](../APIReference/API_CreateWorkforce.md "../APIReference/API_CreateWorkforce.md"). To learn more, see [Create a Private Workforce (OIDC
IdP)](sms-workforce-create-private-oidc.md "sms-workforce-create-private-oidc.md").

## Add work teams

You can use the SageMaker AI console to create a private work team using your OIDC IdP
workforce on the **Labeling workforces** page under
**Ground Truth**. If you are creating a Ground Truth labeling job, you can also
create a private work team while creating a labeling job.

###### Note

You create and manage work teams for Amazon A2I in the Ground Truth area of the SageMaker AI
console.

You can also use the SageMaker API and associated language-specific SDKs to create a
private work team.

Use the following procedures to learn how to create a private work team using the SageMaker AI
console and API.

###### To create a private work team on the Labeling workforces page (console)

1. Go to the Ground Truth area of the SageMaker AI console: [https://console.aws.amazon.com/sagemaker/groundtruth](https://console.aws.amazon.com/sagemaker/groundtruth "https://console.aws.amazon.com/sagemaker/groundtruth").
2. Select **Labeling workforces**.
3. Select **Private**.
4. In the **Private teams** section, select **Create
   private team**.
5. In the **Team details** section, enter a **Team
   name**.
6. In the **Add workers** section, enter the name of a single
   user group. All workers associated with this group in your IdP are added to this
   work team.
7. To add more than one user group, select **Add new user
   group** and enter the names of the user groups you want to add to
   this work team. Enter one user group per line.
8. (Optional) For Ground Truth labeling jobs, if you provide an email for workers in
   your JWT, Ground Truth notifies workers when a new labeling task is available if you
   select an SNS topic.
9. Select **Create private team**.

###### To create a private work team while creating a Ground Truth labeling job

(console)

1. Go to the Ground Truth area of the SageMaker AI console: [https://console.aws.amazon.com/sagemaker/groundtruth](https://console.aws.amazon.com/sagemaker/groundtruth "https://console.aws.amazon.com/sagemaker/groundtruth").
2. Select **Labeling jobs**.
3. Use the instructions in [Create a Labeling Job (Console)](sms-create-labeling-job-console.md "sms-create-labeling-job-console.md") to create a labeling job.
   Stop when you get to the **Workers** section on the second
   page.
4. Select **Private** for your worker type.
5. Enter a **Team name**.
6. In the **Add workers** section, enter the name of a single
   user group under **User groups**. All workers associated with
   this group in your IdP are added to this work team.

###### Important

The group names you specify for **User groups** must
match the group names specified in your OIDC IdP. 7. To add more than one user group, select **Add new user
group** and enter the names of the user groups you want to add to
this work team. Enter one user group per line. 8. Complete all remaining steps to create your labeling job.

The private team that you create is used for this labeling job, and is listed in the
**Labeling workforces** section of the SageMaker AI console.

###### To create a private work team using the SageMaker API

You can create a private work team using the SageMaker API operation `CreateWorkteam`.

When you use this operation, list all user groups that you want included in the work
team in the `OidcMemberDefinition` parameter `Groups`.

###### Important

The group names you specify for `Groups` must match the group names
specified in your OIDC IdP.

For example, if your user group names are `group1`, `group2`,
and `group3` in your OIDC IdP, configure `OidcMemberDefinition` as
follows:

```
 "OidcMemberDefinition": {
    "Groups": ["group1", "group2", "group3"]
  }
```

Additionally, you must give the work team a name using the `WorkteamName`
parameter.

## Add or remove IdP groups from work

teams

After you've created a work team, you can use the SageMaker API to manage that work team.
Use the [`UpdateWorkteam`](../APIReference/API_UpdateWorkteam.md "../APIReference/API_UpdateWorkteam.md") operation to update the IdP user groups
included in that work team.

- Use the `WorkteamName` parameter to identify the work team that you
  want to update.
- When you use this operation, list all user groups that you want included in
  the work team in the [`OidcMemberDefinition`](../APIReference/API_OidcMemberDefinition.md "../APIReference/API_OidcMemberDefinition.md") parameter
  `Groups`. If a user group is associated with a work team and you do
  _not_ include it in this list, that user group is no
  longer associated with this work team.

## Delete a work

team

You can delete a work team using the SageMaker AI console and SageMaker API.

###### To delete a private work team in the SageMaker AI console

1. Go to the Ground Truth area of the SageMaker AI console: [https://console.aws.amazon.com/sagemaker/groundtruth](https://console.aws.amazon.com/sagemaker/groundtruth "https://console.aws.amazon.com/sagemaker/groundtruth").
2. Select **Labeling workforces**.
3. Select **Private**.
4. In the **Private teams** section, select the work team that
   you want to delete.
5. Select **Delete**.

###### To delete a private work team (API)

You can delete a private work team using the SageMaker API operation `DeleteWorkteam`.

## Manage Individual Workers

When you create a workforce using your own OIDC IdP, you cannot use Ground Truth or
Amazon A2I to manage individual workers.

- To add a worker to a work team, add that worker to a group associated with
  that work team.
- To remove a worker from a work team, remove that worker from all user groups
  associated with that work team.

## Update, Delete, and Describe Your

Workforce

You can update, delete, and describe your OIDC IdP workforce using the SageMaker API. The
following is a list of API operations that you can use to manage your workforce. For
additional details, including how you can locate your workforce name, see [Private workforce management using the
Amazon SageMaker API](sms-workforce-management-private-api.md "sms-workforce-management-private-api.md").

- [`UpdateWorkforce`](../APIReference/API_UpdateWorkforce.md "../APIReference/API_UpdateWorkforce.md") – You may want to update a
  workforce created using your own OIDC IdP to specify a different authorization
  endpoint, token endpoint, or issuer. You can update any parameter found in
  `OidcConfig` using this operation.

You can only update your OIDC IdP configuration when there are no work teams
associated with your workforce. To learn how to delete work teams, see [Delete a work
team](#sms-workforce-manage-private-oidc-workteam-delete "#sms-workforce-manage-private-oidc-workteam-delete").

- [`DeleteWorkforce`](../APIReference/API_DeleteWorkforce.md "../APIReference/API_DeleteWorkforce.md") – Use this operation to
  delete your private workforce. If you have any work teams associated with your
  workforce, you must delete those work teams before you delete your work force.
  For more information, see [Delete a work
  team](#sms-workforce-manage-private-oidc-workteam-delete "#sms-workforce-manage-private-oidc-workteam-delete").
- [`DescribeWorkforce`](../APIReference/API_DescribeWorkforce.md "../APIReference/API_DescribeWorkforce.md") – Use this operation to
  list private workforce information, including workforce name, Amazon Resource
  Name (ARN), and, if applicable, allowed IP address ranges (CIDRs).
