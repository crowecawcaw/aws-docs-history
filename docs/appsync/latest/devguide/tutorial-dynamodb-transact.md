# Performing DynamoDB transactions in AWS AppSync

###### Note

We now primarily support the APPSYNC_JS runtime and its documentation. Please consider using the
APPSYNC_JS runtime and its guides [here](tutorials-js.md "tutorials-js.md").

AWS AppSync supports using Amazon DynamoDB transaction operations across one or more tables in
a single region. Supported operations are `TransactGetItems` and
`TransactWriteItems`. By using these features in AWS AppSync, you can
perform tasks such as:

- Pass a list of keys in a single query and return the results from a table
- Read records from one or more tables in a single query
- Write records in transaction to one or more tables in an all-or-nothing way
- Execute transactions when some conditions are satisfied

## Permissions

Like other resolvers, you need to create a data source in AWS AppSync and either
create a role or use an existing one. Because transaction operations require different
permissions on DynamoDB tables, you need to grant the configured role permissions for read
or write actions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "dynamodb:DeleteItem",
 "dynamodb:GetItem",
 "dynamodb:PutItem",
 "dynamodb:Query",
 "dynamodb:Scan",
 "dynamodb:UpdateItem"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:dynamodb:us-east-1:111122223333:table/TABLENAME",
 "arn:aws:dynamodb:us-east-1:111122223333:table/TABLENAME/*"
 ]
 }
 ]
}`

```

**Note**: Roles are tied to data sources in AWS AppSync,
and resolvers on fields are invoked against a data source. Data sources configured to
fetch against DynamoDB only have one table specified, to keep configuration simple.
Therefore, when performing a transaction operation against multiple tables in a single
resolver, which is a more advanced task, you must grant the role on that data source
access to any tables the resolver will interact with. This would be done in the
**Resource** field in the IAM policy above.
Configuration of the transaction calls against the tables is done in the resolver
template, which we describe below.

## Data Source

For the sake of simplicity, we’ll use the same data source for all the resolvers used
in this tutorial. On the **Data sources** tab, create a new
DynamoDB data source and name it **TransactTutorial**. The
table name can be anything because table names are specified as part of the request
mapping template for transaction operations. We will give the table name
`empty`.

We’ll have two tables called **savingAccounts** and
**checkingAccounts**, both with
`accountNumber` as partition key, and a **transactionHistory** table with `transactionId` as partition
key.

For this tutorial, any role with the following inline policy will work. Replace
`region` and `accountId` with your region and account
ID:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "dynamodb:DeleteItem",
 "dynamodb:GetItem",
 "dynamodb:PutItem",
 "dynamodb:Query",
 "dynamodb:Scan",
 "dynamodb:UpdateItem"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:dynamodb:us-east-1:111122223333:table/savingAccounts",
 "arn:aws:dynamodb:us-east-1:111122223333:table/savingAccounts/*",
 "arn:aws:dynamodb:us-east-1:111122223333:table/checkingAccounts",
 "arn:aws:dynamodb:us-east-1:111122223333:table/checkingAccounts/*",
 "arn:aws:dynamodb:us-east-1:111122223333:table/transactionHistory",
 "arn:aws:dynamodb:us-east-1:111122223333:table/transactionHistory/*"
 ]
 }
 ]
}`

```

## Transactions

For this example, the context is a classic banking transaction, where we’ll use
`TransactWriteItems` to:

- Transfer money from saving accounts to checking accounts
- Generate new transaction records for each transaction

And then we’ll use `TransactGetItems` to retrieve details from saving
accounts and checking accounts.

###### Warning

`TransactWriteItems` is not supported when used with conflict detection
and resolution. These settings must be disabled to prevent possible errors.

We define our GraphQL schema as follows:

```
type SavingAccount {
    accountNumber: String!
    username: String
    balance: Float
}

type CheckingAccount {
    accountNumber: String!
    username: String
    balance: Float
}

type TransactionHistory {
    transactionId: ID!
    from: String
    to: String
    amount: Float
}

type TransactionResult {
    savingAccounts: [SavingAccount]
    checkingAccounts: [CheckingAccount]
    transactionHistory: [TransactionHistory]
}

input SavingAccountInput {
    accountNumber: String!
    username: String
    balance: Float
}

input CheckingAccountInput {
    accountNumber: String!
    username: String
    balance: Float
}

input TransactionInput {
    savingAccountNumber: String!
    checkingAccountNumber: String!
    amount: Float!
}

type Query {
    getAccounts(savingAccountNumbers: [String], checkingAccountNumbers: [String]): TransactionResult
}

type Mutation {
    populateAccounts(savingAccounts: [SavingAccountInput], checkingAccounts: [CheckingAccountInput]): TransactionResult
    transferMoney(transactions: [TransactionInput]): TransactionResult
}

schema {
    query: Query
    mutation: Mutation
}
```

### TransactWriteItems - Populate Accounts

In order to transfer money between accounts, we need to populate the table with
the details. We’ll use the GraphQL operation `Mutation.populateAccounts`
to do so.

In the Schema section, click on **Attach** next to the
`Mutation.populateAccounts` operation. Go to VTL Unit Resolvers, then choose the same
`TransactTutorial` data source.

Now use the following request mapping template:

**Request Mapping Template**

```
#set($savingAccountTransactPutItems = [])
#set($index = 0)
#foreach($savingAccount in ${ctx.args.savingAccounts})
    #set($keyMap = {})
    $util.qr($keyMap.put("accountNumber", $util.dynamodb.toString($savingAccount.accountNumber)))
    #set($attributeValues = {})
    $util.qr($attributeValues.put("username", $util.dynamodb.toString($savingAccount.username)))
    $util.qr($attributeValues.put("balance", $util.dynamodb.toNumber($savingAccount.balance)))
    #set($index = $index + 1)
    #set($savingAccountTransactPutItem = {"table": "savingAccounts",
        "operation": "PutItem",
        "key": $keyMap,
        "attributeValues": $attributeValues})
    $util.qr($savingAccountTransactPutItems.add($savingAccountTransactPutItem))
#end

#set($checkingAccountTransactPutItems = [])
#set($index = 0)
#foreach($checkingAccount in ${ctx.args.checkingAccounts})
    #set($keyMap = {})
    $util.qr($keyMap.put("accountNumber", $util.dynamodb.toString($checkingAccount.accountNumber)))
    #set($attributeValues = {})
    $util.qr($attributeValues.put("username", $util.dynamodb.toString($checkingAccount.username)))
    $util.qr($attributeValues.put("balance", $util.dynamodb.toNumber($checkingAccount.balance)))
    #set($index = $index + 1)
    #set($checkingAccountTransactPutItem = {"table": "checkingAccounts",
        "operation": "PutItem",
        "key": $keyMap,
        "attributeValues": $attributeValues})
    $util.qr($checkingAccountTransactPutItems.add($checkingAccountTransactPutItem))
#end

#set($transactItems = [])
$util.qr($transactItems.addAll($savingAccountTransactPutItems))
$util.qr($transactItems.addAll($checkingAccountTransactPutItems))

{
    "version" : "2018-05-29",
    "operation" : "TransactWriteItems",
    "transactItems" : $util.toJson($transactItems)
}
```

And the following response mapping template:

**Response Mapping Template**

```
#if ($ctx.error)
    $util.appendError($ctx.error.message, $ctx.error.type, null, $ctx.result.cancellationReasons)
#end

#set($savingAccounts = [])
#foreach($index in [0..2])
    $util.qr($savingAccounts.add(${ctx.result.keys[$index]}))
#end

#set($checkingAccounts = [])
#foreach($index in [3..5])
    $util.qr($checkingAccounts.add(${ctx.result.keys[$index]}))
#end

#set($transactionResult = {})
$util.qr($transactionResult.put('savingAccounts', $savingAccounts))
$util.qr($transactionResult.put('checkingAccounts', $checkingAccounts))

$util.toJson($transactionResult)
```

Save the resolver and navigate to the **Queries**
section of the AWS AppSync console to populate the accounts.

Execute the following mutation:

```
mutation populateAccounts {
  populateAccounts (
    savingAccounts: [
      {accountNumber: "1", username: "Tom", balance: 100},
      {accountNumber: "2", username: "Amy", balance: 90},
      {accountNumber: "3", username: "Lily", balance: 80},
    ]
    checkingAccounts: [
      {accountNumber: "1", username: "Tom", balance: 70},
      {accountNumber: "2", username: "Amy", balance: 60},
      {accountNumber: "3", username: "Lily", balance: 50},
    ]) {
    savingAccounts {
      accountNumber
    }
    checkingAccounts {
      accountNumber
    }
  }
}
```

We populated 3 saving accounts and 3 checking accounts in one mutation.

Use the DynamoDB console to validate that data shows up in both the **savingAccounts** and **checkingAccounts** tables.

### TransactWriteItems - Transfer Money

Attach a resolver to the `transferMoney` mutation with the following
**Request Mapping Template**. Note the values of
`amounts`, `savingAccountNumbers`, and
`checkingAccountNumbers` are the same.

```
#set($amounts = [])
#foreach($transaction in ${ctx.args.transactions})
    #set($attributeValueMap = {})
    $util.qr($attributeValueMap.put(":amount", $util.dynamodb.toNumber($transaction.amount)))
    $util.qr($amounts.add($attributeValueMap))
#end

#set($savingAccountTransactUpdateItems = [])
#set($index = 0)
#foreach($transaction in ${ctx.args.transactions})
    #set($keyMap = {})
    $util.qr($keyMap.put("accountNumber", $util.dynamodb.toString($transaction.savingAccountNumber)))
    #set($update = {})
    $util.qr($update.put("expression", "SET balance = balance - :amount"))
    $util.qr($update.put("expressionValues", $amounts[$index]))
    #set($index = $index + 1)
    #set($savingAccountTransactUpdateItem = {"table": "savingAccounts",
        "operation": "UpdateItem",
        "key": $keyMap,
        "update": $update})
    $util.qr($savingAccountTransactUpdateItems.add($savingAccountTransactUpdateItem))
#end

#set($checkingAccountTransactUpdateItems = [])
#set($index = 0)
#foreach($transaction in ${ctx.args.transactions})
    #set($keyMap = {})
    $util.qr($keyMap.put("accountNumber", $util.dynamodb.toString($transaction.checkingAccountNumber)))
    #set($update = {})
    $util.qr($update.put("expression", "SET balance = balance + :amount"))
    $util.qr($update.put("expressionValues", $amounts[$index]))
    #set($index = $index + 1)
    #set($checkingAccountTransactUpdateItem = {"table": "checkingAccounts",
        "operation": "UpdateItem",
        "key": $keyMap,
        "update": $update})
    $util.qr($checkingAccountTransactUpdateItems.add($checkingAccountTransactUpdateItem))
#end

#set($transactionHistoryTransactPutItems = [])
#foreach($transaction in ${ctx.args.transactions})
    #set($keyMap = {})
    $util.qr($keyMap.put("transactionId", $util.dynamodb.toString(${utils.autoId()})))
    #set($attributeValues = {})
    $util.qr($attributeValues.put("from", $util.dynamodb.toString($transaction.savingAccountNumber)))
    $util.qr($attributeValues.put("to", $util.dynamodb.toString($transaction.checkingAccountNumber)))
    $util.qr($attributeValues.put("amount", $util.dynamodb.toNumber($transaction.amount)))
    #set($transactionHistoryTransactPutItem = {"table": "transactionHistory",
        "operation": "PutItem",
        "key": $keyMap,
        "attributeValues": $attributeValues})
    $util.qr($transactionHistoryTransactPutItems.add($transactionHistoryTransactPutItem))
#end

#set($transactItems = [])
$util.qr($transactItems.addAll($savingAccountTransactUpdateItems))
$util.qr($transactItems.addAll($checkingAccountTransactUpdateItems))
$util.qr($transactItems.addAll($transactionHistoryTransactPutItems))

{
    "version" : "2018-05-29",
    "operation" : "TransactWriteItems",
    "transactItems" : $util.toJson($transactItems)
}
```

We will have 3 banking transactions in a single `TransactWriteItems`
operation. Use the following **Response Mapping
Template**:

```
#if ($ctx.error)
    $util.appendError($ctx.error.message, $ctx.error.type, null, $ctx.result.cancellationReasons)
#end

#set($savingAccounts = [])
#foreach($index in [0..2])
    $util.qr($savingAccounts.add(${ctx.result.keys[$index]}))
#end

#set($checkingAccounts = [])
#foreach($index in [3..5])
    $util.qr($checkingAccounts.add(${ctx.result.keys[$index]}))
#end

#set($transactionHistory = [])
#foreach($index in [6..8])
    $util.qr($transactionHistory.add(${ctx.result.keys[$index]}))
#end

#set($transactionResult = {})
$util.qr($transactionResult.put('savingAccounts', $savingAccounts))
$util.qr($transactionResult.put('checkingAccounts', $checkingAccounts))
$util.qr($transactionResult.put('transactionHistory', $transactionHistory))

$util.toJson($transactionResult)
```

Now navigate to the **Queries** section of the
AWS AppSync console and execute the **transferMoney**
mutation as follows:

```
mutation write {
  transferMoney(
    transactions: [
      {savingAccountNumber: "1", checkingAccountNumber: "1", amount: 7.5},
      {savingAccountNumber: "2", checkingAccountNumber: "2", amount: 6.0},
      {savingAccountNumber: "3", checkingAccountNumber: "3", amount: 3.3}
    ]) {
    savingAccounts {
      accountNumber
    }
    checkingAccounts {
      accountNumber
    }
    transactionHistory {
      transactionId
    }
  }
}
```

We sent 2 banking transactions in one mutation. Use the DynamoDB console to validate
that data shows up in the **savingAccounts**, **checkingAccounts**, and **transactionHistory** tables.

### TransactGetItems - Retrieve Accounts

In order to retrieve the details from saving accounts and checking accounts in a single transactional
request we’ll attach a resolver to the `Query.getAccounts` GraphQL operation on our schema.
Select **Attach**, go to VTL Unit Resolvers, then on the next screen, pick
the same `TransactTutorial` data source created at the beginning of the tutorial. Configure
the templates as follows:

**Request Mapping Template**

```
#set($savingAccountsTransactGets = [])
#foreach($savingAccountNumber in ${ctx.args.savingAccountNumbers})
    #set($savingAccountKey = {})
    $util.qr($savingAccountKey.put("accountNumber", $util.dynamodb.toString($savingAccountNumber)))
    #set($savingAccountTransactGet = {"table": "savingAccounts", "key": $savingAccountKey})
    $util.qr($savingAccountsTransactGets.add($savingAccountTransactGet))
#end

#set($checkingAccountsTransactGets = [])
#foreach($checkingAccountNumber in ${ctx.args.checkingAccountNumbers})
    #set($checkingAccountKey = {})
    $util.qr($checkingAccountKey.put("accountNumber", $util.dynamodb.toString($checkingAccountNumber)))
    #set($checkingAccountTransactGet = {"table": "checkingAccounts", "key": $checkingAccountKey})
    $util.qr($checkingAccountsTransactGets.add($checkingAccountTransactGet))
#end

#set($transactItems = [])
$util.qr($transactItems.addAll($savingAccountsTransactGets))
$util.qr($transactItems.addAll($checkingAccountsTransactGets))

{
    "version" : "2018-05-29",
    "operation" : "TransactGetItems",
    "transactItems" : $util.toJson($transactItems)
}
```

**Response Mapping Template**

```
#if ($ctx.error)
    $util.appendError($ctx.error.message, $ctx.error.type, null, $ctx.result.cancellationReasons)
#end

#set($savingAccounts = [])
#foreach($index in [0..2])
    $util.qr($savingAccounts.add(${ctx.result.items[$index]}))
#end

#set($checkingAccounts = [])
#foreach($index in [3..4])
    $util.qr($checkingAccounts.add($ctx.result.items[$index]))
#end

#set($transactionResult = {})
$util.qr($transactionResult.put('savingAccounts', $savingAccounts))
$util.qr($transactionResult.put('checkingAccounts', $checkingAccounts))

$util.toJson($transactionResult)
```

Save the resolver and navigate to the **Queries**
sections of the AWS AppSync console. In order to retrieve the saving accounts and
checing accounts, execute the following query:

```
query getAccounts {
  getAccounts(
    savingAccountNumbers: ["1", "2", "3"],
    checkingAccountNumbers: ["1", "2"]
  ) {
    savingAccounts {
      accountNumber
      username
      balance
    }
    checkingAccounts {
      accountNumber
      username
      balance
    }
  }
}
```

We have successfully demonstrated the use of DynamoDB transactions using
AWS AppSync.
