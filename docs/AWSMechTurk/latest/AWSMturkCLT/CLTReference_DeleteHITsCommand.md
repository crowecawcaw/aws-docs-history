


|  | 
| --- |
| **This software is not currently supported by Amazon Mechanical Turk**<br />The Amazon Mechanical Turk Command Line Tools (CLT) are not currently maintained by Amazon Mechanical Turk. If you would still like to use Amazon Mechanical Turk from the command line, use the `mturk` command in the AWS Command Line Interface (CLI). For more information, see the `mturk` section of the [ AWS CLI Command Reference ](https://docs.aws.amazon.com/cli/latest/reference/mturk/index.html).  | 

 

# deleteHITs
<a name="CLTReference_DeleteHITsCommand"></a>

## Description
<a name="w2aab9c22b2"></a>

 The `deleteHITs` command deletes your HITs from Amazon Mechanical Turk. Use the arguments to specify how to handle assignments that have not been approved or are still available to Workers. You specify the HITs to delete in a file, which you generate as the output of [getResults](CLTReference_GetResultsCommand.md). 

## Arguments
<a name="w2aab9c22b4"></a>

 The following table describes the arguments for the `deleteHITs` command. 


| Name | Description | Required | 
| --- | --- | --- | 
| `-approve` | Automatically approves any assignments that have been submitted and have not been approved or rejected. Assignments that are in the review or reviewing states cannot be deleted. <br />Example: `-approve` | No | 
| `-expire` | Automatically expires any HITs that are still available to Workers on Amazon Mechanical Turk. Live HITs cannot be deleted. <br />Example: `-expire` | No | 
| `-force` | Specifies *not* to prompt for manual confirmation before deleting the HITs. Only advanced developers should use this argument. <br />Example: `-force` | No | 
| `-help` or `-h` | Displays the help for this operation. <br />Example:`-help` | No | 
| `-sandbox` | Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes precedence even if you specify the production web site in your `mturk.properties` file. <br /> Example:`-sandbox`  | No | 
| `-successfile [filename]` |  Specifies the success file that contains the HITs to be deleted. For information about this file, see *The success file* in [Files Used by the Command Line Tools](CLTFilesArticle.md). <br />Example: `-successfile helloworld.success` | Yes | 

## Example
<a name="w2aab9c22b6"></a>

 The following examples for Unix and Windows show how to use the `deleteHITs` command. This example deletes five assignments in the file `survey.success`. If any HITs in the file have been submitted, this example approves them. If any HITs are still available, this example expires them. 

### Windows
<a name="w2aab9c22b6b4"></a>

 The following example demonstrates how to call this command from Microsoft Windows. 

```
deleteHITs -successfile survey.success -approve -expire
```

### Unix
<a name="w2aab9c22b6b6"></a>

 The following example demonstrates how to call this command from Unix. 

```
./deleteHITs.sh -successfile survey.success -approve -expire
```

## Output
<a name="w2aab9c22b8"></a>

These examples produce the following output.

```
--- Starting to delete HITs ---
You are about to delete 5 HITs.
To confirm this operation, please press ENTER (or press Ctrl+C to abort):

[X1F6ZRZ8GW1ETS561XR0] Successfully deleted HIT (1/5)
[8X3GV2YWKAZZR9ZCEYB0] Successfully deleted HIT (2/5)
[YA3ZKSYWVWMWZ053TYKZ] Successfully deleted HIT (3/5)
[DYBZQP51T3VEKHXXFWR0] Successfully deleted HIT (4/5)
[F09PWRZ81WDEW5Z2FZJZ] Successfully deleted HIT (5/5)
--- Finished to delete HITs ---
  5 HITs have been deleted or were deleted previously.
  0 errors occurred.
```