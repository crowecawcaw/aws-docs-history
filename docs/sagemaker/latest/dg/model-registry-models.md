# Model Registry Models, Model Versions, and Model

Groups

The SageMaker Model Registry is structured as several Model (Package) Groups with model packages in
each group. These Model Groups can optionally be added to one or more Collections. Each
model package in a Model Group corresponds to a trained model. The version of each model
package is a numerical value that starts at 1 and is incremented with each new model
package added to a Model Group. For example, if 5 model packages are added to a Model
Group, the model package versions will be 1, 2, 3, 4, and 5.

A model package is the actual model that is registered into the Model Registry as a versioned
entity. There are two types of model packages in SageMaker AI. One type is used in the AWS
Marketplace, and the other is used in the Model Registry. Model packages used in the AWS
Marketplace are not versionable entities and are not associated with Model Groups in the
Model Registry. The Model Registry receives every new model that you retrain, gives it a version,
and assigns it to a Model Group inside the Model Registry. The following image shows an
example of a Model Group with 25 consecutively-versioned models. For more information
about model packages used in the AWS Marketplace, see [Algorithms and packages in the AWS Marketplace](sagemaker-marketplace.md "sagemaker-marketplace.md").

The model packages used in the Model Registry are versioned, and **must** be associated with a Model Group. The ARN of this model package
type has the structure:
`'arn:aws:sagemaker:`region`:`account`:`model-package-group`/`version`'`

The following topics show you how to create and work with models, model versions, and
Model Groups in the Model Registry.

###### Topics

- [Create a Model Group](model-registry-model-group.md "model-registry-model-group.md")
- [Delete a Model Group](model-registry-delete-model-group.md "model-registry-delete-model-group.md")
- [Register a Model Version](model-registry-version.md "model-registry-version.md")
- [View Model Groups and Versions](model-registry-view.md "model-registry-view.md")
- [Update the Details of a Model
  Version](model-registry-details.md "model-registry-details.md")
- [Compare Model Versions](model-registry-version-compare.md "model-registry-version-compare.md")
- [View and Manage Model Group and Model Version
  Tags](model-registry-tags.md "model-registry-tags.md")
- [Delete a Model Version](model-registry-delete-model-version.md "model-registry-delete-model-version.md")
- [Staging Construct for your Model
  Lifecycle](model-registry-staging-construct.md "model-registry-staging-construct.md")
- [Update the Approval Status of a
  Model](model-registry-approve.md "model-registry-approve.md")
- [Deploy a Model from the Registry with
  Python](model-registry-deploy.md "model-registry-deploy.md")
- [Deploy a Model in Studio](model-registry-deploy-studio.md "model-registry-deploy-studio.md")
- [Cross-account discoverability](model-registry-ram.md "model-registry-ram.md")
- [View the Deployment History of a
  Model](model-registry-deploy-history.md "model-registry-deploy-history.md")
- [View model lineage details in
  Studio](model-registry-lineage-view-studio.md "model-registry-lineage-view-studio.md")
