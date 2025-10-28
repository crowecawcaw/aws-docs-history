# AWS Direct Connect Failover Test

The AWS Direct Connect Resiliency Toolkit resiliency models are designed to ensure that you have the
appropriate number of virtual interface connections in multiple locations. After you
complete the wizard, use the AWS Direct Connect Resiliency Toolkit failover test to bring down the BGP peering
session in order to verify that traffic routes to one of your redundant virtual interfaces,
and meets your resiliency requirements.

Use the test to make sure that traffic routes over redundant virtual interfaces when a
virtual interface is out of service. You start the test by selecting a virtual interface,
BGP peering session, and how long to run the test. AWS places the selected virtual
interface BGP peering session in the down state. When the interface is in this state,
traffic should go over a redundant virtual interface. If your configuration does not contain
the appropriate redundant connections, the BGP peering session fails, and traffic does not
get routed. When the test completes, or you manually stop the test, AWS restores the BGP
session. After the test is complete, you can use the AWS Direct Connect Resiliency Toolkit to adjust your
configuration.

###### Note

Do not use this feature during a Direct Connect maintenance period as the BGP session might
be restored prematurely either during or after the maintenance.

## Test history

AWS deletes the test history after 365 days. The test history includes the status for
tests that were run on all BGP peers. The history includes which BGP peering sessions
were tested, the start and end times, and the test status, which can be any of the
following values:

- In progress - The test is currently running.
- Completed - The test ran for the time that you
  specified.
- Cancelled - The test was cancelled before the specified time.
- Failed - The test did not run for the time that you
  specified. This can happen when there is an issue with the router.

For more information, see [View AWS Direct Connect Resiliency Toolkit virtual interface failover test history](view_failover_test.md "view_failover_test.md").

## Validation permissions

The only account that has permission to run the failover test is the account that owns
the virtual interface. The account owner receives an indication through AWS CloudTrail that a
test ran on a virtual interface.

###### Topics

- [Start a virtual interface failover
  test](start_failover_test.md "start_failover_test.md")
- [View a virtual interface failover test history](view_failover_test.md "view_failover_test.md")
- [Stop a virtual interface failover
  test](stop_failover_test.md "stop_failover_test.md")
