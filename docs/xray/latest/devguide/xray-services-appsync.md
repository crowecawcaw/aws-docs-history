# AWS AppSync and AWS X-Ray

You can enable and trace requests for AWS AppSync. For more information, see [Tracing with AWS X-Ray](../../../appsync/latest/devguide/x-ray-tracing.md "../../../appsync/latest/devguide/x-ray-tracing.md") for instructions.

When X-Ray tracing is enabled for an AWS AppSync API, an AWS Identity and Access Management [service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md")
is automatically created in your account with the appropriate permissions. This allows AWS AppSync to send
traces to X-Ray in a secure way.
