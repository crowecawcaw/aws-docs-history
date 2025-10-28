# SAP OData activation

Complete the following steps for SAP OData connection:

## ODP Sources

Before you can transfer data from an ODP provider, you must meet the following requirements:

- You have an SAP NetWeaver AS ABAP instance.
- Your SAP NetWeaver instance contains an ODP provider that you want to transfer data from. ODP providers include:
  - SAP DataSources (Transaction code RSO2)
  - SAP Core Data Services ABAP CDS Views
  - SAP BW or SAP BW/4HANA systems (InfoObject, DataStore Object)
  - Real-time replication of Tables and DB-Views from SAP Source System via SAP Landscape Replication Server (SAP SLT)
  - SAP HANA Information Views in SAP ABAP based Sources

- Your SAP NetWeaver instance has the SAP Gateway Foundation component.
- You have created an OData service that extracts data from your ODP provider. To create the OData service, you use the SAP Gateway Service Builder. To access your ODP data, Amazon AppFlow calls this service by using the OData API. For more information, see [Generating a Service for Extracting ODP Data via OData](https://help.sap.com/docs/SAP_BPC_VERSION_BW4HANA/dd104a87ab9249968e6279e61378ff66/69b481859ef34bab9cc7d449e6fff7b6.html?version=11.0 "https://help.sap.com/docs/SAP_BPC_VERSION_BW4HANA/dd104a87ab9249968e6279e61378ff66/69b481859ef34bab9cc7d449e6fff7b6.html?version=11.0") in the SAP BW/4HANA documentation.
- To generate an OData service based on ODP data sources, SAP Gateway Foundation must be installed locally in your ERP/BW stack or in a hub configuration.
  - For your ERP/BW applications, the SAP NetWeaver AS ABAP stack must be at 7.50 SP02 or above.
  - For the hub system (SAP Gateway), the SAP NetWeaver AS ABAP of the hub system must be 7.50 SP01 or above for remote hub setup.

## Non-ODP Sources

- Your SAP NetWeaver stack version must be 7.40 SP02 or above.
- You must enable catalog service for service discovery.
  - **OData V2.0**: The OData V2.0 catalog service(s) can be enabled in your SAP Gateway via transaction `/IWFND/MAINT_SERVICE`

- Your SAP OData service must support client side pagination/query options such as `$top` and `$skip`. It must also support system query option `$count`.
- For OAuth 2.0, you must enable OAuth 2.0 for the OData service and register the OAuth client per SAP documentation and set the authorized redirect URL as follows:
  - `https://<region>.console.aws.amazon.com/gluestudio/oauth`, replacing `<region>` with the region where AWS Glue is running, example: us-east-1.
  - You must enable secure setup for connecting over HTTPS.

- You must provide required authorization for the user in SAP to discover the services and extract data using SAP OData services. Please refer to the security documentation provided by SAP.
