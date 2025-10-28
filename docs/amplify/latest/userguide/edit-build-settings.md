# Editing the build specification

You can customize an application's build settings by editing the build specification (buildspec) in
the Amplify console. The build settings are applied to all the branches in your app, except
for the branches that have an `amplify.yml` file saved in the Git
repository.

###### To edit build settings in the Amplify console

1. Sign in to the AWS Management Console and open the [Amplify
   console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. Choose the app that you want to edit the build settings for.
3. In the navigation pane, choose **Hosting**, then choose
   **Build settings**.
4. On the **Build settings** page, in the **App build
   specification** section, choose **Edit**.
5. In the **Edit build spec** window, enter your updates.
6. Choose **Save**.
   You can use the examples described in the following topics to update your build settings
   for specific scenarios.

###### Topics

- [Setting branch-specific build settings with
  scripting](#branch-specific-build-settings "#branch-specific-build-settings")
- [Setting a command to navigate to a
  subfolder](#navigating-to-a-subfolder "#navigating-to-a-subfolder")
- [Deploying the backend with the front end for a Gen 1
  app](#frontend-with-backend "#frontend-with-backend")
- [Setting the output folder](#setting-the-output-folder "#setting-the-output-folder")
- [Installing packages as part of a
  build](#installing-packages-as-part-of-your-build "#installing-packages-as-part-of-your-build")
- [Using a private npm registry](#using-a-private-npm-registry "#using-a-private-npm-registry")
- [Installing OS packages](#installing-os-packages "#installing-os-packages")
- [Setting key-value storage for every
  build](#key-value-storage-for-every-build "#key-value-storage-for-every-build")
- [Skipping the build for a commit](#skip-build-for-a-commit "#skip-build-for-a-commit")
- [Turning off automatic builds on every
  commit](#disable-automatic-builds "#disable-automatic-builds")
- [Configuring diff based frontend build and
  deploy](#enable-diff-deploy "#enable-diff-deploy")
- [Configuring diff based backend builds for a Gen 1
  app](#enable-diff-backend "#enable-diff-backend")

## Setting branch-specific build settings with

scripting

You can use bash shell scripting to set branch-specific build settings. For example, the
following script uses the system environment variable _$AWS_BRANCH_ to run one set of commands if the branch name is _main_ and a different set of commands if the branch name
is _dev_.

```
frontend:
  phases:
    build:
      commands:
        - if [ "${AWS_BRANCH}" = "main" ]; then echo "main branch"; fi
        - if [ "${AWS_BRANCH}" = "dev" ]; then echo "dev branch"; fi
```

## Setting a command to navigate to a

subfolder

For monorepos, users want to be able to `cd` into a folder to run the build.
After you run the `cd` command, it applies to all stages of your build so you
don’t need to repeat the command in separate phases.

```
version: 1
env:
  variables:
    key: value
frontend:
  phases:
    preBuild:
      commands:
        - cd react-app
        - npm ci
    build:
      commands:
        - npm run build
```

## Deploying the backend with the front end for a Gen 1

app

###### Note

This section applies to Amplify Gen 1 applications only. A Gen 1 backend is created
using Amplify Studio and the Amplify command line interface (CLI).

The `amplifyPush` command is a helper script that helps you with backend
deployments. The build settings below automatically determine the correct backend
environment to deploy for the current branch.

```
version: 1
env:
  variables:
    key: value
backend:
  phases:
    build:
      commands:
        - amplifyPush --simple
```

## Setting the output folder

The following build settings set the output directory to the public folder.

```
frontend:
  phases:
    commands:
      build:
        - yarn run build
  artifacts:
    baseDirectory: public
```

## Installing packages as part of a

build

You can use the `npm` or `yarn` commands to install packages
during the build.

```
frontend:
  phases:
    build:
      commands:
        - npm install -g <package>
        - <package> deploy
        - yarn run build
  artifacts:
    baseDirectory: public
```

## Using a private npm registry

You can add references to a private registry in your build settings or add it as an
environment variable.

```
build:
  phases:
    preBuild:
      commands:
        - npm config set <key> <value>
        - npm config set registry https://registry.npmjs.org
        - npm config set always-auth true
        - npm config set email hello@amplifyapp.com
        - yarn install
```

## Installing OS packages

Amplify's AL2023 image runs your code with a non-privileged user named
`amplify`. Amplify grants this user privileges to run OS commands using the
Linux `sudo` command. If you want to install OS packages for missing
dependencies, you can use commands such as `yum` and `rpm` with
`sudo`.

The following example build section demonstrates the syntax for installing an OS package
using the `sudo` command.

```
build:
  phases:
    preBuild:
      commands:
        - sudo yum install -y <package>
```

## Setting key-value storage for every

build

The `envCache` provides key-value storage at build time. Values stored in the
`envCache` can only be modified during a build and can be re-used at the next
build. Using the `envCache`, we can store information on the deployed environment
and make it available to the build container in successive builds. Unlike values stored in
the `envCache`, changes to environment variables during a build are not persisted
to future builds.

Example usage:

```
envCache --set <key> <value>
envCache --get <key>
```

## Skipping the build for a commit

To skip an automatic build on a particular commit, include the text **[skip-cd]** at the end of the commit message.

## Turning off automatic builds on every

commit

You can configure Amplify to turn off automatic builds on every code commit. To set
up, choose **App settings**, **Branch settings**, and then
locate the **Branches** section that lists the connected branches. Select a
branch, and then choose **Actions**, **Disable auto
build**. New commits to that branch will no longer start a new build.

## Configuring diff based frontend build and

deploy

You can configure Amplify to use diff based frontend builds. If enabled, at the start
of each build Amplify attempts to run a diff on either your `appRoot`, or the
`/src/` folder by default. If Amplify doesn't find any differences, it skips
the frontend build, test (if configured), and deploy steps, and does not update your hosted
app.

###### To configure diff based frontend build and deploy

1. Sign in to the AWS Management Console and open the [Amplify
   console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. Choose the app to configure diff based frontend build and deploy for.
3. In the navigation pane, choose **Hosting**, **Environment
   variables**.
4. In the **Environment variables** section, choose **Manage
   variables**.
5. The procedure for configuring the environment variable varies depending on whether
   you are enabling or disabling diff based frontend build and deploy.
   - To enable diff based frontend build and deploy
     1. In the **Manage variables** section, under
        **Variable**, enter `AMPLIFY_DIFF_DEPLOY`.
     2. For **Value**, enter `true`.

   - To disable diff based frontend build and deploy
     1. Do one of the following:
        - In the **Manage variables** section, locate
          `AMPLIFY_DIFF_DEPLOY`. For **Value**, enter
          `false`.
        - Remove the `AMPLIFY_DIFF_DEPLOY` environment variable.

6. Choose **Save**.

Optionally, you can set the `AMPLIFY_DIFF_DEPLOY_ROOT` environment variable
to override the default path with a path relative to the root of your repo, such as
`dist`.

## Configuring diff based backend builds for a Gen 1

app

###### Note

This section applies to Amplify Gen 1 applications only. A Gen 1 backend is created
using Amplify Studio and the Amplify command line interface (CLI).

You can configure Amplify Hosting to use diff based backend builds using the
`AMPLIFY_DIFF_BACKEND` environment variable. When you enable diff based backend
builds, at the start of each build Amplify attempts to run a diff on the
`amplify` folder in your repository. If Amplify doesn't find any differences,
it skips the backend build step, and doesn't update your backend resources. If your project
doesn't have an `amplify` folder in your repository, Amplify ignores the value
of the `AMPLIFY_DIFF_BACKEND` environment variable.

If you currently have custom commands specified in the build settings of your backend
phase, conditional backend builds won't work. If you want those custom commands to run, you
must move them to the frontend phase of your build settings in your app's
`amplify.yml` file.

###### To configure diff based backend builds

1. Sign in to the AWS Management Console and open the [Amplify
   console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. Choose the app to configure diff based backend builds for.
3. In the navigation pane, choose **Hosting**, **Environment
   variables**.
4. In the **Environment variables** section, choose **Manage
   variables**.
5. The procedure for configuring the environment variable varies depending on whether
   you are enabling or disabling diff based backend builds.
   - To enable diff based backend builds
     1. In the **Manage variables** section, under
        **Variable**, enter `AMPLIFY_DIFF_BACKEND`.
     2. For **Value**, enter `true`.

   - To disable diff based backend builds
     1. Do one of the following:
        - In the **Manage variables** section, locate
          `AMPLIFY_DIFF_BACKEND`. For **Value**, enter
          `false`.
        - Remove the `AMPLIFY_DIFF_BACKEND` environment
          variable.

6. Choose **Save**.
