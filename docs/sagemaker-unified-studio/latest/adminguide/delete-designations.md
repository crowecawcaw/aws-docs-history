

# Delete designations
<a name="delete-designations"></a>

You can delete a designation only when **Allow delete** is selected for the designation. You cannot delete managed designations (Owner and Contributor).

**Important**  
Before deleting a designation, verify that no project members are currently assigned to it. If you delete a designation that is assigned to project members, those members remain members of the project but have no permissions within that project. You must reassign those members to a valid designation to restore their access.

## To delete a designation
<a name="delete-designation-console"></a>

1. Sign in to the Amazon SageMaker Unified Studio domain management portal.

1. In the navigation pane, choose **Designations**.

1. Select the designation that you want to delete.

1. Verify that **Allow delete** is selected for the designation. If it is not selected, edit the designation and select **Allow delete** before proceeding.

1. Choose **Delete**.

1. In the **Delete designation** dialog box, enter **confirm**.

1. Choose **Delete**.

![Delete a designation in Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/images/designations/Designations-Delete.png)


## To delete a designation (AWS CLI)
<a name="delete-designation-cli"></a>

To delete a designation using the AWS CLI, run the `delete-designation` command.

```
aws datazone delete-designation \
    --domain-identifier "dzd_example1234" \
    --identifier "dry7c1plpxl0k6"
```

To delete a designation that has deletion protection turned on, you must first update the designation to turn off deletion protection. Run the following command to turn off deletion protection, and then run the `delete-designation` command.

```
aws datazone update-designation \
    --domain-identifier "dzd_example1234" \
    --identifier "dry7c1plpxl0k6" \
    --no-deletion-protection
```