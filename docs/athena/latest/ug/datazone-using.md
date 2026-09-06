

# Use Amazon DataZone in Athena
<a name="datazone-using"></a>

You can use [Amazon DataZone](https://aws.amazon.com/datazone) to share, search, and discover data at scale across organizational boundaries. DataZone simplifies your experience across AWS analytics services like Athena, AWS Glue, and AWS Lake Formation. For example, if you have petabytes of data in different data sources, you can use Amazon DataZone to build business use case based groupings of people, data and tools. For more information, see [What is Amazon DataZone?](https://docs.aws.amazon.com/datazone/latest/userguide/what-is-datazone.html).

In Athena, you can use the query editor to access and query DataZone environments. A DataZone environment specifies a DataZone project and domain combination. When you use a DataZone environment from the Athena console, you assume the IAM role of the DataZone environment, and you see only the databases and tables that belong to that environment. Permissions are determined by the roles that you specify in DataZone.

In Athena, you can use the **DataZone environment** selector on the query editor page to choose a DataZone environment.

**To open a DataZone environment in Athena**

1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home).

1. In the upper right of the Athena console, next to **Workgroup**, choose **DataZone environment**.
**Note**  
The **DataZone environment** option is present only when you have one or more domains available in DataZone.   
![Choose DataZone environment.](http://docs.aws.amazon.com/athena/latest/ug/images/datazone-using-1.png)

1. Use the **DataZone environment** selector to choose a DataZone environment.  
![Choose a DataZone environment](http://docs.aws.amazon.com/athena/latest/ug/images/datazone-using-2.png)

1. In the **Switch to DataZone environment** dialog box, verify that the environment is the one that you want, and then choose **Switch to DataZone environment**.  
![Verify the change to a DataZone environment.](http://docs.aws.amazon.com/athena/latest/ug/images/datazone-using-3.png)

For more information about getting started with DataZone and Athena, see the [Getting started](https://docs.aws.amazon.com/datazone/latest/userguide/getting-started.html) tutorial in the *Amazon DataZone User Guide*.