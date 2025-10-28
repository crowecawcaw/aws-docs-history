# Delete an application inference profile

If you no longer need an application inference profile, you can delete it. You can only delete inference profiles through the Amazon Bedrock API.

To delete an inference profile, send a [DeleteInferenceProfile](../APIReference/API_DeleteInferenceProfiles.md "../APIReference/API_DeleteInferenceProfiles.md") request with an [Amazon Bedrock control plane endpoint](../../../general/latest/gr/bedrock.md#br-cp "../../../general/latest/gr/bedrock.md#br-cp") and specify the Amazon Resource Name (ARN) or ID of the inference profile to delete in the `inferenceProflieIdentifier` field.
