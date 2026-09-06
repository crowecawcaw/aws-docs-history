

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Best practices for AWS Transform MGN
<a name="best_practices_mgn"></a>

## Planning
<a name="planning"></a>

During the phases of your migration project, review these best practices to help you to a successful outcome.

1. Plan your Migration project before installing the AWS Replication Agent on your source servers. 

1. Do not perform any reboots on the source servers before a cutover. 

1. Do not archive or disconnect the source server from AWS until your launched cutover instance in AWS is working as expected. 

## Testing
<a name="Testing"></a>

1. Perform a test at least two weeks before you plan to migrate your source servers. This time frame is intended for identifying potential problems and solving them, before the actual cutover takes place. After performing the test launch, validate connectivity to your test instances (using SSH for Linux or RDP for Windows), and perform acceptance tests for your application. 

1. Ensure that you perform a Test before performing a cutover. 

## Successful implementation
<a name="succesful-implementation"></a>

The following are the required steps to complete a successful migration implementation with AWS Transform MGN:

1. Deploy the AWS Replication Agent on your source servers. 

1. Confirm that the data replication status is **Healthy**. 

1. Test the launch of Test instances a week before the actual cutover. 

1. Address any issues that come up, such as Launch setting misconfiguration and potential AWS limits.

1. Launch cutover instances for the servers on the planned date. 

## Ensuring project success
<a name="project-success"></a>

1. Train a field technical team & assign an AWS Transform MGN SME.

1. Share project timelines with AWS Transform MGN.

1. Monitor data replication progress and report any issues in advance. 

1. Perform a test for every server in advance, and report issues to AWS Transform MGN.

1. Coordinate cutover windows with AWS Transform MGN in advance.