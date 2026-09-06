


|  | 
| --- |
| **This software is not currently supported by Amazon Mechanical Turk**<br />The Amazon Mechanical Turk Command Line Tools (CLT) are not currently maintained by Amazon Mechanical Turk. If you would still like to use Amazon Mechanical Turk from the command line, use the `mturk` command in the AWS Command Line Interface (CLI). For more information, see the `mturk` section of the [ AWS CLI Command Reference ](https://docs.aws.amazon.com/cli/latest/reference/mturk/index.html).  | 

 

# unblockWorker
<a name="CLTReference_UnblockWorkerCommand"></a>

## Description
<a name="w2aab9c64b2"></a>

 The `unblockWorker` command unblocks a Worker who has been blocked from working on your HITs. 

## Arguments
<a name="w2aab9c64b4"></a>

 The following table describes the arguments for the `unblockWorker` command. 


| Name | Description | Required | 
| --- | --- | --- | 
| `-help` or `-h` |  Displays the help for this operation. <br />Example: `-help` | No | 
| `-reason` |  The reason why you are unblocking the Worker. This reason is logged in our system for auditing purposes. Enclose this string in quotation marks. <br />Example: `-reason "Made a mistake. Blocked the wrong Worker ID"` | Yes | 
| `-sandbox` |  Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes precedence even if you specify the production web site in your `mturk.properties` file. <br /> Example:`-sandbox`  | No | 
| `-workerid [worker ID]` |  The ID of the Worker to unblock. <br />Example: `-workerid A3C4G8DMXFG5PQ` | Yes | 

## Example
<a name="w2aab9c64b6"></a>

 The following examples for Unix and Windows show how to use the `unblockWorker` command. These examples unblock a specified Worker. 

### Unix
<a name="w2aab9c64b6b4"></a>

 The following example demonstrates how to call this command from Unix. 

```
./unblockWorker.sh -workerid A3C4G8DMXFG5PQ -reason "Made a mistake. Blocked the wrong Worker ID."
```

### Windows
<a name="w2aab9c64b6b6"></a>

 The following example demonstrates how to call this command from Microsoft Windows. 

```
unblockWorker -workerid A3C4G8DMXFG5PQ -reason "Made a mistake. Blocked the wrong Worker ID."
```

## Output
<a name="w2aab9c64b8"></a>

These examples produce the following output.

```
Unblocked A3C4G8DMXFG5PQ with reason:  Made a mistake. Blocked the wrong Worker ID.
```