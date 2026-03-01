# Updating a static website deployed to Amplify from an S3 bucket

If you update any of the objects for a static website in general purpose S3
bucket hosted on Amplify, you must redeploy the application to Amplify
Hosting to cause the changes to take effect. Amplify Hosting doesn't automatically
detect changes to the S3 bucket. We recommend that you use the AWS Command Line Interface
(CLI) to update your website.

**Sync updates to S3**

After you make changes to your website's project files, use the following [s3 sync](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/sync.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/sync.html") command to synchronize the changes that you made to your local
source directory with your target Amazon S3 general purpose bucket. To use this example,
replace `<source>` with the name of your local directory and
`<target>` with the name of your Amazon S3 bucket.

```
aws s3 sync `<source>` `<target>`
```

**Redeploy the website to Amplify Hosting**

Use the following [amplify start-deployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/start-deployment.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/start-deployment.html") command to redeploy your updated application in an
Amazon S3 bucket to Amplify Hosting. To use this example, replace
`<app_id>` with the id of your Amplify application,
`<branch_name>` with the name of your branch, and
`s3://amzn-s3-demo-website-bucket/prefix` with your
S3 bucket and prefix. .

```
aws amplify start-deployment --app-id `<app_id>` --branch-name `<branch_name>` --source-url `s3://amzn-s3-demo-website-bucket/prefix` --source-url-type BUCKET_PREFIX

```
