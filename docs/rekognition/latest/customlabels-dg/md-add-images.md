# Adding more images to a dataset

You can add more images to your datasets by using the Amazon Rekognition Custom Labels console or by the
calling the `UpdateDatasetEntries` API.

###### Topics

- [Adding more images (console)](#md-add-images-console "#md-add-images-console")
- [Adding more images (SDK)](#md-add-images-sdk "#md-add-images-sdk")

## Adding more images (console)

When you use the Amazon Rekognition Custom Labels console, you upload images from your local computer.
The images are added to the Amazon S3 bucket location (console or external) where the
images used to create the dataset are stored.

###### To add more images to your dataset (console)

1. Open the Amazon Rekognition console at
   [https://console.aws.amazon.com/rekognition/](https://console.aws.amazon.com/rekognition/ "https://console.aws.amazon.com/rekognition/").
2. In the left pane, choose Use **Custom Labels**. The
   Amazon Rekognition Custom Labels landing page is shown.
3. In the left navigation pane, choose **Projects**. The
   Projects view is shown.
4. Choose the project that you want to use.
5. In the left navigation pane, under the project name, choose
   **Dataset**.
6. Choose **Actions** and select the dataset that you want
   to add images to.
7. Choose the images you want to upload to the dataset. You can drag the
   images or choose the images that you want to upload from your local
   computer. You can upload up to 30 images at a time.
8. Choose **Upload images**.
9. Choose **Save changes**.
10. Label the images. For more information, see [Labeling images](md-labeling-images.md "md-labeling-images.md").

## Adding more images (SDK)

`UpdateDatasetEntries` updates or adds JSON lines to a manifest file.
You pass the JSON lines as a byte64 encoded data object in the
`GroundTruth`field. If you are using an AWS SDK to call
`UpdateDatasetEntries`, the SDK encodes the data for you. Each JSON
line contains information for a single image, such as assigned labels or bounding
box information. For example:

```
{"source-ref":"s3://bucket/image","BB":{"annotations":[{"left":1849,"top":1039,"width":422,"height":283,"class_id":0},{"left":1849,"top":1340,"width":443,"height":415,"class_id":1},{"left":2637,"top":1380,"width":676,"height":338,"class_id":2},{"left":2634,"top":1051,"width":673,"height":338,"class_id":3}],"image_size":[{"width":4000,"height":2667,"depth":3}]},"BB-metadata":{"job-name":"labeling-job/BB","class-map":{"0":"comparator","1":"pot_resistor","2":"ir_phototransistor","3":"ir_led"},"human-annotated":"yes","objects":[{"confidence":1},{"confidence":1},{"confidence":1},{"confidence":1}],"creation-date":"2021-06-22T10:11:18.006Z","type":"groundtruth/object-detection"}}

```

For more information, see [Creating a manifest file](md-create-manifest-file.md "md-create-manifest-file.md").

Use `source-ref` field as a key to identify images that you want to
update. If the dataset doesn't contain a matching `source-ref` field
value, the JSON line is added as a new image.

###### To add more images to a dataset (SDK)

1. If you haven't already done so, install and configure the AWS CLI and the AWS SDKs. For more information, see
   [Step 4: Set up the AWS CLI and AWS SDKs](su-awscli-sdk.md "su-awscli-sdk.md").
2. Use the following examples to add JSON lines to a dataset.

CLI
Replace the value of `GroundTruth` with the JSON
Lines that you want to use. You need to escape any special
characters within the JSON Line.

```
aws rekognition update-dataset-entries\
  --dataset-arn `dataset_arn` \
  --changes '{"GroundTruth" : "`{\"source-ref\":\"s3://your_bucket/your_image\",\"BB\":{\"annotations\":[{\"left\":1776,\"top\":1017,\"width\":458,\"height\":317,\"class_id\":0},{\"left\":1797,\"top\":1334,\"width\":418,\"height\":415,\"class_id\":1},{\"left\":2597,\"top\":1361,\"width\":655,\"height\":329,\"class_id\":2},{\"left\":2581,\"top\":1020,\"width\":689,\"height\":338,\"class_id\":3}],\"image_size\":[{\"width\":4000,\"height\":2667,\"depth\":3}]},\"BB-metadata\":{\"job-name\":\"labeling-job/BB\",\"class-map\":{\"0\":\"comparator\",\"1\":\"pot_resistor\",\"2\":\"ir_phototransistor\",\"3\":\"ir_led\"},\"human-annotated\":\"yes\",\"objects\":[{\"confidence\":1},{\"confidence\":1},{\"confidence\":1},{\"confidence\":1}],\"creation-date\":\"2021-06-22T10:10:48.492Z\",\"type\":\"groundtruth/object-detection\"}}"` }' \
  --cli-binary-format raw-in-base64-out \
  --profile custom-labels-access
```

Python
Use the following code. Supply the following command line parameters:

    * dataset\_arn— the ARN of the dataset that you want to update.
    * updates\_file— the file that contains the JSON Line updates.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Purpose
Shows how to add entries to an Amazon Rekognition Custom Labels dataset.
"""

import argparse
import logging
import time
import json
import boto3

from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

def update_dataset_entries(rek_client, dataset_arn, updates_file):
    """
    Adds dataset entries to an Amazon Rekognition Custom Labels dataset.
    :param rek_client: The Amazon Rekognition Custom Labels Boto3 client.
    :param dataset_arn: The ARN of the dataset that yuo want to update.
    :param updates_file: The manifest file of JSON Lines that contains the updates.
    """

    try:
        status=""
        status_message=""

        # Update dataset entries.
        logger.info("Updating dataset %s", dataset_arn)


        with open(updates_file) as f:
            manifest_file = f.read()


        changes=json.loads('{ "GroundTruth" : ' +
            json.dumps(manifest_file) +
            '}')

        rek_client.update_dataset_entries(
            Changes=changes, DatasetArn=dataset_arn
        )

        finished=False
        while finished is False:

            dataset=rek_client.describe_dataset(DatasetArn=dataset_arn)

            status=dataset['DatasetDescription']['Status']
            status_message=dataset['DatasetDescription']['StatusMessage']

            if status == "UPDATE_IN_PROGRESS":

                logger.info("Updating dataset: %s ", dataset_arn)
                time.sleep(5)
                continue

            if status == "UPDATE_COMPLETE":
                logger.info("Dataset updated: %s : %s : %s",
                    status, status_message, dataset_arn)
                finished=True
                continue

            if status == "UPDATE_FAILED":
                error_message = f"Dataset update failed: {status} : {status_message} : {dataset_arn}"
                logger.exception(error_message)
                raise Exception (error_message)

            error_message = f"Failed. Unexpected state for dataset update: {status} : {status_message} : {dataset_arn}"
            logger.exception(error_message)
            raise Exception(error_message)

        logger.info("Added entries to dataset")

        return status, status_message


    except ClientError as err:
        logger.exception("Couldn't update dataset: %s", err.response['Error']['Message'])
        raise

def add_arguments(parser):
    """
    Adds command line arguments to the parser.
    :param parser: The command line parser.
    """

    parser.add_argument(
        "dataset_arn", help="The ARN of the dataset that you want to update."
    )

    parser.add_argument(
        "updates_file", help="The manifest file of JSON Lines that contains the updates."
    )

def main():

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    try:

        #get command line arguments
        parser = argparse.ArgumentParser(usage=argparse.SUPPRESS)
        add_arguments(parser)
        args = parser.parse_args()

        print(f"Updating dataset {args.dataset_arn} with entries from {args.updates_file}.")

        # Update the dataset.
        session = boto3.Session(profile_name='custom-labels-access')
        rekognition_client = session.client("rekognition")

        status, status_message=update_dataset_entries(rekognition_client,
            args.dataset_arn,
            args.updates_file)

        print(f"Finished updates dataset: {status} : {status_message}")


    except ClientError as err:
        logger.exception("Problem updating dataset: %s", err)
        print(f"Problem updating dataset: {err}")

    except Exception as err:
        logger.exception("Problem updating dataset: %s", err)
        print(f"Problem updating dataset: {err}")


if __name__ == "__main__":
    main()

```

Java V2

    * dataset\_arn— the ARN of the dataset that you want to update.
    * update\_file— the file that contains the JSON Line updates.

```
/*
   Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
   SPDX-License-Identifier: Apache-2.0
*/
package com.example.rekognition;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.core.SdkBytes;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.rekognition.RekognitionClient;
import software.amazon.awssdk.services.rekognition.model.DatasetChanges;
import software.amazon.awssdk.services.rekognition.model.DatasetDescription;
import software.amazon.awssdk.services.rekognition.model.DatasetStatus;
import software.amazon.awssdk.services.rekognition.model.DescribeDatasetRequest;
import software.amazon.awssdk.services.rekognition.model.DescribeDatasetResponse;
import software.amazon.awssdk.services.rekognition.model.RekognitionException;
import software.amazon.awssdk.services.rekognition.model.UpdateDatasetEntriesRequest;
import software.amazon.awssdk.services.rekognition.model.UpdateDatasetEntriesResponse;

import java.io.FileInputStream;
import java.io.InputStream;
import java.util.logging.Level;
import java.util.logging.Logger;

public class UpdateDatasetEntries {

    public static final Logger logger = Logger.getLogger(UpdateDatasetEntries.class.getName());

    public static String updateMyDataset(RekognitionClient rekClient, String datasetArn,
            String updateFile
            ) throws Exception, RekognitionException {

        try {

            logger.log(Level.INFO, "Updating dataset {0}",
                    new Object[] { datasetArn});


            InputStream sourceStream = new FileInputStream(updateFile);
            SdkBytes sourceBytes = SdkBytes.fromInputStream(sourceStream);

            DatasetChanges datasetChanges = DatasetChanges.builder()
                    .groundTruth(sourceBytes).build();

            UpdateDatasetEntriesRequest updateDatasetEntriesRequest = UpdateDatasetEntriesRequest.builder()
                    .changes(datasetChanges)
                    .datasetArn(datasetArn)
                    .build();

            UpdateDatasetEntriesResponse response = rekClient.updateDatasetEntries(updateDatasetEntriesRequest);

            boolean updated = false;

            //Wait until update completes

            do {

                DescribeDatasetRequest describeDatasetRequest = DescribeDatasetRequest.builder()
                        .datasetArn(datasetArn).build();
                DescribeDatasetResponse describeDatasetResponse = rekClient.describeDataset(describeDatasetRequest);

                DatasetDescription datasetDescription = describeDatasetResponse.datasetDescription();

                DatasetStatus status = datasetDescription.status();

                logger.log(Level.INFO, " dataset ARN: {0} ", datasetArn);

                switch (status) {

                case UPDATE_COMPLETE:
                    logger.log(Level.INFO, "Dataset updated");
                    updated = true;
                    break;

                case UPDATE_IN_PROGRESS:
                    Thread.sleep(5000);
                    break;

                case UPDATE_FAILED:
                    String error = "Dataset update failed: " + datasetDescription.statusAsString() + " "
                            + datasetDescription.statusMessage() + " " + datasetArn;
                    logger.log(Level.SEVERE, error);
                    throw new Exception(error);

                default:
                    String unexpectedError = "Unexpected update state: " + datasetDescription.statusAsString() + " "
                            + datasetDescription.statusMessage() + " " + datasetArn;
                    logger.log(Level.SEVERE, unexpectedError);
                    throw new Exception(unexpectedError);
                }

            } while (updated == false);

            return datasetArn;

        } catch (RekognitionException e) {
            logger.log(Level.SEVERE, "Could not update dataset: {0}", e.getMessage());
            throw e;
        }

    }

    public static void main(String args[]) {

        String updatesFile = null;
        String datasetArn = null;


        final String USAGE = "\n" + "Usage: " + "<project_arn> <dataset_arn> <updates_file>\n\n" + "Where:\n"
                + "   dataset_arn - the ARN of the dataset that you want to update.\n\n"
                + "   update_file - The file that includes in JSON Line updates.\n\n";

        if (args.length != 2) {
            System.out.println(USAGE);
            System.exit(1);
        }

        datasetArn = args[0];
        updatesFile = args[1];


        try {

            // Get the Rekognition client.
            RekognitionClient rekClient = RekognitionClient.builder()
                .credentialsProvider(ProfileCredentialsProvider.create("custom-labels-access"))
                .region(Region.US_WEST_2)
                .build();

             // Update the dataset
            datasetArn = updateMyDataset(rekClient, datasetArn, updatesFile);

            System.out.println(String.format("Dataset updated: %s", datasetArn));

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
