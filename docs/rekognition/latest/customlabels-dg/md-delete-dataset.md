# Deleting a dataset

You can delete the training and test datasets from a project.

###### Topics

- [Deleting a dataset (Console)](#md-delete-dataset-console "#md-delete-dataset-console")
- [Deleting an Amazon Rekognition Custom Labels dataset
  (SDK)](#md-delete-dataset-sdk "#md-delete-dataset-sdk")

## Deleting a dataset (Console)

Use the following procedure to delete a dataset. Afterwards, if the project has
one remaining dataset (train or test), the project details page is shown. If the
project has no remaining datasets, the **Create dataset** page is
shown.

If you delete the training dataset, you must create a new training dataset for the
project before you can train a model. For more information, see [Creating training and test datasets with images](md-create-dataset.md "md-create-dataset.md").

If you delete the test dataset, you can train a model without creating a new test
dataset. During training, the training dataset is split to create a new test dataset
for the project. Splitting the training dataset reduces the number of images
available for training. To maintain quality, we recommend creating a new test
dataset before training a model. For more information, see [Adding a dataset to a project](md-add-dataset.md "md-add-dataset.md").

###### To delete a dataset

1. Open the Amazon Rekognition console at
   [https://console.aws.amazon.com/rekognition/](https://console.aws.amazon.com/rekognition/ "https://console.aws.amazon.com/rekognition/").
2. In the left pane, choose Use **Custom Labels**. The
   Amazon Rekognition Custom Labels landing page is shown.
3. In the left navigation pane, choose **Projects**. The
   Projects view is shown.
4. Choose the project that contains the dataset that you want to delete.
5. In the left navigation pane, under the project name, choose
   **Dataset**
6. Choose **Actions**
7. To delete the training dataset, choose **Delete training
   dataset.**
8. To delete the test dataset, choose **Delete test
   dataset.**
9. In the **Delete _train or test_
   dataset** dialog box, enter **delete** to
   confirm that you want to delete the dataset.
10. Choose **Delete _train or test_
    dataset** to delete the dataset.

## Deleting an Amazon Rekognition Custom Labels dataset

(SDK)

You delete an Amazon Rekognition Custom Labels dataset by calling [DeleteDataset](../APIReference/API_DeleteDataset.md "../APIReference/API_DeleteDataset.md") and supplying the
Amazon Resource Name (ARN) of the dataset that you want to delete. To get the ARNs
of the training and test datasets within a project, call [DescribeProjects](../APIReference/API_DescribeProjects.md "../APIReference/API_DescribeProjects.md"). The response
includes an array of [ProjectDescription](../APIReference/API_ProjectDescription.md "../APIReference/API_ProjectDescription.md") objects. The dataset ARNs (`DatasetArn`)
and dataset types (`DatasetType`) are in the `Datasets` list.

If you delete the training dataset, you need to create a new training dataset for
the project before you can train a model. If you delete the test dataset, you need
to create a new test dataset before you can train the model. For more information,
see [Adding a dataset to a project (SDK)](md-add-dataset.md#md-add-dataset-sdk "md-add-dataset.md#md-add-dataset-sdk").

###### To delete a dataset (SDK)

1. If you haven't already done so, install and configure the AWS CLI and the AWS SDKs. For more information, see
   [Step 4: Set up the AWS CLI and AWS SDKs](su-awscli-sdk.md "su-awscli-sdk.md").
2. Use the following code to delete a dataset.

AWS CLI
Change the value of `dataset-arn` with the ARN of
the dataset that you want to delete.

```
aws rekognition delete-dataset --dataset-arn `dataset-arn` \
  --profile custom-labels-access
```

Python
Use the following code. Supply the following command line
parameters:

    * dataset\_arn — the ARN of the
     dataset that you want to delete.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Purpose
Shows how to delete an Amazon Rekognition Custom Labels dataset.
"""
import argparse
import logging
import time
import boto3

from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


def delete_dataset(rek_client, dataset_arn):
    """
    Deletes an Amazon Rekognition Custom Labels dataset.
    :param rek_client: The Amazon Rekognition Custom Labels Boto3 client.
    :param dataset_arn: The ARN of the dataset that you want to delete.
    """

    try:
        # Delete the dataset,
        logger.info("Deleting dataset: %s", dataset_arn)

        rek_client.delete_dataset(DatasetArn=dataset_arn)

        deleted = False

        logger.info("waiting for dataset deletion %s", dataset_arn)

        # Dataset might not be deleted yet, so wait.
        while deleted is False:
            try:
                rek_client.describe_dataset(DatasetArn=dataset_arn)
                time.sleep(5)
            except ClientError as err:
                if err.response['Error']['Code'] == 'ResourceNotFoundException':
                    logger.info("dataset deleted: %s", dataset_arn)
                    deleted = True
                else:
                    raise

        logger.info("dataset deleted: %s", dataset_arn)

        return True

    except ClientError as err:
        logger.exception("Couldn't delete dataset - %s: %s",
                         dataset_arn, err.response['Error']['Message'])
        raise


def add_arguments(parser):
    """
    Adds command line arguments to the parser.
    :param parser: The command line parser.
    """

    parser.add_argument(
        "dataset_arn", help="The ARN of the dataset that you want to delete."
    )


def main():

    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s: %(message)s")

    try:

        # Get command line arguments.
        parser = argparse.ArgumentParser(usage=argparse.SUPPRESS)
        add_arguments(parser)
        args = parser.parse_args()

        print(f"Deleting dataset: {args.dataset_arn}")

        # Delete the dataset.
        session = boto3.Session(profile_name='custom-labels-access')
        rekognition_client = session.client("rekognition")

        delete_dataset(rekognition_client,
                       args.dataset_arn)

        print(f"Finished deleting dataset: {args.dataset_arn}")

    except ClientError as err:
        error_message = f"Problem deleting dataset: {err}"
        logger.exception(error_message)
        print(error_message)


if __name__ == "__main__":
    main()

```

Java V2
Use the following code. Supply the following command line
parameters:

    * dataset\_arn — the ARN of the
     dataset that you want to delete.

```
/*
   Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
   SPDX-License-Identifier: Apache-2.0
*/
package com.example.rekognition;

import java.util.logging.Level;
import java.util.logging.Logger;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.rekognition.RekognitionClient;
import software.amazon.awssdk.services.rekognition.model.DeleteDatasetRequest;
import software.amazon.awssdk.services.rekognition.model.DeleteDatasetResponse;
import software.amazon.awssdk.services.rekognition.model.DescribeDatasetRequest;
import software.amazon.awssdk.services.rekognition.model.RekognitionException;

public class DeleteDataset {

    public static final Logger logger = Logger.getLogger(DeleteDataset.class.getName());

    public static void deleteMyDataset(RekognitionClient rekClient, String datasetArn) throws InterruptedException {

        try {

            logger.log(Level.INFO, "Deleting dataset: {0}", datasetArn);

            // Delete the dataset

            DeleteDatasetRequest deleteDatasetRequest = DeleteDatasetRequest.builder().datasetArn(datasetArn).build();

            DeleteDatasetResponse response = rekClient.deleteDataset(deleteDatasetRequest);

            // Wait until deletion finishes

            DescribeDatasetRequest describeDatasetRequest = DescribeDatasetRequest.builder().datasetArn(datasetArn)
                    .build();

            Boolean deleted = false;

            do {

                try {

                    rekClient.describeDataset(describeDatasetRequest);
                    Thread.sleep(5000);
                } catch (RekognitionException e) {
                    String errorCode = e.awsErrorDetails().errorCode();
                    if (errorCode.equals("ResourceNotFoundException")) {
                        logger.log(Level.INFO, "Dataset deleted: {0}", datasetArn);
                        deleted = true;
                    } else {
                        logger.log(Level.SEVERE, "Client error occurred: {0}", e.getMessage());
                        throw e;
                    }

                }

            } while (Boolean.FALSE.equals(deleted));

            logger.log(Level.INFO, "Dataset deleted: {0} ", datasetArn);

        } catch (

        RekognitionException e) {
            logger.log(Level.SEVERE, "Client error occurred: {0}", e.getMessage());
            throw e;
        }

    }

    public static void main(String args[]) {

        final String USAGE = "\n" + "Usage: " + "<dataset_arn>\n\n" + "Where:\n"
                + "   dataset_arn - The ARN of the dataset that you want to delete.\n\n";

        if (args.length != 1) {
            System.out.println(USAGE);
            System.exit(1);
        }

        String datasetArn = args[0];

        try {

            // Get the Rekognition client.
            RekognitionClient rekClient = RekognitionClient.builder()
                .credentialsProvider(ProfileCredentialsProvider.create("custom-labels-access"))
                .region(Region.US_WEST_2)
                .build();


            // Delete the dataset
            deleteMyDataset(rekClient, datasetArn);

            System.out.println(String.format("Dataset deleted: %s", datasetArn));

            rekClient.close();

        } catch (RekognitionException rekError) {
            logger.log(Level.SEVERE, "Rekognition client error: {0}", rekError.getMessage());
            System.exit(1);
        }

        catch (InterruptedException intError) {
            logger.log(Level.SEVERE, "Exception while sleeping: {0}", intError.getMessage());
            System.exit(1);
        }

    }

}

```
