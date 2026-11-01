

# Assign designations
<a name="assign-designations"></a>

You assign project-level designations when you add members to a project or by editing existing project members. Each member has one designation through direct assignment. Members can also inherit designations through group membership. If you directly assign one designation to a user who also belongs to a group with a different designation, the user receives the union of both permission sets.

![Assign designations to project members in Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/images/designations/Designations-Assign.png)


**Important**  
Admin project membership takes precedence over project designations. If a user is a member of the `admin-project-{{accountID}}`, those permissions override the designation that is assigned to them in another project. For example, a user who belongs to the admin project but has a read-only designation in a separate project can still perform privileged actions in that project, such as deleting project members.

## To assign designations from the Amazon SageMaker Unified Studio portal (Identity Center-based domains)
<a name="assign-designations-portal"></a>

1. Navigate to the project in the Amazon SageMaker Unified Studio portal.

1. Choose the **Members** tab.

1. To add members, choose **Add members**.

1. Select the member.

1. Select the designation for the member.

1. Choose **Add members**.

1. To update an existing member, select a designation from the **Designation** column for that user.

## To assign designations from the domain management portal
<a name="assign-designations-domain-portal"></a>

You can assign designations from the domain management portal for both IAM and Identity Center-based domains.

1. Sign in to the Amazon SageMaker Unified Studio domain management portal.

1. In the navigation pane, choose **Projects**.

1. Select the project.

1. Choose the **Members** tab.

1. To update an existing member, select a designation from the **Project designation** column for that user.

1. To add members, choose **Add members**.

1. Select the **Type** and **Member**.

## To assign a designation (AWS CLI)
<a name="assign-designations-cli"></a>

To assign a designation using the AWS CLI, run the `create-project-membership` command.

The `--designation` field accepts one of the following values: `PROJECT_OWNER`, `PROJECT_CONTRIBUTOR`, or `USER_CREATED_DESIGNATION`. When you specify `USER_CREATED_DESIGNATION`, you must also specify the `--user-created-designation-id` parameter, which is the ID of the custom designation to assign.

```
aws datazone create-project-membership \
    --domain-identifier "dzd_example1234" \
    --project-identifier "proj_example5678" \
    --member '{"userIdentifier": "u-abc123def456"}' \
    --designation "USER_CREATED_DESIGNATION" \
    --user-created-designation-id "123456789"
```