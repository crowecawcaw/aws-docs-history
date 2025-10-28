# Using open source adapters for any SSR

framework

You can use any SSR framework build adapter that has been created for integration with
Amplify Hosting. Each framework that offers an adapter determines how the adapter is
configured and connected to their build process. Typically, you will install the adapter as
an npm development dependency.

After you create an app with a framework, use the framework's documentation to learn how
to install the Amplify Hosting adapter and configure it in your application's
configuration file.

Next, create an `amplify.yml` file in your project's root directory.
In the `amplify.yml` file, set the `baseDirectory` to your
application's build output directory. The framework runs the adapter during the build
process to transform the output into the Amplify Hosting deployment bundle.

The name of the build output directory can be anything, but the
`.amplify-hosting` filename has significance. Amplify first looks for
a directory defined as the `baseDirectory`. If it exists, Amplify looks for the
build output there. If the directory doesn't exist, Amplify looks for the build output
inside `.amplify-hosting`, even if it has not been defined by the
customer.

The following is an example of the build settings for an app. The
`baseDirectory` is set to `.amplify-hosting` to indicate that the
build output is in the `.amplify-hosting` folder. As long as the contents of the
`.amplify-hosting` folder match the Amplify Hosting deployment specification,
the app will deploy successfully.

```
version: 1
frontend:
  preBuild:
    commands:
      - npm install
  build:
    commands:
      - npm run build
  artifacts:
    baseDirectory: .amplify-hosting
```

After your app is configured to use a framework adapter, you can deploy it to Amplify
Hosting. For detailed instructions, see [Deploying an SSR app to Amplify](server-side-rendering-amplify.md#deploy-ssr-framework-app "server-side-rendering-amplify.md#deploy-ssr-framework-app")
