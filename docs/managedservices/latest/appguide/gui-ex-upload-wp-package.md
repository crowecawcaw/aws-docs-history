# Upload the WordPress Application

You automatically have access to any S3 bucket instance that you create. You can access it through your Bastions
(see [Accessing Instances](../userguide/using-bastions.md "../userguide/using-bastions.md")), or through the S3 console, and upload the CodeDeploy bundle.
The bundle needs to be in place in order to continue deploying the stack. The example uses the bucket name previously created.

You can use this AWS command to zip up the bundle:

```
aws s3 cp wordpress/wordpress.zip s3://ACCOUNT_ID-codedeploy-bundles/
```
