

# Listing Storage Lens group tags
<a name="storage-lens-groups-list-tags"></a>

The following examples demonstrate how to list the AWS resource tags associated with a Storage Lens group. You can list tags by using the Amazon S3 console, AWS Command Line Interface (AWS CLI), and AWS SDK for Java.

## Using the S3 console
<a name="storage-lens-groups-list-tags-console"></a>

**To review the list of tags and tag values for a Storage Lens group**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **Storage Lens groups**.

1. Under **Storage Lens groups**, choose the Storage Lens group that you're interested in.

1. Scroll down to the **AWS resource tags** section. All of the user-defined AWS resource tags that are added to your Storage Lens group are listed along with their tag values.

## Using the AWS CLI
<a name="storage-lens-group-list-tags-cli"></a>

The following AWS CLI example command lists all the Storage Lens group tag values for the Storage Lens group named `{{marketing-department}}`. To use this example command, replace the `{{user input placeholders}}` with your own information.

```
aws s3control list-tags-for-resource --account-id {{111122223333}} \
--resource-arn arn:aws:s3:{{us-east-1}}:{{111122223333}}:storage-lens-group/{{marketing-department}} \
--region {{us-east-1}}
```

## Using the AWS SDK for Java
<a name="storage-lens-group-list-tags-sdk-java"></a>

The following AWS SDK for Java example lists the Storage Lens group tag values for the Storage Lens group Amazon Resource Name (ARN) that you specify. To use this example, replace the `{{user input placeholders}}` with your own information.

```
package aws.example.s3control;

import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3control.S3ControlClient;
import software.amazon.awssdk.services.s3control.model.ListTagsForResourceRequest;
import software.amazon.awssdk.services.s3control.model.ListTagsForResourceResponse;

public class ListTagsForResource {
    public static void main(String[] args) {
        String resourceARN = "{{Resource_ARN}}";
        String accountId = "{{111122223333}}";

        try {
            ListTagsForResourceRequest listTagsForResourceRequest = ListTagsForResourceRequest.builder()
                    .resourceArn({{resourceARN}})
                    .accountId({{accountId}})
                    .build();
            S3ControlClient s3ControlClient = S3ControlClient.builder()
                    .region(Region.{{US_WEST_2}})
                    .credentialsProvider(ProfileCredentialsProvider.create())
                    .build();
            ListTagsForResourceResponse response = s3ControlClient.listTagsForResource(listTagsForResourceRequest);
            System.out.println(response);
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