

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# Blusam application console REST endpoints
<a name="ba-endpoints-bac"></a>

In this section, you can learn about the Blusam application console, which is an API designed to simplify the management of modernized VSAM datasets. Endpoints for the Blusam web application use the root path `/bac`.

**Topics**
+ [Data sets related endpoints](#ba-endpoints-bac-datasets)
+ [Bulk data sets related endpoints](#ba-endpoints-bac-bulk)
+ [Records](#ba-endpoints-bac-records)
+ [Masks](#ba-endpoints-bac-masks)
+ [Other](#ba-endpoints-bac-other)
+ [BAC user-management endpoints](#ba-endpoints-bac-users)

## Data sets related endpoints
<a name="ba-endpoints-bac-datasets"></a>

Use the following endpoints to create or manage a specific data set.

**Topics**
+ [Create a data set](#ba-create-data-set)
+ [Upload a file](#ba-upload-file)
+ [Load a data set (POST)](#ba-load-data-set-post)
+ [Load a data set (GET)](#ba-load-data-set-get)
+ [Load a data set from an Amazon S3 bucket](#ba-load-data-set-s3)
+ [Export a data set to an Amazon S3 bucket](#ba-export-data-set-s3)
+ [Clear a data set](#ba-clear-data-set)
+ [Delete a data set](#ba-delete-data-set)
+ [Count data set records](#ba-count-data-set-records)

### Create a data set
<a name="ba-create-data-set"></a>

You can use this endpoint to create a data set definition.
+ Supported methods: POST
+ Requires authentication and the ROLE\_ADMIN role.
+ Path: `/api/services/rest/bluesamservice/createDataSet`
+ Arguments:  
name  
(required, string): the name of the data set.   
type  
(required, string): the data set type. Possible values are: `ESDS`, `KSDS`, `RRDS`.   
recordSize  
(optional, string): Maximum size of each record of the data set.   
fixedLength  
(optional, boolean) : Indicates if the records length is fixed.   
compression  
(optional, boolean) : Indicates if the dataset is compressed.   
cacheEnable  
(optional, boolean) : Indicates if caching is enabled for the dataset.   
alternativeKeys  
(optional, list of keys):  
  + offset (required, number)
  + length (required, number)
  + name (required, number)
+ Returns a JSON file representing the newly created data set.

Sample request:

```
POST /api/services/rest/bluesamservice/createDataSet
{
  "name": "DATASET",
  "checked": false,
  "records": [],
  "primaryKey": {
    "name": "PK"
  },
  "alternativeKeys": [
    {
      "offset": 10,
      "length": 10,
      "name": "ALTK_0"
    }
  ],
  "type": "ESDS",
  "recordSize": 10,
  "compression": true,
  "cacheEnable": true
}
```

Sample response:

```
{
    "dataSet": {
      "name": "DATASET",
      "checked": false,
      "nbRecords": 0,
      "keyLength": -1,
      "recordSize": 10,
      "compression": false,
      "fixLength": true,
      "type": "ESDS",
      "cacheEnable": false,
      "cacheWarmup": false,
      "cacheEviction": "100ms",
      "creationDate": 1686744961234,
      "modificationDate": 1686744961234,
      "records": [],
      "primaryKey": {
        "name": "PK",
        "offset": null,
        "length": null,
        "columns": null,
        "unique": true
      },
      "alternativeKeys": [
        {
          "offset": 10,
          "length": 10,
          "name": "ALTK_0"
        }
      ],
      "readLimit": 0,
      "readEncoding": null,
      "initCharacter": null,
      "defaultCharacter": null,
      "blankCharacter": null,
      "strictZoned": null,
      "decimalSeparator": null,
      "currencySign": null,
      "pictureCurrencySign": null
    },
    "message": null,
    "result": true
  }
```

### Upload a file
<a name="ba-upload-file"></a>

You can use this endpoint to upload files to the server. The file is stored in a temporary folder that corresponds to each specific user. Use this endpoint every time you need to upload a file.
+ Supported methods: POST
+ Requires authentication and the ROLE\_ADMIN role.
+ Path: `/api/services/rest/bluesamservice/upload`
+ Arguments:  
file  
(required, multipart/form-data): The file to upload.
+ Returns a boolean reflecting the status of the upload

### Load a data set (POST)
<a name="ba-load-data-set-post"></a>

After you use `createDataSet` to create the data set definition, you can load records that are associated with the uploaded file to a specific data set.
+ Supported methods: POST
+ Requires authentication and the ROLE\_ADMIN role.
+ Path: `/api/services/rest/bluesamservice/loadDataSet`
+ Arguments:  
name  
(required, string): the name of the data set.
+ Returns the status of the request and the loaded data set.

### Load a data set (GET)
<a name="ba-load-data-set-get"></a>
+ Supported methods: GET
+ Requires authentication and the ROLE\_ADMIN role.
+ Path: `/api/services/rest/bluesamservice/loadDataSet`
+ Arguments:  
listcatFileOrDatasetName  
(required, string): the name of the data set.  
datasetFile  
(required, string): the data set file name.
+ Returns the status of the request and the loaded data set.

### Load a data set from an Amazon S3 bucket
<a name="ba-load-data-set-s3"></a>

Loads a data set using a listcat file from an Amazon S3 bucket.
+ Supported methods: GET
+ Requires authentication and the ROLE\_ADMIN role.
+ Path: `/api/services/rest/bluesamservice/loadDataSetFromS3`
+ Arguments:  
listcatFileS3Location  
(required, string): the Amazon S3 location of the listcat file.  
datasetFileS3Location  
(required, string): the Amazon S3 location of the data set file.  
region  
(required, string): the Amazon S3 AWS Region where the files are stored.
+ Returns the newly created data set

Sample request:

```
/BAC/api/services/rest/bluesamservice/loadDataSetFromS3?region=us-east-1&listcatFileS3Location=s3://bucket-name/listcat.json&datasetFileS3Location=s3://bucket-name/dataset.DAT
```

### Export a data set to an Amazon S3 bucket
<a name="ba-export-data-set-s3"></a>

Exports a data set to the specified Amazon S3 bucket.
+ Supported methods: GET
+ Requires authentication and the ROLE\_ADMIN role.
+ Path: `/api/services/rest/bluesamservice/exportDataSetToS3`
+ Arguments:  
s3Location  
(required, string): the Amazon S3 location to export the data set to.  
datasetName   
(required, string): the name of the data set to export.  
region  
(required, string): the AWS Region of the Amazon S3 bucket.  
kmsKeyId  
(optional, string): the AWS KMS ID to be used for encryption of the exported data set to the Amazon S3 bucket.
+ Returns the exported data set

Sample request:

```
/BAC/api/services/rest/bluesamservice/exportDataSetToS3?region=eu-west-1&s3Location=s3://bucket-name/dump&datasetName=dataset
```

### Clear a data set
<a name="ba-clear-data-set"></a>

 Clears all records from a data set.
+ Supported methods: POST, GET
+ Requires authentication and the ROLE\_ADMIN role.
+ Path: `/api/services/rest/bluesamservice/clearDataSet`
+ Arguments:   
name  
(required, string): the name of the data set to clear. When using the GET method, the parameter name is `datasetName`.
+ Returns the status of the request.

### Delete a data set
<a name="ba-delete-data-set"></a>

Deletes the data set definition and records.
+ Supported methods: POST
+ Requires authentication and the ROLE\_ADMIN role.
+ Path: `/api/services/rest/bluesamservice/deleteDataSet`
+ Arguments:  
name  
(required, string): the name of the data set to delete.
+ Returns the status of the request and the deleted data set.

### Count data set records
<a name="ba-count-data-set-records"></a>

This endpoint returns the number of records associated with a data set.
+ Supported methods: POST
+ Requires authentication and the ROLE\_USER role.
+ Path: `/api/services/rest/bluesamservice/countRecords`
+ Arguments:  
name  
(required, string): the name of the data set.
+ Returns: the number of records

## Bulk data sets related endpoints
<a name="ba-endpoints-bac-bulk"></a>

Use the following endpoints to create or manage multiple data sets at once.

**Topics**
+ [Export data sets (GET)](#ba-export-data-sets-get)
+ [Export data sets (POST)](#ba-export-data-sets-post)
+ [Create multiple data sets](#ba-create-multiple-data-sets)
+ [List all data sets](#ba-list-all-data-sets)
+ [Direct list all data sets](#ba-direct-list-all-data-sets)
+ [Direct list all data sets by page](#ba-direct-list-all-data-sets-by-page)
+ [Stream data set](#ba-stream-data-sets)
+ [Delete all data sets](#ba-delete-all-data-sets)
+ [Get data set definitions from listcat file](#ba-get-definitions-listcat)
+ [Get data set definitions from uploaded list cat file](#ba-get-definitions-uploaded-listcat)
+ [Get a data set](#ba-get-data-set)
+ [Load listcat from JSON file](#ba-load-listcat)

### Export data sets (GET)
<a name="ba-export-data-sets-get"></a>
+ Supported methods: GET
+ Requires authentication and the ROLE\_ADMIN role.
+ Path: `/api/services/rest/bluesamservice/exportDataSet`
+ Arguments:  
datasetName  
(required, string): the name of the data set to export.   
datasetOutputFile  
(required, string): the path of the folder where you want to store the exported dataset on the server.  
rdw  
(required, boolean): whether you want the record descriptor word (RDW) to be part of the exported records. If the data set has fixed length records, the value of this parameter is ignored.
+ Returns the status of the request and the path to the file containing the exported data set (if any). If the dataset is null in the response, that means the system was not able to locate a data set with the given name.

### Export data sets (POST)
<a name="ba-export-data-sets-post"></a>
+ Supported methods: POST
+ Requires authentication and the ROLE\_USER role.
+ Path: `/api/services/rest/bluesamservice/exportDataSet`
+ Arguments:  
dumpParameters  
(required, BACReadParameters): Bluesam read parameters.
+ Returns the status of the exported data set.

### Create multiple data sets
<a name="ba-create-multiple-data-sets"></a>
+ Supported methods: POST
+ Requires authentication and the ROLE\_ADMIN role.
+ Path: `/api/services/rest/bluesamservice/createAllDataSets`
+ Arguments:
  + List of data sets  
name  
(required, string): the name of the data set.   
type  
(required, string): the data set type. Possible values are: `ESDS`, `KSDS`, `RRDS`.   
recordSize  
(optional, string) : Maximum size of each record of the data set.  
fixedLength  
(optional, boolean) : Indicates if the records length is fixed.  
compression  
(optional, boolean) : Indicates if the dataset is compressed.   
cacheEnable  
(optional, boolean) : Indicates if caching is enabled for the dataset.
+ Returns: the status of the request and the newly created data set.

### List all data sets
<a name="ba-list-all-data-sets"></a>
+ Supported methods: GET
+ Requires authentication and the ROLE\_USER role.
+ Path: `/api/services/rest/bluesamservice/listDataSet`
+ Arguments: None
+ Returns: the status of the request and the list of the data sets.

### Direct list all data sets
<a name="ba-direct-list-all-data-sets"></a>
+ Supported methods: GET
+ Requires authentication and the ROLE\_USER role.
+ Path: `/api/services/rest/bluesamservice/directListDataSet`
+ Arguments: None
+ Returns: the status of the request and the list of the data sets.

### Direct list all data sets by page
<a name="ba-direct-list-all-data-sets-by-page"></a>
+ Supported methods: GET
+ Requires authentication and the ROLE\_USER role.
+ Path: `/api/services/rest/bluesamservice/directListDataSetByPage`
+ Arguments:  
name  
(required, string): the name of the data set. Defaults to `%` (all data sets) if not specified.  
page  
(required, int): the page number (minimum 0).  
pageSize  
(required, int): the page size (minimum 1, maximum 500).
+ Returns: the status of the request and the list of the data sets.

### Stream data set
<a name="ba-stream-data-sets"></a>
+ Supported methods: GET
+ Requires authentication and the ROLE\_ADMIN role.
+ Path: `/api/services/rest/bluesamservice/streamDataset`
+ Arguments:  
datasetName  
(required, string): the name of the data set.
+ Returns: A stream of the requested data sets.

### Delete all data sets
<a name="ba-delete-all-data-sets"></a>
+ Supported methods: POST
+ Requires authentication and the ROLE\_ADMIN role.
+ Path: `/api/services/rest/bluesamservice/removeAll`
+ Arguments: None
+ Returns: a boolean that represents the status of the request.

### Get data set definitions from listcat file
<a name="ba-get-definitions-listcat"></a>
+ Supported methods: POST
+ Requires authentication and the ROLE\_ADMIN role.
+ Path: `/api/services/rest/bluesamservice/getDataSetsDefinitionFromListcat`
+ Arguments:   
paramFilePath  
(required, string): The path to the listcat file.
+ Returns: a list of data sets

### Get data set definitions from uploaded list cat file
<a name="ba-get-definitions-uploaded-listcat"></a>
+ Supported methods: POST
+ Requires authentication and the ROLE\_ADMIN role.
+ Path: `/api/services/rest/bluesamservice/getDataSetsDefinitionFromUploadedListcat`
+ Arguments: None
+ Returns: a list of data sets

### Get a data set
<a name="ba-get-data-set"></a>
+ Supported methods: GET
+ Requires authentication and the ROLE\_USER role.
+ Path: `/api/services/rest/bluesamservice/getDataSet`
+ Arguments:  
name  
(required, string): the name of the data set.
+ Returns the requested data set.

### Load listcat from JSON file
<a name="ba-load-listcat"></a>
+ Supported methods: GET
+ Requires authentication and the ROLE\_ADMIN role.
+ Path: `/api/services/rest/bluesamservice/loadListcatFromJsonFile`
+ Arguments:   
filePath  
(required, string): The path to the listcat file.
+ Returns: a list of data sets

## Records
<a name="ba-endpoints-bac-records"></a>

Use the following endpoints to create or manage records within a data set.

**Topics**
+ [Create a record](#ba-create-record)
+ [Read a data set](#ba-read-data-set)
+ [Delete a record](#ba-delete-record)
+ [Update a record](#ba-update-record)
+ [Save a record](#ba-save-record)
+ [Validate a record](#ba-validate-record)
+ [Get a record tree](#ba-get-record-tree)

### Create a record
<a name="ba-create-record"></a>

You can use this endpoint to create a new record.
+ Supported methods: POST
+ Requires authentication and the ROLE\_USER role.
+ Path: `/api/services/rest/crud/createRecord`
+ Arguments:  
dataset  
(required, DataSet): the data set object  
mask  
(required, mask): the mask object.
+ Returns the status of the request and the created record.

### Read a data set
<a name="ba-read-data-set"></a>

You can use this endpoint to read a data set.
+ Supported methods: POST
+ Requires authentication and the ROLE\_USER role.
+ Path: `/api/services/rest/crud/readDataSet`
+ Arguments:  
dataset  
(required, DataSet): the data set object.
+ Returns the status of the request and the data set with the records.

### Delete a record
<a name="ba-delete-record"></a>

You can use this endpoint to delete a record from a data set.
+ Supported methods: POST
+ Requires authentication and the ROLE\_USER role.
+ Path: `/api/services/rest/crud/deleteRecord`
+ Arguments:  
dataset  
(required, DataSet): the data set object  
record  
(required, Record): the record to delete
+ Returns the status of the deletion.

### Update a record
<a name="ba-update-record"></a>

You can use this endpoint to update a record associated with a data set.
+ Supported methods: POST
+ Requires authentication and the ROLE\_USER role.
+ Path: `/api/services/rest/crud/updateRecord`
+ Arguments:  
dataset  
(required, DataSet): the data set object  
record  
(required, Record): the record to update  
mask  
(optional, Mask): the mask object to apply during the update.
+ Returns the status of the request and the data set with the records.

### Save a record
<a name="ba-save-record"></a>

You can use this endpoint to save a record to a data set and using a mask.
+ Supported methods: POST
+ Requires authentication and the ROLE\_USER role.
+ Path: `/api/services/rest/crud/saveRecord`
+ Arguments:  
dataset  
(required, DataSet): the data set object  
record  
(required, Record): the record to save  
mask  
(optional, Mask): the mask object to apply during the save.
+ Returns the status of the request and the data set with the records.

### Validate a record
<a name="ba-validate-record"></a>

Use this endpoint to validate a record.
+ Supported methods: POST
+ Requires authentication and the ROLE\_USER role.
+ Path: `/api/services/rest/crud/validateRecord`
+ Arguments:  
dataset  
(required, DataSet): the data set object  
record  
(optional, Record): the record to validate.  
mask  
(optional, Mask): the mask object to apply during validation.
+ Returns the status of the request and the data set with the records.

### Get a record tree
<a name="ba-get-record-tree"></a>

Use this endpoint to get the hierarchical tree of a record.
+ Supported methods: POST
+ Requires authentication and the ROLE\_USER role.
+ Path: `/api/services/rest/crud/getRecordTree`
+ Arguments:  
dataset  
(required, DataSet): the data set object  
record  
(required, Record): the record to fetch  
mask  
(optional, Mask): the mask object.
+ Returns the status of the request and the hierarchical tree of the requested record.

## Masks
<a name="ba-endpoints-bac-masks"></a>

Use the following endpoints to load or apply masks to a data set.

**Topics**
+ [Load masks](#ba-load-mask)
+ [Apply mask](#ba-apply-mask)
+ [Apply mask filter](#ba-apply-mask-filter)

### Load masks
<a name="ba-load-mask"></a>

You can use this endpoint to retrieve all the masks that are associated with a specific data set.
+ Supported methods: POST
+ Requires authentication and the ROLE\_USER role.
+ Path: `/api/services/rest/crud/loadMasks`
+ Path variables:  
recordSize: .../loadMasks/{recordSize}  
(optional, numeric): the record size, filter loaded masks that match this record size
+ Arguments:  
dataset  
(required, DataSet): the data set object
+ Returns the status of the request and the list of the masks.

### Apply mask
<a name="ba-apply-mask"></a>

You can use this endpoint to apply a mask to a specific data set.
+ Supported methods: POST
+ Requires authentication and the ROLE\_USER role.
+ Path: `/api/services/rest/crud/applyMask`
+ Arguments:  
dataset  
(required, DataSet): the data set object  
mask  
(required, Mask): the data set object
+ Returns the status of the request and the data set with the applied mask.

### Apply mask filter
<a name="ba-apply-mask-filter"></a>

You can use this endpoint to apply a mask and a filter to a specific data set.
+ Supported methods: POST
+ Requires authentication and the ROLE\_USER role.
+ Path: `/api/services/rest/crud/applyMaskFilter`
+ Arguments:  
dataset  
(required, DataSet): the data set object  
mask  
(required, Mask): the mask object  
filter  
(required, Filter): the filter object to apply.
+ Returns the status of the request and the data set with the applied mask and filter.

## Other
<a name="ba-endpoints-bac-other"></a>

Use the following endpoints to manage cache for a data set or check data set characteristics

**Topics**
+ [Check warm up cache](#ba-check-warm-up-cache)
+ [Check cache enabled](#ba-check-cache-enabled)
+ [Enable cache](#ba-enable-cache)
+ [Check allocated RAM cache](#ba-check-allocated-ram-cache)
+ [Check persistence](#ba-check-persistence)
+ [Check supported data set types](#ba-check-supported-data-set-types)
+ [Check server health](#ba-check-server-health)
+ [Check PostgreSQL multi-schema configuration](#ba-check-postgres-multi-schema)

### Check warm up cache
<a name="ba-check-warm-up-cache"></a>

Checks if the warmup cache is enabled for a specific data set.
+ Supported methods: POST
+ Requires authentication and the ROLE\_ADMIN role.
+ Path: `/api/services/rest/bluesamservice/warmupCache`
+ Arguments:  
name  
(required, string): the name of the data set. 
+ Returns: true if the warm up cache is enabled and false otherwise.

### Check cache enabled
<a name="ba-check-cache-enabled"></a>

Checks if the cache is enabled for a specific data set.
+ Supported methods: GET
+ Requires authentication and the ROLE\_USER role.
+ Path: `/api/services/rest/bluesamservice/isEnableCache`
+ Arguments: None
+ Returns true if the caching is enabled.

### Enable cache
<a name="ba-enable-cache"></a>
+ Supported methods: POST
+ Requires authentication and the ROLE\_ADMIN and ROLE\_SUPER\_ADMIN roles.
+ Path: `/api/services/rest/bluesamservice/enableDisableCache/{enable}`
+ Arguments:   
enable  
(required, boolean): if set to true, it will enable caching.  
dataset  
(required, DataSet): the data set object.
+ Returns None

### Check allocated RAM cache
<a name="ba-check-allocated-ram-cache"></a>

You can use this endpoint to retrieve the allocated RAM cache memory.
+ Supported methods: GET
+ Requires authentication and the ROLE\_USER role.
+ Path: `/api/services/rest/bluesamservice/allocatedRamCache`
+ Arguments: None
+ Returns: the size of the memory as a string

### Check persistence
<a name="ba-check-persistence"></a>
+ Supported methods: GET
+ Requires authentication and the ROLE\_USER role.
+ Path: `/api/services/rest/bluesamservice/persistence`
+ Arguments: None
+ Returns: the persistence used as a string

### Check supported data set types
<a name="ba-check-supported-data-set-types"></a>
+ Supported methods: GET
+ Path: `/api/services/rest/bluesamservice/getDataSetTypes`
+ Requires authentication and the ROLE\_USER role.
+ Arguments: None
+ Returns: the list of supported data set types as a list of strings.

### Check server health
<a name="ba-check-server-health"></a>
+ Supported methods: GET
+ Path: `/api/services/rest/bluesamserver/serverIsUp`
+ Arguments: None
+ Returns: None. HTTP response status code 200 indicates that the server is up and running.

### Check PostgreSQL multi-schema configuration
<a name="ba-check-postgres-multi-schema"></a>

Checks whether the PostgreSQL multi-schema configuration is enabled.
+ Supported methods: GET
+ Requires authentication and the ROLE\_USER role.
+ Path: `/api/services/rest/bluesamservice/isPostgresMultiSchema`
+ Arguments: None
+ Returns: true if the PostgreSQL multi-schema configuration is enabled and false otherwise.

## BAC user-management endpoints
<a name="ba-endpoints-bac-users"></a>

Use the following endpoints to manage user interactions.

**Topics**
+ [Log a user in](#ba-log-user-in)
+ [Verify whether at least one user exists in the system](#ba-verify-at-least-one-user-exists)
+ [Record a new user](#ba-record-new-user)
+ [Get user info](#ba-user-info)
+ [List users](#ba-list-users)
+ [Delete a user](#ba-delete-user)
+ [Log the current user out](#ba-log-user-out)

### Log a user in
<a name="ba-log-user-in"></a>
+ Supported method: POST
+ Path: `/api/services/security/servicelogin/login`
+ Arguments: None
+ Returns the JSON serialization of a `com.netfective.bluage.bac.entities.SignOn` object, representing the user whose credentials are provided in the current request. The password is hidden from the view in the returned object. The roles given to the used are being listed.

Sample response:

```
{
     "login": "some-admin",
     "password": null,
     "roles": [
       {
         "id": 0,
         "roleName": "ROLE_ADMIN"
       }
     ]
   }
```

### Verify whether at least one user exists in the system
<a name="ba-verify-at-least-one-user-exists"></a>
+ Supported method: GET
+ Path: `/api/services/security/servicelogin/hasAccount`
+ Arguments: None
+ Returns the boolean value `true` if at least one user other than the default super admin user has been created. Returns `false` otherwise.

### Record a new user
<a name="ba-record-new-user"></a>
+ Supported method: POST
+ Requires authentication and the ROLE\_ADMIN role.
+ Path: `/api/services/security/servicelogin/recorduser`
+ Arguments: the JSON serialization of a `com.netfective.bluage.bac.entities.SignOn` object that represents the user to be added to the storage. The roles for the user must be defined, otherwise the user might not be able to use the BAC facility and endpoints.
+ Returns the boolean value `true` if the user was successfully created. Returns `false` otherwise.
+ Sample request JSON:

  ```
   {
       "login": "simpleuser",
       "password": "simplepassword",
       "roles": [
         {
           "id": 2,
           "roleName": "ROLE_USER"
         }
       ]
     }
  ```

  The following are the two valid values for `roleName`: 
  + `ROLE_ADMIN`: can manage Blusam resources and users.
  + `ROLE_USER`: can manage Blusam resources but not users.

### Get user info
<a name="ba-user-info"></a>
+ Supported method: GET
+ Path: `/api/services/security/servicelogin/userInfo`
+ Arguments: None
+ Returns the username and role of the currently connected user

### List users
<a name="ba-list-users"></a>
+ Supported method: GET
+ Requires authentication and the ROLE\_ADMIN role.
+ Path: `/api/services/security/servicelogin/listusers`
+ Arguments: None
+ Returns a list of `com.netfective.bluage.bac.entities.SignOn`, serialized as JSON.

### Delete a user
<a name="ba-delete-user"></a>

**Important**  
This action cannot be undone. The deleted user won't be able to connect to the BAC application again.
+ Supported method: POST
+ Requires authentication and the ROLE\_ADMIN role.
+ Path: `/api/services/security/servicelogin/deleteuser`
+ Arguments: the JSON serialization of a `com.netfective.bluage.bac.entities.SignOn` object that represents the user to be removed from the storage.
+ Returns the boolean value `true` if the user was successfully removed.

### Log the current user out
<a name="ba-log-user-out"></a>
+ Supported method: GET
+ Path: `/api/services/security/servicelogout/logout`
+ Arguments: None
+ Returns the JSON message `{"success":true}` if the current user was successfully logged out. The related HTTP session will be invalidated.