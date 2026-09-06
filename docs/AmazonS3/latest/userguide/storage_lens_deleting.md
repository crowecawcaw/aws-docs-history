

# Delete an Amazon S3 Storage Lens dashboard
<a name="storage_lens_deleting"></a>

You can't delete the default dashboard. However, you can disable it. Before deleting a dashboard that you've created, consider the following:
+ As an alternative to deleting a dashboard, you can *disable* the dashboard so that it is available to be re-enabled in the future. For more information, see [Using the S3 console](storage_lens_console_disabling.md).
+ Deleting the dashboard deletes all the configuration settings that are associated with it.
+ Deleting a dashboard makes all the historic metrics data unavailable. This historical data is still retained for 15 months. If you want to access this data again, create a dashboard with the same name in the same home Region as the one that was deleted. 

## Using the AWS SDK for Java
<a name="S3DeleteStorageLensConfigurationJava"></a>

**Example – Delete an Amazon S3 Storage Lens dashboard configuration**  
The following example shows you how to delete an S3 Storage Lens configuration using SDK for Java:  

```
package aws.example.s3control;

import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.s3control.AWSS3Control;
import com.amazonaws.services.s3control.AWSS3ControlClient;
import com.amazonaws.services.s3control.model.DeleteStorageLensConfigurationRequest;

import static com.amazonaws.regions.Regions.{{US_WEST_2}};

public class DeleteDashboard {

    public static void main(String[] args) {
        String configurationId = "{{ConfigurationId}}";
        String sourceAccountId = "{{111122223333}}";
        try {
            AWSS3Control s3ControlClient = AWSS3ControlClient.builder()
                    .withCredentials(new ProfileCredentialsProvider())
                    .withRegion({{US_WEST_2}})
                    .build();

            s3ControlClient.deleteStorageLensConfiguration(new DeleteStorageLensConfigurationRequest()
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