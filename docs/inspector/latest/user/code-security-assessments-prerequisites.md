# Prerequisites for Code Security

Before you can begin using Code Security, you must activate Code Security and decide how to encrypt your data.
This can be information like integration credentials, code, or any other information related to your integrations, code repositories, and projects.
By default, your data is encrypted with an [AWS owned key](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk").
This means the key is created, owned, and managed by the service.
If you want to own and manage the key used to encrypt your data, you can create a [customer managed KMS key](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk").
