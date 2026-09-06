

# View an Amazon S3 Storage Lens dashboard configuration details
<a name="storage_lens_viewing"></a>

You can view a Amazon S3 Storage Lens dashboard from the Amazon S3 console, AWS CLI, and SDK for Java.

## Using the AWS CLI
<a name="S3ListStorageLensConfigurationsCLI"></a>

**Example**  
The following example retrieves an S3 Storage Lens configuration so that you can view the configuration details. To use these examples, replace the `{{user input placeholders}}` with your own information.  

```
aws s3control get-storage-lens-configuration --account-id={{222222222222}} --config-id={{your-configuration-id}} --region={{us-east-1}}
```

## Using the AWS SDK for Java
<a name="S3GetStorageLensConfigurationJava"></a>

**Example – Retrieve and view an S3 Storage Lens configuration**  
The following example shows you how to retrieve an S3 Storage Lens configuration in SDK for Java so that you can view the configuration details. To use this example, replace the `{{user input placeholders}}` with your own information.  

```
package aws.example.s3control;

import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.s3control.AWSS3Control;
import com.amazonaws.services.s3control.AWSS3ControlClient;
import com.amazonaws.services.s3control.model.GetStorageLensConfigurationRequest;
import com.amazonaws.services.s3control.model.GetStorageLensConfigurationResult;
import com.amazonaws.services.s3control.model.StorageLensConfiguration;

import static com.amazonaws.regions.Regions.{{US_WEST_2}};

public class GetDashboard {

    public static void main(String[] args) {
        String configurationId = "{{ConfigurationId}}";
        String sourceAccountId = "{{111122223333}}";

        try {
            AWSS3Control s3ControlClient = AWSS3ControlClient.builder()
                    .withCredentials(new ProfileCredentialsProvider())
                    .withRegion({{US_WEST_2}})
                    .build();

            final StorageLensConfiguration configuration =
                    s3ControlClient.getStorageLensConfiguration(new GetStorageLensConfigurationRequest()
                            .withAccountId(sourceAccountId)
                            .withConfigId(configurationId)
                    ).getStorageLensConfiguration();

            System.out.println(configuration.toString());
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