

# Configure IBM Security® Verify for AppFabric
<a name="ibm-security"></a>

The IBM Security® Verify family provides automated, cloud-based and on-premises capabilities for administering identity governance, managing workforce and consumer identity and access, and controlling privileged accounts. Whether you need to deploy a cloud or on-premises solution, IBM Security® Verify helps you establish trust and protect against insider threats to both your [workforce](https://www.ibm.com/products/verify-identity/workforce-iam) and [consumers](https://www.ibm.com/products/verify-identity/ciam).

You can use AWS AppFabric for security to receive audit logs and user data from IBM Security® Verify, normalize the data into Open Cybersecurity Schema Framework (OCSF) format, and output the data to an Amazon Simple Storage Service (Amazon S3) bucket or an Amazon Data Firehose stream.

**Topics**
+ [AppFabric support for the IBM Security® Verify](#ibm-security-appfabric-support)
+ [Connecting AppFabric to your IBM Security® Verify account](#ibm-security-appfabric-connecting)

## AppFabric support for the IBM Security® Verify
<a name="ibm-security-appfabric-support"></a>

AppFabric supports receiving user information and audit logs from IBM Security® Verify.

### Prerequisites
<a name="ibm-security-prerequisites"></a>

To use AppFabric to transfer audit logs from IBM Security® Verify to supported destinations, you must meet the following requirements:
+ To access the audit logs, you need to have an [IBM Security® Verify SaaS account](https://www.ibm.com/products/verify-identity).
+ To access the audit logs, you need to have an administrator role in your IBM Security® Verify SaaS account.

### Rate limit considerations
<a name="ibm-security-rate-limits"></a>

IBM Security® Verify imposes rate limits on the IBM Security® Verify API. For more information about the IBM Security® Verify API rate limits, see [IBM Terms](https://www.ibm.com/support/customer/csol/terms/?id=i126-7765&lc=en). If the combination of AppFabric and your existing IBM Security® Verify API applications exceed IBM Security® Verify limits, audit logs appearing in AppFabric might be delayed.

### Data delay considerations
<a name="ibm-security-data-delay"></a>

You may see up to 30-minute delay in an audit event to get delivered to your destination. This is due to delay in audit events made available by the application as well as due to precautions taken to reduce data loss. However, this may be customizable on an account level. For assistance, contact [Support](https://aws.amazon.com/contact-us/).

## Connecting AppFabric to your IBM Security® Verify account
<a name="ibm-security-appfabric-connecting"></a>

After you create your app bundle within the AppFabric service, you must authorize AppFabric with IBM Security® Verify. To find the information required to authorize IBM Security® Verify with AppFabric, use the following steps.

### Create an OAuth application
<a name="ibm-security-create-oauth-application"></a>

AppFabric integrates with the IBM Security® Verify using OAuth. To create an OAuth application in IBM Security® Verify, see [Create an API client](https://docs.verify.ibm.com/verify/docs/support-developers-create-api-client) on the *IBM documentation website*.

1. For first-time login, use the login URL and credentials that were sent to your registered email address.

1. Access the administration console at `https://{{<hostname>}}.verify.ibm.com/ui/admin/`. For more information, see [Accessing IBM Security® Verify](https://www.ibm.com/docs/en/security-verify?topic=overview-accessing-security-verify#taskt_login_admin_ui__steps__1).

1. In the administration console, under **Security** < **API Access** < **API Client**, choose **Add**.

1. Select the following options. These are required for reading audit log and user details.
   + Read reports
   + Read users and groups

1. Keep the **Default** option in the **Client Authentication method**.

   Don't edit the **Custom scopes** field.

1. Choose **Next**.

1. Don't edit the **IP filter** field.

1. Choose **Next**.

1. Don't edit the **Additional properties** field.

1. Choose **Next**.

1. Specify a **Name** and **Description**. The description is optional.

1. Choose **Create API client**.

### App authorizations
<a name="ibm-security-app-authorizations"></a>

#### Tenant ID
<a name="ibm-security-tenant-id"></a>

AppFabric will request your tenant ID. You can locate the tenant ID in the IBM Security® Verify standard URL. For instance, in the `https://{{hostname}}.verify.ibm.com/` URL, the tenant ID is the {{hostname}} that can be found before `.verify.ibm.com` (or before `ice.ibmcloud.com` if you are using a former hostname). If you are using a vanity URL, contact your IBM Security® Verify support team to obtain your standard URL.

#### Tenant name
<a name="ibm-security-tenant-name"></a>

Enter a name that identifies this unique IBM Security® Verify tenant. AppFabric uses the tenant name to label the app authorizations and any ingestion created from the app authorization.

#### Client ID
<a name="ibm-security-client-id"></a>

AppFabric will request a client ID. To find your client ID in IBM Security® Verify, use the following steps:

1. For first-time login, use the login URL and credentials that were sent to your registered email address.

1. Access the administration console at `https://<hostname>.verify.ibm.com/ui/admin/`. For more information, see [Accessing IBM Security® Verify](https://www.ibm.com/docs/en/security-verify?topic=overview-accessing-security-verify#taskt_login_admin_ui__steps__1).

1. In the administration console, under **Security** < **API Access** < **API Client**, choose the ellipsis (⋮) next to the specific OAuth app.

1. Choose **Connection details**.

1. Locate **Client ID** under **API credentials**.

#### Client secret
<a name="ibm-security-client-secret"></a>

AppFabric will request a client secret. To find your client secret in IBM Security® Verify, use the following steps:

1. For first-time login, use the login URL and credentials that were sent to your registered email address.

1. Access the administration console at `https://<hostname>.verify.ibm.com/ui/admin/`. For more information, see [Accessing IBM Security® Verify](https://www.ibm.com/docs/en/security-verify?topic=overview-accessing-security-verify#taskt_login_admin_ui__steps__1).

1. In the administration console, under **Security** < **API Access** < **API Client**, choose the ellipsis (⋮) next to the specific OAuth app.

1. Choose **Connection details**.

1. Locate **Client secret** under **API credentials**.