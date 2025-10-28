# SAProuter and SAP Solution Manager

The following sections describe options for SAProuter and SAP Solution Manager when running SAP solutions on AWS.

## For SAP All-on-AWS Architecture

When setting up an SAP environment on AWS, you will need to set up an SAP Solution Manager system and SAProuter with a connection to the SAP support network, as you would with any infrastructure. See the all-on-AWS architecture diagram ([Figure 3: SAP all-on-AWS architecture](overview-sap-planning.md#figure-3 "overview-sap-planning.md#figure-3")) for an illustration.

When setting up the SAProuter and SAP support network connection, follow these guidelines:

- Launch the instance that the SAProuter software is installed on into a public subnet of the VPC and assign it an Elastic IP address.
- Create a specific security group for the SAProuter instance with the necessary rules to allow the required inbound and outbound access to the SAP support network.
- Use the Secure Network Communications (SNC) type of internet connection. For more information, see [https://service.sap.com/internetconnection](https://service.sap.com/internetconnection "https://service.sap.com/internetconnection").
