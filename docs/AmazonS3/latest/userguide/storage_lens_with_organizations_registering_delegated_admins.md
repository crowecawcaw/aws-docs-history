# Registering a delegated administrator for S3 Storage Lens

You can create organization-level dashboards by using your organization’s management
account or delegated administrator accounts. Delegated administrator accounts allow other
accounts besides your management account to create organization-level dashboards. Only the
management account of an organization can register and deregister other accounts as
delegated administrators for the organization.

After enabling trusted access, you can register delegate administrator access to
accounts in your organization by using the AWS Organizations REST API, AWS CLI,
or SDKs from the [management account](../../../managedservices/latest/userguide/management-account.md "../../../managedservices/latest/userguide/management-account.md"). (For more information, see [RegisterDelegatedAdministrator](../../../organizations/latest/APIReference/API_RegisterDelegatedAdministrator.md "../../../organizations/latest/APIReference/API_RegisterDelegatedAdministrator.md") in the
_AWS Organizations API Reference_.) When an account is registered as a delegated administrator,
the account receives authorization to access all read-only AWS Organizations API operations. This
provides visibility to the members and structures of your organization so that they can
create S3 Storage Lens dashboards on your behalf.

###### Note

Before you can designate a delegated administrator by using the AWS Organizations REST API, AWS CLI,
or SDKs, you must call the [EnableAWSServiceAccess](../../../organizations/latest/APIReference/API_EnableAWSServiceAccess.md "../../../organizations/latest/APIReference/API_EnableAWSServiceAccess.md") operation.

###### To register delegated administrators for S3 Storage Lens

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. On the left navigation pane, navigate to **Storage Lens**.
3. Choose **AWS Organizations settings**.
4. Under **Delegated administrators**, choose **Register account**.
5. Add an AWS account ID to register the account as a delegated administrator. The
   delegated administrator is able to create organization-level dashboards for all accounts
   and storage in your organization.
6. Choose **Register account**.

###### Example

The following example shows you how to register Organizations delegated administrators for S3 Storage Lens using the AWS CLI.
To use this example, replace the `user input
 placeholders` with your own information.

```
aws organizations register-delegated-administrator --service-principal storage-lens.s3.amazonaws.com --account-id `111122223333`
```

###### Example– Register Organizations delegated administrators for S3 Storage Lens

The following example shows you how to register AWS Organizations delegated administrators for S3 Storage Lens in SDK for Java.
To use this example, replace the `user input
 placeholders` with your own information.

```
import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.organizations.AWSOrganizations;
import com.amazonaws.services.organizations.AWSOrganizationsClient;
import com.amazonaws.services.organizations.model.RegisterDelegatedAdministratorRequest;

public class RegisterOrganizationsDelegatedAdministrator {
	private static final String S3_STORAGE_LENS_SERVICE_PRINCIPAL = "storage-lens.s3.amazonaws.com";

	public static void main(String[] args) {
		try {
            String delegatedAdminAccountId = "`111122223333`"; // Account Id for the delegated administrator.
            AWSOrganizations organizationsClient = AWSOrganizationsClient.builder()
                .withCredentials(new ProfileCredentialsProvider())
                .withRegion(Regions.`US_EAST_1`)
                .build();

            organizationsClient.registerDelegatedAdministrator(new RegisterDelegatedAdministratorRequest()
                .withAccountId(delegatedAdminAccountId)
                .withServicePrincipal(S3_STORAGE_LENS_SERVICE_PRINCIPAL));
        } catch (AmazonServiceException e) {
            // The call was transmitted successfully, but AWS Organizations couldn't process
            // it and returned an error response.
            e.printStackTrace();
        } catch (SdkClientException e) {
            // AWS Organizations couldn't be contacted for a response, or the client
            // couldn't parse the response from AWS Organizations.
            e.printStackTrace();
        }
	}
}
```
