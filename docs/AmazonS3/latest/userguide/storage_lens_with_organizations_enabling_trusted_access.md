# Enabling trusted access for

S3 Storage Lens

By enabling trusted access, you allow Amazon S3 Storage Lens to access your AWS Organizations
hierarchy, membership, and structure through AWS Organizations API operations. S3 Storage Lens then becomes
a trusted service for your entire organization's structure.

Whenever a dashboard configuration is created, S3 Storage Lens creates service-linked roles in
your organization's management or delegated administrator accounts. The service-linked role
grants S3 Storage Lens permission to perform the following actions:

- Describe organizations
- List accounts
- Verify a list of AWS service access for the organizations
- Get delegated administrators for the organizations
  S3 Storage Lens can then ensure that it has access to collect the cross-account metrics for the
  accounts in your organization. For more information, see [Using service-linked roles for Amazon S3 Storage Lens](using-service-linked-roles.md "using-service-linked-roles.md").

After enabling trusted access, you can assign delegated administrator access to accounts
in your organization. When an account is marked as a delegated administrator for a service,
the account receives authorization to access all read-only organization API operations. This
access provides the delegated administrator visibility to the members and structures of your
organization so that they too can create S3 Storage Lens dashboards.

###### Note

- Trusted access can only be enabled by the [management
  account](../../../managedservices/latest/userguide/management-account.md "../../../managedservices/latest/userguide/management-account.md").
- Only the management account and delegated administrators can create S3 Storage Lens
  dashboards or configurations for your organization.

###### To enable S3 Storage Lens to have AWS Organizations trusted access

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. On the left navigation pane, navigate to **Storage Lens**.
3. Choose **AWS Organizations settings**. The **AWS Organizations access for Storage Lens** page displays.
4. Under **AWS Organizations trusted access**, choose
   **Edit**.

The **AWS Organizations access** page displays. 5. Choose **Enable** to enable trusted access for your S3 Storage Lens dashboard. 6. Choose **Save changes**.

###### Example

The following example shows you how to enable AWS Organizations trusted access for S3 Storage Lens in AWS CLI.

```
aws organizations enable-aws-service-access --service-principal storage-lens.s3.amazonaws.com
```

###### Example– Enable AWS Organizations trusted access for S3 Storage Lens using SDK for Java

The following example shows you how to enable trusted access for S3 Storage Lens in SDK for Java.
To use this example, replace the `user input
 placeholders` with your own information.

```
import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.organizations.AWSOrganizations;
import com.amazonaws.services.organizations.AWSOrganizationsClient;
import com.amazonaws.services.organizations.model.EnableAWSServiceAccessRequest;

public class EnableOrganizationsTrustedAccess {
	private static final String S3_STORAGE_LENS_SERVICE_PRINCIPAL = "storage-lens.s3.amazonaws.com";

	public static void main(String[] args) {
		try {
            AWSOrganizations organizationsClient = AWSOrganizationsClient.builder()
                .withCredentials(new ProfileCredentialsProvider())
                .withRegion(Regions.`US_EAST_1`)
                .build();

            organizationsClient.enableAWSServiceAccess(new EnableAWSServiceAccessRequest()
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
