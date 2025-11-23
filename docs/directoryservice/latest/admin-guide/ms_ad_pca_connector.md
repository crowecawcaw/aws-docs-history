# Set up AWS Private CA Connector for AD for AWS Managed Microsoft AD

You can integrate your AWS Managed Microsoft AD with [AWS Private Certificate Authority (CA)](../../../privateca/latest/userguide/connector-for-ad.md "../../../privateca/latest/userguide/connector-for-ad.md") to issue
and manage certificates for your Active Directory domain controllers, domain joined users, groups, and
machines. AWS Private CA Connector for Active Directory allows you to use a fully managed AWS Private CA drop-in
replacement for your self-managed enterprise CAs without the need to deploy, patch, or
update local agents or proxy servers.

You can set up AWS Private CA integration with your directory through the Directory Service console, the AWS Private CA
Connector for Active Directory console, or by calling the [`CreateTemplate`](../../../pca-connector-ad/latest/APIReference/API_CreateTemplate.md "../../../pca-connector-ad/latest/APIReference/API_CreateTemplate.md") API. To set up the Private CA integration
through the AWS Private CA Connector for Active Directory console, see [Creating a
connector template](../../../privateca/latest/userguide/create-ad-template.md "../../../privateca/latest/userguide/create-ad-template.md"). See the following steps on how to set up this integration
from the Directory Service console.

## Setting up AWS Private CA Connector for AD

###### To create a Private CA connector for Active Directory

1. Sign in to the AWS Management Console and open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/").
2. On the **Directories** page, choose your directory ID.
3. Under the **Application Management** tab and **AWS apps & services** section, choose **AWS Private CA Connector for AD**.
4. On the **Create Private CA certificate for Active Directory** page, complete the steps to create your Private CA for Active Directory connector.

For more information, see [Creating a connector](../../../privateca/latest/userguide/create-connector-for-ad.md "../../../privateca/latest/userguide/create-connector-for-ad.md").

## Viewing AWS Private CA Connector for AD

###### To view Private CA connector details

1.  Sign in to the AWS Management Console and open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/").
2.  On the **Directories** page, choose your directory ID.
3.  Under the **Application Management** tab and **AWS apps & services** section, view your Private CA connectors and associated Private CA. The following fields display:
    1.  **AWS Private CA Connector ID** – The unique identifier for a AWS Private CA connector. Choose it to view the details page.
    2.  **AWS Private CA subject** – Information regarding the distinguished name for the CA. Choose it to view the details page.
    3.  **Status** – Status check results for the AWS Private CA Connector and AWS Private CA:

            * **Active** – Both checks pass
            * **1/2 checks failed** – One check fails
            * **Failed** – Both checks fail

        For failed status details, hover over the hyperlink to see which check failed.

    4.  **DC Certificates Enrollment status** – Status check for domain controller certificate status:
        - **Enabled** – Certificate enrollment is enabled
        - **Disabled** – Certificate enrollment is disabled

    5.  **Date created** – When the AWS Private CA Connector was created.

For more information, see [View connector details](../../../privateca/latest/userguide/view-connector-for-ad.md "../../../privateca/latest/userguide/view-connector-for-ad.md").

The following table shows the different statuses for domain controller certificate
enrollment for AWS Managed Microsoft AD with AWS Private CA.

| DC enrollment status | Description                                                                                         | Action required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| -------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Enabled              | Domain controller certificates are successfully enrolled to your<br>directory.                      | No action required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Failed               | Domain controller certificate enrollment enablement or disablement<br>failed for your directory.    | If your enablement action fails, retry by turning off domain<br>controller certificates and then turning on again. If your<br>disablement action fails, retry by turning on domain controller<br>certificates and then turning off again. If retry fails, contact<br>AWS Support.                                                                                                                                                                                                                                                                             |
| Impaired             | Domain controllers have network connectivity issues communicating<br>with AWS Private CA endpoints. | Check AWS Private CA VPC endpoint and S3 bucket policies to allow network<br>connectivity with your directory. For more information, see [Troubleshoot AWS Private Certificate Authority exception<br>messages](../../../privateca/latest/userguide/PCATsExceptions.md "../../../privateca/latest/userguide/PCATsExceptions.md") and [Troubleshoot AWS Private CA certificate revocation<br>issues](../../../privateca/latest/userguide/troubleshoot-certificate-revocation.md "../../../privateca/latest/userguide/troubleshoot-certificate-revocation.md"). |
| Disabled             | Domain controller certificate enrollment is successfully turned<br>off for your directory.          | No action required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Disabling            | Domain controller certificate enrollment disablement is in<br>progress.                             | No action required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Enabling             | Domain controller certificate enrollment enablement is in<br>progress.                              | No action required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## Configuring AD Policies

AWS Private CA Connector for AD must be configured so AWS Managed Microsoft AD domain controllers and
objects can request and receive certificates. Configure your group policy object ([GPO](https://learn.microsoft.com/previous-versions/windows/desktop/policy/group-policy-objects "https://learn.microsoft.com/previous-versions/windows/desktop/policy/group-policy-objects")) so AWS Private CA can issue certificates to AWS Managed Microsoft AD objects.

### Configuring Active Directory policies for

domain controllers

###### Turn on Active Directory policies for domain controllers

1. Open the **Network & Security** tab.
2. Choose **AWS Private CA Connectors**.
3. Choose a connector linked to the AWS Private CA subject that issues domain
   controller certificates to your directory.
4. Choose **Actions**, **Enable domain controller
   certificates**.

###### Important

Configure a valid domain controller template before you turn on domain
controller certificates to avoid delayed updates.

After you turn on domain controller certificate enrollment, your directory's
domain controllers request and receive certificates from
AWS Private CA Connector for AD.

To change your issuing AWS Private CA for domain controller certificates, first connect the
new AWS Private CA to your directory using a new AWS Private CA Connector for AD. Before you turn on
certificate enrollment on the new AWS Private CA, turn off certificate enrollment on the
existing one:

###### Turn off domain controller certificates

1. Open the **Network & Security** tab.
2. Choose **AWS Private CA Connectors**.
3. Choose a connector linked to the AWS Private CA subject that issues domain
   controller certificates to your directory.
4. Choose **Actions**, **Disable domain controller
   certificates**.

### Configuring Active Directory policies for

domain joined users, computers and machines

###### Configure group policy objects

1. Connect to the AWS Managed Microsoft AD admin instance and open [Server Manager](https://learn.microsoft.com/windows-server/administration/server-manager/server-manager "https://learn.microsoft.com/windows-server/administration/server-manager/server-manager") from the **Start** menu.
2. Under **Tools**, choose **Group Policy
   Management**.
3. Under **Forest and Domains**, find your subdomain
   organizational unit (OU) (for example, `corp` is your subdomain
   organizational unit if you followed the procedures outlined in [Creating your AWS Managed Microsoft AD](ms_ad_getting_started.md#ms_ad_getting_started_create_directory "ms_ad_getting_started.md#ms_ad_getting_started_create_directory")) and
   right-click on your subdomain OU. Choose **Create a GPO in this
   domain, and link it here** and enter PCA GPO for the name.
   Choose **OK**.
4. The newly created GPO appears following your subdomain name. Right-click
   on `PCA GPO` and choose **Edit**. If a dialog
   box opens with an alert message stating **`This is a link and that
changes are globally propagated`**, acknowledge the message by
   choosing **OK** to continue. The **Group Policy
   Management Editor** window opens.
5. In the **Group Policy Management Editor** window, go to
   \*\*Computer Configuration > Policies > Windows Settings
   > Security Settings > Public Key Policies\*\* (choose the
   > folder).
6. Under **Object Type**, choose **Certificate
   Services Client - Certificate Enrollment Policy**.
7. In the **Certificate Services Client - Certificate Enrollment
   Policy** window, change **Configuration
   Model** to **Enabled**.
8. Confirm that **Active Directory Enrollment Policy** is selected and
   **Enabled**. Choose **Add**.
9. The **Certificate Enrollment Policy Server** dialog box
   opens. Enter the certificate enrollment policy server endpoint that you
   generated when you created your connector in the **Enter enrollment
   server policy URI** field. Leave the **Authentication
   Type** as **Windows** integrated.
10. Choose **Validate**. After validation succeeds, choose
    **Add**.
11. Return to **Certificate Services Client - Certificate Enrollment
    Policy** dialog box and select the box beside the newly created
    connector to make sure that the connector is the default enrollment policy.
12. Choose **Active Directory Enrollment Policy** and choose
    **Remove**.
13. In the confirmation dialog box, choose **Yes** to delete
    the LDAP-based authentication.
14. Choose **Apply** and then **OK** in the
    **Certificate Services Client - Certificate Enrollment
    Policy** window. Then close the window.
15. Under **Object Type** for the **Public Key
    Policies folder, choose Certificate Services Client -
    Auto-Enrollment.**
16. Change the **Configuration Model** option to
    **Enabled**.
17. Confirm that **Renew expired certificates** and
    **Update Certificates** options are both selected.
    Leave the other settings as they are.
18. Choose **Apply**, then **OK**, and close
    the dialog box.

Next, configure the Public Key Policies for user configuration by repeating steps
6-17 in the **User Configuration > Policies > Windows Settings >
Security Settings > Public Key Policies** section.

After you finish configuring GPOs and Public Key Policies, objects in the domain
request certificates from AWS Private CA Connector for AD and receive certificates issued by
AWS Private CA.

## Confirming AWS Private CA issued a

certificate

The process to update AWS Private CA to issue certificates for your AWS Managed Microsoft AD can take up to
8 hours.

You can do one of the following:

- You can wait this period of time.
- You can restart the AWS Managed Microsoft AD domain joined machines that were configured
  to receive certificates from the AWS Private CA. Then you can confirm the AWS Private CA has
  issued certificates to members of your AWS Managed Microsoft AD domain by following the
  procedure in [Microsoft documentation](https://learn.microsoft.com/dotnet/framework/wcf/feature-details/how-to-view-certificates-with-the-mmc-snap-in "https://learn.microsoft.com/dotnet/framework/wcf/feature-details/how-to-view-certificates-with-the-mmc-snap-in").
- You can use the following PowerShell command to update the
  certificates for your AWS Managed Microsoft AD:

```
certutil -pulse
```
