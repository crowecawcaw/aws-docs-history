# SAP OData connector for Amazon AppFlow

The Amazon AppFlow SAP OData connector provides the ability to fetch, create, and update records
exposed by SAP S/4HANA and SAP on premises systems through OData APIs.

With this connector, you can connect Amazon AppFlow to your OData services, including those that
extract data from SAP applications that use the Operational Data Provisioning (ODP) framework.
These applications are called ODP providers. For more information about how OData services can
extract ODP data in SAP, see [ODP-Based Data Extraction via OData](https://help.sap.com/docs/SAP_BPC_VERSION_BW4HANA/dd104a87ab9249968e6279e61378ff66/11853413cf124dde91925284133c007d.html?version=11.0 "https://help.sap.com/docs/SAP_BPC_VERSION_BW4HANA/dd104a87ab9249968e6279e61378ff66/11853413cf124dde91925284133c007d.html?version=11.0") in the SAP BW/4HANA documentation.

When you connect Amazon AppFlow to ODP providers, you can create flows that run full data transfers
or incremental updates. Incremental updates for ODP data are efficient because they transfer only
those records that changed since the prior flow run.

## Amazon AppFlow support for SAP OData

With the SAP OData connector, Amazon AppFlow supports SAP as follows.

**Supported as a data source?**

Yes. You can use Amazon AppFlow to transfer data from SAP.

**Supported as a data destination?**

Amazon AppFlow supports SAP OData as a destination, but not for ODP data. You can use Amazon AppFlow to
transfer data to an OData service, but you can't transfer data to an ODP provider.

## Before you begin

To use Amazon AppFlow to transfer data from SAP OData to supported destinations, you must meet these
requirements:

- Your SAP NetWeaver stack version must be 7.40 SP02 or above.
- You must enable catalog service for service discovery.
  - **OData V2.0:** The OData V2.0 catalog service(s) can be
    enabled in your SAP Gateway via transaction **/IWFND/MAINT_SERVICE** .

  ![Service catalog interface showing two catalog services with version and description details.](images/sapodata-odatav2-catalog-service-enablement.png)
  - **OData V4.0:** The OData V4.0 catalog services can be
    enabled in your SAP Gateway environment by publishing the service groups **/IWFND/CONFIG** or as described in the SAP documentation relevant to
    your gateway version.

  ![Service group configuration interface showing available system aliases and services.](images/sapodata-odatav4-catalog-service-enablement.png)

- You must enable OData V2.0/V4.0 services in your SAP Gateway. The OData V2.0 services can
  be enabled via transaction **/IWFND/MAINT_SERVICE** and V4.0
  services can be published via transaction **/IWFND/V4_ADMIN**.
- Your SAP OData service must support client side pagination/query options such as **$top** and **$skip**. It must also support
  system query option **$count**.
- Amazon AppFlow supports following authentication mechanisms:
  - **Basic** - Supported for OData V2.0 and OData V4.0
  - **OAuth 2.0** - Supported for only OData V2.0. You must
    enable OAuth 2.0 for the OData service and register the OAuth client per SAP documentation
    and set the authorized redirect URL as follows:
    - https://console.aws.amazon.com/appflow/oauth for the us-east-1 Region
    - https://region.console.aws.amazon.com/appflow/oauth for all other Regions

- You must enable secure setup for connecting over HTTPS.
- You must provide required authorization for the user in SAP to discover the services and
  extract data using SAP OData services. Please refer to the security documentation provided by
  SAP.

### ODP Requirements

Before you can transfer data from an ODP provider, you need to meet the following
requirements:

- You have an SAP NetWeaver AS ABAP instance.
- Your SAP NetWeaver instance contains an ODP provider that you want to transfer data from.
  ODP providers include:
  - SAP DataSources (Transaction code RSO2)
  - SAP Core Data Services ABAP CDS Views
  - SAP BW or SAP BW/4HANA systems (InfoObject, DataStore Object)
  - Real-time replication of Tables and DB-Views from SAP Source System via SAP Landscape
    Replication Server (SAP SLT)
  - SAP HANA Information Views in SAP ABAP based Sources

- Your SAP NetWeaver instance has the SAP Gateway Foundation component.
- You have created an OData service that extracts data from your ODP provider. To create
  the OData service, you use the SAP Gateway Service Builder. To access your ODP data, Amazon AppFlow
  calls this service by using the OData API. For more information, see [Generating a Service for Extracting ODP Data via OData](https://help.sap.com/docs/SAP_BPC_VERSION_BW4HANA/dd104a87ab9249968e6279e61378ff66/69b481859ef34bab9cc7d449e6fff7b6.html?version=11.0 "https://help.sap.com/docs/SAP_BPC_VERSION_BW4HANA/dd104a87ab9249968e6279e61378ff66/69b481859ef34bab9cc7d449e6fff7b6.html?version=11.0") in the SAP BW/4HANA
  documentation.
- To generate an OData service based on ODP data sources, SAP Gateway Foundation must be
  installed locally in your ERP/BW stack or in a hub configuration.
  - For your ERP/BW applications, the SAP NetWeaver AS ABAP stack must be at 7.50 SP02 or
    above.
  - For the hub system (SAP Gateway), the SAP NetWeaver AS ABAP of the hub system must be
    7.50 SP01 or above for remote hub setup.

### Private Connection Requirements

Before you can create a private connection to SAP, you need to meet the following
requirements:

- You need to create VPC Endpoint Service for your SAP OData instance running in a VPC.
  This VPC endpoint service must have Amazon AppFlow service principal **appflow.amazonaws.com** as allowed principal and must be available in **at least more than 50% AZs in a region**.
- When creating connection using OAuth, your **Authorization Code
  URL** must be reachable by the network from where the connection is being setup.
  This is because OAuth connection involves browser interaction with SAP Login Page which cannot
  happen over AWS PrivateLink. The network from where the connection is being setup must be
  connected to SAP OData instance running in a VPC so that hostname of authorization code url
  can be resolved. Alternately, you can choose to make your Authorization Code URL available
  over public internet so that console user interaction can happen from any network.
- For OAuth, in addition to **Application Host URL**, your
  **Authorization Tokens URL** must also be available behind VPC
  Endpoint Service to fetch Access/Refresh tokens over private network.
- For OAuth, you must set your OAuthCode expiry to at least 5 minutes.

## Connecting Amazon AppFlow to your SAP account

To connect Amazon AppFlow to your SAP account, provide details about your SAP OData service
so that Amazon AppFlow can access your data. If you haven't yet configured your SAP OData
service for Amazon AppFlow integration, see [Before you begin](#sapodata-requirements "#sapodata-requirements").

###### To create an SAP OData connection

1.  Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2.  In the navigation pane on the left, choose **Connections**.
3.  On the **Manage connections** page, for **Connectors**,
    choose **SAP OData**.
4.  Choose **Create connection**.
5.  In the **Connect to SAP OData** window, enter the following
    information:

        1. Under **Application Host URL**, enter your Application host url. This
         application host url must be accessible over public internet for non PrivateLink
         connection.
        2. Under **Application Service Path**, enter your catalog service path.
         e.g.**/sap/opu/odata/iwfnd/catalogservice;v=2**. Amazon AppFlow doesn’t accept
         specific object path.
        3. Under **Port Number**, enter your port number.
        4. Under **Client Number**, enter your 3 digit client number. Acceptable
         values are [001-999]. e.g.**010**
        5. Under **Logon Language**, enter your two character logon language. e.g.
         **EN**.
        6. (Optional) To use private connection for data transfer, under **AWS PrivateLink
         service name**, enter your VPC Endpoint (PrivateLink) service name. e.g.
         **com.amazonaws.vpce.us-east-1.vpce-svc-xxxxxxxxxxxxxx**
        7. Select your preferred Authentication Mode.


        	* If Basic,


        		1. Under **User name**, enter your useraname.
        		2. Under **Password**, enter your password.
        	* If OAuth2,


        		1. Under **Authorization Code URL**, enter your authorization code
        		 URL.
        		2. Under **Authorization Tokens URL**, enter your authorization token
        		 URL.
        		3. Under **OAuth Scopes**, enter your OAuth scopes separated by space.
        		 e.g.**/IWFND/SG\_MED\_CATALOG\_0002 ZAPI\_SALES\_ORDER\_SRV\_0001**
        		4. Under **Client ID**, enter your client id .
        		5. Under **Client Secret**, enter your client secret .
        8. Optionally, under **Data encryption**, choose **Customize
         encryption settings (advanced)** if you want to encrypt your data with a customer
         managed key in the AWS Key Management Service (AWS KMS).


        By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
         for you. Choose this option if you want to encrypt your data with your own KMS key instead.


        Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
         [Data protection in Amazon AppFlow](data-protection.md "data-protection.md").


        If you want to use a KMS key from the current AWS account, select this key under
         **Choose an AWS KMS key**. If you want to use a KMS key from a different
         AWS account, enter the Amazon Resource Name (ARN) for that key.
        9. Under **Connection name**, specify a name for your connection.
        10. Choose **Continue**.
        11. If using OAuth, you will be redirected to the SAP login page. When prompted, grant
         Amazon AppFlow permissions to access your SAP account.

    ![Form to connect SAP OData with AWS PrivateLink, showing fields for configuration and OAuth2 authentication.](images/connection_setup-sapodata-console.png)

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses SAP OData as the data source, you can select this connection.

If you chose to enable PrivateLink, note the following:

- Amazon AppFlow creates AWS PrivateLink Endpoint (if not already present) connection to your
  VPC Endpoint Service before any metadata/data transfer calls can be made to your SAP OData
  instance over private network. AWS PrivateLink Endpoint creation can take 3-5 minutes, and
  until its created, profile status would be PENDING. While the connection status is PENDING, you
  are unable to transfer SAP OData objects with a flow.
- If your VPC Endpoint Service has **Acceptance Required** setting set to
  true, you will need to accept the connection in the AWS account which has VPC Endpoint service
  for AWS PrivateLink endpoint provisioning to start.
- Once the AWS PrivateLink Endpoint connection is established, Amazon AppFlow fetches (only for
  OAuth) access/refresh tokens using the authCode, makes a test connection call over private
  network, and finally changes connection status from PENDING to CREATED.
- If for any reason private connection creation fails, connection status would change to
  FAILED.

## Transferring data from SAP OData with a flow

To transfer data from SAP OData, create an Amazon AppFlow flow, and choose
SAP OData as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose which data object you want to transfer. If the data
object originates from an ODP provider, you can configure the flow so that it runs efficient
incremental updates that transfer changed records only.

### Transferring ODP data

When you create a flow that transfers an ODP data object, you can configure the flow to run
_incremental_ or _full_ data
transfers.

#### Incremental ODP data transfers

When you create a flow that transfers ODP data incrementally, it does the
following:

- It subscribes to the _operational delta queue_ of your
  ODP provider. This queue provides Amazon AppFlow with delta tokens, which indicate changes made to
  the provider's records in SAP.
- For the initial flow run, it performs a full data transfer. It obtains all available
  records from your ODP provider, except for any that you omit by adding filters to your flow
  configuration.
- For subsequent flow runs, it performs incremental data transfers. By using the
  information provided by the delta tokens, it transfers only those records that changed after
  the last flow run.

When you create an SAP OData flow in the Amazon AppFlow console, you can configure it to transfer
data incrementally in the **Flow trigger** section, where you do the
following:

1. Choose **Run flow on schedule**.
2. Use the scheduling fields to specify when the flow begins, how often it repeats, and
   when it ends.
3. Under **Transfer mode**, choose **Incremental
   transfer**.

For ODP data objects specifically, the console requires no additional input. This
behavior differs from SAP data objects that don't come from an ODP provider. For those
objects, you must specify a source timestamp field that Amazon AppFlow uses to identify new or
changed records. For ODP data, no such timestamp is necessary because Amazon AppFlow uses the
information that's provided by the delta token that it receives from the operational delta
queue.

###### Important

When you create an incremental flow for an ODP data object, the flow creates a
subscription to the operational delta queue for that object. Although Amazon AppFlow creates these
subscriptions, it doesn't administer them on your behalf. Keep the following subscription
behaviors in mind to prevent unwanted effects:

- When a flow subscribes to a queue, it also removes all prior subscriptions to that
  queue. If you previously created any scheduled flows that transfer the same object, delete
  those flows. They no longer receive delta tokens, and they stop performing incremental data
  transfers. For any individual ODP object, maintain only one scheduled flow at a time.
- When you delete a flow that subscribes to an operational delta queue, that operation
  does not delete the subscription itself. You can only delete the subscription by using the
  SAP system to do so.

#### Full ODP data transfers

You can create flows that run full data transfers of your ODP data. For these flows,
Amazon AppFlow does not create subscriptions to operational delta queues like it does for incremental
flows.

When you create an SAP OData flow in the Amazon AppFlow console, you can configure it to run full
data transfers in the **Flow trigger** section, where you do the
following:

- Under **Choose how to trigger the flow**, do either of the
  following:
  - Choose **Run on demand**. After you create an on-demand flow, you run
    it manually by choosing **Run flow** on its details page in the Amazon AppFlow
    console.
  - Choose **Run flow on schedule** and define your schedule:.
    1. Use the scheduling fields to specify when the flow begins, how often it repeats, and
       when it ends.
    2. For **Transfer mode**, choose **Full
       transfer.**

    ###### Note

    To create a flow that runs full data transfers, the frequency that you choose must
    be no more frequent than **Daily**. If it is more frequent, then you
    won't be able to choose **Full transfer**.

## Advanced capabilities for the SAP OData connector

For the SAP OData connector, Amazon AppFlow supports a couple unique capabilities that are
unavailable with other destination-enabled connectors. With it, you can:

- Capture the SAP success response when you create a new
  record.
- Create deep entities with the SAP OData deep insert feature. For more information about
  this feature, see [Deep Insert](https://help.sap.com/viewer/68bf513362174d54b58cddec28794093/7.40.22/en-US/11a426519eff236ee10000000a445394.html "https://help.sap.com/viewer/68bf513362174d54b58cddec28794093/7.40.22/en-US/11a426519eff236ee10000000a445394.html") in the SAP Gateway Foundation documentation.

You can use these capabilities individually or in combination. For example, you can capture
SAP's success response when you insert a deep entity.

To enable these capabilities, complete the following steps.

###### To capture the SAP success response for new records

1. Create an Amazon S3 bucket. The bucket must be in the same AWS Region as the flow that you
   create for your SAP OData connector. For the steps to create a bucket, see [Creating a
   bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon S3 User Guide_.
2. Configure the flow by following the steps in [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md"), but do one additional step:
   1. On the **Configure flow** page, under **Response
      handling**, select the bucket that you created. The SAP success response payload is
      delivered to this bucket when finish creating your flow.

###### To create SAP deep entities

1. Generate a JSON Lines input file that defines one deep entity per line, as shown by the
   following example.

JSON Lines (required format)
The following input file defines two deep entities in JSON Lines format (also called
newline-delimited JSON). In this format, each line is a complete JSON object that defines an
individual deep entity.

Each deep entity can include multiple levels of hierarchical data. This example creates
two Sales Orders, and each contains two associated Sales Order Items.

```
{"SalesOrderType": "OR","SalesOrganization": "1710","DistributionChannel": "10","OrganizationDivision": "00","SoldToParty": "USCU_S13","TransactionCurrency": "USD","PurchaseOrderByCustomer": "TEST-PO2021","to_Item": [{"Material": "MZ-FG-C990","RequestedQuantity": "10","RequestedQuantityUnit": "PC"},{"Material": "MZ-FG-M500","RequestedQuantity": "10","RequestedQuantityUnit": "PC"}]}
{"SalesOrderType": "OR","SalesOrganization": "1710","DistributionChannel": "10","OrganizationDivision": "00","SoldToParty": "USCU_S13","TransactionCurrency": "USD","PurchaseOrderByCustomer": "TEST-PO2021","to_Item": [{"Material": "MZ-FG-C990","RequestedQuantity": "10","RequestedQuantityUnit": "PC"},{"Material": "MZ-FG-M500","RequestedQuantity": "10","RequestedQuantityUnit": "PC"}]}
```

Formatted JSON (for readability)
The following example shows one of the deep entities from the JSON Lines input file.
This example is formatted for readability so that you can more easily see the nested JSON
values.

```
{
  "SalesOrderType": "OR",
  "SalesOrganization": "1710",
  "DistributionChannel": "10",
  "OrganizationDivision": "00",
  "SoldToParty": "USCU_S13",
  "TransactionCurrency": "USD",
  "PurchaseOrderByCustomer": "TEST-PO2021",
  "to_Item":
  [
    {
      "Material": "MZ-FG-C990",
      "RequestedQuantity": "10",
      "RequestedQuantityUnit": "PC"
    },
    {
      "Material": "MZ-FG-M500",
      "RequestedQuantity": "10",
      "RequestedQuantityUnit": "PC"
    }
  ]
}
```

Remember that Amazon AppFlow requires JSON Lines format, so this example would be an invalid
input file. 2. Create an Amazon S3 bucket. The bucket must be in the same AWS Region as the flow that you
create for your SAP OData connector. For the steps to create a bucket, see [Creating a
bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon S3 User Guide_. 3. Upload your deep entities input file to the bucket that you created. For the steps to
upload a file, see [Uploading objects](../../../AmazonS3/latest/userguide/upload-objects.md "../../../AmazonS3/latest/userguide/upload-objects.md") in the _Amazon S3 User Guide_. 4. Configure the flow by following the steps in [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md"), but do one alternate step:

    1. On the **Map data fields** page, under **Mapping
     method**, choose **Passthrough fields without
     modification**.


    ###### Note

    When you choose this option, the console disables the options under **Source to
     destination field mapping**. With this option, you don't define mappings in the
     console. Instead, the fields in your input file must match the fields that you use in
     SAP.

### Transferring data with concurrent processes

When you configure a flow that transfers OData records from an SAP instance, you can speed
up the transfer by setting multiple _concurrent processes_.
Each concurrent process is a query that retrieves a batch of records from your SAP instance.
When the flow transfers your data, it runs these processes at the same time. As a result, the
flow uses multiple parallel threads that can transfer large datasets more quickly.

###### Note

Amazon AppFlow supports concurrent processes only for flows that do the following:

- Transfer OData records.
- Transfer from SAP as the data source.
  Amazon AppFlow doesn’t support this feature for ODP records or for flows that transfer to SAP as
  the data destination.

###### To transfer your data with concurrent processes

Configure the flow by following the steps in [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md"), and do these additional steps:

1. On the **Configure flow** page, choose your SAP OData connector under
   **Source details**.
2. In the **Source details** section, under **Additional
   settings**, set the following options:

**Batch size**

The maximum number of records that Amazon AppFlow receives in each page of the response from
your SAP application. For transfers of OData records, the maximum page size is 3,000. For
transfers of data that comes from an ODP provider, the maximum page size is 10,000.

**Maximum number of concurrent processes**

The maximum number of processes that Amazon AppFlow runs at the same time when it retrieves
your data. The default value is one. You can specify up to 10.

![Additional settings panel with batch size and concurrent processes options for SAP data transfer.](images/sapodata-concurrent-processes.png)

When the flow runs, Amazon AppFlow calculates how many processes it needs by dividing the number of
records in your instance with the batch size. If the number is less than the maximum, the flow
runs the processes only once, and it runs only as many processes as it needs. If the number
exceeds the maximum, the flow runs the processes multiple times, and it doesn’t exceed the
maximum at any one time.

## Notes

- When you use SAP OData as a source, you can run schedule-triggered flows at a maximum
  frequency of one flow runs per minute.
- If you have a private ConnectorProfile for a VPC endpoint service, and you try to create
  another private ConnectorProfile for the same VPC endpoint service, Amazon AppFlow will re-use the
  already created private connection, and thus you would not need to wait for private connection
  provisioning to complete to list and choose SAP OData object.
- Amazon AppFlow allows at max 1000 flow executions at a time per AWS account. If you choose to
  run multiple flows against the same SAP OData instance, you need to accordingly scale your
  instance.

## Supported destinations

When you create a flow that uses SAP OData as the data source, you can set the destination to any of the following connectors:

- Amazon Connect
- Amazon Redshift
- Amazon S3
- SAP OData

You can also set the destination to any custom connectors that you
create with the Amazon AppFlow Custom Connector SDKs for [Python](https://github.com/awslabs/aws-appflow-custom-connector-python "https://github.com/awslabs/aws-appflow-custom-connector-python") or [Java](https://github.com/awslabs/aws-appflow-custom-connector-java "https://github.com/awslabs/aws-appflow-custom-connector-java") . You can download these SDKs from GitHub.

## Related resources

- [Setting up SAP
  Gateway](https://help.sap.com/viewer/product/SAP_GATEWAY "https://help.sap.com/viewer/product/SAP_GATEWAY") in _SAP_ documentation.
