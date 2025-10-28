# Update a model

package stage and status in Studio

To use a model package stage construct, you will need to assume an execution
role with the relevant permissions. The following page provides information on
how to update the stage status using Amazon SageMaker Studio.

All stage constructs defined in the domain will be viewable by all users.
To update a stage, you will need have the administrator set up the relevant
permissions for you to access it. For information on how, see [Set up Staging
Construct Examples](model-registry-staging-construct-set-up.md "model-registry-staging-construct-set-up.md").

The following procedure will take you to the Studio UI where you can
update your model package stage.

1. Sign in to Amazon SageMaker Studio. For more information, see [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. In the left navigation pane, choose the
   **Models**.
3. Find your model.
   - You can use the tabs to find your models. For example, choose
     the **Registered models** or
     **Deployable models** tabs.
   - You can use the **My models** and
     **Shared with me** options to find models
     you created or ones that are shared by you.

4. Select the checkbox next to the model you wish to update.
5. Choose the **More options** icon.
6. Choose **Update model lifecycle**. This will take you
   to the **Update model lifecycle** section.
7. Complete the tasks to update the stage.

If you cannot update the stage, you will receive an error. Your
administrator will need to set up the permissions for you to do so. For
information on how to set up the permissions, see [Set up Staging
Construct Examples](model-registry-staging-construct-set-up.md "model-registry-staging-construct-set-up.md").
