AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Blusam application console REST endpoints

In this section, you can learn about the Blusam application console, which is an API designed
to simplify the management of modernized VSAM datasets. Endpoints for the Blusam web application
use the root path `/bac`.

###### Topics

- [Data sets related endpoints](#ba-endpoints-bac-datasets "#ba-endpoints-bac-datasets")
- [Bulk data sets related endpoints](#ba-endpoints-bac-bulk "#ba-endpoints-bac-bulk")
- [Records](#ba-endpoints-bac-records "#ba-endpoints-bac-records")
- [Masks](#ba-endpoints-bac-masks "#ba-endpoints-bac-masks")
- [Other](#ba-endpoints-bac-other "#ba-endpoints-bac-other")
- [BAC user-management endpoints](#ba-endpoints-bac-users "#ba-endpoints-bac-users")

## Data sets related endpoints

Use the following endpoints to create or manage a specific data set.

###### Topics

- [Create a data set](#ba-create-data-set "#ba-create-data-set")
- [Upload a file](#ba-upload-file "#ba-upload-file")
- [Load a data set (POST)](#ba-load-data-set-post "#ba-load-data-set-post")
- [Load a data set (GET)](#ba-load-data-set-get "#ba-load-data-set-get")
- [Load a data set from an Amazon S3 bucket](#ba-load-data-set-s3 "#ba-load-data-set-s3")
- [Export a data set to an Amazon S3 bucket](#ba-export-data-set-s3 "#ba-export-data-set-s3")
- [Clear a data set](#ba-clear-data-set "#ba-clear-data-set")
- [Delete a data set](#ba-delete-data-set "#ba-delete-data-set")
- [Count data set records](#ba-count-data-set-records "#ba-count-data-set-records")

### Create a data set

You can use this endpoint to create a data set definition.

- Supported methods: POST
- Requires authentication and the ROLE_ADMIN role.
- Path: `/api/services/rest/bluesamservice/createDataSet`
- Arguments:

name

(required, string): the name of the data set.

type

(required, string): the data set type. Possible values are: `ESDS`,
`KSDS`, `RRDS`.

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

- Returns a JSON file representing the newly created data set.

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

You can use this endpoint to upload files to the server. The file is stored in a temporary
folder that corresponds to each specific user. Use this endpoint every time you need to upload a
file.

- Supported methods: POST
- Requires authentication and the ROLE_ADMIN role.
- Path: `/api/services/rest/bluesamservice/upload`
- Arguments:

file

(required, multipart/form-data): The file to upload.

- Returns a boolean reflecting the status of the upload

### Load a data set (POST)

After you use `createDataSet` to create the data set definition, you can load
records that are associated with the uploaded file to a specific data set.

- Supported methods: POST
- Requires authentication and the ROLE_ADMIN role.
- Path: `/api/services/rest/bluesamservice/loadDataSet`
- Arguments:

name

(required, string): the name of the data set.

- Returns the status of the request and the loaded data set.

### Load a data set (GET)

- Supported methods: GET
- Requires authentication and the ROLE_ADMIN role.
- Path: `/api/services/rest/bluesamservice/loadDataSet`
- Arguments:

name

(required, string): the name of the data set.

dataset file

(required, string): the data set file name.

- Returns the status of the request and the loaded data set.

### Load a data set from an Amazon S3 bucket

Loads a data set using a listcat file from an Amazon S3 bucket.

- Supported methods: GET
- Requires authentication and the ROLE_ADMIN role.
- Path: `/api/services/rest/bluesamservice/loadDataSetFromS3`
- Arguments:

listcatFileS3Location

(required, string): the Amazon S3 location of the listcat file.

datasetFileS3Location

(required, string): the Amazon S3 location of the data set file.

region

(required, string): the Amazon S3 AWS Region where the files are stored.

- Returns the newly created data set

Sample request:

```
`/BAC/api/services/rest/bluesamservice/loadDataSetFromS3?region=us-east-1&listcatFileS3Location=s3://bucket-name/listcat.json&datasetFileS3Location=s3://bucket-name/dataset.DAT`
```

### Export a data set to an Amazon S3 bucket

Exports a data set to the specified Amazon S3 bucket.

- Supported methods: GET
- Requires authentication and the ROLE_ADMIN role.
- Path: `/api/services/rest/bluesamservice/exportDataSetToS3`
- Arguments:

s3Location

(required, string): the Amazon S3 location to export the data set to.

datasetName

(required, string): the name of the data set to export.

region

(required, string): the AWS Region of the Amazon S3 bucket.

kmsKeyId

(optional, string): the AWS KMS ID to be used for encryption of the exported data set to
the Amazon S3 bucket.

- Returns the exported data set

Sample request:

```
`/BAC/api/services/rest/bluesamservice/exportDataSetToS3?region=eu-west-1&s3Location=s3://bucket-name/dump&datasetName=dataset`
```

### Clear a data set

Clears all records from a data set.

- Supported methods: POST, GET
- Requires authentication and the ROLE_ADMIN role.
- Path: `/api/services/rest/bluesamservice/clearDataSet`
- Arguments:

name

(required, string): the name of the data set to clear.

- Returns the status of the request.

### Delete a data set

Deletes the data set definition and records.

- Supported methods: POST
- Requires authentication and the ROLE_ADMIN role.
- Path: `/api/services/rest/bluesamservice/deleteDataSet`
- Arguments:

name

(required, string): the name of the data set to delete.

- Returns the status of the request and the deleted data set.

### Count data set records

This endpoint returns the number of records associated with a data set.

- Supported methods: POST
- Requires authentication and the ROLE_USER role.
- Path: `/api/services/rest/bluesamservice/countRecords`
- Arguments:

name

(required, string): the name of the data set.

- Returns: the number of records

## Bulk data sets related endpoints

Use the following endpoints to create or manage multiple data sets at once.

###### Topics

- [Export data sets (GET)](#ba-export-data-sets-get "#ba-export-data-sets-get")
- [Export data sets (POST)](#ba-export-data-sets-post "#ba-export-data-sets-post")
- [Create multiple data sets](#ba-create-multiple-data-sets "#ba-create-multiple-data-sets")
- [List all data sets](#ba-list-all-data-sets "#ba-list-all-data-sets")
- [Direct list all data sets](#ba-direct-list-all-data-sets "#ba-direct-list-all-data-sets")
- [Direct list all data sets by page](#ba-direct-list-all-data-sets-by-page "#ba-direct-list-all-data-sets-by-page")
- [Stream data set](#ba-stream-data-sets "#ba-stream-data-sets")
- [Delete all data sets](#ba-delete-all-data-sets "#ba-delete-all-data-sets")
- [Get data set definitions from listcat file](#ba-get-definitions-listcat "#ba-get-definitions-listcat")
- [Get data set definitions from uploaded
  list cat file](#ba-get-definitions-uploaded-listcat "#ba-get-definitions-uploaded-listcat")
- [Get a data set](#ba-get-data-set "#ba-get-data-set")
- [Load listcat from JSON file](#ba-load-listcat "#ba-load-listcat")

### Export data sets (GET)

- Supported methods: GET
- Requires authentication and the ROLE_USER role.
- Path: `/api/services/rest/bluesamservice/exportDataSet`
- Arguments:

datasetName

(required, string): the name of the data set to export.

datasetOutputFile

(required, string): the path of the folder where you want to store the exported
dataset on the server.

rdw

(required, boolean): whether you want the record descriptor word (RDW) to be part of
the exported records. If the data set has fixed length records, the value of this parameter
is ignored.

- Returns the status of the request and the path to the file containing the exported data
  set (if any). If the dataset is null in the response, that means the system was not able to
  locate a data set with the given name.

### Export data sets (POST)

- Supported methods: POST
- Requires authentication and the ROLE_USER role.
- Path: `/api/services/rest/bluesamservice/exportDataSet`
- Arguments:

dumpParameters

(required, BACReadParameters): Bluesam read parameters.

- Returns the status of the exported data set.

### Create multiple data sets

- Supported methods: POST
- Requires authentication and the ROLE_ADMIN role.
- Path: `/api/services/rest/bluesamservice/createAllDataSets`
- Arguments:
  - List of data sets

  name

  (required, string): the name of the data set.

  type

  (required, string): the data set type. Possible values are: `ESDS`,
  `KSDS`, `RRDS`.

  recordSize

  (optional, string) : Maximum size of each record of the data set.

  fixedLength

  (optional, boolean) : Indicates if the records length is fixed.

  compression

  (optional, boolean) : Indicates if the dataset is compressed.

  cacheEnable

  (optional, boolean) : Indicates if caching is enabled for the dataset.

- Returns: the status of the request and the newly created data set.

### List all data sets

- Supported methods: GET
- Requires authentication and the ROLE_USER role.
- Path: `/api/services/rest/bluesamservice/listDataSet`
- Arguments: None
- Returns: the status of the request and the list of the data sets.

### Direct list all data sets

- Supported methods: GET
- Requires authentication and the ROLE_USER role.
- Path: `/api/services/rest/bluesamservice/directListDataSet`
- Arguments: None
- Returns: the status of the request and the list of the data sets.

### Direct list all data sets by page

- Supported methods: GET
- Requires authentication and the ROLE_USER role.
- Path: `/api/services/rest/bluesamservice/directListDataSetByPage`
- Arguments:

datasetName

(required, string): the name of the data set.

pageNumber

(required, int): the page number.

pageSize

(required, int): the page size.

- Returns: the status of the request and the list of the data sets.

### Stream data set

- Supported methods: GET
- Requires authentication and the ROLE_ADMIN role.
- Path: `/api/services/rest/bluesamservice/streamDataset`
- Arguments:

datasetName

(required, string): the name of the data set.

- Returns: A stream of the requested data sets.

### Delete all data sets

- Supported methods: POST
- Requires authentication and the ROLE_ADMIN role.
- Path: `/api/services/rest/bluesamservice/removeAll`
- Arguments: None
- Returns: a boolean that represents the status of the request.

### Get data set definitions from listcat file

- Supported methods: POST
- Requires authentication and the ROLE_ADMIN role.
- Path:
  `/api/services/rest/bluesamservice/getDataSetsDefinitionFromListcat`
- Arguments:

paramFilePath

(required, string): The path to the listcat file.

- Returns: a list of data sets

### Get data set definitions from uploaded

list cat file

- Supported methods: POST
- Requires authentication and the ROLE_ADMIN role.
- Path:
  `/api/services/rest/bluesamservice/getDataSetsDefinitionFromUploadedListcat`
- Arguments: None
- Returns: a list of data sets

### Get a data set

- Supported methods: GET
- Requires authentication and the ROLE_USER role.
- Path: `/api/services/rest/bluesamservice/getDataSet`
- Arguments:

name

(required, string): the name of the data set.

- Returns the requested data set.

### Load listcat from JSON file

- Supported methods: GET
- Requires authentication and the ROLE_ADMIN role.
- Path: `/api/services/rest/bluesamservice/loadListcatFromJsonFile`
- Arguments:

filePath

(required, string): The path to the listcat file.

- Returns: a list of data sets

## Records

Use the following endpoints to create or manage records within a data set.

###### Topics

- [Create a record](#ba-create-record "#ba-create-record")
- [Read a data set](#ba-read-data-set "#ba-read-data-set")
- [Delete a record](#ba-delete-record "#ba-delete-record")
- [Update a record](#ba-update-record "#ba-update-record")
- [Save a record](#ba-save-record "#ba-save-record")
- [Validate a record](#ba-validate-record "#ba-validate-record")
- [Get a record tree](#ba-get-record-tree "#ba-get-record-tree")

### Create a record

You can use this endpoint to create a new record.

- Supported methods: POST
- Requires authentication and the ROLE_USER role.
- Path: `/api/services/rest/crud/createRecord`
- Arguments:

dataset

(required, DataSet): the data set object

mask

(required, mask): the mask object.

- Returns the status of the request and the created record.

### Read a data set

You can use this endpoint to read a data set.

- Supported methods: POST
- Requires authentication and the ROLE_USER role.
- Path: `/api/services/rest/crud/readDataSet`
- Arguments:

dataset

(required, DataSet): the data set object.

- Returns the status of the request and the data set with the records.

### Delete a record

You can use this endpoint to delete a record from a data set.

- Supported methods: POST
- Requires authentication and the ROLE_USER role.
- Path: `/api/services/rest/crud/deleteRecord`
- Arguments:

dataset

(required, DataSet): the data set object

record

(required, Record): the record to delete

- Returns the status of the deletion.

### Update a record

You can use this endpoint to update a record associated with a data set.

- Supported methods: POST
- Requires authentication and the ROLE_USER role.
- Path: `/api/services/rest/crud/updateRecord`
- Arguments:

dataset

(required, DataSet): the data set object

record

(required, Record): the record to update

- Returns the status of the request and the data set with the records.

### Save a record

You can use this endpoint to save a record to a data set and using a mask.

- Supported methods: POST
- Requires authentication and the ROLE_USER role.
- Path: `/api/services/rest/crud/saveRecord`
- Arguments:

dataset

(required, DataSet): the data set object

record

(required, Record): the record to save

- Returns the status of the request and the data set with the records.

### Validate a record

Use this endpoint to validate a record.

- Supported methods: POST
- Requires authentication and the ROLE_USER role.
- Path: `/api/services/rest/crud/validateRecord`
- Arguments:

dataset

(required, DataSet): the data set object

- Returns the status of the request and the data set with the records.

### Get a record tree

Use this endpoint to get the hierarchical tree of a record.

- Supported methods: POST
- Requires authentication and the ROLE_USER role.
- Path: `/api/services/rest/crud/getRecordTree`
- Arguments:

dataset

(required, DataSet): the data set object

record

(required, Record): the record to fetch

- Returns the status of the request and the hierarchical tree of the requested
  record.

## Masks

Use the following endpoints to load or apply masks to a data set.

###### Topics

- [Load masks](#ba-load-mask "#ba-load-mask")
- [Apply mask](#ba-apply-mask "#ba-apply-mask")
- [Apply mask filter](#ba-apply-mask-filter "#ba-apply-mask-filter")

### Load masks

You can use this endpoint to retrieve all the masks that are associated with a specific
data set.

- Supported methods: POST
- Requires authentication and the ROLE_USER role.
- Path: `/api/services/rest/crud/loadMasks`
- Path variables:

recordSize: .../loadMasks/{recordSize}

(optional, numeric): the record size, filter loaded masks that match this record
size

- Arguments:

dataset

(required, DataSet): the data set object

- Returns the status of the request and the list of the masks.

### Apply mask

You can use this endpoint to apply a mask to a specific data set.

- Supported methods: POST
- Requires authentication and the ROLE_USER role.
- Path: `/api/services/rest/crud/applyMask`
- Arguments:

dataset

(required, DataSet): the data set object

mask

(required, Mask): the data set object

- Returns the status of the request and the data set with the applied mask.

### Apply mask filter

You can use this endpoint to apply a mask and a filter to a specific data set.

- Supported methods: POST
- Requires authentication and the ROLE_USER role.
- Path: `/api/services/rest/crud/applyMaskFilter`
- Arguments:

dataset

(required, DataSet): the data set object

mask

(required, Mask): the data set object

- Returns the status of the request and the data set with the applied mask and
  filter.

## Other

Use the following endpoints to manage cache for a data set or check data set
characteristics

###### Topics

- [Check warm up cache](#ba-check-warm-up-cache "#ba-check-warm-up-cache")
- [Check cache enabled](#ba-check-cache-enabled "#ba-check-cache-enabled")
- [Enable cache](#ba-enable-cache "#ba-enable-cache")
- [Check allocated RAM cache](#ba-check-allocated-ram-cache "#ba-check-allocated-ram-cache")
- [Check persistence](#ba-check-persistence "#ba-check-persistence")
- [Check supported data set types](#ba-check-supported-data-set-types "#ba-check-supported-data-set-types")
- [Check server health](#ba-check-server-health "#ba-check-server-health")

### Check warm up cache

Checks if the warmup cache is enabled for a specific data set.

- Supported methods: POST
- Requires authentication and the ROLE_ADMIN role.
- Path: `/api/services/rest/bluesamservice/warmupCache`
- Arguments:

name

(required, string): the name of the data set.

- Returns: true if the warm up cache is enabled and false otherwise.

### Check cache enabled

Checks if the cache is enabled for a specific data set.

- Supported methods: GET
- Requires authentication and the ROLE_USER role.
- Path: `/api/services/rest/bluesamservice/isEnableCache`
- Arguments: None
- Returns true if the caching is enabled.

### Enable cache

- Supported methods: POST
- Requires authentication and the ROLE_ADMIN and ROLE_SUPER_ADMIN roles.
- Path: `/api/services/rest/bluesamservice/enableDisableCache/{enable}`
- Arguments:

enable

(required, boolean): if set to true, it will enable caching.

- Returns None

### Check allocated RAM cache

You can use this endpoint to retrieve the allocated RAM cache memory.

- Supported methods: GET
- Requires authentication and the ROLE_USER role.
- Path: `/api/services/rest/bluesamservice/allocatedRamCache`
- Arguments: None
- Returns: the size of the memory as a string

### Check persistence

- Supported methods: GET
- Requires authentication and the ROLE_USER role.
- Path: `/api/services/rest/bluesamservice/persistence`
- Arguments: None
- Returns: the persistence used as a string

### Check supported data set types

- Supported methods: GET
- Path: `/api/services/rest/bluesamservice/getDataSetTypes`
- Requires authentication and the ROLE_USER role.
- Arguments: None
- Returns: the list of supported data set types as a list of strings.

### Check server health

- Supported methods: GET
- Path: `/api/services/rest/bluesamserver/serverIsUp`
- Arguments: None
- Returns: None. HTTP response status code 200 indicates that the server is up and
  running.

## BAC user-management endpoints

Use the following endpoints to manage user interactions.

###### Topics

- [Log a user in](#ba-log-user-in "#ba-log-user-in")
- [Verify whether at least one user exists in
  the system](#ba-verify-at-least-one-user-exists "#ba-verify-at-least-one-user-exists")
- [Record a new user](#ba-record-new-user "#ba-record-new-user")
- [Get user info](#ba-user-info "#ba-user-info")
- [List users](#ba-list-users "#ba-list-users")
- [Delete a user](#ba-delete-user "#ba-delete-user")
- [Log the current user out](#ba-log-user-out "#ba-log-user-out")

### Log a user in

- Supported method: POST
- Path: `/api/services/security/servicelogin/login`
- Arguments: None
- Returns the JSON serialization of a
  `com.netfective.bluage.bac.entities.SignOn` object, representing the user whose
  credentials are provided in the current request. The password is hidden from the view in the
  returned object. The roles given to the used are being listed.

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

### Verify whether at least one user exists in

the system

- Supported method: GET
- Path: `/api/services/security/servicelogin/hasAccount`
- Arguments: None
- Returns the boolean value `true` if at least one user other than the default
  super admin user has been created. Returns `false` otherwise.

### Record a new user

- Supported method: POST
- Requires authentication and the ROLE_ADMIN role.
- Path: `/api/services/security/servicelogin/recorduser`
- Arguments: the JSON serialization of a
  `com.netfective.bluage.bac.entities.SignOn` object that represents the user to be
  added to the storage. The roles for the user must be defined, otherwise the user might not be
  able to use the BAC facility and endpoints.
- Returns the boolean value `true` if the user was successfully created. Returns
  `false` otherwise.
- Sample request JSON:

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

- Supported method: GET
- Path: `/api/services/security/servicelogin/userInfo`
- Arguments: None
- Returns the username and role of the currently connected user

### List users

- Supported method: GET
- Requires authentication and the ROLE_ADMIN role.
- Path: `/api/services/security/servicelogin/listusers`
- Arguments: None
- Returns a list of `com.netfective.bluage.bac.entities.SignOn`, serialized as
  JSON.

### Delete a user

###### Important

This action cannot be undone. The deleted user won't be able to connect to the BAC
application again.

- Supported method: POST
- Requires authentication and the ROLE_ADMIN role.
- Path: `/api/services/security/servicelogin/deleteuser`
- Arguments: the JSON serialization of a
  `com.netfective.bluage.bac.entities.SignOn` object that represents the user to be
  removed from the storage.
- Returns the boolean value `true` if the user was successfully removed.

### Log the current user out

- Supported method: GET
- Path: `/api/services/security/servicelogout/logout`
- Arguments: None
- Returns the JSON message `{"success":true}` if the current user was
  successfully logged out. The related HTTP session will be invalidated.
