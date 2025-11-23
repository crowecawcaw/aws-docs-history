# Stages for HTTP APIs in API Gateway

An API stage is a logical reference to a lifecycle state of your API (for example,
`dev`, `prod`, `beta`, or `v2`). API stages
are identified by their API ID and stage name, and they're included in the URL you use to
invoke the API. Each stage is a named reference to a deployment of the API and is made
available for client applications to call.

You can create a `$default` stage that is served from the base of your API's
URL—for example, `https://{api_id}.execute-api.{region}.amazonaws.com/`.
You use this URL to invoke an API stage.

A deployment is a snapshot of your API configuration. After you deploy an API to a stage,
it’s available for clients to invoke. You must deploy an API for changes to take effect. If
you enable automatic deployments, changes to an API are automatically released for
you.
