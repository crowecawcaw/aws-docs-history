# Configuring how AWS DataSync verifies

data integrity

During a transfer, AWS DataSync uses checksum verification to verify the integrity of the
data that you copy between locations. You also can configure DataSync to perform additional
verification at the end of your transfer.

## Data verification options

Use the following information to help you decide if and how you want DataSync to
perform these additional checks.

| Console option                                    | API option                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Verify only transferred data**<br>(recommended) | [VerifyMode](API_Options.md#DataSync-Type-Options-VerifyMode "API_Options.md#DataSync-Type-Options-VerifyMode") set to<br>`ONLY_FILES_TRANSFERRED`   | DataSync calculates the checksum of transferred data (including<br>metadata) at the source location. At the end of your transfer,<br>DataSync compares this checksum to the checksum calculated on that<br>same data at the destination.<br>We recommend this option when transferring to<br>S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive<br>storage classes. For more information, see [Storage class considerations with Amazon S3<br>transfers](create-s3-location.md#using-storage-classes "create-s3-location.md#using-storage-classes").                                                                                                                                                                           |
| **Verify all data**                               | [VerifyMode](API_Options.md#DataSync-Type-Options-VerifyMode "API_Options.md#DataSync-Type-Options-VerifyMode") set to<br>`POINT_IN_TIME_CONSISTENT` | At the end of your transfer, DataSync checks the entire source<br>and destination to verify that both locations are fully<br>synchronized.<br>NoteNot supported when your task uses [Enhanced mode](choosing-task-mode.md "choosing-task-mode.md").<br>If you use a [manifest](transferring-with-manifest.md "transferring-with-manifest.md"), DataSync only scans and verifies what's<br>listed in the manifest.<br>You can't use this option when transferring to<br>S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive<br>storage classes. For more information, see [Storage class considerations with Amazon S3<br>transfers](create-s3-location.md#using-storage-classes "create-s3-location.md#using-storage-classes"). |
| **Don't verify data after transfer**              | [VerifyMode](API_Options.md#DataSync-Type-Options-VerifyMode "API_Options.md#DataSync-Type-Options-VerifyMode") set to<br>`NONE`                     | DataSync performs data integrity checks only during your transfer.<br>Unlike other options, there's no additional verification at the end<br>of your transfer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## Configuring data verification

You can configure data verification options when creating a task, updating a task,
or starting a task execution.

The following instructions describe how to configure data verification
options when creating a task.

###### To configure data verification by using the console

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/ "https://console.aws.amazon.com/datasync/").
2. In the left navigation pane, expand **Data transfer**, then choose **Tasks**, and
   then choose **Create task**.
3. Configure your task's source and destination locations.

For more information, see [Where can I transfer my data with
AWS DataSync?](working-with-locations.md "working-with-locations.md") 4. For **Verification**, choose one of the
following:

    * **Verify only transferred data**
     (recommended)
    * **Verify all data**
    * **Don't verify data after
     transfer**

You can configure how DataSync verifies data by using the
`VerifyMode` parameter with any of the following
operations:

- [CreateTask](API_CreateTask.md "API_CreateTask.md")
- [UpdateTask](API_UpdateTask.md "API_UpdateTask.md")
- [StartTaskExecution](API_StartTaskExecution.md "API_StartTaskExecution.md")
