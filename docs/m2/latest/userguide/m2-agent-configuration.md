

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# Configure a File Transfer agent
<a name="m2-agent-configuration"></a>

Once you have installed a file transfer agent, follow these steps to configure the agent. If you need to install a new agent, follow instructions on the [Install a File Transfer agent](m2-agent-installation.md) page.

**Topics**
+ [Step 1: Configure permissions and Started Task Control (STC)](#configure-permissions)
+ [Step 2: Create Amazon S3 buckets](#filetransfer-s3-buckets)
+ [Step 3: Create an AWS KMS customer managed key for encryption](#filetransfer-kms-encryption)
+ [Step 4: Create an AWS Secrets Manager secret for the mainframe credentials](#filetransfer-secret-manager)
+ [Step 5: Create an IAM policy](#filetransfer-IAM-policy)
+ [Step 6: Create an IAM user with long-term access credentials](#filetransfer-create-IAM-user)
+ [Step 7: Create an IAM role for the agent to assume](#filetransfer-create-IAM-role)
+ [Step 8: Agent configuration](#agent-configuration)

## Step 1: Configure permissions and Started Task Control (STC)
<a name="configure-permissions"></a>

1. Update and submit one of `SYS2.AWS.M2.SAMPLIB(SEC#RACF)` (for setting up RACF permissions) or `SYS2.AWS.M2.SAMPLIB(SEC#TSS)` (for setting up TSS permissions) in accordance with their instructions. These members were created by the previous `CPY#PDS` step.
**Note**  
`SYS2.AWS.M2` should be replaced with the high-level qualifier (HLQ) chosen during installation.

1. Update the PWD export in the `SYS2.AWS.M2.SAMPLIB(M2AGENT)` STC JCL, if the default File Transfer agent directory path(`/usr/lpp/aws/m2-agent`) was changed.

1. Update the PROC according to your site standards: 

   1. Update the PROC card per your installation requirements.

   1. Update the STEPLIB with the `M2 LOADLIB PDSE ALIAS`. 

   1. Edit PWD to point the agent installation path (only this is included).

   1. Update `JAVA_HOME` if required.

1. Update and copy the `SYS2.AWS.M2.SAMPLIB(M2AGENT)` JCL to `SYS1.PROCLIB` or a one of the PROCLIBs in your `PROCLIB` concatenation.

1. Add `SYS2.AWS.M2.LOADLIB` to the APF list using the following command:

   ```
   SETPROG APF ADD DSNAME(SYS2.AWS.M2.LOADLIB) SMS
   ```

1. Set the agent’s group and owner to the agent user/group (M2USER/M2GROUP). Use the following command in the OMVS:

   ```
   chown -R {{M2USER:M2GROUP}} $AGENT_DIR/current-version
   ```
**Note**  
Edit the M2USER and M2GROUP with the names you used in the security definitions job.

## Step 2: Create Amazon S3 buckets
<a name="filetransfer-s3-buckets"></a>

AWS Mainframe Modernization File Transfer requires an intermediate Amazon S3 bucket as a work area. We recommend creating a bucket specifically for this. 

Optionally, create a new target Amazon S3 bucket for the transferred data sets. Otherwise you can also use your existing Amazon S3 bucket. For more information on creating Amazon S3 buckets, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html).

## Step 3: Create an AWS KMS customer managed key for encryption
<a name="filetransfer-kms-encryption"></a>

**To create a customer managed key in AWS KMS**

1. Open the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms).

1. Choose **Customer managed keys** in left navigation pane.

1. Choose **Create key**.

1. Under **Configure key**, choose **Key type** as **Symmetric**, and **Key usage** as **Encrypt and decrypt**. Use other default configurations.

1. Choose **Next**.

1. In **Add labels**, add Alias and description for your key.

1. Choose **Next**.

1. Under **Define key administrative permissions**, choose at least one IAM user and role who administers this key.

1. Choose **Next**.

1. Optionally, under **Define key administrative permissions**, choose at least one IAM user and role who can use this key.

1. Choose **Next**.

1. In **Edit key policy** section, choose **Edit**, and add the following syntax to the **Key policy**. This allows the AWS Mainframe Modernization service to read and use these keys for encryption/decryption.
**Important**  
Add the statement to the existing statements. Don't replace what's already in the policy.

   ```
   {
       "Sid" : "Enable AWS M2 File Transfer Permissions",
       "Effect" : "Allow",
       "Principal" : {
           "Service" : "m2.amazonaws.com"
       },
       "Action" : [
           "kms:Encrypt",
           "kms:Decrypt"
       ],
      "Resource" : "*"
   },
   ```

1. Choose **Next**.

1. On the **Review** page, check all the details, and choose **Finish**.

Copy and save the ARN for the customer managed key by opening the newly created KMS key. It will be used in the policy later.

## Step 4: Create an AWS Secrets Manager secret for the mainframe credentials
<a name="filetransfer-secret-manager"></a>

Mainframe credentials are required to access the data sets to be transferred and these must be stored as an AWS Secrets Manager secret.

**To create an AWS Secrets Manager secret**

1. Open Secrets manager console at [https://console.aws.amazon.com/secretsmanager](https://console.aws.amazon.com/secretsmanager).

1. Choose **Store a new secret**.

1. In **Choose Secret type**, choose **Other type of secret**.

1. Use the key value `userId` for the mainframe userId that has access to the data sets.. Use the key value `password` for the password field.

1. For **Encryption Key**, choose the AWS customer managed key created earlier.

1. Choose **Next**.

1. On the **Configure secret** page, provide a name and description.

1. On the same page, edit the **Resource permissions**, and use the following resource policy so the AWS Mainframe Modernization service can access it.

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement" : [ {
       "Effect" : "Allow",
       "Principal" : {
           "Service" : "m2.amazonaws.com"
       },
       "Action" : [ "secretsmanager:GetSecretValue", 
                    "secretsmanager:DescribeSecret" ],
       "Resource" : "*"
     } ]
   }
   ```

------

1. Choose **Save** to save the updated permissions.

1. Choose **Next**.

1. Skip through **Configure rotations** page, and choose **Next**. 

1. On the **Review** page, check all configurations and choose **Store** to save the secret.

**Important**  
The `userId` and `password` secret keys are case-sensitive and must be entered as shown.

## Step 5: Create an IAM policy
<a name="filetransfer-IAM-policy"></a>

**To create a new policy with the permissions required for the agent**

1. Open the IAM console at [https://console.aws.amazon.com/iam](https://console.aws.amazon.com/iam).

1. Choose **Policies** under **Access management**. 

1. Choose **Create policy**.

1. On **Specify permissions** page, under **Policy editor**, switch from the Visual editor to the JSON editor and replace the contents with the following template:

1. Replace the `111122223333` in the request-queue and response-queue ARN’s with your account. 
**Note**  
These are wildcard ARN’s that match the two Amazon SQS queues created during the data transfer endpoint initialization. After creating a File Transfer endpoint, optionally replace these ARN’s with the actual values from Amazon SQS.

1. Replace `file-transfer-endpoint-intermediate-bucket-arn` with the ARN of the transfer bucket created earlier. Leave the “/\*” wildcard at the end.

1. Replace `kms-key-arn` with the ARN of the AWS KMS key created earlier.

1. Choose **Next**.

1. On the **Review and create** page, add the Policy name and description.

1. Choose **Create policy**.

## Step 6: Create an IAM user with long-term access credentials
<a name="filetransfer-create-IAM-user"></a>

Create an IAM user that allows the mainframe agent to connect to your AWS account. The agent will connect with this user and then assume a role you define with permissions to use Amazon SQS response and request queues and to save datasets to Amazon S3 buckets. 

**To create this IAM user**

1. Navigate to the IAM console at [https://console.aws.amazon.com/iam](https://console.aws.amazon.com/iam).

1. Choose **Users** under **Access management**.

1. Choose **Create user**. 

1. Add a meaningful **User name** under **User details**. For example, `Configure-ft-agent`.

1. Choose **Next**.

1. In the **Permissions options**, choose the **Attach policies directly** option but do not attach any permissions policies. These permissions will be managed by a role that will be attached.

1. Choose **Next**.

1. Review the details, and choose **Create user**. 

1. Once the user is created, choose the user and open **Security credentials** tab.

1. Under **Access keys**, choose **Create access key**. 

1. Then, choose **Other** when prompted for Use case. 

1. Choose **Next**.

1. Optionally, you can set description tag such as, `Access key for configuring file transfer agent`.

1. Choose **Create access key**.

1. Copy, and securely save the generated **Access key**, and **Secret access key**. These will be used later.

For more information on creating IAM access key, see [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html).

**Important**  
Save the **Access key** and **Secret access key** displayed on the last page of the access key creation wizard, before choosing **Done**. These keys are used to configure the mainframe agent, and cannot be retrieved later.

**Note**  
Save the IAM user ARN used to set up a trust relationship with an IAM role.

## Step 7: Create an IAM role for the agent to assume
<a name="filetransfer-create-IAM-role"></a>

**To create a new IAM role for the agent**

1. Choose **Roles** in the IAM console at [https://console.aws.amazon.com/iam](https://console.aws.amazon.com/iam).

1. Choose **Create role**.

1. On the **Select trusted entity** page, choose **Custom trust policy** for the **Trusted entity type**. 

1. Replace the Custom trust policy with the following and replace `<iam-user-arn>` with the ARN of the user created earlier.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [ {
            "Sid": "FileTransferAgent",
            "Effect": "Allow",
            "Principal": {
               "AWS": "<IAM-User-arn>"
            },
            "Action": "sts:AssumeRole"
       } ]
   }
   ```

------

1. Choose **Next**.

1. In **Add Permissions**, filter for the **Policy name** you created earlier and choose it.

1. Choose **Next**.

1. Name the role, and choose **Create Role**.

**Note**  
Save the *role name*, which you will use later to configure the mainframe agent.

## Step 8: Agent configuration
<a name="agent-configuration"></a>

**To configure the File Transfer agent**

1. Navigate to `$AGENT_DIR/current-version/config`.

1. Edit the agent’s configuration file `appication.properties` to add an environments configuration using the following command:

   ```
   oedit $AGENT_DIR/current-version/config/application.properties
   ```

   For example:

   ```
   agent.environments[0].account-id=<AWS_ACCOUNT_ID>
   agent.environments[0].agent-role-name=<AWS_IAM_ROLE_NAME>
   agent.environments[0].access-key-id=<AWS_IAM_ROLE_ACCESS_KEY>
   agent.environments[0].secret-access-id=<AWS_IAM_ROLE_SECRET_KEY>
   agent.environments[0].bucket-name=<AWS_S3_BUCKET_NAME>
   agent.environments[0].environment-name=<AWS_REGION>
   agent.environments[0].region=<AWS_REGION>
   zos.complex-name=<File_Transfer_Endpoint_Name>
   ```

   Where:
   + `AWS_ACCOUNT_ID` is the ID of the AWS account.
   + `AWS_IAM_ROLE_NAME` is the name of the IAM role created in the [Step 7: Create an IAM role for the agent to assume](#filetransfer-create-IAM-role).
   + `AWS_IAM_ROLE_ACCESS_KEY` is the access key of the IAM user created in [Step 6: Create an IAM user with long-term access credentials](#filetransfer-create-IAM-user).
   + `AWS_IAM_ROLE_SECRET_KEY` is the access secret key for the IAM user created in [Step 6: Create an IAM user with long-term access credentials](#filetransfer-create-IAM-user).
   + `AWS_S3_BUCKET_NAME` is the name of the transfer bucket created with the data transfer endpoint.
   + `AWS_REGION` is the region in which you configure the File Transfer agent.
**Note**  
You can have the File Transfer agent transfer to multiple regions and accounts in AWS by defining multiple environments.
   + (Optional). `zos.complex-name` is the complex name you created when creating a File Transfer endpoint.
**Note**  
This field is necessary only if you want to customize the complex name (which defaults to your sysplex name) that is the same as you defined when creating your File Transfer endpoint. For more information, see [Create data transfer endpoints for File Transfer](filetransfer-data-transfer-endpoints.md).
**Important**  
There can be several such sections, as long as the index in brackets — `[0]`— is incremented for each.

You must restart the agent for changes to take effect.

**Requirements**

1. When a parameter is added or removed, the agent has to be stopped and started. Start the File transfer agent using the following command in the CLI:

   ```
   /S M2AGENT
   ```

   To stop the M2 agent, use the following command in CLI:

   ```
   /P M2AGENT
   ```

1. You can have the File Transfer agent configured to transfer data to multiple regions and accounts in AWS by defining environment entries.
**Note**  
Replace the values with the parameter values you created and configured previously.

   ```
   #Region 1
   agent.environments[0].account-id=AWS_ACCOUNT_ID
   agent.environments[0].agent-role-name=AWS_IAM_ROLE_NAME
   agent.environments[0].access-key-id=AWS_IAM_ROLE_ACCESS_KEY
   agent.environments[0].secret-access-id=AWS_IAM_ROLE_SECRET_KEY
   agent.environments[0].bucket-name=AWS_S3_BUCKET_NAME
   agent.environments[0].environment-name=AWS_REGION
   agent.environments[0].region=AWS_REGION
   
   #Region 2
   agent.environments[1].account-id=AWS_ACCOUNT_ID
   agent.environments[1].agent-role-name=AWS_IAM_ROLE_NAME
   agent.environments[1].access-key-id=AWS_IAM_ROLE_ACCESS_KEY
   agent.environments[1].secret-access-id=AWS_IAM_ROLE_SECRET_KEY
   agent.environments[1].bucket-name=AWS_S3_BUCKET_NAME
   agent.environments[1].environment-name=AWS_REGION
   agent.environments[1].region=AWS_REGION
   ```