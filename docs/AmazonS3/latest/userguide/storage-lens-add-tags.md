# Add AWS resource tags to a Storage Lens dashboard

The following examples demonstrate how to add AWS resource tags to an S3 Storage Lens
dashboard. You can add resource tags by using the Amazon S3 console, AWS Command Line Interface (AWS CLI), and
AWS SDK for Java.

###### To add AWS resource tags to a Storage Lens dashboard

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, navigate to **Storage Lens** on the left navigation panel.
3. Choose **Dashboards**.
4. Choose the radio button for the Storage Lens dashboard that you want to update. Then, choose **Edit**.
5. Under **General**, choose **Add
   tag**.
6. On the **Add tag** page, add the new key-value
   pair.

###### Note

Adding a new tag with the same key as an existing tag overwrites
the previous tag value. 7. (Optional) To add more than one new tag, choose **Add
tag** again to continue adding new entries. You can add up
to 50 AWS resource tags to your Storage Lens dashboard. 8. (Optional) If you want to remove a newly added entry, choose
**Remove** next to the tag that you want to
remove. 9. Choose **Save changes**.

###### Example

The following example command adds tags to a S3 Storage Lens dashboard configuration. To use these
examples, replace the `user input placeholders` with
your own information.

```
aws s3control put-storage-lens-configuration-tagging --account-id=`222222222222` --region=`us-east-1` --config-id=`your-configuration-id` --tags=`file://./tags.json`
```

The following example adds tags to an Amazon S3 Storage Lens configuration in SDK for Java. To use this example, replace the `user
 input placeholders` with your own
information.

###### Example– Add tags to an S3 Storage Lens configuration

```
package aws.example.s3control;

import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.s3control.AWSS3Control;
import com.amazonaws.services.s3control.AWSS3ControlClient;
import com.amazonaws.services.s3control.model.PutStorageLensConfigurationTaggingRequest;
import com.amazonaws.services.s3control.model.StorageLensTag;

import java.util.Arrays;
import java.util.List;

import static com.amazonaws.regions.Regions.`US_WEST_2`;

public class PutDashboardTagging {

    public static void main(String[] args) {
        String configurationId = "`ConfigurationId`";
        String sourceAccountId = "`111122223333`";

        try {
            List<StorageLensTag> tags = Arrays.asList(
                    new StorageLensTag().withKey("`key-1`").withValue("`value-1`"),
                    new StorageLensTag().withKey("`key-2`").withValue("`value-2`")
            );

            AWSS3Control s3ControlClient = AWSS3ControlClient.builder()
                    .withCredentials(new ProfileCredentialsProvider())
                    .withRegion(`US_WEST_2`)
                    .build();

            s3ControlClient.putStorageLensConfigurationTagging(new PutStorageLensConfigurationTaggingRequest()
                    .withAccountId(sourceAccountId)
                    .withConfigId(configurationId)
                    .withTags(tags)
            );
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
