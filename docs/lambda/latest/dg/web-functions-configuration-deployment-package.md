

# Web Function deployment package
<a name="web-functions-configuration-deployment-package"></a>

You package your Web Function code as a .zip file and store it in a versioned Amazon S3 bucket. The revision's `codeConfig` references the bucket, the key, and optionally an object version. If you omit the version, Lambda uses the latest version at creation time, so each revision points to a specific version of your package. Uploading a new package to the same key doesn't change existing revisions, and you can roll back to an earlier revision as long as its object version remains in the bucket.

The package must include your application's entry file and all of its dependencies (for example, `node_modules`). By default, Lambda loads `index.js` at the package root as the entry file and runs it to start your HTTP server. To use a different name or path (for example, `dist/index.js`), set the `AWS_LAMBDA_NODEJS_ENTRYPOINT` environment variable; see [Environment variables](web-functions-revisions-env-vars.md).

For how to build and upload the package to Amazon S3 and create a revision that references it, see [Deploying Web Function code from Amazon S3](web-functions-code-s3.md) and [Creating a Lambda Web Function](web-functions-create.md).