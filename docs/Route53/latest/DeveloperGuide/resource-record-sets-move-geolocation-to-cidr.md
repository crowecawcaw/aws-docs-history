

# Moving geolocation routing to IP-based routing
<a name="resource-record-sets-move-geolocation-to-cidr"></a>

If you use geolocation or geoproximity routing and specific clients are consistently routed to a non-optimal endpoint based on their physical location or network topology, you can target those clients’ public IP ranges with IP-based routing instead.

**To move geolocation routing to IP-based routing**

1. Identify the geolocation records you want to override. The following example shows a geolocation configuration that you want to fine-tune for California IP ranges.


**Example geolocation configuration**  

<table>
<thead>
  <tr><th>Record set name</th><th>Routing policy and origin</th><th>IP address of the application endpoint </th></tr>
</thead>
<tbody>
  <tr><td>example.com</td><td>Geolocation-routing (US)</td><td><code>198.51.100.1</code></td></tr>
  <tr><td>example.com</td><td>Geolocation-routing (EU)</td><td><code>198.51.100.2</code></td></tr>
</tbody>
</table>


1. To override IP ranges from California to a new application endpoint, recreate the geolocation routing records under a new record set name (for example, `geo.example.com` instead of `example.com`).


**Recreated geolocation records**  

<table>
<thead>
  <tr><th>Record set name</th><th>Routing policy and origin</th><th>IP address of the application endpoint </th></tr>
</thead>
<tbody>
  <tr><td>geo.example.com</td><td>Geolocation-routing (US)</td><td><code>198.51.100.1</code></td></tr>
  <tr><td>geo.example.com</td><td>Geolocation-routing (EU)</td><td><code>198.51.100.2</code></td></tr>
</tbody>
</table>


1. Create IP-based routing records and a default record that points to your recreated geolocation routing record set.


**IP-based routing records**  

<table>
<thead>
  <tr><th>Record set name</th><th>Routing policy and origin</th><th>IP address of the application endpoint </th></tr>
</thead>
<tbody>
  <tr><td>example.com</td><td>IP-based routing (default)</td><td>Alias record to geo.example.com. For example, <code>198.51.100.1</code>.</td></tr>
  <tr><td>example.com</td><td>IP-based routing (California IP ranges)</td><td><code>198.51.100.3</code></td></tr>
</tbody>
</table>
