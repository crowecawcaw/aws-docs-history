# Teardown

###### Note

Please make sure you empty s3 buckets before deletion of
CidDataCollectionStack.

1. In the Data Collection Account, go to S3 and search for bucket names that contain "costoptimization" or cid-data, select the radio button next to the bucket name and then click **Empty**.
2. Navigate to CloudFormation console and search for the Stack named **CidDataCollectionStack**, select the radio button next to the Stack and click **Delete**.
3. In the Management Account, go to CloudFormation Console and search for Stack named **CidDataCollectionReadPermissionsStack**, select the radio button next to the Stack and click **Delete**. This will delete IAM Role created in Management Account to be assumed by Lambda for reading data.
