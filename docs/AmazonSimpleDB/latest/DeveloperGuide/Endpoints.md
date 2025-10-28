# Region Endpoints

To improve latency and to store data in a location that meets your requirements, Amazon SimpleDB enables you to select different region endpoints.

For information about this Amazon SimpleDB regions and endpoints, go to
[Regions and Endpoints](../../../general/latest/gr/rande.md#sdb_region "../../../general/latest/gr/rande.md#sdb_region")
in the Amazon Web Services General Reference.

For example, to create a SimpleDB domain in Europe, you would generate a REST request
similar to the following:

```

https://sdb.eu-west-1.amazonaws.com/?Action=CreateDomain
&DomainName=MyDomain
&<authentication parameters>

```

Each Amazon SimpleDB endpoint is entirely independent. For example, if you have two domains called "MyDomain," one in sdb.amazonaws.com and one in sdb.eu-west-1.amazonaws.com, they are completely independent and do not share any data.
