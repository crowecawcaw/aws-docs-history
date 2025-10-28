# Custom ML modeling

prerequisites

Before you can perform custom ML modeling, you should consider the
following:

- Determine whether both model training and inference on the trained model
  is going to be performed in the collaboration.
- Determine the role that each collaboration member will perform and assign
  them the appropriate abilities.
  - Assign the `CAN_QUERY` ability to the member who will
    train the model and run inference on the trained model.
  - Assign the `CAN_RECEIVE_RESULTS` to at least one member
    of the collaboration.
  - Assign `CAN_RECEIVE_MODEL_OUTPUT` or
    `CAN_RECEIVE_INFERENCE_OUTPUT` abilities to the
    member that will receive trained model exports or inference
    output,
    respectively. You can choose to use both abilities if they are
    required by your use-case.

- Determine the maximum size of the trained model artifacts or inference
  results that you will allow to be exported.
- We recommend that all users have the `CleanrooomsFullAccess`
  and `CleanroomsMLFullAccess` policies attached to their role.
  Using custom ML models requires using both the AWS Clean Rooms and AWS Clean Rooms ML
  SDKs.
- Consider the following information about IAM roles.
  - All data providers must have a service access role that allows
    AWS Clean Rooms to read data from their AWS Glue catalogs and tables, and the
    underlying Amazon S3 locations. These roles are similar to those required
    for SQL querying. This allows you to use the
    `CreateConfiguredTableAssociation` action. For more
    information, see [Create a service role to
    create a configured table association](ml-roles.md#ml-roles-custom-configure-table "ml-roles.md#ml-roles-custom-configure-table").
  - All members that want to receive metrics must have a service
    access role that allows them to write CloudWatch metrics and logs. This
    role is used by Clean Rooms ML to write all model metrics and logs to the
    member's AWS account during model training and inference. We also
    provide privacy controls to determine which members have access to
    the metrics and logs. This allows you to use the
    `CreateMLConfiguration` action. For more information
    see, [Create a service role for custom ML
    modeling - ML Configuration](ml-roles.md#ml-roles-custom-configure "ml-roles.md#ml-roles-custom-configure").

  The member receiving results must provide a service access role
  with permissions to write to their Amazon S3 bucket. This role allows
  Clean Rooms ML to export results (trained model
  artifacts
  or inference results) to an Amazon S3 bucket. This allows you to use the
  `CreateMLConfiguration` action. For more information,
  see [Create a service role for custom ML
  modeling - ML Configuration](ml-roles.md#ml-roles-custom-configure "ml-roles.md#ml-roles-custom-configure").
  - The model provider must provide a service access role with
    permissions to read their Amazon ECR repository and image. This allows
    you to use the `CreateConfigureModelAlgorithm` action.
    For more information, see [Create a service role to
    provide a custom ML model](ml-roles.md#ml-roles-custom-model-provider "ml-roles.md#ml-roles-custom-model-provider").
  - The member that creates the `MLInputChannel` to
    generate datasets for
    training
    or inference must provide a service access role that allows Clean Rooms ML
    to execute an SQL query in AWS Clean Rooms. This allows you to use the
    `CreateTrainedModel` and
    `StartTrainedModelInferenceJob` actions. For more
    information, see [Create a service role to query a
    dataset](ml-roles.md#ml-roles-custom-query-dataset "ml-roles.md#ml-roles-custom-query-dataset").

- Model authors should follow the [Model authoring guidelines for the
  training container](custom-model-guidelines.md "custom-model-guidelines.md") and [Model authoring guidelines for the
  inference container](inference-model-guidelines.md "inference-model-guidelines.md") to ensure model inputs and
  outputs are configured as expected by AWS Clean Rooms.
