# Huge pages

for RDS for PostgreSQL

_Huge pages_ are a memory management feature that
reduces overhead when a DB instance is working with large contiguous chunks of
memory, such as that used by shared buffers. This PostgreSQL feature is supported by
all currently available RDS for PostgreSQL versions. You allocate huge pages for your
application by using calls to `mmap` or `SYSV` shared memory.
RDS for PostgreSQL supports both 4-KB and 2-MB page sizes.

You can turn huge pages on or off by changing the value of the
`huge_pages` parameter. The feature is turned on by default for all
the DB instance classes other than micro, small, and medium DB instance
classes.

RDS for PostgreSQL uses huge pages based on the available shared memory. If the DB
instance can't use huge pages due to shared memory constraints, Amazon RDS prevents
the DB instance from starting. In this case, Amazon RDS sets the status of the DB
instance to an incompatible parameters state. If this occurs, you can set the
`huge_pages` parameter to `off` to allow Amazon RDS to start
the DB instance.

The `shared_buffers` parameter is key to setting the shared memory pool
that is required for using huge pages. The default value for the
`shared_buffers` parameter uses a database parameters macro. This
macro sets a percentage of the total 8 KB pages available for the DB instance's
memory. When you use huge pages, those pages are located with the huge pages. Amazon RDS
puts a DB instance into an incompatible parameters state if the shared memory
parameters are set to require more than 90 percent of the DB instance memory.

To learn more about PostgreSQL memory management, see [Resource Consumption](https://www.postgresql.org/docs/current/static/runtime-config-resource.html "https://www.postgresql.org/docs/current/static/runtime-config-resource.html") in the PostgreSQL documentation.
