# Amazon SWF in AWS GovCloud (US)

Amazon Simple Workflow Service (Amazon SWF) makes it easy to build applications that coordinate work across distributed components. In Amazon SWF, a task represents a logical unit of work that is performed by a component of your application. Coordinating tasks across the application involves managing intertask dependencies, scheduling, and concurrency in accordance with the logical flow of the application. Amazon SWF gives you full control over implementing tasks and coordinating them without worrying about underlying complexities such as tracking their progress and maintaining their state.

## How Amazon Simple Workflow Service Differs for AWS GovCloud (US)

This service has no differences between the AWS GovCloud (US) and the standard AWS Regions.

## Documentation for Amazon Simple Workflow Service

[Amazon SWF documentation](http://aws.amazon.com/documentation/swf/ "http://aws.amazon.com/documentation/swf/").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- No export-controlled data can be entered, stored, or processed in Amazon SWF.
- Amazon SWF metadata is not permitted to contain export-controlled data. This metadata
  includes all of the configuration data that you enter when setting up and maintaining your
  workflows.

For example, do not enter export-controlled data in the following fields:

    + Workflow type name
    + Workflow type version
    + Activity type name
    + Activity type version
    + Execution workflow ID
    + Activity task ID
    + The `input`, `result`, or `details` arguments to
     workflow executions
    + The `input`, `result`, or `details` arguments to
     activity tasks
