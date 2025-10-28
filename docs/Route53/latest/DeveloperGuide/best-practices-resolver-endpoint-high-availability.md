# High

availability for Resolver endpoints

When you create your Route 53 Resolver inbound endpoints, Route 53 requires that you create at least
two IP addresses that the DNS resolvers on your network will forward queries to. You
should also specify IP addresses in at least two Availability Zones for redundancy.

If you require more than one elastic network interface endpoint to be available at
all times, we recommend that you create at least one more network interface than you
need, to make sure you have additional capacity available for handling possible
traffic surges. The additional network interface also ensures availability during
service operations like maintenance or upgrades.

For more information, see this detailed blog article: [How to achieve DNS high availability with Route 53 Resolver endpoints](https://aws.amazon.com/blogs/networking-and-content-delivery/how-to-achieve-dns-high-availability-with-route-53-resolver-endpoints/ "https://aws.amazon.com/blogs/networking-and-content-delivery/how-to-achieve-dns-high-availability-with-route-53-resolver-endpoints/") and [Values that you specify when you create or edit inbound endpoints](resolver-forwarding-inbound-queries-values.md "resolver-forwarding-inbound-queries-values.md").
