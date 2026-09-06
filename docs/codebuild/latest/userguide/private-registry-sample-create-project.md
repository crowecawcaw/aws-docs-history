

# Create a CodeBuild project with a private registry
<a name="private-registry-sample-create-project"></a>

1. For information about how to create a free private repository, see [Repositories on Docker Hub](https://docs.docker.com/docker-hub/repos/). You can also run the following commands in a terminal to pull an image, get its ID, and push it to a new repository. 

   ```
   docker pull amazonlinux
   docker images amazonlinux --format {{.ID}}
   docker tag {{image-id}} {{your-username}}/{{repository-name}}:{{tag}}
   docker login
   docker push {{your-username}}/{{repository-name}}
   ```

1.  Follow the steps in [Create an AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) in the *AWS Secrets Manager User Guide*.

   

   1.  In step 3, in **Choose secret type**, choose **Other type of secret**. 

   1. In **Key/value pairs**, create one key-value pair for your Docker Hub user name and one key-value pair for your Docker Hub password. 

   1.  Continue following the steps in [Create an AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html). 

   1.  In step 5, on the **Configure automatic rotation** page, turn it off because the keys correspond to your Docker Hub credentials. 

   1.  Finish following the steps in [Create an AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html). 

    For more information, see [What is AWS Secrets Manager?](https://docs.aws.amazon.com/secretsmanager/latest/userguide/) 

1.  When you create an AWS CodeBuild project in the console, CodeBuild attaches the required permission for you. If you use an AWS KMS key other than `DefaultEncryptionKey`, you must add it to the service role. For more information, see [Modifying a role (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_modify.html#roles-managingrole-editing-console) in the *IAM User Guide*. 

    For your service role to work with Secrets Manager, it must have, at a minimum, the `secretsmanager:GetSecretValue` permission.   
![The service role configuration.](http://docs.aws.amazon.com/codebuild/latest/userguide/images/private-registry-sample-iam.png)

1.  To use the console to create a project with an environment stored in a private registry, do the following while you create a project. For information, see [Create a build project (console)](create-project.md#create-project-console). 
**Note**  
 If your private registry is in your VPC, it must have public internet access. CodeBuild cannot pull an image from a private IP address in a VPC. 

   1.  In **Environment image**, choose **Custom image**. 

   1.  For **Environment type**, choose **Linux** or **Windows**. 

   1.  For **Image registry**, choose **Other registry**. 

   1.  In **External registry URL**, enter the image location and in **Registry credential - optional** enter the ARN or name of your Secrets Manager credentials.
**Note**  
 If your credentials do not exist in your current Region, then you must use the ARN. You cannot use the credential name if the credentials exist in a different Region. 