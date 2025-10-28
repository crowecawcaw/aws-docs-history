After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Managed kdb Insights databases

A Managed kdb Insights database acts as a highly available and scalable repository to
store your kdb data files so that they can be used with one or more historical database
(HDB) clusters in FinSpace kdb. Data in a database may consist of either kdb objects, kdb
splayed tables, or kdb partitioned tables. These represent different types of kdb table
structures and each must follow a prescribed file and path layout. You can learn more about
each of these structures [here](https://code.kx.com/q/database/ "https://code.kx.com/q/database/").

Data is loaded into a database by defining a changeset, which lets you import a file or
set of files into a database. The files in the kdb database are placed into logical paths
called the _Database paths_. Creating a database does not
automatically load any data. You must add data to the kdb database through changesets.
