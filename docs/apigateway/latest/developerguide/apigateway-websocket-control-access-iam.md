# Control access to WebSocket APIs with IAM authorization

IAM authorization in WebSocket APIs is similar to that for [REST
APIs](api-gateway-control-access-using-iam-policies-to-invoke-api.md "api-gateway-control-access-using-iam-policies-to-invoke-api.md"), with the following exceptions:

- The `execute-api` action supports `ManageConnections` in
  addition to existing actions (`Invoke`,
  `InvalidateCache`). `ManageConnections` controls access to
  the @connections API.
- WebSocket routes use a different ARN format:

```
arn:aws:execute-api:`region`:`account-id`:`api-id`/`stage-name`/`route-key`
```

- The `@connections` API uses the same ARN format as REST
  APIs:

```
arn:aws:execute-api:`region`:`account-id`:`api-id`/`stage-name`/POST/@connections
```

###### Important

When you use IAM
authorization, you must sign requests with [Signature Version 4
(SigV4)](../../../IAM/latest/UserGuide/create-signed-request.md "../../../IAM/latest/UserGuide/create-signed-request.md").

For example, you could set up the following policy to the client. This example allows
everyone to send a message (`Invoke`) for all routes except for a secret
route in the `prod` stage and prevents everyone from sending a message back
to connected clients (`ManageConnections`) for all stages.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "execute-api:Invoke"
 ],
 "Resource": [
 "arn:aws:execute-api:`us-east-1`:`111122223333`:`api-id`/prod/*"
 ]
 },
 {
 "Effect": "Deny",
 "Action": [
 "execute-api:Invoke"
 ],
 "Resource": [
 "arn:aws:execute-api:`us-east-1`:`111122223333`:`api-id`/prod/secret"
 ]
 },
 {
 "Effect": "Deny",
 "Action": [
 "execute-api:ManageConnections"
 ],
 "Resource": [
 "arn:aws:execute-api:`us-east-1`:`111122223333`:`api-id`/*"
 ]
 }
 ]
}`

```
