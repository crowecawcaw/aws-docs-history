# Transitioning from customer to AWS managed

monitors

If you currently use multiple customer managed monitors to track individual accounts,
teams, or categories, you can transition to AWS managed monitors for simplified
management and automatic coverage.

**Transition Process**

1.  **Create your AWS managed monitor alongside existing
    customer managed monitors**
    - Choose the dimension that matches your primary cost organization
      method
    - The AWS managed monitor will begin tracking all values
      automatically

2.  **Verify detection coverage**
    - Allow the AWS managed monitor to run for at least 24-48 hours
    - Compare detected anomalies with your existing customer managed
      monitors
    - Ensure the AWS managed monitor is detecting anomalies as
      expected

3.  **Configure alert subscriptions**
    - Set appropriate thresholds for your AWS managed monitor
    - Note that alert subscriptions attached to AWS managed monitors
      use the same threshold across all tracked values
    - For value-specific routing, configure AWS User Notifications
      with JSON patterns

4.  **Remove redundant customer managed monitors**

        * After confirming complete coverage, delete individual customer
         managed monitors
        * Keep any customer managed monitors that serve specific purposes
         (such as grouping related accounts)

    **Example transition scenario:** If you have 50 customer
    managed monitors tracking individual application teams via cost allocation tags:

5.  Create one AWS managed cost allocation tag monitor using your team tag
    key
6.  Verify it detects anomalies across all teams
7.  Configure alert subscriptions with appropriate thresholds
8.  Delete the 50 individual customer managed monitors
    **Important notes:**

- Direct conversion from customer managed to AWS managed monitors is not
  supported
- AWS managed monitors may initially generate more anomaly detections
  due to comprehensive coverage
- Historical anomaly data from customer managed monitors is preserved when
  you delete them (available via API only; deleted monitors and their anomalies do not
  appear in the console)
- Consider keeping some customer managed monitors for specific use cases
  requiring different thresholds
