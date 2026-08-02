# Considerations when working with public hosted zones

Note the following considerations when working with public hosted zones:

**NS and SOA records**
When you create a hosted zone, Amazon Route 53 creates a name server (NS) record and a
start of authority (SOA) record for the zone. The NS record lists the four name servers that you give to your
registrar or your DNS service so that DNS queries reach Route 53 name servers. For more information about
NS and SOA records, see [NS and SOA records that Amazon Route 53 creates for a public hosted zone](SOA-NSrecords.md "SOA-NSrecords.md").

**Multiple hosted zones that have the same name**
You can create more than one hosted zone with the same name and add different records to each.
Route 53 assigns four name servers to every hosted zone, and the name servers differ for each one. When you
update your registrar's name server records, be careful to use the Route 53 name servers for the correct hosted zone—the
one that has the records you want Route 53 to use when responding to queries for your domain. Route 53
never returns values for records in other hosted zones that have the same name.

**Reusable delegation sets**
By default, Route 53 assigns a unique set of four name servers (called a delegation set) to each hosted zone
that you create. If you want to create many hosted zones, you can create a reusable delegation set with the API.
(Reusable delegation sets aren't available in the Route 53 console.) You can then create hosted zones with the API and assign
the same four name servers to each one.

Reusable delegation sets make it simpler to migrate DNS service to Route 53. You can tell your registrar
to use the same four name servers for all the domains that you want Route 53 to serve. For more information,
see [CreateReusableDelegationSet](../APIReference/API_CreateReusableDelegationSet.md "../APIReference/API_CreateReusableDelegationSet.md") in the
_Amazon Route 53 API Reference_.
