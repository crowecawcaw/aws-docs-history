# Neptune Loader Get-Status Responses

The following example response from the Neptune Get-Status API describes the overall structure of the response,
explains the various fields and their data types, as well as the error handling and error log details.

## Neptune Loader Get-Status Response JSON layout

The general layout of a loader status response is as follows:

```
{
    "status" : "200 OK",
    "payload" : {
        "feedCount" : [
            {
                "LOAD_FAILED" : `number`
            }
        ],
        "overallStatus" : {
            "fullUri" : "s3://`bucket`/`key`",
            "runNumber" : `number`,
            "retryNumber" : `number`,
            "status" : "`string`",
            "totalTimeSpent" : `number`,
            "startTime" : `number`,
            "totalRecords" : `number`,
            "totalDuplicates" : `number`,
            "parsingErrors" : `number`,
            "datatypeMismatchErrors" : `number`,
            "insertErrors" : `number`,
        },
        "failedFeeds" : [
            {
                "fullUri" : "s3://`bucket`/`key`",
                "runNumber" : `number`,
                "retryNumber" : `number`,
                "status" : "`string`",
                "totalTimeSpent" : `number`,
                "startTime" : `number`,
                "totalRecords" : `number`,
                "totalDuplicates" : `number`,
                "parsingErrors" : `number`,
                "datatypeMismatchErrors" : `number`,
                "insertErrors" : `number`,
            }
        ],
        "errors" : {
            "startIndex" : `number`,
            "endIndex" : `number`,
            "loadId" : "`string`,
            "errorLogs" : [ ]
        }
    }
}
```

## Neptune Loader Get-Status

`overallStatus` and `failedFeeds` response objects

The possible responses returned for each failed feed, including the error
descriptions, are the same as for the `overallStatus` object in a `Get-Status`
response.

The following fields appear in the `overallStatus` object for all loads, and the
`failedFeeds` object for each failed feed:

- **`fullUri`**   –  
  The URI of the file or files to be loaded.

_Type:_ _string_

_Format_:
`s3://`bucket`/`key``.

- **`runNumber`**   –  
  The run number of this load or feed. This is incremented when the load is restarted.

_Type:_ _unsigned long_.

- **`retryNumber`**   –  
  The retry number of this load or feed. This is incremented when the loader automatically
  retries a feed or load.

_Type:_ _unsigned long_.

- **`status`**   –  
  The returned status of the load or feed. `LOAD_COMPLETED` indicates
  a successful load with no problems. For a list of other load-status messages, see [Neptune Loader Error and Feed Messages](loader-message.md "loader-message.md").

_Type:_ _string_.

- **`totalTimeSpent`**   –  
  The time, in seconds, spent to parse and insert data for the load or feed. This does
  not include the time spent fetching the list of source files.

_Type:_ _unsigned long_.

- **`totalRecords`**   –  
  Total records loaded or attempted to load.

_Type:_ _unsigned long_.

Note that when loading from a CSV file, the record count does not refer
to the number of lines loaded, but rather to the number of individual
records in those lines. For example, take a tiny CSV file like this:

```
~id,~label,name,team
'P-1','Player','Stokes','England'
```

Neptune would consider this file to contain 3 records, namely:

```
P-1  label Player
P-1  name  Stokes
P-1  team  England
```

- **`totalDuplicates`**   –  
  The number of duplicate records encountered.

_Type:_ _unsigned long_.

As in the case of the `totalRecords` count, this value
contains the number of individual duplicate records in a CSV file, not
the number of duplicate lines. Take this small CSV file, for example:

```
~id,~label,name,team
P-2,Player,Kohli,India
P-2,Player,Kohli,India
```

The status returned after loading it would look like this,
reporting 6 total records, of which 3 are duplicates:

```
{
  "status": "200 OK",
  "payload": {
    "feedCount": [
      {
        "LOAD_COMPLETED": 1
      }
    ],
    "overallStatus": {
      "fullUri": "`(the URI of the CSV file)`",
      "runNumber": 1,
      "retryNumber": 0,
      "status": "LOAD_COMPLETED",
      "totalTimeSpent": 3,
      "startTime": 1662131463,
      "totalRecords": 6,
      "totalDuplicates": 3,
      "parsingErrors": 0,
      "datatypeMismatchErrors": 0,
      "insertErrors": 0
    }
  }
}
```

For openCypher loads, a duplicate is counted when:

    + The loader detects that a row in a node file has an ID
     without an ID space that is the same as another ID value without an ID
     space, either in another row or belonging to an existing node.
    + The loader detects that a row in a node file has an ID
     with an ID space that is the same as another ID value with ID space,
     either in another row or belonging to an existing node.

See [Special considerations for loading openCypher data](load-api-reference-load.md#load-api-reference-load-parameters-opencypher "load-api-reference-load.md#load-api-reference-load-parameters-opencypher").

- **`parsingErrors`**   –  
  The number of parsing errors encountered.

_Type:_ _unsigned long_.

- **`datatypeMismatchErrors`**   –  
  The number of records with a data type that did not match the given data.

_Type:_ _unsigned long_.

- **`insertErrors`**   –  
  The number of records that could not be inserted due to errors.

_Type:_ _unsigned long_.

## Neptune Loader Get-Status `errors` response object

Errors fall into the following categories:

- **`Error 400`**   –  
  An invalid `loadId` returns an HTTP `400` bad request error.
  The message describes the error.
- **`Error 500`**   –  
  A valid request that cannot be processed returns an HTTP `500` internal server
  error. The message describes the error.

See [Neptune Loader Error and Feed Messages](loader-message.md "loader-message.md")
for a list of the error and feed messages returned by the loader in case
of errors.

When an error occurs, a JSON `errors` object is returned in the
`BODY` of the response, with the following fields:

- **`startIndex`**   –  
  The index of the first included error.

_Type:_ _unsigned long_.

- **`endIndex`**   –  
  The index of the last included error.

_Type:_ _unsigned long_.

- **`loadId`**   –  
  The ID of the load. You can use this ID to print the errors for the load by setting
  the `errors` parameter to `TRUE`.

_Type:_ _string_.

- **`errorLogs`**   –  
  A list of the errors.

_Type:_ _list_.

## Neptune Loader Get-Status `errorLogs` response object

The `errorLogs` object under `errors` in the loader Get-Status
response contains an object describing each error using the following fields:

- **`errorCode`**   –  
  Identifies the nature of error.

It can take one of the following values:

    + `PARSING_ERROR`
    + `S3_ACCESS_DENIED_ERROR`
    + `FROM_OR_TO_VERTEX_ARE_MISSING`
    + `ID_ASSIGNED_TO_MULTIPLE_EDGES`
    + `SINGLE_CARDINALITY_VIOLATION`
    + `FILE_MODIFICATION_OR_DELETION_ERROR`
    + `OUT_OF_MEMORY_ERROR`
    + `INTERNAL_ERROR` (returned when the bulk loader
     cannot determine the type of the error).

- **`errorMessage`**   –  
  A message describing the error.

This can be a generic message associated with the error code or a specific
message containing details, for example about a missing from/to vertex or
about a parsing error.

- **`fileName`**   –  
  The name of the feed.
- **`recordNum`**   –  
  In the case of a parsing error, this is the record number in the file of the
  record that could not be parsed. It is set to zero if the record number is
  not applicable to the error, or if it could not be determined.

For example, the bulk loader would generate a parsing error if it encountered
a faulty row such as the following in an RDF `nquads` file:

```
<http://base#subject> |http://base#predicate> <http://base#true> .
```

As you can see, the second `http` in the row above should be preceded
by  `<`  rather than  `|` .
The resulting error object under `errorLogs` in a status response
would look like this:

```
{
    "errorCode" : "PARSING_ERROR",
    "errorMessage" : "Expected '<', found: |",
    "fileName" : "`s3://bucket/key`",
    "recordNum" : `12345`
},
```
