

# Geographic IP filtering in Suricata compatible AWS Network Firewall rule groups
<a name="rule-groups-geo-ip-filtering"></a>

You can use Geographic IP filtering with **Suricata compatible rule strings** and with **standard Network Firewall stateful rule groups**. This optional filter matches country codes for the IP addresses of network traffic.

Suricata supports filtering for source and destination IPs. You can filter on either of these types by itself, by specifying `dst` or `src`. You can filter on the two types together with AND or OR logic, by specifying `both` or `any`. For more information see the Suricata `geoip` keyword documentation at [IP Keywords: geoip](https://docs.suricata.io/en/suricata-8.0.3/rules/header-keywords.html?highlight=geoip#geoip).

To use a Geographic IP filter, you provide the `geoip` keyword, the filter type, and the country codes for the countries that you want to filter for, for example `geoip:dst,CN,US;`. For additional examples, see [Stateful rules examples: Geographic IP filter](suricata-examples.md#suricata-example-rule-with-geo-ip-filter). 

For more information about adding Geographic IP filtering to your Suricata compatible rule groups via the console, see the [Creating a stateful rule group](rule-group-stateful-creating.md) procedure. 

**IPv4 and IPv6 support**  
The Network Firewall implementation of Suricata `geoip` provides support for IPv6 and IPv4. This is an expansion of the support provided by Suricata.

**MaxMind IP geolocation**  
Suricata determines the location of requests using MaxMind GeoIP databases. MaxMind reports very high accuracy of their data at the country level, although accuracy varies according to factors such as country and type of IP. For more information about MaxMind, see [MaxMind IP Geolocation](https://support.maxmind.com/hc/en-us/sections/4407519834267-IP-Geolocation). 

If you think any of the geographic IP data is incorrect, you can submit a correction request to Maxmind at [MaxMind Correct GeoIP Data](https://support.maxmind.com/hc/en-us/articles/4408252036123-GeoIP-Correction).

**Country codes**  
IP geolocation uses the alpha-2 country codes from the International Organization for Standardization (ISO) 3166 standard. 
+ You can search country codes at the ISO website, at [ISO Online Browsing Platform (OBP)](https://www.iso.org/obp/ui#home). 
+ You can also find them listed on Wikipedia, at [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2).

Network Firewall only allows you to save Geographic IP filter rules that have valid country codes. 

If you configure Geographic IP rules to allow or pass connections to IP addresses in specific countries, we recommend that you set the Default action on your firewall policy to one of our available Drop actions. Geographic IP country mappings are derived from the MaxMind database, and IP-to-country associations can change between database updates. By configuring a default drop action, you ensure that if an IP address is reassigned to a different country and no longer matches your allow rule or any other rules in your firewall policy, the firewall drops the connection. 

AWS Network Firewall uses the MaxMind GeoIP database to resolve IP addresses to their associated countries. While MaxMind provides industry-standard geolocation data, IP-to-country associations may be inaccurate or change over time due to IP address reassignments, database updates, or other factors. Before you create or troubleshoot Geographic IP rules, verify the country mapping of your target IP addresses by using the [MaxMind IP lookup tool](https://www.maxmind.com/en/geoip-demo). This helps you confirm that the IP addresses you expect to match a given country code are correctly classified in the database and can prevent unexpected rule behavior. However, the lookup tool reflects MaxMind's most current data - AWS Network Firewall's database is updated on a rolling basis, so there may be a brief window where mappings differ. If this is the case, refer to the Workarounds section below for options to override specific IPs. 

If you observe that an IP address is being incorrectly allowed by a Geographic IP rule due to a country mapping change or database inaccuracy, you can create an explicit deny or reject rule in your rule group that targets the specific IP address. You would need to place this rule with a higher priority than the original rule for it to take precedence. Please see [Managing Evaluation order for Suricata compatible rules in AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-rule-evaluation-order.html). 