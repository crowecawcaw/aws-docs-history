# Updating Storage Lens group tag
 values

The following examples demonstrate how to update Storage Lens group tag values by
 using the Amazon S3 console, AWS Command Line Interface (AWS CLI), and AWS SDK for Java.

###### To update an AWS resource tag for a Storage Lens group

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Storage Lens
 groups**.
3. Under **Storage Lens groups**, choose the Storage
 Lens group that you want to update.
4. Under **AWS resource tags**, select the tag that
 you want to update.
5. Add the new tag value, using the same key of the key-value pair that
 you want to update. Choose the checkmark icon to update the tag
 value.


###### Note

Adding a new tag with the same key as an existing tag overwrites
 the previous tag value.
6. (Optional) If you want to add new tags, choose **Add
 tag** to add new entries. The **Add tags**
 page appears. 


You can add up to 50 AWS resource tags for your Storage Lens group.
 When you're finished adding new tags, choose **Save
 changes**.
7. (Optional) If you want to remove a newly added entry, choose
 **Remove** next to the tag that you want to remove.
 When you're finished removing tags, choose **Save
 changes**.
The following example AWS CLI command updates two tag values for the Storage
 Lens group named ``marketing-department``.
 To use this example command, replace the ``user input
 placeholders`` with your own information.


```
aws s3control tag-resource --account-id `111122223333` \
--resource-arn arn:aws:s3:`us-east-1`:`111122223333`:storage-lens-group/`marketing-department` \
--region `us-east-1` --tags Key=`k1`,Value=`v3` Key=`k2`,Value=`v4`
```
The following AWS SDK for Java example updates two Storage Lens group tag values. To
 use this example, replace the ``user input
 placeholders`` with your own information.


```
package aws.example.s3control;

import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3control.S3ControlClient;
import software.amazon.awssdk.services.s3control.model.Tag;
import software.amazon.awssdk.services.s3control.model.TagResourceRequest;

public class UpdateTagsForResource {
    public static void main(String[] args) {
        String resourceARN = "`Resource_ARN`";
        String accountId = "`111122223333`";

        try {
            Tag updatedResourceTag1 = Tag.builder()
                .key("`resource-tag-key-1`")
                .value("`resource-tag-updated-value-1`")
                .build();
            Tag updatedResourceTag2 = Tag.builder()
                    .key("`resource-tag-key-2`")
                    .value("`resource-tag-updated-value-2`")
                    .build();
            TagResourceRequest tagResourceRequest = TagResourceRequest.builder()
                    .resourceArn(`resourceARN`)
                    .tags(`updatedResourceTag1`, `updatedResourceTag2`)
                    .accountId(`accountId`)
                    .build();
            S3ControlClient s3ControlClient = S3ControlClient.builder()
                    .region(Region.`US_WEST_2`)
                    .credentialsProvider(ProfileCredentialsProvider.create())
                    .build();
            s3ControlClient.tagResource(tagResourceRequest);
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
