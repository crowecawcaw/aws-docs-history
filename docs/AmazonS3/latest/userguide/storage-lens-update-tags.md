# Updating Storage Lens dashboard tags

The following examples demonstrate how to update Storage Lens dashboard tags by
using the Amazon S3 console, AWS Command Line Interface (AWS CLI), and AWS SDK for Java.

###### To update an AWS resource tag for a Storage Lens dashboard

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, navigate to **Storage Lens**.
3. Choose **Dashboards**.
4. Choose the radio button for the Storage Lens dashboard configuration that you want to view. Then, choose **View dashboard configuration**.
5. Under **Tags**, review the tags associated with the dashboard.
6. (Optional) If you want to add a new tag, choose **Edit**. Then, choose **Add
   tag**. On the **Add tag** page, add the new key-value
   pair.

###### Note

Adding a new tag with the same key as an existing tag overwrites
the previous tag value. 7. (Optional) If you want to remove a newly added entry, choose
**Remove** next to the tag that you want to
remove. 8. Choose **Save changes**.

###### Example

The following example command adds or replaces tags on an existing Amazon S3 Storage Lens dashboard configuration. To use these
examples, replace the `user input placeholders` with
your own information.

```
aws s3control put-storage-lens-configuration-tagging --account-id=`111122223333` --config-id=`example-dashboard-configuration-id` --region=`us-east-1` --config-id=`your-configuration-id`
```

The following AWS SDK for Java example updates the AWS resource tags on an existing Storage Lens dashboard. To
use this example, replace the `user input
 placeholders` with your own information.

###### Example– Update tags on an existing Storage Lens dashboard configuration

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
