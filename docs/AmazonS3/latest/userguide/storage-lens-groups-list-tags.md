# Listing Storage Lens group tags

The following examples demonstrate how to list the AWS resource tags associated with
 a Storage Lens group. You can list tags by using the Amazon S3 console, AWS Command Line Interface (AWS CLI),
 and AWS SDK for Java.

###### To review the list of tags and tag values for a Storage Lens
 group

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Storage Lens
 groups**.
3. Under **Storage Lens groups**, choose the Storage
 Lens group that you're interested in.
4. Scroll down to the **AWS resource tags** section.
 All of the user-defined AWS resource tags that are added to your
 Storage Lens group are listed along with their tag values.
The following AWS CLI example command lists all the Storage Lens group tag
 values for the Storage Lens group named
 ``marketing-department``. To use
 this example command, replace the ``user input
 placeholders`` with your own information.


```
aws s3control list-tags-for-resource --account-id `111122223333` \
--resource-arn arn:aws:s3:`us-east-1`:`111122223333`:storage-lens-group/`marketing-department` \
--region `us-east-1`
```
The following AWS SDK for Java example lists the Storage Lens group tag values for
 the Storage Lens group Amazon Resource Name (ARN) that you specify. To use this
 example, replace the ``user input
 placeholders`` with your own information.


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
        String resourceARN = "`Resource_ARN`";
        String accountId = "`111122223333`";

        try {
            ListTagsForResourceRequest listTagsForResourceRequest = ListTagsForResourceRequest.builder()
                    .resourceArn(`resourceARN`)
                    .accountId(`accountId`)
                    .build();
            S3ControlClient s3ControlClient = S3ControlClient.builder()
                    .region(Region.`US_WEST_2`)
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
