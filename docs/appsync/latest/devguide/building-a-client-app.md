# Building

a client application using Amplify client

You can connect to your AWS AppSync GraphQL API using any GraphQL client, but we strongly
recommend the Amplify v6 client. Amplify not only autogenerates strongly typed client SDKs
for your GraphQL API but also offers support for real-time data and enhanced GraphQL query
capabilities in client applications. For web applications, Amplify can produce a JavaScript
client. For those targeting cross-platform or mobile environments, Amplify caters to
Android, iOS, and React Native. To delve deeper into client code generation for these
platforms, consult the Amplify [documentation](https://docs.amplify.aws/cli/graphql/client-code-generation/ "https://docs.amplify.aws/cli/graphql/client-code-generation/").
Here's a guide to kickstart your journey with a JavaScript React application:

###### Note

You need to install and configure both [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm "https://docs.npmjs.com/downloading-and-installing-node-js-and-npm") and
the [Amazon CLI](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/") before getting started. If
you're using the Amplify v6 client, [follow this guide](https://docs.amplify.aws/react/build-a-backend/graphqlapi/connect-to-api/#configure-the-default-authorization-mode "https://docs.amplify.aws/react/build-a-backend/graphqlapi/connect-to-api/#configure-the-default-authorization-mode").

To get started:

1. On your local machine, navigate to your project's directory. Install the Amplify library using the
   command below:

```
npm install aws-amplify
```

2. Download your configuration file and place it in your project folder. Your
   configuration file will typically contain a `config` variable with some
   settings (endpoint, Region, authorization mode, etc.) defined. For example, it may look
   like this:

```
const config =  {
    API: {
        GraphQL: {
          endpoint: 'https://abcdefghijklmnopqrstuvwxyz.appsync-api.us-west-2.amazonaws.com/graphql',
          region: 'us-west-2',
          defaultAuthMode: 'apiKey',
          apiKey: ''
        }
    }
};

export default config;
```

3. In your code, import the Amplify Library and your configuration to set up
   Amplify:

```
import { Amplify } from 'aws-amplify';
import config from './aws-exports.js';

Amplify.configure(config);
```

Alternatively, use the snippet in your API configuration to set up Amplify
directly:

```
import { Amplify } from 'aws-amplify';

Amplify.configure({
  API: {
    GraphQL: {
      endpoint: 'https://abcdefghijklmnopqrstuvwxyz.appsync-api.us-west-2.amazonaws.com/graphql',
      region: 'us-west-2',
      defaultAuthMode: 'apiKey',
      apiKey: ''
    }
  }
});
```

4. Using the Amplify toolchain, you have the option to autogenerate operations based
   on your schema, which saves you the effort of manual scripting. In your application's
   root directory, use the following CLI command:

```
npx @aws-amplify/cli codegen add --apiId `<id goes here>` --region `<region goes here>`
```

This will download your API's schema and, by default, generate client helper code
into the `src/graphql` folder. After every API deployment, you can rerun the
following command to generate updated GraphQL statements and types:

```
npx @aws-amplify/cli codegen
```

5. You can now generate models for Android, Swift, Flutter, and JavaScript DataStore.
   Use the following command to download your schema:

```
aws appsync get-introspection-schema --api-id `<id goes here>` --region `<region goes here>` --format SDL schema.graphql
```

Then, run the following command from your application's root directory:

```
npx @aws-amplify/cli codegen models \
--model-schema schema.graphql \
--target [android|ios|flutter|javascript|typescript] \
--output-dir ./
```
