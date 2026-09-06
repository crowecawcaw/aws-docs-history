

# Delete a dataset
<a name="assistant-console-delete-dataset"></a>

**Note**  
The SiteWise Monitor feature is no longer available to new customers. Existing customers can continue to use the service as normal. For more information, see [SiteWise Monitor availability change](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html).

------
#### [ Console ]

**Delete a dataset**

1.  Datasets are displayed in the **Datasets** section of the **Assistant** page. Choose a dataset. Choose **Delete**. 

1. Type **confirm** in the popup to confirm the delete.  
![Deleting a dataset final picture in the Assistant page of the console](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/ai-assistant-del-details-dataset.png)

1.  Choose **Delete**. 

------
#### [ AWS CLI ]

**Delete a dataset**
+ Delete the dataset with `datasetId`.

  ```
  aws iotsitewise delete-dataset --region us-east-1 --dataset-id <UUID>
  ```

------