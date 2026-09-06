

# List connectors for Active Directory
<a name="list-connector-for-ads"></a>

You can use the AWS Private CA Connector for Active Directory console or AWS CLI to list the connectors that you own.

------
#### [ Console ]

**To list your connectors using the console**

1. Sign in to your AWS account and open the AWS Private CA Connector for Active Directory console at **[https://console.aws.amazon.com/pca-connector-ad/home](https://console.aws.amazon.com/pca-connector-ad/home)**. 

1. Review the information in the **Connectors for Active Directory** list. You can navigate through multiple pages of connectors using the page numbers at upper-right. Each connector occupies a row displaying the following columns of information by default. 
+ **Connector ID** – The unique ID of the connector.
+ **Directory name** – The Active Directory resource associated with the connector.
+ **Connector status** – Connector status. Possible values are: **Creating** \| **Active** \| **Deleting** \| **Failed**.
+ **Service principal name status** – Status of the service principal name (SPN) associated with the connector. Possible values are: **Creating** \| **Active** \| **Deleting** \| **Failed**.
+ **Directory registration status** – Registration status of the associate director. Possible values are:**Creating** \| **Active** \| **Deleting** \| **Failed**.
+ **Created at** – Time stamp at the connector's creation.

By choosing the gear icon in the upper-right corner of the console, you can customize the number of connectors shown on a page using the **Page size** preference.

------
#### [ API ]

**To list your connectors using the API**

Use the [ListConnectors](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ListConnectors.html) action in the AWS Private CA Connector for Active Directory API.

------
#### [ CLI ]

**To list your connectors using the AWS CLI**

Use the [list-connectors](https://docs.aws.amazon.com/cli/latest/reference/pca-connector-ad/list-connectors.html) command to list your connectors.

------