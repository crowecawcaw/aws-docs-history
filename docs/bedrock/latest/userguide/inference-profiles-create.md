# Create an application inference profile

You can create an application inference profile with one or more Regions to track usage and costs when invoking a model.

- To create an application inference profile for one Region, specify a foundation model. Usage and costs for requests made to that Region with that model will be tracked.
- To create an application inference profile for multiple Regions, specify a cross Region (system-defined) inference profile. The inference profile will route requests to the Regions defined in the cross Region (system-defined) inference profile that you choose. Usage and costs for requests made to the Regions in the inference profile will be tracked.
  Currently, you can only create an inference profile using the Amazon Bedrock API.

To create an inference profile, send a [CreateInferenceProfile](../APIReference/API_CreateInferenceProfile.md "../APIReference/API_CreateInferenceProfile.md") request with an [Amazon Bedrock control plane endpoint](../../../general/latest/gr/bedrock.md#br-cp "../../../general/latest/gr/bedrock.md#br-cp").

The following fields are required:

| Field                | Use case                                                                                                                                                                 |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| inferenceProfileName | To specify a name for the inference profile.                                                                                                                             |
| modelSource          | To specify the foundation model or cross Region (system-defined) inference profile<br>that defines the model and Regions for which you want to track costs and<br>usage. |

The following fields are optional:

| Field              | Use case                                                                                                                                                                                                                                                                                                                           |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| description        | To provide a description for the inference profile.                                                                                                                                                                                                                                                                                |
| tags               | To attach tags to the inference profile. For more information,<br>see [Tagging Amazon Bedrock resources](tagging.md "tagging.md") and [Organizing and tracking costs using AWS cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md"). |
| clientRequestToken | To ensure the API request completes only once. For more information, see [Ensuring idempotency](../../../ec2/latest/devguide/ec2-api-idempotency.md "../../../ec2/latest/devguide/ec2-api-idempotency.md").                                                                                                                        |

The response returns an `inferenceProfileArn` that can be used in other inference profile-related actions and that can be used with model invocation and Amazon Bedrock resources.
