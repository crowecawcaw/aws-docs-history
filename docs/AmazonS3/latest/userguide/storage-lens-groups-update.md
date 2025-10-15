# Updating a Storage Lens group

The following examples demonstrate how to update an Amazon S3 Storage Lens group. You can
 update a Storage Lens group by using the Amazon S3 console, AWS Command Line Interface (AWS CLI), and
 AWS SDK for Java.

###### To update a Storage Lens group

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Storage Lens
 groups**.
3. Under **Storage Lens groups**, choose the Storage Lens
 group that you want to update.
4. Under **Scope**, choose **Edit**.
5. On the **Scope** page, select the filter that you want to
 apply to your Storage Lens group. To apply multiple filters, select your
 filters, and choose the **AND** or **OR**
 logical operator.




	* For the **Prefixes** filter, select
	 **Prefixes**, and enter a prefix string. To add
	 multiple prefixes, choose **Add prefix**. To remove
	 a prefix, choose **Remove** next to the prefix that
	 you want to remove.
	* For the **Object tags** filter, enter the
	 key-value pair for your object. Then, choose **Add
	 tag**. To remove a tag, choose
	 **Remove** next to the tag that you want to
	 remove.
	* For the **Suffixes** filter, select
	 **Suffixes**, and enter a suffix string. To add
	 multiple suffixes, choose **Add suffix**. To remove
	 a suffix, choose **Remove** next to the suffix that
	 you want to remove.
	* For the **Age** filter, specify the object age
	 range in days. Choose **Specify minimum object
	 age**, and enter the minimum object age. For
	 **Specify maximum object age**, enter the
	 maximum object age.
	* For the **Size** filter, specify the object size
	 range and unit of measurement. Choose **Specify minimum
	 object size**, and enter the minimum object size. For
	 **Specify maximum object size**, enter the
	 maximum object size.
6. Choose **Save changes**. The details page for the Storage
 Lens group appears.
7. (Optional) If you want to add a new AWS resource tag, scroll to the
 **AWS resource tags** section, then choose
 **Add tags**. The **Add tags** page
 appears. 


Add the new key-value pair, then choose **Save changes**.
 The details page for the Storage Lens group appears.
8. (Optional) If you want to remove an existing AWS resource tag, scroll to
 the **AWS resource tags** section, and select the
 resource tag. Then, choose **Delete**. The **Delete
 AWS tags** dialog box appears. 


Choose **Delete** again to permanently delete the AWS
 resource tag.


###### Note

After you permanently delete an AWS resource tag, it can’t be
 restored.
The following AWS CLI example command returns the configuration details for a
 Storage Lens group named
 ``marketing-department``. To use this
 example command, replace the ``user input
 placeholders`` with your own information.


```
aws s3control get-storage-lens-group --account-id `111122223333` \ 
--region `us-east-1` --name `marketing-department`
```
The following AWS CLI example updates a Storage Lens group. To use this example
 command, replace the ``user input placeholders``
 with your own information. 


```
aws s3control update-storage-lens-group --account-id `111122223333` \ 
--region `us-east-1` --storage-lens-group=file://./`marketing-department`.json
```
For example JSON configurations, see [Storage Lens groups
 configuration](storage-lens-groups.md#storage-lens-groups-configuration "storage-lens-groups.md#storage-lens-groups-configuration").

The following AWS SDK for Java example returns the configuration details for the
 ``Marketing-Department`` Storage Lens
 group in account ``111122223333``. To
 use this example, replace the ``user input
 placeholders`` with your own information.


```
package aws.example.s3control;

import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3control.S3ControlClient;
import software.amazon.awssdk.services.s3control.model.GetStorageLensGroupRequest;
import software.amazon.awssdk.services.s3control.model.GetStorageLensGroupResponse;

public class GetStorageLensGroup {
    public static void main(String[] args) {
        String storageLensGroupName = "`Marketing-Department`";
        String accountId = "`111122223333`";

        try {
            GetStorageLensGroupRequest getRequest = GetStorageLensGroupRequest.builder()
                    .name(`storageLensGroupName`)
                    .accountId(`accountId`).build();
            S3ControlClient s3ControlClient = S3ControlClient.builder()
                    .region(Region.`US_WEST_2`)
                    .credentialsProvider(ProfileCredentialsProvider.create())
                    .build();
            GetStorageLensGroupResponse response = s3ControlClient.getStorageLensGroup(getRequest);
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
The following example updates the Storage Lens group named
 ``Marketing-Department`` in account
 ``111122223333``. This example updates
 the dashboard scope to include objects that match any of the following suffixes:
 ``.png``,
 ``.gif``,
 ``.jpg``, or
 ``.jpeg``. To use this example, replace
 the ``user input placeholders`` with your own
 information.


```
package aws.example.s3control;

import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3control.S3ControlClient;
import software.amazon.awssdk.services.s3control.model.StorageLensGroup;
import software.amazon.awssdk.services.s3control.model.StorageLensGroupFilter;
import software.amazon.awssdk.services.s3control.model.UpdateStorageLensGroupRequest;

public class UpdateStorageLensGroup {
    public static void main(String[] args) {
        String storageLensGroupName = "`Marketing-Department`";
        String accountId = "`111122223333`";

        try {
            // Create updated filter.
            StorageLensGroupFilter suffixFilter = StorageLensGroupFilter.builder()
                    .matchAnySuffix("`.png`", "`.gif`", "`.jpg`", "`.jpeg`")
                    .build();

            StorageLensGroup storageLensGroup = StorageLensGroup.builder()
                    .name(`storageLensGroupName`)
                    .filter(suffixFilter)
                    .build();

            UpdateStorageLensGroupRequest updateStorageLensGroupRequest = UpdateStorageLensGroupRequest.builder()
                    .name(`storageLensGroupName`)
                    .storageLensGroup(`storageLensGroup`)
                    .accountId(`accountId`)
                    .build();

            S3ControlClient s3ControlClient = S3ControlClient.builder()
                    .region(Region.`US_WEST_2`)
                    .credentialsProvider(ProfileCredentialsProvider.create())
                    .build();
            s3ControlClient.updateStorageLensGroup(updateStorageLensGroupRequest);
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
For example JSON configurations, see [Storage Lens groups
 configuration](storage-lens-groups.md#storage-lens-groups-configuration "storage-lens-groups.md#storage-lens-groups-configuration").
