# Neptune Loader Get-Status Examples

The following examples showcase the usage of the Neptune loader's GET-Status API, which allows you to retrieve
information about the status of your data loads into the Amazon Neptune graph database. These examples cover three
main scenarios: retrieving the status of a specific load, listing the available load IDs, and requesting detailed
status information for a specific load.

## Example request for load status

The following is a request sent via HTTP `GET` using the
`curl` command.

```
curl -X GET 'https://`your-neptune-endpoint`:`port`/loader/`loadId (a UUID)`'
```

###### Example Response

```
{
    "status" : "200 OK",
    "payload" : {
        "feedCount" : [
            {
                "LOAD_FAILED" : 1
            }
        ],
        "overallStatus" : {
            "datatypeMismatchErrors" : 0,
            "fullUri" : "s3://`bucket`/`key`",
            "insertErrors" : 0,
            "parsingErrors" : 5,
            "retryNumber" : 0,
            "runNumber" : 1,
            "status" : "LOAD_FAILED",
            "totalDuplicates" : 0,
            "totalRecords" : 5,
            "totalTimeSpent" : 3.0
        }
    }
}
```

## Example request for loadIds

The following is a request sent via HTTP `GET` using the
`curl` command.

```
curl -X GET 'https://`your-neptune-endpoint`:`port`/loader?limit=3'
```

###### Example Response

```
{
    "status" : "200 OK",
    "payload" : {
         "loadIds" : [
            "a2c0ce44-a44b-4517-8cd4-1dc144a8e5b5",
            "09683a01-6f37-4774-bb1b-5620d87f1931",
            "58085eb8-ceb4-4029-a3dc-3840969826b9"
        ]
    }
}
```

## Example request for detailed status

The following is a request sent via HTTP `GET` using the
`curl` command.

```
curl -X GET 'https://`your-neptune-endpoint`:`port`/loader/`loadId (a UUID)`?details=true'
```

###### Example Response

```
{
    "status" : "200 OK",
    "payload" : {
        "failedFeeds" : [
            {
                "datatypeMismatchErrors" : 0,
                "fullUri" : "s3://`bucket`/`key`",
                "insertErrors" : 0,
                "parsingErrors" : 5,
                "retryNumber" : 0,
                "runNumber" : 1,
                "status" : "LOAD_FAILED",
                "totalDuplicates" : 0,
                "totalRecords" : 5,
                "totalTimeSpent" : 3.0
            }
        ],
        "feedCount" : [
            {
                "LOAD_FAILED" : 1
            }
        ],
        "overallStatus" : {
            "datatypeMismatchErrors" : 0,
            "fullUri" : "s3://`bucket`/`key`",
            "insertErrors" : 0,
            "parsingErrors" : 5,
            "retryNumber" : 0,
            "runNumber" : 1,
            "status" : "LOAD_FAILED",
            "totalDuplicates" : 0,
            "totalRecords" : 5,
            "totalTimeSpent" : 3.0
        }
    }
}
```
