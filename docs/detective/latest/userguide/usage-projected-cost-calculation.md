# How Amazon Detective calculates projected cost

To calculate the projected cost values that it displays on the **Usage**
page, Detective does the following.

1. To get the projected cost for an individual account in a behavior graph, Detective does the
   following.
   1. Calculates the average volume per day. It adds the data volume across all of the active
      days and then divides by the number of days that the account has been active.

   If the account was enabled more than 30 days ago, then the number of days is 30. If the
   account was enabled fewer than 30 days ago, then it is the number of days since the acceptance
   date.

   For example, if the account was enabled 12 days ago, then Detective adds the volume ingested
   for those 12 days and then divides it by 12. 2. Multiplies the account's daily average by 30. This is the projected 30-day usage for the
   account. 3. Uses its pricing model to calculate the projected 30-day cost for the projected 30-day
   usage.

2. To get the total projected cost for a behavior graph, Detective does the following:
   1. Combines the projected 30-day usage from all of the accounts in the behavior
      graph.
   2. Uses its pricing model to calculate the projected 30-day cost for the total projected
      30-day usage.

3. To get the total projected cost for a member account across behavior graphs, Detective does the
   following:
   1. Combines the projected 30-day usage across all of the behavior graphs.
   2. Uses its pricing model to calculated the projected 30-day cost for the total projected
      30-day usage.

4. If you are using a shared Amazon VPC, Detective calculates the projected cost based on monitoring
   activity. We recommend that you review the projected cost for your investigations specific to
   your environment.
   1. If a Detective member account has a shared Amazon VPC and there are other non-Detective accounts using
      the shared VPC, Detective will monitor all traffic from that VPC. The usage and cost will increase
      and Detective will provide visualization on all the traffic flow within the VPC.
   2. If you have an EC2 instance inside a shared Amazon VPC and the shared owner is not a Detective
      member, Detective will not monitor any traffic from the VPC, and the usage and cost will decrease.
      If you want to view the traffic flow within the VPC, you must add the Amazon VPC owner as a member
      of your Detective graph.
