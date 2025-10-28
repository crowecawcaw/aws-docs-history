# Rendering live view using AWS DCV Web

Client

Amazon Bedrock AgentCore's live view is powered by **AWS DCV**.
Each browser session launches a dedicated DCV server that streams the browser interface and
enables real-time user interaction.

To render the live view, you must use the **AWS DCV Web
Client**, which supports interactive display within a browser. Authentication is
handled via **IAM SigV4-signed query parameters**, which must be
appended to the live view URL to authorize access.

The example SDK includes a lightweight **web server** that
hosts the DCV Web Client and connects to the live view, enabling an end-to-end interactive
experience out of the box.

If you want to directly integrate the live view experience into their own web
applications, they can embed the **DCV Web Client** and generate
the signed connection URL using the SDK's helper methods. This allows full customization of
the UI while leveraging Amazon Bedrock AgentCore's Browser Tool capabilities.

## Using Callbacks to Customize URL

Parameters

The DCV Web SDK supports custom callbacks that you can use to modify the URLs used
during authentication and session establishment. This feature enables advanced integration
scenarios, including the ability to append custom query parameters and add AWS Signature
Version 4 (SigV4) signed values to secure and authorize connections through external
systems.

### Customizing Authentication and connection

URL:`httpExtraSearchParamsCallback`

The `authenticate` method supports a callback parameter,
`httpExtraSearchParamsCallback`. Before initiating the request, you can use
this callback to inject custom query parameters into the authentication URL.

When establishing a WebSocket connection to the DCV server, you can use the
`httpExtraSearchParamsCallback` in the `connect` method to
customize the URL used.

Example:

### Example

The following shows a sample code:

```

async function startAndConnect() {
  const response = await fetch('/presigned-url');
  const { sessionId, presignedUrl: url } = await response.json();
  presignedUrl = url; // Set global variable

  dcv.setLogLevel(dcv.LogLevel.INFO);
  auth = dcv.authenticate(presignedUrl, {
    promptCredentials: onPromptCredentials,
    error: onError,
    success: (auth, result) => {
      const { sessionId, authToken } = result[0];
      connect(presignedUrl, sessionId, authToken);
    },
    httpExtraSearchParams: httpExtraSearchParamsCb
  });
}


function connect(serverUrl, sessionId, authToken) {
  dcv.connect({
    url: serverUrl,
    sessionId,
    authToken,
    divId: 'dcv-display',
    observers: {
      httpExtraSearchParams: httpExtraSearchParamsCb,
      displayLayout: displayLayoutCallbackCb,
    }
  })
    .then((conn) => {
      console.log('Connection established');
      connection = conn;
    })
    .catch((error) => {
      console.error('Connection failed:', error.message);
    });
}

function httpExtraSearchParamsCb(method, url, body) {
  const presignedUrl = getPresignedUrlForLiveViewEndpoint();
  const searchParams = new URL(presignedUrl).searchParams;

  return searchParams;
}

```

These callbacks offer fine-grained control over the URL and headers used by the SDK
during key stages of session negotiation and connection, supporting advanced use cases and
integration with existing security infrastructure.
