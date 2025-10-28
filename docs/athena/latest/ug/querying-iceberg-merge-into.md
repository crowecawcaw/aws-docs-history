# MERGE INTO

Conditionally updates, deletes, or inserts rows into an Iceberg table. A single
statement can combine update, delete, and insert actions. For syntax, see [MERGE INTO](merge-into-statement.md "merge-into-statement.md").

###### Note

`MERGE INTO` is transactional and is supported only for Apache
Iceberg tables in Athena engine version 3.

The following example deletes all customers from table `t` that are in
the source table `s`.

```
MERGE INTO accounts t USING monthly_accounts_update s
ON t.customer = s.customer
WHEN MATCHED
THEN DELETE

```

The following example updates target table `t` with customer
information from source table `s`. For customer rows in table
`t` that have matching customer rows in table `s`, the
example increments the purchases in table t. If table `t` has no match
for a customer row in table `s`, the example inserts the customer row
from table `s` into table `t`.

```
MERGE INTO accounts t USING monthly_accounts_update s
    ON (t.customer = s.customer)
    WHEN MATCHED
        THEN UPDATE SET purchases = s.purchases + t.purchases
    WHEN NOT MATCHED
        THEN INSERT (customer, purchases, address)
              VALUES(s.customer, s.purchases, s.address)
```

The following example conditionally updates target table `t` with
information from the source table `s`. The example deletes any matching
target row for which the source address is Centreville. For all other matching rows,
the example adds the source purchases and sets the target address to the source
address. If there is no match in the target table, the example inserts the row from
the source table.

```
MERGE INTO accounts t USING monthly_accounts_update s
    ON (t.customer = s.customer)
    WHEN MATCHED AND s.address = 'Centreville'
        THEN DELETE
    WHEN MATCHED
        THEN UPDATE
            SET purchases = s.purchases + t.purchases, address = s.address
    WHEN NOT MATCHED
        THEN INSERT (customer, purchases, address)
              VALUES(s.customer, s.purchases, s.address)
```
