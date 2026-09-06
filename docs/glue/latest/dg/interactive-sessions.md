

# Getting started with AWS Glue interactive sessions using Livy
<a name="interactive-sessions"></a>

These sections describe how to run AWS Glue interactive sessions locally.

## Prerequisites for setting up interactive sessions locally
<a name="glue-is-prereqs"></a>

The following are prerequisites for installing interactive sessions:
+ Supported Python versions are 3.6 - 3.10\+. 
+  See sections below for MacOS/Linux and Windows instructions. 
+  Review the [interactive sessions pricing](https://docs.aws.amazon.com/glue/latest/dg/interactive-sessions-session-pricing.html) documentation to understand the cost structure. 

## Installing Jupyter and AWS Glue interactive sessions Jupyter kernels
<a name="interactive-sessions-install"></a>

 Use the following to install the kernel locally. 

 The command, `install-glue-kernels`, installs the jupyter kernelspec for both pyspark and spark kernels and also installs logos in the right directory. 

```
pip3 install --upgrade jupyter boto3 aws-glue-sessions
```

```
install-glue-kernels
```

## Running Jupyter
<a name="w2aac29c15c13"></a>

 To run Jupyter Notebook, complete the following steps. 

1.  Run the following command to launch Jupyter Notebook. 

   ```
   jupyter notebook
   ```

1.  Choose **New**, and then choose one of the AWS Glue kernels to begin coding against AWS Glue. 

## Configuring session credentials and region
<a name="interactive-sessions-credentials"></a>

### MacOS/Linux instructions
<a name="interactive-sessions-macos-linux-instructions"></a>

 AWS Glue interactive sessions requires the same IAM permissions as AWS Glue Jobs and Dev Endpoints. Specify the role used with interactive sessions in one of two ways: 

1.  With the `%iam_role` and `%region` magics 

1.  With an additional line in `~/.aws/config` 

 **Configuring a session role with magic** 

 In the first cell, type `%iam_role <YourGlueServiceRole>` in the first cell executed. 

 **Configuring a session role with `~/.aws/config`** 

 AWS Glue Service Role for interactive sessions can either be specified in the notebook itself or stored alongside the AWS CLI config. If you have a role you typically use with AWS Glue Jobs this will be that role. If you do not have a role you use for AWS Glue jobs, please follow this guide, [ Configuring IAM permissions for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/configure-iam-for-glue.html) , to set one up. 

 To set this role as the default role for interactive sessions: 

1.  With a text editor, open `~/.aws/config`. 

1.  Look for the profile you use for AWS Glue. If you don't use a profile, use the `[Default]` profile. 

1.  Add a line in the profile for the role you intend to use like `glue_role_arn=<AWSGlueServiceRole>`. 

1.  [Optional]: If your profile does not have a default region set, I recommend adding one with `region=us-east-1`, replacing `us-east-1` with your desired region. 

1.  Save the config. 

 For more information, see [Interactive sessions with IAM](glue-is-security.md). 

### Windows instructions
<a name="interactive-sessions-windows-instructions"></a>

 AWS Glue interactive sessions requires the same IAM permissions as AWS Glue Jobs and Dev Endpoints. Specify the role used with interactive sessions in one of two ways: 

1.  With the `%iam_role` and `%region` magics 

1.  With an additional line in `~/.aws/config` 

 **Configuring a session role with magic** 

 In the first cell, type `%iam_role <YourGlueServiceRole>` in the first cell executed. 

 ** Configuring a session role with `~/.aws/config` ** 

 AWS Glue Service Role for interactive sessions can either be specified in the notebook itself or stored alongside the AWS CLI config. If you have a role you typically use with AWS Glue Jobs this will be that role. If you do not have a role you use for AWS Glue jobs, please follow this guide, [ Setting up IAM permissions for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/configure-iam-for-glue.html) , to set one up. 

 To set this role as the default role for interactive sessions: 

1.  With a text editor, open `~/.aws/config`. 

1.  Look for the profile you use for AWS Glue. If you don't use a profile, use the `[Default]` profile. 

1.  Add a line in the profile for the role you intend to use like `glue_role_arn=<AWSGlueServiceRole>`. 

1.  [Optional]: If your profile does not have a default region set, I recommend adding one with `region=us-east-1`, replacing `us-east-1` with your desired region. 

1.  Save the config. 

 For more information, see [Interactive sessions with IAM](glue-is-security.md). 

## Upgrading from the interactive sessions preview
<a name="interactive-sessions-upgrading-from-preview"></a>

 The kernel was upgraded with new names when it was released with version 0.27. To clean up preview versions of the kernels run the following from a terminal or PowerShell. 

**Note**  
If you are a part of any other AWS Glue preview that requires a custom service model, removing the kernel will remove the custom service model.

```
# Remove Old Glue Kernels
jupyter kernelspec remove glue_python_kernel
jupyter kernelspec remove glue_scala_kernel

# Remove Custom Model
cd ~/.aws/models
rm -rf glue/
```