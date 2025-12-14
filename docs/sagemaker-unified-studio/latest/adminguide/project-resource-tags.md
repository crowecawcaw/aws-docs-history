# Project resource tags

Project resource tags in Amazon SageMaker Unified Studio are custom key-value pairs that you assign to
projects to help organize, categorize, and manage your resources. You can use tags for cost
allocation, access control, and resource organization across your Amazon SageMaker Unified Studio
projects.

Tags are configured through a Project Profile, applied at the project level and inherited
by resources created through the create project and update project actions.

The following considerations apply for project resource tags in Amazon SageMaker Unified Studio:

- Configure project profiles with project resource tags using AWS CLI or API
  only.
- You can add up to 25 tags per project profile.
- Tag keys must conform to the IAM policy permissions of the domain provisioning
  role.
- Tag keys must be unique within a project and can contain up to 128 characters.
- Tag values are optional and can contain up to 256 characters.
- Tag keys and values can contain letters, numbers, spaces, and the following
  characters: + - = . \_ : / @
- Tag keys and values are case-sensitive.

## IAM permissions for project resource tags

By default, the tag Key must begin with the string "AmazonDataZone". This condition is
set in the domain provisioning role. If Amazon SageMaker Unified Studio created the provisioning role for you
it will be the AmazonSageMakerProvisioning-AccountId role. To create tags with a different
string pattern (i.e. begins with, contains, etc.), a policy with appropriate permissions
must be attached to the domain provisioning role.

###### To configure IAM policy for project resource tags

1. Navigate to the Identity and Access Management (IAM) console.
2. In the navigation pane, choose **Roles**.
3. In the list, search for AmazonSageMakerProvisioning-accountId or your custom domain
   provisioning role.
4. Choose the **Permissions** tab.
5. Choose **Add permissions**, and then choose **Create inline
   policy**.
6. Under **Policy editor**, choose **JSON**.
7. Enter the policy.
8. Save to attach the policy to the role.

The following is an example policy allowing tag Keys to begin with "AmazonDataZone" or
"SageMaker". Modify aws:TagKeys within the condition to meet your tag Key name
requirements.

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CustomTagsUnTagPermissions",
            "Effect": "Allow",
            "Action": [
                "codecommit:UntagResource",
                "iam:UntagRole",
                "logs:UntagResource",
                "athena:UntagResource",
                "redshift-serverless:UntagResource",
                "scheduler:UntagResource",
                "bedrock:UntagResource",
                "neptune-graph:UntagResource",
                "quicksight:UntagResource",
                "glue:UntagResource",
                "airflow:UntagResource",
                "secretsmanager:UntagResource",
                "lambda:UntagResource",
                "emr-serverless:UntagResource",
                "elasticmapreduce:RemoveTags",
                "sagemaker:DeleteTags",
                "ec2:DeleteTags"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                },
                "ForAllValues:StringLike": {
                    "aws:TagKeys": [
                        "AmazonDataZone*",
                        "SageMaker*"
                    ]
                },
                "Null": {
                    "aws:ResourceTag/AmazonDataZoneProject": "false"
                }
            }
        },
        {
            "Sid": "CustomTagsTaggingPermissions",
            "Effect": "Allow",
            "Action": [
                "cloudformation:TagResource",
                "codecommit:TagResource",
                "iam:TagRole",
                "glue:TagResource",
                "athena:TagResource",
                "lambda:TagResource",
                "redshift-serverless:TagResource",
                "logs:TagResource",
                "secretsmanager:TagResource",
                "sagemaker:AddTags",
                "emr-serverless:TagResource",
                "neptune-graph:TagResource",
                "bedrock:TagResource",
                "elasticmapreduce:AddTags",
                "airflow:TagResource",
                "scheduler:TagResource",
                "quicksight:TagResource",
                "emr-containers:TagResource",
                "logs:CreateLogGroup",
                "athena:CreateWorkGroup",
                "scheduler:CreateScheduleGroup",
                "cloudformation:CreateStack",
                "ec2:*"
            ],
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringLike": {
                    "aws:TagKeys": [
                        "AmazonDataZone*",
                        "SageMaker*"
                    ]
                },
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        }
    ]
}

```

###### Note

it is possible to scope down the specific AWS service tag and un-tag permissions
based on which blueprints / capabilities are used.

## Configure project resource tags

Project resource tags are configured in the project profile. The project profile sets
the key/value tag pairs, whether the value can be modified by the project creator, and
whether projects using the project profile can create their own project resource tags at the
time of project creation. Once configured, project resource tags will be applied to all
projects using the project profile.

To use the AWS CLI to create a project profile with project resource tags, use the
create-project-profile command.

Parameter --project-resource-tags sets tags within the project profile. Each tag is
composed of a key (string), value (string), and isValueEditable (boolean). IsValueEditable
set to true means the value can be changed during project creation or update.

The following example shows the parameter project-resource-tags with tags
configured.

```

--project-resource-tags '[
	{
		"key": "SageMaker",
		"value": "application",
		"isValueEditable": false
	},
	{
		"key": "AmazonDataZone-CostCenter",
		"value": "123",
		"isValueEditable": true
	}
]'

```

Parameter --allow-custom-project-resource-tags true | false permits the project creator
to create additional key/value pairings. The key needs to conform to the policy of the
domain provisioning role.

Parameter --project-resource-tags-description is a description field for project
resource tags. The max character limit is 2048. The description needs to be passed in every
time create-project-profile or update-project-profile is called.

## Update project resource tags

Updates to project resource tags in the project profile apply automatically to new
projects created from that point forward. For existing projects using the project profile,
an update notification will be triggered in the project and the changes will be applied when
the project is updated. Existing resources retain their current tags until they are
recreated or manually updated.

To use the AWS CLI to update a project profile with project resource tags, use the
update-project-profile command. Parameters --project-resource-tags and
--allow-custom-project-resource-tags can be updated.

There are three ways to work with the project-resource-tags parameter when updating the
project profile.

- Passing a non-empty list of project resource tags will replace the tags currently
  configured on the project profile. Updating project resource tags in the project profile
  is not an additive action - include the exhaustive set of tags.
- Passing an empty list of project resource tags will clear out all previously
  configured tags:

--project-resource-tags '[]'

- Not including the project resource tag parameter will keep previously configured
  tags as-is.

## Update the project

Projects need to be updated when:

1. Project resource tags are updated in the project profile.
2. The project, when permitted by the project profile, updates existing tag values or
   adds new tags.

To use the AWS CLI to update a project with project resource tags, use the
update-project command.

Parameter --resource-tags updates tags in the project. Tag values can be updated when
their property isValueEditable is set to true. New tags can be added if parameter
--allow-custom-project-resource-tags from the project profile is set to true.

The following example shows the parameter --resource-tags in the update project
call.

```

  --resource-tags '[
	{
		"key": "AmazonDataZone-CostCenter ",
		"value": "456"

]'

```

Project level tags (those not configured from the project profile) need to be passed
during project update in order to be preserved. For tags with isValueEditable = true
configured from the project profile, any override previously set needs to be applied or the
value will revert to the default from the project profile.

## Delete project resource tags

To delete project resource tags set from the project profile use the
update-project-profile command followed by the update-project command.

1. Call the update-project-profile command with an empty list for parameter
   --project-resource-tags to remove project resource tags from the project profile.
   Existing project resources that already have these tags will retain them. New projects
   created using this project profile will not inherit the deleted tags.

--project-resource-tags '[]' 2. Call the update-project command to remove project resource tags from the project
resources. This removes the project resource tags set from the project profile. This
will not remove the project resource tags set directly from the project.

To delete project resource tags set from the project use the update-project command with
an empty list for parameter --resource-tags.

--resource-tags '[]'
