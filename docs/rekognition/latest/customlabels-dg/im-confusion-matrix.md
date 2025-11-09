# Viewing the confusion matrix for a

model

A confusion matrix allows you to see the labels that your model confuses with
other labels in your model. By using a confusion matrix, you can focus your
improvements to the model.

During model evaluation, Amazon Rekognition Custom Labels create a confusion matrix by using the test
images to identify mis-identified (confused) labels. Amazon Rekognition Custom Labels only creates a
confusion matrix for classification models. The classification matrix is accessible
from the summary file that Amazon Rekognition Custom Labels creates during model training. You can't view
the confusion matrix in the Amazon Rekognition Custom Labels console.

###### Topics

- [Using a confusion matrix](#im-using-confusion-matrix "#im-using-confusion-matrix")
- [Getting the confusion matrix for a model](#im-getting-confusion-matrix "#im-getting-confusion-matrix")

## Using a confusion matrix

The following table is the confusion matrix for the [Rooms image classification](getting-started.md#gs-image-classification-example "getting-started.md#gs-image-classification-example")
example project. Column headings are the labels (ground truth labels) assigned
to the test images. Row headings are the labels that the model predicts for the
test images. Each cell is the percentage of predictions for a label (row) that
should be the ground truth label (column). For example, 67% of the predictions
for bathrooms were correctly labeled as bathrooms. 33% percent of bathrooms were
incorrectly labeled as kitchens. A high performing model has high cell values
when the predicted label matches the ground truth label. You can see these as a
diagonal line from the first to last predicted and ground truth labels. If a
cell value is 0, no predictions were made for the cell's predicted label that
should be the cell's ground truth label.

###### Note

Since models are non-deterministic, the confusion matrix cell values you
get from training the Rooms project might differ from the following table.

The confusion matrix identifies areas to focus on. For example, the confusion
matrix shows that 50% of the time the model confused closets for bedrooms. In
this situation, you should add more images of closets and bedrooms to your
training dataset. Also check that the existing closet and bedroom images are
correctly labeled. This should help the model better distinguish between the two
labels. To add more images to a dataset, see [Adding more images to a dataset](md-add-images.md "md-add-images.md").

While the confusion matrix is helpful, it's important to consider other
metrics. For example, 100% of the predictions correctly found the floor_plan
label, which indicates excellent performance. However, the test dataset only has
2 images with the floor_plan label. It also has 11 images with the living_space
label. This imbalance is also in the training dataset (13 living_space images
and 2 closet images). To get a more accurate evaluation, balance the training
and test datasets by adding more images of under-represented labels (floor plans
in this example). To get the number of test images per label, see [Accessing evaluation metrics (Console)](im-access-training-results.md "im-access-training-results.md").

The following table is a sample confusion matrix, comparing the predicted
label (on the y-axis) against the ground truth label:

| Predicted label | backyard | bathroom | bedroom | closet | entry_way | floor_plan | front_yard | kitchen | living_space | patio |
| --------------- | -------- | -------- | ------- | ------ | --------- | ---------- | ---------- | ------- | ------------ | ----- |
| backyard        | 75%      | 0%       | 0%      | 0%     | 0%        | 0%         | 33%        | 0%      | 0%           | 0%    |
| bathroom        | 0%       | 67%      | 0%      | 0%     | 0%        | 0%         | 0%         | 0%      | 0%           | 0%    |
| bedroom         | 0%       | 0%       | 82%     | 50%    | 0%        | 0%         | 0%         | 0%      | 9%           | 0%    |
| closet          | 0%       | 0%       | 0%      | 50%    | 0%        | 0%         | 0%         | 0%      | 0%           | 0%    |
| entry_way       | 0%       | 0%       | 0%      | 0%     | 33%       | 0%         | 0%         | 0%      | 0%           | 0%    |
| floor_plan      | 0%       | 0%       | 0%      | 0%     | 0%        | 100%       | 0%         | 0%      | 0%           | 0%    |
| front_yard      | 25%      | 0%       | 0%      | 0%     | 0%        | 0%         | 67%        | 0%      | 0%           | 0%    |
| kitchen         | 0%       | 33%      | 0%      | 0%     | 0%        | 0%         | 0%         | 88%     | 0%           | 0%    |
| living_space    | 0%       | 0%       | 18%     | 0%     | 67%       | 0%         | 0%         | 12%     | 91%          | 33%   |
| patio           | 0%       | 0%       | 0%      | 0%     | 0%        | 0%         | 0%         | 0%      | 0%           | 67%   |

## Getting the confusion matrix for a model

The following code uses the [DescribeProjects](../APIReference/API_DescribeProjects.md "../APIReference/API_DescribeProjects.md") and
[DescribeProjectVersions](../APIReference/API_DescribeProjectVersions.md "../APIReference/API_DescribeProjectVersions.md") operations to get the [summary file](im-summary-file-api.md "im-summary-file-api.md") for a model. It then
uses the summary file to display the confusion matrix for the model.

###### To display the confusion matrix for a model (SDK)

1. If you haven't already done so, install and configure the AWS CLI and the AWS SDKs. For more information, see
   [Step 4: Set up the AWS CLI and AWS SDKs](su-awscli-sdk.md "su-awscli-sdk.md").
2. Use the following code to display the confusion matrix for a model. Supply
   the following command line arguments:
   - `project_name` – the name of the project you
     want to use. You can get the project name from the projects page in the
     Amazon Rekognition Custom Labels console.
   - `version_name` – the version of the model that
     you want to use. You can get the version name from the project details page in
     the Amazon Rekognition Custom Labels console.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Purpose

Shows how to display the confusion matrix for an Amazon Rekognition Custom labels image
classification model.
"""


import json
import argparse
import logging
import boto3
import pandas as pd
from botocore.exceptions import ClientError


logger = logging.getLogger(__name__)


def get_model_summary_location(rek_client, project_name, version_name):
    """
    Get the summary file location for a model.

    :param rek_client: A Boto3 Rekognition client.
    :param project_arn: The Amazon Resource Name (ARN) of the project that contains the model.
    :param model_arn: The Amazon Resource Name (ARN) of the model.
    :return: The location of the model summary file.
    """

    try:
        logger.info(
            "Getting summary file for model %s in project %s.", version_name, project_name)

        summary_location = ""

        # Get the project ARN from the project name.
        response = rek_client.describe_projects(ProjectNames=[project_name])

        assert len(response['ProjectDescriptions']) > 0, \
            f"Project {project_name} not found."

        project_arn = response['ProjectDescriptions'][0]['ProjectArn']

        # Get the summary file location for the model.
        describe_response = rek_client.describe_project_versions(ProjectArn=project_arn,
                                                                 VersionNames=[version_name])
        assert len(describe_response['ProjectVersionDescriptions']) > 0, \
            f"Model {version_name} not found."

        model=describe_response['ProjectVersionDescriptions'][0]

        evaluation_results=model['EvaluationResult']

        summary_location=(f"s3://{evaluation_results['Summary']['S3Object']['Bucket']}"
                            f"/{evaluation_results['Summary']['S3Object']['Name']}")

        return summary_location

    except ClientError as err:
        logger.exception(
            "Couldn't get summary file location: %s", err.response['Error']['Message'])
        raise


def show_confusion_matrix(summary):
    """
    Shows the confusion matrix for an Amazon Rekognition Custom Labels
    image classification model.
    :param summary: The summary file JSON object.
    """
    pd.options.display.float_format = '{:.0%}'.format

    # Load the model summary JSON into a DataFrame.

    summary_df = pd.DataFrame(
        summary['AggregatedEvaluationResults']['ConfusionMatrix'])

    # Get the confusion matrix.
    confusion_matrix = summary_df.pivot_table(index='PredictedLabel',
                                              columns='GroundTruthLabel',
                                              fill_value=0.0).astype(float)

    # Display the confusion matrix.
    print(confusion_matrix)


def get_summary(s3_resource, summary):
    """
    Gets the summary file.
    : return: The summary file in bytes.
    """
    try:
        summary_bucket, summary_key = summary.replace(
            "s3://", "").split("/", 1)

        bucket = s3_resource.Bucket(summary_bucket)
        obj = bucket.Object(summary_key)
        body = obj.get()['Body'].read()
        logger.info(
            "Got summary file '%s' from bucket '%s'.",
            obj.key, obj.bucket_name)
    except ClientError:
        logger.exception(
            "Couldn't get summary file '%s' from bucket '%s'.",
            obj.key, obj.bucket_name)
        raise
    else:
        return body


def add_arguments(parser):
    """
    Adds command line arguments to the parser.
    : param parser: The command line parser.
    """

    parser.add_argument(
        "project_name", help="The ARN of the project in which the model resides."
    )
    parser.add_argument(
        "version_name", help="The version of the model that you want to describe."
    )


def main():
    """
    Entry point for script.
    """

    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s: %(message)s")

    try:

        # Get the command line arguments.
        parser = argparse.ArgumentParser(usage=argparse.SUPPRESS)
        add_arguments(parser)
        args = parser.parse_args()

        print(
            f"Showing confusion matrix for: {args.version_name} for project {args.project_name}.")

        session = boto3.Session(profile_name='custom-labels-access')
        rekognition_client = session.client("rekognition")
        s3_resource = session.resource('s3')

        # Get the summary file for the model.
        summary_location = get_model_summary_location(rekognition_client, args.project_name,
                                                      args.version_name
                                                      )
        summary = json.loads(get_summary(s3_resource, summary_location))

        # Check that the confusion matrix is available.
        assert 'ConfusionMatrix' in summary['AggregatedEvaluationResults'], \
            "Confusion matrix not found in summary. Is the model a classification model?"

        # Show the confusion matrix.
        show_confusion_matrix(summary)
        print("Done")

    except ClientError as err:
        logger.exception("Problem showing confusion matrix: %s", err)
        print(f"Problem describing model: {err}")

    except AssertionError as err:
        logger.exception(
            "Error: %s.\n", err)
        print(
            f"Error: {err}\n")


if __name__ == "__main__":
    main()

```
