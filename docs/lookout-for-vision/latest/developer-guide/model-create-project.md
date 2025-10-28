End of support notice: On October 31, 2025, AWS
will discontinue support for Amazon Lookout for Vision. After October 31, 2025, you will
no longer be able to access the Lookout for Vision console or Lookout for Vision resources.
For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision "https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision").

# Creating your project

An Amazon Lookout for Vision project is a grouping of the resources needed to create and manage a
Lookout for Vision model. A project manages the following:

- **Dataset** – The images and image labels
  used to train a model. For more information, see [Creating your dataset](model-create-dataset.md "model-create-dataset.md").
- **Model** – The software that you train to
  detect anomalies. You can have multiple versions of a model. For more
  information, see [Training your model](model-train.md "model-train.md").
  We recommend that you use a project for a single use case, such as detecting anomalies
  in a single type of machine part.

###### Note

You can use AWS CloudFormation to provision and configure Amazon Lookout for Vision projects. For more
information, see [Creating Amazon Lookout for Vision resources with
AWS CloudFormation](creating-projects-with-cloudformation.md "creating-projects-with-cloudformation.md").

To view your projects, see [Viewing your projects](view-projects.md "view-projects.md") or open the [Using the Amazon Lookout for Vision dashboard](dashboard.md "dashboard.md"). To delete a model,
see [Deleting a model](delete-model.md "delete-model.md").

###### Topics

- [Creating a project (console)](#create-project-console "#create-project-console")
- [Creating a project (SDK)](#create-project-sdk "#create-project-sdk")

## Creating a project (console)

The following procedure shows you how to create a project using the
console.

###### To create a project (console)

1. Open the Amazon Lookout for Vision console at [https://console.aws.amazon.com/lookoutvision/](https://console.aws.amazon.com/lookoutvision/ " https://console.aws.amazon.com/lookoutvision/").
2. In the left navigation pane, choose **Projects**.
3. Choose **Create project**.
4. In **Project name**, enter a name for your
   project.
5. Choose **Create project**. The details page for your
   project is displayed.
6. Follow the steps in [Creating your dataset](model-create-dataset.md "model-create-dataset.md") to create your dataset.

## Creating a project (SDK)

You use the [CreateProject](../APIReference/API_CreateProject.md "../APIReference/API_CreateProject.md")
operation to create an Amazon Lookout for Vision project. The response from
`CreateProject` includes the project name and the Amazon Resource
Name (ARN) of the project. Afterwards, call [CreateDataset](../APIReference/API_CreateDataset.md "../APIReference/API_CreateDataset.md") to add a training
and a test dataset to your project. For more information, see [Creating a dataset with a manifest file
(SDK)](create-dataset-sdk.md "create-dataset-sdk.md").

To view the projects that you have created in a project, call
`ListProjects`. For more information, see [Viewing your projects](view-projects.md "view-projects.md").

###### To create a project (SDK)

1. If you haven't already done so, install and configure the AWS CLI and the AWS SDKs. For more information, see
   [Step 4: Set up the AWS CLI and AWS SDKs](su-awscli-sdk.md "su-awscli-sdk.md").
2. Use the following example code to create a model.

CLI
Change the value of `project-name` to the name that
you want to use for the project.

```
aws lookoutvision create-project --project-name `project name` \
  --profile lookoutvision-access
```

Python
This code is taken from the AWS Documentation SDK examples GitHub repository. See the full example
[here](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/lookoutvision/train_host.py "https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/lookoutvision/train_host.py").

```
    @staticmethod
    def create_project(lookoutvision_client, project_name):
        """
        Creates a new Lookout for Vision project.

        :param lookoutvision_client: A Boto3 Lookout for Vision client.
        :param  project_name: The name for the new project.
        :return project_arn: The ARN of the new project.
        """
        try:
            logger.info("Creating project: %s", project_name)
            response = lookoutvision_client.create_project(ProjectName=project_name)
            project_arn = response["ProjectMetadata"]["ProjectArn"]
            logger.info("project ARN: %s", project_arn)
        except ClientError:
            logger.exception("Couldn't create project %s.", project_name)
            raise
        else:
            return project_arn


```

Java V2
This code is taken from the AWS Documentation SDK examples GitHub repository. See the full example
[here](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javav2/example_code/lookoutvision/src/main/java/com/example/lookoutvision/CreateProject.java "https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javav2/example_code/lookoutvision/src/main/java/com/example/lookoutvision/CreateProject.java").

```
/**
 * Creates an Amazon Lookout for Vision project.
 *
 * @param lfvClient   An Amazon Lookout for Vision client.
 * @param projectName The name of the project that you want to create.
 * @return ProjectMetadata Metadata information about the created project.
 */
public static ProjectMetadata createProject(LookoutVisionClient lfvClient, String projectName)
                throws LookoutVisionException {

        logger.log(Level.INFO, "Creating project: {0}", projectName);
        CreateProjectRequest createProjectRequest = CreateProjectRequest.builder().projectName(projectName)
                        .build();

        CreateProjectResponse response = lfvClient.createProject(createProjectRequest);

        logger.log(Level.INFO, "Project created. ARN: {0}", response.projectMetadata().projectArn());

        return response.projectMetadata();

}
```

3. Follow the steps in [Creating a dataset using an Amazon SageMaker AI
   Ground Truth manifest file](create-dataset-ground-truth.md "create-dataset-ground-truth.md") to create your
   dataset.
