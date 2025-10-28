# Adding a custom source in Security Lake

After creating the IAM role to invoke the AWS Glue crawler, follow these steps to add a
custom source in Security Lake.

Console

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/ "https://console.aws.amazon.com/securitylake/").
2. By using the AWS Region selector in the upper-right corner of
   the page, select the Region where you want to create the custom
   source.
3. Choose **Custom sources** in the navigation pane,
   and then choose **Create custom source**.
4. In the **Custom source details** section, enter a
   globally unique name for your custom source. Then, select an OCSF
   event class that describes the type of data that the custom source
   will send to Security Lake.
5. For **AWS account with permission to write
   data**, enter the **AWS account ID**
   and **External ID** of the custom source that will
   write logs and events to the data lake.
6. For **Service Access**, create and use a new
   service role or use an existing service role that gives Security Lake
   permission to invoke AWS Glue.
7. Choose **Create**.

API
To add a custom source programmatically, use the [CreateCustomLogSource](../APIReference/API_CreateCustomLogSource.md "../APIReference/API_CreateCustomLogSource.md") operation of the Security Lake API. Use the
operation in the AWS Region where you want to create the custom
source. If you're using the AWS Command Line Interface (AWS CLI), run the [create-custom-log-source](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-custom-log-source.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-custom-log-source.html") command.

In your request, use the supported parameters to specify configuration
settings for the custom source:

- `sourceName` – Specify a name for the source. The name
  must be a Regionally unique value.
- `eventClasses` – Specify one or more OCSF event
  classes to describe the type of data that the source will send to
  Security Lake. For a list of OCSF event classes supported as source in Security Lake,
  see [Open Cybersecurity Schema Framework (OCSF)](https://schema.ocsf.io/classes?extensions "https://schema.ocsf.io/classes?extensions").
- `sourceVersion` – Optionally, specify a value to
  limit log collection to a specific version of custom source
  data.
- `crawlerConfiguration` – Specify the Amazon Resource
  Name (ARN) of the IAM role that you created to invoke the AWS Glue
  crawler. For the detailed steps to create an IAM role, see [Prerequisites to adding a custom source](custom-sources.md#iam-roles-glue-crawler "custom-sources.md#iam-roles-glue-crawler")
- `providerIdentity` – Specify the AWS identity and
  external ID that the source will use to write logs and events to the
  data lake.

The following example adds a custom source as a log source in the
designated log provider account in designated Regions. This example is formatted for
Linux, macOS, or Unix, and it uses the backslash (\) line-continuation
character to improve readability.

```
`$` `aws securitylake create-custom-log-source \
--source-name `EXAMPLE_CUSTOM_SOURCE` \
--event-classes '[`"DNS_ACTIVITY", "NETWORK_ACTIVITY"`]' \
--configuration crawlerConfiguration=`{"roleArn=arn:aws:iam::XXX:role/service-role/RoleName"}`,providerIdentity=`{"externalId=ExternalId,principal=principal"}`  \
--region=`[“ap-southeast-2”]``
```

## Keeping custom source data updated in AWS Glue

After you add a custom source in Security Lake, Security Lake creates an AWS Glue crawler. The crawler connects to your
custom source, determines the data structures, and populates the
AWS Glue Data Catalog with tables.

We recommend manually running the crawler to keep your custom source schema up to date and maintain query
functionality in Athena and other querying services. Specifically, you should run the crawler if either of the following changes
occur in your input data set for a custom source:

- The data set has one or more new top-level columns.
- The data set has one or more new fields in a column with a `struct` datatype.

For instructions on running a crawler, see [Scheduling an AWS Glue crawler](../../../glue/latest/dg/schedule-crawler.md "../../../glue/latest/dg/schedule-crawler.md") in the _AWS Glue Developer Guide_.

Security Lake can't delete or update existing crawlers in your account. If you delete a custom source, we recommend
deleting the associated crawler if you plan to create a custom source with the same name in the future.

## Supported OCSF event classes

The Open Cybersecurity Schema Framework (OCSF) event classes describes the type of
data that the custom source will send to Security Lake. The list of supported event classes are:

```
public enum OcsfEventClass {
    ACCOUNT_CHANGE,
    API_ACTIVITY,
    APPLICATION_LIFECYCLE,
    AUTHENTICATION,
    AUTHORIZE_SESSION,
    COMPLIANCE_FINDING,
    DATASTORE_ACTIVITY,
    DEVICE_CONFIG_STATE,
    DEVICE_CONFIG_STATE_CHANGE,
    DEVICE_INVENTORY_INFO,
    DHCP_ACTIVITY,
    DNS_ACTIVITY,
    DETECTION_FINDING,
    EMAIL_ACTIVITY,
    EMAIL_FILE_ACTIVITY,
    EMAIL_URL_ACTIVITY,
    ENTITY_MANAGEMENT,
    FILE_HOSTING_ACTIVITY,
    FILE_SYSTEM_ACTIVITY,
    FTP_ACTIVITY,
    GROUP_MANAGEMENT,
    HTTP_ACTIVITY,
    INCIDENT_FINDING,
    KERNEL_ACTIVITY,
    KERNEL_EXTENSION,
    MEMORY_ACTIVITY,
    MODULE_ACTIVITY,
    NETWORK_ACTIVITY,
    NETWORK_FILE_ACTIVITY,
    NTP_ACTIVITY,
    PATCH_STATE,
    PROCESS_ACTIVITY,
    RDP_ACTIVITY,
    REGISTRY_KEY_ACTIVITY,
    REGISTRY_VALUE_ACTIVITY,
    SCHEDULED_JOB_ACTIVITY,
    SCAN_ACTIVITY,
    SECURITY_FINDING,
    SMB_ACTIVITY,
    SSH_ACTIVITY,
    USER_ACCESS,
    USER_INVENTORY,
    VULNERABILITY_FINDING,
    WEB_RESOURCE_ACCESS_ACTIVITY,
    WEB_RESOURCES_ACTIVITY,
    WINDOWS_RESOURCE_ACTIVITY,
    // 1.3 OCSF event classes
    ADMIN_GROUP_QUERY,
    DATA_SECURITY_FINDING,
    EVENT_LOG_ACTIVITY,
    FILE_QUERY,
    FILE_REMEDIATION_ACTIVITY,
    FOLDER_QUERY,
    JOB_QUERY,
    KERNEL_OBJECT_QUERY,
    MODULE_QUERY,
    NETWORK_CONNECTION_QUERY,
    NETWORK_REMEDIATION_ACTIVITY,
    NETWORKS_QUERY,
    PERIPHERAL_DEVICE_QUERY,
    PROCESS_QUERY,
    PROCESS_REMEDIATION_ACTIVITY,
    REMEDIATION_ACTIVITY,
    SERVICE_QUERY,
    SOFTWARE_INVENTORY_INFO,
    TUNNEL_ACTIVITY,
    USER_QUERY,
    USER_SESSION_QUERY,
    // 1.3 OCSF event classes (Win extension)
    PREFETCH_QUERY,
    REGISTRY_KEY_QUERY,
    REGISTRY_VALUE_QUERY,
    WINDOWS_SERVICE_ACTIVITY
}
```
