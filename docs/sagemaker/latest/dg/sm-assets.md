# Controlled access to assets with Amazon SageMaker Assets

Use Amazon SageMaker Assets to provide controlled and regulated access to _assets_,
models or data tables, belonging to your organization. Within SageMaker Assets, users from different
AWS accounts can create and share assets related to specific business problems without
additional administrator overhead. Instead of having permissions being statically tied to
their identity, users can provide permissions to assets that they’re using for their active
workflows.

Assets are ML assets or data assets. ML assets are metadata that point to Amazon SageMaker Feature Store feature
groups or SageMaker Model Registry Model Groups. Data assets are metadata that point to Amazon Redshift
tables or AWS Glue tables.

For example, the asset for a model group contains the model group name and the Amazon
Resource Name (ARN) for the model package group. The asset points to the underlying
collection of models. The asset itself can be shared between users.

Users can create assets for their own projects. They can make them visible to users who
aren't members of those projects. The users who aren't project members can search through
the assets and read their metadata. They can use the metadata to determine whether they want
to access to the underlying source of data.

To understand the SageMaker Assets workflow better, imagine that you have two groups of users in
your organization, Group A and Group B. The users in Group A are looking to predict home
prices. They’re looking to collaborate with the users in Group B who are in a different
AWS account. They have housing data stored in AWS Glue tables. They also have different
models saved as model packages within a model group. With SageMaker Assets, the users in Group A can
share their AWS Glue tables and model packages with the users in Group B in a few clicks.
Without administrator intervention, the users in Group A provided precisely scoped
permissions to the users in Group B.

Users can create assets and publish them to make them visible throughout the organization.
Other users can request access to those assets.

###### Topics

- [Set up SageMaker Assets (administrator guide)](sm-assets-set-up.md "sm-assets-set-up.md")
- [Work with assets (user guide)](sm-assets-user-guide.md "sm-assets-user-guide.md")
