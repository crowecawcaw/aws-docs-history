# Deploying a Next.js SSR application to Amplify

By default, Amplify deploys new SSR apps using Amplify Hosting's compute service
with support for Next.js versions 12 through 15. Amplify Hosting compute fully manages the
resources required to deploy an SSR app. SSR apps in your Amplify account that you
deployed before November 17, 2022 are using the Classic (Next.js 11 only) SSR provider.

We strongly recommend that you migrate apps using Classic (Next.js 11 only) SSR to the
Amplify Hosting compute SSR provider. Amplify doesn't perform automatic migrations for
you. You must manually migrate your app and then initiate a new build to complete the
update. For instructions, see [Migrating a Next.js 11 SSR app to Amplify Hosting compute](update-app-nextjs-version.md "update-app-nextjs-version.md").

Use the following instructions to deploy a new Next.js SSR app.

###### To deploy an SSR app to Amplify using the Amplify Hosting compute SSR provider

1. Sign in to the AWS Management Console and open the [Amplify
   console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. On the **All apps** page, choose **Create new
   app**.
3. On the **Start building with Amplify** page, choose your Git
   repository provider, then choose **Next**.
4. On the **Add repository branch** page, do the following:
   1. In the **Recently updated repositories** list, select the name
      of the repository to connect.
   2. In the **Branch** list, select the name of the repository
      branch to connect.
   3. Choose **Next**.

5. The app requires an IAM service role that Amplify assumes when calling other
   services on your behalf. You can either allow Amplify Hosting compute to automatically
   create a service role for you or you can specify a role that you have created.
   - To allow Amplify to automatically create a role and attach it to your
     app:
     1. Choose **Create and use a new service role**.

   - To attach a service role that you previously created:
     1. Choose **Use an existing service role**.
     2. Select the role to use from the list.

6. Choose **Next**.
7. On the **Review** page, choose **Save and
   deploy**.

## Package.json file settings

When you deploy a Next.js app, Amplify inspects the app's build script in the
`package.json` file to determine the application type.

The following is an example of the build script for a Next.js app. The build script
`"next build"` indicates that the app supports both SSG and SSR pages. This
build script is also used for Next.js 14 or later SSG only apps.

```
"scripts": {
  "dev": "next dev",
  "build": "next build",
  "start": "next start"
},
```

The following is an example of the build script for a Next.js 13 or earlier SSG app.
The build script `"next build && next export"` indicates that the app
supports only SSG pages.

```
"scripts": {
  "dev": "next dev",
  "build": "next build && next export",
  "start": "next start"
},
```

## Amplify build settings for a Next.js SSR application

After inspecting your app's `package.json` file, Amplify checks the build
settings for the app. You can save build settings in the Amplify console or in an
`amplify.yml` file in the root of your repository. For more information, see
[Configuring the build settings for an Amplify application](build-settings.md "build-settings.md").

If Amplify detects that you are deploying a Next.js SSR app, and no
`amplify.yml` file is present, it generates a buildspec for the app and sets
`baseDirectory` to `.next`. If you are deploying an app where an
`amplify.yml` file is present, the build settings in the file override any
build settings in the console. Therefore, you must manually set the
`baseDirectory` to `.next` in the file.

The following is an example of the build settings for an app where
`baseDirectory` is set to `.next`. This indicates that the build
artifacts are for a Next.js app that supports SSG and SSR pages.

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

## Amplify build settings for a Next.js 13 or earlier SSG application

If Amplify detects that you are deploying a Next.js 13 or earlier SSG app, it
generates a build specification for the app and sets `baseDirectory` to
`out`. If you are deploying an app where an `amplify.yml`
file is present, you must manually set the `baseDirectory` to `out`
in the file. The `out` directory is the default folder that Next.js creates to
store exported static assets. When you configure your app's build specification settings,
change the name of the `baseDirectory` folder to match your app's
configuration.

The following is an example of the build settings for an app where
`baseDirectory` is set to `out` to indicate that the build artifacts are for a
Next.js 13 or earlier app that supports only SSG pages.

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
    baseDirectory: out
    files:
      - '**/*'
  cache:
    paths:
      - node_modules/**/*

```

## Amplify build settings for a Next.js 14 or later SSG application

In Next.js version 14, the `next export` command was deprecated and
replaced with `output: 'export'` in the `next.config.js`
file to enable static exports. If you are deploying a Next.js 14 SSG only application in
the console, Amplify generates a buildspec for the app and sets
`baseDirectory` to `.next`. If you are deploying an app where an
`amplify.yml` file is present, you must manually set the
`baseDirectory` to `.next` in the file. This is the same
`baseDirectory` setting that Amplify uses for Next.js
`WEB_COMPUTE` applications that support both SSG and SSR pages.

The following is an example of the build settings for a Next.js 14 SSG only app with
the `baseDirectory` set to `.next`.

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
