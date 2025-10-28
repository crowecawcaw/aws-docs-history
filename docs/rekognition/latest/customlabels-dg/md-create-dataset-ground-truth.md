# Using a manifest file to import

images

You can create a dataset using an Amazon SageMaker AI Ground Truth format manifest file. You
can use the manifest file from an Amazon SageMaker AI Ground Truth job. If your images and
labels aren't in the format of a SageMaker AI Ground Truth manifest file, you can create a
SageMaker AI format manifest file and use it to import your labeled images.

The `CreateDataset` operation is updated to allow you to optionally
specify tags when creating a new dataset. Tags are key-value pairs that you can use
to categorize and manage your resources.

###### Topics

- [Creating a dataset with
  a SageMaker AI Ground Truth manifest file (Console)](#md-create-dataset-ground-truth-console "#md-create-dataset-ground-truth-console")
- [Creating a dataset with a
  SageMaker AI Ground Truth manifest file (SDK)](#md-create-dataset-ground-truth-sdk "#md-create-dataset-ground-truth-sdk")
- [Create dataset request](#create-dataset-ground-truth-request "#create-dataset-ground-truth-request")
- [Labeling images with an Amazon SageMaker AI Ground Truth job](md-create-dataset-ground-truth-job.md "md-create-dataset-ground-truth-job.md")
- [Creating a manifest file](md-create-manifest-file.md "md-create-manifest-file.md")
- [Importing
  image-level labels in manifest files](md-create-manifest-file-classification.md "md-create-manifest-file-classification.md")
- [Object
  localization in manifest files](md-create-manifest-file-object-detection.md "md-create-manifest-file-object-detection.md")
- [Validation rules
  for manifest files](md-create-manifest-file-validation-rules.md "md-create-manifest-file-validation-rules.md")
- [Converting other dataset formats to a
  manifest file](md-converting-to-sm-format.md "md-converting-to-sm-format.md")

## Creating a dataset with

a SageMaker AI Ground Truth manifest file (Console)

The following procedure shows you how to create a dataset by using a SageMaker AI
Ground Truth format manifest file.

1.  Create a manifest file for your training dataset by doing one of the
    following:

        * Create a manifest file with a SageMaker AI GroundTruth Job by
         following the instructions at [Labeling images with an Amazon SageMaker AI Ground Truth job](md-create-dataset-ground-truth-job.md "md-create-dataset-ground-truth-job.md").
        * Create your own manifest file by following the instructions at
         [Creating a manifest file](md-create-manifest-file.md "md-create-manifest-file.md").

    If you want to create a test dataset, repeat step 1 to create the test
    dataset.

2.  Open the Amazon Rekognition console at
    [https://console.aws.amazon.com/rekognition/](https://console.aws.amazon.com/rekognition/ "https://console.aws.amazon.com/rekognition/").
3.  Choose **Use Custom Labels**.
4.  Choose **Get started**.
5.  In the left navigation pane, choose
    **Projects**.
6.  In the **Projects** page, choose the project to which
    you want to add a dataset. The details page for your project is
    displayed.
7.  Choose **Create dataset**. The **Create
    dataset** page is shown.
8.  In **Starting configuration**, choose either
    **Start with a single dataset** or **Start
    with a training dataset**. To create a higher quality
    model, we recommend starting with separate training and test
    datasets.

Single dataset

    1. In the **Training dataset
     details** section, choose
     **Import images labeled by SageMaker
     Ground Truth**.
    2. In **.manifest file location**
     enter the location of the manifest file that you
     created in step 1.
    3. Choose **Create Dataset**. The
     datasets page for your project opens.

Separate training and test datasets

    1. In the **Training dataset
     details** section, choose
     **Import images labeled by SageMaker
     Ground Truth**.
    2. In **.manifest file location**
     enter the location of the training dataset manifest
     file you created in step 1.
    3. In the **Test dataset details**
     section, choose **Import images labeled by
     SageMaker Ground Truth**.


    ###### Note

    Your training and test datasets can have
     different image sources.
    4. In **.manifest file location**
     enter the location of the test dataset manifest file
     you created in step 1.
    5. Choose **Create Datasets**. The
     datasets page for your project opens.

9. If you need to add or change labels, do [Labeling images](md-labeling-images.md "md-labeling-images.md").
10. Follow the steps in [Training a model (Console)](training-model.md#tm-console "training-model.md#tm-console") to train your model.

## Creating a dataset with a

SageMaker AI Ground Truth manifest file (SDK)

The following procedure shows you how to create training or test datasets from
a manifest file by using the [CreateDataset](../APIReference/API_CreateDataset.md "../APIReference/API_CreateDataset.md") API.

You can use an existing manifest file, such as the output from an [SageMaker AI Ground Truth job](md-create-dataset-ground-truth-job.md "md-create-dataset-ground-truth-job.md"),
or create your own [manifest file](md-create-manifest-file.md "md-create-manifest-file.md").

1.  If you haven't already done so, install and configure the AWS CLI and the AWS SDKs. For more information, see
    [Step 4: Set up the AWS CLI and AWS SDKs](su-awscli-sdk.md "su-awscli-sdk.md").
2.  Create a manifest file for your training dataset by doing one of the
    following:

        * Create a manifest file with a SageMaker AI GroundTruth Job by
         following the instructions at [Labeling images with an Amazon SageMaker AI Ground Truth job](md-create-dataset-ground-truth-job.md "md-create-dataset-ground-truth-job.md").
        * Create your own manifest file by following the instructions at
         [Creating a manifest file](md-create-manifest-file.md "md-create-manifest-file.md").

    If you want to create a test dataset, repeat step 2 to create the test
    dataset.

3.  Use the following example code to create the training and test
    dataset.

AWS CLI
Use the following code to create a dataset. Replace the
following:

    * `project_arn` — the ARN of the
     project that you want to add the test dataset
     to.
    * `type` — the type of dataset
     that you want to create (TRAIN or TEST)
    * `bucket` — the bucket that
     contains the manifest file for the dataset.
    * `manifest_file` — the path and
     file name of the manifest file.

```
aws rekognition create-dataset --project-arn `project_arn` \
  --dataset-type `type` \
  --dataset-source '{ "GroundTruthManifest": { "S3Object": { "Bucket": "`bucket`", "Name": "`manifest_file`" } } }' \
  --profile custom-labels-access
  --tags '{"key1": "value1", "key2": "value2"}'
```

Python
Use the following values to create a dataset. Supply the
following command line parameters:

    * `project_arn` — the ARN of the
     project that you want to add the test dataset
     to.
    * `dataset_type` — the type of
     dataset that you want to create (`train`
     or `test`).
    * `bucket` — the bucket that
     contains the manifest file for the dataset.
    * `manifest_file` — the path and
     file name of the manifest file.

```
#Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-custom-labels-developer-guide/blob/master/LICENSE-SAMPLECODE.)


import argparse
import logging
import time
import json
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

def create_dataset(rek_client, project_arn, dataset_type, bucket, manifest_file):
    """
    Creates an Amazon Rekognition Custom Labels dataset.
    :param rek_client: The Amazon Rekognition Custom Labels Boto3 client.
    :param project_arn: The ARN of the project in which you want to create a dataset.
    :param dataset_type: The type of the dataset that you want to create (train or test).
    :param bucket: The S3 bucket that contains the manifest file.
    :param manifest_file: The path and filename of the manifest file.
    """

    try:
        #Create the project
        logger.info("Creating %s dataset for project %s",dataset_type, project_arn)

        dataset_type = dataset_type.upper()

        dataset_source = json.loads(
            '{ "GroundTruthManifest": { "S3Object": { "Bucket": "'
            + bucket
            + '", "Name": "'
            + manifest_file
            + '" } } }'
        )

        response = rek_client.create_dataset(
            ProjectArn=project_arn, DatasetType=dataset_type, DatasetSource=dataset_source
        )

        dataset_arn=response['DatasetArn']

        logger.info("dataset ARN: %s",dataset_arn)

        finished=False
        while finished is False:

            dataset=rek_client.describe_dataset(DatasetArn=dataset_arn)

            status=dataset['DatasetDescription']['Status']

            if status == "CREATE_IN_PROGRESS":
                logger.info("Creating dataset: %s ",dataset_arn)
                time.sleep(5)
                continue

            if status == "CREATE_COMPLETE":
                logger.info("Dataset created: %s", dataset_arn)
                finished=True
                continue

            if status == "CREATE_FAILED":
                error_message = f"Dataset creation failed: {status} : {dataset_arn}"
                logger.exception(error_message)
                raise Exception (error_message)

            error_message = f"Failed. Unexpected state for dataset creation: {status} : {dataset_arn}"
            logger.exception(error_message)
            raise Exception(error_message)

        return dataset_arn


    except ClientError as err:
        logger.exception("Couldn't create dataset: %s",err.response['Error']['Message'])
        raise

def add_arguments(parser):
    """
    Adds command line arguments to the parser.
    :param parser: The command line parser.
    """

    parser.add_argument(
        "project_arn", help="The ARN of the project in which you want to create the dataset."
    )

    parser.add_argument(
        "dataset_type", help="The type of the dataset that you want to create (train or test)."
    )

    parser.add_argument(
        "bucket", help="The S3 bucket that contains the manifest file."
    )

    parser.add_argument(
        "manifest_file", help="The path and filename of the manifest file."
    )


def main():

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    try:

        #Get command line arguments.
        parser = argparse.ArgumentParser(usage=argparse.SUPPRESS)
        add_arguments(parser)
        args = parser.parse_args()

        print(f"Creating {args.dataset_type} dataset for project {args.project_arn}")

        #Create the dataset.
        session = boto3.Session(profile_name='custom-labels-access')
        rekognition_client = session.client("rekognition")

        dataset_arn=create_dataset(rekognition_client,
            args.project_arn,
            args.dataset_type,
            args.bucket,
            args.manifest_file)

        print(f"Finished creating dataset: {dataset_arn}")


    except ClientError as err:
        logger.exception("Problem creating dataset: %s", err)
        print(f"Problem creating dataset: {err}")



if __name__ == "__main__":
    main()

```

Java V2
Use the following values to create a dataset. Supply the
following command line parameters:

    * `project_arn` — the ARN of the
     project that you want to add the test dataset
     to.
    * `dataset_type` — the type of
     dataset that you want to create (`train`
     or `test`).
    * `bucket` — the bucket that
     contains the manifest file for the dataset.
    * `manifest_file` — the path and
     file name of the manifest file.

```
/*
   Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
   SPDX-License-Identifier: Apache-2.0
*/

package com.example.rekognition;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.rekognition.RekognitionClient;
import software.amazon.awssdk.services.rekognition.model.CreateDatasetRequest;
import software.amazon.awssdk.services.rekognition.model.CreateDatasetResponse;
import software.amazon.awssdk.services.rekognition.model.DatasetDescription;
import software.amazon.awssdk.services.rekognition.model.DatasetSource;
import software.amazon.awssdk.services.rekognition.model.DatasetStatus;
import software.amazon.awssdk.services.rekognition.model.DatasetType;
import software.amazon.awssdk.services.rekognition.model.DescribeDatasetRequest;
import software.amazon.awssdk.services.rekognition.model.DescribeDatasetResponse;
import software.amazon.awssdk.services.rekognition.model.GroundTruthManifest;
import software.amazon.awssdk.services.rekognition.model.RekognitionException;
import software.amazon.awssdk.services.rekognition.model.S3Object;

import java.util.logging.Level;
import java.util.logging.Logger;

public class CreateDatasetManifestFiles {

    public static final Logger logger = Logger.getLogger(CreateDatasetManifestFiles.class.getName());

    public static String createMyDataset(RekognitionClient rekClient, String projectArn, String datasetType,
            String bucket, String name) throws Exception, RekognitionException {

        try {

            logger.log(Level.INFO, "Creating {0} dataset for project : {1} from s3://{2}/{3} ",
                    new Object[] { datasetType, projectArn, bucket, name });

            DatasetType requestDatasetType = null;

            switch (datasetType) {
            case "train":
                requestDatasetType = DatasetType.TRAIN;
                break;
            case "test":
                requestDatasetType = DatasetType.TEST;
                break;
            default:
                logger.log(Level.SEVERE, "Could not create dataset. Unrecognized dataset type: {0}", datasetType);
                throw new Exception("Could not create dataset. Unrecognized dataset type: " + datasetType);

            }

            GroundTruthManifest groundTruthManifest = GroundTruthManifest.builder()
                    .s3Object(S3Object.builder().bucket(bucket).name(name).build()).build();

            DatasetSource datasetSource = DatasetSource.builder().groundTruthManifest(groundTruthManifest).build();

            CreateDatasetRequest createDatasetRequest = CreateDatasetRequest.builder().projectArn(projectArn)
                    .datasetType(requestDatasetType).datasetSource(datasetSource).build();

            CreateDatasetResponse response = rekClient.createDataset(createDatasetRequest);

            boolean created = false;

            do {

                DescribeDatasetRequest describeDatasetRequest = DescribeDatasetRequest.builder()
                        .datasetArn(response.datasetArn()).build();
                DescribeDatasetResponse describeDatasetResponse = rekClient.describeDataset(describeDatasetRequest);

                DatasetDescription datasetDescription = describeDatasetResponse.datasetDescription();

                DatasetStatus status = datasetDescription.status();

                logger.log(Level.INFO, "Creating dataset ARN: {0} ", response.datasetArn());

                switch (status) {

                case CREATE_COMPLETE:
                    logger.log(Level.INFO, "Dataset created");
                    created = true;
                    break;

                case CREATE_IN_PROGRESS:
                    Thread.sleep(5000);
                    break;

                case CREATE_FAILED:
                    String error = "Dataset creation failed: " + datasetDescription.statusAsString() + " "
                            + datasetDescription.statusMessage() + " " + response.datasetArn();
                    logger.log(Level.SEVERE, error);
                    throw new Exception(error);

                default:
                    String unexpectedError = "Unexpected creation state: " + datasetDescription.statusAsString() + " "
                            + datasetDescription.statusMessage() + " " + response.datasetArn();
                    logger.log(Level.SEVERE, unexpectedError);
                    throw new Exception(unexpectedError);
                }

            } while (created == false);

            return response.datasetArn();

        } catch (RekognitionException e) {
            logger.log(Level.SEVERE, "Could not create dataset: {0}", e.getMessage());
            throw e;
        }

    }

    public static void main(String[] args) {

        String datasetType = null;
        String bucket = null;
        String name = null;
        String projectArn = null;
        String datasetArn = null;

        final String USAGE = "\n" + "Usage: " + "<project_arn> <dataset_type> <dataset_arn>\n\n" + "Where:\n"
                + "   project_arn - the ARN of the project that you want to add copy the datast to.\n\n"
                + "   dataset_type - the type of the dataset that you want to create (train or test).\n\n"
                + "   bucket - the S3 bucket that contains the manifest file.\n\n"
                + "   name - the location and name of the manifest file within the bucket.\n\n";

        if (args.length != 4) {
            System.out.println(USAGE);
            System.exit(1);
        }

        projectArn = args[0];
        datasetType = args[1];
        bucket = args[2];
        name = args[3];

        try {

            // Get the Rekognition client
            RekognitionClient rekClient = RekognitionClient.builder()
                .credentialsProvider(ProfileCredentialsProvider.create("custom-labels-access"))
                .region(Region.US_WEST_2)
                .build();


             // Create the dataset
            datasetArn = createMyDataset(rekClient, projectArn, datasetType, bucket, name);

            System.out.println(String.format("Created dataset: %s", datasetArn));

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

4. If you need to add or change labels, see [Managing Labels (SDK)](md-labels.md#md-labels-sdk "md-labels.md#md-labels-sdk").
5. Follow the steps in [Training a model (SDK)](training-model.md#tm-sdk "training-model.md#tm-sdk") to
   train your model.

## Create dataset request

The following is the foramt of the CreateDataset operation request:

```

{
"DatasetSource": {
"DatasetArn": "string",
"GroundTruthManifest": {
"S3Object": {
"Bucket": "string",
"Name": "string",
"Version": "string"
}
}
},
"DatasetType": "string",
"ProjectArn": "string",
"Tags": {
"string": "string"
}
}

```
