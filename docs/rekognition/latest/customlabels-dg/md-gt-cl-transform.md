# Transforming multi-label SageMaker AI Ground Truth

manifest files

This topic shows you how to transform a multi-label Amazon SageMaker AI Ground Truth
manifest file to an Amazon Rekognition Custom Labels format manifest file.

SageMaker AI Ground Truth manifest files for multi-label jobs are formatted
differently than Amazon Rekognition Custom Labels format manifest files. Multi-label
classification is when an image is classified into a set of classes, but
might belong to multiple classes at once. In this case, the image can
potentially have multiple labels (multi-label), such as
_football_ and _ball_.

For information about multi-label SageMaker AI Ground Truth jobs, see [Image Classification (Multi-label)](../../../sagemaker/latest/dg/sms-image-classification-multilabel.md "../../../sagemaker/latest/dg/sms-image-classification-multilabel.md"). For information about
multi-label format Amazon Rekognition Custom Labels manifest files, see [Adding multiple image-level labels to an image](md-create-manifest-file-classification.md#md-dataset-purpose-classification-multiple-labels "md-create-manifest-file-classification.md#md-dataset-purpose-classification-multiple-labels").

## Getting the manifest file for a

SageMaker AI Ground Truth job

The following procedure shows you how to get the output manifest file
(`output.manifest`) for an Amazon SageMaker AI Ground Truth
job. You use `output.manifest` as input to the next
procedure.

###### To download a SageMaker AI Ground Truth job manifest file

1. Open the [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. In the navigation pane, choose **Ground
   Truth** and then choose **Labeling
   Jobs**.
3. Choose the labeling job that contains the manifest file that
   you want to use.
4. On the details page, choose the link under **Output
   dataset location**. The Amazon S3 console is opened at
   the dataset location.
5. Choose `Manifests`,
   `output` and then
   `output.manifest`.
6. Choose **Object Actions** and then choose
   **Download** to download the manifest
   file.

## Transforming a multi-label SageMaker AI

manifest file

The following procedure creates a multi-label format Amazon Rekognition Custom Labels
manifest file from an existing multi-label format SageMaker AI GroundTruth
manifest file.

###### Note

To run the code, you need Python version 3, or higher.

###### To transform a

multi-label SageMaker AI manifest file

1. Run the following python code. Supply the name of the manifest
   file that you created in [Getting the manifest file for a
   SageMaker AI Ground Truth job](#md-get-gt-manifest "#md-get-gt-manifest") as a command line
   argument.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier:  Apache-2.0
"""
Purpose
Shows how to create and Amazon Rekognition Custom Labels format
manifest file from an Amazon SageMaker Ground Truth Image
Classification (Multi-label) format manifest file.
"""
import json
import logging
import argparse
import os.path

logger = logging.getLogger(__name__)

def create_manifest_file(ground_truth_manifest_file):
    """
    Creates an Amazon Rekognition Custom Labels format manifest file from
    an Amazon SageMaker Ground Truth Image Classification (Multi-label) format
    manifest file.
    :param: ground_truth_manifest_file: The name of the Ground Truth manifest file,
    including the relative path.
    :return: The name of the new Custom Labels manifest file.
    """

    logger.info('Creating manifest file from %s', ground_truth_manifest_file)
    new_manifest_file = f'custom_labels_{os.path.basename(ground_truth_manifest_file)}'

    # Read the SageMaker Ground Truth manifest file into memory.
    with open(ground_truth_manifest_file) as gt_file:
        lines = gt_file.readlines()

    #Iterate through the lines one at a time to generate the
    #new lines for the Custom Labels manifest file.
    with open(new_manifest_file, 'w') as the_new_file:
        for line in lines:
            #job_name - The of the Amazon Sagemaker Ground Truth job.
            job_name = ''
            # Load in the old json item from the Ground Truth manifest file
            old_json = json.loads(line)

            # Get the job name
            keys = old_json.keys()
            for key in keys:
                if 'source-ref' not in key and '-metadata' not in key:
                    job_name = key

            new_json = {}
            # Set the location of the image
            new_json['source-ref'] = old_json['source-ref']

            # Temporarily store the list of labels
            labels = old_json[job_name]

            # Iterate through the labels and reformat to Custom Labels format
            for index, label in enumerate(labels):
                new_json[f'{job_name}{index}'] = index
                metadata = {}
                metadata['class-name'] = old_json[f'{job_name}-metadata']['class-map'][str(label)]
                metadata['confidence'] = old_json[f'{job_name}-metadata']['confidence-map'][str(label)]
                metadata['type'] = 'groundtruth/image-classification'
                metadata['job-name'] = old_json[f'{job_name}-metadata']['job-name']
                metadata['human-annotated'] = old_json[f'{job_name}-metadata']['human-annotated']
                metadata['creation-date'] = old_json[f'{job_name}-metadata']['creation-date']
                # Add the metadata to new json line
                new_json[f'{job_name}{index}-metadata'] = metadata
            # Write the current line to the json file
            the_new_file.write(json.dumps(new_json))
            the_new_file.write('\n')

    logger.info('Created %s', new_manifest_file)
    return  new_manifest_file

def add_arguments(parser):
    """
    Adds command line arguments to the parser.
    :param parser: The command line parser.
    """

    parser.add_argument(
        "manifest_file", help="The Amazon SageMaker Ground Truth manifest file"
        "that you want to use."
    )


def main():
    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s: %(message)s")
    try:
        # get command line arguments
        parser = argparse.ArgumentParser(usage=argparse.SUPPRESS)
        add_arguments(parser)
        args = parser.parse_args()
        # Create the manifest file
        manifest_file = create_manifest_file(args.manifest_file)
        print(f'Manifest file created: {manifest_file}')
    except FileNotFoundError as err:
        logger.exception('File not found: %s', err)
        print(f'File not found: {err}. Check your manifest file.')

if __name__ == "__main__":
    main()

```

2. Note the name of the new manifest file that the script
   displays. You use it in the next step.
3. [Upload your
   manifest files](../../../AmazonS3/latest/userguide/upload-objects.md "../../../AmazonS3/latest/userguide/upload-objects.md") to the Amazon S3 bucket that you want to
   use for storing the manifest file.

###### Note

Make sure Amazon Rekognition Custom Labels has access to the Amazon S3 bucket
referenced in the `source-ref` field of the
manifest file JSON lines. For more information, see [Accessing external Amazon S3 Buckets](su-console-policy.md#su-external-buckets "su-console-policy.md#su-external-buckets"). If your Ground
Truth job stores images in the Amazon Rekognition Custom Labels Console Bucket,
you don't need to add permissions. 4. Follow the instructions at [Creating a dataset with
a SageMaker AI Ground Truth manifest file (Console)](md-create-dataset-ground-truth.md#md-create-dataset-ground-truth-console "md-create-dataset-ground-truth.md#md-create-dataset-ground-truth-console") to
create a dataset with the uploaded manifest file. For step 8, in
**.manifest file location**, enter the Amazon S3
URL for the location of the manifest file. If you are using the
AWS SDK, do [Creating a dataset with a
SageMaker AI Ground Truth manifest file (SDK)](md-create-dataset-ground-truth.md#md-create-dataset-ground-truth-sdk "md-create-dataset-ground-truth.md#md-create-dataset-ground-truth-sdk").
