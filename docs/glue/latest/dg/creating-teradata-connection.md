# Creating a Teradata Vantage connection

To connect to Teradata Vantage from AWS Glue, you will need to create and store your Teradata credentials in an
AWS Secrets Manager secret, then associate that secret with a AWS Glue Teradata connection.

**Prerequisites**:

- If you are accessing your Teradata environment through Amazon VPC, configure Amazon VPC to allow your AWS Glue job to communicate
  with the Teradata environment. We discourage accessing the Teradata environment over the public internet.

In Amazon VPC, identify or create a **VPC**, **Subnet** and
**Security group** that AWS Glue will use while executing the job. Additionally, you
need to ensure Amazon VPC is configured to permit network traffic between your Teradata instance and this
location. Your job will need to establish a TCP connection with your Teradata client port. For more
information about Teradata ports, see the [Teradata documentation](https://docs.teradata.com/r/Teradata-VantageTM-on-AWS-DIY-Installation-and-Administration-Guide/April-2020/Before-Deploying-Vantage-on-AWS-DIY/Security-Groups-and-Ports "https://docs.teradata.com/r/Teradata-VantageTM-on-AWS-DIY-Installation-and-Administration-Guide/April-2020/Before-Deploying-Vantage-on-AWS-DIY/Security-Groups-and-Ports").

Based on your network layout, secure VPC connectivity may require changes in Amazon VPC and other networking services.
For more information about AWS connectivity, consult [AWS Connectivity Options](https://docs.teradata.com/r/Teradata-VantageCloud-Enterprise/Get-Started/Connecting-Your-Environment/AWS-Connectivity-Options "https://docs.teradata.com/r/Teradata-VantageCloud-Enterprise/Get-Started/Connecting-Your-Environment/AWS-Connectivity-Options")
in the Teradata documentation.

###### To configure a AWS Glue Teradata connection:

1.  In your Teradata configuration, identify or create a user and password AWS Glue will connect with, `teradataUser` and `teradataPassword`. For more information,
    consult [Vantage Security Overview](https://docs.teradata.com/r/Configuring-Teradata-VantageTM-After-Installation/January-2021/Security-Overview/Vantage-Security-Overview "https://docs.teradata.com/r/Configuring-Teradata-VantageTM-After-Installation/January-2021/Security-Overview/Vantage-Security-Overview")
    in the Teradata documentation.
2.  In AWS Secrets Manager, create a secret using your Teradata credentials.
    To create a secret in Secrets Manager, follow the tutorial available in [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the AWS Secrets Manager documentation.
    After creating the secret, keep the Secret name, `secretName` for the next step.
    - When selecting **Key/value pairs**, create a pair for
      the key `user` with the value `teradataUsername`.
    - When selecting **Key/value pairs**, create a pair for
      the key `password` with the value `teradataPassword`.

3.  In the AWS Glue console, create a connection by following the steps in [Adding an AWS Glue connection](console-connections.md "console-connections.md").
    After creating the connection, keep the connection name, `connectionName`, for the next step.
    - When selecting a **Connection type**, select Teradata.
    - When providing **JDBC URL**, provide the URL for your instance. You can also hardcode
      certain comma separated connection parameters in your JDBC URL. The URL must conform to the
      following format:
      `jdbc:teradata://`teradataHostname`/`ParameterName`=`ParameterValue`,`ParameterName`=`ParameterValue``

    Supported URL parameters include:

        + `DATABASE`– name of database on host to access by default.
        + `DBS_PORT`– the database port, used when running on a nonstandard port.

    - When selecting a **Credential type**, select **AWS Secrets Manager**, then set **AWS Secret** to `secretName`.

4.  In the following situations, you may require additional configuration:
    - For Teradata instances hosted on AWS in an Amazon VPC
      - You will need to provide Amazon VPC connection information to the AWS Glue connection that defines your Teradata security credentials. When creating or updating your connection,
        set **VPC**, **Subnet** and **Security groups** in **Network options**.
