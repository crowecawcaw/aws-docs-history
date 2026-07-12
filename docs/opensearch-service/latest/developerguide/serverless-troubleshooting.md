# Troubleshooting Amazon OpenSearch Serverless

Most access problems on an Amazon OpenSearch Serverless collection endpoint appear as one of two client
errors. A `401 Unauthorized` response means the collection's network policy
doesn't permit the request source. A `403 Forbidden` response means the request
reached the collection, but either the request signature is invalid or no data access
policy permits the operation.

###### Topics

- [HTTP 401 errors: network policy](#serverless-troubleshooting-401 "#serverless-troubleshooting-401")
- [HTTP 403 errors: signing or data access](#serverless-troubleshooting-403 "#serverless-troubleshooting-403")

## HTTP 401 errors: network policy

A `401` response means the collection's network policy doesn't allow the
source of the request. OpenSearch Serverless blocks the request before it reaches the collection and
returns the response header
`x-aoss-response-hint: X01:network-policy-deny`.

Confirm that a network policy grants access from the source your client uses. For
private access, verify that the VPC endpoint ID the client connects through is listed in
the policy. For more information about network policies, see [Network access for Amazon OpenSearch Serverless](serverless-network.md "serverless-network.md").

## HTTP 403 errors: signing or data access

A `403 Forbidden` response means the request reached the collection but a
policy denied it. Confirm the following common causes of `403`
responses:

Signature Version 4 (SigV4) signing

The request signature is missing or invalid. You must sign every request
to a collection endpoint with SigV4. Signing problems are the most common
cause of `403` errors from SDK clients, custom HTTP clients, and
ingestion pipelines. Check the following items for common signing
mistakes:

- Verify that the credential is scoped to the `aoss`
  service, not `es`. Signing for `es` is a
  frequent cause of `403` errors when you reuse OpenSearch Service
  client code.
- Verify that the request includes the
  `x-amz-content-sha256` header with the payload hash. Also
  verify that this header is part of the signed headers. If you omit
  this header, OpenSearch Serverless can't validate the signature.
- Verify that the credentials and signature aren't expired, and that
  temporary credentials include the session token.
- Verify that the client strips the default port (`:443`)
  from the `Host` and `:authority` headers.
  SigV4 omits `:443` when it computes the signature, so
  keeping it causes a mismatch.

For more information, see [Signing AWS API
requests](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") in the _AWS General Reference_.
AWS SDKs handle SigV4 signing for you when you configure them with the
`aoss` service and the collection's Region.

Data access policy

No data access policy grants your principal permission to perform the
attempted operation.
Confirm that a policy grants the required permission and targets the correct
collection, index, or document resource. Collection-level access doesn't
automatically include document read or write access. For more information
about supported operations and permissions, see [Supported policy permissions](serverless-data-access.md#serverless-data-supported-permissions "serverless-data-access.md#serverless-data-supported-permissions"). A `403`
from a data access policy denial includes the response header
`x-aoss-response-hint: X01:gw-helper-deny`.

IAM permissions

A data access policy entry alone doesn't grant access. You must also hold
the applicable IAM permission:

- Use `aoss:APIAccessAll` for data plane API access to
  collection data.
- Use `aoss:DashboardsAccessAll` for OpenSearch Dashboards
  access.

Without the required permission, OpenSearch Serverless returns a `403`
response. For examples of identity-based policies for data plane access,
see [Using OpenSearch API operations](security-iam-serverless.md#security_iam_id-based-policy-examples-data-plane "security-iam-serverless.md#security_iam_id-based-policy-examples-data-plane").
