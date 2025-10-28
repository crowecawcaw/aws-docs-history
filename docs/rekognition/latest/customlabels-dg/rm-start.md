# Starting an Amazon Rekognition Custom Labels model

You can start running an Amazon Rekognition Custom Labels model by using the console or by using
the [StartProjectVersion](../APIReference/API_StartProjectVersion.md "../APIReference/API_StartProjectVersion.md") operation.

###### Important

You are charged for the number of hours that your model is running and for the
number of inference units that your model uses while it is running. For more
information, see [Running a trained Amazon Rekognition Custom Labels model](running-model.md "running-model.md").

Starting a model might take a few minutes to complete.
To check the current status of the model readiness, check the details page for the project or
use [DescribeProjectVersions](../APIReference/API_DescribeProjectVersions.md "../APIReference/API_DescribeProjectVersions.md").

After the model is started you use [DetectCustomLabels](../APIReference/API_DetectCustomLabels.md "../APIReference/API_DetectCustomLabels.md"),
to analyze images using the model. For more information,
see [Analyzing an image with a trained model](detecting-custom-labels.md "detecting-custom-labels.md"). The console
also provides example code to call `DetectCustomLabels`.

###### Topics

- [Starting an Amazon Rekognition Custom Labels model (Console)](#rm-start-console "#rm-start-console")
- [Starting an Amazon Rekognition Custom Labels model (SDK)](#rm-start-sdk "#rm-start-sdk")

## Starting an Amazon Rekognition Custom Labels model (Console)

Use the following procedure to start running an Amazon Rekognition Custom Labels model with the console.
You can start the model directly from the console or use the AWS SDK code provided by the console.

###### To start a model (console)

1. Open the Amazon Rekognition console at
   [https://console.aws.amazon.com/rekognition/](https://console.aws.amazon.com/rekognition/ "https://console.aws.amazon.com/rekognition/").
2. Choose **Use Custom Labels**.
3. Choose **Get started**.
4. In the left navigation pane, choose **Projects**.
5. On the **Projects** resources page, choose the project that contains the trained model that you want
   to start.
6. In the **Models** section, choose the model that you want to start.
7. Choose the **Use model** tab.
8. Do one of the following:

Start model using the console
In the **Start or stop model** section do the following:

    1. Select the number of inference units that you want to use. For more information, see
     [Running a trained Amazon Rekognition Custom Labels model](running-model.md "running-model.md").
    2. Choose **Start**.
    3. In the **Start model** dialog box, choose **Start**.

Start model using the AWS SDK
In the **Use your model** section do the following:

    1. Choose **API Code.**
    2. Choose either **AWS CLI** or
     **Python**.
    3. In **Start model** copy the example code.
    4. Use the example code to start your model. For more information, see
     [Starting an Amazon Rekognition Custom Labels model (SDK)](#rm-start-sdk "#rm-start-sdk").

9. To go back to the project overview page, choose your project name at the
   top of the page .
10. In the **Model** section, check the status of the model. When the model status is
    **RUNNING**, you can use the model to analyze
    images. For more information, see [Analyzing an image with a trained model](detecting-custom-labels.md "detecting-custom-labels.md").

## Starting an Amazon Rekognition Custom Labels model (SDK)

You start a model by calling the [StartProjectVersion](../APIReference/API_StartProjectVersion.md "../APIReference/API_StartProjectVersion.md") API and passing the
Amazon Resource Name (ARN) of the model in the `ProjectVersionArn` input parameter.
You also specify the number of inference units that you want to use. For more information, see
[Running a trained Amazon Rekognition Custom Labels model](running-model.md "running-model.md").

A model might take a while to start. The Python and Java examples in this topic
use waiters to wait for the model to start. A waiter is a utility method that polls for a
particular state to occur. Alternatively, you can check the current status by calling
[DescribeProjectVersions](../APIReference/API_DescribeProjectVersions.md "../APIReference/API_DescribeProjectVersions.md").

###### To start a model (SDK)

1. If you haven't already done so, install and configure the AWS CLI and the AWS SDKs. For more information, see
   [Step 4: Set up the AWS CLI and AWS SDKs](su-awscli-sdk.md "su-awscli-sdk.md").
2. Use the following example code to start a model.

CLI
Change the value of `project-version-arn` to the ARN of the
model that you want to start. Change the value of `--min-inference-units` to the number of inference
units that you want to use. Optionally, change `--max-inference-units` to the maximum number of inference units that Amazon Rekognition Custom Labels
can use to automatically scale the model.

```
aws rekognition start-project-version  --project-version-arn `model_arn` \
   --min-inference-units `minimum number of units \`
   --max-inference-units `maximum number of units \`
   --profile custom-labels-access

```

Python
Supply the following command line parameters:

    * `project_arn` – the ARN of the
     project that contains the model that you want to start.
    * `model_arn` – the ARN of the
     model that you want to start.
    * `min_inference_units` – the number of inference
     units that you want to use.
    * (Optional) `--max_inference_units` The maximum number of inference units that Amazon Rekognition Custom Labels
     can use to auto-scale the model.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Purpose
Shows how to start running an Amazon Lookout for Vision model.
"""

import argparse
import logging
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


def get_model_status(rek_client, project_arn, model_arn):
    """
    Gets the current status of an Amazon Rekognition Custom Labels model
    :param rek_client: The Amazon Rekognition Custom Labels Boto3 client.
    :param project_name:  The name of the project that you want to use.
    :param model_arn:  The name of the model that you want the status for.
    :return: The model status
    """

    logger.info("Getting status for %s.", model_arn)

    # Extract the model version from the model arn.
    version_name = (model_arn.split("version/", 1)[1]).rpartition('/')[0]

    models = rek_client.describe_project_versions(ProjectArn=project_arn,
                                                  VersionNames=[version_name])

    for model in models['ProjectVersionDescriptions']:

        logger.info("Status: %s", model['StatusMessage'])
        return model["Status"]

    error_message = f"Model {model_arn} not found."
    logger.exception(error_message)
    raise Exception(error_message)


def start_model(rek_client, project_arn, model_arn, min_inference_units, max_inference_units=None):
    """
    Starts the hosting of an Amazon Rekognition Custom Labels model.
    :param rek_client: The Amazon Rekognition Custom Labels Boto3 client.
    :param project_name:  The name of the project that contains the
    model that you want to start hosting.
    :param min_inference_units: The number of inference units to use for hosting.
    :param max_inference_units: The number of inference units to use for auto-scaling
    the model. If not supplied, auto-scaling does not happen.
    """

    try:
        # Start the model
        logger.info(f"Starting model: {model_arn}. Please wait....")

        if max_inference_units is None:
            rek_client.start_project_version(ProjectVersionArn=model_arn,
                                             MinInferenceUnits=int(min_inference_units))
        else:
            rek_client.start_project_version(ProjectVersionArn=model_arn,
                                             MinInferenceUnits=int(
                                                 min_inference_units),
                                             MaxInferenceUnits=int(max_inference_units))

        # Wait for the model to be in the running state
        version_name = (model_arn.split("version/", 1)[1]).rpartition('/')[0]
        project_version_running_waiter = rek_client.get_waiter(
            'project_version_running')
        project_version_running_waiter.wait(
            ProjectArn=project_arn, VersionNames=[version_name])

        # Get the running status
        return get_model_status(rek_client, project_arn, model_arn)

    except ClientError as err:
        logger.exception("Client error: Problem starting model: %s", err)
        raise


def add_arguments(parser):
    """
    Adds command line arguments to the parser.
    :param parser: The command line parser.
    """

    parser.add_argument(
        "project_arn", help="The ARN of the project that contains that the model you want to start."
    )
    parser.add_argument(
        "model_arn", help="The ARN of the model that you want to start."
    )
    parser.add_argument(
        "min_inference_units", help="The minimum number of inference units to use."
    )
    parser.add_argument(
        "--max_inference_units",  help="The maximum number of inference units to use for auto-scaling the model.", required=False
    )


def main():

    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s: %(message)s")

    try:

        # Get command line arguments.
        parser = argparse.ArgumentParser(usage=argparse.SUPPRESS)
        add_arguments(parser)
        args = parser.parse_args()

        # Start the model.
        session = boto3.Session(profile_name='custom-labels-access')
        rekognition_client = session.client("rekognition")

        status = start_model(rekognition_client,
                             args.project_arn, args.model_arn,
                             args.min_inference_units,
                             args.max_inference_units)

        print(f"Finished starting model: {args.model_arn}")
        print(f"Status: {status}")

    except ClientError as err:
        error_message = f"Client error: Problem starting model: {err}"
        logger.exception(error_message)
        print(error_message)

    except Exception as err:
        error_message = f"Problem starting model:{err}"
        logger.exception(error_message)
        print(error_message)


if __name__ == "__main__":
    main()

```

Java V2
Supply the following command line parameters:

    * `project_arn` – the ARN of the
     project that contains the model that you want to start.
    * `model_arn` – the ARN of the
     model that you want to start.
    * `min_inference_units` – the number of inference
     units that you want to use.
    * (Optional)`max_inference_units` – the maximum number of inference
     units that Amazon Rekognition Custom Labels can use to automatically scale the model. If you don't specify a value, automatic scaling doesn't
     happen.

```
/*
   Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
   SPDX-License-Identifier: Apache-2.0
*/
package com.example.rekognition;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.core.waiters.WaiterResponse;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.rekognition.RekognitionClient;
import software.amazon.awssdk.services.rekognition.model.DescribeProjectVersionsRequest;
import software.amazon.awssdk.services.rekognition.model.DescribeProjectVersionsResponse;
import software.amazon.awssdk.services.rekognition.model.ProjectVersionDescription;
import software.amazon.awssdk.services.rekognition.model.ProjectVersionStatus;
import software.amazon.awssdk.services.rekognition.model.RekognitionException;
import software.amazon.awssdk.services.rekognition.model.StartProjectVersionRequest;
import software.amazon.awssdk.services.rekognition.model.StartProjectVersionResponse;
import software.amazon.awssdk.services.rekognition.waiters.RekognitionWaiter;

import java.util.Optional;
import java.util.logging.Level;
import java.util.logging.Logger;

public class StartModel {

    public static final Logger logger = Logger.getLogger(StartModel.class.getName());



    public static int findForwardSlash(String modelArn, int n) {

        int start = modelArn.indexOf('/');
        while (start >= 0 && n > 1) {
            start = modelArn.indexOf('/', start + 1);
            n -= 1;
        }
        return start;

    }

    public static void startMyModel(RekognitionClient rekClient, String projectArn, String modelArn,
            Integer minInferenceUnits, Integer maxInferenceUnits
            ) throws Exception, RekognitionException {

        try {

            logger.log(Level.INFO, "Starting model: {0}", modelArn);

            StartProjectVersionRequest startProjectVersionRequest = null;

            if (maxInferenceUnits == null) {
                startProjectVersionRequest = StartProjectVersionRequest.builder()
                    .projectVersionArn(modelArn)
                    .minInferenceUnits(minInferenceUnits)
                    .build();
            }
            else {
                startProjectVersionRequest = StartProjectVersionRequest.builder()
                        .projectVersionArn(modelArn)
                        .minInferenceUnits(minInferenceUnits)
                        .maxInferenceUnits(maxInferenceUnits)
                        .build();

            }

            StartProjectVersionResponse response = rekClient.startProjectVersion(startProjectVersionRequest);

            logger.log(Level.INFO, "Status: {0}", response.statusAsString() );


            // Get the model version

            int start = findForwardSlash(modelArn, 3) + 1;
            int end = findForwardSlash(modelArn, 4);

            String versionName = modelArn.substring(start, end);


            // wait until model starts

            DescribeProjectVersionsRequest describeProjectVersionsRequest = DescribeProjectVersionsRequest.builder()
                    .versionNames(versionName)
                    .projectArn(projectArn)
                    .build();

            RekognitionWaiter waiter = rekClient.waiter();

            WaiterResponse<DescribeProjectVersionsResponse> waiterResponse = waiter
                    .waitUntilProjectVersionRunning(describeProjectVersionsRequest);

            Optional<DescribeProjectVersionsResponse> optionalResponse = waiterResponse.matched().response();

            DescribeProjectVersionsResponse describeProjectVersionsResponse = optionalResponse.get();

            for (ProjectVersionDescription projectVersionDescription : describeProjectVersionsResponse
                    .projectVersionDescriptions()) {
                if(projectVersionDescription.status() == ProjectVersionStatus.RUNNING) {
                    logger.log(Level.INFO, "Model is running" );

                }
                else {
                    String error = "Model training failed: " + projectVersionDescription.statusAsString() + " "
                            + projectVersionDescription.statusMessage() + " " + modelArn;
                    logger.log(Level.SEVERE, error);
                    throw new Exception(error);
                }

            }


        } catch (RekognitionException e) {
            logger.log(Level.SEVERE, "Could not start model: {0}", e.getMessage());
            throw e;
        }

    }

    public static void main(String[] args) {

        String modelArn = null;
        String projectArn = null;
        Integer minInferenceUnits = null;
        Integer maxInferenceUnits = null;




        final String USAGE = "\n" + "Usage: " + "<project_name> <version_name> <min_inference_units> <max_inference_units>\n\n" + "Where:\n"
                + "   project_arn - The ARN of the project that contains the model that you want to start. \n\n"
                + "   model_arn - The ARN of the model version that you want to start.\n\n"
                + "   min_inference_units - The number of inference units to start the model with.\n\n"
                + "   max_inference_units - The maximum number of inference units that Custom Labels can use to "
                + "   automatically scale the model. If the value is null, automatic scaling doesn't happen.\n\n";

        if (args.length < 3  || args.length >4) {
            System.out.println(USAGE);
            System.exit(1);
        }

        projectArn = args[0];
        modelArn = args[1];
        minInferenceUnits=Integer.parseInt(args[2]);

        if (args.length == 4) {
            maxInferenceUnits = Integer.parseInt(args[3]);
        }

        try {


            // Get the Rekognition client.
            RekognitionClient rekClient = RekognitionClient.builder()
            .credentialsProvider(ProfileCredentialsProvider.create("custom-labels-access"))
            .region(Region.US_WEST_2)
            .build();

            // Start the model.
            startMyModel(rekClient, projectArn, modelArn, minInferenceUnits, maxInferenceUnits);


            System.out.println(String.format("Model started: %s", modelArn));

            rekClient.close();

        } catch (RekognitionException rekError) {
            logger.log(Level.SEVERE, "Rekognition client error: {0}", rekError.getMessage());
            System.exit(1);
        } catch (Exception rekError) {
            logger.log(Level.SEVERE, "Error: {0}", rekError.getMessage());
            System.exit(1);
        }



    }

}

```
