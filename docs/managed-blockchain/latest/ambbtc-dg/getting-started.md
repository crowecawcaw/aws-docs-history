# Getting started with Amazon Managed Blockchain (AMB) Access Bitcoin

Use the step-by-step tutorials in this section to learn how to perform tasks by using
Amazon Managed Blockchain (AMB) Access Bitcoin. These examples require you to complete some prerequisites. If you are new to
AMB Access Bitcoin, review the _Setting up_ section of this guide to make sure you
have completed those prerequisites. For more information, see [Setting up Amazon Managed Blockchain (AMB) Access Bitcoin](bitcoin-setting-up.md "bitcoin-setting-up.md").

###### Topics

- [Create an IAM policy to access Bitcoin
  JSON-RPCs](#getting-started-next-steps "#getting-started-next-steps")
- [Make Bitcoin remote procedure call (RPC) requests on the AMB
  Access RPC editor using the AWS Management Console](#gs-console-bitcoin "#gs-console-bitcoin")
- [Make AMB Access Bitcoin JSON-RPC requests in awscurl by
  using the AWS CLI](#awscurl-bitcoin-rpc-requests "#awscurl-bitcoin-rpc-requests")
- [Make Bitcoin JSON-RPC requests in Node.js](#nodejs-bitcoin-rpc-requests "#nodejs-bitcoin-rpc-requests")
- [Use AMB Access Bitcoin over AWS PrivateLink](#bitcoin-rpc-requests-privatelink "#bitcoin-rpc-requests-privatelink")

## Create an IAM policy to access Bitcoin

JSON-RPCs

In order to access the public endpoints for the Bitcoin Mainnet and Testnet to make JSON-RPC
calls, you must have user credentials (AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY) that have
the appropriate IAM permissions for Amazon Managed Blockchain (AMB) Access Bitcoin. In a terminal with the AWS CLI installed,
run the following command to create an IAM Policy to access both Bitcoin endpoints:

```
cat <<EOT > ~/amb-btc-access-policy.json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid" : "`AMBBitcoinAccessPolicy`",
            "Effect": "Allow",
            "Action": [
                "managedblockchain:InvokeRpcBitcoin*"
            ],
            "Resource": "*"
        }
    ]
}
EOT
aws iam create-policy --policy-name AmazonManagedBlockchainBitcoinAccess --policy-document file://$HOME/amb-btc-access-policy.json

```

###### Note

The previous example gives you access to both the Bitcoin Mainnet and Testnet. To get access to a
specific endpoint, use the following `Action` command:

- `"managedblockchain:InvokeRpcBitcoinMainnet"`
- `"managedblockchain:InvokeRpcBitcoinTestnet"`

After you create the policy, attach that policy to your IAM user’s Role for it to take
effect. In the AWS Management Console, navigate to the IAM service, and attach the policy
`AmazonManagedBlockchainBitcoinAccess` to the Role assigned to your IAM user. For
more information, see [Creating a Role and assigning to an
IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md").

## Make Bitcoin remote procedure call (RPC) requests on the AMB

Access RPC editor using the AWS Management Console

You can edit and submit remote procedure calls (RPCs) on the AWS Management Console using AMB Access.
With these RPCs, you can read data, write, and submit transactions on the Bitcoin
network.

###### Example

The following example shows how to get information about the
_00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09_
`blockhash` by using `getBlock` RPC. Replace the highlighted variables
with your own inputs or choose one of the other **RPC methods** listed and
enter the relevant inputs required.

1. Open the Managed Blockchain console at [https://console.aws.amazon.com/managedblockchain/](https://console.aws.amazon.com/managedblockchain/ "https://console.aws.amazon.com/managedblockchain/").
2. Choose **RPC editor**.
3. In the **Request** section, choose `BITCOIN_MAINNET` as the
   **Blockchain Network**.
4. Choose `getblock` as the **RPC method**.
5. Enter `00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09`
   as the **Block number** and choose `0` as the
   **verbosity**.
6. Then, choose **Submit RPC**.
7. You will get results in the **Response** section of this page. You can then
   copy the full raw transactions for further analysis or to use in business logic for your
   applications.

For more information, see the [RPCs supported by AMB Access Bitcoin](bitcoin-api.md "bitcoin-api.md")

## Make AMB Access Bitcoin JSON-RPC requests in awscurl by

using the AWS CLI

###### Example

Sign requests with your IAM user credentials by using [Signature Version 4 (SigV4)](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") in
order to make Bitcoin JSON-RPC calls to the AMB Access Bitcoin endpoints. The [awscurl](https://github.com/okigan/awscurl "https://github.com/okigan/awscurl") command line tool can help you
sign requests to AWS services using SigV4. For more information, see the [awscurl README.md](https://github.com/okigan/awscurl#readme "https://github.com/okigan/awscurl#readme").

Install awscurl by using the method appropriate to your operating system. On macOS, HomeBrew
is the recommended application:

```
brew install awscurl
```

If you have already installed and configured the AWS CLI, your IAM user credentials and
default AWS Region are set in your environment and have access to awscurl. Using awscurl,
submit a request to both the Bitcoin _Mainnet_ and
_Testnet_ by invoking the `getblock` RPC. This call accepts
a string parameter corresponding to the block hash for which you want to retrieve
information.

The following command retrieves the block header data from the Bitcoin Mainnet by using
the block hash in the `params` array to select the specific block for which to
retrieve the headers. This example uses the `us-east-1` endpoint. You can replace
this with your preferred Bitcoin JSON-RPC and AWS Region that is supported by
Amazon Managed Blockchain (AMB) Access Bitcoin. Furthermore, you can make a request against the Testnet network, rather than
Mainnet, by replacing `mainnet` with `testnet` in the command.

```
awscurl -X POST -d '{ "jsonrpc": "1.0", "id": "`getblockheader-curltest`", "method": "`getblockheader`", "params": ["`0000000000000000000105bebab2f9dd16234a30950d38ec6ddc24d466e750a0`"] }' --service managedblockchain https://`mainnet`.bitcoin.managedblockchain.`us-east-1`.amazonaws.com  --region `us-east-1` -k
```

The results include details from the block headers and a list of transaction hashes included
in the requested block. See the following example:

```
{"result":{"hash":"0000000000000000000105bebab2f9dd16234a30950d38ec6ddc24d466e750a0",
      "confirmations":2,"height":799243,"version":664485888,"versionHex":"279b4000",
      "merkleroot":"568e79752e1921ecf40c961435abb41bc5700fe2833ecadc4abfc2f615ddc1b8",
      "time":1689684290,"mediantime":1689681317,"nonce":2091174943,"bits":"17053894",
      "difficulty":53911173001054.59,
      "chainwork":"00000000000000000000000000000000000000004f375cf72ff64e2404c1589c",
      "nTx":2135,
      "previousblockhash":"00000000000000000002ffe4efe07ae74ec8b92c7696f5e12b5da506f015ba6b",
      "nextblockhash":"000000000000000000038f05ddcf3f483fdcb74f4be606c022bcb673424fa4ca"},
      "error":null,"id":"curltest"}
```

## Make Bitcoin JSON-RPC requests in Node.js

You can submit signed requests by using HTTPS to access the Bitcoin
_Mainnet_ and _Testnet_ endpoints and to make JSON-RPC
API calls by using the [native https module in
Node.js](https://nodejs.org/api/https.html "https://nodejs.org/api/https.html"), or you can use a third-party library such as [AXIOS](https://axios-http.com "https://axios-http.com"). The following example shows you how to make a
Bitcoin JSON-RPC request to the AMB Access Bitcoin endpoints.

###### Example

To run this example Node.js script, apply the following prerequisites:

1. You must have node version manager (nvm) and Node.js installed on
   your machine. You can find installation instructions for your OS [here](https://github.com/nvm-sh/nvm "https://github.com/nvm-sh/nvm").
2. Use the `node --version` command and confirm that you are using _Node
   version 14_ or higher. If required, you can use the `nvm install
14` command, followed by the `nvm use 14` command, to install
   _version 14_.
3. The environment variables `AWS_ACCESS_KEY_ID` and
   `AWS_SECRET_ACCESS_KEY` must contain the credentials that are
   associated with your account. The environment variables `AMB_HTTP_ENDPOINT`
   must contain your AMB Access Bitcoin endpoints.

Export these variables as strings on your client by using the following commands. Replace
the highlighted values in the following strings with appropriate values from your IAM
user account.

```
export AWS_ACCESS_KEY_ID="`AKIAIOSFODNN7EXAMPLE`"
export AWS_SECRET_ACCESS_KEY="`wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`"
```

After you complete all prerequisites, copy the following `package.json` file and
`index.js` script into your local environment by using your editor:

_package.json_

```
{
  "name": "bitcoin-rpc",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "@aws-crypto/sha256-js": "^4.0.0",
    "@aws-sdk/credential-provider-node": "^3.360.0",
    "@aws-sdk/protocol-http": "^3.357.0",
    "@aws-sdk/signature-v4": "^3.357.0",
    "axios": "^1.4.0"
  }
}
```

_index.js_

```
const axios = require('axios');
const SHA256 = require('@aws-crypto/sha256-js').Sha256
const defaultProvider = require('@aws-sdk/credential-provider-node').defaultProvider
const HttpRequest = require('@aws-sdk/protocol-http').HttpRequest
const SignatureV4 = require('@aws-sdk/signature-v4').SignatureV4

// define a signer object with AWS service name, credentials, and region
const signer = new SignatureV4({
  credentials: defaultProvider(),
  service: 'managedblockchain',
  region: 'us-east-1',
  sha256: SHA256,
});


const rpcRequest = async () => {

  // create a remote procedure call (RPC) request object definig the method, input params
  let rpc = {
    jsonrpc: "1.0",
    id: "1001",
    method: 'getblock',
    params: ["00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09"]
  }

  //bitcoin endpoint
  let bitcoinURL = 'https://mainnet.bitcoin.managedblockchain.us-east-1.amazonaws.com/';

  // parse the URL into its component parts (e.g. host, path)
  const url = new URL(bitcoinURL);

  // create an HTTP Request object
  const req = new HttpRequest({
    hostname: url.hostname.toString(),
    path: url.pathname.toString(),
    body: JSON.stringify(rpc),
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Accept-Encoding': 'gzip',
      host: url.hostname,
    }
  });


  // use AWS SignatureV4 utility to sign the request, extract headers and body
  const signedRequest = await signer.sign(req, { signingDate: new Date() });

  try {
    //make the request using axios
    const response = await axios({...signedRequest, url: bitcoinURL, data: req.body})

    console.log(response.data)
  } catch (error) {
    console.error('Something went wrong: ', error)
    throw error
  }


}

rpcRequest();
```

The previous sample code uses Axios to make RPC requests to the Bitcoin endpoint, and it
signs those requests with the appropriate Signature Version 4 (SigV4) headers by using the
official AWS SDK v3 tools. To run the code, open a terminal in the same directory as your
files and run the following:

```
npm i
node index.js
```

The result that is generated will resemble the following:

```
{"hash":"00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09","
    confirmations":784126,"height":1000, "version":1,"versionHex":"00000001",
    "merkleroot":"fe28050b93faea61fa88c4c630f0e1f0a1c24d0082dd0e10d369e13212128f33",
    "time":1232346882,
    "mediantime":1232344831,"nonce":2595206198,"bits":"1d00ffff","difficulty":1,
    "chainwork":"000000000000000000000000000000000000000000000000000003e903e903e9",
    "nTx":1,
    "previousblockhash":"0000000008e647742775a230787d66fdf92c46a48c896bfbc85cdc8acc67e87d",
    "nextblockhash":"00000000a2887344f8db859e372e7e4bc26b23b9de340f725afbf2edb265b4c6",
    "strippedsize":216,"size":216,"weight":864,
    "tx":["fe28050b93faea61fa88c4c630f0e1f0a1c24d0082dd0e10d369e13212128f33"]},
    "error":null,"id":"1001"}
```

###### Note

The sample request in the previous script makes the `getblock` call with the same
input parameter block hash as the [Make AMB Access Bitcoin JSON-RPC requests in awscurl by
using the AWS CLI](#awscurl-bitcoin-rpc-requests "#awscurl-bitcoin-rpc-requests") example. To make other calls, modify the
`rpc` object in the script with a different Bitcoin JSON-RPC. You can change
the host property option to the Bitcoin `testnet` to make calls on that
endpoint.

## Use AMB Access Bitcoin over AWS PrivateLink

AWS PrivateLink is a highly available, scalable technology that you can use to connect your
VPC to services privately as if they were in your VPC. You do not have to use an internet
gateway, NAT device, public IP address, AWS Direct Connect connection, or AWS Site-to-Site
VPN connection to communicate with the service from your private subnets. For more information
about AWS PrivateLink or to set up AWS PrivateLink, see [What is AWS PrivateLink?](../../../vpc/latest/privatelink/what-is-privatelink.md "../../../vpc/latest/privatelink/what-is-privatelink.md")

You can send Bitcoin JSON-RPC requests to AMB Access Bitcoin over AWS PrivateLink by using a VPC
endpoint. Requests to this private endpoint aren't passed over the open internet, so you can
send requests directly to the Bitcoin endpoints by using the same _SigV4_
authentication. For more information, see [Access AWS services
through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md").

For the _Service name_, look for _Amazon Managed Blockchain_ in the _AWS
service_ column. For more information, see [AWS
services that integrate with AWS PrivateLink](../../../vpc/latest/privatelink/aws-services-privatelink-support.md "../../../vpc/latest/privatelink/aws-services-privatelink-support.md").
The service name for the endpoint will be in the following format:
`com.amazonaws.`AWS-REGION`.managedblockchain.bitcoin.`NETWORK-TYPE``.

For example:
`com.amazonaws.`us-east-1`.managedblockchain.bitcoin.`testnet``.
