# Creating a manifest file from a CSV

file

This example Python script simplifies the creation of a manifest file by
using a Comma Separated Values (CSV) file to label images. You create the
CSV file. The manifest file is suitable for [Multi-label image
classification](getting-started.md#gs-multi-label-image-classification-example "getting-started.md#gs-multi-label-image-classification-example") or [Multi-label image classification](getting-started.md#gs-multi-label-image-classification-example "getting-started.md#gs-multi-label-image-classification-example"). For more
information, see [Find objects, scenes, and concepts](understanding-custom-labels.md#tm-classification "understanding-custom-labels.md#tm-classification").

###### Note

This script doesn't create a manifest file suitable for finding [object locations](understanding-custom-labels.md#tm-object-localization "understanding-custom-labels.md#tm-object-localization") or for
finding [brand
locations](understanding-custom-labels.md#tm-brand-detection-localization "understanding-custom-labels.md#tm-brand-detection-localization").

A manifest file describes the images used to train a model. For example,
image locations and labels assigned to images. A manifest file is made up of
one or more JSON lines. Each JSON line describes a single image.

For more information, see [Importing
image-level labels in manifest files](md-create-manifest-file-classification.md "md-create-manifest-file-classification.md").

A CSV file represents tabular data over multiple rows in a text file.
Fields on a row are separated by commas. For more information, see [comma
separated values](https://en.wikipedia.org/wiki/Comma-separated_values "https://en.wikipedia.org/wiki/Comma-separated_values"). For this script, each row in your CSV file
represents a single image and maps to a JSON Line in the manifest file. To
create a CSV file for a manifest file that supports [Multi-label image
classification](getting-started.md#gs-multi-label-image-classification-example "getting-started.md#gs-multi-label-image-classification-example"), you add one or more image-level labels to each
row. To create a manifest file suitable for [Image classification](getting-started.md#gs-image-classification-example "getting-started.md#gs-image-classification-example"), you add a single
image-level label to each row.

For example, The following CSV file describes the images in the [Multi-label image classification](getting-started.md#gs-multi-label-image-classification-example "getting-started.md#gs-multi-label-image-classification-example") (Flowers)
_Getting started_ project.

```
camellia1.jpg,camellia,with_leaves
camellia2.jpg,camellia,with_leaves
camellia3.jpg,camellia,without_leaves
helleborus1.jpg,helleborus,without_leaves,not_fully_grown
helleborus2.jpg,helleborus,with_leaves,fully_grown
helleborus3.jpg,helleborus,with_leaves,fully_grown
jonquil1.jpg,jonquil,with_leaves
jonquil2.jpg,jonquil,with_leaves
jonquil3.jpg,jonquil,with_leaves
jonquil4.jpg,jonquil,without_leaves
mauve_honey_myrtle1.jpg,mauve_honey_myrtle,without_leaves
mauve_honey_myrtle2.jpg,mauve_honey_myrtle,with_leaves
mauve_honey_myrtle3.jpg,mauve_honey_myrtle,with_leaves
mediterranean_spurge1.jpg,mediterranean_spurge,with_leaves
mediterranean_spurge2.jpg,mediterranean_spurge,without_leaves

```

The script generates JSON Lines for each row. For example, the following
is the JSON Line for the first row
(`camellia1.jpg,camellia,with_leaves`) .

```
{"source-ref": "s3://bucket/flowers/train/camellia1.jpg","camellia": 1,"camellia-metadata":{"confidence": 1,"job-name": "labeling-job/camellia","class-name": "camellia","human-annotated": "yes","creation-date": "2022-01-21T14:21:05","type": "groundtruth/image-classification"},"with_leaves": 1,"with_leaves-metadata":{"confidence": 1,"job-name": "labeling-job/with_leaves","class-name": "with_leaves","human-annotated": "yes","creation-date": "2022-01-21T14:21:05","type": "groundtruth/image-classification"}}
```

In the example CSV, the Amazon S3 path to the image is not present. If your CSV
file doesn't include the Amazon S3 path for the images, use the
`--s3_path` command line argument to specify the Amazon S3 path to
the image.

The script records the first entry for each image in a deduplicated image
CSV file. The deduplicated image CSV file contains a single instance of each
image found in the input CSV file. Further occurrences of an image in the
input CSV file are recorded in a duplicate image CSV file. If the script
finds duplicate images, review the duplicate image CSV file and update the
deduplicated image CSV file as necessary. Rerun the script with the
deduplicated file. If no duplicates are found in the input CSV file, the
script deletes the deduplicated image CSV file and duplicate image CSVfile,
as they are empty.

In this procedure, you create the CSV file and run the Python script to
create the manifest
file.

###### To create a manifest file from a CSV file

1. Create a CSV file with the following fields in each row (one row
   per image). Don't add a header row to the CSV file.

| Field 1                                                                                                                                                                                               | Field 2                                       | Field n                                                                                                                                                                                                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| The image name or the Amazon S3 path the image. For<br>example,<br>`s3://my-bucket/flowers/train/camellia1.jpg`.<br>You can't have a mixture of images with the Amazon S3<br>path and images without. | The first image level label for the<br>image. | One or more additional image-level labels<br>separated by commas. Add only if you want to<br>create a manifest file that supports [Multi-label image classification](getting-started.md#gs-multi-label-image-classification-example "getting-started.md#gs-multi-label-image-classification-example"). |

For example `camellia1.jpg,camellia,with_leaves` or
`s3://my-bucket/flowers/train/camellia1.jpg,camellia,with_leaves` 2. Save the CSV file. 3. Run the following Python script. Supply the following
arguments:

    * `csv_file` – The CSV file that you
     created in step 1.
    * `manifest_file` – The name of the
     manifest file that you want to create.
    * (Optional)`--s3_path
     `s3://path_to_folder/``
     – The Amazon S3 path to add to the image file names (field
     1). Use `--s3_path` if the images in field 1
     don't already contain an S3 path.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier:  Apache-2.0

from datetime import datetime, timezone
import argparse
import logging
import csv
import os
import json

"""
Purpose
Amazon Rekognition Custom Labels model example used in the service documentation.
Shows how to create an image-level (classification) manifest file from a CSV file.
You can specify multiple image level labels per image.
CSV file format is
image,label,label,..
If necessary, use the bucket argument to specify the S3 bucket folder for the images.
https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-gt-cl-transform.html
"""

logger = logging.getLogger(__name__)


def check_duplicates(csv_file, deduplicated_file, duplicates_file):
    """
    Checks for duplicate images in a CSV file. If duplicate images
    are found, deduplicated_file is the deduplicated CSV file - only the first
    occurence of a duplicate is recorded. Other duplicates are recorded in duplicates_file.
    :param csv_file: The source CSV file.
    :param deduplicated_file: The deduplicated CSV file to create. If no duplicates are found
    this file is removed.
    :param duplicates_file: The duplicate images CSV file to create. If no duplicates are found
    this file is removed.
    :return: True if duplicates are found, otherwise false.
    """

    logger.info("Deduplicating %s", csv_file)

    duplicates_found = False

    # Find duplicates.
    with open(csv_file, 'r', newline='', encoding="UTF-8") as f,\
            open(deduplicated_file, 'w', encoding="UTF-8") as dedup,\
            open(duplicates_file, 'w', encoding="UTF-8") as duplicates:

        reader = csv.reader(f, delimiter=',')
        dedup_writer = csv.writer(dedup)
        duplicates_writer = csv.writer(duplicates)

        entries = set()
        for row in reader:
            # Skip empty lines.
            if not ''.join(row).strip():
                continue

            key = row[0]
            if key not in entries:
                dedup_writer.writerow(row)
                entries.add(key)
            else:
                duplicates_writer.writerow(row)
                duplicates_found = True

    if duplicates_found:
        logger.info("Duplicates found check %s", duplicates_file)

    else:
        os.remove(duplicates_file)
        os.remove(deduplicated_file)

    return duplicates_found


def create_manifest_file(csv_file, manifest_file, s3_path):
    """
    Reads a CSV file and creates a Custom Labels classification manifest file.
    :param csv_file: The source CSV file.
    :param manifest_file: The name of the manifest file to create.
    :param s3_path: The S3 path to the folder that contains the images.
    """
    logger.info("Processing CSV file %s", csv_file)

    image_count = 0
    label_count = 0

    with open(csv_file, newline='', encoding="UTF-8") as csvfile,\
            open(manifest_file, "w", encoding="UTF-8") as output_file:

        image_classifications = csv.reader(
            csvfile, delimiter=',', quotechar='|')

        # Process each row (image) in CSV file.
        for row in image_classifications:
            source_ref = str(s3_path)+row[0]

            image_count += 1

            # Create JSON for image source ref.
            json_line = {}
            json_line['source-ref'] = source_ref

            # Process each image level label.
            for index in range(1, len(row)):
                image_level_label = row[index]

                # Skip empty columns.
                if image_level_label == '':
                    continue
                label_count += 1

               # Create the JSON line metadata.
                json_line[image_level_label] = 1
                metadata = {}
                metadata['confidence'] = 1
                metadata['job-name'] = 'labeling-job/' + image_level_label
                metadata['class-name'] = image_level_label
                metadata['human-annotated'] = "yes"
                metadata['creation-date'] = \
                    datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')
                metadata['type'] = "groundtruth/image-classification"

                json_line[f'{image_level_label}-metadata'] = metadata

                # Write the image JSON Line.
            output_file.write(json.dumps(json_line))
            output_file.write('\n')

    output_file.close()
    logger.info("Finished creating manifest file %s\nImages: %s\nLabels: %s",
                manifest_file, image_count, label_count)

    return image_count, label_count


def add_arguments(parser):
    """
    Adds command line arguments to the parser.
    :param parser: The command line parser.
    """

    parser.add_argument(
        "csv_file", help="The CSV file that you want to process."
    )

    parser.add_argument(
        "--s3_path", help="The S3 bucket and folder path for the images."
        " If not supplied, column 1 is assumed to include the S3 path.", required=False
    )


def main():

    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s: %(message)s")

    try:

        # Get command line arguments
        parser = argparse.ArgumentParser(usage=argparse.SUPPRESS)
        add_arguments(parser)
        args = parser.parse_args()

        s3_path = args.s3_path
        if s3_path is None:
            s3_path = ''

        # Create file names.
        csv_file = args.csv_file
        file_name = os.path.splitext(csv_file)[0]
        manifest_file = f'{file_name}.manifest'
        duplicates_file = f'{file_name}-duplicates.csv'
        deduplicated_file = f'{file_name}-deduplicated.csv'

        # Create manifest file, if there are no duplicate images.
        if check_duplicates(csv_file, deduplicated_file, duplicates_file):
            print(f"Duplicates found. Use {duplicates_file} to view duplicates "
                  f"and then update {deduplicated_file}. ")
            print(f"{deduplicated_file} contains the first occurence of a duplicate. "
                  "Update as necessary with the correct label information.")
            print(f"Re-run the script with {deduplicated_file}")
        else:
            print("No duplicates found. Creating manifest file.")

            image_count, label_count = create_manifest_file(csv_file,
                                                            manifest_file,
                                                            s3_path)

            print(f"Finished creating manifest file: {manifest_file} \n"
                  f"Images: {image_count}\nLabels: {label_count}")

    except FileNotFoundError as err:
        logger.exception("File not found: %s", err)
        print(f"File not found: {err}. Check your input CSV file.")


if __name__ == "__main__":
    main()



```

4. If you plan to use a test dataset, repeat steps 1–3 to
   create a manifest file for your test dataset.
5. If necessary, copy the images to the Amazon S3 bucket path that you
   specified in column 1 of the CSV file (or specified in the
   `--s3_path` command line). You can use the following
   AWS S3 command.

```
aws s3 cp --recursive `your-local-folder` `s3://your-target-S3-location`
```

6. [Upload your manifest
   files](../../../AmazonS3/latest/userguide/upload-objects.md "../../../AmazonS3/latest/userguide/upload-objects.md") to the Amazon S3 bucket that you want to use for
   storing the manifest file.

###### Note

Make sure Amazon Rekognition Custom Labels has access to the Amazon S3 bucket referenced
in the `source-ref` field of the manifest file JSON
lines. For more information, see [Accessing external Amazon S3 Buckets](su-console-policy.md#su-external-buckets "su-console-policy.md#su-external-buckets"). If your Ground Truth
job stores images in the Amazon Rekognition Custom Labels Console Bucket, you don't
need to add permissions. 7. Follow the instructions at [Creating a dataset with
a SageMaker AI Ground Truth manifest file (Console)](md-create-dataset-ground-truth.md#md-create-dataset-ground-truth-console "md-create-dataset-ground-truth.md#md-create-dataset-ground-truth-console") to
create a dataset with the uploaded manifest file. For step 8, in
**.manifest file location**, enter the Amazon S3 URL
for the location of the manifest file. If you are using the AWS
SDK, do [Creating a dataset with a
SageMaker AI Ground Truth manifest file (SDK)](md-create-dataset-ground-truth.md#md-create-dataset-ground-truth-sdk "md-create-dataset-ground-truth.md#md-create-dataset-ground-truth-sdk").
