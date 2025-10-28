# AWS Glue support for SAP OData

AWS Glue supports SAP OData as follows:

###### Supported as a source?

Yes. You can use AWS Glue ETL jobs to query data from SAP OData.

###### Supported as a target?

Yes. You can use AWS Glue ETL jobs to write records into SAP OData.

###### Supported SAP OData API versions

The following SAP OData API versions are supported:

- 2.0

###### Supported sources

The following sources are supported:

- ODP (Operational Data Provisioning) Sources:
  - BW Extractors (DataSources)
  - CDS Views
  - SLT

- Non-ODP Sources, for example:
  - CDS View Services
  - RFC-based Services
  - Custom ABAP Services

###### Supported SAP Components

The following are minimum requirements:

- You must enable catalog service for service discovery.
  - Configure operational data provisioning (ODP) data sources for extraction in the SAP Gateway of your SAP system.
  - **OData V2.0**: Enable the OData V2.0 catalog service(s) in your SAP Gateway via transaction `/IWFND/MAINT_SERVICE`.
  - Enable OData V2.0 services in your SAP Gateway via transaction `/IWFND/MAINT_SERVICE`.
  - Your SAP OData service must support client side pagination/query options such as `$top` and `$skip`. It must also support system query option `$count`.
  - You must provide the required authorization for the user in SAP to discover the services and extract data using SAP OData services. Refer to the security documentation provided by SAP.

- If you want to use OAuth 2.0 as an authorization mechanism, you must enable OAuth 2.0 for the OData service and register the OAuth client per SAP documentation.
- To generate an OData service based on ODP data sources, SAP Gateway Foundation must be installed locally in your ERP/BW stack or in a hub configuration.
  - For your ERP/BW applications, the SAP NetWeaver AS ABAP stack must be at 7.50 SP02 or above.
  - For the hub system (SAP Gateway), the SAP NetWeaver AS ABAP of the hub system must be 7.50 SP01 or above for remote hub setup.

- For non-ODP sources, your SAP NetWeaver stack version must be 7.40 SP02 or above.

###### Supported Authentication Methods

The following authentication methods are supported:

- Basic Authentication
- OAuth 2.0
