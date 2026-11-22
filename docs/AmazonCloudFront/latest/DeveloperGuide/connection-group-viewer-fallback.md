

# Serve viewers that don't send SNI with a viewer fallback

Some HTTPS clients, such as older libraries, embedded devices, and some proxies, don't send Server Name Indication (SNI) in the TLS handshake. Without SNI, CloudFront can't tell which certificate to present, so it rejects these handshakes.

With a viewer fallback, you choose a multi-tenant distribution whose certificate CloudFront uses for viewers that connect to your connection group's Anycast static IP addresses without SNI. You set the viewer fallback on the connection group.

**Topics**
+ [How viewer fallback works](#connection-group-viewer-fallback-how-it-works)
+ [Viewer fallback requirements and restrictions](#connection-group-viewer-fallback-requirements)
+ [Set a viewer fallback](#connection-group-viewer-fallback-set-up)

## How viewer fallback works
<a name="connection-group-viewer-fallback-how-it-works"></a>

When a viewer connects to one of the connection group's Anycast static IP addresses and doesn't send SNI, CloudFront completes the TLS handshake with the certificate and TLS settings of the viewer fallback multi-tenant distribution. CloudFront then routes each request on the connection by its `Host` header, as usual.

The viewer fallback multi-tenant distribution only supplies TLS settings for the handshake. CloudFront doesn't route requests to it, and it doesn't need to serve any domain on the Anycast static IP list. Viewers that send SNI aren't affected by the viewer fallback.

When the certificate on the viewer fallback multi-tenant distribution changes or renews, viewers without SNI get the new certificate. You don't need to update the connection group.

**Example – API clients that don't send SNI**  
A connection group that uses an Anycast static IP list contains distribution tenants for an API at `api.example.com` and for the sign-in domains of several customers. Some of the API's clients don't send SNI. The multi-tenant distribution `E2EXAMPLE33333` has a certificate for `*.example.com`, so you set it as the connection group's viewer fallback.  
The following table shows how CloudFront handles requests on the connection group's Anycast static IP addresses.  


| SNI | `Host` | Result | 
| --- | --- | --- | 
| login.customer.com | login.customer.com | The customer's distribution tenant serves the request. The viewer fallback doesn't apply. | 
| None | api.example.com | CloudFront completes the handshake with the \*.example.com certificate from E2EXAMPLE33333. The API distribution tenant serves the request. | 
| None | login.customer.com | CloudFront completes the handshake with the \*.example.com certificate from E2EXAMPLE33333, which doesn't cover login.customer.com. A viewer that validates the certificate ends the connection. | 

## Viewer fallback requirements and restrictions
<a name="connection-group-viewer-fallback-requirements"></a>

To set a viewer fallback, the following must be true:
+ The connection group uses an Anycast static IP list, and no other connection group uses that list.
+ The viewer fallback is a multi-tenant distribution in the same AWS account as the connection group. You can't use a standard distribution.
+ The multi-tenant distribution is enabled and has a custom TLS certificate, not the default `*.cloudfront.net` certificate.

When a connection group has a viewer fallback, the following restrictions apply:
+ You can't change the connection group's Anycast static IP list or IPv6 setting, unless you remove the viewer fallback in the same update.
+ You can't change the Anycast static IP list itself, such as its IP address type. To change the list, first remove the viewer fallback from the connection group.
+ Removing the viewer fallback doesn't unblock these changes if a distribution tenant in the connection group also serves a domain with `anycast-ip-list-only`. Remove those domains too. For more information, see [Address-based selection requirements and restrictions](address-based-selection.md#address-based-selection-requirements).
+ You can't associate the Anycast static IP list with another connection group.
+ You can't disable or delete the viewer fallback multi-tenant distribution, or replace its custom certificate with the default `*.cloudfront.net` certificate.

## Set a viewer fallback
<a name="connection-group-viewer-fallback-set-up"></a>

You can set a viewer fallback when you create a connection group with the **create-connection-group** command, or on an existing connection group with the **update-connection-group** command. The following example sets a viewer fallback on an existing connection group.

**To set a viewer fallback**

1. Get the connection group's current ETag. Replace the connection group ID with your own.

   ```bash
   aws cloudfront get-connection-group \
       --identifier {{cg_EXAMPLE33333}}
   ```

1. Update the connection group. Replace the connection group ID, the ETag, and the multi-tenant distribution ID with your own.

   ```bash
   aws cloudfront update-connection-group \
       --id {{cg_EXAMPLE33333}} \
       --if-match {{E1ABCDEXAMPLE}} \
       --viewer-fallback DistributionId={{E2EXAMPLE33333}}
   ```

   The response shows the viewer fallback. The connection group's `Status` is `InProgress` until CloudFront deploys the change, which can take a few minutes.

   ```json
   {
       "ETag": "E2QWRUHEXAMPLE",
       "ConnectionGroup": {
           "Id": "cg_EXAMPLE33333",
           "Name": "example-group",
           "Arn": "arn:aws:cloudfront::123456789012:connection-group/cg_EXAMPLE33333",
           "RoutingEndpoint": "d111111abcdef8.cloudfront.net",
           "AnycastIpListId": "aip_EXAMPLE11111",
           "ViewerFallback": {
               "DistributionId": "E2EXAMPLE33333"
           },
           "Ipv6Enabled": false,
           "Enabled": true,
           "Status": "InProgress",
           "IsDefault": false
       }
   }
   ```

If you omit `--viewer-fallback` when you update the connection group, CloudFront keeps the current viewer fallback. To remove the viewer fallback, specify an empty viewer fallback. Replace the connection group ID and the ETag with your own.

```bash
aws cloudfront update-connection-group \
    --id {{cg_EXAMPLE33333}} \
    --if-match {{E2QWRUHEXAMPLE}} \
    --viewer-fallback '{}'
```