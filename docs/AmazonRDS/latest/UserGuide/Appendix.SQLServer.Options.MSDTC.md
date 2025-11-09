# Disabling MSDTC

To disable MSDTC, remove the `MSDTC` option from its option group.

###### To remove the MSDTC option from its option group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Option groups**.
3. Choose the option group with the `MSDTC` option (`msdtc-se-2016` in
   the previous examples).
4. Choose **Delete option**.
5. Under **Deletion options**, choose **MSDTC** for
   **Options to delete**.
6. Under **Apply immediately**, choose **Yes** to delete
   the option immediately, or **No** to delete it at
   the next maintenance window.
7. Choose **Delete**.

###### To remove the MSDTC option from its option group

- Use one of the following commands.

For Linux, macOS, or Unix:

```
aws rds remove-option-from-option-group \
    --option-group-name `msdtc-se-2016` \
    --options MSDTC \
    --apply-immediately
```

For Windows:

```
aws rds remove-option-from-option-group ^
    --option-group-name `msdtc-se-2016` ^
    --options MSDTC ^
    --apply-immediately
```
