# Managing migration projects in AWS Database Migration Service

After you create your migration project, you can modify or delete it. For example, to change the source
or target data provider, modify your migration project.

You can modify or delete your migration project only after you close the schema conversion or data migration
operations. To do so, choose your migration project from the list, and choose **Schema conversion**
or **Data migrations**. Next, choose **Close schema conversion** for DMS Schema Conversion
and confirm your choice. For homogeneous data migrations, choose your data migration, then choose **Stop** on the
**Actions** menu. After you edit your migration project, you can launch schema conversion or
start your data migration again.

###### To modify a migration project

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. Choose **Migration projects**. The **Migration projects** page
   opens.
3. Choose your migration project, and then choose **Modify**.
4. Update the name of your project, edit the instance profile, or change source
   and target data providers. Optionally, add or edit migration rules that change
   the object names during conversion.
5. Choose **Save changes**.

###### To delete a migration project

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. Choose **Migration projects**. The **Migration projects** page
   opens.
3. Choose your migration project, and then choose **Delete**.
4. Choose **Delete** to confirm your choice.
