# Copying an Amazon Rekognition Custom Labels model (SDK)

You can use the [CopyProjectVersion](../APIReference/API_CopyProjectVersion.md "../APIReference/API_CopyProjectVersion.md") operation to copy an Amazon Rekognition Custom Labels model version from a
source Amazon Rekognition Custom Labels project to a destination project. The destination project can be in a
different AWS account, or in the same AWS account. A typical scenario is copying a
tested model from a development AWS account to a production AWS account.

Alternatively, you can train the model in the destination account with the source
dataset. Using the `CopyProjectVersion` operation has the following
advantages.

- Model behavior is consistent. Model training is non-deterministic and two
  models trained with same dataset aren't guaranteed to make the same predictions.
  Copying the model with `CopyProjectVersion` helps make sure that the
  behavior of the copied model is consistent with the source model and you won't
  need to re-test the model.
- Model training isn't required. This saves you money as you are charged for
  each successful training of a model.
  To copy a model to a different AWS account, you must have an Amazon Rekognition Custom Labels project in
  the destination AWS account. For information about creating a project, see [Creating a project](mp-create-project.md "mp-create-project.md"). Be sure to create
  the project in the destination AWS account.

A [project policy](md-create-project-policy-document.md "md-create-project-policy-document.md") is a
resource-based policy that sets copy permissions for the model version that you want to
copy. You will need to use a [project
policy](md-create-project-policy-document.md "md-create-project-policy-document.md") when the destination project is in a different AWS account from the
source project.

You do not need to use a [project
policy](md-create-project-policy-document.md "md-create-project-policy-document.md"), when copying model versions within the same account. However, you can
choose to use a [project policy](md-create-project-policy-document.md "md-create-project-policy-document.md")
on inter-account projects if you would like more control over these resources.

You attach the project policy to the source project by calling the [PutProjectPolicy](../APIReference/API_PutProjectPolicy.md "../APIReference/API_PutProjectPolicy.md") operation.

You can't use `CopyProjectVersion` to copy a model to a project in a
different AWS Region. Also, you can't copy a model with the Amazon Rekognition Custom Labels console. In
these cases, you can train the model in the destination project with the datasets used
to train the source model. For more information, see [Training an Amazon Rekognition Custom Labels model](training-model.md "training-model.md").

To copy a model from a source project to a destination project, do the
following:

###### To copy a model

1. [Create a project policy
   document](md-create-project-policy-document.md "md-create-project-policy-document.md").
2. [Attach the project policy to the
   source project](md-attach-project-policy.md "md-attach-project-policy.md").
3. [Copy the model with the
   CopyProjectVersion operation](md-copy-model-sdk.md "md-copy-model-sdk.md").
   To remove a project policy from a project, call [DeleteProjectPolicy](../APIReference/API_DeleteProjectPolicy.md "../APIReference/API_DeleteProjectPolicy.md"). To get a list of project policies attached to a
   project, call [ListProjectPolicies](../APIReference/API_ListProjectPolicies.md "../APIReference/API_ListProjectPolicies.md").

###### Topics

- [Creating a project policy
  document](md-create-project-policy-document.md "md-create-project-policy-document.md")
- [Attaching a project policy (SDK)](md-attach-project-policy.md "md-attach-project-policy.md")
- [Copying a model (SDK)](md-copy-model-sdk.md "md-copy-model-sdk.md")
- [Listing project policies (SDK)](md-list-project-policies.md "md-list-project-policies.md")
- [Deleting a project policy (SDK)](md-delete-project-policy.md "md-delete-project-policy.md")
