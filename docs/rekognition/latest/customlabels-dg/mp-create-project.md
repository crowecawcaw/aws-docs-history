# Creating a project

A project manages the model versions, training dataset, and test dataset for a model. You
can create a project with the Amazon Rekognition Custom Labels console or with the API. For other project tasks,
such deleting a project, see [Managing an Amazon Rekognition Custom Labels project](managing-project.md "managing-project.md").

You can use tags to categorize and manage your Amazon Rekognition Custom Labels resources, including your
projects.

The [CreateProject](../APIReference/API_CreateProject.md "../APIReference/API_CreateProject.md") operation allows you to optionally specify tags when creating a
new project, providing the Tags as key-value pairs that you can use to categorize and manage
your resources.

## Creating an Amazon Rekognition Custom Labels Project

(Console)

You can use the Amazon Rekognition Custom Labels console to create a project. The first time you use the
console in a new AWS Region, Amazon Rekognition Custom Labels asks to create an Amazon S3 bucket (console
bucket) in your AWS account. The bucket is used to store project files. You can't use
the Amazon Rekognition Custom Labels console unless the console bucket is created.

You can use the Amazon Rekognition Custom Labels console to create a project.

###### To create a project (console)

1. Sign in to the AWS Management Console and open the Amazon Rekognition console at
   [https://console.aws.amazon.com/rekognition/](https://console.aws.amazon.com/rekognition/ "https://console.aws.amazon.com/rekognition/").
2. In the left pane, choose **Use Custom Labels**. The
   Amazon Rekognition Custom Labels landing page is shown.
3. The Amazon Rekognition Custom Labels landing page, choose **Get started**.
4. In the left pane, Choose **Projects**.
5. Choose **Create Project**.
6. In **Project name**, enter a name for your project.
7. Choose **Create project** to create your project.
8. Follow the steps in [Creating training and test datasets](creating-datasets.md "creating-datasets.md") to create the training and test datasets
   for your project.

## Creating an Amazon Rekognition Custom Labels project (SDK)

You create an Amazon Rekognition Custom Labels project by calling [CreateProject](../APIReference/API_CreateProject.md "../APIReference/API_CreateProject.md"). The
response is an Amazon Resource Name (ARN) that identifies the project. After you create
a project, you create datasets for training and testing a model. For more information,
see [Creating training and test datasets with images](md-create-dataset.md "md-create-dataset.md").

###### To create a project (SDK)

1. If you haven't already done so, install and configure the AWS CLI and the AWS SDKs. For more information, see
   [Step 4: Set up the AWS CLI and AWS SDKs](su-awscli-sdk.md "su-awscli-sdk.md").
2. Use the following code to create a project.

AWS CLI
The following example creates a project and displays its
ARN.

Change the value of `project-name` to the name of the
project that you want to create.

```
aws rekognition create-project --project-name `my_project` \
 --profile custom-labels-access --"CUSTOM_LABELS" --tags'{"key1":"value1","key2":"value2"}'
```

Python
The following example creates a project and displays its ARN.
Supply the following command line arguments:

    * `project_name` – the name of the project
     you want to create.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import argparse
import logging
import boto3

from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

def create_project(rek_client, project_name):
    """
    Creates an Amazon Rekognition Custom Labels project
    :param rek_client: The Amazon Rekognition Custom Labels Boto3 client.
    :param project_name: A name for the new prooject.
    """

    try:
        #Create the project.
        logger.info("Creating project: %s",project_name)

        response=rek_client.create_project(ProjectName=project_name)

        logger.info("project ARN: %s",response['ProjectArn'])

        return response['ProjectArn']


    except ClientError as err:
        logger.exception("Couldn't create project - %s: %s", project_name, err.response['Error']['Message'])
        raise

def add_arguments(parser):
    """
    Adds command line arguments to the parser.
    :param parser: The command line parser.
    """

    parser.add_argument(
        "project_name", help="A name for the new project."
    )


def main():

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    try:

        # Get command line arguments.
        parser = argparse.ArgumentParser(usage=argparse.SUPPRESS)
        add_arguments(parser)
        args = parser.parse_args()

        print(f"Creating project: {args.project_name}")

        # Create the project.
        session = boto3.Session(profile_name='custom-labels-access')
        rekognition_client = session.client("rekognition")

        project_arn=create_project(rekognition_client,
            args.project_name)

        print(f"Finished creating project: {args.project_name}")
        print(f"ARN: {project_arn}")

    except ClientError as err:
        logger.exception("Problem creating project: %s", err)
        print(f"Problem creating project: {err}")


if __name__ == "__main__":
    main()

```

Java V2
The following example creates a project and displays its
ARN.

Supply the following command line argument:

    * `project_name` – the name of the project
     you want to create.

```
/*
   Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
   SPDX-License-Identifier: Apache-2.0
*/
package com.example.rekognition;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.rekognition.RekognitionClient;
import software.amazon.awssdk.services.rekognition.model.CreateProjectRequest;
import software.amazon.awssdk.services.rekognition.model.CreateProjectResponse;
import software.amazon.awssdk.services.rekognition.model.RekognitionException;

import java.util.logging.Level;
import java.util.logging.Logger;

public class CreateProject {

    public static final Logger logger = Logger.getLogger(CreateProject.class.getName());

    public static String createMyProject(RekognitionClient rekClient, String projectName) {

        try {

            logger.log(Level.INFO, "Creating project: {0}", projectName);
            CreateProjectRequest createProjectRequest = CreateProjectRequest.builder().projectName(projectName).build();

            CreateProjectResponse response = rekClient.createProject(createProjectRequest);

            logger.log(Level.INFO, "Project ARN: {0} ", response.projectArn());

            return response.projectArn();

        } catch (RekognitionException e) {
            logger.log(Level.SEVERE, "Could not create project: {0}", e.getMessage());
            throw e;
        }

    }

    public static void main(String[] args) {

        final String USAGE = "\n" + "Usage: " + "<project_name> <bucket> <image>\n\n" + "Where:\n"
                + "   project_name - A name for the new project\n\n";

        if (args.length != 1) {
            System.out.println(USAGE);
            System.exit(1);
        }

        String projectName = args[0];
        String projectArn = null;
        ;

        try {

            // Get the Rekognition client.
            RekognitionClient rekClient = RekognitionClient.builder()
                .credentialsProvider(ProfileCredentialsProvider.create("custom-labels-access"))
                .region(Region.US_WEST_2)
                .build();

            // Create the project
            projectArn = createMyProject(rekClient, projectName);

            System.out.println(String.format("Created project: %s %nProject ARN: %s", projectName, projectArn));

            rekClient.close();

        } catch (RekognitionException rekError) {
            logger.log(Level.SEVERE, "Rekognition client error: {0}", rekError.getMessage());
            System.exit(1);
        }

    }

}

```

3. Note the name of the project ARN that's displayed in the response. You'll need
   it to create a model.
4. Follow the steps in [Create training and test datasets (SDK)](md-create-dataset.md#cd-create-dataset-sdk "md-create-dataset.md#cd-create-dataset-sdk") to create the training and test
   datasets for your project.

## CreateProject operation request

The following is the foramt of the CreateProject operation request:

```

{
 "AutoUpdate": "string",
 "Feature": "string",
 "ProjectName": "string",
 "Tags": {
 "string": "string"
 }
}

```
