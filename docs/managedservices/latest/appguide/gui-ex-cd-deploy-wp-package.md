

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Deploy the WordPress Application with CodeDeploy
<a name="gui-ex-cd-deploy-wp-package"></a>

Deploy the CodeDeploy application.

REQUIRED DATA:
+ `VPC-ID`: The VPC you are using, this should be the same as the previously used VPC.
+ `CodeDeployApplicationName`: Use the name for the CodeDeploy application that you previously created.
+ `CodeDeployDeploymentGroupName`: Use the name of the CodeDeploy deployment group that you created previously.
+ `S3Location` (where you uploaded the application bundle): `S3Bucket`: The BucketName that you previously created, `S3BundleType` and `S3Key`: The type of, and name of, the bundle that you put on your S3 store.

1. Deploy the WordPress CodeDeploy Application Bundle

   On the **Create RFC** page, select the category **Deployment**, subcategory **Applications**, item **CodeDeploy application**, and operation **Deploy** from the RFC CT pick list. Choose **Basic** and set the values as shown. Click **Submit** when finished.
**Note**  
Reference the CodeDeploy application, CodeDeploy deployment group, S3 bucket and bundle previously created.

   ```
   Subject:                                  WP-CD-Deploy-RFC
   CodeDeployApplicationName:                {{WordPress}}
   CodeDeployDeploymentGroupName:            {{WPCDGroup}}
   RevisionType:                             S3
   S3Bucket:                                 {{ACCOUNT_ID-codedeploy-bundles}}
   S3BundleType:                             zip
   S3Key:                                    wordpress.zip   
   VpcId:                                    {{VPC_ID}}
   Name:                                     WordPress
   ```

1. Click **Submit** when finished.