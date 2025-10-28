# Listing all Storage Lens groups

The following examples demonstrate how to list all Amazon S3 Storage Lens groups in an
AWS account and home Region. These examples show how list all Storage Lens groups by using
the Amazon S3 console, AWS Command Line Interface (AWS CLI), and AWS SDK for Java.

###### To list all Storage Lens groups in an account and home Region

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Storage Lens
   groups**.
3. Under **Storage Lens groups**, the list of Storage Lens
   groups in your account is displayed.
   The following AWS CLI example lists all of the Storage Lens groups for your account.
   To use this example command, replace the `user input
 placeholders` with your own information.

```
aws s3control list-storage-lens-groups --account-id `111122223333` \
--region `us-east-1`
```

The following AWS SDK for Java example lists the Storage Lens groups for account
`111122223333`. To use this
example, replace the `user input placeholders`
with your own information.

```
package aws.example.s3control;

import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3control.S3ControlClient;
import software.amazon.awssdk.services.s3control.model.ListStorageLensGroupsRequest;
import software.amazon.awssdk.services.s3control.model.ListStorageLensGroupsResponse;

public class ListStorageLensGroups {
    public static void main(String[] args) {
        String accountId = "`111122223333`";

        try {
            ListStorageLensGroupsRequest listStorageLensGroupsRequest = ListStorageLensGroupsRequest.builder()
                    .accountId(`accountId`)
                    .build();
            S3ControlClient s3ControlClient = S3ControlClient.builder()
                    .region(Region.`US_WEST_2`)
                    .credentialsProvider(ProfileCredentialsProvider.create())
                    .build();
            ListStorageLensGroupsResponse response = s3ControlClient.listStorageLensGroups(listStorageLensGroupsRequest);
            System.out.println(response);
        } catch (AmazonServiceException e) {
            // The call was transmitted successfully, but Amazon S3 couldn't process
            // it and returned an error response.
            e.printStackTrace();
        } catch (SdkClientException e) {
            // Amazon S3 couldn't be contacted for a response, or the client
            // couldn't parse the response from Amazon S3.
            e.printStackTrace();
        }
    }
}
```
