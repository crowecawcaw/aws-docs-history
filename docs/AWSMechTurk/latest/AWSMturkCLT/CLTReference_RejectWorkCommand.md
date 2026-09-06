


|  | 
| --- |
| **This software is not currently supported by Amazon Mechanical Turk**<br />The Amazon Mechanical Turk Command Line Tools (CLT) are not currently maintained by Amazon Mechanical Turk. If you would still like to use Amazon Mechanical Turk from the command line, use the `mturk` command in the AWS Command Line Interface (CLI). For more information, see the `mturk` section of the [ AWS CLI Command Reference ](https://docs.aws.amazon.com/cli/latest/reference/mturk/index.html).  | 

 

# rejectWork
<a name="CLTReference_RejectWorkCommand"></a>

## Description
<a name="w2aab9c52b2"></a>

 The `rejectWork` command rejects assignments submitted by Workers. You can reject single assignments, or you can specify a file that contains the assignments to reject. 

## Arguments
<a name="w2aab9c52b4"></a>

 The following table describes the arguments for the `rejectWork` command. 


| Name | Description | Required | 
| --- | --- | --- | 
| `-assignment [assignment IDs]` |  Specifies the assignment ID to reject. For multiple assignments, separate each assignment ID with a comma. <br />Condition: Required if the `rejectfile` argument is not specified.<br /> Example: `-assignment 0YFZ2TYJF3HZPGZV4Z40EZD4YZZFDSTZ0YG78W2Z`  | Conditional | 
| `-force` |  Specifies *not* to prompt for manual confirmation before performing the reject operation. Only advanced developers should use this argument. <br />Example: `-force` | No | 
| `-help` or `-h` |  Displays the help for this operation. <br />Example: `-help` | No | 
| `-rejectfile [filename]` |  Specifies a text file that contains a list of assignment IDs and optional rejection comments. For information about this file, see *The reject file* in [Files Used by the Command Line Tools](CLTFilesArticle.md). <br />Condition: Required if the `assignment` argument is not specified.<br />Example: `-rejectfile helloworld_reject.txt` | Conditional | 
| `-sandbox` |  Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes precedence even if you specify the production web site in your `mturk.properties` file. <br /> Example:`-sandbox`  | No | 

## Example
<a name="w2aab9c52b6"></a>

 The following examples for Unix and Windows show how to use the `rejectWork` command. These examples reject the specified assignment with no additional comments. 

### Unix
<a name="w2aab9c52b6b4"></a>

 The following example demonstrates how to call this command from Unix. 

```
./rejectWork.sh -assignment 0YFZ2TYJF3HZPGZV4Z40EZD4YZZFDSTZ0YG78W2Z 
```

### Windows
<a name="w2aab9c52b6b6"></a>

 The following example demonstrates how to call this command from Microsoft Windows. 

```
rejectWork -assignment 0YFZ2TYJF3HZPGZV4Z40EZD4YZZFDSTZ0YG78W2Z
```

## Output
<a name="w2aab9c52b8"></a>

These examples produce the following output.

```
You are about to reject 1 assignment(s).
To confirm this operation, please press ENTER (or press Ctrl+C to abort):

If you would like to supply a comment to the worker(s), please type it below then press ENTER. 
If not, just hit ENTER:
	
[0YFZ2TYJF3HZPGZV4Z40EZD4YZZFDSTZ0YG78W2Z] Assignment successfully rejected with comment ()
```