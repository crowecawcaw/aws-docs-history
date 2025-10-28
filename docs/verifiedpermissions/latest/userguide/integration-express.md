# Integrating Express with Amazon Verified Permissions

The Verified Permissions Express integration provides a middleware-based approach to implementing
authorization in your Express.js applications. With this integration, you can protect your API
endpoints using fine-grained authorization policies without modifying your existing route
handlers. The integration handles authorization checks automatically by intercepting requests,
evaluating them against your defined policies, and ensuring that only authorized users can
access protected resources.

This topic walks you through setting up the Express integration, from creating a policy
store to implementing and testing the authorization middleware. By following these steps, you
can add robust authorization controls to your Express application with minimal code
changes.

The following GitHub repos are referenced throughout this topic:

- [cedar-policy/authorization-for-expressjs](https://github.com/cedar-policy/authorization-for-expressjs "https://github.com/cedar-policy/authorization-for-expressjs") - The Cedar authorization middleware for Express.js
- [verifiedpermissions/authorization-clients-js](https://github.com/verifiedpermissions/authorization-clients-js "https://github.com/verifiedpermissions/authorization-clients-js") - The Verified Permissions authorization clients for JavaScript
- [verifiedpermissions/examples/express-petstore](https://github.com/verifiedpermissions/examples/tree/main/express-petstore "https://github.com/verifiedpermissions/examples/tree/main/express-petstore") - Example implementation using the Express.js middleware

## Prerequisites

Before you implement the Express integration, ensure you have:

- An [AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md") with access to Verified Permissions
- [Node.js](https://nodejs.org/ "https://nodejs.org/") and [npm](https://docs.npmjs.com/ "https://docs.npmjs.com/") installed
- An [Express.js](https://expressjs.com/ "https://expressjs.com/") application
- An OpenID Connect (OIDC) identity provider (such as [Amazon Cognito](../../../cognito/latest/developerguide/what-is-amazon-cognito.md "../../../cognito/latest/developerguide/what-is-amazon-cognito.md"))
- [AWS CLI](../../../cli/latest/userguide/getting-started-quickstart.md "../../../cli/latest/userguide/getting-started-quickstart.md") configured with appropriate permissions

## Setting up the integration

### Step 1: Create a policy store

Create a policy store using the AWS CLI:

```
aws verifiedpermissions create-policy-store --validation-settings "mode=STRICT"
```

###### Note

Save the policy store ID returned in the response for use in subsequent steps.

### Step 2: Install dependencies

Install the required packages in your Express application:

```
npm i --save @verifiedpermissions/authorization-clients-js
npm i --save @cedar-policy/authorization-for-expressjs
```

## Configuring authorization

### Step 1: Generate and upload Cedar schema

A schema defines the authorization model for an application, including the entities types in the application and the actions users are allowed to take. We recommend defining a [namespace](https://docs.cedarpolicy.com/overview/terminology.html#term-namespaces "https://docs.cedarpolicy.com/overview/terminology.html#term-namespaces") for your schema. In this example, we use `YourNamespace`. You attach your schema to your Verified Permissions policy stores, and when policies are added or modified, the service automatically validates the policies against the schema.

The `@cedar-policy/authorization-for-expressjs` package can analyze the [OpenAPI specifications](https://swagger.io/specification/ "https://swagger.io/specification/") of your application and generate a Cedar schema. Specifically, the paths object is required in your specification.

If you don't have an OpenAPI specification, you can follow the quick instructions of the [express-openapi-generator](https://github.com/nklisch/express-openapi-generator "https://github.com/nklisch/express-openapi-generator") package to generate an OpenAPI specification.

Generate a schema from your OpenAPI specification:

```
npx @cedar-policy/authorization-for-expressjs generate-schema --api-spec schemas/openapi.json --namespace `YourNamespace` --mapping-type SimpleRest
```

Next, format the Cedar schema for use with the AWS CLI. For more information about the specific format required, see [Amazon Verified Permissions policy store schema](schema.md "schema.md"). If you need help formatting the schema, there's a script called `prepare-cedar-schema.sh` in the [verifiedpermissions/examples](https://github.com/verifiedpermissions/examples/tree/main/express-petstore/start/scripts "https://github.com/verifiedpermissions/examples/tree/main/express-petstore/start/scripts") GitHub repo. The following is an example call to that script that outputs the Verified Permissions formatted schema in the `v2.cedarschema.forAVP.json` file.

```
./scripts/prepare-cedar-schema.sh v2.cedarschema.json v2.cedarschema.forAVP.json
```

Upload the formatted schema to your policy store, replacing `policy-store-id` with your policy store ID:

```
aws verifiedpermissions put-schema \
  --definition file://v2.cedarschema.forAVP.json \
  --policy-store-id `policy-store-id`
```

### Step 2: Create authorization

policies

If no policies are configured, Cedar denies all authorization requests. The Express framework integration helps bootstrap this process by generating example policies based on the previously generated schema.

When using this integration in your production applications, we recommend creating new policies using infrastructure as a code (IaaC) tools. For more information, see [Creating Amazon Verified Permissions resources with
AWS CloudFormation](cloudformation-verified-permissions.md "cloudformation-verified-permissions.md").

Generate sample Cedar policies:

```
npx @cedar-policy/authorization-for-expressjs generate-policies --schema v2.cedarschema.json
```

This will generate sample policies in the `/policies` directory. You can then customize these policies based on your use cases. For example:

```
// Defines permitted administrator user group actions
permit (
    principal in YourNamespace::UserGroup::"<userPoolId>|administrator",
    action,
    resource
);

// Defines permitted employee user group actions
permit (
    principal in YourNamespace::UserGroup::"<userPoolId>|employee",
    action in
        [YourNamespace::Action::"GET /resources",
         YourNamespace::Action::"POST /resources",
         YourNamespace::Action::"GET /resources/{resourceId}",
         YourNamespace::Action::"PUT /resources/{resourceId}"],
    resource
);
```

Format the policies for use with the AWS CLI. Fore more information about the required format, see [create-policy](../../../cli/latest/reference/verifiedpermissions/create-policy.md "../../../cli/latest/reference/verifiedpermissions/create-policy.md") in the _AWS CLI reference_. If you need help formatting the policies, there's a script called `convert_cedar_policies.sh` in the [verifiedpermissions/examples](https://github.com/verifiedpermissions/examples/tree/main/express-petstore/start/scripts "https://github.com/verifiedpermissions/examples/tree/main/express-petstore/start/scripts") GitHub repo. The following is a call to that script:

```
./scripts/convert_cedar_policies.sh
```

Upload the formatted policies to Verified Permissions, replacing `policy_1.json` with the path and name of your policy file and `policy-store-id` with your policy store ID:

```
aws verifiedpermissions create-policy \
  --definition file://`policies/json/policy_1.json` \
  --policy-store-id `policy-store-id`
```

### Step 3: Connect an identity provider

By default, the Verified Permissions authorizer middleware reads a JSON Web Token (JWT) provided within the authorization header of the API request to get user information. Verified Permissions can validate the token in addition to performing authorization policy evaluation.

Create an identity source configuration file named
`identity-source-configuration.txt` that looks like the following with
your `userPoolArn` and `clientId`:

```
{
    "cognitoUserPoolConfiguration": {
        "userPoolArn": "`arn:aws:cognito-idp:region:account:userpool/pool-id`",
        "clientIds": ["`client-id`"],
        "groupConfiguration": {
            "groupEntityType": "YourNamespace::UserGroup"
        }
    }
}
```

Create the identity source by running the following AWS CLI command, replacing `policy-store-id` with your policy store ID:

```
aws verifiedpermissions create-identity-source \
  --configuration file://identity-source-configuration.txt \
  --policy-store-id `policy-store-id` \
  --principal-entity-type YourNamespace::User
```

## Implementing the authorization middleware

Update your Express application to include the authorization middleware. In this example we're using identity tokens, but you can also use access tokens. For more information, see [authorization-for-expressjs](https://github.com/cedar-policy/authorization-for-expressjs "https://github.com/cedar-policy/authorization-for-expressjs") on GitHub.

```
const { ExpressAuthorizationMiddleware } = require('@cedar-policy/authorization-for-expressjs');

const { AVPAuthorizationEngine } = require('@verifiedpermissions/authorization-clients');

const avpAuthorizationEngine = new AVPAuthorizationEngine({
    policyStoreId: '`policy-store-id`',
    callType: 'identityToken'
});

const expressAuthorization = new ExpressAuthorizationMiddleware({
    schema: {
        type: 'jsonString',
        schema: fs.readFileSync(path.join(__dirname, '../v4.cedarschema.json'), 'utf8'),
    },
    authorizationEngine: avpAuthorizationEngine,
    principalConfiguration: { type: 'identityToken' },
    skippedEndpoints: [],
    logger: {
        debug: (s) => console.log(s),
        log: (s) => console.log(s),
    }
});

// Add the middleware to your Express application
app.use(expressAuthorization.middleware);
```

## Testing the integration

You can test your authorization implementation by making requests to your API endpoints with different user tokens. The authorization middleware will automatically evaluate each request against your defined policies.

For example, if you've set up different user groups with different permissions:

- Administrators: Full access to all resources and management functions
- Employees: Can view, create, and update resources
- Customers: Can only view resources

You can validate that the permissions policies are working as expected by signing in with different users and attempting various operations. In the terminal for the Express application, you can see log output that provides additional details about the authorization decisions.

## Troubleshooting

If you have authorization failures, try the following:

- Verify your policy store ID is correct
- Ensure your identity source is properly configured
- Check that your policies are correctly formatted
- Validate that your JWT tokens are valid

## Next steps

After implementing the basic integration, consider:

- Implementing custom mappers for specific authorization scenarios
- Setting up monitoring and logging for authorization decisions
- Creating additional policies for different user roles
