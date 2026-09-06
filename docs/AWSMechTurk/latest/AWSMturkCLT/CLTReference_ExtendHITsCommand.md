


|  | 
| --- |
| **This software is not currently supported by Amazon Mechanical Turk**<br />The Amazon Mechanical Turk Command Line Tools (CLT) are not currently maintained by Amazon Mechanical Turk. If you would still like to use Amazon Mechanical Turk from the command line, use the `mturk` command in the AWS Command Line Interface (CLI). For more information, see the `mturk` section of the [ AWS CLI Command Reference ](https://docs.aws.amazon.com/cli/latest/reference/mturk/index.html).  | 

 

# extendHITs
<a name="CLTReference_ExtendHITsCommand"></a>

## Description
<a name="w2aab9c28b2"></a>

 The `extendHITs` command extends the expiration date or increases the maximum number of assignments for all HITs in the specified `-successfile`. If you extend the expiration date, and the HIT has not expired, the new expiration date is the existing date plus the amount of time specified. If the HIT has already expired, the new expiration date is the current time plus the amount of time specified. If you add additional assignments, you must be sure that you have enough funds to pay for the assignments. 

## Arguments
<a name="w2aab9c28b4"></a>

 The following table describes the arguments for the `extendHITs` command. 


| Name | Description | Required | 
| --- | --- | --- | 
| `-assignments [integer]` |  The number of assignments to add to the HITs. <br />Example: `-assignments 12` | No | 
| `-help` or `-h` |  Displays the help for this operation. <br />Example: `-help` | No | 
| `-hours [integer]` |  The amount of time, in hours, by which to extend the expiration date of the HITs. <br />Example: `-hours 12` | No | 
| `-sandbox` |  Runs this command in the Amazon Mechanical Turk sandbox. This argument takes precedence even if you specify the production web site in your `mturk.properties` file. <br /> Example:`-sandbox`  | No | 
| `-successfile [filename]` |  The path to the `.success` file that contains the HITs to extend. This is the file that [loadHITs](CLTReference_LoadHITsCommand.md) returns. For information about this file, see *The success file* in [Files Used by the Command Line Tools](CLTFilesArticle.md). <br /> Example:`-successfile ..\mysurvey\mysurvey.success`  | Yes | 

## Example
<a name="w2aab9c28b6"></a>

 The following examples for Unix and Windows show how to use the `extendHITs` command. These examples add four assignments and three hours to the five HITs in the `.success` file. 

### Unix
<a name="w2aab9c28b6b4"></a>

 The following example demonstrates how to call this command from Unix. 

```
./extendHITs.sh -successfile ..\mysurvey\mysurvey.success -assignments 4 -hours 3
```

### Windows
<a name="w2aab9c28b6b6"></a>

 The following example demonstrates how to call this command from Microsoft Windows. 

```
extendHITs -successfile ..\mysurvey\mysurvey.success -assignments 4 -hours 3
```

## Output
<a name="w2aab9c28b8"></a>

This example produces output similar to the following.

```
--- Starting to extend HITs ---
[0YFZ2TYJF3HZPGZV4Z40] Successfully extended HIT (1/5)
[4GMZSHZKKK9WT9M9XWA0] Successfully extended HIT (2/5)
[XYTZY0YK1W2ZTCZM9Z80] Successfully extended HIT (3/5)
[RZGZZ4Z6GXKTV5DX81B0] Successfully extended HIT (4/5)
[M26ZN61JMT9E4MG0M94Z] Successfully extended HIT (5/5)
--- Finished to extend HITs ---
  5 HITs have been extended (added 4 assignment(s), 3 hour(s))
  0 HITs failed to be extended.
```