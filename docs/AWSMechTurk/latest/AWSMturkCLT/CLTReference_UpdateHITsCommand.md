


|  | 
| --- |
| **This software is not currently supported by Amazon Mechanical Turk**<br />The Amazon Mechanical Turk Command Line Tools (CLT) are not currently maintained by Amazon Mechanical Turk. If you would still like to use Amazon Mechanical Turk from the command line, use the `mturk` command in the AWS Command Line Interface (CLI). For more information, see the `mturk` section of the [ AWS CLI Command Reference ](https://docs.aws.amazon.com/cli/latest/reference/mturk/index.html).  | 

 

# updateHITs
<a name="CLTReference_UpdateHITsCommand"></a>

## Description
<a name="w2aab9c67b2"></a>

 The `updateHITs` command updates properties of HITs that are already on Amazon Mechanical Turk. 

 All properties of a HIT can be modified: 
+ Title
+ Description
+ Keywords
+ AssignmentDurationInSeconds
+ AutoApprovalDelayInSeconds
+ Qualification requirements

 

**Important**  
 The Reward property can only be updated for HITs that do not have any assignments that have been accepted, submitted, approved or rejected. 

## Arguments
<a name="w2aab9c67b4"></a>

 The following table describes the arguments for the `updateHITs` command. 


| Name | Description | Required | 
| --- | --- | --- | 
| `-properties [filename]` |  The HIT properties file that contains the new properties for the HITs. The HITs are updated with all the values defined in this file. For information about this file, see *The HIT properties file* in [Files Used by the Command Line Tools](CLTFilesArticle.md). <br />Example: `-properties helloworld.properties` | Yes | 
| `-help` or `-h` |  Displays the help for this operation. <br />Example: `-help` | No | 
| `-sandbox` |  Runs this command in the Amazon Mechanical Turk sandbox for testing. This argument takes precedence even if you specify the production web site in your `mturk.properties` file. <br /> Example:`-sandbox`  | No | 
| `-success [filename]` |  Specifies the success file that contains the IDs of the HITs to be updated. For information about this file, see *The success file* in [Files Used by the Command Line Tools](CLTFilesArticle.md). <br />Example: `-success helloworld.success` | Yes | 

## Example
<a name="w2aab9c67b6"></a>

 The following examples for Unix and Windows show how to use the `updateHITs` command. These examples update four HITs in the file `..\survey\survey.success` with the new properties in the file `..\survey\survey.properties` 

### Unix
<a name="w2aab9c67b6b4"></a>

 The following example demonstrates how to call this command from Unix. 

```
./updateHITs.sh -success ..\survey\survey.success -properties ..\survey\survey.properties
```

### Windows
<a name="w2aab9c67b6b6"></a>

 The following example demonstrates how to call this command from Microsoft Windows. 

```
updateHITs -success ..\survey\survey.success -properties ..\survey\survey.properties
```

## Output
<a name="w2aab9c67b8"></a>

These examples produce the following output.

```
--[Initializing]----------
 Success File: ..\survey\survey.success
 Properties: ..\survey\survey.properties
--[Updating HITs]----------
  Start time: Fri Dec 14 16:48:03 PST 2007
  Input: 4 hitids
  New HITTypeId: SWZZPTZ7Y14ZY8WXNZH0
Updated HIT #0 (4GMZSHZKKK9WT9M9XWA0) to new HITTypeId SWZZPTZ7Y14ZY8WXNZH0
Updated HIT #1 (XYTZY0YK1W2ZTCZM9Z80) to new HITTypeId SWZZPTZ7Y14ZY8WXNZH0
Updated HIT #2 (RZGZZ4Z6GXKTV5DX81B0) to new HITTypeId SWZZPTZ7Y14ZY8WXNZH0
Updated HIT #3 (M26ZN61JMT9E4MG0M94Z) to new HITTypeId SWZZPTZ7Y14ZY8WXNZH0
  End time: Fri Dec 14 16:48:05 PST 2007
--[Done Updating HITs]----------
4 HITS were processed
4 HITS were updated
  Total load time: 2 seconds.
```