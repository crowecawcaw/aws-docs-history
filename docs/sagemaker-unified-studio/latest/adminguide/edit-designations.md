

# Edit designations

When you update a designation's permissions, the change takes effect immediately for all members assigned that designation across all projects. You don't need to reassign the designation to members.

You can start with broad permissions and restrict them over time, or add permissions as new capabilities become available in Amazon SageMaker Unified Studio. You can't edit the permissions of the managed designations (Owner and Contributor). However, you can add, change, or remove a layout customization for any designation, including the managed Owner and Contributor designations.

## To edit a designation
<a name="edit-designation-console"></a>

1. Sign in to the Amazon SageMaker Unified Studio domain management portal.

1. In the navigation pane, choose **Designations**.

1. Choose the name of the designation that you want to update.

1. Choose **Edit**.

1. Modify the permissions in the visual permission selector.

1. To change the designation's layout customization, select the navigation items to show, and clear the ones to hide. To remove the layout customization, clear the **Define a layout customization for this designation** checkbox at the top of step two. Members who have the designation then see the full default left navigation pane.

1. Choose **Save**.

**Note**  
For the managed Owner and Contributor designations, you can modify only the layout customization. You can't change their permissions.

The following image shows the edit designation page, where you can change the designation's permissions and its layout customization options.

![The edit designation page in Amazon SageMaker Unified Studio, showing the layout customization options](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/images/designations/designation-edit-v2.png)


## To edit a designation (AWS CLI)
<a name="edit-designation-cli"></a>

To update a designation using the AWS CLI, run the `update-designation` command.

```bash
aws datazone update-designation \
    --domain-identifier "dzd_example1234" \
    --identifier "dry7c1plpxl0k6" \
    --name "Data Analyst" \
    --description "Can manage data sources and create assets" \
    --policy 'permit(principal, action in [DataZone::Action::"CreateDataSource", DataZone::Action::"UpdateDataSource", DataZone::Action::"CreateAsset"], resource);' \
    --deletion-protection
```