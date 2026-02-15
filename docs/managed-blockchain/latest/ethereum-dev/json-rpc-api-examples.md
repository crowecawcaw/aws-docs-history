# Making JSON-RPC API calls to an Ethereum node in Amazon Managed Blockchain (AMB)

The following examples demonstrate ways to make Ethereum JSON-RPC API calls to an Ethereum node in Amazon Managed Blockchain (AMB).

###### Topics

- [Using Signature Version 4 to make JSON-RPC API calls to an Ethereum node](#json-rpc-api-sigv4-examples "#json-rpc-api-sigv4-examples")
- [Using token based access to make JSON-RPC API calls to an Ethereum node](#json-rpc-api-tba-examples "#json-rpc-api-tba-examples")

## Using Signature Version 4 to make JSON-RPC API calls to an Ethereum node

The following sections demonstrate ways to make JSON-RPC API calls to an Ethereum node on Amazon Managed Blockchain (AMB) using the Signature Version 4 signing process.

###### Important

The Signature Version 4 signing process requires the credentials that are associated with an
AWS account. Some examples in this section export these sensitive credentials to the
shell environment of the client. Only use these examples on a client that run in a
trusted context. Do not use these examples in an untrusted context, such as in a web
browser or mobile app. Never embed client credentials in user-facing applications. To
expose an Ethereum node in AMB Access to anonymous users visiting from trusted web domains,
you can set up a separate endpoint in [Amazon API Gateway](../../../apigateway/latest/developerguide/welcome.md "../../../apigateway/latest/developerguide/welcome.md") that's backed by
a Lambda function that forwards requests to your node using the proper IAM
credentials.

###### Topics

- [Endpoint format for making JSON-RPC API calls over
  WebSocket and HTTP connections using Signature Version 4](#json-rpc-sigv4-api-endpoints "#json-rpc-sigv4-api-endpoints")
- [Using web3.js to make JSON-RPC API calls](#json-rpc-web3-sigv4-examples "#json-rpc-web3-sigv4-examples")
- [Making JSON-RPC API call
  using AWS SDK for JavaScript with a WebSocket connection to an Ethereum node in Amazon Managed Blockchain (AMB)](#json-rpc-connect-to-node-websockets-awsjssdk "#json-rpc-connect-to-node-websockets-awsjssdk")
- [Making JSON-RPC API calls using awscurl over HTTP](#sigv4-connect-to-node-http "#sigv4-connect-to-node-http")

### Endpoint format for making JSON-RPC API calls over

WebSocket and HTTP connections using Signature Version 4

###### Example

An Ethereum node created using AMB Access Ethereum hosts one endpoint for WebSocket connections and another for HTTP connections. These endpoints conform to the following patterns.

###### Note

The node ID is case sensitive and must be lowercase where indicated, or a signature mismatch
error occurs.

**WebSocket endpoint format**

```
wss://`your-node-id-lowercase`.wss.ethereum.managedblockchain.`us-east-1`.amazonaws.com/
```

For example:
`wss://nd-6eaj5va43jggnpxouzp7y47e4y.wss.ethereum.managedblockchain.us-east-1.amazonaws.com/`

**HTTP endpoint format**

```
https://`your-node-id-lowercase`.ethereum.managedblockchain.`us-east-1`.amazonaws.com/
```

For example, `https://nd-6eaj5va43jggnpxouzp7y47e4y.ethereum.managedblockchain.us-east-1.amazonaws.com/`

### Using web3.js to make JSON-RPC API calls

[Web3.js](https://web3js.readthedocs.io/en/v1.3.0/ "https://web3js.readthedocs.io/en/v1.3.0/") is a popular
collection of JavaScript libraries available using the Node package manager (npm). You can
run the following examples to send a JSON-RPC API call to Ethereum using a Javascript file
for Node.js. The examples demonstrate an HTTP connection and a WebSocket connection to an
Ethereum node.

Both HTTP and WebSocket connection types rely on a local connection provider library
to open the Signature Version 4 authenticated connection to the Ethereum node. You install
the provider for the connection locally by copying the source code to a file on your
client. Then, reference the library files in the script that makes the Ethereum API
call.

#### Prerequisites

###### Example

Running the example scripts requires the following prerequisites. Prerequisites for both HTTP and WebSocket connections are included.

1. You must have node version manager (nvm) and Node.js installed on your machine. If
   you use an Amazon EC2 instance as your Ethereum client, see [Tutorial: Setting Up Node.js on an Amazon EC2 Instance](../../../sdk-for-javascript/v2/developer-guide/setting-up-node-on-ec2-instance.md "../../../sdk-for-javascript/v2/developer-guide/setting-up-node-on-ec2-instance.md") for more
   information.
2. Type `node --version` and verify that you are using Node version 14 or later. If
   necessary, you can use the `nvm install 14` command followed by the
   `nvm use 14` command to install version 14.
3. The environment variables `AWS_ACCESS_KEY_ID` and
   `AWS_SECRET_ACCESS_KEY` must contain the credentials that are
   associated with the same AWS account that created the node. The environment
   variables `AMB_HTTP_ENDPOINT` and `AMB_WS_ENDPOINT` must
   contain your Ethereum node's HTTP and WebSocket endpoints respectively.

Export these variables as strings on your client using the following commands.
Replace the values with appropriate values from your IAM user account.

```
export AWS_ACCESS_KEY_ID="`AKIAIOSFODNN7EXAMPLE`"
```

```
export AWS_SECRET_ACCESS_KEY="`wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`"
```

```
export AMB_HTTP_ENDPOINT="https://`nd-6eaj5va43jggnpxouzp7y47e4y`.ethereum.managedblockchain.us-east-1.amazonaws.com/"
```

```
export AMB_WS_ENDPOINT="wss://`nd-6eaj5va43jggnpxouzp7y47e4y`.wss.ethereum.managedblockchain.us-east-1.amazonaws.com/"
```

###### Example

###### To make an Ethereum API call using web3.js over HTTP to your Ethereum node in the AMB Access

1. This example script uses the ECMAScript (ES) module. Therefore, add
   the `"type": "module"` line to your `package.json` file.
   The example `package.json` snippet that follows shows the
   contents required to successfully run this example.

```
{
  "type": "module",
  "dependencies": {
 "@aws-crypto/sha256-js": "^4.0.0",
 "@aws-sdk/credential-providers": "^3.352.0",
 "@aws-sdk/fetch-http-handler": "^3.353.0",
 "@aws-sdk/protocol-http": "^3.347.0",
 "@aws-sdk/signature-v4": "^3.347.0",
 "@aws-sdk/types": "^3.347.0",
 "web3": "^1.10.0",
 "xhr2": "^0.2.1"
 }
}
```

2. Use node package manager (npm) to install the requisite
   dependencies.

```
npm install
```

3. Copy the contents of the example that follows, and then use your preferred text editor to save
   it to a file that's named `awsHttpSigV4-v2.js` on your client machine
   in the same directory where you run your script.

**Contents of awsHttpSigV4-v2.js**

```
/////////////////////////////////////////////////////
// Authored by Rafia Tapia
// Senior Blockchain Solutions Architect, AWS
// licensed under GNU Lesser General Public License
// https://github.com/ethereum/web3.js
/////////////////////////////////////////////////////
import HttpProvider from 'web3-providers-http';
import XHR2 from 'xhr2';
import { fromEnv} from '@aws-sdk/credential-providers';
import sigv4 from '@aws-sdk/signature-v4';
import http from '@aws-sdk/protocol-http';
import crypto from "@aws-crypto/sha256-js";
export default class AWSHttpSigV4_v2Provider extends HttpProvider {
  constructor(connectionStr) {
    super(connectionStr);
  }
  send(payload, callback) {
    const self = this;
    /* ******************** XHR2 *************************** */
    const request = new XHR2(); // eslint-disable-line
    request.timeout = self.timeout;
    request.open('POST', self.host, true);
    request.setRequestHeader('Content-Type', 'application/json');
    request.onreadystatechange = () => {
      if (request.readyState === 4 && request.timeout !== 1) {
        let result = request.responseText; // eslint-disable-line
        let error = null; // eslint-disable-line
        try {
          result = JSON.parse(result);
        } catch (jsonError) {
          let message;
          if (!!result && !!result.error && !!result.error.message) {
            message = `[aws-ethjs-provider-http] ${result.error.message}`;
          } else {
            message = `[aws-ethjs-provider-http] Invalid JSON RPC response from host provider ${self.host}: ` +
              `${JSON.stringify(result, null, 2)}`;
          }
          error = new Error(message);
        }
        self.connected = true;
        callback(error, result);
      }
    };
    request.ontimeout = () => {
      self.connected = false;
      callback(`[aws-ethjs-provider-http] CONNECTION TIMEOUT: http request timeout after ${self.timeout} ` +
        `ms. (i.e. your connect has timed out for whatever reason, check your provider).`, null);
    };
    /* ******************** END XHR2 *************************** */
    const strPayload = JSON.stringify(payload);
    const region = process.env.AWS_DEFAULT_REGION || 'us-east-1';
    try {
      const urlparser=new URL(self.host)
      let signerV4 = new sigv4.SignatureV4({ credentials: fromEnv(), region: region, service: "managedblockchain", sha256: crypto.Sha256 });
      let requestOptions={
        protocol:urlparser.protocol,
        hostname:urlparser.hostname,
        method: 'POST',
        body:strPayload,
        headers:{'host':urlparser.host},
        path:urlparser.pathname
      }
      const newReq = new http.HttpRequest(requestOptions);
      signerV4.sign(newReq,{signingDate:new Date(),}).then(signedHttpRequest => {
        request.setRequestHeader('authorization', signedHttpRequest.headers['authorization']);
        request.setRequestHeader('x-amz-date', signedHttpRequest.headers['x-amz-date']);
        request.setRequestHeader('x-amz-content-sha256', signedHttpRequest.headers['x-amz-content-sha256']);
        request.send(strPayload);
      }).catch(sigError => {
        console.log(sigError);
      });
    } catch (error) {
      callback(`[aws-ethjs-provider-http] CONNECTION ERROR: Couldn't connect to node '${self.host}': ` +
        `${JSON.stringify(error, null, 2)}`, null);
    }
  }
}
```

4. Copy the contents of the following example, and then use your preferred text editor to save it
   to a file that's named `web3-example-http.js` in the same directory where
   you saved the provider from the previous step. The example script runs the
   `getNodeInfo` Ethereum method. You can
   modify the script to include other methods and their parameters.

**Contents of web3-example-http.js**

```
import AWSHttpSigV4_v2Provider from './awsHttpSigV4-v2.js';
const endpoint = process.env.AMB_HTTP_ENDPOINT
const web3 = new Web3(new AWSHttpSigV4_v2Provider(endpoint));
web3.eth.getNodeInfo().then(console.log);
```

5. Run the script to call the Ethereum API method over HTTP on your Ethereum node.

```
node web3-example-http.js
```

The output is similar to the following.

```
Geth/v1.9.24-stable-cc05b050/linux-amd64/go1.15.5
```

###### To make an Ethereum API call using web3.js over WebSocket to your Ethereum node in the AMB Access

1. The following example `package.json` snippet that
   follows shows the _dependencies_ required to successfully run the example.

```
"@aws-sdk/credential-providers": "^3.352.0",
"@aws-sdk/fetch-http-handler": "^3.353.0",
"@aws-sdk/protocol-http": "^3.347.0",
"@aws-sdk/signature-v4": "^3.347.0",
"@aws-sdk/types": "^3.347.0",
"web3": "^1.10.0",
"websocket": "^1.0.34"1*"
```

2. Use node package manager (npm) to install the requisite
   dependencies.

```
npm install
```

3. Copy the contents of the example that follows, and then use a text editor of your choosing to
   save it to a file that's named `web3-example-ws.js` in the same
   directory on your client where you run your script.

**Contents of web3-example-ws.js**

```
// Authored by Rafia Tapia
// Senior Blockchain Solutions Architect, AWS
// licensed under GNU Lesser General Public License
// https://github.com/ethereum/web3.js
/////////////////////////////////////////////////////

import Web3 from 'web3';
import WebsocketProvider from 'web3-providers-ws';
import { fromEnv } from '@aws-sdk/credential-providers';
import sigv4 from '@aws-sdk/signature-v4';
import http from '@aws-sdk/protocol-http';
import crypto from "@aws-crypto/sha256-js";

const endpoint = process.env.AMB_WS_ENDPOINT
const region = process.env.AWS_DEFAULT_REGION || 'us-east-1';
const urlparser = new URL(endpoint);
let signerV4 = new sigv4.SignatureV4({ credentials: fromEnv(), region: region, service: "managedblockchain", sha256: crypto.Sha256 });
let reqOptions = {
    protocol: "HTTPS",
    hostname: urlparser.hostname,
    method: 'GET',
    body: "",
    headers: { 'host': urlparser.host },
    path: urlparser.pathname

};
const newReq = new http.HttpRequest(reqOptions);
signerV4.sign(newReq, { signingDate: new Date(), }).then(signedHttpRequest => {
    const options = {
        headers: {
            'Authorization': signedHttpRequest.headers['authorization'],
            "X-Amz-Date": signedHttpRequest.headers['x-amz-date'],
            "X-Amz-Content-Sha256": signedHttpRequest.headers['x-amz-content-sha256'],
            'host':signedHttpRequest.headers['host']
        }
    };
    const web3 = new Web3(new WebsocketProvider(endpoint, options));
    web3.eth.getNodeInfo().then(console.log).then(() => {
        web3.currentProvider.connection.close();
    });

}).catch(sigError => {
    console.log(sigError);
})
```

4. Run the script to call the Ethereum API method over WebSocket on your Ethereum node.

```
node web3-example-ws.js
```

The output is similar to following.

```
Geth/v1.9.24-stable-cc05b050/linux-amd64/go1.15.5
```

### Making JSON-RPC API call

using AWS SDK for JavaScript with a WebSocket connection to an Ethereum node in Amazon Managed Blockchain (AMB)

The following example uses a JavaScript file for Node.js to open a WebSocket
connection to the Ethereum node endpoint in AMB Access and sends an Ethereum JSON-RPC API
call.

Running the example script requires the following:

- Node.js is installed on your machine. If you are using an Amazon EC2 instance, see [Tutorial: Setting Up Node.js on an Amazon EC2 Instance](../../../sdk-for-javascript/v2/developer-guide/setting-up-node-on-ec2-instance.md "../../../sdk-for-javascript/v2/developer-guide/setting-up-node-on-ec2-instance.md").
- The following example `package.json` snippet that
  follows shows the _dependencies_ required to successfully run the example.

```
"@aws-sdk/credential-providers": "^3.352.0",
"@aws-sdk/fetch-http-handler": "^3.353.0",
"@aws-sdk/protocol-http": "^3.347.0",
"@aws-sdk/signature-v4": "^3.347.0",
"@aws-sdk/types": "^3.347.0",
"web3": "^1.10.0",
"websocket-client": "^1.0.0",
"ws": "^8.14.2"
```

- Use node package manager (npm) to install the requisite
  dependencies.

###### Example To make an Ethereum API call over WebSocket to your Ethereum node on AMB Access

1. Copy the contents of the following script and save it to a file on your machine (for example,
   `ws-ethereum-example.js`).

The example calls the Ethereum JSON-RPC method `eth_subscribe` along
with the `newHeads` parameter. You can replace this method and its
parameters with any method that's listed in [Supported JSON-RPC methods](supported-json-rpc.md "supported-json-rpc.md").

**Contents of ws-ethereum-example.js**

```
// Authored by Rafia Tapia
// Senior Blockchain Solutions Architect, AWS
// licensed under GNU Lesser General Public License
// https://github.com/ethereum/web3.js
/////////////////////////////////////////////////////

import Web3 from 'web3';
import { fromEnv } from '@aws-sdk/credential-providers';
import sigv4 from '@aws-sdk/signature-v4';
import http from '@aws-sdk/protocol-http';
import crypto from "@aws-crypto/sha256-js";
import WebSocket from 'ws';

const endpoint = process.env.AMB_WS_ENDPOINT
const region = process.env.AWS_DEFAULT_REGION || 'us-east-1';
const urlparser = new URL(endpoint);
let signerV4 = new sigv4.SignatureV4({ credentials: fromEnv(), region: region, service: "managedblockchain", sha256: crypto.Sha256 });
let reqOptions = {
    protocol: "HTTPS",
    hostname: urlparser.hostname,
    method: 'GET',
    body: "",
    headers: { 'host': urlparser.host },
    path: urlparser.pathname

};
const newReq = new http.HttpRequest(reqOptions);
signerV4.sign(newReq, { signingDate: new Date(), }).then(signedHttpRequest => {
    let payload = {
        jsonrpc: '2.0',
        method: '`eth_subscribe`',
        params: ["`newHeads`"],
        id: 67
    }
    const ws = new WebSocket(endpoint, { headers: signedHttpRequest.headers });
    ws.onopen = async () => {
        ws.send(JSON.stringify(payload));
        console.log('Sent request');
    }
    ws.onerror = (error) => {
        console.error(`WebSocket error: ${error.message}`)
    }
    ws.onmessage = (e) => {
        console.log(e.data)
    }
}).catch(sigError => {
    console.log(sigError);
})
```

2. Run the following command to call the Ethereum API method over WebSocket on your Ethereum
   node.

```
node ws-ethereum-example.js
```

The `eth_subscribe` method with the `newHeads` parameter
generates a notification each time a new header is appended to the chain. Output is
similar to the following example. The WebSocket connection remains open and
additional notifications appear until you cancel the command.

```
sent request
{"id":67,"jsonrpc":"2.0","result":"0xabcd123456789efg0h123ijk45l6m7n8"}
```

### Making JSON-RPC API calls using awscurl over HTTP

###### Example

The example that follows uses [awscurl](https://pypi.org/project/awscurl/0.6/ "https://pypi.org/project/awscurl/0.6/"), which sends a signed HTTP request based on the current credentials you have set for the AWS CLI. If you construct your own HTTP requests, see [Signing AWS requests with Signature Version 4](../../../general/latest/gr/sigv4_signing.md "../../../general/latest/gr/sigv4_signing.md") in the _AWS General Reference_.

Replace `your-node-id-lowercase` with the ID of a
node in your account (for example, `nd-6eaj5va43jggnpxouzp7y47e4y`). The example calls the
`web3_clientVersion` method, which takes an empty parameter block. You can
replace this method and its parameters with any method that's listed in [Supported JSON-RPC methods](supported-json-rpc.md "supported-json-rpc.md").

```
awscurl --service managedblockchain \
-X POST -d '{"jsonrpc": "2.0", "method": "web3_clientVersion", "params": [], "id": 67}' \
https://`your-node-id-lowercase`.ethereum.managedblockchain.us-east-1.amazonaws.com
```

The command returns output similar to the following.

```
{"jsonrpc":"2.0","id":67,"result":"Geth/v1.9.22-stable-c71a7e26/linux-amd64/go1.15.5"}
```

## Using token based access to make JSON-RPC API calls to an Ethereum node

You can use Accessor tokens to make Ethereum API calls to an Ethereum node as a convenient
alternative to the Signature Version 4 (SigV4) signing process. You must provide a `BILLING_TOKEN`
from one of the Accessor tokens that you create as a query parameter with the call. For more information on creating and managing Accessor tokens,
see the topic on [Using token based
access](ethereum-tokens.md "ethereum-tokens.md").

###### Important

- If you prioritize security and auditability over convenience, use the SigV4 signing
  process instead.
- You can access the Ethereum APIs using Signature Version 4 (SigV4) and token based access. However,
  if you choose to use token based access, then any security benefits that are provided by using
  SigV4 are negated.
- Never embed Accessor tokens in user-facing applications.

The following examples demonstrate ways to make Ethereum JSON-RPC API calls to an Ethereum node on Amazon Managed Blockchain (AMB)
using token based access.

###### Topics

- [Endpoint format for WebSocket and HTTP connections using token based access](#json-rpc-api-tba-endpoints "#json-rpc-api-tba-endpoints")
- [Using wscat to connect and JSON-RPC API calls to your Ethereum node over WebSocket connection using token based access](#json-rpc-api-tba-wscat "#json-rpc-api-tba-wscat")
- [Using awscurl to make JSON-RPC API calls to your Ethereum node over HTTP using token based access](#json-rpc-api-tba-curl "#json-rpc-api-tba-curl")

### Endpoint format for WebSocket and HTTP connections using token based access

###### Example

Each Ethereum node hosts one endpoint for WebSocket connections and another for HTTP connections.
For token based access, these endpoints conform to the following patterns:

###### Note

The node ID is case sensitive and must be lowercase where indicated, or a signature mismatch error occurs.

**WebSocket endpoint format**

```
wss://`your-node-id-lowercase`.wss.t.ethereum.managedblockchain.`us-east-1`.amazonaws.com?billingtoken=`your-billing-token`
```

For example, `nd-6eaj5va43jggnpxouzp7y47e4y.wss.t.ethereum.managedblockchain.us-east-1.amazonaws.com?billingtoken=n-MWY63ZJZU5HGNCMBQER7IN6OIU`

**HTTP endpoint format**

```
https://`your-node-id-lowercase`.t.ethereum.managedblockchain.`us-east-1`.amazonaws.com?billingtoken=`your-billing-token`
```

For example, `https://nd-6eaj5va43jggnpxouzp7y47e4y.t.ethereum.managedblockchain.us-east-1.amazonaws.com?billingtoken=n-MWY63ZJZU5HGNCMBQER7IN6OIU`

### Using wscat to connect and JSON-RPC API calls to your Ethereum node over WebSocket connection using token based access

###### Example

This section describes how you can use a third party utility, [wscat](https://www.npmjs.com/package/wscat "https://www.npmjs.com/package/wscat"), to connect to your node using a token.

After installing wscat, use the following command to open a WebSocket connection to your ethereum node.

```
wscat --connect wss://`your-node-id`.wss.t.ethereum.managedblockchain.us-east-1.amazonaws.com?billingtoken=`your-billing-token`
```

This opens an active WebSocket connection to your node as shown in the following example response:

```
Connected (press CTRL+C to quit)
>
```

JSON-RPC calls can now be executed as follows,

```
{"jsonrpc":"2.0","method":"`eth_blockNumber`","params":`[]`,"id": `1`}
```

A reply should arrive back with the same id.

```
> {"jsonrpc":"2.0","method":"`eth_blockNumber`","params":`[]`,"id": `1`}
< {"jsonrpc":"2.0","id":1,"result":"0x9798e5
```

For subscriptions, calls can be executed in the following format,

```
> {"jsonrpc":"2.0","method":"`eth_subscribe`","params":["`newHeads`"],"id": `1`}
< {"id":1,"jsonrpc":"2.0","result":"0x4742411a16a232389a5877d4184e57b9"}
```

You should continuously get subscription messages that correspond to new blocks
roughly every 15 seconds. To stop the messages, unsubscribe by using the subscription
ID from the initial response.

```
> {"jsonrpc":"2.0","method":"`eth_unsubscribe`","params":["`0x4742411a16a232389a5877d4184e57b9`"],"id": `1`}
< {"id":`1`,"jsonrpc":"2.0","result":true}
```

### Using awscurl to make JSON-RPC API calls to your Ethereum node over HTTP using token based access

###### Example

The following example uses [awscurl](https://pypi.org/project/awscurl/0.6/ "https://pypi.org/project/awscurl/0.6/"), which sends a signed HTTP request based on the credentials that you
set for the AWS CLI.

```
awscurl -X POST -d '{"jsonrpc":"2.0","method":"`eth_blockNumber`","params":`[]`,"id": `1`}' 'https://`your-node-id`.t.ethereum.managedblockchain.`us-east-1`.amazonaws.com?billingtoken=`your-billing-token`'
```

Example Reply (Contents may differ):

```
{"jsonrpc":"2.0","id":1,"result":"0x9798d2"}
```
