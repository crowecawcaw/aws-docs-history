


|  | 
| --- |
| **This software is not currently supported by Amazon Mechanical Turk**<br />The Amazon Mechanical Turk Command Line Tools (CLT) are not currently maintained by Amazon Mechanical Turk. If you would still like to use Amazon Mechanical Turk from the command line, use the `mturk` command in the AWS Command Line Interface (CLI). For more information, see the `mturk` section of the [ AWS CLI Command Reference ](https://docs.aws.amazon.com/cli/latest/reference/mturk/index.html).  | 

 

# approveWork
<a name="CLTReference_ApproveWorkCommand"></a>

## Description
<a name="w2aab9c10b2"></a>

 The `approveWork` command approves assignments Workers have submitted to Amazon Mechanical Turk. To specify the assignments to approve you can: 
+  Obtain the assignment IDs from a call to [getResults](CLTReference_GetResultsCommand.md) then call the `approveWork` command and use the `assignment` argument to list the IDs. When you use this argument, you are prompted to provide optional comments that the Worker can see in the **Status** section of the web site. 
+  Use the file that a call the `getResults` returns as the `approvefile` argument. You can provide optional comments for Workers in this file. For information about the format of this file, see [Files Used by the Command Line Tools](CLTFilesArticle.md). 
+  Provide a path to the `.success` file that a call to [loadHITs](CLTReference_LoadHITsCommand.md) returns. The `approveWork` command attempts to approve all assignments for all HITs in the `.success` file. 

 When you use this command, it initiates two payments from your Requester account. Amazon Mechanical Turk pays the reward specified in the HIT to the Worker who submitted the assignment, and also debits your account for any fees. If your Requester account does not have adequate funds for these payments, this command returns an error. 

## Arguments
<a name="w2aab9c10b4"></a>

 The following table describes the arguments for the `approveWork` command. 


| Name | Description | Required | 
| --- | --- | --- | 
| `-approvefile [filename]` |  The name of a text file that contains a list of assignment IDs and, optionally, approval comments. For information about this file, see *The approve file* in [Files Used by the Command Line Tools](CLTFilesArticle.md). <br />Condition: Required if neither the `-assignment` argument nor the `-successfile` argument is specified.<br />Example: `-approvefile helloworld_approve.txt` | Conditional | 
| `-assignment [assignment ID]` |  The assignment to approve. Multiple assignments IDs are comma separated. <br /> Condition: Required if neither the `-approvefile` argument nor the `-successfile` argument is specified.<br /> Example: `-assignment SYSZH6HTMKFG2ZDECWS0`  | Conditional | 
| `-force` |  Specifies *not* to prompt for manual confirmation before performing the operation. Only advanced developers should use this argument. <br />Example: `-force` | No | 
| `-help` or `-h` |  Displays the help for this operation. <br />Example: `-help` | No | 
| `-sandbox` |  Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes precedence even if you specify the production web site in your `mturk.properties` file. <br /> Example:`-sandbox`  | No | 
| `-successfile [path]` |  The path to the `.success` file that a call to [loadHITs](CLTReference_LoadHITsCommand.md) returned. This argument attempts to approve all assignments for all HITs in the file. For information about this file, see *The success file* in [Files Used by the Command Line Tools](CLTFilesArticle.md). <br />Condition: Required if neither the `-approvefile` argument nor the `-assignment` argument is specified.<br />Example: `-approvefile helloworld_approve.txt` | Conditional | 

## Example
<a name="w2aab9c10b6"></a>

 The following examples for Unix and Windows show how to use the `approveWork` command. The examples approve one assignment in the file `approval.txt`. 

### Unix
<a name="w2aab9c10b6b4"></a>

 The following example demonstrates how to call this command from Unix. 

```
./approveWork.sh -approvefile approval.txt
```

### Windows
<a name="w2aab9c10b6b6"></a>

 The following example demonstrates how to call this command from Microsoft Windows. 

```
approveWork -approvefile approval.txt
```

## Output
<a name="w2aab9c10b8"></a>

These examples produce the following output.

```
--- Starting approval ---
[62145TS44X94HHYGW0PZK2CP0E1K9T1PR8Z42WEZ] Assignment successfully approved 
for HIT 62145TS44X94HHYGW0PZ
--- Finished approval ---
  1 assignments approved.
  0 assignments failed to be approved.
```

## Related Commands
<a name="w2aab9c10c10"></a>

 
+  [rejectWork](CLTReference_RejectWorkCommand.md) 