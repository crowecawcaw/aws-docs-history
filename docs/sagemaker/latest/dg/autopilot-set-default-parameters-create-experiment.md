# Configure the default

parameters of an Autopilot experiment (for administrators)

Autopilot supports setting default values to simplify the configuration of Amazon SageMaker Autopilot when you
create an Autopilot experiment using the Studio Classic UI. Administrators can use Studio Classic [lifecycle configurations](studio-lcc.md "studio-lcc.md") (LCC) to set infrastructure,
networking, and security values in configuration files and pre-populate the [advanced settings](autopilot-automate-model-development-create-experiment-ui.md#advanced-settings "autopilot-automate-model-development-create-experiment-ui.md#advanced-settings") of `AutoML` jobs.

By doing so, they can fully control network connectivity and access permissions for the
resources associated with Amazon SageMaker Studio Classic, including SageMaker AI instances, data sources, output data,
and other related services. Specifically, administrators can configure a desired network
architecture, such as Amazon VPC, subnets, and security groups, for a Studio Classic domain or
individual user profiles. Data scientists can focus on data science specific parameters when
creating their Autopilot experiments using the Studio Classic UI. Furthermore, administrators can
manage the encryption of data on the instance in which Autopilot experiments run by setting
default encryption keys.

###### Note

This feature is currently not available in the Asia Pacific (Hong Kong) and Middle East
(Bahrain) opt-in Regions.

In the following sections, you can find the full list of parameters supporting the setting
of defaults when creating an Autopilot experiment using the Studio Classic UI, and learn how to set
those default values.

###### Topics

- [List of default
  parameters supported](#autopilot-list-default-parameters-create-experiment "#autopilot-list-default-parameters-create-experiment")
- [Set default
  Autopilot experiment parameters](#autopilot-set-default-parameters-create-experiment-howto "#autopilot-set-default-parameters-create-experiment-howto")

## List of default

parameters supported

The following parameters support setting default values with a configuration file for
creating an Autopilot experiment using the Studio Classic UI. Once set, the values automatically
fill in their corresponding field in the Autopilot' **Create Experiment** tab
in the Studio Classic UI. See [Advanced settings
(optional)](autopilot-automate-model-development-create-experiment-ui.md#advanced-settings "autopilot-automate-model-development-create-experiment-ui.md#advanced-settings") for a full description of each field.

- **Security:** Amazon VPC, subnets, and security
  groups.
- **Access:** AWS IAM role ARNs.
- **Encryption:** AWS KMS key IDs.
- **Tags:** Key-value pairs used to label and organize
  SageMaker AI resources.

## Set default

Autopilot experiment parameters

Administrators can set default values in a configuration file, then manually place the
file in a recommended location within the Studio Classic environment of specific users, or they
can pass the file to a lifecycle configuration script (LCC) to automate the customization of
the Studio Classic environment for a given domain or user profile.

- To set up the configuration file, start by filling in its default parameters.

To configure any or all default values listed in [List of default
parameters supported](#autopilot-list-default-parameters-create-experiment "#autopilot-list-default-parameters-create-experiment"), administrators
can create a configuration file named `config.yaml`, the structure of which
should adhere to this [sample configuration file](https://sagemaker.readthedocs.io/en/stable/overview.html#configuration-file-structure "https://sagemaker.readthedocs.io/en/stable/overview.html#configuration-file-structure"). The following snippet shows a sample configuration
file with all the supported `AutoML` parameters. For more information on the
format of this file, refer to the [full schema](https://github.com/aws/sagemaker-python-sdk/blob/master/src/sagemaker/config/config_schema.py "https://github.com/aws/sagemaker-python-sdk/blob/master/src/sagemaker/config/config_schema.py").

```
SchemaVersion: '1.0'
SageMaker:
  AutoMLJob:
    # https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html
    AutoMLJobConfig:
      SecurityConfig:
        EnableInterContainerTrafficEncryption: true
        VolumeKmsKeyId: '`kms-key-id`'
        VpcConfig:
          SecurityGroupIds:
            - '`security-group-id-1`'
            - '`security-group-id-2`'
          Subnets:
            - '`subnet-1`'
            - '`subnet-2`'
    OutputDataConfig:
      KmsKeyId: '`kms-key-id`'
    RoleArn: '`arn:aws:iam::111222333444:role/Admin`'
    Tags:
    - Key: '`tag_key`'
      Value: '`tag_value`'
```

- Then, place the configuration file in the recommended location by either [manually copying the file](#autopilot-intelligent-defaults-manual-setup "#autopilot-intelligent-defaults-manual-setup")
  to its recommended paths or using a [lifecycle configuration](#autopilot-intelligent-defaults-lcc-setup "#autopilot-intelligent-defaults-lcc-setup")
  (LCC).

The configuration file needs to be present in at least one of the following
locations in the user's Studio Classic environment. By default, SageMaker AI searches for a
configuration file in two locations:

    + First, in `/etc/xdg/sagemaker/config.yaml`. We refer to this file as
     the *administrator configuration file*.
    + Then, in `/root/.config/sagemaker/config.yaml`. We refer to this file
     as the *user configuration file*.

Using the _administrator_ configuration file,
administrators can define a set of default values. Optionally, they can use the
_user_ configuration file to override values set in
the _administrator_ configuration file, or set
additional default parameter values.

The following snippet shows a sample script
which writes the default parameters configuration file to the _administrator_ location in the user's Studio Classic environment. You can
replace `/etc/xdg/sagemaker` with `/root/.config/sagemaker` to
write the file to the _user_ location.

```
## Sample script with AutoML intelligent defaults
#!/bin/bash

sudo mkdir -p /etc/xdg/sagemaker

echo "SchemaVersion: '1.0'
CustomParameters:
  AnyStringKey: 'AnyStringValue'
SageMaker:
  AutoMLJob:
    # https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html
    AutoMLJobConfig:
      SecurityConfig:
        EnableInterContainerTrafficEncryption: true
        VolumeKmsKeyId: '`kms-key-id`'
        VpcConfig:
          SecurityGroupIds:
            - '`security-group-id-1`'
            - '`security-group-id-2`'
          Subnets:
            - '`subnet-1`'
            - '`subnet-2`'
    OutputDataConfig:
      KmsKeyId: '`kms-key-id`'
    RoleArn: '`arn:aws:iam::111222333444:role/Admin`'
    Tags:
    - Key: '`tag_key`'
      Value: '`tag_value`'
" | sudo tee /etc/xdg/sagemaker/config.yaml
```

    + **Copy the files
     manually** – To copy the configuration files manually, run the
     [script](#autopilot-intelligent-defaults-manual-setup "#autopilot-intelligent-defaults-manual-setup") created
     in the previous step from a Studio Classic terminal. In this case, the user profile that
     executed the script can create Autopilot experiments with the default values applicable
     only to them.
    + **Create a SageMaker AI lifecycle configuration** –
     Alternatively, you can use a [lifecycle configuration](studio-lcc.md "studio-lcc.md") (LCC) to
     automate the customization of your Studio Classic environment. LCC are shell scripts
     triggered by Amazon SageMaker Studio Classic lifecycle events such as starting a Studio Classic
     application. This customization includes installing custom packages, configuring
     notebook extensions, pre-loading datasets, setting up source code repositories, or,
     in our case, pre-populating default parameters. Administrators can attach the LCC to
     a Studio Classic domain to automate the configuration of default values for each
     user profile within that domain.


    The following sections detail how to create a lifecycle configuration so users
     can load Autopilot default parameters automatically when launching Studio Classic. You can
     choose to create an LCC using the SageMaker AI Console or the AWS CLI.



    Create a LCC from the SageMaker AI Console
    Use the following steps to create an LCC containing your default
     parameters, attach the LCC to a domain or a user profile, then launch a
     Studio Classic application pre-populated with the default parameters set by the
     LCC using the SageMaker AI Console.




    	- **To create a lifecycle configuration that runs
    	 the [script](#autopilot-intelligent-defaults-script "#autopilot-intelligent-defaults-script")
    	 containing your default values using the SageMaker AI Console**




    		* Open the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
    		* On the left side, navigate to **Admin
    		 configurations**, then **Lifecycle
    		 configurations**.
    		* From the **Lifecycle configurations** page,
    		 navigate to the Studio Classic tab, then choose **Create
    		 configuration**.
    		* For **Name**, type a name using alphanumeric
    		 characters and "-", but no spaces. The name can have a maximum of 63
    		 characters.
    		* Paste your [script](#autopilot-intelligent-defaults-script "#autopilot-intelligent-defaults-script") in the **Scripts** section.
    		* Choose **Create configuration** to create the
    		 lifecycle configuration. This creates an LCC of type `Kernel
    		 gateway app`.
    	- **To attach the lifecycle configuration to a
    	 Studio Classic domain, a space, or a user profile**


    	Follow the steps in [Attach the lifecycle configuration to Studio Classic domain or user
    	 profile](studio-lcc-create-console.md#studio-lcc-create-console-step2 "studio-lcc-create-console.md#studio-lcc-create-console-step2")  to attach your LCC to a Studio Classic domain or a
    	 specific user profile.
    	- **To launch your Studio Classic application with the
    	 lifecycle configuration**


    	Once the LCC is attached to a domain or a user profile, impacted
    	 users can start a Studio Classic application from the landing page of
    	 Studio Classic in Studio to pick up the defaults set by the LCC
    	 automatically. This auto-populates the Studio Classic UI when creating an
    	 Autopilot experiment.

    Create a LCC from the AWS CLI
    Use the following snippets to launch a Studio Classic application that runs
     your [script](#autopilot-intelligent-defaults-manual-setup "#autopilot-intelligent-defaults-manual-setup")
     using the AWS CLI. Note that `lifecycle_config.sh` is the name given
     to your script in this example.


    Before getting started:




    	- Ensure that you have updated and configured AWS CLI by completing the
    	 prerequisites described in [Create a lifecycle
    	 configuration from the AWS CLI](studio-lcc-create-cli.md "studio-lcc-create-cli.md").
    	- Install [OpenSSL](https://www.openssl.org/source/ "https://www.openssl.org/source/")
    	 documentation. The AWS CLI command uses the open-source library *OpenSSL* to encode your script in Base64 format.
    	 This requirement prevents errors that occur from spacing and line break
    	 encoding.
    You can now follow these three steps:




    	- **Create a new lifecycle configuration referencing the
    	 configuration script `lifecycle_config.sh`**



    	```
    	LCC_CONTENT=`openssl base64 -A -in `lifecycle_config.sh``

    	## Create a new lifecycle config
    	aws sagemaker create-studio-lifecycle-config --region `region` \
    	--studio-lifecycle-config-name `lcc-name` \
    	--studio-lifecycle-config-content $LCC_CONTENT \
    	--studio-lifecycle-config-app-type default
    	```

    	Note the ARN of the newly created lifecycle configuration that is
    	 returned. This ARN is required to attach the lifecycle configuration to
    	 your application.
    	- **Attach the lifecycle configuration to your
    	 `JupyterServerApp`**


    	The following example shows how to create a new user profile with a
    	 lifecycle configuration attached. To update an existing user profile, use
    	 the AWS CLI [update-user-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-user-profile.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-user-profile.html") command. To create or update a domain,
    	 see [create-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-domain.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-domain.html") and [update-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-domain.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-domain.html"). Add the lifecycle configuration ARN from the
    	 previous step to the settings of the `JupyterServerAppSettings`
    	 application type. You can add multiple lifecycle configurations at the
    	 same time by using a list of lifecycle configurations.



    	```
    	# Create a new UserProfile
    	aws sagemaker create-user-profile --domain-id `domain-id` \
    	--user-profile-name `user-profile-name` \
    	--region `region` \
    	--user-settings '{
    	"JupyterServerAppSettings": {
    	  "LifecycleConfigArns":
    	    ["`lifecycle-configuration-arn`"]
    	  }
    	}'
    	```

    	Once the LCC is attached to a domain or a user profile, impacted
    	 users can shut down and update their existing Studio Classic application by
    	 following the steps in [Shut down and
    	 Update Amazon SageMaker Studio Classic](studio-tasks-update-studio.md "studio-tasks-update-studio.md"), or start a new Studio Classic application
    	 from the AWS Console to pick up the defaults set by the LCC
    	 automatically. This auto-populates the Studio Classic UI when creating an
    	 Autopilot experiment. Alternatively, they can launch a new Studio Classic
    	 application using the AWS CLI as follows.
    	- **Launch your Studio Classic application with the
    	 lifecycle configuration using the AWS CLI**



    	```
    	# Create a Jupyter Server application
    	aws sagemaker create-app --domain-id `domain-id` \
    	--user-profile-name `user-profile-name` \
    	--region `region` \
    	--app-type JupyterServer \
    	--resource-spec LifecycleConfigArn=`lifecycle-configuration-arn` \
    	--app-name default
    	```

    	For more information on creating a lifecycle configuration using the
    	 AWS CLI, see [Create a Lifecycle
    	 Configuration from the AWS CLI](studio-lcc-create-cli.md "studio-lcc-create-cli.md").
