NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Best practices for AWS Application Migration Service

## Planning

During the phases of your migration project, review these best practices to help you to a successful outcome.

1. Plan your Migration project prior to installing the AWS Replication Agent on your source
   servers.
2. Do not perform any reboots on the source servers prior to a cutover.
3. Do not archive or disconnect the source server from AWS until your launched cutover
   instance in AWS is working as expected.

## Testing

1. Perform test at least two weeks before you plan to migrate your source servers. This time
   frame is intended for identifying potential problems and solving them, before the actual
   cutover takes place. After performing the test launch, validate connectivity to your test
   instances (using SSH for Linux or RDP for Windows), and perform acceptance tests for your
   application.
2. Ensure that you perform a Test prior to performing a cutover.

## Successful implementation

The following are the required steps to complete a successful migration implementation with
AWS Application Migration Service:

1. Deploy the AWS Replication Agent on your source servers.
2. Confirm that the data replication status is **Healthy**.
3. Test the launch of Test instances a week before the actual cutover.
4. Address any issues that come up, such as Launch setting misconfiguration and potential
   AWS limits.
5. Launch cutover instances for the servers on the planned date.

## Ensuring project success

1. Train a field technical team & assign an AWS Application Migration Service SME.
2. Share project timelines with AWS Application Migration Service.
3. Monitor data replication progress and report any issues in advance.
4. Perform a test for every server in advance, and report issues to AWS Application Migration Service.
5. Coordinate cutover windows with AWS Application Migration Service in advance.
