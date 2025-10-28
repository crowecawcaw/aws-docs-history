# Set up and configure the AWS CLI

for Lightsail operations

The AWS Command Line Interface (AWS CLI) is a tool that allows advanced users and developers to control the
Amazon Lightsail service by typing commands in the terminal (on Linux and Unix) or Command Prompt
(on Windows). You can also control Lightsail using the Lightsail console, a graphical user
interface, and the Lightsail application program interface (API).

###### Tip

You can also use AWS CloudShell to manage your Lightsail resources by running AWS CLI commands
without downloading or installing command line tools. CloudShell is a browser-based,
pre-authenticated shell that you can launch directly from the Lightsail console. For more
information, see [Manage Lightsail resources with
AWS CloudShell](amazon-lightsail-cloudshell.md "amazon-lightsail-cloudshell.md").

###### Topics

- [Step 1: Install the AWS CLI](#lightsail-install-the-cli "#lightsail-install-the-cli")
- [Step 2: Create a new access
  key](#set-up-access-keys-create-new-access-key "#set-up-access-keys-create-new-access-key")
- [Step 3: Configure the AWS CLI](#set-up-access-keys- "#set-up-access-keys-")
- [Next steps](#set-up-access-keys-next-steps "#set-up-access-keys-next-steps")

## Step 1: Install the AWS CLI

You can install the AWS CLI on your local desktop or install it on your Lightsail
instance. For more information about the AWS CLI, see [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").

- To install the AWS CLI on your local desktop, see [Installing the
  AWS CLI](../../../cli/latest/userguide/installing.md "../../../cli/latest/userguide/installing.md") in the AWS Command Line Interface documentation.
- To install the AWS CLI on your Ubuntu-based Lightsail instance, connect to your
  instance, and type `sudo apt-get -y install awscli`.

###### Note

The AWS CLI should already be installed on the Amazon Linux Lightsail instance. If you
need to reinstall it, connect to your instance, and type `sudo yum install
 aws-cli`.

After you install the AWS CLI, you need to generate access keys and then configure the AWS CLI
to use them.

## Step 2: Create a new access

key

To use the Lightsail API or the AWS Command Line Interface (AWS CLI), you need to create a new access key. The access key consists of an **Access Key ID** and a **Secret Access
Key**. Use the following procedure to create the key.

1. Sign in to the [the IAM
   console](https://console.aws.amazon.com/iam/home#/users "https://console.aws.amazon.com/iam/home#/users").
2. Choose the name of the user for which you want to create an access key. The user you
   choose should have full access or specific access to Lightsail actions.
3. Choose the **Security credentials** tabs.
4. Choose **Create access key** under the **Access
   keys** section of the page.

###### Note

You can have a maximum of two access keys (active or inactive) at a time per user.
If you already have two access keys, then you must delete one of them before creating a
new one. Make sure that an access key is not actively in use before deleting it. 5. Make note of the **Access key ID** and **Secret access
key** listed. Choose **Show** under the **Secret
access key** column to see your **Secret access key**.

You can copy them from this screen or choose **Download Key File** to
download a `.csv` file containing the access key ID and secret access key.

###### Important

Keep your access keys in a safe place. You should name the file something like
`MyLightsailKeys.csv` so that you don't struggle to find them later. If
you've downloaded the CSV file from the IAM console, you should delete it after you've
completed the next step. You can create a new access keys later if you need to.

## Step 3: Configure the AWS CLI

You need to configure the AWS CLI to use your access keys so that you can use it.

1. Open a terminal window or command prompt.
2. Type `aws configure`.
3. Paste your **AWS Access Key ID** from the
   `.csv` file you created in the previous step.
4. Paste your **AWS Secret Access Key** when prompted.
5. Enter the AWS Region where your resources are located. For example, if your
   resources are primarily in Ohio, choose `us-east-2` when prompted for the
   **Default region name**.

For more information about using the AWS CLI `--region` option, see [General Options](../../../cli/latest/topic/config-vars.md#general-options "../../../cli/latest/topic/config-vars.md#general-options") in the _AWS CLI Reference_. 6. Choose a **Default output format**, such as `json`.

You can now interact with Lightsail programmatically using the AWS CLI. You can find the
Amazon Lightsail commands in the [AWS CLI Command
Reference](../../../cli/latest/reference/lightsail/index.md "../../../cli/latest/reference/lightsail/index.md").

## Next steps

The following resources can help you get started with installing language-specific AWS
SDKs and becoming familiar with the Lightsail API.

- [Install language-specific AWS SDKs](https://aws.amazon.com/tools/#sdk "https://aws.amazon.com/tools/#sdk")
- [Review the Lightsail API Reference](../../2016-11-28/api-reference/Welcome.md "../../2016-11-28/api-reference/Welcome.md")
