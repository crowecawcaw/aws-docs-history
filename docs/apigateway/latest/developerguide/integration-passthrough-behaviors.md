# Method request behavior for payloads without mapping

templates for REST APIs in API Gateway

If your method request has a payload and you don't have a mapping template defined for the
`Content-Type` header, you can choose to pass the client-supplied request payload through the
integration request to the backend without transformation. The process is known as integration passthrough.

The actual passthrough behavior of an incoming request is determined by this setting. There are three
options:

**When no template matches the request Content-Type header**
Choose this option if you want the method request body to pass through the integration request to the backend
without transformation when the method request content type does not match any content types associated with
the mapping templates.

When calling the API Gateway API, you choose this option by setting `WHEN_NO_MATCH` as the
`passthroughBehavior` property value on the [Integration](../api/API_Integration.md "../api/API_Integration.md").

**When there are no templates defined (recommended)**

Choose this option if you want the method request body to pass through the integration request to the
backend without transformation when no mapping template is defined in the integration request. If a template
is defined when this option is selected, the method request with a payload and content type that doesn't
match any defined mapping template will be rejected with an HTTP 415 Unsupported Media Type response.

When calling the API Gateway API, you choose this option by setting `WHEN_NO_TEMPLATES` as the
`passthroughBehavior` property value on the [Integration](../api/API_Integration.md "../api/API_Integration.md").

**Never**

Choose this option if you do not want the method request body to pass through the integration request to the backend without transformation when no
mapping template is defined in the integration request. If a template is defined when this option is
selected, the method request of an unmapped content type will be rejected with an HTTP 415 Unsupported
Media Type response.

When calling the API Gateway API, you choose this option by setting `NEVER` as the
`passthroughBehavior` property value on the [Integration](../api/API_Integration.md "../api/API_Integration.md").

The following examples show the possible passthrough behaviors.

Example 1: One mapping template is defined in the integration request for the
`application/json` content type.

| Content-type                                       | Passthrough option  | Behavior                                                                       |
| -------------------------------------------------- | ------------------- | ------------------------------------------------------------------------------ |
| None<br>API Gateway defaults to `application/json` | `WHEN_NO_MATCH`     | The request payload is transformed using the template.                         |
| None<br>API Gateway defaults to `application/json` | `WHEN_NO_TEMPLATES` | The request payload is transformed using the template.                         |
| None<br>API Gateway defaults to `application/json` | `NEVER`             | The request payload is transformed using the template.                         |
| `application/json`                                 | `WHEN_NO_MATCH`     | The request payload is transformed using the template.                         |
| `application/json`                                 | `WHEN_NO_TEMPLATES` | The request payload is transformed using the template.                         |
| `application/json`                                 | `NEVER`             | The request payload is transformed using the template.                         |
| `application/xml`                                  | `WHEN_NO_MATCH`     | The request payload is not transformed and is sent to the backend<br>as-is.    |
| `application/xml`                                  | `WHEN_NO_TEMPLATES` | The request is rejected with an HTTP `415 Unsupported Media<br>Type` response. |
| `application/xml`                                  | `NEVER`             | The request is rejected with an HTTP `415 Unsupported Media<br>Type` response. |

Example 2: One mapping template is defined in the integration request for the
`application/xml` content type.

| Content-type                                       | Passthrough option  | Behavior                                                                       |
| -------------------------------------------------- | ------------------- | ------------------------------------------------------------------------------ |
| None<br>API Gateway defaults to `application/json` | `WHEN_NO_MATCH`     | The request payload is not transformed and is sent to the backend<br>as-is.    |
| None<br>API Gateway defaults to `application/json` | `WHEN_NO_TEMPLATES` | The request is rejected with an HTTP `415 Unsupported Media<br>Type` response. |
| None<br>API Gateway defaults to `application/json` | `NEVER`             | The request is rejected with an HTTP `415 Unsupported Media<br>Type` response. |
| `application/json`                                 | `WHEN_NO_MATCH`     | The request payload is not transformed and is sent to the backend<br>as-is.    |
| `application/json`                                 | `WHEN_NO_TEMPLATES` | The request is rejected with an HTTP `415 Unsupported Media<br>Type` response. |
| `application/json`                                 | `NEVER`             | The request is rejected with an HTTP `415 Unsupported Media<br>Type` response. |
| `application/xml`                                  | `WHEN_NO_MATCH`     | The request payload is transformed using the template.                         |
| `application/xml`                                  | `WHEN_NO_TEMPLATES` | The request payload is transformed using the template.                         |
| `application/xml`                                  | `NEVER`             | The request payload is transformed using the template.                         |

Example 3: No mapping templates are defined in the integration request.

| Content-type                                       | Passthrough option  | Behavior                                                                       |
| -------------------------------------------------- | ------------------- | ------------------------------------------------------------------------------ |
| None<br>API Gateway defaults to `application/json` | `WHEN_NO_MATCH`     | The request payload is not transformed and is sent to the backend<br>as-is.    |
| None<br>API Gateway defaults to `application/json` | `WHEN_NO_TEMPLATES` | The request payload is not transformed and is sent to the backend<br>as-is.    |
| None<br>API Gateway defaults to `application/json` | `NEVER`             | The request is rejected with an HTTP `415 Unsupported Media<br>Type` response. |
| `application/json`                                 | `WHEN_NO_MATCH`     | The request payload is not transformed and is sent to the backend<br>as-is.    |
| `application/json`                                 | `WHEN_NO_TEMPLATES` | The request payload is not transformed and is sent to the backend<br>as-is.    |
| `application/json`                                 | `NEVER`             | The request is rejected with an HTTP `415 Unsupported Media<br>Type` response. |
| `application/xml`                                  | `WHEN_NO_MATCH`     | The request payload is not transformed and is sent to the backend<br>as-is.    |
| `application/xml`                                  | `WHEN_NO_TEMPLATES` | The request payload is not transformed and is sent to the backend<br>as-is.    |
| `application/xml`                                  | `NEVER`             | The request is rejected with an HTTP `415 Unsupported Media<br>Type` response. |
