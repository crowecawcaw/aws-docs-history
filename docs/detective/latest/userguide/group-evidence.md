# Informational findings in finding groups

Amazon Detective identifies additional information related to a finding group based on data
in your behavior graph collected within the last 45 days. Detective presents this
information as a finding with the **Informational** severity. Evidence
provides supporting information that highlights an unusual activity or unknown behavior
that is potentially suspicious when viewed within a finding group. This might include
newly observed geolocations or API calls observed within the scope time of a finding.
Evidence findings are only viewable in Detective and are not sent to AWS Security Hub CSPM.

Detective determines the location of requests using MaxMind GeoIP databases.
MaxMind reports very high accuracy of their data at the country level,
although accuracy varies according to factors such as country and type of
IP. For more information about MaxMind, see [MaxMind IP Geolocation](https://support.maxmind.com/hc/en-us/sections/4407519834267-IP-Geolocation "https://support.maxmind.com/hc/en-us/sections/4407519834267-IP-Geolocation"). If you think any of the GeoIP data is incorrect, you can submit a correction request
to Maxmind at [MaxMind Correct GeoIP2 Data](https://support.maxmind.com/hc/en-us/articles/4408252036123-GeoIP-Correction "https://support.maxmind.com/hc/en-us/articles/4408252036123-GeoIP-Correction").

You can observe evidence for different principal types (such as IAM user or IAM
role). For some evidence types, you can observe evidence for **all
accounts**. This means evidences affect your entire behavior graph. If an
evidence finding is observed for all accounts, you will also see at least one additional
informational evidence finding of the same type for an individual IAM role. For
example, if you see a **New geolocation observed for all accounts**
finding, you will see another for **New geolocation observed for a
principal**.

###### **Types of evidence in finding groups**

- New geolocation observed
- New Autonomous System Organization (ASO) observed
- New user agent observed
- New API call issued
- New geolocation observed for all accounts
- New IAM principal observed for all accounts
