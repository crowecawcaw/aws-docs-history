# Attaching a project policy (SDK)

You attach a project policy to an Amazon Rekognition Custom Labels project by calling the [PutProjectpolicy](../APIReference/API_PutProjectPolicy.md "../APIReference/API_PutProjectPolicy.md") operation.

Attach multiple project policies to a project by calling
`PutProjectPolicy` for each project policy that you want to add. You
can attach up to five project project policies to a project. If you need to attach
more project policies, you can request a [limit](limits.md "limits.md")
increase.

When you first attach a unique project policy to a project, don't specify a
revision ID in the `PolicyRevisionId` input parameter. The response from
`PutProjectPolicy` is a revision ID for the project policy that
Amazon Rekognition Custom Labels creates for you. You can use the revision ID to update or delete the
latest revision of a project policy. Amazon Rekognition Custom Labels only keeps the latest revision of a
project policy. If you try to update or delete a previous revision of a project
policy, you get an `InvalidPolicyRevisionIdException` error.

To update an existing project policy, specify the revision ID of the project
policy in the `PolicyRevisionId` input parameter. You can get the
revision IDs for project policies in a project by calling [ListProjectPolicies](../APIReference/API_ListProjectPolicies.md "../APIReference/API_ListProjectPolicies.md").

After you attach a project policy to a source project, you can copy the model from
the source project to the destination project. For more information, see [Copying a model (SDK)](md-copy-model-sdk.md "md-copy-model-sdk.md").

To remove a project policy from a project, call [DeleteProjectPolicy](../APIReference/API_DeleteProjectPolicy.md "../APIReference/API_DeleteProjectPolicy.md"). To get a list of project policies attached to a
project, call [ListProjectPolicies](../APIReference/API_ListProjectPolicies.md "../APIReference/API_ListProjectPolicies.md").

###### To attach a project policy to a project (SDK)

1. If you haven't already done so, install and configure the AWS CLI and the AWS SDKs. For more information, see
   [Step 4: Set up the AWS CLI and AWS SDKs](su-awscli-sdk.md "su-awscli-sdk.md").
2. [Create a project
   policy document](md-create-project-policy-document.md "md-create-project-policy-document.md").
3. Use the following code to attach the project policy to the project, in the
   trusting AWS account, that contains the model version that you want to
   copy. To get the project ARN, call [DescribeProjects](md-describing-project-sdk.md "md-describing-project-sdk.md"). To get the model version ARN call [DescribeProjectVersions](md-describing-model-sdk.md "md-describing-model-sdk.md").

AWS CLI
Change the following values:

    * `project-arn` to the ARN of the source
     project in the trusting AWS account that contains the
     model version that you want to copy.
    * `policy-name` to a policy name that you
     choose.
    * `principal` To the principal that you want
     to allow or deny access to the model versions that you
     specify in `Model version ARN`.
    * `project-version-arn` to the ARN of the
     model version that you want to copy.

If you want to update an existing project policy, specify the
`policy-revision-id` parameter and supply the
revision ID of the desired project policy.

```
aws rekognition put-project-policy \
  --project-arn `project-arn` \
  --policy-name `policy-name` \
  --policy-document '{ "Version": "2012-10-17",		 	 	  "Statement":[{ "Effect":"`ALLOW or DENY`", "Principal":{ "AWS":"`principal`" }, "Action":"rekognition:CopyProjectVersion", "Resource":"`project-version-arn`" }]}' \
  --profile custom-labels-access
```

Python
Use the following code. Supply the following command line
parameters:

    * `project_arn` – The ARN of the
     source project that you want to attach the project
     policy to.
    * `policy_name` – A policy name that
     you choose.
    * `project_policy` – The file that
     contains the project policy document,.
    * `policy_revision_id` – (Optional).
     If you want to update an existing revision of a project
     policy, specify the revision ID of the project
     policy.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Purpose
Amazon Rekognition Custom Labels model example used in the service documentation:
https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-copy-model-sdk.html
Shows how to attach a project policy to an Amazon Rekognition Custom Labels project.
"""

import boto3
import argparse
import logging
import json
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


def put_project_policy(rek_client, project_arn, policy_name, policy_document_file, policy_revision_id=None):
    """
    Attaches a project policy to an Amazon Rekognition Custom Labels project.
    :param rek_client: The Amazon Rekognition Custom Labels Boto3 client.
    :param policy_name: A name for the project policy.
    :param project_arn: The Amazon Resource Name (ARN) of the source project
    that you want to attach the project policy to.
    :param policy_document_file: The JSON project policy document to
    attach to the source project.
    :param policy_revision_id: (Optional) The revision of an existing policy to update.
    Pass None to attach new policy.
    :return The revision ID for the project policy.
    """

    try:

        policy_document_json = ""
        response = None

        with open(policy_document_file, 'r') as policy_document:
            policy_document_json = json.dumps(json.load(policy_document))

        logger.info(
            "Attaching %s project_policy to project %s.",
            policy_name, project_arn)

        if policy_revision_id is None:
            response = rek_client.put_project_policy(ProjectArn=project_arn,
                                                     PolicyName=policy_name,
                                                     PolicyDocument=policy_document_json)

        else:
            response = rek_client.put_project_policy(ProjectArn=project_arn,
                                                     PolicyName=policy_name,
                                                     PolicyDocument=policy_document_json,
                                                     PolicyRevisionId=policy_revision_id)

        new_revision_id = response['PolicyRevisionId']

        logger.info(
            "Finished creating project policy %s. Revision ID: %s",
            policy_name, new_revision_id)

        return new_revision_id

    except ClientError as err:
        logger.exception(
            "Couldn't attach %s project policy to project %s: %s }",
            policy_name, project_arn, err.response['Error']['Message'] )
        raise


def add_arguments(parser):
    """
    Adds command line arguments to the parser.
    :param parser: The command line parser.
    """

    parser.add_argument(
        "project_arn",  help="The Amazon Resource Name (ARN) of the project "
        "that you want to attach the project policy to."
    )
    parser.add_argument(
        "policy_name",  help="A name for the project policy."

    )

    parser.add_argument(
        "project_policy",  help="The file containing the project policy JSON"
    )

    parser.add_argument(
        "--policy_revision_id",  help="The revision of an existing policy to update. "
        "If you don't supply a value, a new project policy is created.",
        required=False
    )


def main():

    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s: %(message)s")

    try:

        # get command line arguments
        parser = argparse.ArgumentParser(usage=argparse.SUPPRESS)
        add_arguments(parser)

        args = parser.parse_args()

        print(f"Attaching policy to {args.project_arn}")

        session = boto3.Session(profile_name='custom-labels-access')
        rekognition_client = session.client("rekognition")


        # Attach a new policy or update an existing policy.

        response = put_project_policy(rekognition_client,
                                      args.project_arn,
                                      args.policy_name,
                                      args.project_policy,
                                      args.policy_revision_id)

        print(
            f"project policy {args.policy_name} attached to project {args.project_arn}")
        print(f"Revision ID: {response}")

    except ClientError as err:
        print("Problem attaching project policy: %s", err)


if __name__ == "__main__":
    main()

```

Java V2
Use the following code. Supply the following command line
parameters:

    * `project_arn` – The ARN of the
     source project that you want to attach the project
     policy to.
    * `project_policy_name` – A policy
     name that you choose.
    * `project_policy_document` – The file
     that contains the project policy document.
    * `project_policy_revision_id` –
     (Optional). If you want to update an existing revision
     of a project policy, specify the revision ID of the
     project policy.

```
/*
   Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
   SPDX-License-Identifier: Apache-2.0
*/

package com.example.rekognition;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.logging.Level;
import java.util.logging.Logger;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.rekognition.RekognitionClient;
import software.amazon.awssdk.services.rekognition.model.PutProjectPolicyRequest;
import software.amazon.awssdk.services.rekognition.model.RekognitionException;

public class PutProjectPolicy {

    public static final Logger logger = Logger.getLogger(PutProjectPolicy.class.getName());

    public static void putMyProjectPolicy(RekognitionClient rekClient, String projectArn, String projectPolicyName,
             String projectPolicyFileName, String projectPolicyRevisionId) throws IOException {

        try {

            Path filePath = Path.of(projectPolicyFileName);



            String policyDocument = Files.readString(filePath);

            String[] logArguments = new String[] { projectPolicyFileName, projectPolicyName };

            PutProjectPolicyRequest putProjectPolicyRequest = null;

            logger.log(Level.INFO, "Attaching Project policy: {0} to project: {1}", logArguments);

            // Attach the project policy.

            if (projectPolicyRevisionId == null) {
                putProjectPolicyRequest = PutProjectPolicyRequest.builder().projectArn(projectArn)
                        .policyName(projectPolicyName).policyDocument(policyDocument).build();
            } else {
                putProjectPolicyRequest = PutProjectPolicyRequest.builder().projectArn(projectArn)
                        .policyName(projectPolicyName).policyRevisionId(projectPolicyRevisionId)
                        .policyDocument(policyDocument)

                        .build();
            }

            rekClient.putProjectPolicy(putProjectPolicyRequest);

            logger.log(Level.INFO, "Attached Project policy: {0} to project: {1}", logArguments);

        } catch (

        RekognitionException e) {
            logger.log(Level.SEVERE, "Client error occurred: {0}", e.getMessage());
            throw e;
        }

    }

    public static void main(String args[]) {

        final String USAGE = "\n" + "Usage: "
                + "<project_arn> <project_policy_name> <policy_document> <project_policy_revision_id>\n\n" + "Where:\n"
                + "   project_arn - The ARN of the project that you want to attach the project policy to.\n\n"
                + "   project_policy_name - A name for the project policy.\n\n"
                + "   project_policy_document - The file name of the project policy.\n\n"
                + "   project_policy_revision_id - (Optional) The revision ID of the project policy that you want to update.\n\n";

        if (args.length < 3 || args.length > 4) {
            System.out.println(USAGE);
            System.exit(1);
        }

        String projectArn = args[0];
        String projectPolicyName = args[1];
        String projectPolicyDocument = args[2];
        String projectPolicyRevisionId = null;

        if (args.length == 4) {
            projectPolicyRevisionId = args[3];
        }

        try {

            RekognitionClient rekClient = RekognitionClient.builder()
            .credentialsProvider(ProfileCredentialsProvider.create("custom-labels-access"))
            .region(Region.US_WEST_2)
            .build();


            // Attach the project policy.
            putMyProjectPolicy(rekClient, projectArn, projectPolicyName, projectPolicyDocument,
                    projectPolicyRevisionId);

            System.out.println(
                    String.format("project policy %s: attached to project: %s", projectPolicyName, projectArn));

            rekClient.close();

        } catch (RekognitionException rekError) {
            logger.log(Level.SEVERE, "Rekognition client error: {0}", rekError.getMessage());
            System.exit(1);
        }

        catch (IOException intError) {
            logger.log(Level.SEVERE, "Exception while reading policy document: {0}", intError.getMessage());
            System.exit(1);
        }

    }

}

```

4. Copy the model version by following the instructions at [Copying a model (SDK)](md-copy-model-sdk.md "md-copy-model-sdk.md").
