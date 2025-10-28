# Amazon OpenSearch Service API permissions reference

When you set up [access control](ac.md "ac.md"), you write permission
policies that you can attach to an IAM identity (identity-based policies). For
detailed reference information, see the following topics in the
_Service Authorization Reference_:

- [Actions, resources, and condition keys for OpenSearch Service](../../../service-authorization/latest/reference/list_amazonopensearchservice.md "../../../service-authorization/latest/reference/list_amazonopensearchservice.md").
- [Actions, resources, and condition keys for OpenSearch Ingestion](../../../service-authorization/latest/reference/list_opensearchingestionservice.md "../../../service-authorization/latest/reference/list_opensearchingestionservice.md").
  This reference contains information about which API operations can be used in an IAM
  policy. It also includes the AWS resource for which you can grant the permissions, and
  condition keys that you can include for fine-grained access control.

You specify the actions in the policy's `Action` field, the resource value
in the policy's `Resource` field, and conditions in the policy's
`Condition` field. To specify an action for OpenSearch Service, use the
`es:` prefix followed by the API operation name (for example,
`es:CreateDomain`). To specify an action for OpenSearch Ingestion, use the
`osis:` prefix followed by the API operation (for example,
`osis:CreatePipeline`).
