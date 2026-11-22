

# Geographic IP filtering

Firewall rules support the Suricata compatible `geoip` keyword to match traffic by the country associated with its source or destination IP address, the same way that Classic Network Firewall stateful rules do. For the Classic version of this feature, see [Geographic IP filtering in Suricata compatible AWS Network Firewall rule groups](rule-groups-geo-ip-filtering.md).

You filter on source or destination IP addresses by specifying `src` or `dst`, or on both together by specifying `both` or `any`. You provide the `geoip` keyword, the filter type, and the alpha-2 country codes for the countries to filter for, for example `geoip:dst,DE;`.

The following firewall rule accepts the flow only when the destination IP address is in Germany (`DE`). Because the `geoip` keyword matches at a packet hook, the rule uses the `tcp:all` hook and doesn't require separate TCP carrier rules. With a drop firewall default action, traffic to any other country falls through to the default action and is dropped.

```
accept:flow tcp:all any any -> any any (msg:"Allow traffic to DE"; geoip:dst,DE; sid:1;)
```

Network Firewall saves Geographic IP filter rules only if they have valid alpha-2 country codes from the International Organization for Standardization (ISO) 3166 standard. Because IP-to-country associations can change over time, if you use Geographic IP rules to allow traffic to specific countries, set the policy's firewall default action to a drop action, so that an IP address that's reassigned to a different country no longer matches your allow rule. For the country-code details and best practices, see [Geographic IP filtering in Suricata compatible AWS Network Firewall rule groups](rule-groups-geo-ip-filtering.md).

Geographic IP filter rules count toward the maximum number of firewall rules per Next Generation policy. For that quota, see [AWS Network Firewall quotas](quotas.md).