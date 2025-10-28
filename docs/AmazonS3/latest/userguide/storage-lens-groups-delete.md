# Deleting a Storage Lens group

The following examples demonstrate how to delete an Amazon S3 Storage Lens group by using the
Amazon S3 console, AWS Command Line Interface (AWS CLI), and AWS SDK for Java.

###### To delete a Storage Lens group

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Storage Lens
   groups**.
3. Under **Storage Lens groups**, choose the option button
   next to the Storage Lens group that you want to delete.
4. Choose **Delete**. A **Delete Storage Lens
   group** dialog box displays.
5. Choose **Delete** again to permanently delete your
   Storage Lens group.

###### Note

After you delete a Storage Lens group, it can't be restored.
The following AWS CLI example deletes the Storage Lens group named
`marketing-department`. To use this
example command, replace the `user input
 placeholders` with your own information.

```
aws s3control delete-storage-lens-group --account-id `111122223333` \
--region `us-east-1` --name `marketing-department`
```

The following AWS SDK for Java example deletes the Storage Lens group named
`Marketing-Department` in account
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
import software.amazon.awssdk.services.s3control.model.DeleteStorageLensGroupRequest;

public class DeleteStorageLensGroup {
    public static void main(String[] args) {
        String storageLensGroupName = "`Marketing-Department`";
        String accountId = "`111122223333`";

        try {
            DeleteStorageLensGroupRequest deleteStorageLensGroupRequest = DeleteStorageLensGroupRequest.builder()
                    .name(storageLensGroupName)
                    .accountId(`accountId`).build();
            S3ControlClient s3ControlClient = S3ControlClient.builder()
                    .region(Region.`US_WEST_2`)
                    .credentialsProvider(ProfileCredentialsProvider.create())
                    .build();
            s3ControlClient.deleteStorageLensGroup(deleteStorageLensGroupRequest);
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
