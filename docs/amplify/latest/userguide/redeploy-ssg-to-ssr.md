# Adding SSR functionality to a static Next.js

app

You can add SSR functionality to an existing static (SSG) Next.js app deployed with
Amplify. Before you start the process of converting your SSG app to SSR, update the app to
use Next.js version 12 or later and add SSR functionality. Then you will need to perform the
following steps.

1. Use the AWS Command Line Interface to change the app's platform type.
2. Add a service role to the app.
3. Update the output directory in the app's build settings.
4. Update the app's `package.json` file to indicate that the app uses
   SSR.

## Updating the platform

There are three valid values for platform type. An SSG app is set to platform type
`WEB`. An SSR app using Next.js version 11 is set to platform type
`WEB_DYNAMIC`. For apps deployed to Next.js 12 or later using SSR managed by
Amplify Hosting compute, the platform type is set to `WEB_COMPUTE`.

When you deployed your app as an SSG app, Amplify set the platform type to
`WEB`. Use the AWS CLI to change the platform for your app to
`WEB_COMPUTE`. Open a terminal window and enter the following command,
updating the text in red with your unique app id and Region.

```
aws amplify update-app --app-id `abcd1234` --platform WEB_COMPUTE --region `us-west-2`
```

## Adding a service role

A service role is the AWS Identity and Access Management (IAM) role that Amplify assumes when calling other
services on your behalf. Follow these steps to add a service role to an SSG app that's
already deployed with Amplify.

###### To add a service role

1. Sign in to the AWS Management Console and open the [Amplify
   console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. If you haven't already created a service role in your Amplify account, see [Adding a service role](amplify-service-role.md "amplify-service-role.md") to
   complete this prerequisite step.
3. Choose the static Next.js app that you want to add a service role to.
4. In the navigation pane, choose **App settings**,
   **General**.
5. On the **App details** page, choose
   **Edit**
6. For **Service role**, choose the name of an existing service role
   or the name of the service role that you created in step 2.
7. Choose **Save**.

## Updating the build settings

Before you redeploy your app with SSR functionality, you must update the build
settings for the app to set the output directory to `.next`. You can edit the
build settings in the Amplify console or in an `amplify.yml` file stored in
your repo. For more information see, [Configuring the build settings for an Amplify application](build-settings.md "build-settings.md").

The following is an example of the build settings for an app where
`baseDirectory` is set to `.next`.

```
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - npm ci
    build:
      commands:
        - npm run build
  artifacts:
    baseDirectory: .next
    files:
      - '**/*'
  cache:
    paths:
      - node_modules/**/*

```

## Updating the package.json file

After you add a service role and update the build settings, update the app's
`package.json` file. As in the following example, set the build script to
`"next build"` to indicate that the Next.js app supports both SSG and SSR
pages.

```
"scripts": {
  "dev": "next dev",
  "build": "next build",
  "start": "next start"
},
```

Amplify detects the change to the `package.json` file in your repo and
redeploys the app with SSR functionality.
