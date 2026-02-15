# Attaching or removing S3 Storage Lens groups

to or from your dashboard

After you've upgraded to the advanced tier in Amazon S3 Storage Lens, you can attach a [Storage Lens group](storage-lens-groups-overview.md "storage-lens-groups-overview.md") to your dashboard. If you have several Storage Lens groups, you
can include or exclude the groups that you want.

Your Storage Lens groups must reside within the designated home Region in the dashboard
account. After you attach a Storage Lens group to your dashboard, you'll receive the
additional Storage Lens group aggregation data in your metrics export within 48 hours.

###### Note

If you want to view aggregated metrics for your Storage Lens group, you must attach it
to your Storage Lens dashboard. For examples of Storage Lens group JSON configuration
files, see [S3 Storage Lens example configuration with Storage Lens groups in JSON](S3LensHelperFilesCLI.md#StorageLensGroupsHelperFilesCLI "S3LensHelperFilesCLI.md#StorageLensGroupsHelperFilesCLI").

###### To attach a Storage Lens group to a Storage Lens dashboard

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, under **Storage Lens**, choose
   **Dashboards**.
3. Choose the option button for the Storage Lens dashboard that you want to
   attach a Storage Lens group to.
4. Choose **Edit**.
5. Under **Metrics selection**, choose **Advanced
   metrics and recommendations**.
6. Select **Storage Lens group aggregation**.

###### Note

By default, **Advanced metrics** is also selected.
However, you can also deselect this setting as it's not required to
aggregate Storage Lens groups data. 7. Scroll down to **Storage Lens group aggregation** and specify
the Storage Lens group or groups that you either want to include or exclude in
the data aggregation. You can use the following filtering options:

    * If you want to include certain Storage Lens groups, choose
     **Include Storage Lens groups**. Under
     **Storage Lens groups to include**, select your
     Storage Lens groups.
    * If you want to include all Storage Lens groups, select
     **Include all Storage Lens groups in home Region in this
     account**.
    * If you want to exclude certain Storage Lens groups, choose
     **Exclude Storage Lens groups**. Under
     **Storage Lens groups to exclude**, select the
     Storage Lens groups that you want to exclude.

8. Choose **Save changes**. If you've configured your Storage
   Lens groups correctly, you will see the additional Storage Lens group
   aggregation data in your dashboard within 48 hours.

###### To remove a Storage Lens group from an S3 Storage Lens dashboard

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, under **Storage Lens**, choose
   **Dashboards**.
3. Choose the option button for the Storage Lens dashboard that you want to remove a
   Storage Lens group from.
4. Choose **View dashboard configuration**.
5. Choose **Edit**.
6. Scroll down to the **Metrics selection** section.
7. Under **Storage Lens group aggregation**, choose the
   **X** next to the Storage Lens group that you want to remove. This
   removes your Storage Lens group.

If you included all of your Storage Lens groups in your dashboard, clear the check
box next to **Include all Storage Lens groups in home Region in this
account**. 8. Choose **Save changes**.

###### Note

It will take up to 48 hours for your dashboard to reflect the configuration
updates.

###### Example– Attach all Storage Lens groups to a dashboard

The following SDK for Java example attaches all Storage Lens groups in the account `111122223333` to the `DashBoardConfigurationId` dashboard:

```
package aws.example.s3control;


import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import com.amazonaws.services.s3control.AWSS3Control;
import com.amazonaws.services.s3control.AWSS3ControlClient;
import com.amazonaws.services.s3control.model.BucketLevel;
import com.amazonaws.services.s3control.model.PutStorageLensConfigurationRequest;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.s3control.model.AccountLevel;
import com.amazonaws.services.s3control.model.StorageLensConfiguration;
import com.amazonaws.services.s3control.model.StorageLensGroupLevel;

import static com.amazonaws.regions.Regions.`US_WEST_2`;

public class CreateDashboardWithStorageLensGroups {
    public static void main(String[] args) {
        String configurationId = "`ExampleDashboardConfigurationId`";
        String sourceAccountId = "`111122223333`";

        try {
            StorageLensGroupLevel storageLensGroupLevel = new StorageLensGroupLevel();

            AccountLevel accountLevel = new AccountLevel()
                    .withBucketLevel(new BucketLevel())
                    .withStorageLensGroupLevel(`storageLensGroupLevel`);

            StorageLensConfiguration configuration = new StorageLensConfiguration()
                    .withId(configurationId)
                    .withAccountLevel(accountLevel)
                    .withIsEnabled(true);

            AWSS3Control s3ControlClient = AWSS3ControlClient.builder()
                    .withCredentials(new ProfileCredentialsProvider())
                    .withRegion(`US_WEST_2`)
                    .build();

            s3ControlClient.putStorageLensConfiguration(new PutStorageLensConfigurationRequest()
                    .withAccountId(sourceAccountId)
                    .withConfigId(configurationId)
                    .withStorageLensConfiguration(configuration)
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

###### Example– Attach two Storage Lens groups to a dashboard

The following AWS SDK for Java example attaches two Storage Lens groups
(`StorageLensGroupName1` and
`StorageLensGroupName2`) to the
`ExampleDashboardConfigurationId` dashboard.

```
package aws.example.s3control;

import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.s3control.AWSS3Control;
import com.amazonaws.services.s3control.AWSS3ControlClient;
import com.amazonaws.services.s3control.model.AccountLevel;
import com.amazonaws.services.s3control.model.BucketLevel;
import com.amazonaws.services.s3control.model.PutStorageLensConfigurationRequest;
import com.amazonaws.services.s3control.model.StorageLensConfiguration;
import com.amazonaws.services.s3control.model.StorageLensGroupLevel;
import com.amazonaws.services.s3control.model.StorageLensGroupLevelSelectionCriteria;

import static com.amazonaws.regions.Regions.`US_WEST_2`;

public class CreateDashboardWith2StorageLensGroups {
    public static void main(String[] args) {
        String configurationId = "`ExampleDashboardConfigurationId`";
        String storageLensGroupName1 = "`StorageLensGroupName1`";
        String storageLensGroupName2 = "`StorageLensGroupName2`";
        String sourceAccountId = "`111122223333`";

        try {
            StorageLensGroupLevelSelectionCriteria selectionCriteria = new StorageLensGroupLevelSelectionCriteria()
                    .withInclude(
                            "arn:aws:s3:" + `US_WEST_2`.getName() + ":" + sourceAccountId + ":storage-lens-group/" + `storageLensGroupName1`,
                            "arn:aws:s3:" + `US_WEST_2`.getName() + ":" + sourceAccountId + ":storage-lens-group/" + `storageLensGroupName2`);

            System.out.println(selectionCriteria);
            StorageLensGroupLevel storageLensGroupLevel = new StorageLensGroupLevel()
                    .withSelectionCriteria(selectionCriteria);

            AccountLevel accountLevel = new AccountLevel()
                    .withBucketLevel(new BucketLevel())
                    .withStorageLensGroupLevel(storageLensGroupLevel);

            StorageLensConfiguration configuration = new StorageLensConfiguration()
                    .withId(configurationId)
                    .withAccountLevel(accountLevel)
                    .withIsEnabled(true);

            AWSS3Control s3ControlClient = AWSS3ControlClient.builder()
                    .withCredentials(new ProfileCredentialsProvider())
                    .withRegion(`US_WEST_2`)
                    .build();

            s3ControlClient.putStorageLensConfiguration(new PutStorageLensConfigurationRequest()
                    .withAccountId(sourceAccountId)
                    .withConfigId(configurationId)
                    .withStorageLensConfiguration(configuration)
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

###### Example– Attach all Storage Lens groups with exclusions

The following SDK for Java example attaches all Storage Lens groups to the
`ExampleDashboardConfigurationId` dashboard, excluding the two specified
(`StorageLensGroupName1` and `StorageLensGroupName2`):

```
package aws.example.s3control;


import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.s3control.AWSS3Control;
import com.amazonaws.services.s3control.AWSS3ControlClient;
import com.amazonaws.services.s3control.model.AccountLevel;
import com.amazonaws.services.s3control.model.BucketLevel;
import com.amazonaws.services.s3control.model.PutStorageLensConfigurationRequest;
import com.amazonaws.services.s3control.model.StorageLensConfiguration;
import com.amazonaws.services.s3control.model.StorageLensGroupLevel;
import com.amazonaws.services.s3control.model.StorageLensGroupLevelSelectionCriteria;

import static com.amazonaws.regions.Regions.`US_WEST_2`;

public class CreateDashboardWith2StorageLensGroupsExcluded {
    public static void main(String[] args) {
        String configurationId = "`ExampleDashboardConfigurationId`";
        String storageLensGroupName1 = "`StorageLensGroupName1`";
        String storageLensGroupName2 = "`StorageLensGroupName2`";
        String sourceAccountId = "`111122223333`";

        try {
            StorageLensGroupLevelSelectionCriteria selectionCriteria = new StorageLensGroupLevelSelectionCriteria()
                    .withInclude(
                            "arn:aws:s3:" + `US_WEST_2`.getName() + ":" + sourceAccountId + ":storage-lens-group/" + `storageLensGroupName1`,
                            "arn:aws:s3:" + `US_WEST_2`.getName() + ":" + sourceAccountId + ":storage-lens-group/" + `storageLensGroupName2`);

            System.out.println(selectionCriteria);
            StorageLensGroupLevel storageLensGroupLevel = new StorageLensGroupLevel()
                    .withSelectionCriteria(selectionCriteria);

            AccountLevel accountLevel = new AccountLevel()
                    .withBucketLevel(new BucketLevel())
                    .withStorageLensGroupLevel(storageLensGroupLevel);

            StorageLensConfiguration configuration = new StorageLensConfiguration()
                    .withId(configurationId)
                    .withAccountLevel(accountLevel)
                    .withIsEnabled(true);

            AWSS3Control s3ControlClient = AWSS3ControlClient.builder()
                    .withCredentials(new ProfileCredentialsProvider())
                    .withRegion(`US_WEST_2`)
                    .build();

            s3ControlClient.putStorageLensConfiguration(new PutStorageLensConfigurationRequest()
                    .withAccountId(sourceAccountId)
                    .withConfigId(configurationId)
                    .withStorageLensConfiguration(configuration)
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
