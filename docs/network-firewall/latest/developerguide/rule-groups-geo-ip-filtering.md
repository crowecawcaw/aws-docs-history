# Geographic IP filtering in Suricata compatible AWS Network Firewall rule groups

You can use Geographic IP filtering with **Suricata compatible rule strings** and with **standard Network Firewall stateful rule groups**.
This optional filter matches country codes for the IP addresses of network traffic.

Suricata supports filtering for source and destination IPs. You can filter on either of these types by itself, by specifying `dst`
or `src`. You can filter on the two types together with AND or OR logic, by specifying `both` or `any`.
For more information see the Suricata `geoip` keyword documentation at
[IP Keywords: geoip](https://docs.suricata.io/en/suricata-7.0.8/rules/header-keywords.html?highlight=geoip#geoip "https://docs.suricata.io/en/suricata-7.0.8/rules/header-keywords.html?highlight=geoip#geoip").

To use a Geographic IP filter, you provide the `geoip` keyword, the filter type, and the country codes for the countries that
you want to filter for, for example `geoip:dst,CN,US;`. For additional examples, see [Stateful rules examples: Geographic IP filter](suricata-examples.md#suricata-example-rule-with-geo-ip-filter "suricata-examples.md#suricata-example-rule-with-geo-ip-filter").

For more information about adding Geographic IP filtering to your Suricata compatible rule groups via the console, see the [Creating a stateful rule group](rule-group-stateful-creating.md "rule-group-stateful-creating.md") procedure.

###### IPv4 and IPv6 support

The Network Firewall implementation of Suricata `geoip` provides support for IPv6 and IPv4. This is an expansion
of the support provided by Suricata.

###### MaxMind IP geolocation

Suricata determines the location of requests using MaxMind GeoIP databases.
MaxMind reports very high accuracy of their data at the country level, although accuracy varies according to factors such as country and type of IP.

For more information about MaxMind, see [MaxMind IP Geolocation](https://support.maxmind.com/hc/en-us/sections/4407519834267-IP-Geolocation "https://support.maxmind.com/hc/en-us/sections/4407519834267-IP-Geolocation").

If you think any of the geographic IP data is incorrect, you can submit a correction request
to Maxmind at [MaxMind Correct GeoIP Data](https://support.maxmind.com/hc/en-us/articles/4408252036123-GeoIP-Correction "https://support.maxmind.com/hc/en-us/articles/4408252036123-GeoIP-Correction").

###### Country codes

IP geolocation uses the alpha-2 country codes from the International Organization for Standardization (ISO) 3166 standard.

- You can search country codes at the ISO website, at [ISO Online Browsing Platform (OBP)](https://www.iso.org/obp/ui#home "https://www.iso.org/obp/ui#home").
- You can also find them listed on Wikipedia, at [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2 "https://en.wikipedia.org/wiki/ISO_3166-2").
  Network Firewall only allows you to save Geographic IP filter rules that have valid country codes.
