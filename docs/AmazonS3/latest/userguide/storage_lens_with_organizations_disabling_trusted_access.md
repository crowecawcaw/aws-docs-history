# Disabling trusted access for S3 Storage Lens

Removing an account as a delegated administrator or disabling trusted access limits the
account owner's S3 Storage Lens dashboard metrics to work only on an account level. Each account holder
is then only be able to see the benefits of S3 Storage Lens through the limited scope of their account,
and not their entire organization.

When you disable trusted access in S3 Storage Lens, any dashboards
requiring trusted access are no longer updated. Any organizational dashboards that
are created are also no longer updated. Instead, you're only able to query [historic data for the S3 Storage Lens dashboard](storage_lens_basics_metrics_recommendations.md#storage_lens_basics_data_queries "storage_lens_basics_metrics_recommendations.md#storage_lens_basics_data_queries"), while the data is still available.

###### Note

- Disabling trusted access for S3 Storage Lens also automatically stops all organization-level
  dashboards from collecting and aggregating storage metrics. This is because S3 Storage Lens no
  longer has trusted access to the organization accounts.
- Your management and delegate administrator accounts can still see the historic data
  for any disabled dashboards. They can also query this historic data while it is still
  available.

###### To disable trusted access for S3 Storage Lens

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. On the left navigation pane, navigate to **Storage Lens**.
3. Choose **AWS Organizations settings**. The **AWS Organizations access for Storage Lens** page displays.
4. Under **AWS Organizations trusted access**, choose
   **Edit**.

The **AWS Organizations access** page displays. 5. Choose **Disable** to disable trusted access for your S3 Storage Lens dashboard. 6. Choose **Save changes**.

###### Example

The following example disables trusted access for S3 Storage Lens using the AWS CLI.

```
aws organizations disable-aws-service-access --service-principal storage-lens.s3.amazonaws.com
```

###### Example– Disable AWS Organizations trusted access for S3 Storage Lens

The following example shows you how to disable AWS Organizations trusted access for S3 Storage Lens in SDK for Java.
To use this example, replace the `user input
 placeholders` with your own information.

```
import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.organizations.AWSOrganizations;
import com.amazonaws.services.organizations.AWSOrganizationsClient;
import com.amazonaws.services.organizations.model.DisableAWSServiceAccessRequest;

public class DisableOrganizationsTrustedAccess {
	private static final String S3_STORAGE_LENS_SERVICE_PRINCIPAL = "storage-lens.s3.amazonaws.com";

	public static void main(String[] args) {
		try {
            AWSOrganizations organizationsClient = AWSOrganizationsClient.builder()
                .withCredentials(new ProfileCredentialsProvider())
                .withRegion(Regions.`US_EAST_1`)
                .build();

            // Make sure to remove any existing delegated administrator for S3 Storage Lens
            // before disabling access; otherwise, the request will fail.
            organizationsClient.disableAWSServiceAccess(new DisableAWSServiceAccessRequest()
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
