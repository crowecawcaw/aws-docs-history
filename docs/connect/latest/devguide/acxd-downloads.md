

# Downloads
<a name="acxd-downloads"></a>

Configure data exports one-time downloads and scheduled recurring exports.

**Topics**
+ [GetDownload](#acxd-downloads-getdownload)

## GetDownload
<a name="acxd-downloads-getdownload"></a>

Polls the status of an async download job. Returns a pre-signed URL when the download has completed.

### Input
<a name="acxd-downloads-getdownload-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| downloadIdentifier | string | Yes | 

### Output
<a name="acxd-downloads-getdownload-output"></a>

```
{
  "url": "https://s3.amazonaws.com/bucket/path/file.csv?X-Amz-Signature=..."
}
```

### Errors
<a name="acxd-downloads-getdownload-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

### Request Parameters
<a name="acxd-downloads-getdownload-request-parameters"></a>

#### downloadIdentifier
<a name="acxd-downloads-getdownload-request-parameters-downloadidentifier"></a>

Type: String

The download job ID to poll.