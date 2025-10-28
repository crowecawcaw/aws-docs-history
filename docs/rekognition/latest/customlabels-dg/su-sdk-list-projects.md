# Call an Amazon Rekognition Custom Labels operation

Run the following code to confirm that you can make calls to the Amazon Rekognition Custom Labels API. The code lists
the projects in your AWS account, in the current AWS Region. If you haven't previously created a project,
the response is empty, but does confirm that you can call the `DescribeProjects` operation.

In general, calling an example function requires an AWS SDK Rekognition client and any
other required parameters. The AWS SDK client is declared in the main function.

If the code fails, check that the user that you use has the correct permissions. Also
check the AWS Region that you using as Amazon Rekognition Custom Labels is not available in all AWS Regions.

###### To call an Amazon Rekognition Custom Labels operation

1. If you haven't already done so, install and configure the AWS CLI and the AWS SDKs. For more information, see
   [Step 4: Set up the AWS CLI and AWS SDKs](su-awscli-sdk.md "su-awscli-sdk.md").
2. Use the following example code to view your projects.

CLI
Use the `describe-projects` command to list the
projects in your account.

```
aws rekognition describe-projects \
--profile custom-labels-access

```

Python

```

# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This example shows how to describe your Amazon Rekognition Custom Labels projects.
If you haven't previously created a project in the current AWS Region,
the response is an empty list, but does confirm that you can call an
Amazon Rekognition Custom Labels operation.
"""
from botocore.exceptions import ClientError
import boto3

def describe_projects(rekognition_client):
    """
    Lists information about the projects that are in in your AWS account
    and in the current AWS Region.

    : param rekognition_client: A Boto3 Rekognition client.
    """
    try:
        response = rekognition_client.describe_projects()
        for project in response["ProjectDescriptions"]:
            print("Status: " + project["Status"])
            print("ARN: " + project["ProjectArn"])
            print()
        print("Done!")
    except ClientError as err:
        print(f"Couldn't describe projects. \n{err}")
        raise


def main():
    """
    Entrypoint for script.
    """

    session = boto3.Session(profile_name='custom-labels-access')
    rekognition_client = session.client("rekognition")

    describe_projects(rekognition_client)


if __name__ == "__main__":
    main()

```

Java V2

```
/*
   Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
   SPDX-License-Identifier: Apache-2.0
*/

package com.example.rekognition;

import java.util.ArrayList;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.rekognition.RekognitionClient;
import software.amazon.awssdk.services.rekognition.model.DatasetMetadata;
import software.amazon.awssdk.services.rekognition.model.DescribeProjectsRequest;
import software.amazon.awssdk.services.rekognition.model.DescribeProjectsResponse;
import software.amazon.awssdk.services.rekognition.model.ProjectDescription;
import software.amazon.awssdk.services.rekognition.model.RekognitionException;

public class Hello {

    public static final Logger logger = Logger.getLogger(Hello.class.getName());

    public static void describeMyProjects(RekognitionClient rekClient) {

        DescribeProjectsRequest descProjects = null;

        // If a single project name is supplied, build projectNames argument

        List<String> projectNames = new ArrayList<String>();


        descProjects = DescribeProjectsRequest.builder().build();

        // Display useful information for each project.

        DescribeProjectsResponse resp = rekClient.describeProjects(descProjects);

        for (ProjectDescription projectDescription : resp.projectDescriptions()) {

            System.out.println("ARN: " + projectDescription.projectArn());
            System.out.println("Status: " + projectDescription.statusAsString());
            if (projectDescription.hasDatasets()) {
                for (DatasetMetadata datasetDescription : projectDescription.datasets()) {
                    System.out.println("\tdataset Type: " + datasetDescription.datasetTypeAsString());
                    System.out.println("\tdataset ARN: " + datasetDescription.datasetArn());
                    System.out.println("\tdataset Status: " + datasetDescription.statusAsString());
                }
            }
            System.out.println();
        }

    }

    public static void main(String[] args) {

        try {

            // Get the Rekognition client
            RekognitionClient rekClient = RekognitionClient.builder()
                .credentialsProvider(ProfileCredentialsProvider.create("custom-labels-access"))
                .region(Region.US_WEST_2)
                .build();

            // Describe projects

            describeMyProjects(rekClient);

            rekClient.close();

        } catch (RekognitionException rekError) {
            logger.log(Level.SEVERE, "Rekognition client error: {0}", rekError.getMessage());
            System.exit(1);
        }

    }

}

```
