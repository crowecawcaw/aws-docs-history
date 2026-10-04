

Amazon WorkSpaces Secure Browser will no longer be open to new customers starting October 29, 2026. If you would like to use Amazon WorkSpaces Secure Browser, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon WorkSpaces Secure Browser availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html). 

# Protecting data in transit with FIPS endpoints and Amazon WorkSpaces Secure Browser
<a name="fips-endpoints"></a>

By default, when you communicate with the WorkSpaces Secure Browser service as an administrator using the console, the AWS Command Line Interface (AWS CLI), or an AWS SDK, or during a user’s session, all data in transit is encrypted using TLS 1.2.

If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. When you use a FIPS endpoint, all data in transit is encrypted using cryptographic standards that comply with Federal Information Processing Standard (FIPS) 140-3. For information about FIPS endpoints, including a list of WorkSpaces Secure Browser endpoints, see [https://aws.amazon.com/compliance/fips](https://aws.amazon.com/compliance/fips).

After a portal is created with FIPS endpoints, all user sessions and administrative changes are automatically made using FIPS 140-3 endpoints. You can use the `AWS_USE_FIPS_ENDPOINT=true` environment variable to locate FIPS endpoints and send requests with the SDK. The following is an example.

```
$ export AWS_USE_FIPS_ENDPOINT=true
$ aws workspaces-web list-portal
```

You can also use the `—endpoint-url` option to send requests directly to FIPS endpoints. The following is an example calling list portals in the US-West-2 (Oregon) Region:

```
$ aws workspaces-web list-portal --endpoint-url https://workspaces-web-fips.us-west-2.amazonaws.com
```