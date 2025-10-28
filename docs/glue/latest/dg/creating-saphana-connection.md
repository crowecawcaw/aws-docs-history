# Creating a SAP HANA connection

To connect to SAP HANA from AWS Glue, you will need to create and store your SAP HANA credentials
in a AWS Secrets Manager secret, then associate that secret with a SAP HANA AWS Glue connection. You will need to configure
network connectivity between your SAP HANA service and AWS Glue.

**Prerequisites**:

- If your SAP HANA service is in an Amazon VPC, configure Amazon VPC to allow your AWS Glue job to communicate
  with the SAP HANA service without traffic traversing the public internet.

In Amazon VPC, identify or create a **VPC**, **Subnet** and
**Security group** that AWS Glue will use while executing the job. Additionally, you
need to ensure Amazon VPC is configured to permit network traffic between your SAP HANA endpoint and this
location. Your job will need to establish a TCP connection with your SAP HANA JDBC port. For more
information about SAP HANA ports, see the [SAP HANA documentation](https://help.sap.com/docs/HANA_SMART_DATA_INTEGRATION/7952ef28a6914997abc01745fef1b607/88e2e8bded9e4041ad3ad87dc46c7b55.html?locale=en-US "https://help.sap.com/docs/HANA_SMART_DATA_INTEGRATION/7952ef28a6914997abc01745fef1b607/88e2e8bded9e4041ad3ad87dc46c7b55.html?locale=en-US"). Based on your network layout, this may require changes to security
group rules, Network ACLs, NAT Gateways and Peering connections.

###### To configure a connection to SAP HANA:

1.  In AWS Secrets Manager, create a secret using your SAP HANA credentials.
    To create a secret in Secrets Manager, follow the tutorial available in [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the AWS Secrets Manager documentation.
    After creating the secret, keep the Secret name, `secretName` for the next step.
    - When selecting **Key/value pairs**, create a pair for
      the key `username/USERNAME` with the value `saphanaUsername`.
    - When selecting **Key/value pairs**, create a pair for
      the key `password/PASSWORD` with the value `saphanaPassword`.

2.  In the AWS Glue console, create a connection by following the steps in [Adding an AWS Glue connection](console-connections.md "console-connections.md").
    After creating the connection, keep the connection name, `connectionName`, for future use in AWS Glue.

        * When selecting a **Connection type**, select SAP HANA.
        * When providing **SAP HANA URL**, provide the URL for your instance.


        SAP HANA JDBC URLs are in the form `jdbc:sap://`saphanaHostname`:`saphanaPort`/?`databaseName`=`saphanaDBname`,`ParameterName`=`ParameterValue``


        AWS Glue requires the following JDBC URL parameters:




        	+ `databaseName` – A default database in SAP HANA to connect to.
        * When selecting an **AWS Secret**, provide `secretName`.

    After creating a AWS Glue SAP HANA connection, you will need to perform the following steps before running your AWS Glue job:

- Grant the IAM role associated with your AWS Glue job permission to read `secretName`.
