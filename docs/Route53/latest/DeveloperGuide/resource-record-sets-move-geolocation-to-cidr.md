# Moving geolocation routing to IP-based routing

If you use geolocation or geoproximity routing and specific clients are consistently
routed to a non-optimal endpoint based on their physical location or network topology,
you can target those clients’ public IP ranges with IP-based routing instead.

###### To move geolocation routing to IP-based routing

1. Identify the geolocation records you want to override. The following example
   shows a geolocation configuration that you want to fine-tune for California
   IP ranges.

Example geolocation configuration| Record set name | Routing policy and origin | IP address of the application endpoint |
| --- | --- | --- |
| example.com | Geolocation-routing (US) | `198.51.100.1` |
| example.com | Geolocation-routing (EU) | `198.51.100.2` | 2. To override IP ranges from California to a new application endpoint,
recreate the geolocation routing records under a new record set name
(for example, `geo.example.com` instead of `example.com`).

Recreated geolocation records| Record set name | Routing policy and origin | IP address of the application endpoint |
| --- | --- | --- |
| geo.example.com | Geolocation-routing (US) | `198.51.100.1` |
| geo.example.com | Geolocation-routing (EU) | `198.51.100.2` | 3. Create IP-based routing records and a default record that points to your
recreated geolocation routing record set.

IP-based routing records| Record set name | Routing policy and origin | IP address of the application endpoint |
| --- | --- | --- |
| example.com | IP-based routing (default) | Alias record to geo.example.com. For example,<br>`198.51.100.1`. |
| example.com | IP-based routing (California IP ranges) | `198.51.100.3` |
