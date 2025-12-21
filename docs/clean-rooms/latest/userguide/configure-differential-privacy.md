# Configuring differential privacy policy

(optional)

###### Note

AWS Clean Rooms Differential Privacy is only available for collaborations where the data is stored in Amazon S3.

This procedure describes the process of configuring the differential privacy policy in a
collaboration by using the **Guided flow** option in the AWS Clean Rooms console.
This is a one-time step for all tables with differential privacy protection.

###### To configure differential privacy settings (guided flow)

1.  Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home").
2.  In the left navigation pane, choose **Collaborations**.
3.  Choose the collaboration.
4.  On the **Tables** tab of the collaboration page, choose
    **Configure differential privacy policy**.
5.  On the **Configure differential privacy policy** page, choose values
    for the following properties:

        * **Privacy budget**
        * **Refresh privacy budget monthly**
        * **Noise added per query**

    You can use the default values or enter custom values that support your specific use
    case. After choosing values for **Privacy budget** and **Noise
    added per query**, you can preview the resulting utility in terms of the number
    of aggregations that are possible across all queries on your data.

6.  Choose **Configure**.
    You’ll see a confirmation message that you’ve successfully configured the differential
    privacy policy for the collaboration.

Now that you configured differential privacy, you are ready to:

- [Query the data tables](running-sql-queries.md "running-sql-queries.md") (as a member who can
  query)
- [Collaborations](working-with-collaborations.md "working-with-collaborations.md") (if you're the
  collaboration creator)

## Viewing differential privacy usage logs

As a collaboration member who is protecting data with differential privacy, after you have
created a collaboration with differential privacy, you can monitor the usage of the privacy
budget.

###### To view how many aggregations were run and how much of the privacy budget was

used

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home").
2. In the left navigation pane, choose **Collaborations**.
3. Choose the collaboration.
4. Choose the **Tables** tab.
5. Choose **View usage logs** (blue text).
6. View the usage details, including the privacy budget and how much utility was
   provided.

## Editing a differential privacy policy

At any time after configuring the differential privacy policy, you can update it to better
reflect your privacy needs.

###### To edit the differential privacy policy

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home").
2. In the left navigation pane, choose **Collaborations**.
3. Choose the collaboration.
4. On the **Tables** tab of the collaboration page, under
   **Tables associated by you**, choose **Edit**.
5. On the **Edit differential privacy** page, choose new values for the
   following properties:
   - **Privacy budget** – Move the slider bar to either
     increase or decrease the budget at any point during a collaboration. You can't
     decrease the budget after the member who can query has started querying your data. If
     the **Privacy budget** is increased, AWS Clean Rooms will continue using the
     existing budget until it is fully consumed before utilizing the newly added privacy
     budget.
   - **Noise added per query** – Move the slider bar to either
     increase or decrease the **Noise added per query** at any point
     during a collaboration.

###### Note

You can chose **Interactive examples** to explore how different
values of **Privacy budget** and **Noise added per
query** affect the number of aggregate functions that you can run.

You can't change the value of the **Privacy budget refresh**. To
change your selection, you must delete the differential privacy policy and create a new
one. 6. Choose **Save changes**.

You see a confirmation message that you’ve successfully edited the differential privacy
policy.

## Deleting a differential privacy policy

You can delete the differential privacy policy from the **Tables** tab of
a collaboration.

###### To delete the differential privacy policy

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home").
2. In the left navigation pane, choose **Collaborations**.
3. Choose the collaboration.
4. On the **Tables** tab of the collaboration page, next to
   **Differential privacy policy**, select
   **Delete**.
5. If you’re certain that you want to delete the differential privacy policy, choose
   **Delete**.

After deleting a differential privacy policy, you can't access the privacy budget usage
logs from that policy. Tables with differential privacy turned on can't be queried if the
differential privacy policy is deleted.

## Viewing the calculated differential privacy

parameters

For users with expertise in differential privacy, you can view the calculated differential
privacy parameters from the **Analysis** tab of a collaboration.

###### To view the calculated differential privacy parameters

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home").
2. In the left navigation pane, choose **Collaborations**.
3. Choose the collaboration.
4. On the **Analysis** tab, in the **Results** section,
   select **View calculated differential privacy parameters**.

In the **Calculated differential privacy parameters** table, you can see
sensitivity values of aggregate functions, which is defined as the maximum amount by which the
result of a function can change if a single user's records are added, removed, or modified.
The list includes the following differential privacy parameters:

- **User contribution limit** (UCL) is the maximum number of rows
  contributed by a user in a SQL query. For example, if you want to count the total number
  of matched impressions in a specified campaign where each user can have multiple
  impressions, AWS Clean Rooms Differential Privacy needs to bound the number of impressions of a
  single user in order to ensure that the differential privacy calculation is accurate. In
  other words, if any user has more impressions than the bound, then AWS Clean Rooms automatically
  takes a uniform random sample of that user's impressions as per the computed UCL value and
  exclude the remaining impressions of that user while executing the query. The UCL value
  equals to 1 if you are counting the number of unique users. This is because adding,
  removing, or modifying a single user can change the count of distinct users by at most

1.

- **Minimum value** is the lower bound of an expression used within an
  aggregate function such as `sum()`. For example, if the expression is a column
  known as `purchase_value`, minimum value is the lower bound of the
  column.
- **Maximum value** is the upper bound of an expression used within an
  aggregate function such as `sum()`. For example, if the expression is a column
  known as `purchase_value`, maximum value is the upper bound of the column.

In the **Calculated differential privacy parameters** table, you can use
these parameters to better understand the total amount of noise in query results. For example,
when the configured **Noise added per query** is 30 users and a `COUNT
 DISTINCT (user_id)` query is run, then AWS Clean Rooms Differential Privacy adds random noise
that falls between -30 and 30 with high probability because the sensitivity of `COUNT
 DISTINCT` is 1. In the case of a `COUNT` query with the same configuration,
AWS Clean Rooms Differential Privacy adds statistical noise that is scaled by the user contribution
limit because a single user could contribute multiple rows to the query result. In the case of
`SUM` query like `SUM (purchase_value)` where all the column values
are positive, the total noise is scaled by the user contribution limit times the maximum
value. AWS Clean Rooms Differential Privacy automatically computes the sensitivity parameters to perform
noise addition at query run-time and depletes the privacy budget. The depletion of privacy
budget is required because the sensitivity parameters are data-dependent.
