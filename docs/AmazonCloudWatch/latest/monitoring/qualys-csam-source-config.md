

# Source configuration for Qualys CSAM
<a name="qualys-csam-source-config"></a>

## Supported API and platform versions
<a name="qualys-csam-supported-versions"></a>

The following table lists the supported API and platform versions.


| Component | Version | Notes | 
| --- | --- | --- | 
| Qualys CSAM API | v2.0 | CSAM and Global AssetView (GAV) APIs | 
| OCSF schema | v1.5.0 | Open Cybersecurity Schema Framework mapping | 
| OAuth 2.0 token exchange | Not applicable | Form-urlencoded username and password exchange for a JWT bearer token | 

## Qualys Cloud Platform prerequisites
<a name="qualys-csam-product-prerequisites"></a>

Before you begin, make sure you have the following:
+ An active Qualys subscription with the Qualys CSAM module enabled
+ A Qualys user account with API access permissions to CSAM endpoints
+ Your platform-specific Qualys API Gateway hostname, such as `gateway.qg3.apps.qualys.com`

## Configure Qualys CSAM
<a name="qualys-csam-product-setup"></a>

Use the following procedure to create a Qualys Reader user for the integration.

1. Log in to the Qualys Cloud Platform and identify your Qualys API Gateway hostname.

1. From the module picker, choose **Administration** under **Platform And Sensor Management**.

1. On the Administration page, choose the **Users** tab. From the **Create User** menu, choose **Create Reader User**.

1. On the **General Information** tab, complete all required fields: first name, last name, address, country, state, ZIP code, and email address.

1. Choose **User Role** in the left navigation pane, and then configure the following settings:
   + For **User Role**, choose **Reader**.
   + Under **Allow access to**, select **API**. API access is required for the account to authenticate to the Qualys API.
   + Leave **Business Unit** set to **Unassigned** unless your organization uses business units to segment access.

1. Choose **Asset Groups** in the left navigation pane. Use **Add asset groups** to select the asset groups that the user, and therefore the connector, can access. Select all asset groups to retrieve every asset in the subscription, or select specific groups to limit the scope.

1. Choose **Permissions** in the left navigation pane. The extended permissions to manage the VM module, purge host information or history, and manage the PC module are not required for API read access. Leave them cleared unless your process requires this account to manage those modules.

1. Complete the remaining **Options** and **Security** tabs. Configure options such as IP-based login restrictions only if your organization requires them.

1. Choose **Save** or **Create User**. Qualys sends the new user a temporary password.

1. Log in to the Qualys user interface with the temporary password and complete the required password reset. The credentials do not work with the connector until this first-time password reset is complete.

1. Save the final `username` and `password` for use in the AWS connector configuration.

## Qualys API Gateway hostnames
<a name="qualys-csam-gateway-hostnames"></a>

The following list shows the Qualys API Gateway hostname for each platform.<a name="qualys-csam-gateway-hostnames-list"></a>

US Platform 1  
`gateway.qg1.apps.qualys.com`

US Platform 2  
`gateway.qg2.apps.qualys.com`

US Platform 3  
`gateway.qg3.apps.qualys.com`

US Platform 4  
`gateway.qg4.apps.qualys.com`

EU Platform 1  
`gateway.qg1.apps.qualys.eu`

EU Platform 2  
`gateway.qg2.apps.qualys.eu`

India Platform  
`gateway.qg1.apps.qualys.in`

Canada Platform  
`gateway.qg1.apps.qualys.ca`

UAE Platform  
`gateway.qg1.apps.qualys.ae`

Australia Platform  
`gateway.qg1.apps.qualys.com.au`

## AWS prerequisites
<a name="qualys-csam-aws-prerequisites"></a>

Before you configure the data source, make sure you have the following:
+ An AWS account with permissions to create and manage CloudWatch pipelines. For more information, see [API caller permissions](pipeline-iam-reference.md#api-caller-permissions).
+ An AWS account with permissions to create and update secrets in AWS Secrets Manager, and a source role that can retrieve the stored credentials. For more information, see [Third-party sources (API Pull)](pipeline-iam-reference.md#third-party-api-pull).
+ An AWS account with permissions to create and manage CloudWatch Logs log groups. For more information, see [CloudWatch Logs API operations and required permissions for actions](permissions-reference-cw.md#cwl-permissions-table).
+ The Qualys username and password from the product configuration procedure

## Configure the CloudWatch pipeline resources
<a name="qualys-csam-aws-setup"></a>

1. Store the Qualys credentials in AWS Secrets Manager.
   + Open the AWS Secrets Manager console and choose **Store a new secret**.
   + For the secret type, choose **Other type of secret**.
   + Add a `username` key with your Qualys platform username.
   + Add a `password` key with your Qualys platform password.
   + Name the secret, for example, `qualys-csam-credentials`.

1. Create the destination CloudWatch Logs log group. Use a descriptive name, such as `/aws/cloudwatch/pipelines/qualys-csam`.

1. Create the source IAM role with the required permissions. For information about the required trust and permissions policies, see [CloudWatch pipelines IAM policies and permissions](pipeline-iam-reference.md).

1. Open the CloudWatch console and navigate to **Pipelines**. Choose **Qualys CSAM** as the data source, configure authentication with the Qualys API Gateway hostname, username, and password, and then select the destination log group. For the complete pipeline configuration and parameter reference, see [CloudWatch pipelines configuration for Qualys CSAM](qualys-csam-pipeline-setup.md).

1. Configure the CloudWatch Logs resource policy. The required action depends on how you create the pipeline and whether the log group already exists.
   + When you use the console with a new log group, the resource policy is created automatically.
   + When you use the console with an existing log group that already has a resource policy, the console displays the message *Resource Policy Detected: The log group you selected already has a resource policy. Please verify that this policy includes permissions for pipelines to write to the destination log group. You may need to modify the existing resource policy to add the necessary permissions.* Review and update the existing policy to include the required pipeline write permissions. Add the permissions within five minutes of pipeline creation.
   + When you use the AWS CLI or API, a resource policy is never created automatically. Create the [CloudWatch Logs resource policy](pipeline-iam-reference.md#resource-policies) manually before the pipeline becomes active.

1. Wait a few minutes for the initial data retrieval. Check the destination log group for incoming events and monitor [pipeline metrics](pipelines-metrics.md) for successful ingestion.

## Authentication mechanism
<a name="qualys-csam-authentication"></a>

Qualys CSAM uses OAuth 2.0 token exchange for authentication.

The pipeline sends a form-urlencoded POST request containing the username, password, and `token=true` to the Qualys `/auth` endpoint. The endpoint returns a JSON Web Token (JWT) that the connector sends as a bearer token with subsequent API calls.

The token remains valid for four hours, and the connector automatically renews it before expiration. The connector retrieves credentials securely from AWS Secrets Manager at runtime.

## Supported Open Cybersecurity Schema Framework event classes
<a name="qualys-csam-ocsf-support"></a>

This integration supports OCSF schema version v1.5.0 and maps Qualys CSAM events to the following OCSF classes.


| Event type | Application or endpoint ID | OCSF class | Description | 
| --- | --- | --- | --- | 
| [Assets](https://docs.qualys.com/en/csam/api/asset_host_data/get_host_details_of_all_assets.htm) | POST /rest/2.0/search/am/asset | Device Inventory Info (5001) | Discovered hosts and devices with operating system, hardware, network interface, agent, and risk score information | 
| [Software Components](https://docs.qualys.com/en/csam/api/software_component/get_list_of_all_software_components.htm) | POST /rest/2.0/am/asset/component | Software Inventory Info (5020) | Software packages discovered on assets, including name, version, and installation metadata | 
| [Vulnerabilities](https://docs.qualys.com/en/csam/api/vulnerabilities/get_list_easm_discovered_vuln.htm) | POST /rest/2.0/search/am/easm/vulns | Vulnerability Finding (2002) | Vulnerabilities detected on external-facing assets, including CVE, CVSS, and Qualys Vulnerability Score (QVS) information | 
| [Unresolved Domains](https://docs.qualys.com/en/csam/api/domains/get_list_of_unresolved_domains.htm) | POST /rest/2.0/am/domain/list | OSINT Inventory Info (5021) | Unresolved subdomains under monitored domains | 
| [Typosquatted Domains](https://docs.qualys.com/en/csam/api/domains/get_list_of_unresolved_domains.htm) | POST /rest/2.0/am/domain/list?domainType=TYPOSQUATTED\_DOMAINS | OSINT Inventory Info (5021) | Typosquatted domains discovered through permutation analysis that impersonate legitimate domains | 

Events that do not match an OCSF mapping transformation are automatically passed through and sent directly to the configured sink without additional processing.