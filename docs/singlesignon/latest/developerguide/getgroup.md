# GetGroup

Information about an existing group can be retrieved by making a request to
the `/Groups` endpoint with the group ID.

## Not supported

The IAM Identity Center SCIM implementation does not support the following aspects of this API
operation.

- `GetGroup` and `ListGroups` return an empty member
  list. To see group info for a certain member, call `ListGroups`
  with a member filter. For more information, see [ListGroups](listgroups.md "listgroups.md").

## Constraints

The IAM Identity Center SCIM implementation has the following constraints for this API
operation.

- None

## Errors

The following IAM Identity Center SCIM implementation errors are common for this API
operation.

| Error                       | Condition                                                                                                                         | HTTP Status Code |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ValidationException`       | Request cannot be parsed, is syntactically incorrect, or violates schema. This error also occurs if the operation is unsupported. | 400              |
| `UnauthorizedException`     | Authorization header is invalid or missing. This error also occurs if the tenant ID is incorrect.                                 | 401              |
| `AccessDeniedException`     | Operation is not permitted based on the supplied authorization.                                                                   | 403              |
| `ResourceNotFoundException` | Specified group does not exist.                                                                                                   | 404              |
| `ThrottlingException`       | Too many requests exceeded the limits.                                                                                            | 429              |
| `InternalServerException`   | Service failed to process the request.                                                                                            | 500              | ## Examples Following are example requests and responses for this API operation. ###### Example Request `GET https://scim.us-east-1.amazonaws.com/{tenant_id}/scim/v2/Groups/9067729b3d-a2cfc8a5-f4ab-4443-9d7d-b32a9013c554 User-Agent: Mozilla/5.0 Authorization: Bearer <bearer_token>` ###### Example Response `HTTP/1.1 200 Date: Mon, 06 Apr 2020 17:16:53 GMT Content-Type: application/json x-amzn-RequestId: abbf9e53-9ecc-46d2-8efe-104a66ff128f { "id": "9067729b3d-a2cfc8a5-f4ab-4443-9d7d-b32a9013c554", "meta": { "resourceType": "Group", "created": "2020-04-06T16:48:19Z", "lastModified": "2020-04-06T16:48:19Z" }, "schemas": [ "urn:ietf:params:scim:schemas:core:2.0:Group" ], "displayName": "Group Bar" }` |
