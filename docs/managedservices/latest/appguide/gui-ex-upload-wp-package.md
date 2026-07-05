End of support notice: On June 30, 2027, AWS
will end support for AMS Advanced. After June 30, 2027, you will
no longer be able to access the AMS Advanced console or AMS Advanced resources.
For more information, see [AMS Advanced end of support](../userguide/SunsetPlan.md "../userguide/SunsetPlan.md").

# Upload the WordPress Application

You automatically have access to any S3 bucket instance that you create. You can access it through your Bastions
(see [Accessing Instances](../userguide/using-bastions.md "../userguide/using-bastions.md")), or through the S3 console, and upload the CodeDeploy bundle.
The bundle needs to be in place in order to continue deploying the stack. The example uses the bucket name previously created.

You can use this AWS command to zip up the bundle:

```
aws s3 cp wordpress/wordpress.zip s3://ACCOUNT_ID-codedeploy-bundles/
```
