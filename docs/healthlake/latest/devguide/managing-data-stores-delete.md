

# Deleting a HealthLake data store
<a name="managing-data-stores-delete"></a>

Use `DeleteFHIRDatastore` to delete a HealthLake data store. The following menus provide a procedure for the AWS Management Console and code examples for the AWS CLI and AWS SDKs. For more information, see [`DeleteFHIRDatastore`](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DeleteFHIRDatastores.html) in the *AWS HealthLake API Reference*.

**To delete a HealthLake data store**  
Choose a menu based on your access preference to AWS HealthLake.

## AWS CLI and SDKs
<a name="managing-data-stores-delete-cli-sdk"></a>

------
#### [ CLI ]

**AWS CLI**  
**To delete a FHIR data store**  
The following `delete-fhir-datastore` example demonstrates how to delete a data store and all of its contents in AWS HealthLake.  

```
aws healthlake delete-fhir-datastore \
    --datastore-id {{(Data}} {{store}} {{ID)}}
```
Output:  

```
{
    "DatastoreEndpoint": "https://healthlake.us-east-1.amazonaws.com/datastore/(Data store ID)/r4/",
    "DatastoreArn": "arn:aws:healthlake:us-east-1:(AWS Account ID):datastore/(Data store ID)",
    "DatastoreStatus": "DELETING",
    "DatastoreId": "(Data store ID)"
}
```
  
+  For API details, see [DeleteFHIRDatastore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/delete-fhir-datastore.html) in *AWS CLI Command Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  

```
    @classmethod
    def from_client(cls) -> "HealthLakeWrapper":
        """
        Creates a HealthLakeWrapper instance with a default AWS HealthLake client.

        :return: An instance of HealthLakeWrapper initialized with the default HealthLake client.
        """
        health_lake_client = boto3.client("healthlake")
        return cls(health_lake_client)


    def delete_fhir_datastore(self, datastore_id: str) -> None:
        """
        Deletes a HealthLake data store.
        :param datastore_id: The data store ID.
        """
        try:
            self.health_lake_client.delete_fhir_datastore(DatastoreId=datastore_id)
        except ClientError as err:
            logger.exception(
                "Couldn't delete data store with ID %s. Here's why %s",
                datastore_id,
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [DeleteFHIRDatastore](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/DeleteFHIRDatastore) in *AWS SDK for Python (Boto3) API Reference*. 
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/healthlake#code-examples). 

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/hll#code-examples). 

```
    TRY.
        " iv_datastore_id = 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6'
        oo_result = lo_hll->deletefhirdatastore(
          iv_datastoreid = iv_datastore_id
        ).
        MESSAGE 'Data store deleted successfully.' TYPE 'I'.
      CATCH /aws1/cx_hllaccessdeniedex INTO DATA(lo_access_ex).
        DATA(lv_error) = |Access denied: { lo_access_ex->av_err_code }-{ lo_access_ex->av_err_msg }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_access_ex.
      CATCH /aws1/cx_hllconflictexception INTO DATA(lo_conflict_ex).
        lv_error = |Conflict error: { lo_conflict_ex->av_err_code }-{ lo_conflict_ex->av_err_msg }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_conflict_ex.
      CATCH /aws1/cx_hllresourcenotfoundex INTO DATA(lo_notfound_ex).
        lv_error = |Resource not found: { lo_notfound_ex->av_err_code }-{ lo_notfound_ex->av_err_msg }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_notfound_ex.
    ENDTRY.
```
+  For API details, see [DeleteFHIRDatastore](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*. 

------

**Example availability**  
Can't find what you need? Request a code example using the **Provide feedback** link on the right sidebar of this page.

## AWS Console
<a name="managing-data-stores-delete-console"></a>

1. Sign in to the [Data stores](https://console.aws.amazon.com/healthlake/home#/list-datastores) page on the HealthLake Console.

1. Choose a data store.

   The **Data store details** page opens.

1. Choose **Delete**.

   The **Delete data store** page opens.

1. To confirm data store deletion, enter the data store name in the text input field.

1. Choose **Delete**.