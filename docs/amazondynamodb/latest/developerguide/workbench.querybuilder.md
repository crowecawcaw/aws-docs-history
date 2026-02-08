# Building PartiQL statements

To use NoSQL Workbench to build [PartiQL for
DynamoDB](ql-reference.md "ql-reference.md") statements, choose **PartiQL editor** near the
top of the NoSQL Workbench UI.

You can build the following PartiQL statement types in the operation
builder.

###### Topics

- [Singleton
  statements](#workbench.querybuilder.partiql.single "#workbench.querybuilder.partiql.single")
- [Transactions](#workbench.querybuilder.partiql.transaction "#workbench.querybuilder.partiql.transaction")
- [Batch](#workbench.querybuilder.partiql.batch "#workbench.querybuilder.partiql.batch")

## Singleton

statements

To run or generate code for a PartiQL statement, do the following.

1. Choose **PartiQL editor** near the top of the
   window.
2. Enter a valid [PartiQL statement](ql-reference.md "ql-reference.md").
3. If your statement uses parameters:
   1. Choose **Optional request
      parameters**.
   2. Choose **Add new parameters**.
   3. Enter the attribute type and value.
   4. If you want to add additional parameters, repeat steps b and
      c.

4. If you want to generate code, choose **Generate
   code**.

Select your desired language from the displayed tabs. You can now copy
this code and use it in your application. 5. If you want the operation to be run immediately, choose
**Run**. 6. If you want to save this operation for later use, choose
**Save operation**. Then enter a name for your
operation and choose **Save**.

## Transactions

To run or generate code for a PartiQL transaction, do the following.

1. Choose **PartiQLTransaction** from the **More
   operations** dropdown.
2. Choose **Add a new statement**.
3. Enter a valid [PartiQL statement](ql-reference.md "ql-reference.md").

###### Note

Read and write operations are not supported in the same PartiQL
transaction request. A SELECT statement cannot be in the same
request with INSERT, UPDATE, and DELETE statements. See [Performing transactions with PartiQL for DynamoDB](ql-reference.multiplestatements.md "ql-reference.multiplestatements.md") for
more details. 4. If your statement uses parameters

    1. Choose **Optional request
     parameters**.
    2. Choose **Add new parameters**.
    3. Enter the attribute type and value.
    4. If you want to add additional parameters, repeat steps b and
     c.

5. If you want to add more statements, repeat steps 2 to 4.
6. If you want to generate code, choose **Generate
   code**.

Select your desired language from the displayed tabs. You can now copy
this code and use it in your application. 7. If you want the operation to be run immediately, choose
**Run**. 8. If you want to save this operation for later use, choose
**Save operation**. Then enter a name for your
operation and choose **Save**.

## Batch

To run or generate code for a PartiQL batch, do the following.

1. Choose **PartiQLBatch** from the **More
   operations** dropdown.
2. Choose **Add a new statement**.
3. Enter a valid [PartiQL statement](ql-reference.md "ql-reference.md").

###### Note

Read and write operations are not supported in the same PartiQL
batch request, which means a SELECT statement cannot be in the same
request with INSERT, UPDATE, and DELETE statements. Write operations
to the same item are not allowed. As with the BatchGetItem
operation, only singleton read operations are supported. Scan and
query operations are not supported. See [Running batch operations with PartiQL for DynamoDB](ql-reference.multiplestatements.md "ql-reference.multiplestatements.md") for
more details. 4. If your statement uses parameters:

    1. Choose **Optional request
     parameters**.
    2. Choose **Add new parameters**.
    3. Enter the attribute type and value.
    4. If you want to add additional parameters, repeat steps b and
     c.

5. If you want to add more statements, repeat steps 2 to 4.
6. If you want to generate code, choose **Generate
   code**.

Select your desired language from the displayed tabs. You can now copy
this code and use it in your application. 7. If you want the operation to be run immediately, choose
**Run**. 8. If you want to save this operation for later use, choose
**Save operation**. Then enter a name for your
operation and choose **Save**.
