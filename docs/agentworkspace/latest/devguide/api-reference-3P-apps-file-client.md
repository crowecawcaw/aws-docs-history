

# Connect Customer SDK File API

The Connect Customer SDK provides a `FileClient` which serves as an interface that you can use to make file requests to upload, retrieve, and delete attached files.

The `FileClient` constructor accepts a `ConnectClientConfig` argument, which is defined as:

```typescript
export type ConnectClientConfig =
    | AmazonConnectProvider
    | { context: ModuleContext; provider?: AmazonConnectProvider }
    | { provider: AmazonConnectProvider };
```

Pass the `provider` that `AmazonConnectApp.init` returns directly to the constructor:

```typescript
import { FileClient } from "@amazon-connect/file";

const fileClient = new FileClient(provider);
```

**Note**  
You must first instantiate the [ AmazonConnectApp](getting-started-initialize-sdk.md), which initializes the default AmazonConnectProvider and returns `{ provider }`.

**Note**  
Third-party applications must be configured with \* permission in order to utilize the FileClient APIs.

The following sections describe API calls for working with the File API.

**Topics**
+ [batchGetAttachedFileMetadata()](3P-apps-file-requests-batchgetattachedfilemetadata.md)
+ [completeAttachedFileUpload()](3P-apps-file-requests-completeattachedfileupload.md)
+ [deleteAttachedFile()](3P-apps-file-requests-deleteattachedfile.md)
+ [getAttachedFileUrl()](3P-apps-file-requests-getattachedfileurl.md)
+ [startAttachedFileUpload()](3P-apps-file-requests-startattachedfileupload.md)