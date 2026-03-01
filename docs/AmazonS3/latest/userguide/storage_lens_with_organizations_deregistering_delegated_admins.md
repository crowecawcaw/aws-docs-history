# Deregistering a delegated administrator for S3 Storage Lens

After enabling trusted access, you can also deregister delegate administrator access to
accounts in your organization. Delegated administrator accounts allow other accounts besides
your [management account](../../../managedservices/latest/userguide/management-account.md "../../../managedservices/latest/userguide/management-account.md") to create organization-level dashboards. Only the management
account of an organization can deregister accounts as delegated administrators for the
organization.

You can deregister a delegated administrator by using the AWS Organizations AWS Management Console, REST API,
AWS CLI, or AWS SDKS from the management account. For more information, see [DeregisterDelegatedAdministrator](../../../organizations/latest/APIReference/API_DeregisterDelegatedAdministrator.md "../../../organizations/latest/APIReference/API_DeregisterDelegatedAdministrator.md") in the _AWS Organizations API
Reference_.

When an account is deregistered as a delegated administrator, the account loses access to
the following:

- All read-only AWS Organizations API operations that provide visibility to the members and
  structures of your organization.
- All organization-level dashboards created by the delegated administrator. Deregistering
  a delegated administrator also automatically stops all organization-level dashboards created
  by that delegated administrator from aggregating new storage metrics.

###### Note

The deregistered delegated administrator will still be able to see the historic data
for the disabled dashboards that they created if data is still available for
querying.

###### To deregister delegated administrators for S3 Storage Lens

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. On the left navigation pane, navigate to **Storage Lens**.
3. Choose **AWS Organizations settings**.
4. Under **Delegated administrators**, choose the account that you
   wish to deregister.
5. Choose **De-register account**. The deregistered account is no
   longer a delegated administrator and is now unable to create organization-level
   dashboards for all accounts and storage in your organization.
6. Choose **Register account**.

###### Example

The following example shows you how to deregister Organizations delegated administrators for
S3 Storage Lens using the AWS CLI. To use this example, replace
`111122223333` with your own
AWS account ID.

```
aws organizations deregister-delegated-administrator --service-principal storage-lens.s3.amazonaws.com --account-id `111122223333`
```

###### Example– Deregister Organizations delegated administrators for S3 Storage Lens

The following example shows you how to deregister Organizations delegated administrators for
S3 Storage Lens using SDK for Java. To use this example, replace the `user input
 placeholders` with your own information.

```
import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.organizations.AWSOrganizations;
import com.amazonaws.services.organizations.AWSOrganizationsClient;
import com.amazonaws.services.organizations.model.DeregisterDelegatedAdministratorRequest;

public class DeregisterOrganizationsDelegatedAdministrator {
	private static final String S3_STORAGE_LENS_SERVICE_PRINCIPAL = "storage-lens.s3.amazonaws.com";

	public static void main(String[] args) {
		try {
            String delegatedAdminAccountId = "`111122223333`"; // Account Id for the delegated administrator.
            AWSOrganizations organizationsClient = AWSOrganizationsClient.builder()
                .withCredentials(new ProfileCredentialsProvider())
                .withRegion(Regions.`US_EAST_1`)
                .build();

            organizationsClient.deregisterDelegatedAdministrator(new DeregisterDelegatedAdministratorRequest()
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
