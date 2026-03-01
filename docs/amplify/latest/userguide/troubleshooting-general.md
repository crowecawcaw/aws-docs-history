# Troubleshooting general Amplify issues

The following information can help you troubleshoot general issues with Amplify
Hosting.

###### Topics

- [HTTP 429 status code (Too many requests)](#429-request-error "#429-request-error")
- [The Amplify console doesn't display the build status and last update time for my app](#build-status-not-displayed "#build-status-not-displayed")
- [Web previews are not being created for new pull requests](#pull-request-previews "#pull-request-previews")
- [My manual deployment is stuck with a pending status in the Amplify console](#manual-deployment-pending "#manual-deployment-pending")
- [I need to update my application's Node.js version](#update-node-version "#update-node-version")

## HTTP 429 status code (Too many requests)

Amplify controls the number of requests per second (RPS) to your website based
on the processing time and data transfer that incoming requests consume. If your
application returns an HTTP 429 status code, incoming requests are exceeding the
amount of processing time and data transfer allotted to your application. This
application limit is managed by Amplify's `REQUEST_TOKENS_PER_SECOND`
service quota. For more information about quotas, see [Amplify Hosting service quotas](quotas-chapter.md "quotas-chapter.md").

To fix this issue, we recommend optimizing your application to reduce request
duration and data transfer to increase the app's RPS. For example, with the same
20,000 tokens, a highly optimized SSR page that responds within 100 milliseconds can
support higher RPS as compared to a page with latency higher than 200
milliseconds.

Similarly, an application that returns a 1 MB response size will consume more
tokens than an application that returns a 250 KB response size.

We also recommend that you leverage the Amazon CloudFront cache by configuring
Cache-Control headers that maximize the time that a given
response is kept in the cache. Requests that are served from the CloudFront cache don't
count towards the rate limit. Each CloudFront distribution can handle up to 250,000
requests per second, enabling you to scale your app very high using the cache. For
more information about the CloudFront cache, see [Optimizing
caching and availability](../../../AmazonCloudFront/latest/DeveloperGuide/ConfiguringCaching.md "../../../AmazonCloudFront/latest/DeveloperGuide/ConfiguringCaching.md") in the _Amazon CloudFront Developer
Guide_.

## The Amplify console doesn't display the build status and last update time for my app

When you navigate to the **All apps** page in the Amplify
console, a tile is displayed for each of your apps in the current Region. If you
don't see the build status, such as **Deployed**, and the
**Last update** time displayed for an app, the app doesn't have
a `Production` stage branch associated with it.

To list the apps in the console, Amplify uses the `ListApps` API.
Amplify uses the `ProductionBranch.status` attribute to display the
build status and the `ProductionBranch.lastDeployTime` attribute to
display the last update time. For more information about this API, see [ProductionBranch](../APIReference/API_ProductionBranch.md "../APIReference/API_ProductionBranch.md") in the _Amplify Hosting API
documentation_.

Use the following instructions to associate a `Production` stage to
your app's branch.

1. Sign in to the [Amplify
   console](https://console.aws.amazon.com/amplify/home "https://console.aws.amazon.com/amplify/home").
2. On the **All apps** page, choose the app that you want to
   update.
3. In the navigation pane choose **App settings**, then
   **Branch settings**.
4. In the **Branch settings** section, choose
   **Edit**.
5. For **Production branch**, choose the branch name that
   you want to use.
6. Choose **Save**.
7. Return to the **All apps** page. The build status and
   last update time should now be displayed for your app.

## Web previews are not being created for new pull requests

The web previews feature enables you to preview changes from pull requests before
merging them into an integration branch. A web preview deploys every pull request
made to your repository to a unique preview URL which is different from the URL that
your main site uses.

If you have turned on web previews for your app, but they aren't being created for
new PRs, investigate whether one of the following is the cause of your issue.

1. Check to see whether your app has reached the maximum `Branches per
app` service quota. For more information about quotas, see [Amplify Hosting service quotas](quotas-chapter.md "quotas-chapter.md").

To stay within the default quota of 50 branches per app, consider enabling
auto branch deletion in your app. This will prevent you from accumulating
branches in your account that no longer exist in your repository. 2. If you are using a public GitHub repository and your Amplify app has an
IAM service role attached to it, Amplify doesn't create previews for
security reasons. For example, apps with backends and apps that are deployed
to the `WEB_COMPUTE` hosting platform require an IAM service
role. Therefore, you can't enable web previews for these types of apps if
their repository is public.

To enable web previews to work for your app, you can either disassociate
the service role (if the app doesn't have a backend or isn't a
`WEB_COMPUTE` app), or you can make the GitHub repository
private.

## My manual deployment is stuck with a pending status in the Amplify console

Manual deployments enable you to publish your web app with Amplify Hosting
without connecting a Git provider. You can use one of the following four deployment
options.

1. Drag and drop your application folder in the Amplify console.
2. Drag and drop a .zip file (that contains the build artifacts of your site)
   in the Amplify console.
3. Upload a .zip file (that contains the build artifacts of your site) to an
   Amazon S3 bucket and connect the bucket to an app in the Amplify
   console.
4. Use a public URL that points to a .zip file (that contains the build
   artifacts of your site) in the Amplify console.

We are aware of issues with the drag a drop functionality when using an
application folder for a manual deployment in the Amplify console. These
deployments can fail for the following reasons.

- Transient network issues occur.
- There is a local change to the files during upload.
- The browser session attempts to upload a large amount of static assets
  simultaneously.

While we work on improving the reliability of our drag and drop uploads, we
recommend that you use a .zip file instead of dragging and dropping the application
folders.

We highly recommend uploading a .zip file to an Amazon S3 bucket, as this avoids file
uploads from the Amplify console and provides a higher reliability for manual
deployments. Amplify's integration with Amazon S3 simplifies this process. For more
information, see [Deploying a static website to Amplify from an Amazon S3 bucket](deploy-website-from-s3.md "deploy-website-from-s3.md").

## I need to update my application's Node.js version

Amplify support for apps using Node.js versions 14, 16, and 18 ends on September 15, 2025. The behavior after this date depends on your application type:

- SSR Applications: Build failures will occur when using deprecated Node.js versions. You won't
  be able to deploy updates until you upgrade to Node.js 20 or later.
- Non-SSR Applications: Can continue using deprecated Node.js versions if you install them manually through buildspec or live package updates.

Applications that are already deployed will continue running regardless of Node.js version.

If you are using the Amazon Linux 2023 build image, Node.js version 20 is supported by
default. Starting on September 15, 2025, the AL2023 image will automatically
support Node.js 22 and change its default Node.js version from 18 to 22.

Amazon Linux 2 (AL2) doesn't automatically support Node.js version 20 or later. If you are
currently using AL2, we recommend that you switch to AL2023. You can change the
build image in the Amplify console. You can also use a custom build image that
supports the Node.js version that you specify.

Prior to upgrading, we recommend that you test your application on a new branch to verify that it functions correctly.

**Upgrade options**

**Amplify console**
You can use the live package updates feature in the Amplify console to specify the version of Node.js to use. For instructions, see [Using specific package and dependency versions in the build image](custom-build-image.md#setup-live-updates "custom-build-image.md#setup-live-updates").

**Custom build image**
If you are using a custom build image and NVM is installed on your image, you can add
`nvm install 20` to your Dockerfile. To learn more about
the requirements and configuration instructions for a custom build
image, see [Customizing the build image](custom-build-image.md "custom-build-image.md").

**Build settings**
You can specify the Node.js version to use in your application's
`amplify.yml` build settings, by adding the
`nvm use` command to the preBuild commands section. For
instructions on updating an application's build settings, see [Configuring the build settings for an Amplify application](build-settings.md "build-settings.md").

The following example demonstrates how to customize the build settings to
set the default Node.js version to Node.js 18 and upgrade to Node.js
version 20 on a test branch named `node-20`.

```
frontend:
  phases:
    preBuild:
      commands:
        - nvm use 18
        - if [ "${AWS_BRANCH}" = "node-20" ]; then nvm use 20; fi
```

###### Warning

Be aware that `preBuild` commands run after live package updates. The Node.js version specified by the `nvm use` command will override the Node.js version set by live package updates.
