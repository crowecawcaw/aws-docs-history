# Manage Tooling blueprint parameters

The Tooling blueprint provisions infrastructure for each project, including IAM
roles, security groups, and an Amazon SageMaker unified domain. You can customize the
blueprint's behavior by modifying its parameters, such as idle timeout settings, EBS
volume sizes, network isolation, and permissions boundaries. Changes to blueprint
parameters apply to all new projects created under the blueprint.

This topic covers the following tasks:

- Configure Tooling blueprint parameters through the console
- Configure IAM permissions boundaries for roles created by the Tooling
  blueprint

## Configure Tooling blueprint parameters

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector
   in the top navigation bar to choose the appropriate AWS Region.
2. Choose **View domains** and choose the domain's name from the
   list. The name is a hyperlink.
3. On the domain's details page, navigate to the **Project
   profiles** tab.
4. In the **Project profiles** tab, choose a project profile,
   for example, **All capabilities**. The name of the project
   profile is a hyperlink.
5. On the project profile details page, choose **Tooling
   configuration**.
6. In the **Blueprint parameters** section, review the parameter
   values used during project creation.
7. To modify a parameter, choose **Edit** on the
   **Tooling configuration** tab.
8. Select the radio button next to the parameter you want to modify, then choose
   **Edit**.
9. In the **Edit blueprint parameter** dialog, update the value.
   Select **Editable** if you want the value to be configurable
   during project creation. Choose **Save**.

The following parameters are available for the Tooling blueprint:

- `minIdleTimeoutInMinutes` — The minimum time (in minutes) that
  Amazon SageMaker waits after the application becomes idle before shutting
  down the user's space.
- `maxEbsVolumeSize` — The maximum EBS storage volume size (in
  GB) for the user's private spaces.
- `idleTimeoutInMinutes` — The time (in minutes) that Amazon
  SageMaker waits after the application becomes idle before shutting down the
  user's space.
- `enableNetworkIsolation` — Enables network isolation for
  training and deployed inference containers.
- `lifecycleManagement` — Indicates whether idle shutdown is
  activated for this project's Amazon SageMaker unified domain.
- `sagemakerDomainNetworkType` — The network type for this
  project's Amazon SageMaker unified domain.
- `maxIdleTimeoutInMinutes` — The maximum time (in minutes) that
  Amazon SageMaker waits after the application becomes idle before shutting
  down this project's Amazon SageMaker unified domain.
- `allowConnectionToUserGovernedEmrClusters` — Allows connection
  creation to existing user-governed EMR clusters.
- `enableSpaces` — Enables creation of private compute spaces
  for development tools.
- `enableProjectRepositoryAutoSync` — Synchronizes your Git
  repository code artifacts to your project's S3 bucket at
  `s3://{bucket}/{domain_id}/{project_id}/sys/code/dev/{repository_id}/{branch}/`.
  Synchronization is triggered by Git push events.

###### Note

Enabling `maxEbsVolumeSize`, `enableSpaces`, or
`enableProjectRepositoryAutoSync` parameters might result in
incurring additional costs. For more information, see [Amazon SageMaker
pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/").

## Configure IAM permissions boundaries

Amazon SageMaker Unified Studio supports custom permissions boundaries for IAM roles created by
the Tooling blueprint. Organizations that enforce Service Control Policies
requiring permissions boundaries on all IAM roles can configure a permission
boundary on the Tooling blueprint.

When configured, the service attaches the boundary to all
IAM roles provisioned by the Tooling blueprint during project creation, including
the `datazone_usr_role`, `AmazonBedrockServiceRole`, and
`AmazonBedrockLambdaExecutionRole`. To learn more about permission
boundaries, see [Permissions boundaries for IAM entities](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") in the
_AWS Identity and Access Management User Guide_.

You set the permissions boundary at the blueprint configuration level using the
`PermissionsBoundaryArn` regional parameter. When a user creates a new
project that includes the Tooling blueprint, the CloudFormation stack creates IAM roles
with the specified boundary attached. Because you set the boundary at the blueprint
level, it applies to every project created under that blueprint.

Before you configure a permissions boundary, verify that you have the
following:

- An Identity Center-based domain with the Tooling blueprint
  enabled
- AWS CLI configured with permissions to manage domain configurations
- An existing IAM managed policy to use as the permissions boundary

###### To configure a permissions boundary on the Tooling blueprint

1. Retrieve your domain ID by running the following command:

```
aws datazone list-domains \
    --region `region` \
    --query "items[?name=='`domain-name`'].id | [0]" \
    --output text
```

2. Retrieve the Tooling blueprint ID by running the following
   command:

```
aws datazone list-environment-blueprints \
    --domain-identifier `domain-id` \
    --managed \
    --region `region` \
    --query "items[?name=='Tooling'].id | [0]" \
    --output text
```

3. Retrieve the current blueprint configuration by running the following
   command:

```
aws datazone get-environment-blueprint-configuration \
    --domain-identifier `domain-id` \
    --environment-blueprint-identifier `tooling-bp-id` \
    --region `region`
```

Record the following values from the output. You need these values in the next step:

    * `provisioningRoleArn`
    * `manageAccessRoleArn`
    * `enabledRegions`
    * All fields inside `regionalParameters`

4. Update the blueprint configuration to include
   `PermissionsBoundaryArn` in the regional parameters by running
   the following command:

```
aws datazone put-environment-blueprint-configuration \
    --domain-identifier `domain-id` \
    --environment-blueprint-identifier `tooling-bp-id` \
    --enabled-regions '`enabledRegions`' \
    --provisioning-role-arn "`provisioningRoleArn`" \
    --manage-access-role-arn "`manageAccessRoleArn`" \
    --regional-parameters '{
        "`region`": {
            "AZs": "`AZs`",
            "S3Location": "`S3Location`",
            "Subnets": "`Subnets`",
            "VpcId": "`VpcId`",
            "PermissionsBoundaryArn": "arn:aws:iam::`account-id`:policy/`policy-name`"
        }
    }' \
    --region `region`
```

###### Important

The `put-environment-blueprint-configuration` API operates
in overwrite mode. It replaces the entire configuration. You must
include all existing values from the preceding step. The only new
field is `PermissionsBoundaryArn`. Omitting any existing
parameter removes it. 5. Verify the configuration by running the following command:

```
aws datazone get-environment-blueprint-configuration \
    --domain-identifier `domain-id` \
    --environment-blueprint-identifier `tooling-bp-id` \
    --region `region` \
    --query "regionalParameters.\"`region`\".PermissionsBoundaryArn"
```

###### Important considerations

- The permissions boundary only affects new projects. Existing projects
  retain their original configuration.
- The boundary applies to all three IAM roles created by the Tooling
  blueprint. You cannot selectively apply it to individual roles.
- The IAM policy referenced by `PermissionsBoundaryArn`
  must exist in the account before project creation. If the policy is
  deleted or the ARN is invalid, provisioning fails.
- To remove the boundary from future projects, run
  `put-environment-blueprint-configuration` again without the
  `PermissionsBoundaryArn` parameter.
