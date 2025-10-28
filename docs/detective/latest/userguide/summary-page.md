# Using the Detective summary dashboard

Use the Summary dashboard in Amazon Detective to identify entities to investigate the origin of activity
during the previous 24 hours. The Amazon Detective Summary dashboard helps you to identify entities that are
associated with specific types of unusual activity. It is one of several possible starting points
for an investigation.

To display the **Summary** dashboard, in the Detective navigation pane, choose
**Summary**. The **Summary** dashboard is also displayed by default
when you first open the Detective console.

From the **Summary** dashboard, you can identify entities that meet the following
criteria:

- Investigations that show potential security events identified by Detective
- Entities involved in activity that occurred in newly observed geolocations
- Entities that made the largest number of API calls
- EC2 instances that had the largest volume of traffic
- Container clusters that had the largest number of containers
  From each **Summary** dashboard panel, you can pivot to the profile for a
  selected entity.

As you review the **Summary** dashboard, you can adjust the **Scope
time** to view the activity for any 24-hour time frame in the previous 365 days. When
you change the **Start date and time**, the **End date and
time** is automatically updated to 24 hours after your chosen start time.

With Detective, you can access up to a year of historical event data. This data is available through a set of visualizations that show changes in the type and volume of activity over a selected time window. Detective links these changes to GuardDuty findings.

For more information about source data in Detective, see [Source data used in a behavior
graph](detective-source-data-about.md "detective-source-data-about.md").

## Investigations

**Investigations** shows you the potential security events identified by
Detective. On the Investigations panel, you can view Critical investigations and the corresponding
AWS roles and users that were impacted by security events over a set period of time.
Investigations groups together indicators of compromise to help determine if a AWS resource is
involved in unusual activity that could indicate malicious behavior and its impact.

Select **View all investigations** to review findings, triage finding
groups, and resource details to accelerate your security investigation. Investigations are
displayed depending on the selected Scope time. You can adjust the scope time to view
investigations in a 24-hour time frame in the previous 365 days. You can pivot directly to
**Critical investigations** to see a detailed investigation report.

If you identify a AWS role or user that seems to have suspicious activity, you can pivot
directly from the **Investigations** panel to the role or user to continue your
investigation. Pivot to a role or user and click **Run investigation** to
generate an investigations report. Once you run an investigation on a role or user, the role or
user is moved to the **Investigated** tab.

## Newly observed geolocations

**Newly observed geolocations** highlights geographic locations that were
the origin of activity during the previous 24 hours, but that were not seen during the baseline
time period before that.

The panel includes up to 100 geolocations. The locations are marked on the map and listed in
the table below the map.

For each geolocation, the table displays the number of failed and successful API calls made
from that geolocation during the previous 24 hours.

You can expand each geolocation to display the list of users and roles that made API calls
from that geolocation. For each principal, the table lists the type and the associated
AWS account.

If you identify a user or role that seems suspicious, then you can pivot directly from the
panel to the user or role profile to continue your investigation. To pivot to a profile, choose
the user or role identifier.

Detective determines the location of requests using MaxMind GeoIP databases.
MaxMind reports very high accuracy of their data at the country level,
although accuracy varies according to factors such as country and type of
IP. For more information about MaxMind, see [MaxMind IP Geolocation](https://support.maxmind.com/hc/en-us/sections/4407519834267-IP-Geolocation "https://support.maxmind.com/hc/en-us/sections/4407519834267-IP-Geolocation"). If you think any of the GeoIP data is incorrect, you can submit a correction request
to Maxmind at [MaxMind Correct GeoIP2 Data](https://support.maxmind.com/hc/en-us/articles/4408252036123-GeoIP-Correction "https://support.maxmind.com/hc/en-us/articles/4408252036123-GeoIP-Correction").

## Active finding groups in the last 7 days

**Active finding groups in the last 7 days** shows you correlated groupings
of Detective findings, entities, and evidence in your environment that occurred over a set period of
time. These groupings correlate unusual activity that could indicate malicious behavior. The
summary dashboard shows up to five groups sorted by the groups containing the most critical findings
that have been active in the last week.

You can select values in the **Tactic**, **Account**,
**Resource**, and **Findings** content to see more details.

Findings groups are generated on a daily basis. If you identify a finding group of interest,
you can select the title to move to a detailed view of a group profile to continue your
investigation.

## Roles and users with the most API call

volume

**Roles and users with the most API call volume** identifies the users and
roles that have made the largest number of API calls during the previous 24 hours.

The panel can include up to 100 users and roles. For each user or role, you can see the type
(user or role) and the associated account. You can also see the number of API calls issued by
that user or role during the previous 24 hours.

By default, service-linked roles are displayed. Service-linked roles can produce large
volumes of AWS CloudTrail activity, which displaces the principals that you want to investigate
further. You can choose to turn off **Show service-linked roles**, to filter out
service-linked roles from the summary dashboard view.

You can export a comma-separated values (.csv) file that contains the data in this panel.
.

There is also a timeline of the API call volume for the previous 7 days. The timeline can
help you to determine whether the volume of API calls is unusual for that principal.

If you identify a user or role for which the API call volume seems suspicious, then you can
pivot directly from the panel to the user or role profile to continue your investigation. You can
also view the profile of the account associated with the user or role. To view a profile, choose
the user, role, or account identifier.

## EC2 instances with the most traffic volume

**EC2 instances with the most traffic volume** identifies the EC2 instances
that have had the largest total volume of traffic during the previous 24 hours.

The panel can include up to 100 EC2 instances. For each EC2 instance, you can see the
associated account and the number of inbound bytes, outbound bytes, and total bytes from the
previous 24 hours.

You can export a comma-separated values (.csv) file that contains the data in this panel.

You can also see a timeline showing the inbound and outbound traffic over the previous 7
days. The timeline can help determine whether the volume of traffic is unusual for that EC2
instance.

If you identify an EC2 instance that has suspicious traffic volume, then you can go directly
from the panel to the EC2 instance profile to continue your investigation. You can also view the
profile of the account that owns the EC2 instance. To view a profile, choose the EC2 instance or
account identifier.

## Container clusters with the most Kubernetes

pods

**Container clusters with the most Kubernetes pods created** identifies the
clusters that have had the most containers running during the previous 24 hours.

This panel includes up to 100 clusters organized by which clusters had the most findings
associated with them. For each cluster you can see the associated account, the current number of
containers in that cluster, and the number of findings associated with that cluster over the last
24 hours. You can export a comma-separated values (.csv) file that contains the data in this
panel.

If you identify a cluster with recent findings you can pivot directly from the panel to the
cluster profile to continue your investigation. You can also pivot to the profile of the account
that owns the cluster. To pivot to a profile, choose the cluster name or account
identifier.

## Approximate value notification

On **Roles and users with the most API call volume** and **EC2
instances with the most traffic volume**, if a value is followed by an asterisk (\*), it
means that the value is an approximation. The true value is either equal to or greater than the
displayed value.

This occurs because of the method that Detective uses to calculate the volume for each time
interval. On the **Summary** page, the time interval is an hour.

For each hour, Detective calculates the total volume for the 1,000 users, roles, or EC2
instances with the largest volume. It excludes the data for the remaining users, roles, or EC2
instances.

If a resource was sometimes in the top 1,000 and sometimes not, then the calculated volume
for that resource might not include all of the data. The data for the time intervals where it was
not in the top 1,000 is excluded.

Note that this only applies to the **Summary** page. The profile for the
user, role, or EC2 instance provides precise details.
