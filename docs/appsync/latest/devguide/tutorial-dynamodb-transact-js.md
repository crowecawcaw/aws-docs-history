# Performing DynamoDB transactions in

AWS AppSync

AWS AppSync supports using Amazon DynamoDB transaction operations across one or more tables in a single Region.
Supported operations are `TransactGetItems` and `TransactWriteItems`. By using these
features in AWS AppSync, you can perform tasks such as:

- Passing a list of keys in a single query and returning the results from a table
- Reading records from one or more tables in a single query
- Writing records in transactions to one or more tables in an all-or-nothing way
- Running transactions when some conditions are satisfied

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

###### Note

Roles are tied to data sources in AWS AppSync, and resolvers on fields are invoked against a data
source. Data sources configured to fetch against DynamoDB only have one table specified to keep
configurations simple. Therefore, when performing a transaction operation against multiple tables in a
single resolver, which is a more advanced task, you must grant the role on that data source access to
any tables the resolver will interact with. This would be done in the **Resource** field in the IAM policy above. Configuration of the transaction calls against
the tables is done in the resolver code, which we describe below.

## Data source

For the sake of simplicity, we’ll use the same data source for all the resolvers used in this tutorial.

We’ll have two tables called **savingAccounts** and **checkingAccounts**, both with the `accountNumber` as a partition key, and a
**transactionHistory** table with `transactionId` as partition
key. You can use the CLI commands below to create your tables. Make sure to replace `region` with
your Region.

**With the CLI**

```
aws dynamodb create-table --table-name savingAccounts \
  --attribute-definitions AttributeName=accountNumber,AttributeType=S \
  --key-schema AttributeName=accountNumber,KeyType=HASH \
  --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
  --table-class STANDARD --region region

aws dynamodb create-table --table-name checkingAccounts \
  --attribute-definitions AttributeName=accountNumber,AttributeType=S \
  --key-schema AttributeName=accountNumber,KeyType=HASH \
  --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
  --table-class STANDARD --region region

aws dynamodb create-table --table-name transactionHistory \
  --attribute-definitions AttributeName=transactionId,AttributeType=S \
  --key-schema AttributeName=transactionId,KeyType=HASH \
  --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
  --table-class STANDARD --region region
```

In the AWS AppSync console, in **Data sources**, create a new DynamoDB data source
and name it **TransactTutorial**. Select **savingAccounts** as the table (though the specific table does not matter when using
transactions). Choose to create a new role and the data source. You can review the data source configuration
to see the name of the generated role. In the IAM console, you can add an in-line policy that allows the
data source to interact with all the tables.

Replace `region` and `accountID` with your Region and account ID:

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
```

### TransactWriteItems - Populate accounts

In order to transfer money between accounts, we need to populate the table with
the details. We’ll use the GraphQL operation `Mutation.populateAccounts`
to do so.

In the Schema section, click on **Attach** next to the
`Mutation.populateAccounts` operation. Choose the `TransactTutorial` data
source and choose **Create**.

Now use the following code:

```
import { util } from '@aws-appsync/utils'

export function request(ctx) {
	const { savingAccounts, checkingAccounts } = ctx.args

	const savings = savingAccounts.map(({ accountNumber, ...rest }) => {
		return {
			table: 'savingAccounts',
			operation: 'PutItem',
			key: util.dynamodb.toMapValues({ accountNumber }),
			attributeValues: util.dynamodb.toMapValues(rest),
		}
	})

	const checkings = checkingAccounts.map(({ accountNumber, ...rest }) => {
		return {
			table: 'checkingAccounts',
			operation: 'PutItem',
			key: util.dynamodb.toMapValues({ accountNumber }),
			attributeValues: util.dynamodb.toMapValues(rest),
		}
	})
	return {
		version: '2018-05-29',
		operation: 'TransactWriteItems',
		transactItems: [...savings, ...checkings],
	}
}

export function response(ctx) {
	if (ctx.error) {
		util.error(ctx.error.message, ctx.error.type, null, ctx.result.cancellationReasons)
	}
	const { savingAccounts: sInput, checkingAccounts: cInput } = ctx.args
	const keys = ctx.result.keys
	const savingAccounts = sInput.map((_, i) => keys[i])
	const sLength = sInput.length
	const checkingAccounts = cInput.map((_, i) => keys[sLength + i])
	return { savingAccounts, checkingAccounts }
}
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

We populated three saving accounts and three checking accounts in one mutation.

Use the DynamoDB console to validate that data shows up in both the **savingAccounts** and **checkingAccounts** tables.

### TransactWriteItems - Transfer money

Attach a resolver to the `transferMoney` mutation with the following code. For each
transfer, we need a success modifier to both the checking and savings accounts, and we need to track the
transfer in transactions.

```
import { util } from '@aws-appsync/utils'

export function request(ctx) {
	const transactions = ctx.args.transactions

	const savings = []
	const checkings = []
	const history = []
	transactions.forEach((t) => {
		const { savingAccountNumber, checkingAccountNumber, amount } = t
		savings.push({
			table: 'savingAccounts',
			operation: 'UpdateItem',
			key: util.dynamodb.toMapValues({ accountNumber: savingAccountNumber }),
			update: {
				expression: 'SET balance = balance - :amount',
				expressionValues: util.dynamodb.toMapValues({ ':amount': amount }),
			},
		})
		checkings.push({
			table: 'checkingAccounts',
			operation: 'UpdateItem',
			key: util.dynamodb.toMapValues({ accountNumber: checkingAccountNumber }),
			update: {
				expression: 'SET balance = balance + :amount',
				expressionValues: util.dynamodb.toMapValues({ ':amount': amount }),
			},
		})
		history.push({
			table: 'transactionHistory',
			operation: 'PutItem',
			key: util.dynamodb.toMapValues({ transactionId: util.autoId() }),
			attributeValues: util.dynamodb.toMapValues({
				from: savingAccountNumber,
				to: checkingAccountNumber,
				amount,
			}),
		})
	})

	return {
		version: '2018-05-29',
		operation: 'TransactWriteItems',
		transactItems: [...savings, ...checkings, ...history],
	}
}

export function response(ctx) {
	if (ctx.error) {
		util.error(ctx.error.message, ctx.error.type, null, ctx.result.cancellationReasons)
	}
	const tInput = ctx.args.transactions
	const tLength = tInput.length
	const keys = ctx.result.keys
	const savingAccounts = tInput.map((_, i) => keys[tLength * 0 + i])
	const checkingAccounts = tInput.map((_, i) => keys[tLength * 1 + i])
	const transactionHistory = tInput.map((_, i) => keys[tLength * 2 + i])
	return { savingAccounts, checkingAccounts, transactionHistory }
}
```

Now, navigate to the **Queries** section of the AWS AppSync console and
execute the **transferMoney** mutation as follows:

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

We sent three banking transactions in one mutation. Use the DynamoDB console to validate that data shows
up in the **savingAccounts**, **checkingAccounts**, and **transactionHistory** tables.

### TransactGetItems - Retrieve accounts

In order to retrieve the details from savings and checking accounts in a single transactional request,
we’ll attach a resolver to the `Query.getAccounts` GraphQL operation on our schema. Select
**Attach**, pick the same `TransactTutorial` data source
created at the beginning of the tutorial. Use the following code:

```
import { util } from '@aws-appsync/utils'

export function request(ctx) {
	const { savingAccountNumbers, checkingAccountNumbers } = ctx.args

	const savings = savingAccountNumbers.map((accountNumber) => {
		return { table: 'savingAccounts', key: util.dynamodb.toMapValues({ accountNumber }) }
	})
	const checkings = checkingAccountNumbers.map((accountNumber) => {
		return { table: 'checkingAccounts', key: util.dynamodb.toMapValues({ accountNumber }) }
	})
	return {
		version: '2018-05-29',
		operation: 'TransactGetItems',
		transactItems: [...savings, ...checkings],
	}
}

export function response(ctx) {
	if (ctx.error) {
		util.error(ctx.error.message, ctx.error.type, null, ctx.result.cancellationReasons)
	}

	const { savingAccountNumbers: sInput, checkingAccountNumbers: cInput } = ctx.args
	const items = ctx.result.items
	const savingAccounts = sInput.map((_, i) => items[i])
	const sLength = sInput.length
	const checkingAccounts = cInput.map((_, i) => items[sLength + i])
	return { savingAccounts, checkingAccounts }
}
```

Save the resolver and navigate to the **Queries** sections of the
AWS AppSync console. In order to retrieve the savings and checking accounts, execute the following
query:

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
