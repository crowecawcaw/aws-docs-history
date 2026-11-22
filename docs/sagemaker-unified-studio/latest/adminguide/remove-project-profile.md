

# Disassociate a project profile from a project

Projects created in IAM-based and Identity Center-based domains where no project profile was specified might use a managed project profile named "Default Project Profile". With the Default Project Profile, members can deploy only the S3Bucket and S3TableCatalog blueprints from resource blueprints. To allow a project's members to deploy other blueprints, a domain management administrator disassociates the Default Project Profile from the project.

After the project profile is disassociated, the project's resource provisioning is governed by blueprint authorization grants, and members can deploy the blueprints that their designations authorize, on demand.

## Prerequisites
<a name="disassociate-prerequisites"></a>

Only a domain management administrator, who is a member of the admin project (admin-project-{{AccountId}}), can disassociate a project profile. Project owners can't disassociate a project profile, even if they can otherwise update the project.

You can only disassociate a project profile from a project if the project profile uses the ToolingLite managed blueprint. In most cases, this happens if you created projects in an IAM-based domain, or if you created projects in an Identity Center-based domain without specifying a project profile.

## Considerations
<a name="disassociate-considerations"></a>

You can't undo disassociating a project profile. After you disassociate a project profile, you can't associate a project profile with the project again. When you disassociate a profile:
+ Blueprint parameters become editable. Parameters that the profile marked as non-editable become fully editable — for example, a member could select larger compute instances. To keep these controlled, remove the corresponding permissions from the relevant designations, disable the blueprint, or restrict the blueprint's provisioning role.
+ The set of blueprints that members can deploy expands, according to their designation grants.
+ The profile's parameter overrides, locked parameters, and deployment order are permanently removed from the project.

**Note**  
Disassociating a project profile doesn't redeploy any resources. The project's existing environments keep running, and their current parameter values remain unchanged until the next time you update them.

## Disassociate a project profile by using the domain management portal
<a name="disassociate-using-portal"></a>

You can disassociate a project profile from the Amazon SageMaker Unified Studio domain management portal.

1. Sign in to the Amazon SageMaker Unified Studio domain management portal.

1. In the left navigation pane, choose **Projects**.

1. Choose the project.

1. At the top of the project page, in the **Update project to allow resource creation** banner, choose **Update**.

1. In the **Update project** dialog box, choose **Update**.

![The project page in the Amazon SageMaker Unified Studio domain management portal, showing the "Update project to allow resource creation" banner and the "Update project" confirmation dialog box.](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/images/resource-blueprints/resource-blueprints-update.png)


**Note**  
After you update the project, you must still grant designations access to the blueprints that members can deploy. For more information, see [Grant members access to deploy resource blueprints](grant-deploy-resource-blueprints.md).

## Disassociate a project profile by using the API
<a name="disassociate-using-api"></a>

You can disassociate a project profile programmatically with the AWS CLI or the API.

1. Confirm that the project is eligible. Call the `GetProject` operation to get the project's project profile identifier, and then call the `GetProjectProfile` operation to view the profile's details. The project must use the managed project profile named Default Project Profile, whose tooling blueprint is ToolingLite. Disassociation is permitted only when the tooling blueprint is ToolingLite.

   ```
   aws datazone get-project \
       --domain-identifier {{domain-id}} \
       --identifier {{project-id}}
   ```

   ```
   aws datazone get-project-profile \
       --domain-identifier {{domain-id}} \
       --identifier {{project-profile-id}}
   ```

1. Call the `UpdateProject` operation with the `project-profile-action` parameter set to `DISASSOCIATE`.

   ```
   aws datazone update-project \
       --domain-identifier {{domain-id}} \
       --identifier {{project-id}} \
       --project-profile-action DISASSOCIATE
   ```

1. Verify the change. Call the `GetProject` operation again. The response no longer includes a project profile identifier.