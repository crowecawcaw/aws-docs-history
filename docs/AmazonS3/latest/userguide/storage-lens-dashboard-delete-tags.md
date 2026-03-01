# Deleting AWS resource tags from a S3 Storage Lens dashboard

The following examples demonstrate how to delete AWS resource tags from an existing Storage
Lens dashboard. You can delete tags by using the Amazon S3 console, AWS Command Line Interface (AWS CLI), and
AWS SDK for Java.

###### To delete AWS resource tags from an existing Storage Lens dashboard

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, navigate to **Storage Lens**.
3. Choose **Dashboards**.
4. Choose the radio button for the Storage Lens dashboard configuration
   that you want to view. Then, choose **View dashboard
   configuration**.
5. Under **Tags**, review the tags associated with the dashboard.
6. Choose **Remove** next to the tag that you want to
   remove.
7. Choose **Save changes**.
   The following AWS CLI command deletes AWS resource tags from an existing
   Storage Lens dashboard. To use this example command, replace the
   `user input placeholders` with
   your own information.

###### Example

```
aws s3control delete-storage-lens-configuration-tagging --account-id=`222222222222` --config-id=`your-configuration-id` --region=`us-east-1`
```

The following AWS SDK for Java example deletes an AWS resource tag from the
Storage Lens dashboard using the Amazon Resource Name (ARN) that you specify in account
`111122223333`. To use
this example, replace the `user input
 placeholders` with your own information.

###### Example– Delete tags for an S3 Storage Lens dashboard configuration

```
package aws.example.s3control;

import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.s3control.AWSS3Control;
import com.amazonaws.services.s3control.AWSS3ControlClient;
import com.amazonaws.services.s3control.model.DeleteStorageLensConfigurationTaggingRequest;

import static com.amazonaws.regions.Regions.`US_WEST_2`;

public class DeleteDashboardTagging {

    public static void main(String[] args) {
        String configurationId = "`ConfigurationId`";
        String sourceAccountId = "`111122223333`";
        try {
            AWSS3Control s3ControlClient = AWSS3ControlClient.builder()
                    .withCredentials(new ProfileCredentialsProvider())
                    .withRegion(`US_WEST_2`)
                    .build();

            s3ControlClient.deleteStorageLensConfigurationTagging(new DeleteStorageLensConfigurationTaggingRequest()
                    .withAccountId(sourceAccountId)
                    .withConfigId(configurationId)
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
