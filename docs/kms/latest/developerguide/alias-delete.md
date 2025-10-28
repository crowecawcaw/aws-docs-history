# Delete an alias

You can delete an alias in the AWS KMS console or by using the [DeleteAlias](../APIReference/API_DeleteAlias.md "../APIReference/API_DeleteAlias.md") operation. Before deleting an
alias, make sure that it's not in use. Although deleting an alias doesn't affect the
associated KMS key, it might create problems for any application that uses the alias. If you
delete an alias by mistake, you can create a new alias with the same name and associate it
with the same or a different KMS key.

If you delete a KMS key, all aliases associated with that KMS key are deleted.

To delete an alias in the AWS KMS console, use the **Aliases** tab on
the detail page for the KMS key. You can delete multiple aliases for a KMS key at one
time.

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the navigation pane, choose **Customer managed keys**. You cannot manage aliases for AWS managed keys or
   AWS owned keys.
4. In the table, choose the key ID or alias of the KMS key. Then, on the KMS key
   detail page, choose the **Aliases** tab.

If a KMS key has multiple aliases, the **Aliases** column in
the table displays one alias and an alias summary, such as **(+_n_ more)**. Choosing the alias summary takes you
directly to the **Aliases** tab on the KMS key detail page. 5. On the **Aliases** tab, select the check box next to the aliases
that you want to delete. Then choose **Delete**.
To delete an alias, use the [DeleteAlias](../APIReference/API_DeleteAlias.md "../APIReference/API_DeleteAlias.md") operation. This operation deletes one alias at a time. The alias
name is case-sensitive and it must be preceded by the `alias/` prefix.

For example, the following command deletes the `test-key` alias. This
command does not return any output.

```
`$` `aws kms delete-alias --alias-name alias/test-key`
```

To verify that the alias is deleted, use the [ListAliases](../APIReference/API_ListAliases.md "../APIReference/API_ListAliases.md") operation. The following
command uses the `--query` parameter in the AWS CLI to get only the
`test-key` alias. The empty brackets in the response indicate that the
`ListAliases` response didn't include a `test-key` alias. To
eliminate the brackets, use the `--output text` parameter and value.

```
`$` `aws kms list-aliases --query 'Aliases[?AliasName==`alias/test-key`]'`
[]
```
