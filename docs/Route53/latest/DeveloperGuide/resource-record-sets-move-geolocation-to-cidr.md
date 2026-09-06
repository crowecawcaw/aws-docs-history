

# Moving geolocation routing to IP-based routing
<a name="resource-record-sets-move-geolocation-to-cidr"></a>

If you use geolocation or geoproximity routing and specific clients are consistently routed to a non-optimal endpoint based on their physical location or network topology, you can target those clients’ public IP ranges with IP-based routing instead.

**To move geolocation routing to IP-based routing**

1. Identify the geolocation records you want to override. The following example shows a geolocation configuration that you want to fine-tune for California IP ranges.  
**Example geolocation configuration**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-move-geolocation-to-cidr.html)

1. To override IP ranges from California to a new application endpoint, recreate the geolocation routing records under a new record set name (for example, `geo.example.com` instead of `example.com`).  
**Recreated geolocation records**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-move-geolocation-to-cidr.html)

1. Create IP-based routing records and a default record that points to your recreated geolocation routing record set.  
**IP-based routing records**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-move-geolocation-to-cidr.html)