# Changing the SSAS mode

You can change the mode in which SSAS runs, either Tabular or Multidimensional. To
change the mode, use the AWS Management Console or the AWS CLI to modify the options settings in the
SSAS option.

###### Important

You can only use one SSAS mode at a time. Make sure to delete all of the SSAS
databases before changing the mode, or you receive an error.

The following Amazon RDS console procedure changes the SSAS mode to Tabular and
sets the `MAX_MEMORY` parameter to 70 percent.

###### To modify the SSAS option

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Option groups**.
3. Choose the option group with the `SSAS` option that you want to modify
   (`ssas-se-2017` in the previous examples).
4. Choose **Modify option**.
5. Change the option settings:
   1. For **Max memory**, enter `70`.
   2. For **Mode**, choose **Tabular**.

6. Choose **Modify option**.
   The following AWS CLI example changes the SSAS mode to Tabular and sets the `MAX_MEMORY` parameter to 70
   percent.

For the CLI command to work, make sure to include all of the required
parameters, even if you're not modifying them.

###### To modify the SSAS option

- Use one of the following commands.

For Linux, macOS, or Unix:

```
aws rds add-option-to-option-group \
    --option-group-name `ssas-se-2017` \
    --options "OptionName=SSAS,VpcSecurityGroupMemberships=`sg-12345e67`,OptionSettings=[{Name=MAX_MEMORY,Value=70},{Name=MODE,Value=Tabular}]" \
    --apply-immediately
```

For Windows:

```
aws rds add-option-to-option-group ^
    --option-group-name `ssas-se-2017` ^
    --options OptionName=SSAS,VpcSecurityGroupMemberships=`sg-12345e67`,OptionSettings=[{Name=MAX_MEMORY,Value=70},{Name=MODE,Value=Tabular}] ^
    --apply-immediately
```
