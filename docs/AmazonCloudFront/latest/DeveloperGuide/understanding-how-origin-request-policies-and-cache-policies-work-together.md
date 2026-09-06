

# Understand how origin request policies and cache policies work together
<a name="understanding-how-origin-request-policies-and-cache-policies-work-together"></a>

You can use a CloudFront [origin request policy](controlling-origin-requests.md) to control the requests that CloudFront sends to the origin, which are called *origin requests*. To use an origin request policy, you must attach a [cache policy](controlling-the-cache-key.md) to the same cache behavior. You cannot use an origin request policy in a cache behavior without a cache policy. For more information, see [Control origin requests with a policy](controlling-origin-requests.md).

Origin request policies and cache policies work together to determine the values that CloudFront includes in origin requests. All URL query strings, HTTP headers, and cookies that you specify in the cache key (using a cache policy) are automatically included in origin requests. Any additional query strings, headers, and cookies that you specify in an origin request policy are also included in origin requests (but not in the cache key).

Origin request policies and cache policies have settings that might appear to conflict with each other. For example, one policy might allow certain values while another policy blocks them. The following table explains which values CloudFront includes in origin requests when you use the settings of an origin request policy and a cache policy together. These settings generally apply to all types of values (query strings, headers, and cookies), with the exception that you cannot specify all headers or use a header block list in a cache policy.


<table>
<thead>
  <tr><th></th><th colspan="4"><b>Origin request policy</b></th></tr>
  <tr><th></th><th><b>None</b></th><th><b>All</b></th><th><b>Allow list</b></th><th><b>Block list</b></th></tr>
</thead>
<tbody>
  <tr><td colspan="5"><b>Cache policy</b></td></tr>
  <tr><td><b>None</b></td><td>No values from the viewer request are included in the origin request, except for the defaults that are included in every origin request. For more information, see <a href="controlling-origin-requests.md">Control origin requests with a policy</a>.</td><td>All values from the viewer request are included in the origin request.</td><td>Only the values specified in the origin request policy are included in the origin request.</td><td>All values from the viewer request <i><b>except</b></i> those specified in the origin request policy are included in the origin request.</td></tr>
  <tr><td><b>All</b><br /><b>Note:</b> You cannot specify all headers in a cache policy.</td><td>All query strings and cookies from the viewer request are included in the origin request.</td><td>All values from the viewer request are included in the origin request.</td><td>All query strings and cookies from the viewer request, and any headers specified in the origin request policy, are included in the origin request.</td><td>All query strings and cookies from the viewer request are included in the origin request, even those specified in the origin request policy block list. The cache policy setting overrides the origin request policy block list.</td></tr>
  <tr><td><b>Allow list</b></td><td>Only the specified values from the viewer request are included in the origin request.</td><td>All values from the viewer request are included in the origin request.</td><td>All values specified in the cache policy or the origin request policy are included in the origin request.</td><td>The values specified in the cache policy are included in the origin request, even if those same values are specified in the origin request policy block list. The cache policy allow list overrides the origin request policy block list.</td></tr>
  <tr><td><b>Block list</b><br /><b>Note:</b> You cannot specify headers in a cache policy block list.</td><td>All query strings and cookies from the viewer request <i><b>except</b></i> those specified are included in the origin request.</td><td>All values from the viewer request are included in the origin request.</td><td>The values specified in the origin request policy are included in the origin request, even if those same values are specified in the cache policy block list. The origin request policy allow list overrides the cache policy block list.</td><td>All values from the viewer request <i><b>except</b></i> those specified in the cache policy or the origin request policy are included in the origin request.</td></tr>
</tbody>
</table>
