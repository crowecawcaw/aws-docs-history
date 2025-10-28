# Data Set Partitioning

Amazon SimpleDB is designed to support highly parallel applications. To improve performance, you can partition
your dataset among multiple domains to parallelize queries and have them operate on smaller individual
datasets. Although you can only execute a single query against a single domain, you can perform aggregation
of the result sets in the application layer. The following is a list of applications that lend themselves to
parallelized queries:

- Natural Partitions—The data set naturally partitions
  along some dimension. For example, a product catalog might be partitioned in the "Book", "CD" and
  "DVD" domains. Although you can store all the product data in a single domain, partitioning can
  improve overall performance.
- High Performance Application—Useful when the application requires higher throughput than a single domain can provide.
- Large Data Set—Useful when timeout limits are reached because of the data size or query complexity.

In cases where data sets do not partition easily (e.g., logs, events, web crawler data), you can use hashing algorithms to create a uniform distribution of items among multiple domains.

For example, you can determine the hash of an item name using a well-behaved hash function, such as MD5 and use the last 2 bits of the resulting hash value to place each item in a specified domain.

- If last two bits equal 00, place item in Domain0
- If last two bits equal 01, place item in Domain1
- If last two bits equal 10, place item in Domain2
- If last two bits equal 11, place item in Domain3

This algorithm provides a distribution of items among domains, uniformity of which
is directly controlled by the hash function. The additional advantage of this scheme is
the ease with which it can be adjusted to partition your data among larger number of domains
by considering more and more bits of the hash value (3 bits will distribute to 8 domains,
4 bits to 16 domains and so on).
