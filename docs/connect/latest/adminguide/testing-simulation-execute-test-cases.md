# Execute test cases

When you run a test, you are simulating a real interaction with your contact
center experience. A new contact is created to simulate inputs (for example, DTMF,
text/utterance), and your interaction groups begin executing. Each interaction
group is expected to execute exactly once.

In a test flow with multiple interaction groups, whether connected or not, if
an interaction group does not result in a successful validation where the observe
block fails to match an event from the contact flow, the test will eventually
time out after 5 minutes with a failure status.

When interaction groups are connected in sequence, each group depends on the
successful validation of the prior group. If a prior interaction group fails to
observe its expected event, subsequent interaction groups will not be executed.
The test will eventually time out after 5 minutes with a failure status.

When an interaction group is not connected to any other interaction groups, it
is triggered when a matching event occurs independently of any dependent groups.
With independent interaction groups, you can validate experiences that might occur in an undetermined
sequence.

During test execution, please be aware of the following limitations and behaviors:

- **Test Execution Record Retention:** Test execution results and their respective records are retained for 30 days from the execution date for any test cases run before February 9th, 2026. Tests run on or after that date will have their records kept indefinitely.
- **Concurrent Test Limit:** You can run up to 5 concurrent
  tests. Additional tests will remain in Queue state while 5 test cases are
  actively running.
- **Test Execution Queue Capacity:** The system accepts up to 100 test executions in the queue including the five running tests. Any requests exceeding this limit will be rejected.
- **Test Duration Limit:** Each test simulation has a maximum duration of 5 minutes. If a simulation exceeds this time limit, the test execution will automatically timeout and terminate.
- **Automatic Timeout:** Tests that are not manually ended using Action block test commands will automatically timeout after 5 minutes of total execution time.
- **Agent Queue Interaction:** If you do not end the test before the simulated contact is transferred to a queue, the simulated contact might reach the agent queue and connect with a live agent as a contact.
  To prevent simulated contacts from reaching live agents, consider these approaches:

###### Best practice to handle simulated contact in the agent queue

- **Proactive Test Termination:** Use Action blocks to end tests before simulated contacts reach agents, preventing disruption to live operations if applicable.
- **Test Queue Substitution:** Use Action blocks to replace production queues with dedicated test queues in your test case configuration, ensuring real agents are not impacted.

###### To execute a test case

1. Choose **Run Test** to execute the test case.

![Flow designer showing three connected states: initial setup, welcome prompt, and transfer to queue.](images/GIF/test-execution-trigger-gif.gif) 2. After the test case is running, choose the **Test runs** tab to view a
list of in progress and completed test runs for the tests case.

![Test runs tab showing three test runs from November 19, 2025 with Passed outcomes.](images/test-runs.png) 3. Choose a test run to see the interaction block execution status, the
simulated contact ID, and the pass or fail status of each step.

![Test run details showing passed status with session metrics, contact flow information, and test steps.](images/test-execution-detail-page.png)
You can also view all the test runs across all test cases in the
**Test runs** tab. This page lists all of the test executions
in the same Connect Customer instance. You will only see the detail test results for the test
cases you created or test cases you have permission to view.

![Test runs tab showing eight test executions with names, dates, and pass or fail outcomes.](images/test-run-list-page.png)
