# Step 2: Set up the AWS CLI and AWS SDKs

###### Topics

- [Grant programmatic access](sdk-programmatic-access.md "sdk-programmatic-access.md")
- [Using Rekognition with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md")
  The following steps show you how to install the AWS Command Line Interface (AWS CLI) and AWS SDKs that
  the examples in this documentation use. There are a number of different ways to
  authenticate AWS SDK calls. The examples in this guide assume that you're using a
  default credentials profile for calling AWS CLI commands and AWS SDK API
  operations.

For a list of available AWS Regions, see [Regions and
Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in the _Amazon Web Services General Reference_.

Follow the steps to download and configure the AWS SDKs.

###### To set up the AWS CLI and the AWS SDKs

1. Download and install the [AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") and
   the AWS SDKs that you want to use. This
   guide provides examples for the AWS CLI, Java, Python, Ruby, Node.js, PHP, .NET, and JavaScript.
   For information about installing AWS SDKs, see
   [Tools for Amazon Web Services](https://aws.amazon.com/tools/ "https://aws.amazon.com/tools/").
2. Create an access key for the user you created in [Create an AWS Account and User](setting-up.md#setting-up-iam "setting-up.md#setting-up-iam").
   1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
   2. In the navigation pane, choose **Users**.
   3. Choose the name of the user you created in [Create an AWS Account and User](setting-up.md#setting-up-iam "setting-up.md#setting-up-iam").
   4. Choose the **Security credentials** tab.
   5. Choose **Create access key**. Then choose **Download .csv file** to save the
      access key ID and secret access key to a CSV file on your computer. Store the file in a secure location. You will not
      have access to the secret access key again after this dialog box closes. After you have downloaded the CSV file, choose
      **Close**.

3. If you have installed the AWS CLI, you
   can [configure the credentials and region for most AWS SDKs by entering
   `aws configure` at the command prompt](../../../cli/latest/userguide/cli-configure-quickstart.md "../../../cli/latest/userguide/cli-configure-quickstart.md"). Otherwise, use
   the following instructions.
4. On your computer, navigate to your home directory, and create an `.aws` directory. On Unix-based systems,
   such as Linux or macOS, this is in the following location:

```
~/.aws
```

On Windows, this is in the following location:

```
%HOMEPATH%\.aws
```

5. In the `.aws` directory, create a new file named `credentials`.
6. Open the credentials CSV file that you created in step 2 and copy its contents into the
   `credentials` file using the following format:

```
[default]
aws_access_key_id = your_access_key_id
aws_secret_access_key = your_secret_access_key
```

Substitute your access key ID and secret access key for _your_access_key_id_
and _your_secret_access_key_. 7. Save the `Credentials` file and delete the CSV file. 8. In the `.aws` directory, create a new file named `config`. 9. Open the `config` file and enter your region in the following format.

```
[default]
region = your_aws_region
```

Substitute your desired AWS Region (for example, `us-west-2`) for _your_aws_region_.

###### Note

If you don't select a region, then us-east-1 will be used by default. 10. Save the `config` file.
