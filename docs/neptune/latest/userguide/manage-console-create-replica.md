# Creating a Neptune reader instance using the console

After creating the primary instance for your Neptune DB cluster, you can add additional
Neptune reader instances using the Neptune console.

###### To create a Neptune reader instance using the AWS Management Console

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. In the navigation pane, choose **Databases**.
3. Select the DB cluster where you want to create the reader instance.
4. Choose **Actions**, and then choose **Add reader**.
5. On the **Create replica DB instance** page, specify options for your
   Neptune replica. The following table shows settings for a Neptune read replica.

| For This Option...             | Do This                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **DB instance class**          | Choose a DB instance class that defines the processing and memory requirements<br>for the Neptune replica. For a current listing of the DB instance classes that Neptune<br>offers in different regions, see [the<br>Neptune pricing page](https://aws.amazon.com/neptune/pricing/ "https://aws.amazon.com/neptune/pricing/").                                                   |
| **Availability zone**          | Specify an Availability Zone. Choose a different zone than the primary DB<br>instance. The list includes only those Availability Zones that are mapped by the<br>DB subnet group for the DB cluster.                                                                                                                                                                             |
| **Encryption**                 | Enable or disable encryption.                                                                                                                                                                                                                                                                                                                                                    |
| **Read replica source**        | Choose the identifier of the primary instance to create a Neptune replica<br>for.                                                                                                                                                                                                                                                                                                |
| **DB instance identifier**     | Enter a name for the instance that is unique for your account in the Region<br>that you selected. You might choose to add some intelligence to the name, such as<br>including the Availability Zone selected, for example<br>`neptune-us-east-1c`.                                                                                                                               |
| **Database port**              | Port number on which the database accepts connections.                                                                                                                                                                                                                                                                                                                           |
| **DB parameter group**         | The parameter group for this instance.                                                                                                                                                                                                                                                                                                                                           |
| **Log exports**                | Choose the logs you want to publish, if any.                                                                                                                                                                                                                                                                                                                                     |
| **Auto Minor Version Upgrade** | Choose **Yes\*<br>• if you want to enable your Neptune replica<br>to receive minor Neptune DB engine version upgrades automatically when they<br>become available.<br>The **Auto Minor Version Upgrade\*<br>• option<br>applies only to minor upgrades. It does not apply to engine maintenance patches,<br>which are always applied automatically to maintain system stability. |

6. Choose **Create read replica** to create the Neptune replica
   instance.
   To remove a Neptune reader instance from a DB cluster, follow the instructions in [Deleting a DB instance in Amazon Neptune](manage-console-instances-delete.md "manage-console-instances-delete.md").
