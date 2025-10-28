# Creating a Vertica connection

**Prerequisites**:

- An Amazon S3 bucket or folder to use for temporary storage when reading from and writing to the
  database, referred to by `tempS3Path`.

###### Note

When using Vertica in AWS Glue job data previews, temporary files may not be automatically
removed from `tempS3Path`. To ensure the removal of temporary files,
directly end the data preview session by choosing **End session** in the
**Data preview** pane.

If you cannot guarantee the data preview session is ended directly, consider setting Amazon S3
Lifecycle configuration to remove old data. We recommend removing data
older than 49 hours, based on maximum job runtime plus a margin. For more information about
configuring Amazon S3 Lifecycle, see [Managing your storage
lifecycle](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") in the Amazon S3 documentation.

- An IAM policy with appropriate permissions to your Amazon S3 path you can associate with your AWS Glue job role.
- If your Vertica instance is in an Amazon VPC, configure Amazon VPC to allow your AWS Glue job to communicate
  with the Vertica instance without traffic traversing the public internet.

In Amazon VPC, identify or create a **VPC**, **Subnet** and
**Security group** that AWS Glue will use while executing the job. Additionally, you
need to ensure Amazon VPC is configured to permit network traffic between your Vertica instance and this
location. Your job will need to establish a TCP connection with your Vertica client port, (default
5433). Based on your network layout, this may require changes to security group rules, Network ACLs,
NAT Gateways and Peering connections.

###### To configure a connection to Vertica:

1.  In AWS Secrets Manager, create a secret using your Vertica credentials,
    `verticaUsername` and `verticaPassword`. To create
    a secret in Secrets Manager, follow the tutorial available in [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in
    the AWS Secrets Manager documentation. After creating the secret, keep the Secret name,
    `secretName` for the next step.
    - When selecting **Key/value pairs**, create a pair for the key
      `user` with the value `verticaUsername`.
    - When selecting **Key/value pairs**, create a pair for the key
      `password` with the value `verticaPassword`.

2.  In the AWS Glue console, create a connection by following the steps in [Adding an AWS Glue connection](console-connections.md "console-connections.md").
    After creating the connection, keep the connection name, `connectionName`, for the next step.
    - When selecting a **Connection type**, select Vertica.
    - When selecting **Vertica Host**, provide the hostname of your Vertica installation.
    - When selecting **Vertica Port**, the port your Vertica installation is available through.
    - When selecting an **AWS Secret**, provide `secretName`.

3.  In the following situations, you may require additional configuration:

        * For Vertica instances hosted on AWS in an Amazon VPC



        	+ Provide Amazon VPC connection information to the AWS Glue connection that
        	 defines your Vertica security credentials. When creating or updating your
        	 connection, set **VPC**, **Subnet** and
        	 **Security groups** in **Network options**.

    You will need to perform the following steps before running your AWS Glue job:

- Grant the IAM role associated with your AWS Glue job permissions to `tempS3Path`.
- Grant the IAM role associated with your AWS Glue job permission to read `secretName`.
