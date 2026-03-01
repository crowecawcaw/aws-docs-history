# Customizing the build image

You can use a custom build image to provide a customized build environment for an
Amplify app. If you have specific dependencies that take a long time to install during a
build using Amplify's default container, you can create your own Docker image and
reference it during a build. Images can be hosted on Amazon Elastic Container Registry Public.

For a custom build image to work as an Amplify build image, it must meet the following
requirements.

**Custom build image requirements**

1. A Linux distribution that supports the GNU C Library (glibc), such as Amazon
   Linux, compiled for the x86-64 architecture.
2. **cURL**: When we launch your custom image, we
   download our build runner into your container, and therefore we require cURL to be
   present. If this dependency is missing, the build instantly fails without any
   output as our build-runner is unable to produce any output.
3. **Git**: In order to clone your Git repository we
   require Git to be installed in the image. If this dependency is missing, the
   **Cloning repository** step will fail.
4. **OpenSSH**: In order to securely clone your
   repository we require OpenSSH to set up the SSH key temporarily during the build.
   The OpenSSH package provides the commands that the build runner requires to do
   this.
5. **Bash and The Bourne Shell**: These two utilities
   are used to run commands at build time. If they aren't installed, your builds
   might fail prior to starting.
6. **Node.JS+NPM**: Our build runner doesn't install
   Node. Instead, it relies on Node and NPM being installed in the image. This is
   only required for builds that require NPM packages or Node specific commands.
   However, we strongly recommend installing them because when they are present, the
   Amplify build runner can use these tools to improve the build execution.
   Amplify's package override feature uses NPM to install the Hugo-extended package
   when you set an override for Hugo.
   The following packages aren't required, but we strongly recommend that you install them.

7. **NVM (Node Version Manager)**: We
   recommend that you install this version manager if you need to handle different
   versions of Node. When you set an
   override, Amplify’s package override feature uses
   NVM to change Node.js versions before each build.
8. **Wget**: Amplify can use the Wget utility to download files during the build process. We recommend that you install it in your custom image.
9. **Tar**: Amplify can use the Tar utility to uncompress downloaded files during the build process. We recommend that you install it in your custom image.

## Configuring a custom build image for an app

Use the following procedure to configure a custom build image for an application in the Amplify console.

###### To configure a custom build image hosted in Amazon ECR

1. See [Getting
   started](../../../AmazonECR/latest/public/public-getting-started.md "../../../AmazonECR/latest/public/public-getting-started.md") in the _Amazon ECR Public User guide_ to set
   up an Amazon ECR Public repository with a Docker image.
2. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
3. Choose the app that you want to configure a custom build image for.
4. In the navigation pane, choose **Hosting**, **Build
   settings**.
5. On the **Build settings** page, in the **Build image
   settings** section, choose **Edit**.
6. On the **Edit build image settings** page, expand the
   **Build image** menu, and choose **Custom Build
   Image**.
7. Enter the name of the Amazon ECR Public repo that you created in step one. This is
   where your build image is hosted. For example, if the name of your repo is
   _ecr-examplerepo_, you would enter
   `public.ecr.aws/xxxxxxxx/ecr-examplerepo`.
8. Choose **Save**.

## Using specific package and dependency versions in the build image

Live package updates enable you to specify the versions of packages and dependencies to
use in the Amplify default build image. The default build image comes with several
packages and dependencies pre-installed (e.g. Hugo, Amplify CLI, Yarn, etc). With live
package updates you can override the version of these dependencies and specify either a
specific version, or ensure that the latest version is always installed.

If live package updates is
enabled, before your build runs, the build runner first updates (or downgrades) the
specified dependencies. This increases the build time proportional to the time it takes to
update the dependencies, but the benefit is that you can ensure the same version of a
dependency is used to build your app.

###### Warning

Setting the Node.js version to **latest** causes builds to fail. Instead, you must specify an exact Node.js version, such as `18`, `21.5`, or `v0.1.2`.

###### To configure live package updates

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. Choose the app that you want to configure live package updates for.
3. In the navigation pane, choose **Hosting**, **Build
   settings**.
4. On the **Build settings** page, in the **Build image
   settings** section, choose **Edit**.
5. On the **Edit build image settings** page, **Live
   package updates** list, choose **Add new**.
6. For **Package**, select the dependency to override.
7. For **Version**, either keep the default
   **latest** or enter a specific version of the dependency. If
   you use **latest**, the dependency will always be upgraded to the
   latest version available.
8. Choose **Save**.
