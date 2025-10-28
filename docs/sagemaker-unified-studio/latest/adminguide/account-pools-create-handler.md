# Create an account pool with a custom handler source

You can create an account pool where the account authentication is provided by a
custom Lambda handler. Use these steps to create a sample custom handler and provide
it when creating the account pool.

###### To create example custom Lambda handler

- Create a function in Lambda that provides authorization for Amazon SageMaker Unified Studio to use
  when authenticating accounts for the account pool.

The following example provides sample handler code for a python
function.

```
import json

def lambda_handler(event, context):
    print(f'Received Event {event}')
    if event['operationRequest']['listAuthorizedAccountsRequest'] is not None:
        print("ListAuthorizedAccountsRequest Received...")
        return list_authorized_accounts()
    elif event['operationRequest']['validateAccountAuthorizationRequest'] is not None:
        print("ValidateAccountAuthorizationRequest Received...")
        return validate_account_authorization()
    else:
        raise Exception(f'Operation type {operation_type} not supported')

def list_authorized_accounts():
    account1 = {"awsAccountId": "`111122223333`", "awsAccountName": "Acct1", "supportedRegions": ["us-east-1", "us-west-2", "eu-west-1"]}
    account2 = {"awsAccountId": "892325846722", "awsAccountName": "Acct2", "supportedRegions": ["us-east-1", "us-west-2", "us-east-2"]}
    return {
        'operationResponse': {
            'listAuthorizedAccountsResponse': {
                'items': [account1, account2]
            }
        }
    }

def validate_account_authorization():
    return {
        'operationResponse': {
            'validateAccountAuthorizationResponse': {
                'authResult': 'GRANT'
            }
        }
    }
```

After you create your account pool, you can create a project in your
domain that uses the account pool. For more information about associated accounts, see [Associated accounts in Amazon SageMaker Unified Studio](associated-accounts.md "associated-accounts.md").

###### To create an account pool with a custom handler source (CLI)

- Open a terminal (Linux, macOS, or Unix) or command prompt (Windows) and use the AWS CLI
  to run the `create-account-pool` command with the following
  format, where the following are required arguments:
  - `--domain-identifier` - the domain ID in SageMaker
    Unified Studio
  - `--name` - the account pool name
  - `--account-source` - the method for providing account
    information (custom handler or static list)
  - `--resolution-strategy` - the manual option is shown in
    this example
    domain ID, account pool name, and the Lambda handler ARN and IAM role ARN
    are required arguments.

```
aws datazone create-account-pool --domain-identifier `DOMAIN_ID` --name `ACCOUNT_POOL_ID` --resolution-strategy MANUAL --account-source <source>
```

Example command:

```
aws datazone create-account-pool --domain-identifier `dzd_dkqsou2EXAMPLE` --name my-accountpool --resolution-strategy MANUAL --account-source '{"customAccountPoolHandler": {"lambdaFunctionArn": "arn:aws:lambda:us-east-1:`111122223333`:function:MyAccountPoolResolver", "lambdaExecutionRoleArn": "arn:aws:iam::`111122223333`:role/AccountResolutionRole"}}'
```

This command returns output with the account pool details.

```
{
    "domainId": "`dzd_dkqsou2EXAMPLE`",
    "name": "my-accountpool",
    "id": "`cln5qjqEXAMPLE`",
    "resolutionStrategy": "MANUAL",
    "accountSource": {
        "customAccountPoolHandler": {
            "lambdaFunctionArn": "arn:aws:lambda:us-east-1:`111122223333`:function:MyAccountPoolResolver",
            "lambdaExecutionRoleArn": "arn:aws:iam::`111122223333`:role/AccountResolutionRole"
        }
    },
    "createdAt": "2025-08-12T00:26:27.017118+00:00",
    "lastUpdatedAt": "2025-08-12T00:26:27.017118+00:00",
    "domainUnitId": "4njnngous3oyw7"
}
```
