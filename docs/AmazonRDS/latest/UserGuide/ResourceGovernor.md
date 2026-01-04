# Best practices for configuring resource governor on RDS for SQL Server

To control resource consumption, RDS for SQL Server supports Microsoft SQL Server resource governor.
The following best practices help you avoid common configuration issues and optimize database performance.

1. Resource governor configuration is stored in the `master` database.
   We recommend that you always save a copy of resource governor configuration scripts separately.
2. The classifier function extends login processing time hence it's recommended to avoid complex logic in the classifier.
   An overly complex function can cause login delays or connection timeouts including Amazon RDS automation sessions.
   This can impact the ability of Amazon RDS automation to monitor the instance health. Hence, it's always recommended to
   test the classifier function in a pre-production environment before implementing in production environments.
3. Avoid setting high values (above 70) for `REQUEST_MAX_MEMORY_GRANT_PERCENT` in workload groups,
   as this can prevent the database instance from allocating sufficient memory for other concurrent queries,
   potentially resulting in memory grant timeout errors (Error 8645). Conversely, setting this value too low
   (less than 1) or to 0 might prevent queries that need memory workspace (like those involving sort or hash operations)
   from executing properly in user-defined workload groups.
   RDS enforces these limits by restricting values to between 1 and 70 on default workload groups.
4. For binding tempdb to resource pool, after binding memory optimized tempdb metadata to a pool, the pool
   might reach its maximum setting, and any queries that use `tempdb` might fail with out-of-memory errors.
   Under certain circumstances, the SQL Server could potentially stop if an out-of-memory error occurs.
   To reduce the chance of this happening, set the memory pool's `MAX_MEMORY_PERCENT` to a high value.
