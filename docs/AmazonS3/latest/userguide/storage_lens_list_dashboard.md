# List Amazon S3 Storage Lens dashboards

 

###### To list S3 Storage Lens dashboards

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, navigate to **Storage Lens**.
3. Choose **Dashboards**. You can now view the dashboards in your AWS account.
The following example command lists the S3 Storage Lens dashboards in your AWS account. To use these
 examples, replace the ``user input placeholders`` with
 your own information.


```
aws s3control list-storage-lens-configurations --account-id=`222222222222` --region=`us-east-1` --next-token=`abcdefghij1234`
```
The following example lists S3 Storage Lens configurations without a next token. To use these
 examples, replace the ``user input placeholders`` with
 your own information.


```
aws s3control list-storage-lens-configurations --account-id=`222222222222` --region=`us-east-1`
```
###### Example – List S3 Storage Lens dashboard configurations

The following examples shows you how to list S3 Storage Lens configurations in SDK for Java. To use
 this example, replace the ``user input placeholders``
 with your own information." to each example description.


```
package aws.example.s3control;

import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.s3control.AWSS3Control;
import com.amazonaws.services.s3control.AWSS3ControlClient;
import com.amazonaws.services.s3control.model.ListStorageLensConfigurationEntry;
import com.amazonaws.services.s3control.model.ListStorageLensConfigurationsRequest;

import java.util.List;

import static com.amazonaws.regions.Regions.`US_WEST_2`;

public class ListDashboard {

    public static void main(String[] args) {
        String sourceAccountId = "`111122223333`";
        String nextToken = "`nextToken`";

        try {
            AWSS3Control s3ControlClient = AWSS3ControlClient.builder()
                    .withCredentials(new ProfileCredentialsProvider())
                    .withRegion(`US_WEST_2`)
                    .build();

            final List<ListStorageLensConfigurationEntry> configurations =
                    s3ControlClient.listStorageLensConfigurations(new ListStorageLensConfigurationsRequest()
                            .withAccountId(sourceAccountId)
                            .withNextToken(nextToken)
                    ).getStorageLensConfigurationList();

            System.out.println(configurations.toString());
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
