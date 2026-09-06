# Downloads

Configure data exports one-time downloads and scheduled recurring exports.

###### Contents

- [GetDownload](#acxd-downloads-getdownload "#acxd-downloads-getdownload")

## GetDownload

Polls the status of an async download job. Returns a pre-signed URL when the download has completed.

### Input

| Parameter            | Type   | Required |
| -------------------- | ------ | -------- |
| `downloadIdentifier` | string | Yes      |

### Output

```
{
  "url": "https://s3.amazonaws.com/bucket/path/file.csv?X-Amz-Signature=..."
}
```

### Errors

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

### Request Parameters

#### downloadIdentifier

Type: String

The download job ID to poll.
