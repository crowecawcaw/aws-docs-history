# CloudWatch pipelines configuration for Box

Collects audit and activity log data from Box using OAuth 2.0 Client Credentials authentication through the Box Events API.

Configure the Box source with the following parameters:

```
source:
  box:
    enterprise_id: "123456789"
    authentication:
      oauth2:
        client_id: "${{aws_secrets:<secret-name>:client_id}}"
        client_secret: "${{aws_secrets:<secret-name>:client_secret}}"
```

###### Parameters

`enterprise_id` (required)

The Box Enterprise ID for your organization. Found in the Box Admin Console under Account & Billing.

`authentication.oauth2.client_id` (required)

The Box Custom App Client ID, stored in AWS Secrets Manager.

`authentication.oauth2.client_secret` (required)

The Box Custom App Client Secret, stored in AWS Secrets Manager.
