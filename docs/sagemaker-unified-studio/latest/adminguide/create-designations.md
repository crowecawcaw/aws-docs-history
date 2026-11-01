

# Create designations
<a name="create-designations"></a>

You can create designations to define custom permission sets for project members in your Amazon SageMaker Unified Studio domain. After you create a designation, you can assign it to project members to control which actions they can perform within the project.

## Prerequisites
<a name="create-designation-prerequisites"></a>

Before you create a designation, review the following requirements:
+ You must have the Administrator designation at the domain level.
+ Each domain supports up to 10 designations by default, with a maximum of 100.

## To create a designation
<a name="create-designation-console"></a>

1. Sign in to the Amazon SageMaker Unified Studio domain management portal.

1. In the navigation pane, choose **Designations**.

1. Choose **Create designation**.

1. For **Name**, enter a name for the designation. Designation names must be unique within the domain and can contain up to 64 characters.

1. For **Description**, enter a description for the designation.

1. For **Allow delete**, the checkbox is cleared by default, which prevents the designation from being deleted. To allow the designation to be deleted later, select **Allow delete**.

1. In the visual permission selector, select the permissions to include in the designation. Permissions are grouped by categories such as Catalog, Project, Subscriptions, Connections, Notebooks, and Data Agent.

1. Choose **Create**.

![Create designation page in Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/images/designations/Designations-Create.png)


## To duplicate an existing designation
<a name="duplicate-designation"></a>

You can create a designation by duplicating an existing designation. Duplicating pre-selects a set of permissions for you to customize.

1. In the navigation pane, choose **Designations**.

1. For the designation that you want to duplicate, in the **Action** column, choose the options menu (⋮), and then choose **Duplicate designation**.

1. Modify the auto-selected permissions as needed, or leave them as-is.

1. Choose **Create**.

![Duplicate designation in Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/images/designations/Designations-Duplicate.png)


## To create a designation (AWS CLI)
<a name="create-designation-cli"></a>

To create a designation using the AWS CLI, run the `create-designation` command.

```
aws datazone create-designation \
    --domain-identifier "dzd_example1234" \
    --name "Data Engineer" \
    --delete-protection \
    --description "Can manage data sources and create assets" \
    --policy 'permit(principal, action in [DataZone::Action::"CreateDataSource", DataZone::Action::"UpdateDataSource", DataZone::Action::"CreateAsset"], resource);'
```

**Note**  
To create the designation without delete protection, use the `--no-deletion-protection` flag.