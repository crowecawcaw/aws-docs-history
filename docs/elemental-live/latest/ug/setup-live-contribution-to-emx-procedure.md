# Setup

procedure

## Step A: Create a role in IAM and attach policies

You must use AWS Identity and Access Management (IAM) to set up AWS Elemental Live as an AWS user (the "Elemental Live user") and give it permissions so that it can communicate with AWS Secrets Manager and AWS Elemental MediaConnect. You must:

- Create policies that contain specific permissions.
- Create the "Elemental Live user" in your AWS account. The user must be in the same AWS account as the user who is operating MediaConnect.
- Associate the Elemental Live user with those policies, which gives the user the permissions of those policies.

### Create a policy for Elemental Live to make requests to

MediaConnect

Elemental Live must have permissions on MediaConnect. Follow this procedure to set up these permissions:

###### To create a policy for Elemental Live to make requests to MediaConnect

1. Log into the AWS console and go to the IAM console.
2. On the left menu, choose Policies. Use the filters to determine if there is already a policy with a name similar to "ElementalAccessToMediaConnect".
3. If the policy does not exist, choose Create policy. Click the Visual editor tab and create the policy using the IAM policy generator. This generator lets you choose the service from a list and then choose operations from a list:
   - Service: MediaConnect.
   - Actions: Under List, click DescribeFlow and ListFlows.
   - Resources: If your organization does not have strict rules about accessing containers on MediaConnect, you can ignore this section; you will have access to all flows. Otherwise, follow your internal policies to identify specific flows.
   - Give the policy a name such as "ElementalAccessToMediaConnect"

For more information about how to create and manage IAM policies, see the [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").

### Create a policy for Elemental Live to make requests to

Secrets Manager

If you plan to encrypt the output from Elemental Live when you send it to MediaConnect, then Elemental Live must have permissions on AWS Secrets Manager. Follow this procedure to set up these permissions:

###### To create a policy for Elemental Live to make requests to Secrets Manager

1. Log into the AWS console and go to the IAM console. Choose Policies and look for a policy that gives MediaConnect the permissions for Secrets Manager. If you or someone else previously followed the procedure in [Step 2: Create an IAM Policy to Allow AWS Elemental MediaConnect to Access Your Secret](../../../mediaconnect/latest/ug/encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-policy "../../../mediaconnect/latest/ug/encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-policy"), then this policy will be called `SecretsManagerForMediaConnect`.
2. If this policy exists, make sure it contains the following actions:
   - DescribeSecret
   - GetResourcePolicy
   - GetSecretValue
   - ListSecretVersionIds

3. Also make sure that the resources section gives access to the ARN of the secret that you will use. Read the information in [IAM Policy Examples for Secrets in AWS Secrets Manager](../../../mediaconnect/latest/ug/iam-policy-examples-asm-secrets.md "../../../mediaconnect/latest/ug/iam-policy-examples-asm-secrets.md"). You may need to edit the policy to include the ARN for this secret in the resources section.
4. If the policy does not exist, follow the procedure in [Step 2: Create an IAM Policy to Allow AWS Elemental MediaConnect to Access Your Secret](../../../mediaconnect/latest/ug/encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-policy "../../../mediaconnect/latest/ug/encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-policy") to create the policy.

### Create a user

###### To create a user

1. Log into the AWS console and go to the IAM console.
2. If the user does not exist or it does exist but you want to create separate users for each Elemental product, choose Add User. (Note that you may want separate users for separate products, but there is probably no need to create a separate user for each Elemental node.) Follow the prompts to add the user with this information:
   - Give the user a name such as `ElementalUser`.
   - For Access type, choose Programmatic access. Do not choose Console access.
   - In permissions, choose Attach existing policies directly. Attach the policies you created above. For example, `ElementalAccessToMediaConnect` and `SecretsManagerReadSecrets`.
   - Ignore tags.

3. Create the user and choose Close.
4. Choose the user by clicking the name, for example, click ElementalUser.
5. Choose the Security tab.
6. Click **Create Access Key**.
7. On the Create access key dialog, choose to download the .csv file. Save the file in a safe place, so that you have a permanent record of the access key ID
   and the secret access key.

The Access key ID looks like this:AKIAIOSFODNN7EXAMPLE

The Secret access key looks like this: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY 8. Give the Access key ID and the Secret access key to the Elemental Live operator. Do not give the username and password to the operator. 9. How it works: You have created an AWS user with the permissions required to make requests to MediaConnect and optionally to Secrets Manager. When the Elemental Live user sets up the output with MediaConnect as the destination, they will enter the Access key ID and Secret access key. When the Elemental Live event is running, Elemental Live sends these two IDs to the AWS services, instead of sending the user name and password. These IDs provide authorization for the Elemental Live node to make requests to the AWS services.

## Step B: Set up for encryption (optional)

If you are encrypting the Elemental Live output, you must generate an encryption key and set it up in Secrets Manager. In this scenario, Secrets Manager is effectively acting as the key server for the encryption key. Secrets Manager serves the key to Elemental Live so it can encrypt and to MediaConnect to it can decrypt. In this scenario, encryption/decryption is supported with a static SHA-256 encryption key and using the AES-256, AES-192, or AES-128 algorithm.

Perform the following steps according to the security policies and procedures for your organization.

###### To set up for encryption

1. Use a suitable tool for generating a SHA-256 encryption key from a seed that you specify. AWS does not provide a generation tool. Note that you need only one key, even if you are creating two flows.
2. Save the key to the secret, as described in [Setting Up Static Key Encryption Using AWS Elemental MediaConnect](../../../mediaconnect/latest/ug/encryption-static-key-set-up.md "../../../mediaconnect/latest/ug/encryption-static-key-set-up.md"). You must assign a name to the secret, for example, "key_sports". Save the key in the same AWS Region as the flow you plan to create.
3. Make a note of the ARN for this secret. You need this ARN when you create the MediaConnect flow. It looks like the following example, where "key_sports" is the name you assigned to the secret.

`arn:aws:secretsmanager:us-west-2:111122223333:secret:key_sports-7g8H9i`

## Step C: Create the AWS Elemental MediaConnect flows

You must follow this procedure before you create the Elemental Live outputs because Elemental Live needs data that is generated by this procedure.

###### To create the MediaConnect flows

1. Create one or two MediaConnect flows. (Create two flows if your have set up Elemental Live for output redundancy using output locking. If you have not set up redundant outputs, create one flow.)
2. Follow the procedure in [Creating a Flow](../../../mediaconnect/latest/ug/flows-create.md "../../../mediaconnect/latest/ug/flows-create.md") in the
   _AWS Elemental MediaConnect User Guide_.
3. Complete Availability Zone and Name as appropriate. These fields do not relate to using Elemental Live as the source.
4. In the Source section, follow the steps for setting up a standard source. Specifically:
   - Protocol: Zixi push.
   - Whitelist CIDR block: This is the IP address (in CIDR format) of the Elemental node that will be delivering to this flow. It must be a public facing IP address. Speak to your organization's administrator for a value to enter here.
   - Stream ID: You must enter a value when Elemental Live is the source.

5. If you are encrypting the video, check Enable in the Decryption section and complete the fields as described in the MediaConnect documentation. Specifically:
   - Decryption type: Always Static key.
   - Role ARN: The role that has been set up for MediaConnect to be a trusted entity with Secrets Manager. See [Step 3: Create an IAM Role with a Trusted Relationship](../../../mediaconnect/latest/ug/encryption-speke-set-up.md#encryption-speke-set-up-create-iam-role "../../../mediaconnect/latest/ug/encryption-speke-set-up.md#encryption-speke-set-up-create-iam-role") in the
     _AWS Elemental MediaConnect User Guide_. You must specify this role ARN here so that MediaConnect can obtain the encryption key.
   - To find the ARN for the role, go to the IAM console, choose Roles, click the name of the role, and look at the Role ARN field in the Summary.
     The role ARN looks like this:

   `arn:aws:iam::111122223333:role/MediaConnectASM`
   - Secret ARN: The ARN you obtained in step A, for example:
     `arn:aws:secretsmanager:us-west-2:111122223333:secret:key_sports-7g8H9i`
   - Decryption algorithm: Specify the algorithm that you want to use. Elemental Live will be instructed to use this algorithm to encrypt. MediaConnect will read this information and use this algorithm to decrypt.

6. When you create each flow, MediaConnect creates an ARN for that flow. The ARNs look like the following, where "curling_finals_A" and "curling_finals_B" are the flow names you specified in each flow:

`arn:aws:mediaconnect:us-west-1:111122223333:flow:1bgf67:curling_finals_A`

`arn:aws:mediaconnect:us-west-1:111122223333:flow:9pmlk76:curling_finals_B` 7. Make a note of these ARNs. You need them to set up the Elemental Live output(s).

## Step D: Create the Elemental Live output group

You must create one output group of type "Reliable TS". Inside that group, you must create one or two outputs: create two outputs if you created two MediaConnect flows, create one output if you created only one flow.

###### To create the Elemental Live output group

1. In the Elemental Live event, go to Output Groups > Reliable TS.
2. Click Add Output to create an output in this Reliable TS output group.
3. Complete the fields in each output as follows:
   - Delivery Protocol: Choose AWS Elemental MediaConnect.
   - Destination/Amazon Resource Name: Enter the ARN for the flow. Following from the example above, enter the following in the first output:

   `arn:aws:mediaconnect:us-west-1:111122223333:flow:1bgf67:curling_finals_A`
   - Interface: Optional; see the tooltip.
   - Lock icon: Click this icon. Two more fields appear:
     - Username/Access Key ID: The Access key ID for the user you created in AWS IAM. For example, AKIAIOSFODNN7EXAMPLE
     - Password/Secret Access Key: The Secret access key for this user. For example, wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

4. Note that there is no encryption field. See "How It Works at Runtime", below, to understand how encryption is handled.
5. Repeat these steps to create a second output in this output group, if applicable. Use the same Access key ID and Secret access key.
