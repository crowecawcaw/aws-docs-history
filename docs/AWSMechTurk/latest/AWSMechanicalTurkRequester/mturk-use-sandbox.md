# Using the sandbox

Many requesters choose to test their Amazon Mechanical Turk (Mechanical Turk) tasks in the sandbox environment. The
sandbox is a mirror image of the _production_ marketplace and is a useful
way to test task interfaces and processes without spending money on worker rewards or fees. In
the sandbox environment, you can perform all of the same operations you can perform in the
production environment, such as creating HITs and retrieving results. This can be a great way
to test your task interface and confirm that the results you receive meet your needs.

Because the sandbox is a mirror of production environment, you need to complete account
setup a second time, as described in [Set up Amazon Mechanical Turk](SetUpMturk.md "SetUpMturk.md"). To enable easy switching between testing and
production, you can link to the same AWS account and use the same AWS credentials. To switch
to the sandbox environment, simply specify that you want the CLI or SDK to use the sandbox
endpoint (`https://mturk-requester-sandbox.us-east-1.amazonaws.com`).

## API calls using the CLI

When using the sandbox from the AWS CLI, you need to specify the sandbox endpoint with
each operation as shown in the following `GetAccountBalance` request.

```

aws mturk get-account-balance --endpoint https://mturk-requester-sandbox.us-east-1.amazonaws.com

```

This returns an available balance of _10000.00_, the default balance
in the sandbox.

## API calls using the Python SDK (boto3)

The Python AWS SDK, like all of the AWS SDKs, allows you to specify the endpoint when
you instantiate a Mechanical Turk client. The following example shows how you would create a client and
make a request using the `GetAccountBalance` operation.

```

import boto3

client = boto3.client(
    'mturk',
    endpoint_url='https://mturk-requester-sandbox.us-east-1.amazonaws.com'
)
print(client.get_account_balance()['AvailableBalance'])

```

This returns an available balance of _10000.00_, the default balance
in the sandbox.

## Testing HITs

To test your HITs in the sandbox, you can use the same operations described in [Creating HITs](mturk-creating-hits.md "mturk-creating-hits.md"),
provided you've configured the SDK or CLI to use the sandbox endpoint. When you create HITs
in the sandbox, they are published to [https://workersandbox.mturk.com](https://workersandbox.mturk.com "https://workersandbox.mturk.com") instead of the production marketplace. Since this
is a separate location and workers won't receive a reward for completing your tasks there,
you need to create an account and complete the tasks yourself, or have members of your team
assist, to fully test your HITs.

When HITs are completed in the sandbox environment, you can retrieve results using the
same operations as those described in the following sections of this guide.
