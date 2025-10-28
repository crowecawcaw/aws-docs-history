# Delete an Amazon S3 Storage Lens dashboard

You can't delete the default dashboard. However, you can disable it. Before deleting a
dashboard that you've created, consider the following:

- As an alternative to deleting a dashboard, you can _disable_ the dashboard so that it is available to be re-enabled in the
  future. For more information, see [Using the S3 console](storage_lens_console_disabling.md "storage_lens_console_disabling.md").
- Deleting the dashboard deletes all the configuration settings that are associated with
  it.
- Deleting a dashboard makes all the historic metrics data unavailable. This historical
  data is still retained for 15 months. If you want to access this data again, create a
  dashboard with the same name in the same home Region as the one that was deleted.
  You can delete an Amazon S3 Storage Lens dashboard from the Amazon S3 console. However, deleting a dashboard
  prevents it from generating metrics in the future.

###### Deleting an Amazon S3 Storage Lens dashboard

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Storage Lens**,
   **Dashboards**.
3. In the **Dashboards** list, choose the dashboard that you want to
   delete, and then choose **Delete** at the top of the list.
4. On the **Delete dashboards** page, confirm that you want to delete the
   dashboard by entering the name of dashboard in the text field. Then choose
   **Confirm**.
   The following example deletes a S3 Storage Lens configuration. To use these
   examples, replace the `user input placeholders` with
   your own information.

```
aws s3control delete-storage-lens-configuration --account-id=`222222222222` --region=`us-east-1` --config-id=`your-configuration-id`
```

###### Example – Delete an Amazon S3 Storage Lens dashboard configuration

The following example shows you how to delete an S3 Storage Lens configuration using SDK for Java:

```
package aws.example.s3control;

import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.s3control.AWSS3Control;
import com.amazonaws.services.s3control.AWSS3ControlClient;
import com.amazonaws.services.s3control.model.DeleteStorageLensConfigurationRequest;

import static com.amazonaws.regions.Regions.`US_WEST_2`;

public class DeleteDashboard {

    public static void main(String[] args) {
        String configurationId = "`ConfigurationId`";
        String sourceAccountId = "`111122223333`";
        try {
            AWSS3Control s3ControlClient = AWSS3ControlClient.builder()
                    .withCredentials(new ProfileCredentialsProvider())
                    .withRegion(`US_WEST_2`)
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
