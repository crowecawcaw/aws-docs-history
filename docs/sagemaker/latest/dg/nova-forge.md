# Amazon Nova Forge

Amazon Nova Forge is a first-of-its-kind service that offers organizations the easiest and most cost-effective way to build their own frontier models using Nova.

Amazon Nova Forge introduces the concept of “open training" models, which give
organizations access to a variety of early model checkpoints and the ability to blend
proprietary data with Amazon-curated data sets at every stage of model training. This allows
the models to maximize learning from proprietary data while minimizing risk of forgetting
foundational skills like reasoning.

Nova Forge provides the following key capabilities:

- Access checkpoints across all phases of model development, and leverage new Nova models before they are widely available
- Blend your proprietary data with Amazon Nova-curated training data
- Perform reinforcement learning with reward functions in your environment
- Use push-button recipes that are optimized to build with Nova through visual workflows or a command line interface
- Use the built-in responsible AI toolkit to implement custom safety guardrails

## Prerequisites

###### Topics

- [Subscribe to Nova Forge](#nova-forge-prereq-access "#nova-forge-prereq-access")
- [Other prerequisites](#nova-forge-prereq-other "#nova-forge-prereq-other")

### Subscribe to Nova Forge

To request access to the Nova Forge service, first step is to add the following
key-value pair as tags to your role: forge-subscription. After you've added these
tags to your role, please go to SageMaker AI Console > Model training and customization and
click on Nova Forge. On this page, you'll find details about the service, pricing
information and the capabilities. You can request subscription and then manage your
subscription from this page.

1. The role should have permission to call api
   `ListAttachedRolePolicy`, and the response should include
   either `AdministratorAccess` or
   `AmazonSageMakerFullAccess` policy.
2. The sign-in role should have permission to call api
   `ListRoleTags`, and the response tags should include
   `tag.key=forge-subscription`.

### Other prerequisites

Also ensure the following prerequisites are complete:

1. [General
   pre-requisites](nova-model-general-prerequisites.md "nova-model-general-prerequisites.md")
2. Additional steps for SageMaker HyperPod users: Add Restricted Instance Group
   (RIG) to your HyperPod cluster (to complete follow steps [here](nova-hp-cluster.md "nova-hp-cluster.md"))

## Initial HyperPod setup

Follow the steps in the [AWS documentation](nova-hp-train.md "nova-hp-train.md") to connect
the HyperPod CLI to your cluster. Ensure you use `nova-lite-2.0-release`
branch instead of `release_v2` for testing. [This topic](nova-hp-train.md "nova-hp-train.md") covers:

- Setting up AWS IAM permissions and policies
- Configuring the HyperPod CLI
- Creating your cluster with the necessary instance groups
- Connecting to your cluster

**Verification**: After completing the setup, confirm you
can successfully run `hyperpod connect-cluster` and access your
cluster.

## Setting up permissions for Nova Forge

To enable access to Nova Forge models and data mixes, grant your HyperPod
cluster's execution role permissions to access Nova Forge S3 buckets.

1. Locate your execution role.

Your execution role follows the naming convention:

```
arn:aws:iam::<AWS_ACCOUNT_ID>:role/<your-cluster-name>-9610a1d3ExecRole
```

To find your execution role:

    1. Navigate to IAM → Roles in the AWS Management Console
    2. Search for your cluster name (e.g., `9610a1d3Exec`)
    3. Locate the role matching the pattern above
    4. Alternately, if the cluster is already created, the execution role can
     be viewed in the AWS Management Console under SageMaker AI > Cluster management > [Your
     Cluster Name] > Instances > Restricted Instance Groups > Execution Role
     ARN

2. Apply Changes to Existing RIG (if applicable)

###### Important

If you granted this permission after creating your RIG, you must update
the cluster for changes to take effect. See the Troubleshooting section
below for instructions on updating your cluster.

###### Note

Without this permission, your RIG will not have access to Nova datasets or
model checkpoints required for Forge features.
