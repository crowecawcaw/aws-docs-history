


|  | 
| --- |
| **This software is not currently supported by Amazon Mechanical Turk**<br />The Amazon Mechanical Turk Command Line Tools (CLT) are not currently maintained by Amazon Mechanical Turk. If you would still like to use Amazon Mechanical Turk from the command line, use the `mturk` command in the AWS Command Line Interface (CLI). For more information, see the `mturk` section of the [ AWS CLI Command Reference ](https://docs.aws.amazon.com/cli/latest/reference/mturk/index.html).  | 

 

# updateQualificationType
<a name="CLTReference_UpdateQualificationTypeCommand"></a>

## Description
<a name="w2aab9c73b2"></a>

 The `updateQualificationType` command updates the properties of your Qualification. 

## Arguments
<a name="w2aab9c73b4"></a>

 The following table describes the arguments for the `updateQualificationType` command. 


| Name | Description | Required | 
| --- | --- | --- | 
| `-answer [filename]` |  Specifies the Qualification Answer file that contains the new AnswerKey XML for the Qualification test. This file allows the Amazon Mechanical Turk system to automatically evaluate and score a Qualification request. For information about this file, see *The Qualification answer file* in [Files Used by the Command Line Tools](CLTFilesArticle.md). <br />Example: `-answer qualification.answer` | No | 
| `-help` or `-h` |  Displays the help for this operation. <br />Example: `-help` | No | 
| `-properties [filename]` |  Specifies the Qualification properties file that contains the new properties for the Qualification. The Qualification is updated with all the properties defined in the file. For information about this file, see *The Qualification properties file* in [Files Used by the Command Line Tools](CLTFilesArticle.md).  You cannot modify the title of a Qualification. <br />Example: `-properties qualification.properties` | No | 
| `-qualtypeid` |  The Qualification Type ID of the Qualification you want to update. This ID is in the `.success`file generated after you create the Qualification with the [createQualificationType](CLTReference_CreateQualificationTypeCommand.md) command. <br />Example: `-qualtypeid RWFZTKZ55ZPZXN1C8TDZ` | Yes | 
| `-question [filename]` |  Specifies the Qualification question file that contains the new Qualification test. For information about this file, see *The Qualification question file* in [Files Used by the Command Line Tools](CLTFilesArticle.md). <br />Example: `-question qualification.question` | No | 
| `-status [status value]` |  Specifies whether the Qualification is active or inactive. Inactive Qualifications are no longer available for Workers and cannot be used for new HITs. <br />Valid Values: Active \| Inactive<br />Example: `-status Active` | No | 
| `-sandbox` |  Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes precedence even if you specify the production web site in your `mturk.properties` file. <br /> Example:`-sandbox`  | No | 

## Example
<a name="w2aab9c73b6"></a>

 The following examples for Unix and Windows show how to use the `updateQualificationType` command. These examples update the Qualification test. 

### Unix
<a name="w2aab9c73b6b4"></a>

 The following example demonstrates how to call this command from Unix. 

```
./updateQualificationType.sh -qualtypeid RWFZTKZ55ZPZXN1C8TDZ -question survey.question
```

### Windows
<a name="w2aab9c73b6b6"></a>

 The following example demonstrates how to call this command from Microsoft Windows. 

```
updateQualificationType -qualtypeid RWFZTKZ55ZPZXN1C8TDZ -question survey.question
```

## Output
<a name="w2aab9c73b8"></a>

These examples produce the following output.

```
Updated qualification type RWFZTKZ55ZPZXN1C8TDZ
```