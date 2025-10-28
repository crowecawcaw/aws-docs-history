# Amazon Connect Agent Workspace File API

The SDK provides a `FileClient` which serves as an interface that you can
use to make file requests to upload, retrieve, and delete attached files.

The `FileClient` accepts an optional constructor argument,
`ConnectClientConfig` which itself is defined as:

```

export type ConnectClientConfig = {
    context?: ModuleContext;
    provider?: AmazonConnectProvider;
};
```

If you do not provide a value for this config, then the client will default to using
the **AmazonConnectProvider** set in the global provider scope. You can
also manually configure this using **setGlobalProvider**.

You can instantiate the agent client as follows:

```

import { FileClient } from "@amazon-connect/file";

const fileClient = new FileClient();
```

###### Note

For the zero-arg constructor demonstrated above to work correctly, you must first
instantiate the [app](getting-started-initialize-sdk.md "getting-started-initialize-sdk.md") which will set up the default AmazonConnectProvider. This is the
recommended option.

Alternatively, providing a constructor argument:

```

import { FileClient } from "@amazon-connect/file";

const fileClient = new FileClient({
    context: sampleContext,
    provider: sampleProvider
});
```

The following sections describe API calls for working with the File API.

###### Contents

- [batchGetAttachedFileMetadata()](3p-apps-file-requests-batchgetattachedfilemetadata.md "3p-apps-file-requests-batchgetattachedfilemetadata.md")
- [completeAttachedFileUpload()](3p-apps-file-requests-completeattachedfileupload.md "3p-apps-file-requests-completeattachedfileupload.md")
- [deleteAttachedFile()](3p-apps-file-requests-deleteattachedfile.md "3p-apps-file-requests-deleteattachedfile.md")
- [getAttachedFileUrl()](3p-apps-file-requests-getattachedfileurl.md "3p-apps-file-requests-getattachedfileurl.md")
- [startAttachedFileUpload()](3p-apps-file-requests-startattachedfileupload.md "3p-apps-file-requests-startattachedfileupload.md")
