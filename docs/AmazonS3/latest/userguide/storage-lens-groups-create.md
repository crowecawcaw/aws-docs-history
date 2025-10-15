# Creating a Storage Lens group

The following examples demonstrate how to create an Amazon S3 Storage Lens group by using the
 Amazon S3 console, AWS Command Line Interface (AWS CLI), and AWS SDK for Java.

###### To create a Storage Lens group

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar on the top of the page, choose the name of the currently displayed
 AWS Region. Next, choose the Region that you want to switch to.
3. In the left navigation pane, choose **Storage Lens
 groups**.
4. Choose **Create Storage Lens group**.
5. Under **General**, view your **Home
 Region** and enter your **Storage Lens group
 name**.
6. Under **Scope**, choose the filter that you want to apply
 to your Storage Lens group. To apply multiple filters, choose your filters,
 and then choose the **AND** or **OR**
 logical operator.




	* For the **Prefixes** filter, choose
	 **Prefixes**, and enter a prefix string. To add
	 multiple prefixes, choose **Add prefix**. To remove
	 a prefix, choose **Remove** next to the prefix that
	 you want to remove.
	* For the **Object tags** filter, choose
	 **Object tags**, and enter the key-value pair
	 for your object. Then, choose **Add tag**. To
	 remove a tag, choose **Remove** next to the tag
	 that you want to remove.
	* For the **Suffixes** filter, choose
	 **Suffixes**, and enter a suffix string. To add
	 multiple suffixes, choose **Add suffix**. To remove
	 a suffix, choose **Remove** next to the suffix that
	 you want to remove.
	* For the **Age** filter, specify the object age
	 range in days. Choose **Specify minimum object
	 age**, and enter the minimum object age. Then, choose
	 **Specify maximum object age**, and enter the
	 maximum object age.
	* For the **Size** filter, specify the object size
	 range and unit of measurement. Choose **Specify minimum
	 object size**, and enter the minimum object size.
	 Choose **Specify maximum object size**, and enter
	 the maximum object size.
7. (Optional) For AWS resource tags, add the key-value pair, and then
 choose **Add tag**.
8. Choose **Create Storage Lens group**.
The following example AWS CLI command creates a Storage Lens group. To use this
 example command, replace the ``user input
 placeholders`` with your own information.


```
aws s3control create-storage-lens-group --account-id `111122223333` \ 
--region `us-east-1` --storage-lens-group=file://./`marketing-department`.json
```
The following example AWS CLI command creates a Storage Lens group with two
 AWS resource tags. To use this example command, replace the
 ``user input placeholders`` with your
 own information.


```
aws s3control create-storage-lens-group --account-id `111122223333` \ 
--region `us-east-1` --storage-lens-group=file://./`marketing-department`.json \
--tags Key=`k1`,Value=`v1` Key=`k2`,Value=`v2`
```
For example JSON configurations, see [Storage Lens groups
 configuration](storage-lens-groups.md#storage-lens-groups-configuration "storage-lens-groups.md#storage-lens-groups-configuration").

The following AWS SDK for Java example creates a Storage Lens group. To use this
 example, replace the ``user input placeholders``
 with your own information.

###### Example – Create a Storage Lens group with a single
 filter

The following example creates a Storage Lens group named
 ``Marketing-Department``. This group has
 an object age filter that specifies the age range as
 ``30`` to
 ``90`` days. To use this example,
 replace the ``user input placeholders`` with
 your own information.


```
package aws.example.s3control;
 
import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3control.S3ControlClient;
import software.amazon.awssdk.services.s3control.model.CreateStorageLensGroupRequest;
import software.amazon.awssdk.services.s3control.model.MatchObjectAge;
import software.amazon.awssdk.services.s3control.model.StorageLensGroup;
import software.amazon.awssdk.services.s3control.model.StorageLensGroupFilter;
 
public class CreateStorageLensGroupWithObjectAge {
    public static void main(String[] args) {
        String storageLensGroupName = "`Marketing-Department`";
        String accountId = "`111122223333`";
        
        try {
            StorageLensGroupFilter objectAgeFilter = StorageLensGroupFilter.builder()
                    .matchObjectAge(MatchObjectAge.builder()
                            .daysGreaterThan(`30`)
                            .daysLessThan(`90`)
                            .build())
                    .build();

            StorageLensGroup storageLensGroup = StorageLensGroup.builder()
                    .name(`storageLensGroupName`)
                    .filter(`objectAge`Filter)
                    .build();

            CreateStorageLensGroupRequest createStorageLensGroupRequest = CreateStorageLensGroupRequest.builder()
                    .storageLensGroup(`storageLensGroup`)
                    .accountId(`accountId`).build();

            S3ControlClient s3ControlClient = S3ControlClient.builder()
                    .region(Region.`US_WEST_2`)
                    .credentialsProvider(ProfileCredentialsProvider.create())
                    .build();
            s3ControlClient.createStorageLensGroup(createStorageLensGroupRequest);
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
###### Example – Create a Storage Lens group with an
 `AND` operator that includes multiple filters

The following example creates a Storage Lens group named
 ``Marketing-Department``. This group
 uses the `AND` operator to indicate that objects must match **all** of the filter conditions. To use this example,
 replace the ``user input placeholders`` with
 your own information. 


```
package aws.example.s3control;

import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3control.S3ControlClient;
import software.amazon.awssdk.services.s3control.model.CreateStorageLensGroupRequest;
import software.amazon.awssdk.services.s3control.model.MatchObjectAge;
import software.amazon.awssdk.services.s3control.model.MatchObjectSize;
import software.amazon.awssdk.services.s3control.model.S3Tag;
import software.amazon.awssdk.services.s3control.model.StorageLensGroup;
import software.amazon.awssdk.services.s3control.model.StorageLensGroupAndOperator;
import software.amazon.awssdk.services.s3control.model.StorageLensGroupFilter;


public class CreateStorageLensGroupWithAndFilter {
    public static void main(String[] args) {
        String storageLensGroupName = "`Marketing-Department`";
        String accountId = "`111122223333`";

        try {
            // Create object tags.
            S3Tag tag1 = S3Tag.builder()
                    .key("`object-tag-key-1`")
                    .value("`object-tag-value-1`")
                    .build();
            S3Tag tag2 = S3Tag.builder()
                    .key("`object-tag-key-2`")
                    .value("`object-tag-value-2`")
                    .build();

            StorageLensGroupAndOperator andOperator = StorageLensGroupAndOperator.builder()
                    .matchAnyPrefix("`prefix-1`", "`prefix-2`", "`prefix-3/sub-prefix-1`")
                    .matchAnySuffix("`.png`", "`.gif`", "`.jpg`")
                    .matchAnyTag(`tag1`, `tag2`)
                    .matchObjectAge(MatchObjectAge.builder()
                            .daysGreaterThan(`30`)
                            .daysLessThan(`90`).build())
                    .matchObjectSize(MatchObjectSize.builder()
                            .bytesGreaterThan(`1000L`)
                            .bytesLessThan(`6000L`).build())
                    .build();

            StorageLensGroupFilter andFilter = StorageLensGroupFilter.builder()
                    .and(andOperator)
                    .build();

            StorageLensGroup storageLensGroup = StorageLensGroup.builder()
                    .name(`storageLensGroupName`)
                    .filter(andFilter)
                    .build();

            CreateStorageLensGroupRequest createStorageLensGroupRequest = CreateStorageLensGroupRequest.builder()
                    .storageLensGroup(`storageLensGroup`)
                    .accountId(`accountId`).build();

            S3ControlClient s3ControlClient = S3ControlClient.builder()
                    .region(Region.`US_WEST_2`)
                    .credentialsProvider(ProfileCredentialsProvider.create())
                    .build();
            s3ControlClient.createStorageLensGroup(createStorageLensGroupRequest);
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
###### Example – Create a Storage Lens group with an `OR`
 operator that includes multiple filters

The following example creates a Storage Lens group named
 ``Marketing-Department``. This group
 uses an `OR` operator to apply a prefix filter
 (``prefix-1``,
 ``prefix-2``,
 ``prefix3/sub-prefix-1``) or an object
 size filter with a size range between ``1000``
 bytes and ``6000`` bytes. To use this example,
 replace the ``user input placeholders`` with
 your own information.


```
package aws.example.s3control;

import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3control.S3ControlClient;
import software.amazon.awssdk.services.s3control.model.CreateStorageLensGroupRequest;
import software.amazon.awssdk.services.s3control.model.MatchObjectSize;
import software.amazon.awssdk.services.s3control.model.StorageLensGroup;
import software.amazon.awssdk.services.s3control.model.StorageLensGroupFilter;
import software.amazon.awssdk.services.s3control.model.StorageLensGroupOrOperator;

public class CreateStorageLensGroupWithOrFilter {
    public static void main(String[] args) {
        String storageLensGroupName = "`Marketing-Department`";
        String accountId = "`111122223333`";

        try {
            StorageLensGroupOrOperator orOperator = StorageLensGroupOrOperator.builder()
                    .matchAnyPrefix("`prefix-1`", "`prefix-2`", "`prefix-3/sub-prefix-1`")
                    .matchObjectSize(MatchObjectSize.builder()
                            .bytesGreaterThan(`1000L`)
                            .bytesLessThan(`6000L`)
                            .build())
                    .build();

            StorageLensGroupFilter orFilter = StorageLensGroupFilter.builder()
                    .or(orOperator)
                    .build();

            StorageLensGroup storageLensGroup = StorageLensGroup.builder()
                    .name(`storageLensGroupName`)
                    .filter(orFilter)
                    .build();

            CreateStorageLensGroupRequest createStorageLensGroupRequest = CreateStorageLensGroupRequest.builder()
                    .storageLensGroup(`storageLensGroup`)
                    .accountId(`accountId`).build();

            S3ControlClient s3ControlClient = S3ControlClient.builder()
                    .region(Region.`US_WEST_2`)
                    .credentialsProvider(ProfileCredentialsProvider.create())
                    .build();
            s3ControlClient.createStorageLensGroup(createStorageLensGroupRequest);
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
###### Example – Create a Storage Lens group with a single filter
 and two AWS resource tags

The following example creates a Storage Lens group named
 ``Marketing-Department`` that has a
 suffix filter. This example also adds two AWS resource tags to the Storage Lens
 group. To use this example, replace the ``user input
 placeholders`` with your own information.


```
package aws.example.s3control;

import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3control.S3ControlClient;
import software.amazon.awssdk.services.s3control.model.CreateStorageLensGroupRequest;
import software.amazon.awssdk.services.s3control.model.StorageLensGroup;
import software.amazon.awssdk.services.s3control.model.StorageLensGroupFilter;
import software.amazon.awssdk.services.s3control.model.Tag;

public class CreateStorageLensGroupWithResourceTags {
    public static void main(String[] args) {
        String storageLensGroupName = "`Marketing-Department`";
        String accountId = "`111122223333`";

        try {
            // Create AWS resource tags.
            Tag resourceTag1 = Tag.builder()
                    .key("`resource-tag-key-1`")
                    .value("`resource-tag-value-1`")
                    .build();
            Tag resourceTag2 = Tag.builder()
                    .key("`resource-tag-key-2`")
                    .value("`resource-tag-value-2`")
                    .build();

            StorageLensGroupFilter suffixFilter = StorageLensGroupFilter.builder()
                    .matchAnySuffix("`.png`", "`.gif`", ".`jpg`")
                    .build();

            StorageLensGroup storageLensGroup = StorageLensGroup.builder()
                    .name(`storageLensGroupName`)
                    .filter(suffixFilter)
                    .build();

            CreateStorageLensGroupRequest createStorageLensGroupRequest = CreateStorageLensGroupRequest.builder()
                    .storageLensGroup(`storageLensGroup`)
                    .tags(`resourceTag1`, `resourceTag2`)
                    .accountId(`accountId`).build();

            S3ControlClient s3ControlClient = S3ControlClient.builder()
                    .region(Region.`US_WEST_2`)
                    .credentialsProvider(ProfileCredentialsProvider.create())
                    .build();
            s3ControlClient.createStorageLensGroup(createStorageLensGroupRequest);
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
