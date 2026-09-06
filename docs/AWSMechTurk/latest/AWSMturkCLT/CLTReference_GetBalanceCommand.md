


|  | 
| --- |
| **This software is not currently supported by Amazon Mechanical Turk**<br />The Amazon Mechanical Turk Command Line Tools (CLT) are not currently maintained by Amazon Mechanical Turk. If you would still like to use Amazon Mechanical Turk from the command line, use the `mturk` command in the AWS Command Line Interface (CLI). For more information, see the `mturk` section of the [ AWS CLI Command Reference ](https://docs.aws.amazon.com/cli/latest/reference/mturk/index.html).  | 

 

# getBalance
<a name="CLTReference_GetBalanceCommand"></a>

## Description
<a name="w2aab9c31b2"></a>

 The `getBalance` command retrieves the available balance in your Amazon Mechanical Turk account. This amount is your current balance minus any outstanding payments, fees, or bonuses you owe. 

## Arguments
<a name="w2aab9c31b4"></a>

 The following table describes the arguments for the `getBalance` command. 


| Name | Description | Required | 
| --- | --- | --- | 
|  `‑help` or `‑h`  |  Displays the help for this operation. <br />Example: `-help`  | No | 
|  `‑sandbox`  |  Runs this command in the Amazon Mechanical Turk sandbox and gets your sandbox account balance. This amount is always $10000.00. This argument takes precedence even if you specify the production web site in your `mturk.properties` file. <br /> Example:`-sandbox`  | No | 

## Example
<a name="w2aab9c31b6"></a>

 The following examples for Unix and Windows show how to use the `getBalance` command. 

### Unix
<a name="w2aab9c31b6b4"></a>

 The following example demonstrates how to call this command from Unix. 

```
./getBalance.sh 
```

### Windows
<a name="w2aab9c31b6b6"></a>

 The following example demonstrates how to call this command from Microsoft Windows. 

```
getBalance
```

## Output
<a name="w2aab9c31b8"></a>

This example produces output similar to the following.

```
Your account balance: $819.45
```