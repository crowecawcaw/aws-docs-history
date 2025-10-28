# Asynchronous states and operations

When you run a `glue:CreateTable` request, the asynchronous creation of the
Data Catalog view begins. In the following sections, this document describes the
`Status` of a AWS Glue view that is available in a
`glue:GetTable` response. For brevity, this section omits the full
response.

```
{
    "Table": {
        ...
        "Status": {
            ...
            "Action": "CREATE",
            "State": "QUEUED",
        }
    }
}
```

Both of the above attributes represent important diagnostic information which indicates the
state of the asynchronous operation, as well as the actions that can be performed on
this view. Below are the possible values that these attributes can take on.

1.  `Status.Action`
    1. CREATE
    2. UPDATE

2.  `Status.State`

        1. QUEUED
        2. IN\_PROGRESS
        3. SUCCESS
        4. FAILED

    It is also important to note that some updates on a Data Catalog view don't require an
    asynchronous operation. For example, one may wish to update the
    `Description` attribute of the table. Since this does not require any
    asynchronous operations, the resulting table metadata will not have any
    `Status`, and the attribute will be `NULL`.

```
{
    "Table": {
        ...,
        "Description": "I changed this attribute!"
    }
}
```

Next, this topic explores how the above status information can impact operations that can be performed on an AWS Glue view.

###### glue:CreateTable

There are no changes for this API when compared to how `glue:CreateTable` functions for any Glue table. `CreateTable` may be called for any table name that does not already exist.

###### glue:UpdateTable

This operation cannot be performed on an AWS Glue view which has the following status information:

1. Action == CREATE and State == QUEUED
2. Action == CREATE and State == IN_PROGRESS
3. Action == CREATE and state == FAILED
4. Action == UPDATE and state == QUEUED
5. Action == UPDATE and state == IN_PROGRESS
   To summarize, you can update a Data Catalog view only when it meets the following requirements.

6. It has been successfully created for the first time.
   1. Action == CREATE and State == SUCCESS

7. It has reached a terminal state after an asynchronous update operation.
   1. Action == UPDATE and State == SUCCESS
   2. Action == UPDATE and State == FAILED

8. It has a `NULL` state attribute as a result of a synchronous update.

###### glue:DeleteTable

There are no changes for this operation when compared to how `glue:DeleteTable`
functions for any AWS Glue table. You can delete a Data Catalog view regardless of its
state.

###### glue:GetTable

There are no changes for this operation when compared to how `glue:GetTable`
functions for any AWS Glue table. However, you can't query a Data Catalog view from the
analytical engines until it has been successfully created for the first time.
`Action == CREATE and State == SUCCESS`. After you create a
Data Catalog view successfully for the first time, you can query the view regardless of its
status.

###### Note

All of the information in this section applies to all table read APIs such as
`GetTable`, `GetTables`, and
`SearchTables`.
