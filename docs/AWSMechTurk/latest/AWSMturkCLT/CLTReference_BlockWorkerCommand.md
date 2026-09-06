


|  | 
| --- |
| **This software is not currently supported by Amazon Mechanical Turk**<br />The Amazon Mechanical Turk Command Line Tools (CLT) are not currently maintained by Amazon Mechanical Turk. If you would still like to use Amazon Mechanical Turk from the command line, use the `mturk` command in the AWS Command Line Interface (CLI). For more information, see the `mturk` section of the [ AWS CLI Command Reference ](https://docs.aws.amazon.com/cli/latest/reference/mturk/index.html).  | 

 

# blockWorker
<a name="CLTReference_BlockWorkerCommand"></a>

## Description
<a name="w2aab9c16b2"></a>

 The `blockWorker` command blocks a Worker from working on your HITs. 

## Arguments
<a name="w2aab9c16b4"></a>

 The following table describes the arguments for the `blockWorker` command. 


| Name | Description | Required | 
| --- | --- | --- | 
| `-help` or `-h` | Displays the help for this operation.<br />Example: `-help` | No | 
| `-reason [string]` |  The reason why the Worker is being blocked. This reason is logged in our system for auditing purposes and can be used to determine if corrective action against the Worker is necessary. Enclose the reason string in quotation marks.<br /> Example: `-reason "After several warnings, the Worker continued to submit answers without reading the instructions carefully."` | Yes | 
| `-sandbox` |  Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes precedence even if you specify the production web site in your `mturk.properties` file. <br /> Example:`-sandbox`  | No | 
| `-workerid [Worker ID]` | The ID of the Worker you want to block.<br />Example: `-workerid A3C4G8DMXFG5PQ` | Yes | 

## Example
<a name="w2aab9c16b6"></a>

 The following examples for Unix and Windows show how to use the `blockWorker` command. 

### Unix
<a name="w2aab9c16b6b4"></a>

 The following example demonstrates how to call this command from Unix. You must write this command on a single line. It is divided into multiple lines in this example for readability. 

```
./blockWorker.sh -workerid A3C4G8DMXFG5PQ -reason "After several warnings, the Worker continued to 
submit answers without reading the instructions carefully."
```

### Windows
<a name="w2aab9c16b6b6"></a>

 The following example demonstrates how to call this command from Microsoft Windows. You should write this command on a single line. It is divided into multiple lines in this example for readability. 

```
blockWorker -workerid A3C4G8DMXFG5PQ -reason "After several warnings, the Worker continued to 
submit answers without reading the instructions carefully."
```

## Output
<a name="w2aab9c16b8"></a>

These examples produce the following output.

```
Blocked A3C4G8DMXFG5PQ with reason: After several warnings, the Worker continued to submit answers without reading the instructions carefully.
```

## Related Commands
<a name="w2aab9c16c10"></a>

 
+  [unblockWorker](CLTReference_UnblockWorkerCommand.md) 