

# Disabling MSDTC
<a name="Appendix.SQLServer.Options.MSDTC.Disable"></a>

To disable MSDTC, remove the `MSDTC` option from its option group.

## Console
<a name="Options.MSDTC.Disable.Console"></a>

**To remove the MSDTC option from its option group**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Option groups**.

1. Choose the option group with the `MSDTC` option (`msdtc-se-2016` in the previous examples).

1. Choose **Delete option**.

1. Under **Deletion options**, choose **MSDTC** for **Options to delete**.

1. Under **Apply immediately**, choose **Yes** to delete the option immediately, or **No** to delete it at the next maintenance window.

1. Choose **Delete**.

## CLI
<a name="Options.MSDTC.Disable.CLI"></a>

**To remove the MSDTC option from its option group**
+ Use one of the following commands.  
**Example**  

  For Linux, macOS, or Unix:

  ```
  aws rds remove-option-from-option-group \
      --option-group-name {{msdtc-se-2016}} \
      --options MSDTC \
      --apply-immediately
  ```

  For Windows:

  ```
  aws rds remove-option-from-option-group ^
      --option-group-name {{msdtc-se-2016}} ^
      --options MSDTC ^
      --apply-immediately
  ```