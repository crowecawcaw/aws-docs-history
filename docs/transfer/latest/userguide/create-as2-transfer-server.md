# Create an AS2 server

This topic provides instructions for creating an AS2-enabled Transfer Family server, using either the
console or a CloudFormation template. For an end-to-end example AS2 configuration, see [Setting up an AS2 configuration](as2-example-tutorial.md "as2-example-tutorial.md"). After you create
an AS2 server, you can add an agreement to the server.

1. [Import AS2 certificates](managing-as2-partners.md#configure-as2-certificate "managing-as2-partners.md#configure-as2-certificate")
2. [Create AS2 profiles](configure-as2-profile.md "configure-as2-profile.md")
3. Create an AS2 server
4. [Create an AS2 agreement](#as2-agreements "#as2-agreements")
5. [Configure AS2 connectors](configure-as2-connector.md "configure-as2-connector.md")

###### Topics

- [Create an AS2 server using the Transfer Family
  console](#create-server-as2-console "#create-server-as2-console")
- [Use a template to create a demo Transfer Family AS2
  stack](#as2-cfn-demo-template "#as2-cfn-demo-template")
- [Create an AS2 agreement](#as2-agreements "#as2-agreements")

## Create an AS2 server using the Transfer Family

console

This procedure explains how to create an AS2-enabled server by using the Transfer Family console.
If you want to use the AWS CLI instead, see [Step 4: Create a Transfer Family server that uses the AS2
protocol](as2-example-tutorial.md#as2-example-server "as2-example-tutorial.md#as2-example-server").

###### Note

You can attach a file-processing workflow to a Transfer Family server that uses
the AS2 protocol: however, AS2 messages don't execute workflows attached to the server.

###### To create an AS2-enabled server

1. Open the AWS Transfer Family console at [https://console.aws.amazon.com/transfer/](https://console.aws.amazon.com/transfer/ "https://console.aws.amazon.com/transfer/").
2. In the left navigation pane, choose **Servers**, and then
   choose **Create server**.
3. On the **Choose protocols** page, select **AS2
   (Applicability Statement 2)**, and then choose
   **Next**.
4. On the **Choose an identity provider** page, choose
   **Next**.

###### Note

For AS2, you cannot choose an identity provider because basic
authentication is not supported for the AS2 protocol. Instead, you control
access through virtual private cloud (VPC) security groups. 5. On the **Choose an endpoint** page, do the following:

![Console screenshot showing the Choose an endpoint page with VPC hosted selected.](/images/transfer/latest/userguide/images/create-server-choose-endpoint-vpc-internal.png)

    1. For **Endpoint type**, choose **VPC
     hosted** to host your server's endpoint. For
     information about setting up your VPC-hosted endpoint, see [Create a server in a virtual private cloud](create-server-in-vpc.md "create-server-in-vpc.md").


    ###### Note

    Publicly accessible endpoints are not supported for the AS2
     protocol. To make your VPC endpoint accessible over the internet,
     choose **Internet Facing** under
     **Access**, and then supply your Elastic IP
     addresses.
    2. For **Access**, choose one of the following
     options:




    	* **Internal** – Choose this option to
    	 provide access from within your VPC and VPC-connected
    	 environments, such as an on-premises data center over Direct Connect
    	 or VPN.
    	* **Internet Facing** – Choose this
    	 option to provide access over the internet and from within your
    	 VPC and VPC-connected environments, such as an on-premises data
    	 center over Direct Connect or VPN.


    	If you choose **Internet Facing**, supply
    	 your Elastic IP addresses when prompted.
    3. For **VPC**, either choose an existing VPC or choose
     **Create VPC** to create a new VPC.
    4. For **FIPS Enabled**, keep the **FIPS Enabled
     endpoint** check box cleared.


    ###### Note

    FIPS-enabled endpoints are not supported for the AS2
     protocol.
    5. Choose **Next**.

6. On the **Choose a domain** page, choose
   **Amazon S3** to store and access your files as objects by using
   the selected protocol.

Choose **Next**. 7. On the **Configure additional details** page, choose the
settings that you need.

###### Note

If you are configuring any other protocols along with AS2, all of the
additional detail settings apply. However, for the AS2 protocol, the only
settings that apply are those in the **CloudWatch logging** and
**Tags** sections.

Even though setting up a CloudWatch logging role is optional, we highly
recommend setting it up so that you can see the status of your messages and
troubleshoot configuration issues. 8. On the **Review and create** page, review your choices to
make sure they are correct.

    * If you want to edit any of your settings, choose
     **Edit** next to the step that you want to
     change.


    ###### Note

    If you edit a step, we recommend that you review each step after
     the step that you chose to edit.
    * If you have no changes, choose **Create server** to
     create your server. You are taken to the **Servers**
     page, shown following, where your new server is listed.


    It can take several minutes before the status for your new server
     changes to **Online**. At that point, your server can
     perform file operations for your users.

## Use a template to create a demo Transfer Family AS2

stack

We supply a self-contained, CloudFormation template to quickly create an AS2-enabled Transfer Family
server. The template configures the server with a public Amazon VPC endpoint, certificates,
local and partner profiles, an agreement, and a connector.

The basic AS2 server template creates the following resources:

- An AS2-enabled Transfer Family server with a VPC endpoint
- Local and partner AS2 profiles with certificates
- An agreement between the profiles
- An Amazon S3 bucket for file storage
- Required IAM roles and policies
- CloudWatch logging configuration

Before using this template, note the following:

- If you create a stack from this template, you will be billed for the AWS
  resources that are used.
- The template creates multiple certificates and places them in AWS Secrets Manager to
  store them securely. You can delete these certificates from Secrets Manager if you
  want, because you're charged for using this service. Deleting these certificates
  in Secrets Manager doesn't delete them from the Transfer Family server. Therefore, the
  functionality of the demo stack isn't affected. However, for certificates that
  you're going to use with a production AS2 server, you might want to use
  Secrets Manager to manage and periodically rotate your stored certificates.
- We recommend that you use the template as a base only, and mainly for
  demonstration purposes. If you want to use this demo stack in production, we
  recommend that you modify the template's YAML code to create a more robust
  stack. For example, create production-level certificates, and create an
  AWS Lambda function that you can use in production.

###### To create an AS2-enabled Transfer Family server from a CloudFormation template

1. Open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. In the left navigation pane, choose **Stacks**.
3. Choose **Create stack**, and then choose **With new
   resources (standard)**.
4. In the **Prerequisite - Prepare template** section, choose
   **Choose an existing template**.
5. Copy this link, [AS2 demo template](https://s3.amazonaws.com/aws-transfer-resources/as2-templates/aws-transfer-as2-basic.template.yml "https://s3.amazonaws.com/aws-transfer-resources/as2-templates/aws-transfer-as2-basic.template.yml"), and paste it into the **Amazon S3
   URL** field.
6. Choose **Next**.
7. On the **Specify stack details** page, name your stack, and
   then specify the following parameters:
   - Under **AS2**, enter values for **Local AS2
     ID** and **Partner AS2 ID**, or accept the
     defaults, `local` and `partner`, respectively.
   - Under **Network**, enter a value for
     **Security group ingress CIDR IP**, or accept the
     default, `0.0.0.0/0`.

   ###### Note

   This value, in CIDR format, specifies which IP addresses are
   allowed for incoming traffic to the AS2 server. The default value,
   `0.0.0.0/0`, allows all IP addresses.
   - Under **General**, enter a value for
     **Prefix**, or accept the default,
     `transfer-as2`. This prefix is placed before any resource
     names that are created by the stack. For example, if you use the default
     prefix, your Amazon S3 bucket is named
     `transfer-as2-`amzn-s3-demo-bucket``.

8. Choose **Next**. On the **Configure stack
   options** page, choose **Next** again.
9. Review the details for the stack that you're creating, and then choose
   **Create stack**.

###### Note

At the bottom of the page, under **Capabilities**, you
must acknowledge that CloudFormation might create AWS Identity and Access Management (IAM) resources.

After the stack is created, you can send a test AS2 message from the partner server to
your local Transfer Family server by using the AWS Command Line Interface (AWS CLI). A sample AWS CLI command for
sending a test message is created along with all of the other resources in the stack.

To use this sample command, go to the **Outputs** tab of your stack,
and copy the **TransferExampleAs2Command**. You can then run the
command by using the AWS CLI. If you haven't already installed the AWS CLI, see [Installing or updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the
_AWS Command Line Interface User Guide_.

The sample command has the following format:

```
aws s3api put-object --bucket `amzn-s3-demo-bucket` --key test.txt && aws transfer start-file-transfer --region `aws-region` --connector-id `TransferConnectorId` --send-file-paths /`amzn-s3-demo-bucket`/test.txt
```

###### Note

Your version of this command contains the actual values for the
`amzn-s3-demo-bucket` and
`TransferConnectorId` resources in
your stack.

This sample command consists of two separate commands that are chained together by
using the `&&` string.

The first command creates a new, empty text file in your bucket:

```
aws s3api put-object --bucket `amzn-s3-demo-bucket` --key test.txt
```

Then, the second command uses the connector to send the file from the partner profile
to the local profile. The Transfer Family server has an agreement set up that allows the local
profile to accept messages from the partner profile.

```
aws transfer start-file-transfer --region `aws-region` --connector-id `TransferConnectorId` --send-file-paths /`amzn-s3-demo-bucket`/test.txt
```

After you run the command, you can go to your Amazon S3 bucket
(`amzn-s3-demo-bucket`) and view the
contents. If the command is successful, you should see the following objects in your
bucket:

- `processed/` – This folder contains a JSON file that
  describes the transferred file and the MDN response.
- `processing/` – This folder temporarily contains files as
  they are being processed, but after a transfer is completed, this folder should
  be empty.
- ``server-id`/` – This folder is
named based on your Transfer Family server ID. It contains
`from-`partner`` (this folder is
  dynamically named, based on the partner's AS2 ID), which itself contains
  `failed/`, `processed/`, and `processing/`
  folders. The
  `/`server-id`/from-`partner`/processed/`
  folder contains a copy of the transferred text file, and the corresponding JSON
  and MDN files.
- `test.txt` – This object is the (empty) file that was
  transferred.

## Create an AS2 agreement

Agreements are associated with Transfer Family servers. They specify the details for trading
partners that use the AS2 protocol to exchange messages or files by using Transfer Family, for
_inbound_ transfers—sending AS2 files from an external,
partner-owned source to a Transfer Family server.

This procedure explains how to create AS2 agreements by using the Transfer Family console. If you
want to use the AWS CLI instead, see [Step 5: Create an agreement between
you and your partner](as2-example-tutorial.md#as2-create-agreement-example "as2-example-tutorial.md#as2-create-agreement-example").

###### To create an agreement for a Transfer Family server

1. Open the AWS Transfer Family console at [https://console.aws.amazon.com/transfer/](https://console.aws.amazon.com/transfer/ "https://console.aws.amazon.com/transfer/").
2. In the left navigation pane, choose **Servers**, and then
   choose a server that uses the AS2 protocol.

As an alternative, as long as you have at least one Transfer Family server that uses the
AS2 protocol, select **Agreements to receive messages** from
the **AS2 Trading Partners** menu. Then, in the
**Create agreement** screen, select the AS2 server to which
you want to associate this agreement. 3. On the server details page, scroll down to the **Agreements**
section. 4. Choose **Add agreement**. 5. Fill in the agreement parameters, as follows:

    1. In the **Agreement configuration** section, enter a
     descriptive name. Make sure that you can identify the agreement's
     purpose by its name. Also, set the **Status** for the
     agreement: either **Active** (selected by default) or
     **Inactive**.
    2. In the **Communication configuration** section,
     choose a local profile and a partner profile. Also, choose whether or
     not to enforce message signing.




    	* By default, **Enforce message signing** is
    	 enabled, which means that Transfer Family rejects unsigned messages from
    	 your trading partner for this agreement.
    	* Clear this setting to allow Transfer Family to accept unsigned messages
    	 from your trading partner for this agreement.
    3. In the **Inbox directory configuration** section,
     provide the following information.




    	* Determine whether or not to select **Specify separate
    	 directories to store your AS2 messages, MDN files, and JSON
    	 status files**.




    		+ If you select this option, you specify separate
    		 locations for payload files, failed files, MDN files,
    		 status files, and temporary files.
    		+ If you clear this option, all AS2 files go into the
    		 location that you specify for your base
    		 directory.
    	* For **S3 Bucket**, choose an Amazon S3
    	 bucket.
    	* For **Prefix**, you can enter a prefix
    	 (folder) to use for storing files in the bucket.


    	For example, if you enter
    	 `amzn-s3-demo-bucket` for your bucket
    	 and `incoming` for your prefix, your AS2
    	 files are saved to the
    	 `/`amzn-s3-demo-bucket`/incoming`
    	 folder.
    	* For **AWS IAM Role**, choose a role that
    	 can access the bucket you specified.
    	* For **Preserve filename**, choose whether to
    	 preserve original filenames for incoming AS2 message
    	 payloads.




    		+ If you select this setting, the filename provided by
    		 your trading parter is preserved when the file is saved
    		 in Amazon S3.
    		+ If you clear this setting, when Transfer Family saves the file,
    		 the filename is adjusted, as described in [File names and locations](send-as2-messages.md#file-names-as2 "send-as2-messages.md#file-names-as2").
    4. (Optional) Add tags in the **Tags** section.
    5. After you have entered all the information for the agreement, choose
     **Create agreement**.

The new agreement appears in the **Agreements** section of the server
details page.
