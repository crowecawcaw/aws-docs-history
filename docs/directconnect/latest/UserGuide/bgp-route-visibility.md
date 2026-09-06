

# BGP route visibility
<a name="bgp-route-visibility"></a>

With Direct Connect, you can view the BGP routes on your virtual interfaces (VIFs). You can see which routes AWS accepted from your router. You can also see which routes AWS is sending to your router. Each route shows its AS path and community values.

View routes in the Direct Connect console, or use the `ListVirtualInterfaceRoutes` API action. For more information about the API, see [ListVirtualInterfaceRoutes](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ListVirtualInterfaceRoutes.html) in the *Direct Connect API Reference*.

## BGP route visibility concepts
<a name="bgp-route-visibility-concepts"></a>

Accepted routes and advertised routes  
Each route has a direction:  
+ *Accepted routes* – Routes that AWS received from your router. AWS keeps these routes after it applies inbound routing policy.
+ *Advertised routes* – Routes that AWS sends to your router over the VIF.

Route age  
Each route includes the time that AWS received or advertised it on the virtual interface. The console shows this as the route age. In the API and AWS CLI response, the value is an epoch-seconds timestamp; to find the route age, subtract this value from the current time.

Communities  
Routes show their BGP community values in `ASN:value` format. AWS shows only the supported Direct Connect communities and hides all other (internal) community values. The supported communities are:  
+ *Scope communities* (advertised to your router): `7224:9100`, `7224:9200`, and `7224:9300`.
+ *Region and continent communities* (accepted from your router): `7224:8100` and `7224:8200`.
+ *Local preference communities* (accepted from your router): `7224:7100`, `7224:7200`, and `7224:7300`.
The communities that appear depend on the VIF type and route direction. For more information about these communities and how AWS uses them, see [Routing policies and BGP communities](routing-and-bgp.md).

## View BGP routes
<a name="bgp-route-visibility-console"></a>

The Direct Connect console shows BGP route data on the virtual interface detail page. Choose the **Accepted routes** or **Advertised routes** tab to see routes.

Each route tab shows a table with the following columns:
+ Prefix/Network
+ Address family
+ AS path
+ Communities
+ Route age

You can filter routes by prefix, AS path, community, or address family.

------
#### [ Console ]

**To view BGP routes for a virtual interface**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Select the virtual interface.

1. Choose the **Accepted routes** or **Advertised routes** tab to view the corresponding routes.

------
#### [ Command line ]

Use the [list-virtual-interface-routes](https://docs.aws.amazon.com/cli/latest/reference/directconnect/list-virtual-interface-routes.html) command. Use the `routeDirection` filter to return accepted or advertised routes. The following example returns the routes that AWS accepted from your router on the specified virtual interface.

```
aws directconnect list-virtual-interface-routes \
    --virtual-interface-id {{dxvif-abc12345}} \
    --filters '{"routeDirection": "accepted"}'
```

You can also filter the results by address family (`addressFamily`), prefix (`cidrs`), AS path (`asPath`), or community (`communities`).

------