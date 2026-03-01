# Deleting an AWS resource tag from a Storage Lens group

The following examples demonstrate how to delete an AWS resource tag from a Storage
Lens group. You can delete tags by using the Amazon S3 console, AWS Command Line Interface (AWS CLI), and
AWS SDK for Java.

###### To delete an AWS resource tag from a Storage Lens group

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Storage Lens
   groups**.
3. Under **Storage Lens groups**, choose the Storage
   Lens group that you want to update.
4. Under **AWS resource tags**, select the key-value
   pair that you want to delete.
5. Choose **Delete**. The **Delete AWS
   resource tags** dialog box appears.

###### Note

If tags are used to control access, proceeding with this action
can affect related resources. After you permanently delete a tag, it
can't be restored. 6. Choose **Delete** to permanently delete the key-value
pair.
The following AWS CLI command deletes two AWS resource tags from an existing
Storage Lens group: To use this example command, replace the
`user input placeholders` with
your own information.

```
aws s3control untag-resource --account-id `111122223333` \
--resource-arn arn:aws:s3:`us-east-1`:`111122223333`:storage-lens-group/`Marketing-Department` \
--region `us-east-1` --tag-keys `k1` `k2`
```

The following AWS SDK for Java example deletes two AWS resource tags from the
Storage Lens group Amazon Resource Name (ARN) that you specify in account
`111122223333`. To use
this example, replace the `user input
 placeholders` with your own information.

```
package aws.example.s3control;

import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3control.S3ControlClient;
import software.amazon.awssdk.services.s3control.model.UntagResourceRequest;

public class UntagResource {
    public static void main(String[] args) {
        String resourceARN = "`Resource_ARN`";
        String accountId = "`111122223333`";

        try {
            String tagKey1 = "`resource-tag-key-1`";
            String tagKey2 = "`resource-tag-key-2`";
            UntagResourceRequest untagResourceRequest = UntagResourceRequest.builder()
                    .resourceArn(`resourceARN`)
                    .tagKeys(`tagKey1`, `tagKey2`)
                    .accountId(`accountId`)
                    .build();
            S3ControlClient s3ControlClient = S3ControlClient.builder()
                    .region(Region.`US_WEST_2`)
                    .credentialsProvider(ProfileCredentialsProvider.create())
                    .build();
            s3ControlClient.untagResource(untagResourceRequest);
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
