# Multi-Model Endpoint Security

Models and data in a multi-model endpoint are co-located on instance storage volume and in
container memory. All instances for Amazon SageMaker AI endpoints run on a single tenant container that
you own. Only your models can run on your multi-model endpoint. It's your responsibility to
manage the mapping of requests to models and to provide access for users to the correct target
models. SageMaker AI uses [IAM roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") to provide IAM identity-based policies that you use to specify
allowed or denied actions and resources and the conditions under which actions are allowed or
denied.

By default, an IAM principal with [`InvokeEndpoint`](../APIReference/API_InvokeEndpoint.md "../APIReference/API_InvokeEndpoint.md") permissions on a multi-model endpoint can invoke any
model at the address of the S3 prefix defined in the [`CreateModel`](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md") operation, provided that the IAM Execution Role defined
in operation has permissions to download the model. If you need to restrict [`InvokeEndpoint`](../APIReference/API_InvokeEndpoint.md "../APIReference/API_InvokeEndpoint.md") access to a limited set of models in S3, you can do one
of the following:

- Restrict `InvokeEndpont` calls to specific models hosted at the endpoint by
  using the `sagemaker:TargetModel` IAM condition key. For example, the
  following policy allows `InvokeEndpont` requests only when the value of the
  `TargetModel` field matches one of the specified regular expressions:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "sagemaker:InvokeEndpoint"
            ],
            "Effect": "Allow",
            "Resource":
            "arn:aws:sagemaker:`region`:`account-id`:endpoint/`endpoint_name`",
            "Condition": {
                // TargetModel provided must be from this set of values
                "StringLike": {
                    "sagemaker:TargetModel": ["company_a/*", "common/*"]
                }
            }
        }
    ]
}
```

For information about SageMaker AI condition keys, see [Condition Keys for Amazon SageMaker AI](../../../IAM/latest/UserGuide/list_amazonsagemaker.md#amazonsagemaker-policy-keys "../../../IAM/latest/UserGuide/list_amazonsagemaker.md#amazonsagemaker-policy-keys") in the _AWS Identity and Access Management User
Guide_.

- Create multi-model endpoints with more restrictive S3 prefixes.
  For more information about how SageMaker AI uses roles to manage access to endpoints and perform
  operations on your behalf, see [How to use SageMaker AI execution roles](sagemaker-roles.md "sagemaker-roles.md"). Your customers might also have certain data isolation requirements dictated by their own
  compliance requirements that can be satisfied using IAM identities.
