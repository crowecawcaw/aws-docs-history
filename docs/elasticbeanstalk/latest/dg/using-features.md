# Preserving access to an Amazon Machine Image (AMI) for a retired platform

Elastic Beanstalk sets a platform branch status to _retired_ when the operating system or major component used by the branch
reaches End of Life. The _base_ Elastic Beanstalk AMI for the platform branch may also be made private to prevent the use of this
out-of-date AMI. Environments using AMIs that have been made private will no longer be able to launch instances.

If you're unable to migrate your application to a supported environment before it's retired, your environment may be in this situation. The need to
update an environment for a Beanstalk platform branch, where its base Elastic Beanstalk AMI has been made private, may arise. An alternative approach is available. You
can update an existing environment based on a _copy_ of the base Elastic Beanstalk AMI used by your environment.

This topic offers some steps and a standalone script to update an existing environment based on a _copy_ of the base
Elastic Beanstalk AMI used by your environment. Once you're able to migrate your application to a supported platform you can continue to use the standard
procedures for maintaining your application and supported environments.

## Manual steps

###### To update an environment based on an AMI copy of the base Elastic Beanstalk AMI

1. **Determine which AMI your environment is using.** This command returns the AMI used by the Elastic Beanstalk environment that
   you provide in the parameters. The returned value is used as the _source-ami-id_ in the next step.

In a command window, run a command like the following. For more information, see [describe-configuration-settings](../../../cli/latest/reference/elasticbeanstalk/describe-configuration-settings.md "../../../cli/latest/reference/elasticbeanstalk/describe-configuration-settings.md") in the
_AWS CLI Command Reference_.

Specify the AWS Region that stores the source AMI you want to copy. Replace the application name and environment name with those based on the
source AMI. Enter the text for the query parameter as shown.

```
>`aws elasticbeanstalk describe-configuration-settings \
 --application-name `my-application` \
 --environment-name `my-environment` \
 --region `us-east-2` \
 --query "ConfigurationSettings[0].OptionSettings[?OptionName=='ImageId'] | [0].Value"`

```

2. **Copy the AMI into your account.** This command returns the new AMI that results from copying the _source-ami-id_ that was returned in the prior step.

###### Note

Be sure to make a note of the new AMI id that is output by this command. You'll need to enter it in the next step, replacing _copied-ami-id_ in the example command.

In a command window, run a command like the following. For more information, see [copy-image](../../../cli/latest/reference/ec2/copy-image.md "../../../cli/latest/reference/ec2/copy-image.md") in the _AWS CLI Command Reference_.

Specify the AWS Region of the source AMI you want to copy (**--source-region**) and the Region where you want to
use your new custom AMI (**--region**). Replace _source-ami-id_ with the AMI of the
image that you're copying. The _source-ami-id_ was returned by the command in the prior step. Replace _new-ami-name_ with a name to describe the new AMI in the destination Region. The script that follows this procedure
generates the new AMI name by appending the string "_Copy of_" to the beginning of the name of the _source-ami-id._

```
>`aws ec2 copy-image \
 --region `us-east-2` \
 --source-image-id `source-ami-id` \
 --source-region `us-east-2` \
 --name `new-ami-name``

```

3. **Update an environment to use the copied AMI.** After the command runs it returns the status of the
   environment.

In a command window, run a command like the following. For more information, see [update-environment](../../../cli/latest/reference/elasticbeanstalk/update-environment.md "../../../cli/latest/reference/elasticbeanstalk/update-environment.md") in the _AWS CLI Command Reference_.

Specify the AWS Region of the environment and application you need to update. Replace the application name and environment name with those you
need to associate with the _copied-ami-id_ from the prior step. For the **--option-setttings** parameter, replace `copied-ami-id` with the AMI id you noted from the output of the prior
command.

```
>`aws elasticbeanstalk update-environment \
 --application-name `my-application` \
 --environment-name `my-environment` \
 --region `us-east-2` \
 --option-settings "Namespace=aws:autoscaling:launchconfiguration,OptionName=ImageId,Value=`copied-ami-id`"`

```

###### Note

To minimize storage costs, consider cleaning up your custom AMI when you don't need it to launch Elastic Beanstalk environments anymore. For more information,
see [Cleaning up a custom AMI](using-features.md#using-features.customenv.cleanup "using-features.md#using-features.customenv.cleanup").

## Standalone script

The following script provides the same results as the previous manual steps. Download the script by selecting this link: [copy_ami_and_update_env.zip](samples/copy_ami_and_update_env.md "samples/copy_ami_and_update_env.md").

```
#!/bin/bash

set -ue

USAGE="This script is used to copy an AMI used by your Elastic Beanstalk environment into your account to use in your environment.\n\n"
USAGE+="Usage:\n\n"
USAGE+="./$(basename $0) [OPTIONS]\n"
USAGE+="OPTIONS:\n"
USAGE+="\t--application-name <application-name>\tThe name of your Elastic Beanstalk application.\n"
USAGE+="\t--environment-name <environment-name>\tThe name of your Elastic Beanstalk environment.\n"
USAGE+="\t--region <region> \t\t\tThe AWS region your Elastic Beanstalk environment is deployed to.\n"
USAGE+="\n\n"
USAGE+="Script Usage Example(s):\n"
USAGE+="./$(basename $0) --application-name my-application --environment-name my-environment --region us-east-1\n"

if [ $# -eq 0 ]; then
  echo -e $USAGE
  exit
fi

while [[ $# -gt 0 ]]; do
  case $1 in
    --application-name)       APPLICATION_NAME="$2"; shift ;;
    --environment-name)       ENVIRONMENT_NAME="$2"; shift ;;
    --region)                 REGION="$2"; shift ;;
    *)                        echo "Unknown option $1" ; echo -e $USAGE ; exit ;;
  esac
  shift
done

aws_cli_version="$(aws --version)"
if [ $? -ne 0 ]; then
  echo "aws CLI not found. Please install it: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html. Exiting."
  exit 1
fi
echo "Using aws CLI version: ${aws_cli_version}"

account=$(aws sts get-caller-identity --query "Account" --output text)
echo "Using account ${account}"

environment_ami_id=$(aws elasticbeanstalk describe-configuration-settings \
  --application-name "$APPLICATION_NAME" \
  --environment-name "$ENVIRONMENT_NAME" \
  --region "$REGION" \
  --query "ConfigurationSettings[0].OptionSettings[?OptionName=='ImageId'] | [0].Value" \
  --output text)
echo "Image associated with environment ${ENVIRONMENT_NAME} is ${environment_ami_id}"

owned_image=$(aws ec2 describe-images \
  --owners self \
  --image-ids "$environment_ami_id" \
  --region "$REGION" \
  --query "Images[0]" \
  --output text)
if [ "$owned_image" != "None" ]; then
  echo "${environment_ami_id} is already owned by account ${account}. Exiting."
  exit
fi

source_image_name=$(aws ec2 describe-images \
  --image-ids "$environment_ami_id" \
  --region "$REGION" \
  --query "Images[0].Name" \
  --output text)
if [ "$source_image_name" = "None" ]; then
  echo "Cannot find ${environment_ami_id}. Please contact AWS support if you need additional help: https://aws.amazon.com/support."
  exit 1
fi

copied_image_name="Copy of ${source_image_name}"
copied_ami_id=$(aws ec2 describe-images \
  --owners self \
  --filters Name=name,Values="${copied_image_name}" \
  --region "$REGION" \
  --query "Images[0].ImageId" \
  --output text)
if [ "$copied_ami_id" != "None" ]; then
  echo "Detected that ${environment_ami_id} has already been copied by account ${account}. Skipping image copy."
else
  echo "Copying ${environment_ami_id} to account ${account} with name ${copied_image_name}"
  copied_ami_id=$(aws ec2 copy-image \
    --source-image-id "$environment_ami_id" \
    --source-region "$REGION" \
    --name "$copied_image_name" \
    --region "$REGION" \
    --query "ImageId" \
    --output text)
  echo "New AMI ID is ${copied_ami_id}"

  echo "Waiting for ${copied_ami_id} to become available"
  aws ec2 wait image-available \
    --image-ids "$copied_ami_id" \
    --region "$REGION"
  echo "${copied_ami_id} is now available"
fi

echo "Updating environment ${ENVIRONMENT_NAME} to use ${copied_ami_id}"
environment_status=$(aws elasticbeanstalk update-environment \
  --application-name "$APPLICATION_NAME" \
  --environment-name "$ENVIRONMENT_NAME" \
  --option-settings "Namespace=aws:autoscaling:launchconfiguration,OptionName=ImageId,Value=${copied_ami_id}" \
  --region "$REGION" \
  --query "Status" \
  --output text)
echo "Environment ${ENVIRONMENT_NAME} is now ${environment_status}"

echo "Waiting for environment ${ENVIRONMENT_NAME} update to complete"
aws elasticbeanstalk wait environment-updated \
  --application-name "$APPLICATION_NAME" \
  --environment-names "$ENVIRONMENT_NAME" \
  --region "$REGION"
echo "Environment ${ENVIRONMENT_NAME} update complete"
```

###### Note

You must have the AWS CLI installed to execute the script. For installation instructions, see [Install or update the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the
_AWS Command Line Interface User Guide_.

After installing the AWS CLI, you must also configure it to use the AWS account that owns the environment. For more information, see [Configure the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md") in the _AWS Command Line Interface User Guide_. The
account must also have permissions to create an AMI and update the Elastic Beanstalk environment.

These steps describe the process that the script follows.

1. Print the account in use.
2. Determine which AMI is used by the environment (source AMI).
3. Check if the source AMI is already owned by the account. If yes, exit.
4. Determine the name of the source AMI so it can be used in the new AMI name. This also serves to confirm access to the source AMI.
5. Check if the source AMI has already been copied to the account. This is done by searching for AMIs with the name of the copied AMI owned by the
   account. If the AMI name has been changed in between script executions, it will copy the image again.
6. If the source AMI has not already been copied, copy the source AMI to the account and wait for the new AMI to be available.
7. Update the environment configuration to use the new AMI.
8. Wait for the environment update to complete.

After you extract the script from the [copy_ami_and_update_env.zip](samples/copy_ami_and_update_env.md "samples/copy_ami_and_update_env.md") file, run it by executing the following
example. Replace the application name and environment name in the example with your own values.

```
>`sh copy_ami_and_update_env.sh \
 --application-name `my-application` \
 --environment-name `my-environment` \
 --region `us-east-1``
```

###### Note

To minimize storage costs, consider cleaning up your custom AMI when you don't need it to launch Elastic Beanstalk environments anymore. For more information,
see [Cleaning up a custom AMI](using-features.md#using-features.customenv.cleanup "using-features.md#using-features.customenv.cleanup").
