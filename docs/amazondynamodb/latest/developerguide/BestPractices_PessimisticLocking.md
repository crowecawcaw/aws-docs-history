# Pessimistic locking with DynamoDB

transactions

DynamoDB [transactions](transactions.md "transactions.md") provide an all-or-nothing approach
to grouped operations. When you use `TransactWriteItems`, DynamoDB monitors all items in
the transaction. If any item is modified by another operation during the transaction, the entire
transaction is canceled and DynamoDB returns a `TransactionCanceledException`. This
behavior provides a form of pessimistic concurrency control because conflicting concurrent
modifications are prevented rather than detected after the fact.

## When to use transactions for

locking

Transactions are a good fit when:

- You need to update multiple items atomically, either within the same table or
  across tables.
- Your business logic requires all-or-nothing semantics – either all
  changes succeed or none are applied.

Common examples include transferring funds between accounts, placing orders that update
both inventory and order tables, and exchanging items between players in a game.

## Tradeoffs

**Higher write cost**
For items up to 1 KB, transactions consume 2 WCUs per item (one to prepare, one
to commit), compared to 1 WCU for a standard write.

**Item limit**
A single transaction can include up to 100 actions across one or more
tables.

**Conflict sensitivity**
If any item in the transaction is modified by another operation, the entire
transaction fails. In high-contention scenarios, this can lead to frequent
cancellations.

## Implementation

The following example uses `TransactWriteItems` to transfer inventory between
two items atomically. If another process modifies either item during the transaction, the entire
operation is rolled back.

```
import boto3

client = boto3.client('dynamodb')

def transfer_inventory(source_id, target_id, quantity):
    try:
        client.transact_write_items(
            TransactItems=[
                {
                    'Update': {
                        'TableName': 'Inventory',
                        'Key': {'ItemID': {'S': source_id}},
                        'UpdateExpression': 'SET QuantityLeft = QuantityLeft - :qty',
                        'ConditionExpression': 'QuantityLeft >= :qty',
                        'ExpressionAttributeValues': {
                            ':qty': {'N': str(quantity)}
                        }
                    }
                },
                {
                    'Update': {
                        'TableName': 'Inventory',
                        'Key': {'ItemID': {'S': target_id}},
                        'UpdateExpression': 'SET QuantityLeft = QuantityLeft + :qty',
                        'ExpressionAttributeValues': {
                            ':qty': {'N': str(quantity)}
                        }
                    }
                }
            ]
        )
        return True
    except client.exceptions.TransactionCanceledException as e:
        print(f"Transaction canceled: {e}")
        return False
```

In this example, the condition expression checks that sufficient inventory exists, but no
version attribute is needed. DynamoDB automatically cancels the transaction if any item in the
transaction is modified by another operation between the prepare and commit phases. This is what
provides the pessimistic concurrency control – conflicting concurrent modifications are
prevented by the transaction itself.

###### Note

You can combine transactions with optimistic locking by adding version checks as
additional condition expressions. This provides an extra layer of protection but is not
required for the transaction to detect conflicts.

For more information, see [Managing complex workflows with DynamoDB transactions](transactions.md "transactions.md").
