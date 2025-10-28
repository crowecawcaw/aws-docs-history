# Data Set Partitioning

Amazon SimpleDB allows up to 250 domains per subscriber. You can partition your data set among
multiple domains to parallelize queries and operate on smaller data sets. Although
you can only execute a single query against a single domain, you can aggregate
result sets in the application layer.

###### Note

If you require additional domains, go to [https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-simpledb-domains](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-simpledb-domains "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-simpledb-domains").

You might choose to partition data sets across a natural dimension (e.g., product type,
country). For example, you can keep a product catalog in a single domain, but it might be more
efficient to partition it into "Book," "CD," and "DVD" domains. Additionally, you might need
to partition data sets because your data requires higher throughput than a single domain, or
the data set is very large and queries hit the timeout limit.

In some cases, data sets do not naturally present themselves well for partitioning (e.g.,
logs, events, or web-crawler data) and you might use a hashing algorithm to create a uniform
distribution of items among multiple domains. For example, you could partition a data set into
four different domains, determine the hash of items using a hash function such as MD5, and use
the last two digits to place each item in the specified domain:

- Last two bits equal to 00: places item in Domain0
- Last two bits equal to 01: places item in Domain1
- Last two bits equal to 10: places item in Domain2
- Last two bits equal to 11: places item in Domain3
  The additional advantage of this scheme is the ease with which it can be adjusted to
  partition your data across a larger number of domains by considering more and more bits of the
  hash value (3 bits distributes to 8 domains, 4 bits to 16 domains and so on).
