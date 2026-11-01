

# Edit designations
<a name="edit-designations"></a>

When you update a designation's permissions, the change takes effect immediately for all members assigned that designation across all projects. You don't need to reassign the designation to members.

You can start with broad permissions and restrict them over time, or add permissions as new capabilities become available in Amazon SageMaker Unified Studio. You cannot edit managed designations (Owner and Contributor).

## To edit a designation
<a name="edit-designation-console"></a>

1. Sign in to the Amazon SageMaker Unified Studio domain management portal.

1. In the navigation pane, choose **Designations**.

1. Choose the name of the designation that you want to update.

1. Choose **Edit**.

1. Modify the permissions in the visual permission selector.

1. Choose **Save**.

![Edit a designation in Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/images/designations/Designations-Edit-2.png)


## To edit a designation (AWS CLI)
<a name="edit-designation-cli"></a>

To update a designation using the AWS CLI, run the `update-designation` command.

```
aws datazone update-designation \
    --domain-identifier "dzd_example1234" \
    --identifier "dry7c1plpxl0k6" \
    --name "Data Analyst" \
    --description "Can manage data sources and create assets" \
    --policy 'permit(principal, action in [DataZone::Action::"CreateDataSource", DataZone::Action::"UpdateDataSource", DataZone::Action::"CreateAsset"], resource);' \
    --deletion-protection
```