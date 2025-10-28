# Best Practice 14.4 – Consider memory

as an alternative to storage

Consider the performance advantages of using memory for supported scenarios in the
database or application layer. SAP HANA uses memory by default, but might benefit from
options to optimize load or offload static data. Relational databases should take
advantage of caching, and application servers should consider if swap is a
requirement.

**Suggestion 14.4.1 – Optimize memory usage for SAP HANA**

Seek to understand the correlation between SAP HANA memory requirements and operating
system memory indicators to help ensure that memory bottlenecks do not impact performance.

- SAP Documentation: [SAP HANA Memory Usage and the Operating System](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/2.0.05/en-US/ca10596b37f04909a96614553cb8ab1d.html#:~:text=Virtual%2C%20Physical%2C%20and%20Resident%20Memory&text=On%20most%20SAP%20HANA%20hosts,operational%20use%20by%20a%20process. "https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/2.0.05/en-US/ca10596b37f04909a96614553cb8ab1d.html#:~:text=Virtual%2C%20Physical%2C%20and%20Resident%20Memory&text=On%20most%20SAP%20HANA%20hosts,operational%20use%20by%20a%20process.")
- SAP Note: [1999997

* FAQ: SAP HANA Memory](https://launchpad.support.sap.com/#/notes/1999997 "https://launchpad.support.sap.com/#/notes/1999997") [Requires SAP Portal Access]
  To improve database startup performance in scenarios that do not involve a host
  restart, consider the use of the SAP HANA Fast Restart option. The SAP HANA Fast Restart
  option dedicates a portion of RAM as a temporary file system (`tempfs`), which is
  treated by the operating system as persistent memory (until operating system restart) and
  allows placement of column store main portion in that `tempfs`, which remains
  there through an index server restart or crash. Thus, no reloading from storage (using I/O)
  is necessary.

- SAP Documentation: [HANA fast restart documentation](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/2.0.05/en-US/ce158d28135147f099b761f8b1ee43fc.html "https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/2.0.05/en-US/ce158d28135147f099b761f8b1ee43fc.html")

**Suggestion 14.4.2 – Use database caching for relational
databases**

For a relational database with high read IOPS requirements, database caching allows
you to significantly increase throughput and lower the data retrieval latency. The cache
acts as an adjacent data access layer to your database, to improve read performance.

The following documentation provides information about caching use-cases, but as most
of this detail is relevant to AWS databases, consult SAP Notes for information specific
to your relational database configuration.

- AWS Documentation: [Caching](https://aws.amazon.com/caching/ "https://aws.amazon.com/caching/")
  (including [database
  caching](https://aws.amazon.com/caching/database-caching/ "https://aws.amazon.com/caching/database-caching/") )

**Suggestion 14.4.3 – Evaluate swap space requirements for SAP
applications**

When physical memory resources are exhausted, SAP uses swap to move inactive pages to
a dedicated disk-based storage area. Although having swap can prevent the application from
crashing due to memory insufficient memory, we recommend applying configuration parameters
and memory sizing so that swap is used infrequently.

If swap usage is expected, evaluate the characteristics of the allocated volume to
avoid further performance issues. Swap can prevent out of memory situations for SAP
applications, when the host runs out of physical memory.

- SAP Note: [153641 -
  Swap space requirement for R/3 64-bit kernel](https://launchpad.support.sap.com/#/notes/153641 "https://launchpad.support.sap.com/#/notes/153641") [Requires SAP Portal Access]
- SAP Note: [2999334

* SWAP Utilization](https://launchpad.support.sap.com/#/notes/2999334 "https://launchpad.support.sap.com/#/notes/2999334") (HANA related) [Requires SAP Portal Access]

- SAP Note: [2488097

* FAQ: Memory usage for the ABAP Server on Windows](https://launchpad.support.sap.com/#/notes/2488097 "https://launchpad.support.sap.com/#/notes/2488097") [Requires SAP Portal
  Access]
