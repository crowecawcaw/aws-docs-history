# Helper methods for CloudFront SaaS Manager properties

Use the following helper functions for CloudFront SaaS Manager to retrieve values for your
multi-tenant distributions in the function that you create. To use examples on this page, you must
first create a CloudFront function by using JavaScript runtime 2.0. For more information,
[JavaScript runtime 2.0 features for CloudFront Functions](functions-javascript-runtime-20.md "functions-javascript-runtime-20.md").

###### Topics

- [Connection groups](#connection-groups-helper-function "#connection-groups-helper-function")
- [Distribution tenants](#distribution-tenants-helper-functions "#distribution-tenants-helper-functions")

## Connection groups

The connection group that is associated with your distribution tenants has a domain
name.

To get this value, use the `endpoint` field of the `context`
subobject of the event object.

**Request**

```
const value = event.context.endpoint;
```

**Response**

The response is a `string` that contains the connection group's domain
name, such as d111111abcdef8.cloudfront.net. The `endpoint` field only appears
when your function is invoked for a multi-tenant distribution with an associated connection group.
For more information, see [Context object](functions-event-structure.md#functions-event-structure-context "functions-event-structure.md#functions-event-structure-context").

## Distribution tenants

CloudFront Functions has a module that provides access to specific distribution tenant
values.

To use this module, include the following statement in the first line of your
function code:

```
import cf from 'cloudfront';
```

You can use the following examples only in the `handler` function,
either directly or through any nested-call function.

### `distributionTenant.id` field

Use this field to get the value of distribution tenant ID.

**Request**

```
const value = cf.distributionTenant.id;
```

**Response**

The response is a `string` that contains the distribution tenant ID, such as
`dt_1a2b3c4d5e6f7`.

**Error handling**

If your function is invoked for a standard distribution, specifying the
`distributionTenant.id` field will return the
`distributionTenant module is not available` type error. To
handle this use case, you can add a `try` and `catch`
block to your code.

### `distributionTenant.parameters.get()` method

Use this method to return the value for the distribution tenant parameter names that you
specified.

```
distributionTenant.parameters.get("key");
```

`key`: The distribution tenant parameter name that you want to fetch the value
for.

**Request**

```
const value = distributionTenant.parameters.get("key");
```

**Response**

The response is a `string` that contains the value for the distribution tenant
parameter. For example, if your key name is `TenantPath`, then the
value for this parameter might be `tenant1`.

**Error handling**

You might receive the following errors:

- If your function is invoked for a standard distribution, the
  `distributionTenant.parameters.get()` method will return
  the `distributionTenant module is not available` type error.
- The `DistributionTenantParameterKeyNotFound` error is
  returned when the distribution tenant parameter that you specified doesn't exist.

To manage these use cases, you can add a `try` and
`catch` block to your code.
