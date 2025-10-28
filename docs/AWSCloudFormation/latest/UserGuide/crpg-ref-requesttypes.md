# Custom resource request types

The request type is sent in the `RequestType` field in the [request object](crpg-ref-requests.md "crpg-ref-requests.md") sent by AWS CloudFormation when the template developer
creates, updates, or deletes a stack that contains a custom resource.

Each request type has a particular set of fields that are sent with the request, including
an Amazon S3 URL for the response by the custom resource provider. The provider must respond to the S3 bucket with
either a `SUCCESS` or `FAILED` result before the timeout period ends. If
no response is received before the timeout period ends, the request will be considered
unsuccessful and the stack operation fails. Each result also has a particular set of fields
expected by CloudFormation.

This section provides information about the request and response fields, with examples, for
each request type.

###### Topics

- [Create request for CloudFormation custom
  resources](crpg-ref-requesttypes-create.md "crpg-ref-requesttypes-create.md")
- [Delete request for CloudFormation custom
  resources](crpg-ref-requesttypes-delete.md "crpg-ref-requesttypes-delete.md")
- [Update request for CloudFormation custom
  resources](crpg-ref-requesttypes-update.md "crpg-ref-requesttypes-update.md")
