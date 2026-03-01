# Troubleshooting server-side rendered applications

If you experience unexpected issues when deploying an SSR app with Amplify Hosting
compute, review the following troubleshooting topics. If you don't see a solution to
your issue here, see the [SSR web compute troubleshooting guide](https://github.com/aws-amplify/amplify-hosting/blob/main/FAQ.md#ssr-web-compute "https://github.com/aws-amplify/amplify-hosting/blob/main/FAQ.md#ssr-web-compute") in the Amplify Hosting GitHub
Issues repository.

###### Topics

- [I need help using a framework adapter](#ssr-framework-adapter "#ssr-framework-adapter")
- [Edge API routes cause my Next.js build to fail](#nextjs-edge-API-route-not-supported "#nextjs-edge-API-route-not-supported")
- [On-Demand Incremental Static Regeneration isn't working for my app](#on-demand-isr-not-supported "#on-demand-isr-not-supported")
- [My application's build output exceeds the maximum allowed size](#build-output-too-large "#build-output-too-large")
- [My build fails with an out of memory error](#out-of-memory "#out-of-memory")
- [My application's HTTP response size is too large](#http-response-size-too-large "#http-response-size-too-large")
- [How do I measure my compute app's start up time locally?](#out-of-memory "#out-of-memory")
- [My build fails with a deprecated Node.js version error](#nodejs-version "#nodejs-version")

## I need help using a framework adapter

If you are having issues deploying an SSR app that uses a framework adapter, see
[Using open source adapters for any SSR framework](using-framework-adapter.md "using-framework-adapter.md").

## Edge API routes cause my Next.js build to fail

Currently, Amplify doesn't support Next.js Edge API Routes. You must use
non-edge APIs and middleware when hosting your app with Amplify.

## On-Demand Incremental Static Regeneration isn't working for my app

Starting with version 12.2.0, Next.js supports Incremental Static Regeneration
(ISR) to manually purge the Next.js cache for a specific page. However, Amplify
doesn't currently support On-Demand ISR. If your app is using Next.js on-demand
revalidation, this feature won't work when you deploy your app to Amplify.

## My application's build output exceeds the maximum allowed size

Currently, the maximum build output size that Amplify supports for SSR apps is
220 MB. If you get an error message stating that the size of your app's build output
exceeds the maximum allowed size, you must take steps to reduce it.

To reduce the size of an app's build output, you can inspect the app's build
artifacts and identify any large dependencies to update or remove. First, download
the build artifacts to your local computer. Then, check the size of the directories.
For example, the `node_modules` directory might contain binaries
such as `@swc` and `@esbuild` that are
referenced by Next.js server runtime files. Since these binaries aren't required in
the runtime, you can delete them _after_ the build.

Use the following instructions to download an app's build output and inspect the
size of the directories using the AWS Command Line Interface (CLI).

###### To download and inspect the build output for a Next.js app

1. Open a terminal window and run the following command. Change the app id,
   branch name, and job id to your own information. For the job id, use the
   build number for the failed build that you are investigating.

```
`aws amplify get-job --app-id `abcd1234` --branch-name `main` --job-id `2``
```

2. In the terminal output, locate the presigned artifacts URL in the
   `job`, `steps`, `stepName: "BUILD"`
   section. The URL is highlighted in red in the following example
   output.

```
"job": {
    "summary": {
        "jobArn": "arn:aws:amplify:us-west-2:111122223333:apps/abcd1234/main/jobs/0000000002",
        "jobId": "2",
        "commitId": "HEAD",
        "commitTime": "2024-02-08T21:54:42.398000+00:00",
        "startTime": "2024-02-08T21:54:42.674000+00:00",
        "status": "SUCCEED",
        "endTime": "2024-02-08T22:03:58.071000+00:00"
    },
    "steps": [
        {
            "stepName": "BUILD",
            "startTime": "2024-02-08T21:54:42.693000+00:00",
            "status": "SUCCEED",
            "endTime": "2024-02-08T22:03:30.897000+00:00",
            "logUrl": `"https://aws-amplify-prod-us-west-2-artifacts.s3.us-west-2.amazonaws.com/abcd1234/main/0000000002/BUILD/log.txt?X-Amz-Security-Token=IQoJb3JpZ2luX2V...Example`
```

3. Copy and paste the URL into a browser window. An
   `artifacts.zip` file is downloaded to your local
   computer. This is your build output.
4. Run the `du` disk usage command to inspect the size of the
   directories. The following example command returns the size of the
   `compute` and `static`
   directories.

```
`du -csh compute static`
```

The following is an example of the output with size information for the
`compute` and `static`
directories.

```
 29M    compute
3.8M    static
 33M    total
```

5. Open the `compute` directory, and locate the
   `node_modules` folder. Review your dependencies for
   files that you can update or remove to decrease the size of the
   folder.
6. If your app includes binaries that aren't required in the runtime, delete
   them after the build by adding the following commands to the build section
   of your app's `amplify.yml` file.

```
- rm -f node_modules/@swc/core-linux-x64-gnu/swc.linux-x64-gnu.node
- rm -f node_modules/@swc/core-linux-x64-musl/swc.linux-x64-musl.node
```

The following is an example of the build commands section of an
`amplify.yml` file with these commands added
_after_ running a production build.

```
frontend:
  phases:
    build:
      commands:
         -npm run build

         // After running a production build, delete the files
         - rm -f node_modules/@swc/core-linux-x64-gnu/swc.linux-x64-gnu.node
         - rm -f node_modules/@swc/core-linux-x64-musl/swc.linux-x64-musl.node
```

## My build fails with an out of memory error

Next.js enables you to cache build artifacts to improve performance on subsequent
builds. In addition, Amplify's AWS CodeBuild container compresses and uploads this
cache to Amazon S3, on your behalf, to improve subsequent build performance. This could
cause your build to fail with an out of memory error.

Perform the following actions to prevent your app from exceeding the memory limit
during the build phase. First, remove `.next/cache/**/*` from the
cache.paths section of your build settings. Next, remove the
`NODE_OPTIONS` environment variable from your build settings file.
Instead, set the `NODE_OPTIONS` environment variable in the Amplify
console to define the Node maximum memory limit. For more information about setting
environment variables using the Amplify console, see [Setting environment variables](setting-env-vars.md "setting-env-vars.md").

After making these changes, try your build again. If it succeeds, add
`.next/cache/**/*` back to the cache.paths section of your build
settings file.

For more information about Next.js cache configuration to improve build
performance, see [AWS CodeBuild](https://nextjs.org/docs/app/guides/ci-build-caching#aws-codebuild "https://nextjs.org/docs/app/guides/ci-build-caching#aws-codebuild") on the Next.js website.

## My application's HTTP response size is too large

Currently, the maximum response size that Amplify supports for Next.js 12 and
later apps using the Web Compute platform is 5.72 MB. Responses over that limit
return 504 errors with no content to clients.

## How do I measure my compute app's start up time locally?

Use the following instructions to determine the local initialization/start up time
for your Next.js 12 or later Compute app. You can compare your app's performance
locally vs. on Amplify Hosting and use the results to improve your app's
performance.

###### To measure a Next.js Compute app's initialization time locally

1. Open the app's `next.config.js` file and set the
   `output` option to `standalone` as follows.

```
** @type {import('next').NextConfig} */
const nextConfig = {
  // Other options
  output: "standalone",
};

module.exports = nextConfig;
```

2. Open a terminal window and run the following command to build the
   app.

```
next build
```

3. Run the following command to copy the `.next/static`
   folder to `.next/standalone/.next/static`.

```
cp -r .next/static .next/standalone/.next/static
```

4. Run the following command to copy the `public` folder
   to `.next/standalone/public`.

```
cp -r public .next/standalone/public
```

5. Run the following command to start the Next.js server.

```
node .next/standalone/server.js
```

6. Note how long it takes between running the command in step 5 and the
   server starting. When the server is listening on a port, it should print the
   following message.

```
Listening on port 3000
```

7. Note how long it takes for any other modules to load after the starting of
   the server in step 6. For example, libraries like `bugsnag` take
   10-12 seconds to load. After it is loaded, it will display the confirmation
   message `[bugsnag] loaded`.
8. Add the time durations from step 6 and step 7 together. This result is
   your Compute app's local initialization/start up time.

## My build fails with a deprecated Node.js version error

Problem: Your SSR application build fails with a Node.js version not supported error.

```
❌ NODE.JS VERSION NOT SUPPORTED
================================================================================
Your application uses Node.js v18.x.x, which is no longer supported.
AWS Amplify Console has ended support for Node.js 14, Node.js 16 and Node.js 18.

To deploy your application, please upgrade to Node.js 20 or later.

For detailed migration guidelines, visit: https://docs.aws.amazon.com/amplify/latest/userguide/troubleshooting-general.html#update-node-version
================================================================================
```

Cause: Your SSR application was built using a deprecated Node.js version (14.x, 16.x, or 18.x). Effective September 15, 2025, Amplify blocks deployment of SSR applications that use these deprecated versions during the build process.

Update your build environment to use Node.js 20 or later. For detailed instructions, see [I need to update my application's Node.js version](troubleshooting-general.md#update-node-version "troubleshooting-general.md#update-node-version").
