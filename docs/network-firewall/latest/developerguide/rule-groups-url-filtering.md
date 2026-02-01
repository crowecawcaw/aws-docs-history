# URL and Domain Category Filtering in Suricata compatible AWS Network Firewall rule groups

URL and Domain Category filtering enables you to filter network traffic based on predefined content categories. You can use this feature with **Suricata compatible rule strings** and **standard Network Firewall stateful rule groups**.

Network Firewall provides two filtering keywords:

- `aws_url_category` - Evaluates complete URLs and domains in HTTP/HTTPS traffic
- `aws_domain_category` - Evaluates only domain information from TLS SNI or HTTP host headers
  To use URL and Domain Category filtering, you provide either the `aws_url_category` or `aws_domain_category`
  keyword followed by the category you want to filter for, for example `aws_url_category:Malicious;`
  You can specify multiple categories per rule. For additional examples, see [Stateful rules examples: URL/Domain Category filter](suricata-examples.md#suricata-example-rule-with-url-filter "suricata-examples.md#suricata-example-rule-with-url-filter").

###### How URL and Domain Category filtering works

**aws_url_category keyword**

- Supported protocol in rules: HTTP
- Traffic handling:
  - **For HTTP traffic** - Evaluates complete URLs
  - **For HTTPS traffic** - Requires TLS inspection to evaluate URLs. Without TLS inspection, HTTPS traffic is treated as encrypted TLS traffic and cannot be evaluated

- Performs evaluation in the following order:
  - Complete URL path evaluation (up to 30 recursive path lookups)
  - If no match is found, falls back to domain-level evaluation (up to 10 recursive subdomain lookups)

- Matches against:

      + URI field from HTTP request headers (requires TLS inspection for HTTPS traffic)
      + Host field from HTTP request headers

  **aws_domain_category keyword**

- Supported protocols in rules: TLS, HTTP
- Traffic handling:
  - **For HTTP traffic** - Evaluates domain from Host field
  - **For TLS traffic** - Evaluates domain from SNI field
  - No TLS inspection required

- Performs domain-level evaluation:
  - Evaluates only domain-level information (up to 10 recursive subdomain lookups)

- Matches against:
  - Server Name Indication (SNI) field from TLS handshake
  - Host field from HTTP request headers

###### Supported Categories

```
"Abortion",
"Adult and Mature Content",
"Artificial Intelligence and Machine Learning",
"Arts and Culture",
"Business and Economy",
"Career and Job Search",
"Child Abuse",
"Command and Control",
"Criminal and Illegal Activities",
"Cryptocurrency",
"Dating",
"Education",
"Email",
"Entertainment",
"Family and Parenting",
"Fashion",
"Financial Services",
"Food and Dining",
"For Kids",
"Gambling",
"Government and Legal",
"Hacking",
"Health",
"Hobbies and Interest",
"Home and Garden",
"Lifestyle",
"Malicious",
"Malware",
"Marijuana",
"Military",
"News",
"Online Ads",
"Parked Domains",
"Pets",
"Phishing",
"Private IP Address",
"Proxy Avoidance",
"Real Estate",
"Redirect",
"Religion",
"Search Engines and Portals",
"Science",
"Shopping",
"Social Networking",
"Spam",
"Sports and Recreation",
"Technology and Internet",
"Translation",
"Travel",
"Vehicles",
"Violence and Hate Speech"
```

###### Considerations

- [TLS inspection](tls-inspection-configurations.md "tls-inspection-configurations.md") must be enabled on your firewall to perform URL category filtering on HTTPS traffic
- Without TLS inspection, only domain-level filtering is possible for encrypted traffic
- A single URL may map to multiple categories
- Category database is automatically maintained and updated
- You can specify multiple categories in a single rule
- You cannot combine URL/Domain category filtering keywords (`aws_url_category, aws_domain_category`) with geographic IP filtering (`geoip`) in the same rule. You must create separate rules if you want to filter traffic using both geographic IP filter and URL /Domain Category filter.
- Using URL/Domain category filtering may increase traffic latency due to the additional category lookups performed for each connection matching the rule protocol and IP specifications.
