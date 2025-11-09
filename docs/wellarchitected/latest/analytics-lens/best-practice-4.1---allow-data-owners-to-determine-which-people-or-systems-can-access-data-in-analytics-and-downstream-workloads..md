# Best practice 4.1 – Allow data owners to determine which people or systems can access data in analytics and downstream workloads

Data owners are the people that have direct responsibility
for data protection. For instance, the data owners want to
determine which data is publicly accessible, or which data
is restricted access to whom or what systems. The data
owners should be able to provide data access rules, so that
the analytics workload can implement the rules.

## Suggestion 4.1.1 – Identify data owners and assign roles

Data ownership is the management and oversight of an
organization's data assets to help provide business users
with high-quality data that is easily accessible in a
consistent manner. Because the analytics workload
consolidates multiple datasets into a central place, each
dataset is owned by different teams or people. So, it is
important for the analytics workload to identify which
dataset is owned by whom to have the owners control the
data access permissions.

## Suggestion 4.1.2 – Identify permission using a permission matrix for users and roles based on actions performed on the data by users and downstream systems

To aid in identifying and communicating data-access
permissions, an Access Control Matrix is a helpful method
to document which users, roles, or systems have access to
which datasets, and to describe what actions they can
perform. Below is a sample matrix for two users, and two
roles for two schemas with a table in them:

Table 1: Example Access Control Matrix for Users and Roles

| **Permissions**     | **Read**                   | **Write**    |
| ------------------- | -------------------------- | ------------ |
| Schema 1            | User1, User2, Role1, Role2 | Role1        |
| Schema 1 / Table 1  | User1, User2, Role1, Role2 | Role2        |
| Schema 2            | User1, User2, Role1, Role2 | User1, Role1 |
| Schema 2 / Table 2v | User1, User2, Role1, Role2 | User2, Role2 |

The matrix format can help identify the least permissions
that are required by various resources and to avoid
overlaps. An Access Control Matrix should be thought of as
an abstract model of permissions at a given point in time.
Periodically review the actual access permissions against
the permission matrix document to ensure accuracy.
