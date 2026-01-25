# Turning off SSAS

To turn off SSAS, remove the `SSAS` option from its option group.

###### Important

Before you remove the `SSAS` option, delete your SSAS databases.

We highly recommend that you back up your SSAS databases before deleting them and removing
the `SSAS` option.

###### To remove the SSAS option from its option group

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Option groups**.
3. Choose the option group with the `SSAS` option that you want to remove (`ssas-se-2017` in the previous
   examples).
4. Choose **Delete option**.
5. Under **Deletion options**, choose **SSAS** for
   **Options to delete**.
6. Under **Apply immediately**, choose **Yes** to delete
   the option immediately, or **No** to delete it at
   the next maintenance window.
7. Choose **Delete**.

###### To remove the SSAS option from its option group

- Use one of the following commands.

For Linux, macOS, or Unix:

```
aws rds remove-option-from-option-group \
    --option-group-name `ssas-se-2017` \
    --options SSAS \
    --apply-immediately
```

For Windows:

```
aws rds remove-option-from-option-group ^
    --option-group-name `ssas-se-2017` ^
    --options SSAS ^
    --apply-immediately
```
