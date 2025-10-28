# Differential privacy policy

The differential privacy policy controls how many aggregation functions the member who can
query is allowed to run in a collaboration. The **Privacy budget** defines a
common, finite resource that is applied all tables in a collaboration. The **Noise
added per query** governs the rate at which the privacy budget is depleted.

A differential privacy policy is required to make your differential privacy protected
tables available for querying. This is a one-time step in a collaboration and includes two
inputs:

- **Privacy budget** – Quantified in terms of epsilon, the
  privacy budget controls the level of privacy protection. It is a common, finite resource
  that is applied for all of your tables protected with differential privacy in the
  collaboration, because the goal is to preserve the privacy of your users whose information
  can be present in multiple tables.

The **Privacy budget** is consumed every time a query is run on your
tables. When the privacy budget is fully exhausted, the collaboration member who can query
can't run additional queries until it is increased or refreshed. By setting a larger
privacy budget, the member who can receive results can reduce their uncertainty about
individuals within the data. Choose a privacy budget that balances your collaboration
requirements against your privacy needs and after consulting with business
decision-makers.

You can select **Refresh privacy budget monthly** to automatically
create a new privacy budget each calendar month, if you plan to regularly bring new data
into the collaboration. Choosing this option allows arbitrary amounts of information to be
revealed about rows of the data when repeatedly queried across refreshes. Avoid choosing
this if the same rows will be repeatedly queried between privacy budget refreshes.

- **Noise added per query** is measured in terms of the number of users
  whose contributions you want to obscure. This value governs the rate at which the privacy
  budget is depleted. A larger noise value reduces the rate at which the privacy budget is
  depleted, and therefore allows more queries to be run on your data. However, this should
  be balanced against releasing less accurate data insights. Consider the desired accuracy
  for collaboration insights when setting this value.
  You can use the default differential privacy policy to quickly complete the setup or
  customize your differential privacy policy as per your use case. AWS Clean Rooms Differential Privacy
  provides intuitive controls to configure the policy. AWS Clean Rooms Differential Privacy lets you
  preview the utility in terms of the number of aggregations possible across all queries on your
  data and estimate how many queries can be run in a data collaboration.

You can use the interactive examples to understand how different values of
**Privacy budget** and **Noise added per query** would
impact the results for different types of SQL queries. In general, you need to balance your
privacy needs against the number of queries you want to permit and the accuracy of those
queries. A smaller **Privacy budget** or larger **Noise added per
query** can better protect user privacy, but provides less meaningful insights to
your collaboration partners.

If you increase the **Privacy budget** while keeping the **Noise
added per query** parameter the same, the member who can query can run more
aggregations on your tables in the collaboration. You can increase the **Privacy
budget** any time during the collaboration. If you decrease the **Privacy
budget** while keeping the **Noise added per query** parameter the
same, the member who can query can run fewer aggregations. You can't decrease the
**Privacy budget** after the member who can query has started analyzing
your data.

If you increase the **Noise added per query** while keeping the
**Privacy budget** input the same, the member who can query can run more
aggregations on your tables in the collaboration. If you decrease the **Noise added
per query** while keeping the **Privacy budget** input the same,
the member who can query can run fewer aggregations. You can increase or decrease the
**Noise added per query** any time during the collaboration.

The differential privacy policy is managed by the privacy budget template API
actions.
