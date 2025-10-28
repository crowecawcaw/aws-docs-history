# Creating a MongoDB connection

**Prerequisites**:

- If your MongoDB instance is in an Amazon VPC, configure Amazon VPC to allow your AWS Glue job to communicate
  with the MongoDB instance without traffic traversing the public internet.

In Amazon VPC, identify or create a **VPC**, **Subnet** and
**Security group** that AWS Glue will use while executing the job. Additionally, you
need to ensure Amazon VPC is configured to permit network traffic between your MongoDB instance and this
location. Based on your network layout, this may require changes to security group rules, Network ACLs,
NAT Gateways and Peering connections.

###### To configure a connection to MongoDB:

1.  Optionally, in AWS Secrets Manager, create a secret using your MongoDB credentials.
    To create a secret in Secrets Manager, follow the tutorial available in [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the AWS Secrets Manager documentation.
    After creating the secret, keep the Secret name, `secretName` for the next step.
    - When selecting **Key/value pairs**, create a pair for
      the key `username` with the value `mongodbUser`.

    When selecting **Key/value pairs**, create a pair for
    the key `password` with the value `mongodbPass`.

2.  In the AWS Glue console, create a connection by following the steps in [Adding an AWS Glue connection](console-connections.md "console-connections.md").
    After creating the connection, keep the connection name, `connectionName`, for future use in AWS Glue.
    - When selecting a **Connection type**, select **MongoDB** or **MongoDB Atlas**.
    - When selecting **MongoDB URL** or **MongoDB Atlas URL**, provide the hostname of your MongoDB instance.

    A MongoDB URL is provided in the format `mongodb://`mongoHost`:`mongoPort`/`mongoDBname``.

    A MongoDB Atlas URL is provided in the format `mongodb+srv://`mongoHost`:`mongoPort`/`mongoDBname``.

    Providing the default database for the connection, `mongoDBname` is optional.
    - If you chose to create an Secrets Manager secret, choose the AWS Secrets Manager **Credential type**.

    Then, in **AWS Secret** provide `secretName`.
    - If you choose to provide **Username and password**, provide
      `mongodbUser` and `mongodbPass`.

3.  In the following situations, you may require additional configuration:

        * For MongoDB instances hosted on AWS in an Amazon VPC



        	+ You will need to provide Amazon VPC connection information to the AWS Glue connection that
        	 defines your MongoDB security credentials. When creating or updating your
        	 connection, set **VPC**, **Subnet** and
        	 **Security groups** in **Network options**.

    After creating a AWS Glue MongoDB connection, you will need to perform the following steps before running your AWS Glue job:

- When working with AWS Glue jobs in the visual editor, you must provide Amazon VPC connection information
  for your job to connect to MongoDB. Identify a suitable location in Amazon VPC and provide it to your
  AWS Glue MongoDB connection.
- If you chose to create an Secrets Manager secret, grant the IAM role associated with your AWS Glue job permission to read `secretName`.
