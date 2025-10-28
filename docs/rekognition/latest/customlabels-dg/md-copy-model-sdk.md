# Copying a model (SDK)

You can use the `CopyProjectVersion` API to copy a model version from a
source project to a destination project. The destination project can be in a
different AWS account but must be the same AWS Region. If the destination
project is in a different AWS account (or if you want to grant specific
permissions for a model version copied within an AWS account), you must attach a
project policy to the source project. For more information, see [Creating a project policy
document](md-create-project-policy-document.md "md-create-project-policy-document.md"). The
`CopyProjectVersion` API requires access to your Amazon S3 bucket.

The copied model includes the training results for the source model, but doesn't
include the source datasets.

The source AWS account has no ownership over the model copied into a destination
account, unless you set up appropriate permissions.

###### To copy a model (SDK)

1. If you haven't already done so, install and configure the AWS CLI and the AWS SDKs. For more information, see
   [Step 4: Set up the AWS CLI and AWS SDKs](su-awscli-sdk.md "su-awscli-sdk.md").
2. Attach a project policy to the source project by following the
   instructions at [Attaching a project policy (SDK)](md-attach-project-policy.md "md-attach-project-policy.md").
3. If you are copying the model to a different AWS account, make sure that
   you have a project in the destination AWS account.
4. Use the following code to copy the model version to a destination
   project.

AWS CLI
Change the following values:

    * `source-project-arn` to the ARN of the
     source project that contains the model version that you
     want to copy.
    * `source-project-version-arn` to the ARN of
     the model version that that you want to copy.
    * `destination-project-arn` to the ARN of the
     destination project that you want to copy the model to.
    * `version-name` to a version name for the
     model in the destination project.
    * `bucket` to the S3 bucket that you want the
     training results for the source model copied to.
    * `folder` to the folder in
     `bucket` that you want the training
     results for the source model copied to.
    * (Optional) `kms-key-id` to the AWS Key
     Management Service key ID for the model.
    * (Optional) `key` to a tag key of your
     choosing.
    * (Optional) `value` to a tag value of your
     choosing.

```
aws rekognition copy-project-version \
  --source-project-arn `source-project-arn` \
  --source-project-version-arn `source-project-version-arn` \
  --destination-project-arn `destination-project-arn` \
  --version-name `version-name` \
  --output-config '{"S3Bucket":"`bucket`","S3KeyPrefix":"`folder`"}' \
  --kms-key-id arn:`myKey` \
  --tags '{"`key`":"`key`"}' \
  --profile custom-labels-access
```

Python
Use the following code. Supply the following command line
parameters:

    * `source_project_arn` — the ARN of
     the source project in the source AWS account that
     contains the model version that you want to copy.
    * `source_project_version-arn` — the
     ARN of the model version in the source AWS account
     that that you want to copy.
    * `destination_project_arn` — the ARN
     of the destination project that you want to copy the
     model to.
    * `destination_version_name` — a
     version name for the model in the destination project.
    * `training_results` — the S3 location
     that you want the training results for the source model
     version copied to.
    * (Optional) `kms_key_id` to the AWS Key
     Management Service key ID for the model.
    * (Optional) `tag_name` to a tag key of your
     choosing.
    * (Optional) `tag_value` to a tag value of
     your choosing.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import argparse
import logging
import time
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


def copy_model(
    rekognition_client, source_project_arn, source_project_version_arn,
        destination_project_arn, training_results, destination_version_name):
    """
    Copies a version of a Amazon Rekognition Custom Labels model.

    :param rekognition_client: A Boto3 Amazon Rekognition Custom Labels client.
    :param source_project_arn: The ARN of the source project that contains the
    model that you want to copy.
    :param source_project_version_arn: The ARN of the model version that you want
    to copy.
    :param destination_project_Arn: The ARN of the project that you want to copy the model
    to.
    :param training_results: The Amazon S3 location where training results for the model
    should be stored.
    return: The model status and version.
    """
    try:
        logger.info("Copying model...%s from %s to %s ", source_project_version_arn,
                    source_project_arn,
                    destination_project_arn)

        output_bucket, output_folder = training_results.replace(
            "s3://", "").split("/", 1)
        output_config = {"S3Bucket": output_bucket,
                         "S3KeyPrefix": output_folder}

        response = rekognition_client.copy_project_version(
            DestinationProjectArn=destination_project_arn,
            OutputConfig=output_config,
            SourceProjectArn=source_project_arn,
            SourceProjectVersionArn=source_project_version_arn,
            VersionName=destination_version_name
        )

        destination_model_arn = response["ProjectVersionArn"]

        logger.info("Destination model ARN: %s", destination_model_arn)

        # Wait until training completes.
        finished = False
        status = "UNKNOWN"
        while finished is False:
            model_description = rekognition_client.describe_project_versions(ProjectArn=destination_project_arn,
                    VersionNames=[destination_version_name])
            status = model_description["ProjectVersionDescriptions"][0]["Status"]

            if status == "COPYING_IN_PROGRESS":
                logger.info("Model copying in progress...")
                time.sleep(60)
                continue

            if status == "COPYING_COMPLETED":
                logger.info("Model was successfully copied.")

            if status == "COPYING_FAILED":
                logger.info(
                    "Model copy failed: %s ",
                    model_description["ProjectVersionDescriptions"][0]["StatusMessage"])

            finished = True
    except ClientError:
        logger.exception("Couldn't copy model.")
        raise
    else:
        return destination_model_arn, status


def add_arguments(parser):
    """
    Adds command line arguments to the parser.
    :param parser: The command line parser.
    """

    parser.add_argument(
        "source_project_arn",
        help="The ARN of the project that contains the model that you want to copy."
    )

    parser.add_argument(
        "source_project_version_arn",
        help="The ARN of the model version that you want to copy."
    )

    parser.add_argument(
        "destination_project_arn",
        help="The ARN of the project which receives the copied model."
    )

    parser.add_argument(
        "destination_version_name",
        help="The version name for the model in the destination project."
    )

    parser.add_argument(
        "training_results",
        help="The S3 location in the destination account that receives the training results for the copied model."
    )


def main():

    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s: %(message)s")

    try:

        # get command line arguments
        parser = argparse.ArgumentParser(usage=argparse.SUPPRESS)
        add_arguments(parser)
        args = parser.parse_args()

        print(
            f"Copying model version {args.source_project_version_arn} to project {args.destination_project_arn}")

        session = boto3.Session(profile_name='custom-labels-access')
        rekognition_client = session.client("rekognition")

        # Copy the model.

        model_arn, status = copy_model(rekognition_client,
                                       args.source_project_arn,
                                       args.source_project_version_arn,
                                       args.destination_project_arn,
                                       args.training_results,
                                       args.destination_version_name,
                                       )

        print(f"Finished copying model: {model_arn}")
        print(f"Status: {status}")

    except ClientError as err:
        print(f"Problem copying model: {err}")


if __name__ == "__main__":
    main()

```

Java V2
Use the following code. Supply the following command line
parameters:

    * `source_project_arn` — the ARN of
     the source project in the source AWS account that
     contains the model version that you want to copy.
    * `source_project_version-arn` — the
     ARN of the model version in the source AWS account
     that that you want to copy.
    * `destination_project_arn` — the ARN
     of the destination project that you want to copy the
     model to.
    * `destination_version_name` — a
     version name for the model in the destination project.
    * `output_bucket` — the S3 bucket that
     you want the training results for the source model
     version copied to.
    * `output_folder` — the folder in the
     S3 that you want the training results for the source
     model version copied to.

```
/*
   Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
   SPDX-License-Identifier: Apache-2.0
*/

package com.example.rekognition;
import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.rekognition.RekognitionClient;
import software.amazon.awssdk.services.rekognition.model.CopyProjectVersionRequest;
import software.amazon.awssdk.services.rekognition.model.CopyProjectVersionResponse;
import software.amazon.awssdk.services.rekognition.model.DescribeProjectVersionsRequest;
import software.amazon.awssdk.services.rekognition.model.DescribeProjectVersionsResponse;
import software.amazon.awssdk.services.rekognition.model.OutputConfig;
import software.amazon.awssdk.services.rekognition.model.ProjectVersionDescription;

import software.amazon.awssdk.services.rekognition.model.RekognitionException;

import java.util.logging.Level;
import java.util.logging.Logger;

public class CopyModel {

    public static final Logger logger = Logger.getLogger(CopyModel.class.getName());

    public static ProjectVersionDescription copyMyModel(RekognitionClient rekClient,
            String sourceProjectArn,
            String sourceProjectVersionArn,
            String destinationProjectArn,
            String versionName,
            String outputBucket,
            String outputFolder) throws InterruptedException {

        try {

            OutputConfig outputConfig = OutputConfig.builder().s3Bucket(outputBucket).s3KeyPrefix(outputFolder).build();

            String[] logArguments = new String[] { versionName, sourceProjectArn, destinationProjectArn };

            logger.log(Level.INFO, "Copying model {0} for from project {1} to project {2}", logArguments);

            CopyProjectVersionRequest copyProjectVersionRequest = CopyProjectVersionRequest.builder()
                    .sourceProjectArn(sourceProjectArn)
                    .sourceProjectVersionArn(sourceProjectVersionArn)
                    .versionName(versionName)
                    .destinationProjectArn(destinationProjectArn)
                    .outputConfig(outputConfig)
                    .build();

            CopyProjectVersionResponse response = rekClient.copyProjectVersion(copyProjectVersionRequest);

            logger.log(Level.INFO, "Destination model ARN: {0}", response.projectVersionArn());
            logger.log(Level.INFO, "Copying model...");

            // wait until copying completes.

            boolean finished = false;

            ProjectVersionDescription copiedModel = null;

            while (Boolean.FALSE.equals(finished)) {
                DescribeProjectVersionsRequest describeProjectVersionsRequest = DescribeProjectVersionsRequest.builder()
                        .versionNames(versionName)
                        .projectArn(destinationProjectArn)
                        .build();

                DescribeProjectVersionsResponse describeProjectVersionsResponse = rekClient
                        .describeProjectVersions(describeProjectVersionsRequest);

                for (ProjectVersionDescription projectVersionDescription : describeProjectVersionsResponse
                        .projectVersionDescriptions()) {

                    copiedModel = projectVersionDescription;

                    switch (projectVersionDescription.status()) {

                        case COPYING_IN_PROGRESS:
                            logger.log(Level.INFO, "Copying model...");
                            Thread.sleep(5000);
                            continue;

                        case COPYING_COMPLETED:
                            finished = true;
                            logger.log(Level.INFO, "Copying completed");
                            break;

                        case COPYING_FAILED:
                            finished = true;
                            logger.log(Level.INFO, "Copying failed...");
                            break;

                        default:
                            finished = true;
                            logger.log(Level.INFO, "Unexpected copy status %s",
                                    projectVersionDescription.statusAsString());
                            break;

                    }

                }

            }

            logger.log(Level.INFO, "Finished copying model {0} for from project {1} to project {2}", logArguments);

            return copiedModel;

        } catch (RekognitionException e) {
            logger.log(Level.SEVERE, "Could not train model: {0}", e.getMessage());
            throw e;
        }

    }

    public static void main(String args[]) {

        String sourceProjectArn = null;
        String sourceProjectVersionArn = null;
        String destinationProjectArn = null;
        String versionName = null;
        String bucket = null;
        String location = null;

        final String USAGE = "\n" + "Usage: "
                + "<source_project_arn> <source_project_version_arn> <destination_project_arn> <version_name> <output_bucket> <output_folder>\n\n"
                + "Where:\n"
                + "   source_project_arn - The ARN of the project that contains the model that you want to copy. \n\n"
                + "   source_project_version_arn - The ARN of the project that contains the model that you want to copy. \n\n"
                + "   destination_project_arn - The ARN of the destination project that you want to copy the model to. \n\n"
                + "   version_name - A version name for the copied model.\n\n"
                + "   output_bucket - The S3 bucket in which to place the training output. \n\n"
                + "   output_folder - The folder within the bucket that the training output is stored in. \n\n";

        if (args.length != 6) {
            System.out.println(USAGE);
            System.exit(1);
        }

        sourceProjectArn = args[0];
        sourceProjectVersionArn = args[1];
        destinationProjectArn = args[2];
        versionName = args[3];
        bucket = args[4];
        location = args[5];

        try {

            // Get the Rekognition client.
            RekognitionClient rekClient = RekognitionClient.builder()
            .credentialsProvider(ProfileCredentialsProvider.create("custom-labels-access"))
            .region(Region.US_WEST_2)
            .build();

            // Copy the model.
            ProjectVersionDescription copiedModel = copyMyModel(rekClient,
                    sourceProjectArn,
                    sourceProjectVersionArn,
                    destinationProjectArn,
                    versionName,
                    bucket,
                    location);

            System.out.println(String.format("Model copied: %s Status: %s",
                    copiedModel.projectVersionArn(),
                    copiedModel.statusMessage()));

            rekClient.close();

        } catch (RekognitionException rekError) {
            logger.log(Level.SEVERE, "Rekognition client error: {0}", rekError.getMessage());
            System.exit(1);
        } catch (InterruptedException intError) {
            logger.log(Level.SEVERE, "Exception while sleeping: {0}", intError.getMessage());
            System.exit(1);
        }

    }

}

```
