


|  | 
| --- |
| **This software is not currently supported by Amazon Mechanical Turk**<br />The Amazon Mechanical Turk Command Line Tools (CLT) are not currently maintained by Amazon Mechanical Turk. If you would still like to use Amazon Mechanical Turk from the command line, use the `mturk` command in the AWS Command Line Interface (CLI). For more information, see the `mturk` section of the [ AWS CLI Command Reference ](https://docs.aws.amazon.com/cli/latest/reference/mturk/index.html).  | 

 

# createQualificationType
<a name="CLTReference_CreateQualificationTypeCommand"></a>

## Description
<a name="w2aab9c19b2"></a>

 The `createQualificationType` command creates a Qualification that can be used for your HITs. You can use the arguments to specify files that contain the Qualification test and the answers for the test. You can also create a Qualification that does not require a test. For more information about Qualifications, see the [Amazon Mechanical Turk Developer Guide](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/). 

## Arguments
<a name="w2aab9c19b4"></a>

 The following table describes the arguments for the `createQualificationType` command. 


| Name | Description | Required | 
| --- | --- | --- | 
| `-answer [filename]` |  Specifies the file that contains the answers for the Qualification test. If this argument is omitted, you create a Qualification that does not require a test. For information about this file, see *The Qualification answer file* in [Files Used by the Command Line Tools](CLTFilesArticle.md). <br />Example: `-answer qualification.answers` | No | 
| `-help` or `-h` | Displays the help for this operation.<br />Example: `-help` | No | 
| `-noretry` |  Specifies that Workers can only request the Qualification once. <br />Example: `-noretry` | No | 
| `-properties [filename]` |  Specifies the Qualification properties file. For information about this file, see *The Qualification properties file* in [Files Used by the Command Line Tools](CLTFilesArticle.md). <br />Example: `-properties qualification.properties` | Yes | 
| `-question [filename]` |  Specifies the Qualification question file that contains the Qualification test. For information about this file, see *The Qualification question file* in [Files Used by the Command Line Tools](CLTFilesArticle.md). <br />Example:`-question qualification.question` | No | 
| `-sandbox` |  Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes precedence even if you specify the production web site in your `mturk.properties` file. <br /> Example:`-sandbox`  | No | 

## Example
<a name="w2aab9c19b6"></a>

 The following examples for Unix and Windows show how to use the `createQualificationType` command. The examples use the property file `qualification.properties` and the question file `qualification.question`. These examples create the qualification in the test environment. 

### Unix
<a name="w2aab9c19b6b4"></a>

 The following example demonstrates how to call this command from Unix. 

```
.createQualificationType.sh -properties qualification.properties -question qualification.question -noretry -sandbox
```

### Windows
<a name="w2aab9c19b6b6"></a>

 The following example demonstrates how to call this command from Microsoft Windows. 

```
createQualificationType -properties qualification.properties -question qualification.question -noretry -sandbox
```

## Output
<a name="w2aab9c19b8"></a>

 If this command completes successfully, it creates a `.success` file with the name specified in the `-properties` argument. For this example, the file is named `qualification.properties.success`. This file contains the Qualification Type ID of the newly created Qualification. This command also produces output similar to the following.

```
Created qualification type: KYJ4GZZ5G3M6TDCEWYF0
You can take the test here: 
http://workersandbox.mturk.com/mturk/requestqualification?qualificationId=KYJ4GZZ5G3M6TDCEWYF0
```

## Related Commands
<a name="w2aab9c19c10"></a>

 
+  [getQualificationRequests](CLTReference_GetQualificationRequestsCommand.md) 