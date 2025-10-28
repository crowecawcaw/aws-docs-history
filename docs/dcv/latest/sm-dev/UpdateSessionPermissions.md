# UpdateSessionPermissions

Updates the user permissions for a specific Amazon DCV session.

###### Topics

- [Request parameters](#request "#request")
- [Response parameters](#response "#response")
- [Example](#example "#example")

## Request parameters

**`SessionId`**

The ID of the session for which to change the permissions.

Type: String

Required: Yes

**`Owner`**

The owner of the session for which to change the permissions.

Type: String

Required: Yes

**`PermissionFile`**

The Base64-encoded content of the permissions file to use. For more information, see
[Configuring Amazon DCV Authorization](../adminguide/security-authorization.md "../adminguide/security-authorization.md") in the
_Amazon DCV Administrator Guide_.

Type: String

Required: Yes

## Response parameters

**`SessionId`**

The ID of the session.

## Example

Python

###### Request

The following example sets new permissions for a session with a session ID of
`SessionId1897`.

```
from swagger_client.models.update_session_permissions_request_data import UpdateSessionPermissionsRequestData

def get_session_permissions_api():
    api_instance = swagger_client.SessionPermissionsApi(swagger_client.ApiClient(get_client_configuration()))
    set_request_headers(api_instance.api_client)
    return api_instancedef update_session_permissions(session_permissions_to_update):
    update_session_permissions_request = list()
    for session_id, owner, permissions_base64_encoded in session_permissions_to_update:
        a_request = UpdateSessionPermissionsRequestData(
            session_id=session_id, owner=owner, permissions_file=permissions_base64_encoded)
        update_session_permissions_request.append(a_request)
    print('Update Session Permissions Request:', update_session_permissions_request)
    api_instance = get_session_permissions_api()
    api_response = api_instance.update_session_permissions(body=update_session_permissions_request)
    print('Update Session Permissions Response:', api_response)

def main():
    update_session_permissions([('SessionId1897', 'an owner 1890', 'file_base64_encoded')])
```

###### Response

The following is the sample output.

```
{
   'request_id': 'd68ebf66-4022-42b5-ba65-99f89b18c341',
    'successful_list': [
        {'
            session_id': 'SessionId1897'
        }
    ],
    'unsuccessful_list': []
}
```
