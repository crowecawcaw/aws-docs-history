# Work with a staging distribution and continuous deployment policy

You can create, update, and modify staging distributions and continuous deployment
policies in the CloudFront console, with the AWS Command Line Interface (AWS CLI), or with the
CloudFront API.

## Create a staging distribution with a continuous deployment policy

The following procedures show you how to create a staging distribution with a continuous deployment policy.

Console
You can create a staging distribution with a continuous deployment policy
by using the AWS Management Console.

###### To create a staging distribution and continuous deployment policy

(console)

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose
   **Distributions**.
3. Choose the distribution that you want to use as the _primary distribution_. The primary
   distribution is one that currently serves production traffic, the
   one from which you will create the staging distribution.
4. In the **Continuous deployment** section, choose
   **Create staging distribution**. This opens the
   **Create staging distribution** wizard.
5. In the **Create staging distribution** wizard, do
   the following:
   1. (Optional) Type a description for the staging
      distribution.
   2. Choose **Next**.
   3. Modify the configuration of the staging distribution. For
      more information about the settings that you can update, see
      [Update primary and
      staging distributions](understanding-continuous-deployment.md#updating-staging-and-primary-distributions "understanding-continuous-deployment.md#updating-staging-and-primary-distributions").

   When you are finished modifying the staging distribution's
   configuration, choose **Next**. 4. Use the console to specify the **Traffic
   configuration**. This determines how CloudFront routes
   traffic to the staging distribution. (CloudFront stores the
   traffic configuration in a _continuous deployment policy_.)

   For more information about the options in a
   **Traffic configuration**, see [Route requests to
   the staging distribution](understanding-continuous-deployment.md#understanding-continuous-deployment-routing "understanding-continuous-deployment.md#understanding-continuous-deployment-routing").

   When you are finished with the **Traffic
   configuration**, choose
   **Next**. 5. Review the configuration for the staging distribution,
   including the traffic configuration, then choose
   **Create staging distribution**.

When you finish the **Create staging distribution**
wizard in the CloudFront console, CloudFront does the following:

- Creates a staging distribution with the settings that you
  specified (in step 5c)
- Creates a continuous deployment policy with the traffic
  configuration that you specified (in step 5d)
- Attaches the continuous deployment policy to the primary
  distribution that you created the staging distribution from

When the primary distribution's configuration, with the attached
continuous deployment policy, deploys to edge locations, CloudFront begins sending
the specified portion of traffic to the staging distribution based on the
traffic configuration.

CLI
To create a staging distribution and a continuous deployment policy
with the AWS CLI, use the following procedures.

###### To create a staging distribution (CLI)

1. Use the **aws cloudfront get-distribution** and
   **grep** commands together to get the
   `ETag` value of the distribution that you want to use as
   the _primary distribution_. The
   primary distribution is one that currently serves production
   traffic, from which you will create the staging distribution.

The following command shows an example. In the following example,
replace `primary_distribution_ID` with the
ID of the primary distribution.

```

aws cloudfront get-distribution --id `primary_distribution_ID` | grep 'ETag'
```

Copy the `ETag` value because you need it for the
following step. 2. Use the **aws cloudfront copy-distribution**
command to create a staging distribution. The following example
command uses escape characters (\) and line breaks for readability,
but you should omit these from the command. In the following example
command:

    * Replace `primary_distribution_ID`
     with the ID of the primary distribution.
    * Replace
     `primary_distribution_ETag` with
     the `ETag` value of the primary distribution
     (that you got in the previous step).
    * (Optional) Replace `CLI_example`
     with the desired caller reference ID.

```

aws cloudfront copy-distribution --primary-distribution-id `primary_distribution_ID` \
                                 --if-match `primary_distribution_ETag` \
                                 --staging \
                                 --caller-reference '`CLI_example`'
```

The command's output shows information about the staging
distribution and its configuration. Copy the staging distribution's
CloudFront domain name because you need it for a following step.

###### To create a continuous deployment policy (CLI with input

file)

1. Use the following command to create file named
   `continuous-deployment-policy.yaml` that contains
   all of the input parameters for the
   **create-continuous-deployment-policy** command. The
   following command uses escape characters (\) and line breaks for
   readability, but you should omit these from the command.

```

aws cloudfront create-continuous-deployment-policy --generate-cli-skeleton yaml-input \
                                                   > continuous-deployment-policy.yaml
```

2.  Open the file named
    `continuous-deployment-policy.yaml` that you just
    created. Edit the file to specify the continuous deployment policy
    settings that you want, then save the file. When you edit the
    file:
    - In the `StagingDistributionDnsNames`
      section:
      - Change the value of `Quantity` to
        `1`.
      - For `Items`, paste the CloudFront domain name
        of the staging distribution (that you saved from a
        previous step).

    - In the `TrafficConfig` section:

          + Choose a `Type`, either
           `SingleWeight` or
           `SingleHeader`.
          + Remove the settings for the other type. For
           example, if you want a weight-based traffic
           configuration, set `Type` to
           `SingleWeight` and then remove the
           `SingleHeaderConfig` settings.
          + To use a weight-based traffic configuration, set
           the value of `Weight` to a decimal number
           between `.01` (one percent) and
           `.15` (fifteen percent).

      For more information about the options in
      `TrafficConfig`, see [Route requests to
      the staging distribution](understanding-continuous-deployment.md#understanding-continuous-deployment-routing "understanding-continuous-deployment.md#understanding-continuous-deployment-routing") and
      [Session stickiness
      for weight-based configurations](understanding-continuous-deployment.md#understanding-continuous-deployment-sessions "understanding-continuous-deployment.md#understanding-continuous-deployment-sessions").

3.  Use the following command to create the continuous deployment
    policy using input parameters from the
    `continuous-deployment-policy.yaml` file.

```

aws cloudfront create-continuous-deployment-policy --cli-input-yaml file://continuous-deployment-policy.yaml
```

Copy the `Id` value in the command's output. This is
the continuous deployment policy ID, and you need it in a following
step.

###### To attach a continuous deployment policy to a primary distribution

(CLI with input file)

1. Use the following command to save the primary distribution's
   configuration to a file named
   `primary-distribution.yaml`. Replace
   `primary_distribution_ID` with the primary
   distribution's ID.

```

aws cloudfront get-distribution-config --id `primary_distribution_ID` --output yaml > primary-distribution.yaml
```

2.  Open the file named `primary-distribution.yaml`
    that you just created. Edit the file, making the following
    changes:

        * Paste the continuous deployment policy ID (that you copied
         from a previous step) into the
         `ContinuousDeploymentPolicyId` field.
        * Rename the `ETag` field to
         `IfMatch`, but don't change the field's
         value.

    Save the file when finished.

3.  Use the following command to update the primary distribution to
    use the continuous deployment policy. Replace
    `primary_distribution_ID` with the primary
    distribution's ID.

```

aws cloudfront update-distribution --id `primary_distribution_ID` --cli-input-yaml file://primary-distribution.yaml
```

When the primary distribution's configuration, with the attached
continuous deployment policy, deploys to edge locations, CloudFront begins sending
the specified portion of traffic to the staging distribution based on the
traffic configuration.

API
To create a staging distribution and continuous deployment policy with the
CloudFront API, use the following API operations:

- [CopyDistribution](../../../cloudfront/latest/APIReference/API_CopyDistribution.md "../../../cloudfront/latest/APIReference/API_CopyDistribution.md")
- [CreateContinuousDeploymentPolicy](../../../cloudfront/latest/APIReference/API_CreateContinuousDeploymentPolicy.md "../../../cloudfront/latest/APIReference/API_CreateContinuousDeploymentPolicy.md")

For more information about the fields that you specify in these API calls,
see the following:

- [Route requests to
  the staging distribution](understanding-continuous-deployment.md#understanding-continuous-deployment-routing "understanding-continuous-deployment.md#understanding-continuous-deployment-routing")
- [Session stickiness
  for weight-based configurations](understanding-continuous-deployment.md#understanding-continuous-deployment-sessions "understanding-continuous-deployment.md#understanding-continuous-deployment-sessions")
- The API reference documentation for your AWS SDK or other API
  client

After you create a staging distribution and a continuous deployment
policy, use [UpdateDistribution](../../../cloudfront/latest/APIReference/API_UpdateDistribution.md "../../../cloudfront/latest/APIReference/API_UpdateDistribution.md") (on the primary distribution) to attach the
continuous deployment policy to the primary distribution.

## Update a staging distribution

The following procedures show you how to update a staging distribution with a continuous deployment policy.

Console
You can update certain configurations for both the primary and staging distributions. For more information, see [Update primary and
staging distributions](understanding-continuous-deployment.md#updating-staging-and-primary-distributions "understanding-continuous-deployment.md#updating-staging-and-primary-distributions").

###### To update a staging distribution (console)

1. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose
   **Distributions**.
3. Choose the primary distribution. This is the distribution that
   currently serves production traffic, the one from which you created
   the staging distribution.
4. Choose **View staging distribution**.
5. Use the console to modify the configuration of the staging
   distribution. For more information about the settings that you can
   update, see [Update primary and
   staging distributions](understanding-continuous-deployment.md#updating-staging-and-primary-distributions "understanding-continuous-deployment.md#updating-staging-and-primary-distributions").

As soon as the staging distribution's configuration deploys to edge
locations it takes effect for incoming traffic that's routed to the staging
distribution.

CLI

###### To update a staging distribution (CLI with input file)

1. Use the following command to save the staging distribution's
   configuration to a file named
   `staging-distribution.yaml`. Replace
   `staging_distribution_ID` with the staging
   distribution's ID.

```

aws cloudfront get-distribution-config --id `staging_distribution_ID` --output yaml > staging-distribution.yaml
```

2.  Open the file named `staging-distribution.yaml`
    that you just created. Edit the file, making the following
    changes:

        * Modify the configuration of the staging distribution. For
         more information about the settings that you can update, see
         [Update primary and
         staging distributions](understanding-continuous-deployment.md#updating-staging-and-primary-distributions "understanding-continuous-deployment.md#updating-staging-and-primary-distributions").
        * Rename the `ETag` field to
         `IfMatch`, but don't change the field's
         value.

    Save the file when finished.

3.  Use the following command to update the staging distribution's
    configuration. Replace
    `staging_distribution_ID` with the staging
    distribution's ID.

```

aws cloudfront update-distribution --id `staging_distribution_ID` --cli-input-yaml file://staging-distribution.yaml
```

As soon as the staging distribution's configuration deploys to edge
locations it takes effect for incoming traffic that's routed to the staging
distribution.

API
To update the configuration of a staging distribution, use [UpdateDistribution](../../../cloudfront/latest/APIReference/API_UpdateDistribution.md "../../../cloudfront/latest/APIReference/API_UpdateDistribution.md") (on the staging distribution) to modify the
configuration of the staging distribution. For more information about the
settings that you can update, see [Update primary and
staging distributions](understanding-continuous-deployment.md#updating-staging-and-primary-distributions "understanding-continuous-deployment.md#updating-staging-and-primary-distributions").

## Update a continuous deployment policy

The following procedures show you how to update a continuous deployment policy.

Console
You can update your distribution's traffic configuration by updating the continuous deployment policy.

###### To update a continuous deployment policy (console)

1. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose
   **Distributions**.
3. Choose the primary distribution. This is the distribution that
   currently serves production traffic, the one from which you created
   the staging distribution.
4. In the **Continuous deployment** section, choose
   **Edit policy**.
5. Modify the traffic configuration in the continuous deployment
   policy. When you are finished, choose **Save
   changes**.

When the primary distribution's configuration with the updated continuous
deployment policy deploys to edge locations, CloudFront begins sending traffic to
the staging distribution based on the updated traffic configuration.

CLI

###### To update a continuous deployment policy (CLI with input

file)

1. Use the following command to save the continuous deployment
   policy's configuration to a file named
   `continuous-deployment-policy.yaml`. Replace
   `continuous_deployment_policy_ID` with the
   continuous deployment policy's ID. The following command uses escape
   characters (\) and line breaks for readability, but you should omit
   these from the command.

```

aws cloudfront get-continuous-deployment-policy-config --id `continuous_deployment_policy_ID` \
                                                       --output yaml > continuous-deployment-policy.yaml
```

2.  Open the file named
    `continuous-deployment-policy.yaml` that you just
    created. Edit the file, making the following changes:

        * Modify the configuration of the continuous deployment
         policy as desired. For example, you can change from using a
         header-based to a weight-based traffic configuration, or you
         can change the percentage of traffic (weight) for a
         weight-based configuration. For more information, see [Route requests to
         the staging distribution](understanding-continuous-deployment.md#understanding-continuous-deployment-routing "understanding-continuous-deployment.md#understanding-continuous-deployment-routing") and
         [Session stickiness
         for weight-based configurations](understanding-continuous-deployment.md#understanding-continuous-deployment-sessions "understanding-continuous-deployment.md#understanding-continuous-deployment-sessions").
        * Rename the `ETag` field to
         `IfMatch`, but don't change the field's
         value.

    Save the file when finished.

3.  Use the following command to update the continuous deployment
    policy. Replace
    `continuous_deployment_policy_ID` with the
    continuous deployment policy's ID. The following command uses escape
    characters (\) and line breaks for readability, but you should omit
    these from the command.

```

aws cloudfront update-continuous-deployment-policy --id `continuous_deployment_policy_ID` \
                                                   --cli-input-yaml file://continuous-deployment-policy.yaml
```

When the primary distribution's configuration with the updated continuous
deployment policy deploys to edge locations, CloudFront begins sending traffic to
the staging distribution based on the updated traffic configuration.

API
To update a continuous deployment policy, use [UpdateContinuousDeploymentPolicy](../../../cloudfront/latest/APIReference/API_UpdateContinuousDeploymentPolicy.md "../../../cloudfront/latest/APIReference/API_UpdateContinuousDeploymentPolicy.md").

## Promote a staging distribution configuration

The following procedures show you how to promote a staging distribution configuration.

Console
When you _promote_ a staging
distribution, CloudFront copies the configuration from the staging distribution to
the primary distribution. CloudFront also disables the continuous deployment
policy and routes all traffic to the primary distribution.

After you promote a configuration, you can reuse the same staging
distribution the next time you want to test a configuration change.

###### To promote a staging distribution's configuration (console)

1. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose
   **Distributions**.
3. Choose the primary distribution. This is the distribution that
   currently serves production traffic, the one from which you created
   the staging distribution.
4. In the **Continuous deployment** section, choose
   **Promote**.
5. Type `confirm` and then choose
   **Promote**.

CLI
When you _promote_ a staging
distribution, CloudFront copies the configuration from the staging distribution to
the primary distribution. CloudFront also disables the continuous deployment
policy and routes all traffic to the primary distribution.

After you promote a configuration, you can reuse the same staging
distribution the next time you want to test a configuration change.

###### To promote a staging distribution's configuration (CLI)

- Use the **aws cloudfront
  update-distribution-with-staging-config** command to promote
  the staging distribution's configuration to the primary
  distribution. The following example command uses escape characters
  (\) and line breaks for readability, but you should omit these from
  the command. In the following example command:
  - Replace `primary_distribution_ID`
    with the ID of the primary distribution.
  - Replace `staging_distribution_ID`
    with the ID of the staging distribution.
  - Replace
    `primary_distribution_ETag` and
    `staging_distribution_ETag` with
    the `ETag` values of the primary and staging
    distributions. Make sure the primary distribution's value is
    first, as shown in the example.

```

aws cloudfront update-distribution-with-staging-config --id `primary_distribution_ID` \
                                                       --staging-distribution-id `staging_distribution_ID` \
                                                       --if-match '`primary_distribution_ETag`,`staging_distribution_ETag`'
```

API
To promote a staging distribution's configuration to the primary
distribution, use [UpdateDistributionWithStagingConfig](../../../cloudfront/latest/APIReference/API_UpdateDistributionWithStagingConfig.md "../../../cloudfront/latest/APIReference/API_UpdateDistributionWithStagingConfig.md").
