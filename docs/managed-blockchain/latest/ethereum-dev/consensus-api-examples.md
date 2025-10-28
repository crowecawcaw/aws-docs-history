# Making Consensus API calls to an Ethereum node in Amazon Managed Blockchain (AMB)

The following examples demonstrate ways to make Ethereum Consensus API calls to an Ethereum node in Amazon Managed Blockchain (AMB).

###### Topics

- [Using Consensus API calls signed using Signature Version 4 to an
  Ethereum node](#consensus-api-sigv4-examples "#consensus-api-sigv4-examples")
- [Using token based access to make Consensus API calls
  to an Ethereum node](#consensus-api-tba-examples "#consensus-api-tba-examples")

## Using Consensus API calls signed using Signature Version 4 to an

Ethereum node

The following sections demonstrate ways to make Consensus API calls to an Ethereum node on Amazon Managed Blockchain (AMB) using the Signature Version 4 signing process.

###### Important

The Signature Version 4 signing process requires the credentials that are associated with an
AWS account. Some examples in this section export these sensitive credentials to the
shell environment of the client. Only use these examples on a client that run in a trusted
context. Do not use these examples in an untrusted context, such as in a web browser or
mobile app. Never embed client credentials in user-facing applications. To expose an
Ethereum node in AMB Access to anonymous users visiting from trusted web domains, you can set
up a separate endpoint in [Amazon API Gateway](../../../apigateway/latest/developerguide/welcome.md "../../../apigateway/latest/developerguide/welcome.md") that are backed by
a Lambda function that forwards requests to your node using the proper IAM
credentials.

###### Topics

- [Endpoint format for making Consensus API calls
  over HTTP](#consensus-sigv4-api-endpoints "#consensus-sigv4-api-endpoints")
- [Making Consensus API calls using AWS SDK for JavaScript over HTTP](#consensus-sigv4-connect-to-node-http-awsjssdk "#consensus-sigv4-connect-to-node-http-awsjssdk")
- [Using awscurl to make Consensus API calls over HTTP](#consensus-sigv4-connect-to-node-http "#consensus-sigv4-connect-to-node-http")

### Endpoint format for making Consensus API calls

over HTTP

An Ethereum node that's created using AMB Access Ethereum hosts one endpoint for HTTP
connections. This endpoint conforms to the following patterns.

###### Note

The node ID is case sensitive and must be lowercase where indicated, or a signature mismatch
error occurs.

**HTTP endpoint format**

```
https://`your-node-id-lowercase`.ethereum.managedblockchain.`us-east-1`.amazonaws.com/`<followed by HTTP path of the Consensus API>`
```

For example:
`https://`nd-6eaj5va43jggnpxouzp7y47e4y`.ethereum.managedblockchain.us-east-1.amazonaws.com/`eth/v1/beacon/genesis``

### Making Consensus API calls using AWS SDK for JavaScript over HTTP

The following example uses a JavaScript file for Node.js to make Consensus API calls by
sending HTTP requests to the Ethereum node endpoint in Amazon Managed Blockchain (AMB).

Running the example script requires the following:

- Node.js is installed on your machine. If you use an Amazon EC2 instance, see [Tutorial: Setting Up Node.js on an Amazon EC2 Instance](../../../sdk-for-javascript/v2/developer-guide/setting-up-node-on-ec2-instance.md "../../../sdk-for-javascript/v2/developer-guide/setting-up-node-on-ec2-instance.md").
- The Node package manager (npm) is used to install the AWS SDK for JavaScript. The script uses classes from
  these packages.

```
npm install aws-sdk
```

- The environment variables `AWS_ACCESS_KEY_ID` and
  `AWS_SECRET_ACCESS_KEY` must contain the credentials that are associated
  with the same account that created the node.

Otherwise, the alternative is that the ~/.aws/credentials file is
populated.

###### Example — Make a Consensus API call using AWS SDK for JavaScript with an HTTP connection to an Ethereum

node in Amazon Managed Blockchain (AMB)

1. Copy the contents of the script that follows and save it to a file on your machine (for
   example, `consensus-ethereum-example.js`).

**Contents of consensus-ethereum-example.js**

```
const AWS = require('aws-sdk');
const REGION = process.env.AWS_DEFAULT_REGION || '`us-east-1`';

async function signedManagedBlockchainRequest(endpoint, credentials, host) {
    const awsRequest = new AWS.HttpRequest(new AWS.Endpoint(endpoint), REGION);
    awsRequest.method = 'GET';
    awsRequest.headers['host'] = host;
    const signer = new AWS.Signers.V4(awsRequest, 'managedblockchain');
    signer.addAuthorization(credentials, new Date());

    return awsRequest
}

/**
 * Sends Consensus API requests to AMB Ethereum node.
 * @param {*} nodeId - Node ID
 * @param {*} consensusApi - Consensus API to invoke, such as "/eth/v1/beacon/genesis".
 * @param {*} credentials - AWS credentials.
 * @returns A promise with invocation result.
 */
async function sendRequest(nodeId, consensusApi, credentials) {
    const host = `${nodeId}.ethereum.managedblockchain.${REGION}.amazonaws.com`
    const endpoint = `https://${host}${consensusApi}`;
    request = await signedManagedBlockchainRequest(endpoint, credentials, host)
    const client = new AWS.HttpClient();
    return  await  new Promise((resolve, reject) => {
        client.handleRequest(request, null, response => {
            let data = []
            response.on('data', chunk => {
                data.push(chunk);
            });
            response.on('end', () => {
            var responseBody = Buffer.concat(data);
                resolve(responseBody.toString('utf8'))
            });
        })
    });
}

const nodeId = process.env.NODE_ID;
new AWS.CredentialProviderChain()
    .resolvePromise()
    .then(credentials => sendRequest(nodeId, '`/eth/v1/beacon/states/finalized/root`', credentials))
    .then(console.log)
    .catch(err => console.error('ERROR: ' + err))
```

2. Run the script to call the Consensus API method over HTTP on your Ethereum node.

```
NODE_ID=`nd-6eaj5va43jggnpxouzp7y47e4y` AWS_DEFAULT_REGION=us-east-1 node `consensus-ethereum-example.js`
```

### Using awscurl to make Consensus API calls over HTTP

The following example uses [awscurl](https://pypi.org/project/awscurl/0.6/ "https://pypi.org/project/awscurl/0.6/"), which sends a signed HTTP request based on the credentials that you
set for the AWS CLI. If you make your own HTTP requests, see [Signing AWS requests with Signature Version
4](../../../general/latest/gr/sigv4_signing.md "../../../general/latest/gr/sigv4_signing.md") in the _AWS General Reference_.

This example calls the `/eth/v1/beacon/genesis` method, which takes an
empty parameter block. You can replace this method and its parameters with any method
listed in [Supported
Consensus API methods](supported-consensus-apis.md "supported-consensus-apis.md"). Replace
`your-node-id-lowercase` with the ID of a node in
your account (for example, `nd-6eaj5va43jggnpxouzp7y47e4y`).

```
awscurl --service managedblockchain \
-X GET 'https://`your-node-id-lowercase`.ethereum.managedblockchain.us-east-1.amazonaws.com/`eth/v1/beacon/genesis`'
```

The command returns output similar to the following.

```
{"data":{"genesis_time":"1606824023","genesis_validators_root":"0x4b363db94e286120d76eb905340fdd4e54bfe9f06bf33ff6cf5ad27f511bfe95","genesis_fork_version":"0x00000000"}}
```

## Using token based access to make Consensus API calls

to an Ethereum node

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

The following examples demonstrate ways to make Ethereum Consensus API calls to an
Ethereum node on Amazon Managed Blockchain (AMB) using token based access.

###### Topics

- [Endpoint format for making Consensus API calls
  over HTTP using token based access](#consensus-tba-api-endpoints "#consensus-tba-api-endpoints")
- [Making Consensus API calls using AWS SDK for JavaScript over HTTP using token based access](#consensus-tba-connect-to-node-http-awsjssdk "#consensus-tba-connect-to-node-http-awsjssdk")
- [Using awscurl to make Consensus API calls over HTTP using
  token based access](#consensus-tba-connect-to-node-http "#consensus-tba-connect-to-node-http")

### Endpoint format for making Consensus API calls

over HTTP using token based access

An Ethereum node that's created using AMB Access Ethereum hosts one endpoint for HTTP
connections. This endpoint conforms to the following patterns.

###### Note

The node ID is case sensitive and must be lowercase where indicated, or a signature mismatch
error occurs.

**HTTP endpoint format**

```
https://`your-node-id-lowercase`.t.ethereum.managedblockchain.`us-east-1`.amazonaws.com/`<followed by HTTP path of the Consensus API>`?billingtoken=`your-billing-token`
```

For example:
`https://`nd-6eaj5va43jggnpxouzp7y47e4y`.t.ethereum.managedblockchain.us-east-1.amazonaws.com/`eth/v1/beacon/genesis`?billingtoken=`n-MWY63ZJZU5HGNCMBQER7IN6OIU``

### Making Consensus API calls using AWS SDK for JavaScript over HTTP using token based access

The following example uses a JavaScript file for Node.js to make Consensus API calls
using token based access by sending HTTP requests to the Ethereum node endpoint in Amazon Managed Blockchain (AMB).

Running the example script requires the following:

- Node.js is installed on your machine. If you use an Amazon EC2 instance, see [Tutorial: Setting Up Node.js on an Amazon EC2 Instance](../../../sdk-for-javascript/v2/developer-guide/setting-up-node-on-ec2-instance.md "../../../sdk-for-javascript/v2/developer-guide/setting-up-node-on-ec2-instance.md").
- The Node package manager (npm) is used to install the AWS SDK for JavaScript. The script uses classes from
  these packages.

```
npm install aws-sdk
```

- The environment variables `AWS_ACCESS_KEY_ID` and
  `AWS_SECRET_ACCESS_KEY` must contain the credentials that are associated
  with the same account that created the node.

Otherwise, the alternative is that the ~/.aws/credentials file is
populated.

###### Example — Make a Consensus API call using AWS SDK for JavaScript with an HTTP connection using token based access to an Ethereum

node in Amazon Managed Blockchain (AMB)

1. Copy the contents of the script that follows and save it to a file on your machine (for
   example, `consensus-ethereum-example.js`).

**Contents of consensus-ethereum-example.js**

```
const AWS = require('aws-sdk');
const REGION = process.env.AWS_DEFAULT_REGION || '`us-east-1`';

function getManagedBlockchainClient(){
    const endpoint = `https://managedblockchain.${REGION}.amazonaws.com`;
    const client = new AWS.ManagedBlockchain();
    client.setEndpoint(endpoint);
    return client;
}

async function getAccessTokenFromManagedBlockChain() {
    const client = getManagedBlockchainClient();
    const accessorType = { AccessorType : "BILLING_TOKEN"};
    const networkType = { NetworkType : "ETHEREUM_MAINNET"};
    const tokenResponse = await new Promise((resolve, reject) => {
        client.createAccessor( accessorType, networkType, (err, data) => {
            if (err) {
                console.error(err);
                reject(err.message);
            }
            else {
		resolve(data);
	    }
        });
    });
    return tokenResponse;
}

async function deleteAccessTokenFromManagedBlockChain(accessorId) {
    const client = getManagedBlockchainClient();
    const id = { AccessorId : accessorId };
    const tokenResponse = await new Promise((resolve, reject) => {
        client.deleteAccessor( id, (err, data) => {
            if (err) {
                console.error(err);
                reject(err.message);
            }
            else resolve(data);
        });
    });
}

function getManagedBlockchainRequest(endpoint, host) {

    const awsRequest = new AWS.HttpRequest(new AWS.Endpoint(endpoint), REGION);
    awsRequest.method = "GET";
    awsRequest.headers['host'] = host;
    awsRequest.headers['Content-Type'] = 'application/json'

    return awsRequest
}

/**
 * Sends Consensus API requests to AMB Ethereum node.
 * @param {*} nodeId - Node ID
 * @param {*} consensusApi - Consensus API to invoke, such as "/eth/v1/beacon/genesis".
 * @param {*} credentials - AWS credentials.
 * @returns A promise with invocation result.
 */
async function sendRequest(nodeId, consensusApi) {
    const token = await getAccessTokenFromManagedBlockChain();

    const host = `${nodeId}.t.ethereum.managedblockchain.${REGION}.amazonaws.com`;
    const endpoint = `https://${host}${consensusApi}?billingtoken=${token.BillingToken}`;
    request = getManagedBlockchainRequest(endpoint, host)
    const client = new AWS.HttpClient();

    const promise =  await  new Promise((resolve, reject) => {
        client.handleRequest(request, null, response => {
            let data = []
            response.on('data', chunk => {
                data.push(chunk);
            });
            response.on('end', () => {
            var responseBody = Buffer.concat(data);
                resolve(responseBody.toString('utf8'))
            });
        })
    });
    deleteAccessTokenFromManagedBlockChain(token.AccessorId);
    return promise;
}

const nodeId = process.env.NODE_ID;
new AWS.CredentialProviderChain()
    .resolvePromise()
    .then(() => sendRequest(nodeId, '`/eth/v1/beacon/states/finalized/root`'))
    .then(console.log)
    .catch(err => console.error('ERROR: ' + err))
```

2. Run the script to call the Consensus API method over HTTP on your Ethereum node.

```
NODE_ID=`nd-6eaj5va43jggnpxouzp7y47e4y` AWS_DEFAULT_REGION=us-east-1 node `consensus-ethereum-example.js`
```

### Using awscurl to make Consensus API calls over HTTP using

token based access

The following example uses [awscurl](https://pypi.org/project/awscurl/0.6/ "https://pypi.org/project/awscurl/0.6/"), which sends a signed HTTP request based on the credentials that you
set for the AWS CLI.

This example calls the `/eth/v1/beacon/genesis` method, which takes an
empty parameter block. You can replace this method and its parameters with any method
listed in [Supported
Consensus API methods](supported-consensus-apis.md "supported-consensus-apis.md"). Replace
`your-node-id-lowercase` with the ID of a node in
your account (for example, `nd-6eaj5va43jggnpxouzp7y47e4y`).

```
awscurl --service managedblockchain \
-X GET 'https://`your-node-id-lowercase`.t.ethereum.managedblockchain.us-east-1.amazonaws.com/`eth/v1/beacon/genesis`?billingtoken=`your-billing-token`'
```

The command returns output similar to the following.

```
{"data":{"root":"0x71ef3f7c2470a7564af6eb8232855b602401cc9acdfc02c9fdf699e643cf8ba4"}}
```
