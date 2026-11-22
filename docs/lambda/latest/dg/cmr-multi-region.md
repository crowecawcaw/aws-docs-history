

# Deploying runtimes in multiple Regions

Customer-managed runtimes, runtime versions, and runtime aliases are Regional resources. To make a runtime available to Lambda Event Functions in more than one AWS Region, you create and manage the runtime in each Region. This topic is for runtime publishers. It explains how to distribute runtime images across Regions, keep resource names consistent, and roll out updates one Region at a time.

For an overview of customer-managed runtimes, see [Customer-managed runtimes](runtimes-customer-managed.md).

**Topics**
+ [Regional resource model](#cmr-multi-region-resource-model)
+ [Distributing runtime images across Regions](#cmr-multi-region-images)
+ [Using consistent names across Regions](#cmr-multi-region-naming)
+ [Rolling out updates one Region at a time](#cmr-multi-region-rollout)
+ [Automating multi-Region deployments](#cmr-multi-region-automation)
+ [Deploy a runtime to multiple Regions](#cmr-multi-region-deploy)

## Regional resource model
<a name="cmr-multi-region-resource-model"></a>

A runtime exists in exactly one AWS Region. Its runtime versions and runtime aliases exist in the same Region as the runtime. To use a runtime in several Regions, create the runtime, its runtime versions, and its runtime aliases in each Region.

Lambda manages each Region independently. When you create or update a resource in one Region, Lambda doesn't copy the change to other Regions. Because of this, you can control when each Region receives an update.

Each Regional copy of a runtime has its own Amazon Resource Name (ARN). The Region is part of the ARN, as shown in the following format:

```text
arn:aws:lambda:{{region}}:{{account-id}}:runtime/{{runtime-name}}
```

Runtime consumers reference the runtime in the same Region as their function. For example, a function in `eu-west-1` uses the runtime ARN that contains `eu-west-1`. For more information about how consumers configure functions, see [Using a customer-managed runtime](cmr-using.md).

Resource-based policies are also Regional. If you share a runtime with other accounts, you must grant access to the runtime in each Region. For more information, see [Sharing and controlling access to customer-managed runtimes](cmr-permissions.md).

## Distributing runtime images across Regions
<a name="cmr-multi-region-images"></a>

Each runtime version references a container image in Amazon Elastic Container Registry (Amazon ECR). The image must be in the same Region as the runtime. A runtime version can't reference an image in a different Region. The image can be in a different AWS account, as long as it's in the same Region.

Because of this, you must make each runtime image available in every Region where you deploy the runtime. You can use one of the following methods:
+ **Amazon ECR cross-Region replication (recommended)** – You push each image one time to a repository in a source Region. Amazon ECR copies the image to the destination Regions. The runtime version in each Region then references the replica image in that Region.
+ **Push to each Region** – You push the image to a repository in each Region yourself, for example, from your build pipeline. We recommend that you push the same image to every Region, so that a version name refers to the same runtime contents everywhere.

With cross-Region replication, Amazon ECR copies images to repositories with the same name in the destination Regions. Keep the following Amazon ECR behaviors in mind:
+ Amazon ECR replicates only images that you push after you configure replication. It doesn't replicate images that already exist in the repository.
+ Replicated repositories have the same name in every Region.
+ Amazon ECR doesn't replicate repository policies by default. Lambda needs read access to the image in each Region. You can create the repository and its policy in each destination Region in advance. You can also use Amazon ECR repository creation templates to apply the policy to repositories that replication creates.
+ Most images replicate in less than 30 minutes, but replication can take longer. Confirm that replication is complete before you create a runtime version in a destination Region.

For more information, see [Private image replication in Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/replication.html) in the *Amazon Elastic Container Registry User Guide*. For the repository policy that Lambda requires, see [Runtime versions](cmr-versions.md).

You must keep each Regional image in Amazon ECR while a runtime version references it. Standard Amazon ECR storage rates apply in each Region.

You can also keep runtime images in a central image account. Runtimes in other accounts can then use those images, as long as each runtime is in the same Region as the image. For example, a central account can replicate images to each Region. Runtime publisher accounts then create runtime versions from the replica in their own Region.

## Using consistent names across Regions
<a name="cmr-multi-region-naming"></a>

We recommend that you use the same runtime name, runtime version names, and runtime alias names in every Region. With consistent names, your automation and your runtime consumers can predict the ARNs. Only the Region changes from one ARN to the next.

The following table shows the ARNs for the `prod` alias of a runtime named `companyphp8` in three Regions.


**Runtime alias ARNs for the same runtime in three Regions**  

| Region | Runtime alias ARN | 
| --- | --- | 
| us-east-1 | arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/alias/prod | 
| us-west-2 | arn:aws:lambda:us-west-2:123456789012:runtime/companyphp8/alias/prod | 
| eu-west-1 | arn:aws:lambda:eu-west-1:123456789012:runtime/companyphp8/alias/prod | 

Use the same version name for the same image in every Region. For example, if runtime version `v8.3.2` uses a given image in `us-east-1`, create `v8.3.2` from the replica of that image in each other Region. Then the same alias and version names refer to the same runtime contents in every Region.

If you set lifecycle information, we recommend that you set the same values in each Region. For more information, see [Runtime lifecycle](cmr-lifecycle.md).

## Rolling out updates one Region at a time
<a name="cmr-multi-region-rollout"></a>

Because each Region is independent, you can stagger a runtime update across Regions. A staggered rollout limits the impact of a faulty runtime version to the Regions that already received it. Regional staggering is one of several safe rollout practices. For more information, see [Deploying runtime updates](cmr-deploy-updates.md).

A staggered rollout typically uses the following sequence:

1. Create the new runtime version in every Region. A new runtime version doesn't affect any function until an alias points to it.

1. Update the alias in the first Region. We recommend that you start with a Region that has less traffic.

1. Wait for a bake period, and monitor the runtime in that Region.

1. If the runtime is healthy, update the alias in the next Region. Repeat until all Regions use the new runtime version.

Functions pick up an alias update at their next cold start, not immediately. Execution environments that are already running keep the previous runtime version until Lambda replaces them. Choose a bake period that gives functions enough time to move to the new runtime version.

Lambda publishes runtime metrics in each Region separately. In each Region, the metrics combine usage from all accounts and organizations that use the runtime. Before you continue to the next Region, check the `RuntimeInvocations` and `RuntimeInvocationErrors` metrics in the current Region. You can view these metrics by runtime name, runtime version, and runtime alias. For more information, see [Monitoring customer-managed runtimes](cmr-monitoring.md).

If you find a problem, stop the rollout. To roll back a Region, update the alias in that Region to point to the previous runtime version. Regions that you haven't updated yet aren't affected.

You can combine Regional staggering with staged aliases, such as `dev`, `test`, and `prod`. For example, update the `test` alias in all Regions first. Then update the `prod` alias one Region at a time. For more information, see [Runtime aliases](cmr-aliases.md).

## Automating multi-Region deployments
<a name="cmr-multi-region-automation"></a>

Managing a runtime manually in many Regions takes time and can lead to errors. We recommend that you automate your deployments. You can use the following approaches:
+ **CloudFormation StackSets** – Define the runtime, runtime version, and runtime alias in a CloudFormation template. Then use StackSets to deploy the template to multiple Regions. StackSets can deploy to Regions in a sequence that you specify. For more information, see [Managing stacks across accounts and Regions with StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) in the *AWS CloudFormation User Guide*.
+ **Deployment pipeline** – Use a pipeline, such as one built with AWS CodePipeline and AWS CodeBuild, to run each step of a release. A pipeline can build and push the image, and wait for replication. It can then create the runtime version in each Region and update the alias one Region at a time. Add a bake period and metric checks between Regions so that the pipeline stops automatically if it detects a problem.

You can also script the AWS CLI commands in this topic. For an example, see [Step 3: Publish a version and update the alias one Region at a time](#cmr-multi-region-deploy-update).

## Deploy a runtime to multiple Regions
<a name="cmr-multi-region-deploy"></a>

The procedures in this section deploy a runtime named `companyphp8` to the `us-east-1`, `us-west-2`, and `eu-west-1` Regions in account `123456789012`. The source Region for runtime images is `us-east-1`. The procedures deploy runtime version `v8.3.2` through an alias named `prod`.

Before you start, make sure that you have the following:
+ IAM permissions to manage runtimes, runtime versions, and runtime aliases in each Region. To create a runtime version, you also need `ecr:BatchGetImage` and `ecr:GetDownloadUrlForLayer` on the Amazon ECR repository that contains the image in each Region. For the required actions, see [Creating a runtime](cmr-create.md), [Runtime versions](cmr-versions.md), and [Runtime aliases](cmr-aliases.md).
+ IAM permissions to configure Amazon ECR replication and to create and manage repositories in each Region.
+ A runtime image that you can push to Amazon ECR. For more information, see [Building runtime images](cmr-building-images.md).

### Step 1: Set up Amazon ECR cross-Region replication
<a name="cmr-multi-region-replication"></a>

In this step, you create a repository in each Region, grant Lambda read access, and turn on replication from the source Region. You need to complete this step only one time. If you push images to each Region yourself instead, create the repositories and policies, push the image to each Region, and then continue to the next step.

#### Set up replication (AWS CLI)
<a name="cmr-multi-region-replication-cli"></a>

**To set up cross-Region replication (AWS CLI)**

1. Save the following repository policy as `lambda-ecr-policy.json`. This policy grants Lambda read access to the runtime images.

   ```json
   {
     "Version": "2012-10-17",		 	 	 
     "Statement": [
       {
         "Sid": "LambdaReadAccess",
         "Effect": "Allow",
         "Principal": {
           "Service": "lambda.amazonaws.com"
         },
         "Action": [
           "ecr:BatchGetImage",
           "ecr:DescribeImages",
           "ecr:GetDownloadUrlForLayer"
         ],
         "Condition": {
           "StringEquals": {
             "aws:SourceAccount": "123456789012"
           },
           "ArnLike": {
             "aws:SourceArn": "arn:aws:lambda:*:123456789012:runtime/*"
           }
         }
       }
     ]
   }
   ```

   The conditions restrict access to runtimes in your account. The value of `aws:SourceArn` is the runtime ARN, not the runtime version ARN.

1. To create a repository with this policy in each Region, run the following script. The script runs the `create-repository` and `set-repository-policy` commands in each Region.

   ```bash
   for region in {{us-east-1 us-west-2 eu-west-1}}; do
     aws ecr create-repository \
       --region "$region" \
       --repository-name {{companyphp8}}
     aws ecr set-repository-policy \
       --region "$region" \
       --repository-name {{companyphp8}} \
       --policy-text file://lambda-ecr-policy.json
   done
   ```

   If a repository already exists in a Region, `create-repository` fails for that Region. The script still applies the policy to the existing repository.

1. Save the following replication configuration as `replication.json`. This configuration replicates repositories whose names start with `companyphp8` to `us-west-2` and `eu-west-1`.

   ```json
   {
     "rules": [
       {
         "destinations": [
           {
             "region": "us-west-2",
             "registryId": "123456789012"
           },
           {
             "region": "eu-west-1",
             "registryId": "123456789012"
           }
         ],
         "repositoryFilters": [
           {
             "filter": "companyphp8",
             "filterType": "PREFIX_MATCH"
           }
         ]
       }
     ]
   }
   ```

1. To turn on replication in the source Region, run the `put-replication-configuration` command.

   ```bash
   aws ecr put-replication-configuration \
     --region {{us-east-1}} \
     --replication-configuration file://replication.json
   ```

   The output contains the replication configuration that you specified. The replication configuration applies to your whole private registry in the source Region. If your registry already has a replication configuration, this command replaces it. Add your existing rules to `replication.json` first.

1. Push your runtime image, tagged `v8.3.2`, to the `companyphp8` repository in `us-east-1`. For more information, see [Building runtime images](cmr-building-images.md).

1. To confirm that the image replicated, run the `describe-image-replication-status` command.

   ```bash
   aws ecr describe-image-replication-status \
     --region {{us-east-1}} \
     --repository-name {{companyphp8}} \
     --image-id imageTag={{v8.3.2}}
   ```

   You should see output similar to the following:

   ```json
   {
       "repositoryName": "companyphp8",
       "imageId": {
           "imageDigest": "sha256:4b2a9c1e8f3d7a6b5c0e9d8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9a8b",
           "imageTag": "v8.3.2"
       },
       "replicationStatuses": [
           {
               "region": "us-west-2",
               "registryId": "123456789012",
               "status": "COMPLETE"
           },
           {
               "region": "eu-west-1",
               "registryId": "123456789012",
               "status": "COMPLETE"
           }
       ]
   }
   ```

   Wait until the status for each destination Region is `COMPLETE` before you create runtime versions in those Regions.

### Step 2: Create the runtime in each Region
<a name="cmr-multi-region-create"></a>

In this step, you create a runtime with the same name in each Region. You need to complete this step only one time. For details about runtime properties, see [Creating a runtime](cmr-create.md).

#### Create the runtime in each Region (AWS CLI)
<a name="cmr-multi-region-create-cli"></a>

**To create the runtime in each Region (AWS CLI)**

1. To create the runtime in each Region, run the following script. The script runs the `create-runtime` command in each Region with the same name and description.

   ```bash
   for region in {{us-east-1 us-west-2 eu-west-1}}; do
     aws lambda-core create-runtime \
       --region "$region" \
       --name {{companyphp8}} \
       --description "{{PHP 8 runtime with company-approved extensions}}"
   done
   ```

   The output for each Region includes the runtime ARN for that Region. If the runtime already exists in a Region, the command fails in that Region.

1. To confirm that the runtime exists in each Region, run the `get-runtime` command in each Region.

   ```bash
   for region in {{us-east-1 us-west-2 eu-west-1}}; do
     aws lambda-core get-runtime \
       --region "$region" \
       --runtime-name {{companyphp8}} \
       --query Arn \
       --output text
   done
   ```

   You should see output similar to the following:

   ```text
   arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8
   arn:aws:lambda:us-west-2:123456789012:runtime/companyphp8
   arn:aws:lambda:eu-west-1:123456789012:runtime/companyphp8
   ```

To share the runtime with other accounts, update the resource-based policy in each Region. For more information, see [Sharing and controlling access to customer-managed runtimes](cmr-permissions.md).

### Step 3: Publish a version and update the alias one Region at a time
<a name="cmr-multi-region-deploy-update"></a>

In this step, you create runtime version `v8.3.2` in every Region. Then you point the `prod` alias to the new version, one Region at a time. Repeat this step for each new runtime release.

Creating the runtime version in every Region first doesn't affect any functions. Functions start to use the new version only after you update the alias. For more information, see [Runtime versions](cmr-versions.md) and [Runtime aliases](cmr-aliases.md).

#### Publish and roll out a version (AWS CLI)
<a name="cmr-multi-region-deploy-update-cli"></a>

**To publish and roll out a version in each Region (AWS CLI)**

1. To create the runtime version in each Region, run the following script. The script creates the version from the image in that Region's repository. It then waits until the version is `ACTIVE`.

   ```bash
   for region in {{us-east-1 us-west-2 eu-west-1}}; do
     aws lambda-core create-runtime-version \
       --region "$region" \
       --runtime-name {{companyphp8}} \
       --name {{v8.3.2}} \
       --image-uri "{{123456789012}}.dkr.ecr.$region.amazonaws.com/{{companyphp8}}:{{v8.3.2}}" \
       --release-notes "{{Updates PHP to 8.3.2.}}"
     aws lambda-core wait runtime-version-active \
       --region "$region" \
       --runtime-name {{companyphp8}} \
       --name {{v8.3.2}}
   done
   ```

   If a version enters the `FAILED` state, the waiter exits with an error. Don't update the alias in that Region. For more information, see [Runtime versions](cmr-versions.md).

1. To confirm the state of the version in each Region, run the `get-runtime-version` command.

   ```bash
   for region in {{us-east-1 us-west-2 eu-west-1}}; do
     echo -n "$region: "
     aws lambda-core get-runtime-version \
       --region "$region" \
       --runtime-name {{companyphp8}} \
       --name {{v8.3.2}} \
       --query State \
       --output text
   done
   ```

   You should see output similar to the following:

   ```text
   us-east-1: ACTIVE
   us-west-2: ACTIVE
   eu-west-1: ACTIVE
   ```

1. To update the `prod` alias one Region at a time, run the following script. After each Region, the script pauses so that you can check metrics before you continue.

   ```bash
   for region in {{us-east-1 us-west-2 eu-west-1}}; do
     echo "Updating alias prod in $region"
     aws lambda-core update-runtime-alias \
       --region "$region" \
       --runtime-name {{companyphp8}} \
       --name {{prod}} \
       --runtime-version {{v8.3.2}}
     read -p "Check the RuntimeInvocations and RuntimeInvocationErrors metrics in $region. Press Enter to continue, or Ctrl+C to stop. "
   done
   ```

   For the first release, the `prod` alias doesn't exist yet. Use the `create-runtime-alias` command with the same parameters instead. For more information, see [Runtime aliases](cmr-aliases.md).

1. While the script pauses, wait for your bake period. Then check the `RuntimeInvocations` and `RuntimeInvocationErrors` metrics for the runtime alias in that Region. For more information, see [Monitoring customer-managed runtimes](cmr-monitoring.md).

1. If the metrics are healthy, press **Enter** to continue to the next Region. If you find a problem, press **Ctrl\+C** to stop the rollout.

In a production pipeline, replace the manual pause with an automated bake period and alarm check. For more information, see [Automating multi-Region deployments](#cmr-multi-region-automation).

#### Roll back a Region
<a name="cmr-multi-region-rollback"></a>

If a Region shows problems after you update the alias, point the alias in that Region back to the previous runtime version. Functions pick up the previous version at their next cold start. Other Regions aren't affected.

**To roll back the alias in one Region (AWS CLI)**
+ To point the alias back to the previous version, run the `update-runtime-alias` command in the affected Region. The following example rolls back the `prod` alias in `us-west-2` to version `v8.3.1`.

  ```bash
  aws lambda-core update-runtime-alias \
    --region {{us-west-2}} \
    --runtime-name {{companyphp8}} \
    --name {{prod}} \
    --runtime-version {{v8.3.1}}
  ```

Roll back each Region that you already updated, as needed. For more information about rollbacks, see [Deploying runtime updates](cmr-deploy-updates.md).

### Step 4: Automate multi-Region deployments
<a name="cmr-multi-region-automate"></a>

After you set up replication and create the runtime in each Region, you can automate the rest of each release. For an overview of the options, see [Automating multi-Region deployments](#cmr-multi-region-automation).

#### Deploy with CloudFormation StackSets
<a name="cmr-multi-region-automate-stacksets"></a>

You can define the runtime resources in a CloudFormation template and deploy the template to each Region with StackSets. To stagger the rollout, deploy to one Region at a time and limit concurrent deployments.

#### Deploy with a pipeline
<a name="cmr-multi-region-automate-pipeline"></a>

A deployment pipeline for a multi-Region runtime typically includes the following stages:

1. Build the runtime image and push it to Amazon ECR in the source Region.

1. Wait until Amazon ECR replicates the image to each destination Region.

1. Create the runtime version in each Region, and wait until each version is `ACTIVE`.

1. Update the alias in one Region.

1. Wait for a bake period, and check the `RuntimeInvocations` and `RuntimeInvocationErrors` metrics in that Region.

1. Repeat the previous two stages for each remaining Region. Stop and roll back if a metric check fails.