# Retrieve AWS resource tags for a Storage Lens
 dashboard

The following examples demonstrate how to retrieve AWS resource tags for a S3 Storage Lens
 dashboard. You can get resource tags by using the Amazon S3 console, AWS Command Line Interface (AWS CLI), and
 AWS SDK for Java.

###### To retrieve the AWS resource tags for a Storage Lens dashboard

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
 the previous tag value.
7. (Optional) If you want to remove a newly added entry, choose
 **Remove** next to the tag that you want to
 remove.
8. Choose **Save changes**.
The following example command retrieves tags for a S3 Storage Lens dashboard configuration. To use these
 examples, replace the ``user input placeholders`` with
 your own information.


```
aws s3control get-storage-lens-configuration-tagging --account-id=`222222222222` --region=`us-east-1` --config-id=`your-configuration-id` --tags=`file://./tags.json`
```
###### Example – Get tags for an S3 Storage Lens dashboard configuration

The following example shows you how to retrieve tags for an S3 Storage Lens
 dashboard configuration in SDK for Java. To use this example, replace the
 ``user input placeholders`` with
 your own information.


```
package aws.example.s3control;

import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.s3control.AWSS3Control;
import com.amazonaws.services.s3control.AWSS3ControlClient;
import com.amazonaws.services.s3control.model.DeleteStorageLensConfigurationRequest;
import com.amazonaws.services.s3control.model.GetStorageLensConfigurationTaggingRequest;
import com.amazonaws.services.s3control.model.StorageLensTag;

import java.util.List;

import static com.amazonaws.regions.Regions.`US_WEST_2`;

public class GetDashboardTagging {

    public static void main(String[] args) {
        String configurationId = "`ConfigurationId`";
        String sourceAccountId = "`111122223333`";
        try {
            AWSS3Control s3ControlClient = AWSS3ControlClient.builder()
                    .withCredentials(new ProfileCredentialsProvider())
                    .withRegion(`US_WEST_2`)
                    .build();

            final List<StorageLensTag> s3Tags = s3ControlClient
                    .getStorageLensConfigurationTagging(new GetStorageLensConfigurationTaggingRequest()
                            .withAccountId(sourceAccountId)
                            .withConfigId(configurationId)
                    ).getTags();

            System.out.println(s3Tags.toString());
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
