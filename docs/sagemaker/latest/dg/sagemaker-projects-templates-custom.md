

# Create Custom Project Templates
<a name="sagemaker-projects-templates-custom"></a>

**Important**  
As of October 28, 2024, the AWS CodeCommit templates have been removed. For new projects, select from the available project templates that use third-party Git repositories. For more information, see [MLOps Project Templates](sagemaker-projects-templates.md).

If the SageMaker AI-provided templates do not meet your needs (for example, you want to have more complex orchestration in the CodePipeline with multiple stages or custom approval steps), create your own templates.

We recommend starting by using SageMaker AI-provided templates to understand how to organize your code and resources and build on top of it. To do this, after you enable administrator access to the SageMaker AI templates, log in to the [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/), choose **Portfolios**, then choose **Imported**. For information about Service Catalog, see [Overview of Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/what-is_concepts.html) in the *Service Catalog User Guide*.

Create your own project templates to customize your MLOps project. SageMaker AI project templates are Service Catalog–provisioned products to provision the resources for your MLOps project. 

To create a custom project template, complete the following steps.

1. Create a portfolio. For information, see [Step 3: Create an Service Catalog Portfolio](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-portfolio.html).

1. Create a product. A product is a CloudFormation template. You can create multiple versions of the product. For information, see [Step 4: Create an Service Catalog Product](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-product.html).

   For the product to work with SageMaker Projects, add the following parameters to your product template.

   ```
   SageMakerProjectName:
   Type: String
   Description: Name of the project
   
   SageMakerProjectId:
   Type: String
   Description: Service generated Id of the project.
   ```
**Important**  
We recommend that you wrap the CodeCommit repository into the SageMaker AI code repository for the project's repositories to be visible in VPC mode. The sample template and required addition are shown in the following code samples.  
Original (sample) template:  

   ```
   ModelBuildCodeCommitRepository:
       Type: AWS::CodeCommit::Repository
       Properties:
         # Max allowed length: 100 chars
         RepositoryName: !Sub sagemaker-${SageMakerProjectName}-${SageMakerProjectId}-modelbuild # max: 10+33+15+10=68
         RepositoryDescription: !Sub SageMaker Model building workflow infrastructure as code for the Project ${SageMakerProjectName}
         Code:
           S3:
             Bucket: {{SEEDCODE_BUCKETNAME}}
             Key: toolchain/model-building-workflow-v1.0.zip
           BranchName: main
   ```
Additional content to add in VPC mode:  

   ```
   SageMakerRepository:
       Type: AWS::SageMaker::CodeRepository
       Properties:
           GitConfig:
               RepositoryUrl: !GetAtt ModelBuildCodeCommitRepository.CloneUrlHttp
               Branch: main
   ```

1. Add a launch constraint. A launch constraint designates an IAM role that Service Catalog assumes when a user launches a product. For information, see [Step 6: Add a Launch Constraint to Assign an IAM Role](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-launchconstraint.html).

1. Provision the product on [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/) to test the template. If you are satisfied with your template, continue to the next step to make the template available in Studio (or Studio Classic).

1. Grant access to the Service Catalog portfolio that you created in step 1 to your Studio (or Studio Classic) execution role. Use either the domain execution role or a user role that has Studio (or Studio Classic) access. For information about adding a role to the portfolio, see [Step 7: Grant End Users Access to the Portfolio](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-deploy.html).

1. To make your project template available in your **Organization templates** list in Studio (or Studio Classic), create a tag with the following key and value to the Service Catalog product you created in step 2.
   + **key**: `sagemaker:studio-visibility`
   + **value**: `true`

After you complete these steps, Studio (or Studio Classic) users in your organization can create a project with the template you created by following the steps in [Create a MLOps Project using Amazon SageMaker Studio or Studio Classic](sagemaker-projects-create.md) and choosing **Organization templates** when you choose a template.

## Using a template from an Amazon S3 bucket
<a name="sagemaker-projects-templates-s3"></a>

You can also create SageMaker projects using templates stored in Amazon S3.

**Note**  
While you can use the templates in the AWS Service Catalog, we recommend that you store templates in an S3 bucket and create projects using those templates.

### Admin setup
<a name="sagemaker-projects-templates-s3-setup"></a>

Before you can create projects using templates in an S3 bucket, perform the following steps.

1. [Create an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html), and upload your templates to the bucket.

1. [Set up a CORS policy on your S3 bucket to configure access permissions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enabling-cors-examples.html).

1. Add the following key-value tag to the template so they become visible to SageMaker AI.

   ```
   sagemaker:studio-visibility : true
   ```

1. [Create a domain](https://docs.aws.amazon.com/sagemaker/latest/dg/onboard-quick-start.html).

1. After SageMaker AI finishes creating your domain, add the following key-value tag to the domain:

   ```
   sagemaker:projectS3TemplatesLocation : s3://{{<amzn-s3-demo-bucket>}}
   ```

Then use the AWS console, Python, or the [CreateProject](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProject.html) and [UpdateProject](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateProject.html) API operations to create or update a SageMaker project from templates inside the S3 bucket.

------
#### [ Studio ]

**Create a project**

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. Open the SageMaker Studio console by following the instructions in [Launch Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-launch.html).

1. In the left navigation pane, choose **Deployments**, **Projects**, **Create project**.

1. Choose **Organization templates** and then **S3 Templates** to see the templates that are available to you. If you don't see a template that you're expecting, notify your administrator.

1. Choose the template that you want to use, and then choose **Next**.

1. Enter a name for your project, an optional description, and the other required fields. When you're done, choose **Create**.

**Update a project**

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. Open the SageMaker Studio console by following the instructions in [Launch Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-launch.html).

1. Choose the project that you want to update. Choose **Actions**, then choose **Update Project**.

1. When updating a project, you can update the template parameters or the template URL. When you're done, choose **Next**.

1. Review the project updates in the summary table, and choose **Update**.

------
#### [ Python Boto3 ]

After you create the S3 bucket and uploaded your templates, you can use the following example to create a SageMaker project.

```
sagemaker_client = boto3.client('sagemaker', region_name='us-west-2')

response = sagemaker_client.create_project(
    ProjectName='my-custom-project',
    ProjectDescription='SageMaker project with custom CFN template stored in S3',
    TemplateProviders=[{
        'CfnTemplateProvider': {
            'TemplateName': 'CustomProjectTemplate',
            'TemplateURL': f'https://{{<bucket_name>}}.s3.us-west-2.amazonaws.com/{{custom-project-template.yml}}',
            'Parameters': [
                {'Key': 'ParameterKey', 'Value': 'ParameterValue'}
            ]
        }
    }]
)
print(f"Project ARN: {response['ProjectArn']}")
```

To update a SageMaker project, see the following example.

```
sagemaker_client = boto3.client('sagemaker', region_name='us-west-2')

response = sagemaker_client.update_project(
    ProjectName='my-custom-project',
    ProjectDescription='SageMaker project with custom CFN template stored in S3',
    TemplateProvidersToUpdate=[{
        'CfnTemplateProvider': {
            'TemplateName': 'CustomProjectTemplate',
            'TemplateURL': f'https://{{<bucket_name>}}.s3.us-west-2.amazonaws.com/{{custom-project-template.yml}}',
            'Parameters': [
                {'Key': 'ParameterKey', 'Value': 'ParameterValue'}
            ]
        }
    }]
)
print(f"Project ARN: {response['ProjectArn']}")
```

------