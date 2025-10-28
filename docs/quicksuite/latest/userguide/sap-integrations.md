# SAP workload integrations

With SAP workload integrations, you can perform actions within various SAP systems. Manage
business data, inventory, materials, and business processes. These integrations support
action execution only and require Amazon Quick Suite Pro tier or higher.

## What you can do

SAP workload integrations provide enterprise-level connectivity to help you work with
your SAP systems.

**Action connector**

Perform actions within SAP systems. Create, update, and manage business data, inventory records, material information, and other enterprise operations through SAP APIs.

**Multiple SAP modules**

Support for five different integration types: Bill of Materials, Business
Partner, Material Stock, Physical Inventory Documents, and Product
Master.

## Before you begin

Before you set up SAP workload integrations, make sure you have the following:

- SAP system with appropriate modules installed and configured.
- SAP user account with necessary permissions and authorizations.
- Amazon Quick Suite Author or higher.
- Network connectivity between Amazon Quick Suite and your SAP system.

## Prepare SAP system configuration and authentication

Before setting up the integration in Amazon Quick Suite, prepare your SAP system
configuration and user authentication. SAP workload integrations support multiple
authentication methods and require proper system setup.

### Authentication methods

SAP workload integrations support two authentication methods:

**OAuth 2.0 (Recommended)**

Secure authentication method for automated workflows. Requires OAuth configuration in your SAP system.

**Required parameters:**

- **Client ID** - SAP OAuth Client ID
- **Client Secret** - SAP OAuth Client Secret
- **Token URL** - OAuth token endpoint (e.g., `https://hostname:port/sap/bc/sec/oauth2/token?sap-client=100`)
- **Domain URL** - SAP system API endpoint (e.g., `https://hostname:port/sap/opu/odata/sap/API_BUSINESS_PARTNER`)

**Basic Authentication**

Username and password authentication for direct SAP system access.

**Required parameters:**

- **Username** - SAP system username
- **Password** - SAP system password
- **Domain URL** - SAP system API endpoint

### SAP system configuration requirements

Before using SAP workload integrations, ensure your SAP system is properly
configured:

#### OAuth 2.0 setup

For OAuth 2.0 authentication:

- Configure the OAuth authorization server with appropriate scopes
- Verify OAuth is enabled for the service using transaction code `/IWFND/MAINT_SERVICE`
- Refer to SAP documentation for detailed OAuth 2.0 configuration: [OAuth 2.0 Configuration Guide](https://help.sap.com/docs/ABAP_PLATFORM_NEW/fd0fc52fd22b45f29d274a7f8236e768/cdb122d5b0784c77bf1bcce17f730e74.html "https://help.sap.com/docs/ABAP_PLATFORM_NEW/fd0fc52fd22b45f29d274a7f8236e768/cdb122d5b0784c77bf1bcce17f730e74.html")

#### SAP API activation

Ensure the required SAP API services are active:

- Activate the specific API service for your chosen SAP connector
- Verify API service status in your SAP system
- Refer to SAP documentation for API activation: [SAP API Service Activation Guide](https://help.sap.com/doc/saphelp_nw75/7.5.5/en-US/1b/023c1cad774eeb8b85b25c86d94f87/frameset.htm "https://help.sap.com/doc/saphelp_nw75/7.5.5/en-US/1b/023c1cad774eeb8b85b25c86d94f87/frameset.htm")

### Available SAP workload integration

types

Choose the SAP integration type that matches your business needs and ensure the corresponding SAP module is available in your system.

**SAP Bill of Materials**

Manage bill of materials data, including component lists, quantities, and manufacturing specifications.

**Required scope:** `ZAPI_BILL_OF_MATERIAL_SRV_0002`

**SAP Business Partner**

Handle business partner information, including customer and vendor data, contact details, and relationship management.

**Required scope:** `ZAPI_BUSINESS_PARTNER_0001`

**SAP Material Stock**

Access and manage material stock levels, inventory movements, and warehouse information.

**Required scope:** `ZAPI_MATERIAL_STOCK_SRV_0001`

**SAP Physical Inventory Documents**

Create and manage physical inventory documents, stock counts, and inventory reconciliation processes.

**Required scope:** `ZAPI_MATERIAL_STOCK_SRV_0001`

**SAP Product Master**

Maintain product master data, including material specifications, classifications, and product hierarchies.

**Required scope:** `ZAPI_PRODUCT_SRV_0001`

### SAP workload authentication setup

Prepare SAP user authentication credentials and ensure proper system access permissions.

- **SAP system URL** - Obtain the base URL or server address for your SAP system.
- **User credentials** - Create or identify a SAP user account with appropriate permissions.
- **System permissions** - Ensure the user account has the necessary SAP authorizations and transaction codes for the specific SAP modules you plan to integrate.
- **Network access** - Verify that your SAP system is accessible from external connections and that firewall rules allow the integration.

## Set up SAP integrations

After preparing your SAP system configuration and authentication credentials, the setup process is similar for all SAP integration types. Choose between OAuth 2.0 or Basic Authentication based on your security requirements.

1.  In the Amazon Quick Suite console, choose **Integrations**.
2.  Select one of the available SAP connectors:
    - **SAP Bill of Materials**
    - **SAP Business Partner**
    - **SAP Material Stock**
    - **SAP Physical Inventory Documents**
    - **SAP Product Master**

3.  Click **Add** (plus "+" button).
4.  Fill in the name and description for your SAP integration.
5.  Choose the connection type for your integration.
6.  Configure authentication using one of the supported methods:
    1. **OAuth 2.0 configuration**

    For OAuth 2.0 authentication, provide:

        * **Client ID** - Your SAP OAuth Client ID
        * **Client Secret** - Your SAP OAuth Client Secret
        * **Token URL** - OAuth token endpoint URL
        * **Domain URL** - SAP system API endpoint URL

    2. **Basic Authentication configuration**

    For Basic Authentication, provide:

        * **Username** - Your SAP system username
        * **Password** - Your SAP system password
        * **Domain URL** - SAP system API endpoint URL

7.  Select **Create and continue**.
8.  Choose users to share the integration with.
9.  Click **Next**.

### Expected results

After successful setup, your SAP workload integration appears in the integrations
list and is available for use in Amazon Quick Suite workflows, automations, and AI agents.
You can perform SAP-specific actions directly from Amazon Quick Suite using the configured
authentication credentials.

## Available operations by connector type

Each SAP workload connector provides specific operations tailored to its business
domain. Review the available operations for your chosen connector type.

### SAP Bill of Materials operations

Available operations for managing bill of materials data:

- **Get Material BOM Item** - Retrieves bill of material details for specified materials

**Operation ID:** `getMaterialBOMItem`

**Endpoint:** `GET /MaterialBOMItem`

### SAP Business Partner operations

Available operations for managing business partner data:

- **Get Business Partner** - Retrieves business partner general data

**Operation ID:** `getBusinessPartner`

- **Get Business Partner Addresses** - Retrieves business partner address data

**Operation ID:** `getBusinessPartnerAddress`

- **Get Business Partner Roles** - Retrieves business partner role data

**Operation ID:** `getBusinessPartnerRole`

- **Get Business Partner by ID** - Retrieves business partner data by business partner number

**Operation ID:** `getBusinessPartnerByID`

**Required parameter:** `BusinessPartner` (string, max 10 characters)

- **Get Business Partner Role by ID** - Retrieves business partner role data using key fields

**Operation ID:** `getBusinessPartnerRoleByID`

**Required parameters:** `BusinessPartner` (string, max 10 characters), `BusinessPartnerRole` (string, max 6 characters)

### SAP Material Stock operations

Available operations for managing material stock data:

- **Get Material Stock In Account** - Retrieves material stock information posted in the account model

**Operation ID:** `getMaterialStockInAccount`

### SAP Physical Inventory Documents operations

Available operations for managing physical inventory documents:

- **Get PhysInventory Doc Item** - Reads information on physical inventory items

**Operation ID:** `getPhysInventoryDocItem`

### SAP Product Master operations

Available operations for managing product master data:

- **Get Product Master Item** - Returns product master records

**Operation ID:** `getProductMaster`

- **Get Plant Data By Material** - Returns plant data of product master record

**Operation ID:** `getPlantDataByMaterial`

**Required parameter:** `Product` (string, max 40 characters)

- **Get Supply Planning Data By Material** - Returns supply planning data by product number and plant

**Operation ID:** `getSupplyPlanningDataByMaterial`

**Required parameters:** `Product` (string, max 40 characters), `Plant` (string, max 4 characters)

## Query parameters

SAP connectors support standard query parameters to filter, sort, and format API
responses. Use these parameters to optimize data retrieval and processing.

| Supported Query Parameters | #              | Parameter                                   | Description | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------- | -------------- | ------------------------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1                          | `$top`         | Limits the number of returned items         | integer     |
| 2                          | `$skip`        | Skips the specified number of items         | integer     |
| 3                          | `$filter`      | Filters results based on specified criteria | string      |
| 4                          | `$orderby`     | Orders results by specified fields          | array       |
| 5                          | `$select`      | Selects specific properties to return       | array       |
| 6                          | `$expand`      | Expands related entities                    | array       |
| 7                          | `$inlinecount` | Includes count of items in response         | string      | ## Manage SAP workload integrations After you create your SAP workload integration, you can manage it through several options. ### Edit integration settings Follow these steps to modify your SAP workload integration settings. 1. In the Amazon Quick Suite console, choose **Integrations**. 2. Choose your SAP workload integration type from the integration grid. 3. Select your integration from the list and choose **Edit**. 4. Modify integration settings: <br>• Update authentication credentials (username and password). <br>• Change SAP system URL or connection settings. <br>• Modify integration name or description. 5. Choose **Save changes** to apply your modifications. ### Share integration You can share SAP workload action connectors with other users in your organization. 1. From the SAP integration details page, choose **Share**. 2. Configure sharing options: <br>• **Share with specific users** - Enter user names or email addresses. <br>• **Share with organization** - Make available to all users in your organization. 3. Set permission levels for shared access. 4. Choose **Share integration** to apply the sharing settings. ### Delete integration Follow these steps to permanently remove your SAP integration. 1. From the SAP workload integration details page, choose **Delete**. 2. Review the deletion impact, including any workflows or automations using this integration. 3. Type the integration name to confirm deletion. 4. Choose **Delete integration** to permanently remove it. ## Troubleshoot SAP workload integrations Use these troubleshooting tips to resolve common SAP workload integration issues. ### Authentication issues OAuth 2.0 authentication failures **Symptoms:** Token generation fails, invalid client credentials, or OAuth scope errors. **Resolution:** <br>• Verify OAuth client ID and client secret are correct <br>• Check that OAuth is properly configured in SAP using transaction `/IWFND/MAINT_SERVICE` <br>• Ensure the required scopes are properly configured for your SAP workload connector type <br>• Verify the token URL format matches your SAP system configuration Basic authentication failures **Symptoms:** Login failures, invalid credentials, or access denied errors. **Resolution:** <br>• Verify SAP username and password are correct <br>• Check that the user account has necessary SAP authorizations <br>• Ensure the user account is not locked or expired <br>• Verify the domain URL is accessible and correctly formatted ### SAP system configuration issues API service not activated **Symptoms:** Service unavailable errors, API endpoint not found, or HTTP 404 responses. **Resolution:** <br>• Verify the required SAP API service is activated in your system <br>• Check API service status using SAP transaction codes <br>• Ensure the API service corresponds to your chosen SAP connector type <br>• Contact your SAP administrator to activate missing API services Connection timeouts **Symptoms:** Request timeouts, network connectivity errors, or slow response times. **Resolution:** <br>• Check that your SAP system URL is correct and accessible <br>• Verify network connectivity allows connections to SAP system <br>• Ensure firewall rules permit the integration traffic <br>• Check SAP system performance and availability ### Permission and authorization errors Insufficient SAP authorizations **Symptoms:** Access denied errors, missing authorization messages, or restricted operation failures. **Resolution:** <br>• Ensure the authenticated user has required SAP authorizations for the specific module <br>• Verify the user has access to necessary transaction codes <br>• Check that the user account has appropriate role assignments <br>• Contact your SAP administrator to grant missing permissions Scope permission errors **Symptoms:** OAuth scope errors, insufficient permissions for API operations, or restricted access messages. **Resolution:** <br>• Verify the OAuth configuration includes the required scope for your connector type <br>• Check that the scope permissions are properly granted in SAP system <br>• Ensure the OAuth client has been granted the necessary API access rights ### Data format and parameter errors Invalid parameter formats **Symptoms:** Data validation errors, invalid field length messages, or parameter format exceptions. **Resolution:** <br>• Review action parameters and ensure they match expected SAP data formats <br>• Check field lengths match SAP system requirements (e.g., BusinessPartner max 10 characters) <br>• Verify data types are correct for the specific SAP module <br>• Ensure all required fields are provided for the operation Query parameter errors **Symptoms:** Query syntax errors, unsupported parameter messages, or malformed request errors. **Resolution:** <br>• Verify parameters use correct syntax (e.g., `$filter`, `$top`, `$skip`) <br>• Check that the parameter values are properly formatted <br>• Ensure the SAP API supports the specific parameters being used <br>• Refer to SAP API documentation for supported query options ### SAP system availability issues SAP system unavailability **Symptoms:** Connection refused errors, system not responding, or service unavailable messages. **Resolution:** <br>• Check SAP system status and availability with your SAP administrator <br>• Verify if there are scheduled maintenance windows affecting the system <br>• Check for any SAP system alerts or known issues <br>• Retry the operation after confirming system availability |
