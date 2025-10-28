After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Setting up for database maintenance

To perform the database maintenance operations, you need a writeable shallow copy of a
database . A writable shallow copy of a kdb database only loads the metadata of your database
files to make them visible on the file system and loads the actual file content as they are
accessed. To optimise time and memory utilization, it is recommended not to load file content
initially, as not all files may be necessary for a database maintenance operation. For
instance, in the case of renaming a table, no files are read or updated directly.

To create a writeable shallow copy of database, you can create dataviews with read write
property set as true and enable on-demand caching in the configuration. A dataview performs
minimal loading of files on the file system as needed by a database maintenance operation when
on-demand caching is enabled. Reading an existing database file for the first time is slower
as compared to accessing the files that have been previously read or newly written. This is
because files are loaded onto the file system as they are accessed in case of on-demand
caching.

Before you proceed, complete the following prerequisites:

- Create a kdb environment. For more information, see [Creating a kdb environment](using-kdb-environment.md#create-kdb-environment "using-kdb-environment.md#create-kdb-environment").
- Create a kdb database. For more information, see [Creating a kdb database](using-kdb-db.md#create-kdb-db "using-kdb-db.md#create-kdb-db").
- Create a new changeset. For more information, see [Creating a new changeset](using-kdb-db.md#kdb-db-changesets "using-kdb-db.md#kdb-db-changesets").
- Create a kdb volume. Make sure this volume is not used by any other resource. For more information, see [Creating a Managed kdb volume](create-volumes.md "create-volumes.md").

###### To create a writeable dataview

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2. In the left pane, under **Managed kdb Insights**, choose **Kdb
   environments**.
3. From the kdb environments table, choose the name of the environment.
4. On the environment details page, choose the **Databases** tab.
5. From the list of databases, choose a database name.
6. On database details page, choose the **Dataviews** tab.
7. Choose **Create dataview**.
8. On the **Create dataview** page, enter a unique name for the dataview.
9. (Optional) Enter a description for your dataview.
10. Choose the availability zone that you want to associate with the dataview.
    Currently, you can only choose single availability zone.
11. Under **Changeset update settings**, do the
    following.
    1. Choose **Static** mode of update.

    ###### Note

    The **Read Write** option is only available for **Static**
    update mode as you cannot perform automatic updates on a writeable dataview. 2. Select the **Changeset ID** for the changeset you created to indicate
    which version of data you want. 3. Choose **Read Write** as **True** to make this
    dataview as writeable. You cannot change this later.

12. Add **Segment configuration**.

###### Note

    * The **Segment configuration** is required if **Read
     Write** is **True**.
    * You can only add one segment for a writeable dataview.
    * The **Database path** is disabled and defaults to
     **\\*** when **Read Write** is **True**
     as you cannot have partial writeable dataviews on cache.
    1. Choose a volume for caching. Use an exclusive volume for writable dataviews, it should not be
     in use by any other dataviews.
    2. For **On demand caching**, choose **True** to enable on
     demand caching on the selected database path when a particular file or a column of
     a database is accessed. When you enable on demand caching, files will only be
     copied to the dataview when they are accessed by code for reading or writing. When
     you disable on demand caching, everything is cached. The default value is
     **False**.

13. Choose **Create dataview**. The database details page opens and the table
    under **Dataviews** lists the newly created database along with its
    status.
    Before you proceed, complete the following prerequisites:

- Create a kdb environment by using the [CreateKxEnvironment](../management-api/API_CreateKxEnvironment.md "../management-api/API_CreateKxEnvironment.md") API operation.
- Create a kdb database by using the [CreateKxDatabase](../management-api/API_CreateKxDatabase.md "../management-api/API_CreateKxDatabase.md") API operation.
- Create a new changeset by using the [CreateKxChangeset](../management-api/API_CreateKxChangeset.md "../management-api/API_CreateKxChangeset.md") API operation.
- Create a kdb volume by using the [CreateKxVolume](../management-api/API_CreateKxVolume.md "../management-api/API_CreateKxVolume.md")
  API operation. Make sure this volume is unique for this dataview and is not used by
  any other resource.
  To create a dataview with writable shallow copy of a database, create a dataview with the
  volume that has writable segments by using the [CreateKxDataview](../management-api/API_CreateKxDataview.md "../management-api/API_CreateKxDataview.md")
  API operation. You can make dataview as writeable by setting the `readWrite`
  parameter as true. You can only use this parameter for a static update mode. The
  `onDemand` parameter allows you to enable or disable on-demand caching on the
  selected dbPaths.

Sample `CreateKxDataview` API request

```
{
    "autoUpdate": false,
    "availabilityZoneId": "use1-az1",
    "clientToken": "`65117136-4421-4371-0f1a-ce012823126`",
    "changesetId": "`latest_changesetId`",
    "readWrite": true,
    "segmentConfigurations": [{
            "volumeName": "`test_vol`",
            "dbPaths": [
                "/*"
            ],
            "onDemand": true
        }

    ],
    "azMode": "SINGLE",
    "dataviewName": "`test_dv`"
}
```

Following are some of the considerations for the above request.

- The `autoUpdate` must be `false` for if `readWrite` is
  `true` on the dataviews.
- You need exclusive volume for creating a writable dataview. The volume mentioned
  in the `segmentConfiguration` should not be used by any other
  dataview.
- The `dbPath` must be set as "/\*" for writable dataview.
- Only a single `segmentConfiguration` is allowed when
  `readWrite` is true. The `dbPaths` on the segment should be
  set as "\\\*" .
- A dataview with `readWrite` set as `true` is not allowed to
  be updated.
- You cannot update the `readWrite` property later.
- A dataview can only have a single segment if `onDemand` is
  `true` on a segment.
