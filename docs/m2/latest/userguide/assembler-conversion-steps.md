

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# Tutorial: Convert code from Assembler to COBOL in AWS Mainframe Modernization
<a name="assembler-conversion-steps"></a>

You can use this document as a step-by-step guide to understand how to convert the mainframe modernization Assembler code to COBOL. In addition to this, you can also refer the [Automated code conversion from Assembler to COBOL workshop](https://catalog.workshops.aws/awsm2ccm-assembler-cobol/en-US) to learn more about the conversion process.

**Contents**
+ [Prerequisites](#tutorial-assembler-conversion-prerequisites)
+ [Step 1: Share the build assets with AWS account](#tutorial-assembler-conversion-share-assets)
+ [Step 2: Create Amazon S3 buckets](#tutorial-assembler-conversion-create-bucket)
+ [Step 3: Create IAM policy](#tutorial-assembler-conversion-IAM-policy)
+ [Step 4: Create an IAM role](#tutorial-assembler-conversion-IAM-role)
+ [Step 5: Attach the IAM policy to the IAM role](#tutorial-assembler-conversion-attach)
+ [Step 6: Create the CodeBuild project](#tutorial-assembler-conversion-create-project)
  + [Step 6.1: Create the Define project](#tutorial-conversion-define-project)
  + [Step 6.2: Create the Code Analysis project](#tutorial-conversion-analysis-project)
  + [Step 6.3: Create the Code Conversion project](#tutorial-conversion-code-project)
+ [Step 7: Define the project and upload the source code](#tutorial-assembler-conversion-define-upload)
+ [Step 8: Run the analysis and understand the reports](#tutorial-assembler-conversion-run-analysis)
+ [Step 9: Run the Code conversion](#tutorial-assembler-conversion-run-code)
+ [Step 10: Verify the Code conversion](#tutorial-assembler-conversion-verify)
+ [Step 11: Download converted code](#tutorial-assembler-conversion-download)
+ [Clean up resources](#tutorial-assembler-conversion-clean-resources)

## Prerequisites
<a name="tutorial-assembler-conversion-prerequisites"></a>

Read the [Understand Code conversion billing for Assembler conversion](assembler-conversion-billing.md) section to understand how Assembler code conversion generates charges (billing reports) on your AWS Account Management, and the way billing works.

## Step 1: Share the build assets with AWS account
<a name="tutorial-assembler-conversion-share-assets"></a>

In this step, ensure that you share the build assets with your AWS account, especially in the Region where assets are being used.

1. Open the AWS Mainframe Modernization console at [https://console.aws.amazon.com/m2/](https://us-west-2.console.aws.amazon.com/m2/home?region=us-west-2#/).

1. In the left navigation, choose **Tools**.

1. In **AWS Mainframe Modernization Code Conversion with mLogica**, choose **Share assets with my AWS account**.

**Important**  
You need to do this step once in every AWS Region where you intend to do builds.

## Step 2: Create Amazon S3 buckets
<a name="tutorial-assembler-conversion-create-bucket"></a>

In this step, you create Amazon S3 buckets. The first bucket is the project bucket for AWS CodeBuild to hold the source code and then push the output bucket to hold the AWS CodeBuild output (converted code). For more information, see [Creating, configuring, and working with Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets-s3.html) in the *Amazon S3 User Guide*.

1. To create the project bucket, log in to the Amazon S3 console, and choose **Create bucket**.

1. In **General configuration**, provide a name for the bucket and specify the AWS Region where you want to create the bucket. An example name is `codebuild-regionId-accountId-bucket`, where: 
   + `regionId` is the AWS Region of the bucket.
   +  `accountId` is your AWS account ID.
**Note**  
If you are creating the bucket in a different AWS Region from US East (N. Virginia), specify the `LocationConstraint` parameter. For more information, see [Create Bucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html) in the *Amazon Simple Storage Service API Reference*.

1. Retain all other settings, and choose **Create bucket**.

Whatever names you choose for these buckets, be sure to use them throughout this tutorial.

## Step 3: Create IAM policy
<a name="tutorial-assembler-conversion-IAM-policy"></a>

In this step, you create an [IAM policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html). The provided IAM policy grants specific permissions AWS CodeBuild for interacting with Amazon S3, Amazon Elastic Container Registry, [Amazon CloudWatch logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) that CodeBuild generates, and Amazon Elastic Compute Cloud resources for Code conversion. This policy is not customized for customers. The policy grants permissions for AWS Mainframe Modernization to interact, and fetch the Code conversion statistics to bill the customer appropriately.

To learn about creating an IAM policy, see [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM user guide*.

**To create a policy**

1. Log in to the IAM console, and choose **Policies** in the left navigation pane.

1. Choose **Create policy**.

1. Copy and paste the following JSON policy into the policy editor.

------
#### [ JSON ]

****  

   ```
   { 
       "Version":"2012-10-17",		 	 	  
       "Statement": [ 
           { 
               "Action": [
                   "s3:PutObject", 
                   "s3:GetObject", 
                   "s3:GetBucketLocation", 
                   "s3:ListBucket", 
                   "s3:PutObjectAcl", 
                   "s3:GetBucketAcl" 
               ], 
               "Resource": [ 
                   "arn:aws:s3:::codebuild-regionId-accountId-bucket", 
                   "arn:aws:s3:::codebuild-regionId-accountId-bucket/*", 
                   "arn:aws:s3:::aws-m2-repo-*" ], 
                       "Effect": "Allow" 
             }, 
             {
                 "Action": [ 
                   "ecr:GetAuthorizationToken", 
                   "ecr:BatchCheckLayerAvailability", 
                   "ecr:BatchGetImage", 
                   "ecr:GetDownloadUrlForLayer", 
                   "logs:*", 
                   "ec2:DescribeSecurityGroups", 
                   "ec2:DescribeSubnets", 
                   "ec2:DescribeNetworkInterfaces", 
                   "ec2:DeleteNetworkInterface", 
                   "ec2:CreateNetworkInterface", 
                   "ec2:DescribeDhcpOptions", 
                   "ec2:DescribeVpcs", 
                   "ec2:CreateNetworkInterfacePermission" 
               ], 
               "Resource": "*", 
               "Effect": "Allow" 
            } 
       ] 
   }
   ```

------

1. You can optionally add tags to the policy. Tags are key-value pairs that can help you organize, track, or control access for the policy.

1. Choose **Next:Review**.

1. Provide a name for the policy, for example, `CodeBuildAWSM2CCMPolicy`.

1. You can optionally enter a description for the policy, and review the policy summary to ensure it's correct.

1. Choose **Create policy**.

## Step 4: Create an IAM role
<a name="tutorial-assembler-conversion-IAM-role"></a>

In this step, you create a new [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that allows CodeBuild to interact with AWS resources for you, after you associate the IAM policies that you previously created with this new IAM role.

For information about creating a service role, see [Creating a Role to Delegate Permissions to an AWS Service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User guide*.

1. Log in to the IAM console, and choose **Roles** in the left navigation pane.

1. Choose **Create role**.

1. Under **Trusted entity type**, choose **AWS service**.

1. Under **Use cases for other AWS services**, choose **CodeBuild**, and then choose **CodeBuild** again.

1. Choose **Next**.

1. On the **Add permissions** page, choose **Next**. You assign a policy to the role later.

1. Under **Role details**, provide a name for the role, for example, `IAMRoleTaskExecutionRoleForCodeBuild`.

1. Under **Select trusted entities**, verify that the policy document looks like the following:

------
#### [ JSON ]

****  

   ```
   {
             "Version":"2012-10-17",		 	 	 
             "Statement": [
               {
                 "Effect": "Allow",
                 "Principal": {
                   "Service": "codebuild.amazonaws.com"
                 },
                 "Action": "sts:AssumeRole"
               }
             ]
   }
   ```

------

1. Choose **Create role**.

## Step 5: Attach the IAM policy to the IAM role
<a name="tutorial-assembler-conversion-attach"></a>

In this step, you attach the IAM policy you previously created to the `IAMRoleTaskExecutionRoleForCodeBuild` IAM role.

1. Log in to the IAM console, and choose **Roles** in the left navigation pane.

1. In **Roles**, choose the role you created previously, for example, `IAMRoleTaskExecutionRoleForCodeBuild`.

1. In **Permissions policies**, choose **Add permissions**, and then **Attach policies**.

1. In **Other permissions policies**, choose the policies that you created previously, for example, `CodeBuildAWSM2CCMPolicy`.

1. Choose **Attach policies.**

## Step 6: Create the CodeBuild project
<a name="tutorial-assembler-conversion-create-project"></a>

In this step, you create three different CodeBuild projects based on the `buildspec.yml` file mentioned above.

### Step 6.1: Create the Define project
<a name="tutorial-conversion-define-project"></a>

**To create the Define project**

1. Log in to the CodeBuild console, and choose **Create build project**.

1. In the **Project configuration** section, provide a name for the project, for example, `1-awsm2ccm-define-project`.

1. In the **Source** section, for **Source provider**, leave the default selection.

1. In the **Environment** section, choose **Custom image**.

1. In the **Environment type** field, choose **Linux**.

1. Under **Image registry**, choose **Other registry**.

1. In the **External registry URL** field, follow the [AWS Mainframe Modernization container](assembler-conversion-components-process.md#assembler-conversion-components-container) section.

1. Under **Service role**, choose **Existing service role**, and in the **Role ARN** field, choose the service role you created previously (e.g., `IAMRoleTaskExecutionRoleForCodeBuild`).

1. Expand the **Additional configuration** section, do the following:

   1. VPC: Configure if needed based on your setup.

   1. Timeout: Set to **60 minutes**.

   1. Queued timeout: Set to **480 minutes**.

   1. Encryption: Choose the appropriate encryption settings (default is fine).

   1. In the **Environment variables** section, add the following one by one:
      + Name : **PROJECT\_BUCKET**. Value : `codebuild-regionId-accountId- bucket`. Type : **Plaintext**
      + Name : **PROJECT\_DIR**. Value : `prj_codebuild_01`. Type : **Plaintext**
      + Name : **AWSM2CCM\_ACTION**. Value : `define_project`. Type : **Plaintext**
      + Name : **AWSM2CCM\_LOGGING\_BUCKET**. Value : `s3:// codebuild-regionId-accountId-bucket`. Type : **Plaintext**

1. In the **Buildspec** section, choose **Insert build commands**, and then **Switch to editor**.

1. Replace the current values with this:

   ```
   version: 0.2 
   phases: 
       build: 
           commands: 
               - . /app/awsm2ccm_prod/bin/setup_env.sh 
               - run_awsm2ccm.sh $PROJECT_DIR 
   artifacts: 
       files: 
           - '**/*' 
       discard-paths: no 
       base-directory: $PROJECT_DIR
   ```

   where, PROJECT\_DIR are environment variables available within CodeBuild. For more information, see [Environment variables in build environments](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-env-vars.html).

1. In the **Artifacts** section, do this:
   + under **Type**, choose **Amazon S3**, and then choose your output bucket, for example, `codebuild-regionId-accountId-bucket`.
   + for **Path**, leave this field empty.
   + for **Name**, enter `prj_codebuild_01`.
   + for **Artifact packaging**, select **None**.
   + for **Override artifact name**, uncheck this option.
   + for **Encryption**, leave it to default settings.

1. For the **Logs** section, do the following:
   + CloudWatch logs: **Disabled**
   + S3 Logs: **Enabled**
   + Bucket: `codebuild-regionId-account-bucket`
   + Log path: `CODEBUILD-LOGS`

1. Choose **Create build project**.

### Step 6.2: Create the Code Analysis project
<a name="tutorial-conversion-analysis-project"></a>

**To create the Code Analysis project**

1. Log in to the CodeBuild console, and choose **Create build project**.

1. In the **Project configuration** section, provide a name for the project, for example, `2-awsm2ccm-analysis`.

1. In the **Source** section, for **Source provider**, choose **Amazon S3**, and then choose the input bucket you created previously (e.g., `codebuild-regionId-accountId-bucket`).

1. In the **S3 object key** or **S3 folder** field, enter `prj_codebuild_01`.

1. In the **Environment** section, choose **Custom image**.

1. In the **Environment type** field, choose **Linux**.

1. Under **Image registry**, choose **Other registry**.

1. In the **External registry URL** field, follow the [AWS Mainframe Modernization container](assembler-conversion-components-process.md#assembler-conversion-components-container) section.

1. Under **Service role**, choose **Existing service role**, and in the **Role ARN** field, choose the service role you created previously (e.g.,`IAMRoleTaskExecutionRoleForCodeBuild`).

1. Expand the **Additional configuration** section, do the following:

   1. VPC: Configure if needed based on your setup.

   1. Timeout: Set to **60 minutes**.

   1. Queued timeout: Set to **480 minutes**.

   1. Encryption: Choose the appropriate encryption settings (default is fine).

   1. In the **Environment variables** section, add the following one by one:
      + Name: **PROJECT\_BUCKET**. Value : `codebuild-regionId-accountId-bucket`. Type : **Plaintext**
      + Name : **PROJECT\_DIR**. Value : `prj_codebuild_01`. Type : **Plaintext**
      + Name : **AWSM2CCM\_ACTION**. Value : `analysis`. Type : **Plaintext**
      + Name : **AWSM2CCM\_LOGGING\_BUCKET**. Value : `s3:// codebuild-regionId-accountId-bucket`. Type : **Plaintext**

1. In the **Buildspec** section, choose **Insert build commands**, and then **Switch to editor**.

1. Replace the current values with this:

   ```
   version: 0.2 
   phases: 
       build: 
           commands: 
               - ln -s $CODEBUILD_SRC_DIR $PROJECT_DIR 
               - . /app/awsm2ccm_prod/bin/setup_env.sh 
               - run_awsm2ccm.sh $PROJECT_DIR
   artifacts: 
       files: 
           - '*.log' 
           - '_Converted/*/*' 
           - '_Reports/*' 
       secondary-artifacts: 
           reports: 
               files: 
                   - '_Reports/AWSM2CCM*' 
       discard-paths: no 
       base-directory: $PROJECT_DIR
   ```

   where, PROJECT\_DIR are environment variables available within CodeBuild. For more information, see [Environment variables in build environments](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-env-vars.html).

1. In the **Artifacts** section, do this:
   + under **Type**, choose **Amazon S3**, and then choose your output bucket (e.g., `codebuild-regionId-accountId-bucket`).
   + for **Path**, enter **ARTIFACTS**.
   + for **Name**, enter `prj_codebuild_01`.
   + for **Artifact packaging**, select **None**.
   + for **Override artifact name**, uncheck this option.
   + for **Encryption**, leave it to default settings.

1. For the **Logs** section, do the following:
   + CloudWatch logs: **Disabled**
   + S3 Logs: **Enabled**
   + Bucket: `codebuild-regionId-account-bucket`
   + Log path: `CODEBUILD-LOGS`

1. Choose **Create build project**.

### Step 6.3: Create the Code Conversion project
<a name="tutorial-conversion-code-project"></a>

**To create the Code Conversion project**

1. Log in to the CodeBuild console, and choose **Create build project**.

1. In the **Project configuration** section, provide a name for the project (e.g.,`3-awsm2ccm-convert`).

1. In the **Source** section, for **Source provider**, choose **Amazon S3**, and then choose the input bucket you created previously (e.g.,`codebuild-regionId-accountId-bucket`).

1. In the **S3 object key** or **S3 folder** field, enter `prj_codebuild_01`.

1. In the **Environment** section, choose **Custom image**.

1. In the **Environment type** field, choose **Linux**.

1. Under **Image registry**, choose **Other registry**.

1. In the **External registry URL** field, follow the [AWS Mainframe Modernization container](assembler-conversion-components-process.md#assembler-conversion-components-container) section.

1. Under **Service role**, choose **Existing service role**, and in the **Role ARN** field, choose the service role you created previously; for example, `IAMRoleTaskExecutionRoleForCodeBuild`.

1. Expand the **Additional configuration** section, do the following:

   1. VPC: Configure if needed based on your setup.

   1. Timeout: Set to **60 minutes**.

   1. Queued timeout: Set to **480 minutes**.

   1. Encryption: Choose the appropriate encryption settings (default is fine).

   1. In the **Environment variables** section, add the following one by one:
      + Name: **PROJECT\_BUCKET**. Value : `codebuild-regionId-accountId-bucket`. Type : **Plaintext**
      + Name : **PROJECT\_DIR**. Value : `prj_codebuild_01`. Type : **Plaintext**
      + Name : **AWSM2CCM\_ACTION**. Value : `conversion`. Type : **Plaintext**
      + Name : **AWSM2CCM\_LOGGING\_BUCKET**. Value : `s3:// codebuild-regionId-accountId-bucket`. Type : **Plaintext**

1. In the **Buildspec** section, choose **Insert build commands**, and then **Switch to editor**.

1. Replace the current values with this:

   ```
   version: 0.2 
   phases: 
       build: 
           commands: 
               - export AWSM2CCM_PUSH_RUNTIME_COPYBOOKS=y 
               - ln -s $CODEBUILD_SRC_DIR $PROJECT_DIR 
               - . /app/awsm2ccm_prod/bin/setup_env.sh
               - run_awsm2ccm.sh $PROJECT_DIR
   artifacts: 
       files: 
           - '*.log' 
           - '_Converted/*/*' 
           - '_Reports/*'  
       discard-paths: no 
       base-directory: $PROJECT_DIR
   ```

   where, PROJECT\_DIR are environment variables available within CodeBuild. For more information, see [Environment variables in build environments](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-env-vars.html).

1. In the **Artifacts** section, do this:
   + under **Type**, choose **Amazon S3**, and then choose your output bucket (e.g., `codebuild-regionId-accountId-bucket`).
   + for **Path**, enter **ARTIFACTS**.
   + for **Name**, enter `prj_codebuild_01`.
   + for **Artifact packaging**, select **None**.
   + for **Override artifact name**, uncheck this option.
   + for **Encryption**, leave it to default settings.

1. For the **Logs** section, do the following:
   + CloudWatch logs: **Disabled**
   + S3 Logs: **Enabled**
   + Bucket: `codebuild-regionId-account-bucket`
   + Log path: `CODEBUILD-LOGS`

1. Choose **Create build project**.

## Step 7: Define the project and upload the source code
<a name="tutorial-assembler-conversion-define-upload"></a>

The Define Project sets up the project folder and configuration files, initialized with default configurations. In this step, you start the build. To do this:

1. Log in to the AWS CodeBuild console.

1. In the left navigation pane choose **Build projects**.

1. Select the previously created project (`1-awsm2ccm-define-project`) to build

1. Choose **Start build**, and then **Start now** to define the project. Once the build starts, the status will change to *in progress*.

1. Choose **Phase details** to see the progress of each step which is orchestrated by the AWS CodeBuild project.

1. Wait until the status has changed to **succeeded** for all the steps.

1. Go to the Amazon S3 console.

1. Locate and click on Amazon S3 bucket named `codebuild-regionId-accountId-bucket`
   + **`CODEBUILD-LOGS/`** folder contains the AWS CodeBuild logs for the running AWS CodeBuild projects.
   + **`prj_codebuild_01/`** folder that contains the project structure. It's used during analysis, expand\_macros, and convert steps. You can select `prj_codebuild_01/` to explore details
   + **`cobol_reserved.rsw`** configuration file (list of COBOL words) reserved for the converter. It's used during the convert step.
   + **`Macro_Expansion/`** folder contains macros to expand into Assembler programs. It's used during the expand\_macros step.
   + **`macro_settings.json`** configuration file contains customized macro replacement. It's used during the expand\_macros step.
   + **`macrolib/`** folder contains the Assembler macros to be converted. It's used during the analysis and convert step.

     1. Select `macrolib/`.

     1. By default one Assembler macro named `MACRO1.mac` is provided as a sample file. Delete this file since it's not needed for the analysis.

     1. Upload your Macros in this directory.
   + **`project_settings_aux.json`** configuration file contains settings related to code page. It's used during the convert step.
   + **`project_settings.json`** configuration file contains settings for the converter. It's used during the convert step.
   + **`srclib/`** folder contains the Assembler programs to be converted. It's used during the analysis and convert step.

     1. Choose `srclib/`.

     1. By default, two Assembler programs named `SQtest01.asm` and `SQtest02.asm` are provided as samples. Delete these files as they aren't needed for your analysis and conversion.

     1. Upload your Assembler programs in this directory.

1. Verify the status for `1-awsm2ccm-define-project` step. It should have succeeded under the **Latest build status** tab.

You are ready for the next step: **Code analysis**.

## Step 8: Run the analysis and understand the reports
<a name="tutorial-assembler-conversion-run-analysis"></a>

**Note**  
AWS Mainframe Modernization Code conversion *analysis * step is free of charge.

In this step, you kickoff another build:

1. In the left navigation pane, choose **Build projects**.

1. Choose the project you created in step 6.2 to build: `2-awsm2ccm-analysis`.

1. Choose **Start build**, and then **Start now** to generate analysis reports. This will start the build and change status to *in progress*.

1. Choose **Phase details** where you will see the progress of each step orchestrated by the AWS CodeBuild project. Wait until the status changes to *succeeded* for all steps.

1. From the AWS Management Console, go to the Amazon S3 service console.

1. Locate and click on the Amazon S3 bucket: `codebuild-regionId-accountId-bucket`

   1. **`ARTIFACTS/`** folder contains the outputs of *analysis* and *convert* steps.

   1. Choose `ARTIFACTS/prj_codebuild_01/_Reports/`.

   1. The following reports will be available:
      + `AWSM2CCM-Analysis-Report-<timestamp>.pdf` is an executive report that provides the AWS Mainframe Modernization Code conversion billing and scope, improving the conversion, conversion summary, and the detailed conversion statistics. It also summarizes the code counts and billable code counts at a project level and provides metrics and lists of referenced members for each component. It's critical to run and examine this report prior to running the actual conversion.
      + `Conversion_Detailed_Statistics.txt` provides the frequency and expected conversion result (shown as “Conversion status”) for each instruction found in each component. This provides a quick way to identify whether instructions are clear that the converter does not support. Possible *Conversion status* results are:
        + **Totally converted**: the instruction will be accurately converted to COBOL.
        + **Partially converted**: the instruction is supported but uses an unsupported parameter or expression. Manual adjustments are likely required after conversion.
        + **Not converted**: the instruction is not supported by the converter.
        + **Pre-compile instructions to verify**: these are normally included inside the Macros, and refer to what is probably known also as *Conditional Assembly Language* (e.g., AIF, AGO) instructions on mainframe. These are handled by the pre-compiler which is driven by such instructions or directives selects and produces *clean/static* ASM code. These instructions depend on the actual values of the Macro parameters which get compiled. So, the same Macro can generate different pieces of ASM code, depending on the values of the passed parameters. This is because of the presence of such *pre-compile instructions*. In that case, consider expanding or re-engineering the Macro.
      + `Conversion_Global_Statistics.txt` provides a summary of the *Conversion status* at a component level.
      + `CrossReference_PgmToCpyMacro.txt` reports on Assembler program dependencies on Macros. It provides a quick way to determine if any Macros are missing from the uploaded code.
      + `CrossReference_PgmToPgm.txt` reports on Assembler program dependencies on other Assembler programs. It provides a quick way to determine if any Assembler programs are missing from the uploaded code.

1. Return to the AWS CodeBuild service console.

1. Verify the status for **2-awsm2ccm-analysis** step. It should have **succeeded** under the **Latest build status** tab.

You are ready for the next step: **Code conversion**.

## Step 9: Run the Code conversion
<a name="tutorial-assembler-conversion-run-code"></a>

**Important**  
AWS Mainframe Modernization Code conversion *conversion* step will be billed per your usage. For more information on billing, see [Understand Code conversion billing for Assembler conversion](assembler-conversion-billing.md).

In this step, you will configure the conversion process, and then start the build.

1. From the AWS Management Console, go to the Amazon S3 service.

1. Locate and click on the Amazon S3 bucket: `codebuild-regionId-accountId-bucket`.

   1. Go to `prj_codebuild_01/`.

   1. Select `project_settings.json`, and choose **Download**.

   1. Open the `project_settings.json` file to see the following JSON structure:

      ```
      { 
      "Source programs directory":"srclib", 
      "Source copybooks/macros directory":"macrolib", 
      "Copybook/Macros Conversion":"Called_only", 
      "Do not regenerate the Copy/Macro if already exists":"false", 
      "Target Compiler":"IBM", 
      "Endianess":"Big", 
      "Converted programs extension":"", 
      "Converted CICS programs extension":"", 
      "Converted copies/macros extension":"", 
      "Trace Level":"STANDARD", 
      "Trace file open mode":"append", 
      "Data definition level":5, 
      "Start picture column":40, 
      "Generate Sync FILLER with name":"FILL-SYNC", 
      "Use SYNC clause":"yes", 
      "Decimal Point Comma":"true", 
      "Original Source Placement":"RIGHT" 
      }
      ```

      where,
      + **Source program directory**: contains the Assembler programs that are needed for the conversion.
      + **Source copybooks/Macros directory**: contains the Assembler Macros and copybooks that are needed for the conversion.
      + **Copybooks/Macros conversion** can be either:
        + **All**: This radio button denotes that the *full conversion* will convert all copybook/Macros available in the directory irrespective of whether that is being used by the programs or not.
        + **Called\_only**: This radio button denotes that the *full conversion* will only convert the copybook/Macros that actually used by the programs.
      + 
**Important**  
You don't need to regenerate the Copy/Macro if it already exists.

        When this is true, the tool won't convert the copybook/Macro again, if it's already converted (exists in the output folder). 
      + **Target**: The conversion of the programs (generated code) depends on the target COBOL compiler. The following options are supported:
        + "IBM" for IBM mainframe
        + "MF" for Micro Focus COBOL 
        + “VERYANT” for Veryant isCOBOL
        + “NTT” for NTT DATA Enterprise COBOL (Unikix)
      + **Endianess and Bitness**: The conversion of the programs (generated code) depends on the target platform (bit/endianess). This combo allows the selection of the following supported options:
        + Endianess: *Big* (for Big-Endian)/ Little (Little-Endian). For example, IBM z/OS mainframe is Big-Endian, Windows is Little-Endian, Linux varies by distribution (e.g. Amazon Linux 2 on EC2 is Little-Endian).
        + Bitness: 32/64 (if not given, default will be 32). The recommended setting is 32 bits.
      + **Converted program extension**: This is to set the file extension for the generated COBOL programs. Empty (“”): no extension. For Rocket Software (formerly Micro Focus) COBOL targets, *CBL* is recommended to enable Rocket Enterprise Developer to correctly recognize the files.
      + **Converted CICS program extension**: This is to set the file extension for the generated CICS COBOL programs. Empty (“”):: no extension. For Rocket Software COBOL targets, *CBL* is recommended to enable Rocket Enterprise Developer to correctly recognize the files.
      + **Converted copybooks/Macros extension**: This is to set the file extension for the generated COBOL copybooks. Empty (“”):: no extension. For Rocket Software COBOL targets, *CPY* is recommended to enable Rocket Enterprise Developer to correctly recognize the files.
      + **Trace level**: Trace is the information that is logged using CodeBuild during the conversion. The user can select the level of detail by selecting any one of the provided options.
        + **ERROR** = TRACE ERROR: only conversion errors are displayed.
        + **STANDARD** = TRACE STANDARD: conversion errors and standard information are displayed. This is the recommended setting.
        + **ALL** = TRACE ALL: maximum level of tracing
      + **Trace file open mode**: Not used. Default setting of*append* is recommended.
      + **Data definition level**: This indicates the initial level of the sub-fields (after level “01”) defined in working-storage and linkage section. Must be a number.
      + **Start picture column**: This is about the format of the generated COBOL code and indicates the column where the * PIC* clause is placed (after the field names). Must be a number.
      + **Original source placement:** This indicates the position where the comments are placed in the program. It has two options:
        + **RIGHT**: This option will place the comment or additional information at the right position after seventy-third (73) column. In COBOL the code is written in the first seventy-two (1-72) columns and anything from the seventy-third (>= 73) column will be treated as a comment.
        + **ABOVE**: This option will place the comment above the translated content.
      + **Generate Sync FILLER with name**: This option is related to the alignment in memory of binary fields (Assembler "H”, “F”, “D” data-types, which are converted to COBOL “COMP” data-type). In order to guarantee the proper *alignment boundary*, explicit *filler* fields will be added during the conversion. This is a text based option, the value must be a string (like FILL-SYNC).
      + **Use SYNC clause**: This option refers to the alignment in memory of binary fields. Yes = all the fields converted to COBOL. “COMP” will be defined with the clause “SYNC” (e.g.,, 05 WRKFLD PIC S9(09) COMP SYNC).
      + **Decimal point comma**: When this is true, the *DECIMAL-POINT IS COMMA* clause will be added to the "SPECIAL-NAMES" COBOL paragraph.

   1. Based on your requirements, change appropriate parameters, and then save the `project_settings.json`.

   1. Remove the existing `project_settings.json` file from `prj_codebuild_01/` in Amazon S3 bucket, and then upload the new version.

1. Go back to the AWS CodeBuild service.

1. Select the project to build you created previously : `3-awsm2ccm-convert`

   1. Choose **Start build**, and then **Start now** to convert Assembler programs and Macros to COBOL programs and copybooks.

   1. Wait for the build status to change to **Succeeded** for this project. It will be under the **Latest build status** tab.

## Step 10: Verify the Code conversion
<a name="tutorial-assembler-conversion-verify"></a>

1. From the AWS Management Console, go to Amazon S3 service.

1. Locate and click on the Amazon S3 bucket: `codebuild-regionId-accountId-bucket`.

1. Navigate to **`awsm2ccm-do-not-delete `**. AWS Mainframe Modernization Code conversion creates encoded binary files for each Assembler or Macro module during the conversion process. These files are essential for preventing duplicate billing to the customers and also to track how much of the provided Assembler code was analyzed and converted. Files are stored in the following location: `codebuild-regionId-accountId- bucket/awsm2ccm-do-not-delete/<your_AWS_account_id>/Hash`. The encoded files do not contain any Assembler code and It is also not possible to extract customer code from these files.
**Important**  
Neither manually edit these files or delete these files. Editing or deleting these files may result in multiple billings for the same components.

   Treat the **`awsm2ccm-do-not-delete/`** folder as a system-managed directory. Consult Support before making any changes to this directory or its contents.

1. Click `codebuild-regionId-accountId-bucket` to go back to the bucket.

1. Choose **`ARTIFACTS/prj_codebuild_01/`**.**\_Converted/** folder contains the generated COBOL outputs as a result of Code conversion step. It will have the following subdirectories:
   + **copybooks/** folder contains the generated COBOL copybooks.
   + **programs/ ** folder contains the generated COBOL programs.
   + **runtime\_lib/** folder contains additional COBOL programs and copybooks provided by the solution.

1. If the *Analysis Reports* and other reports indicate that the conversion was successful, and the AWS CodeBuild project `3-awsm2ccm-convert` is marked **Succeeded**, download the COBOL code and copybooks from the **\_Converted/** directory.

## Step 11: Download converted code
<a name="tutorial-assembler-conversion-download"></a>

In this step, download the COBOL code and copybooks from the **\_Converted/** directory, and compile them in the target COBOL environment.

1. From the AWS Management Console, go to Amazon S3 service.

1. Locate and click on the Amazon S3 bucket: `codebuild-regionId-accountId-bucket`.

1. Navigate to the location: ` ARTIFACTS/prj_codebuild_01/_Converted/`.

1. Download the converted COBOL code from all the subdirectories under **\_Converted/**. You can also use the following CLI command to download them at once:

   ```
   aws s3 cp s3://codebuild-regionId-accountId- 
   bucket/ARTIFACTS/prj_codebuild_01/_Converted/ . --recursive
   ```

1. Analyze and compile the converted COBOL in the target COBOL environment.

## Clean up resources
<a name="tutorial-assembler-conversion-clean-resources"></a>

If you no longer need the resources that you created for this tutorial, delete them to avoid additional charges. To do so, complete the following steps:
+ Delete the S3 buckets that you created for this tutorial. For more information, see [Deleting a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-bucket.html) in the *Amazon Simple Storage Service User guide*.
+ Delete the IAM policies that you created for this tutorial. For more information, see [Deleting IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-delete.html) in the *IAM User guide*.
+ Delete the IAM role that you created for this tutorial. For more information, see [Deleting roles or instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html) in the *IAM User guide*.
+ Delete the CodeBuild project that you created for this tutorial. For more information, see [Delete a build project in CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/delete-project.html) in the *AWS CodeBuild User guide*.