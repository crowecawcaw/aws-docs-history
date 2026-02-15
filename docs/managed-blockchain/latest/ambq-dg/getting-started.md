# Getting started with Amazon Managed Blockchain (AMB) Query

Use the step-by-step tutorials in this section to learn how to perform tasks by using
Amazon Managed Blockchain (AMB) Query. These procedures requires some prerequisites. If you are new to AMB Query, you can
review the _Setting up_ section of this guide. For more information, see
[Setting up Amazon Managed Blockchain (AMB) Query](ambq-setting-up.md "ambq-setting-up.md").

###### Note

Some variables in these examples have been deliberately obfuscated. Replace them with valid ones of
your own before running these examples.

###### Topics

- [Create an IAM policy to access AMB Query API
  operations](#getting-started-iam-policy "#getting-started-iam-policy")
- [Make Amazon Managed Blockchain (AMB) Query API requests by using Go](#getting-started-go-example "#getting-started-go-example")
- [Make Amazon Managed Blockchain (AMB) Query API requests by using Node.js](#node-amb-query-requests "#node-amb-query-requests")
- [Make Amazon Managed Blockchain (AMB) Query API requests by using Python](#python-amb-query-requests "#python-amb-query-requests")
- [Use Amazon Managed Blockchain (AMB) Query on the AWS Management Console to run the GetTokenBalance operation](#query-console-gettokenbalance-example "#query-console-gettokenbalance-example")

## Create an IAM policy to access AMB Query API

operations

To make AMB Query API requests, you must use the user credentials (AWS_ACCESS_KEY_ID and
AWS_SECRET_ACCESS_KEY) that have the appropriate IAM permissions for Amazon Managed Blockchain (AMB) Query. In a
terminal with the AWS CLI installed, run the following command to create an IAM policy to
access AMB Query API operations:

```
cat <<EOT > ~/`amb-query-access-policy.json`
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid" : "`AMBQueryAccessPolicy`",
            "Effect": "Allow",
            "Action": [
                "managedblockchain-query:*"
            ],
            "Resource": "*"
        }
    ]
}
EOT
aws iam create-policy --policy-name AmazonManagedBlockchainQueryAccess --policy-document `file://$HOME/amb-query-access-policy.json`

```

After you create the policy, attach that policy to an IAM user’s Role for it to take
effect. In the AWS Management Console, navigate to the IAM service, and attach the policy
`AmazonManagedBlockchainQueryAccess` to the Role assigned to the IAM user that will
use the service. For more information, see [Creating a Role and assigning to an
IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md").

###### Note

AWS recommends that you give access to specific API operations rather than using the
wild-card `*`. For more information, see [Accessing
specific Amazon Managed Blockchain (AMB) Query API actions](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-access-ambquery-apis "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-access-ambquery-apis").

## Make Amazon Managed Blockchain (AMB) Query API requests by using Go

With Amazon Managed Blockchain (AMB) Query, you can build applications that depend on instant access to blockchain
data once it is confirmed on the blockchain, even if it has not yet reached
_finality_. AMB Query enables several use cases such as populating the
transaction history of a wallet, providing contextual information about a transaction based on
its transaction hash, or obtaining the balance of a native tokens as well as of ERC-721, ERC-1155,
and ERC-20 tokens.

The following examples are created in the Go language and use the AMB Query API
operations. For more information on Go, see the [Go
Documentation](https://go.dev/doc/ "https://go.dev/doc/"). For more information on the AMB Query
API, see the [Amazon Managed Blockchain (AMB) Query API
Reference Documentation](../AMBQ-APIReference/API_Operations.md "../AMBQ-APIReference/API_Operations.md").

The following examples use the `ListTransactions` and the
`GetTransaction` API actions to first get a list of all transactions for a given
externally owned address (EOA) on the Ethereum Mainnet, and then the next example retrieves the
transaction details for a single transaction from the list.

###### Example— Make the `ListTransactions` API action using Go

Copy the following code to a file named `listTransactions.go` in the
_ListTransactions_ directory.

```
package main

import (
    "fmt"
    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/managedblockchainquery"
    "time"
)

func main() {

    // Set up a session
    ambQuerySession := session.Must(session.NewSessionWithOptions(session.Options{
        Config: aws.Config{
            Region: aws.String("`us-east-1`"),
        },
    }))
    client := managedblockchainquery.New(ambQuerySession)

    // Inputs for ListTransactions API
    ownerAddress := "`0x00000bf26964af9d7eed9e03e53415d********`"
    network := managedblockchainquery.`QueryNetworkEthereumMainnet`
    sortOrder := managedblockchainquery.`SortOrderAscending`
    fromTime := time.`Date(1971, 1, 1, 1, 1, 1, 1, time.UTC)`
    toTime := `time.Now()`
    nonFinal := "`NONFINAL`"
    // Call ListTransactions API. Transactions that have reached finality are always returned
    listTransactionRequest, listTransactionResponse := client.ListTransactionsRequest(&managedblockchainquery.ListTransactionsInput{
        Address: &ownerAddress,
        Network: &network,
        Sort: &managedblockchainquery.ListTransactionsSort{
            SortOrder: &sortOrder,
        },
        FromBlockchainInstant: &managedblockchainquery.BlockchainInstant{
            Time: &fromTime,
        },
        ToBlockchainInstant: &managedblockchainquery.BlockchainInstant{
            Time: &toTime,
        },

        ConfirmationStatusFilter: &managedblockchainquery.ConfirmationStatusFilter{
            Include: []*string{&nonFinal},
          },
    })
    errors := listTransactionRequest.Send()

    if errors == nil {
        // handle API response
        fmt.Println(listTransactionResponse)
    } else {
        // handle API errors
        fmt.Println(errors)
    }
}
```

After you save the file, run the code by using the following command inside the
_ListTransactions_ directory: `go run
 listTransactions.go`.

The output that follows resembles the following:

```
{
  Transactions: [
    {
      ConfirmationStatus: "FINAL",
      Network: "ETHEREUM_MAINNET",
      TransactionHash: "0x12345ea404b45323c0cf458ac755ecc45985fbf2b18e2996af3c8e8693354321",
      TransactionTimestamp: 2020-06-01 01:59:11 +0000 UTC
    },
    {
      ConfirmationStatus: "FINAL",
      Network: "ETHEREUM_MAINNET",
      TransactionHash: "0x1234547c65675d867ebd2935bb7ebe0996e9ec8e432a579a4516c7113bf54321",
      TransactionTimestamp: 2021-09-01 20:06:59 +0000 UTC
    },
     {
      ConfirmationStatus: "NONFINAL",
      Network: "ETHEREUM_MAINNET",
      TransactionHash: "0x123459df7c1cd42336cd1c444cae0eb660ccf13ef3a159f05061232a24954321",
      TransactionTimestamp: 2024-01-23 17:10:11 +0000 UTC
    }
  ]
}
```

###### Example— Make the `GetTransaction` API action by using Go

This example uses a transaction hash from the previous output. Copy the following
code to a file named `GetTransaction.go` in the
_GetTransaction_ directory.

```
package main

import (
    "fmt"
    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/managedblockchainquery"
)

func main() {

    // Set up a session
    ambQuerySession := session.Must(session.NewSessionWithOptions(session.Options{
        Config: aws.Config{
            Region: aws.String("us-east-1"),
        },
    }))
    client := managedblockchainquery.New(ambQuerySession)

    // inputs for GetTransaction API
    transactionHash := "`0x123452695a82868950d9db8f64dfb2f6f0ad79284a6c461d115ede8930754321`"
    network := managedblockchainquery.`QueryNetworkEthereumMainnet`

    // Call GetTransaction API. This operation will return transaction details for all
    // transactions that are conﬁrmed on the blockchain, even if they have not
    // reached ﬁnality.
    getTransactionRequest, getTransactionResponse := client.GetTransactionRequest(&managedblockchainquery.`GetTransactionInput`{
        Network:         &network,
        TransactionHash: &transactionHash,
    })

    errors := getTransactionRequest.Send()
    if errors == nil {
        // handle API response
        fmt.Println(`getTransactionResponse`)
    } else {
        // handle API errors
        fmt.Println(errors)
    }
}
```

After you save the file, run the code by using the following command
inside the _GetTransaction_ directory: `go 
 run GetTransaction.go`.

The output that follows resembles the following:

```
{
  Transaction: {
    BlockHash: "0x000005c6a71d1afbc005a652b6ceca71cd516d97b0fc514c2a1d0f2ca3912345",
    BlockNumber: "11111111",
    CumulativeGasUsed: "5555555",
    EffectiveGasPrice: "44444444444",
    From: "0x9157f4de39ab4c657ad22b9f19997536********",
    GasUsed: "22222",
    Network: "ETHEREUM_MAINNET",
    NumberOfTransactions: 111,
    SignatureR: "0x99999894fd2df2d039b3555dab80df66753f84be475069dfaf6c6103********",
    SignatureS: "0x77777a101e7f37dd2dd0bf878b39080d5ecf3bf082c9bd4f40de783e********",
    SignatureV: 0,
    ConfirmationStatus: "FINAL",
    ExecutionStatus: "SUCCEEDED",
    To: "0x5555564f282bf135d62168c1e513280d********",
    TransactionHash: "0x123452695a82868950d9db8f64dfb2f6f0ad79284a6c461d115ede8930754321",
    TransactionIndex: 11,
    TransactionTimestamp: 2022-02-02 01:01:59 +0000 UTC
  }
}
```

The `GetTokenBalance` API provides a way for you to get the balance of
native tokens (ETH and BTC), which can be used to get the current balance of an
externally owned account (EOA) at a point in time.

###### Example— Use the `GetTokenBalance` API action to get the balance

of a native token in Go

In the following example, you use the `GetTokenBalance` API to get an address
Ether (ETH) balance on the Ethereum Mainnet. Copy the following code to a file named
`GetTokenBalanceEth.go` in the _GetTokenBalance_
directory.

```
package main

import (
    "fmt"
    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/managedblockchainquery"
)

func main() {
    // Set up a session
    ambQuerySession := session.Must(session.NewSessionWithOptions(session.Options{
        Config: aws.Config{
            Region: aws.String("us-east-1"),
        },
    }))
    client := managedblockchainquery.New(ambQuerySession)

    // inputs for GetTokenBalance API
    ownerAddress := "`0xBeE510AF9804F3B459C0419826b6f225********`"
    network := managedblockchainquery.`QueryNetworkEthereumMainnet`
    nativeTokenId  := "`eth`" //Ether on Ethereum mainnet

    // call GetTokenBalance API
    getTokenBalanceRequest, getTokenBalanceResponse := client.GetTokenBalanceRequest(&managedblockchainquery.`GetTokenBalanceInput`{
        TokenIdentifier: &managedblockchainquery.TokenIdentifier{
            Network:         &network,
            TokenId: &nativeTokenId,
        },
        OwnerIdentifier: &managedblockchainquery.OwnerIdentifier{
            Address: &ownerAddress,
        },
    })
    errors := getTokenBalanceRequest.Send()

    if errors == nil {
        // process API response
        fmt.Println(getTokenBalanceResponse)
    } else {
        // process API errors
        fmt.Println(errors)
    }
}
```

After you save the file, run the code by using the following command
inside the _GetTokenBalance_ directory: `go 
 run GetTokenBalanceEth.go`.

The output that follows resembles the following:

```
{
  AtBlockchainInstant: {
    Time: 2020-12-05 11:51:01 +0000 UTC
  },
  Balance: "4343260710",
  LastTransactionHash: "0x00000ce94398e56641888f94a7d586d51664eb9271bf2b3c48297a50a0711111",
  LastTransactionTime: 2023-03-14 18:33:59 +0000 UTC,
  OwnerIdentifier: {
    Address: "0x12345d31750D727E6A3a7B534255BADd********"
  },
  TokenIdentifier: {
    Network: "ETHEREUM_MAINNET",
    TokenId: "eth"
  }
}
```

## Make Amazon Managed Blockchain (AMB) Query API requests by using Node.js

To run these Node examples, the following prerequisites apply:

1. You must have node version manager (nvm) and Node.js installed on
   your machine. You can find installation instruction for your OS [here](https://github.com/nvm-sh/nvm "https://github.com/nvm-sh/nvm").
2. Use the `node --version` command and confirm that you are using _Node
   version 14_ or higher. If required, you can use the `nvm install
14` command, followed by the `nvm use 14` command to install
   _version 14_.
3. The environment variables `AWS_ACCESS_KEY_ID` and
   `AWS_SECRET_ACCESS_KEY` must contain the credentials that are associated with the
   account.

Export these variables as strings on your client by using the following commands. Replace
the highlighted values in the following with appropriate values from the IAM user
account.

```
export AWS_ACCESS_KEY_ID="`AKIAIOSFODNN7EXAMPLE`"
export AWS_SECRET_ACCESS_KEY="`wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`"
```

###### Note

- After you have completed all prerequisites, you can submit signed requests over HTTPS to
  access Amazon Managed Blockchain (AMB) Query API operations and make requests by using the [native https module in Node.js](https://nodejs.org/api/https.html "https://nodejs.org/api/https.html"), or
  you can use a third-party library such as [AXIOS](https://www.npmjs.com/package/axios "https://www.npmjs.com/package/axios") and retrieve data from
  AMB Query.
- These examples use a third-party HTTP client for Node.js, but you can also use the
  AWS JavaScript SDK to make requests to
  AMB Query.
- The following example shows you how to make AMB Query API requests by using Axios and the AWS
  SDK modules for SigV4.

Copy the following `package.json`
file into your local environment's working directory:

```
{
  "name": "`amb-query-examples`",
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

###### Example— Retrieve the historical token balance from a specific externally owned address

(EOA) by using AMB Query `GetTokenBalance` API

You can use the `GetTokenBalance` API to get the balance of various tokens
(for example, ERC20, ERC721, and ERC1155) and native coins (for example, ETH and BTC), which
you can use to get the current balance of an externally owned account (EOA) based on a
historical `timestamp` (Unix timestamp - seconds). In this example, you use the
[`GetTokenBalance`](../AMBQ-APIReference/GetTokenBalance.md "../AMBQ-APIReference/GetTokenBalance.md") API to get an address balance of an ERC20 token,
USDC, on the Ethereum Mainnet.

To test the `GetTokenBalance` API, copy the following code into a file named
`token-balance.js`, and save the file into the same working directory:

```
const axios = require('axios').default;
const SHA256 = require('@aws-crypto/sha256-js').Sha256
const defaultProvider = require('@aws-sdk/credential-provider-node').defaultProvider
const HttpRequest = require('@aws-sdk/protocol-http').HttpRequest
const SignatureV4 = require('@aws-sdk/signature-v4').SignatureV4

// define a signer object with AWS service name, credentials, and region
const signer = new SignatureV4({
  credentials: defaultProvider(),
  service: 'managedblockchain-query',
  region: '`us-east-1`',
  sha256: SHA256,
});

const queryRequest = async (path, data) => {
  //query endpoint
  let queryEndpoint = `https://managedblockchain-query.`us-east-1`.amazonaws.com/${path}`;

  // parse the URL into its component parts (e.g. host, path)
  const url = new URL(queryEndpoint);

  // create an HTTP Request object
  const req = new HttpRequest({
    hostname: url.hostname.toString(),
    path: url.pathname.toString(),
    body: JSON.stringify(data),
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
    const response = await axios({...signedRequest, url: queryEndpoint, data: data})

    console.log(response.data)
  } catch (error) {
    console.error('Something went wrong: ', error)
    throw error
  }


}


let methodArg = 'get-token-balance';

let dataArg = {
  " atBlockchainInstant": {
    "time": `1688071493`
  },
  "ownerIdentifier": {
      "address": "`0xf3B0073E3a7F747C7A38B36B805247B2********`" // externally owned address
  },
  "tokenIdentifier": {
      "contractAddress":"`0xA0b86991c6218b36c1d19D4a2e9Eb0cE********`", //USDC contract address
      "network":"ETHEREUM_MAINNET"
  }
}

//Run the query request.
queryRequest(methodArg, dataArg);

```

To run the code, open a terminal in the same directory as your files and run the following command:

```
npm i
node token-balance.js
```

This command runs the script, passing in the arguments defined in the code to request the ERC20
USDC balance of the EOA listed on the Ethereum Mainnet. The response is similar to the following:

```
 {
  atBlockchainInstant: { time: 1688076218 },
  balance: '140386693440144',
  lastUpdatedTime: { time: 1688074727 },
  ownerIdentifier: { address: '0xf3b0073e3a7f747c7a38b36b805247b2********' },
  tokenIdentifier: {
    contractAddress: '0xa0b86991c6218b36c1d19d4a2e9eb0ce********',
    network: 'ETHEREUM_MAINNET'
  }
```

## Make Amazon Managed Blockchain (AMB) Query API requests by using Python

To run these Python examples, the following prerequisites apply:

1. You must have Python installed on your machine. You can find installation instruction for your
   OS [here](https://wiki.python.org/moin/BeginnersGuide/Download "https://wiki.python.org/moin/BeginnersGuide/Download").
2. Install the [AWS SDK for Python (Boto3)](https://aws.amazon.com/sdk-for-python/ "https://aws.amazon.com/sdk-for-python/") .
3. Install the [AWS Command Line Interface](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") and run the command `aws configure` to
   set the variables for your `Access Key ID`, `Secret Access Key`, and
   `Region`.

After you have completed all prerequisites, you can use the AWS
SDK for Python over HTTPS to make Amazon Managed Blockchain (AMB) Query API requests.

The following Python example uses modules from boto3 to send requests affixed with the
required SigV4 headers to the AMB Query `ListTransactionEvents` API operation. This
example retrieves a list of events emitted by a given transaction on the Ethereum Mainnet.

Copy the following `list-transaction-events.py`
file into your local environment's working directory:

```
import json
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from botocore.session import Session
from botocore.httpsession import URLLib3Session

def signed_request(url, method,  params, service, region):

    session = Session()
    sigv4 = SigV4Auth(session.get_credentials(), service, region)
    data = json.dumps(params)
    request = AWSRequest(method, url, data=data)
    sigv4.add_auth(request)
    http_session = URLLib3Session()
    response = http_session.send(request.prepare())

    return(response)

url = 'https://managedblockchain-query.`us-east-1`.amazonaws.com/`list-transaction-events`'
method = 'POST'
params = {
'network': 'ETHEREUM_MAINNET',
'transactionHash': '0x125714bb4db48757007fff2671b37637bbfd6d47b3a4757ebbd0c5222984f905'
}
service = 'managedblockchain-query'
region = '`us-east-1`'

# Call the listTransactionEvents operation. This operation will return transaction details for
# all transactions that are conﬁrmed on the blockchain, even if they have not reached
# ﬁnality.
listTransactionEvents = signed_request(url, method, params, service, region)

print(json.loads(`listTransactionEvents`.content.decode('utf-8')))
```

To run the sample code to `ListTransactionEvents`, save the file in your
working directory and then run the command `python3 list-transaction-events.py`.
This command runs the script, passing in the arguments defined in the code to request the
events associated with the given transaction hash on the Ethereum Mainnet. The response is
similar to the following:

```
{
 'events':
 [
  {
      'contractAddress': '0x95ad61b0a150d79219dcf64e1e6cc01f********',
      'eventType': 'ERC20_TRANSFER',
      'from': '0xab5801a7d398351b8be11c439e05c5b3********',
      'network': 'ETHEREUM_MAINNET',
      'to': '0xdead0000000000000000420694206942********',
      'transactionHash': '0x125714bb4db48757007fff2671b37637bbfd6d47b3a4757ebbd0c522********',
      'value': '410241996771871894771826174755464'
  }
 ]
}
```

## Use Amazon Managed Blockchain (AMB) Query on the AWS Management Console to run the GetTokenBalance operation

The following example shows how to get a token's balance on the _Ethereum Mainnet_ using Amazon Managed Blockchain (AMB) Query on the AWS Management Console

###### Example

1. Open the Amazon Managed Blockchain console at [https://console.aws.amazon.com/managedblockchain/](https://console.aws.amazon.com/managedblockchain/ "https://console.aws.amazon.com/managedblockchain/").
2. Choose **Query editor** from the **Query** section.
3. Choose **ETHEREUM_MAINNET** as the **Blockchain network**.
4. Choose **GetTokenBalance** as the **Query type**.
5. Enter your **Blockchain address** for the token.
6. Enter the **Contract address** for the token.
7. Enter the optional **Token ID** for the token.
8. Choose the **At date** for the token balance.
9. Enter the optional **At time** for the token balance.
10. Choose **Run query**.
    AMB Query will run your query and you will see results in the **Query results** window.
