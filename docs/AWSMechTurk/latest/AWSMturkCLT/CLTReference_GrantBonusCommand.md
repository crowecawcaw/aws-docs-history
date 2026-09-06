


|  | 
| --- |
| **This software is not currently supported by Amazon Mechanical Turk**<br />The Amazon Mechanical Turk Command Line Tools (CLT) are not currently maintained by Amazon Mechanical Turk. If you would still like to use Amazon Mechanical Turk from the command line, use the `mturk` command in the AWS Command Line Interface (CLI). For more information, see the `mturk` section of the [ AWS CLI Command Reference ](https://docs.aws.amazon.com/cli/latest/reference/mturk/index.html).  | 

 

# grantBonus
<a name="CLTReference_GrantBonusCommand"></a>

## Description
<a name="w2aab9c40b2"></a>

 The `grantBonus` command issues a payment from your account to a Worker. This payment happens separately from the reward you pay to the Worker when you approve the Worker's assignment. You must have enough funds in your account to pay for the bonus. 

## Arguments
<a name="w2aab9c40b4"></a>

 The following table describes the arguments for the `grantBonus` command. 


| Name | Description | Required | 
| --- | --- | --- | 
| `-amount [decimal]` |  The amount of bonus to give the Worker. <br />Example: `-amount 10.50` | Yes | 
| `-assignment [assignment ID]` |  The ID of the assignment associated with this bonus. <br /> Example: `-assignment ZYJZWSCAT0DZRFY5KYP00S0ZS8Y5H0NZR9YAMY1Z`  | Yes | 
| `-help` or `-h` |  Displays the help for this operation. <br />Example: `-help` | No | 
| `-reason [text]` |  The reason for the bonus. You must enclose the string in quotation marks. <br />Example: `-reason "You did the most work last week."` | Yes | 
| `-sandbox` |  Runs this command in the Amazon Mechanical Turk sandbox. This argument takes precedence even if you specify the production web site in your `mturk.properties` file. <br /> Example:`-sandbox`  | No | 
| `-workerid [workerID]` |  The ID of the Worker who gets the bonus. <br />Example: `-workerid A3C4G8DMXFG5PQ` | Yes | 

## Example
<a name="w2aab9c40b6"></a>

 The following examples for Unix and Windows show how to use the `grantBonus` command. 

### Unix
<a name="w2aab9c40b6b4"></a>

 The following example demonstrates how to call this command from Unix. 

```
./grantBonus.sh -workerid A3C4G8DMXFG5PQ -assignment 0YFZ2TYJF3HZPGZV4Z40EZD4YZZFDSTZ0YG78W2Z -reason "Your answers are very accurate." -amount 5.00
```

### Windows
<a name="w2aab9c40b6b6"></a>

 The following example demonstrates how to call this command from Microsoft Windows. 

```
grantBonus -workerid A3C4G8DMXFG5PQ -assignment 0YFZ2TYJF3HZPGZV4Z40EZD4YZZFDSTZ0YG78W2Z-reason "Your answers are very accurate." -amount 5.00
```

## Output
<a name="w2aab9c40b8"></a>

These examples produce output similar to the following.

```
Granted bonus to A3C4G8DMXFG5PQ
```