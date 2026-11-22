

# Route a request through a private service behind a VPC origin with a network call in a CloudFront Functions viewer request event

The following code example shows how to ask a private routing service behind a CloudFront VPC origin with cf.fetch which backend a tenant belongs to, and rewrite the URI.

------
#### [ JavaScript ]

**JavaScript runtime 2.0 for CloudFront Functions**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [CloudFront Functions examples](https://github.com/aws-samples/amazon-cloudfront-functions/tree/main/network-call-vpc-private-routing) repository. 

```javascript
import cf from 'cloudfront';

// Viewer request function.
// Asks a private routing service, an internal Application Load Balancer reached through a
// CloudFront VPC origin, which backend a tenant belongs to, then rewrites the URI.
//   1. KVS kill switch: routing-kill-switch = off forwards unchanged, with no call.
//   2. One network call: GET /route?tenant=<tenant> on the VPC origin.
//   3. Rewrite the URI to /<backend><uri> and set x-backend.
// Any failure forwards unchanged, with x-routing-error (fail open).

// The origin id (the origin's Name in the console) of the VPC origin on this distribution.
const ROUTER_ORIGIN_ID = 'private-router';
const ROUTE_PATH = '/route?tenant=';
const KILL_SWITCH_KEY = 'routing-kill-switch';
const BACKENDS = ['blue', 'green'];
const DEFAULT_TENANT = 'guest';
const TENANT_HEADER = 'x-tenant';
const BACKEND_HEADER = 'x-backend';
const KVS_ERROR_HEADER = 'x-routing-kvs-error';
const ERROR_HEADER = 'x-routing-error';

function describeError(error) {
    return error.name + ': ' + error.message;
}

// Never trust routing headers coming from the viewer. x-tenant is read before this, as input.
function stripRoutingHeaders(headers) {
    delete headers[BACKEND_HEADER];
    delete headers[KVS_ERROR_HEADER];
    delete headers[ERROR_HEADER];
}

// The tenant names a route, not an identity: an x-tenant header, else "guest".
function readTenant(headers) {
    const fromHeader = headers[TENANT_HEADER];
    if (fromHeader && fromHeader.value) {
        return fromHeader.value;
    }
    return DEFAULT_TENANT;
}

// Read before the call, never in parallel: once the call has started, the switch cannot stop it.
// A missing key means routing is on. Any other KVS error also leaves routing on, and is reported.
async function routingSwitchedOff(headers) {
    try {
        const killSwitch = await cf.kvs().get(KILL_SWITCH_KEY);
        return killSwitch === 'off';
    } catch (error) {
        if (error.message.indexOf('KeyNotFound') === -1) {
            headers[KVS_ERROR_HEADER] = { value: describeError(error) };
        }
        return false;
    }
}

// The one network call. Resolves to one of BACKENDS, or throws.
async function lookupBackend(tenant) {
    const routeResponse = await cf.fetch(ROUTE_PATH + encodeURIComponent(tenant), {
        originId: ROUTER_ORIGIN_ID,
        includeBody: true, // default false; the backend is in the body
    });
    if (!routeResponse.ok) {
        throw new Error('route service returned ' + routeResponse.status);
    }
    const text = await routeResponse.text(); // assign first: no await inside call arguments
    const route = JSON.parse(text);
    if (BACKENDS.indexOf(route.backend) === -1) {
        throw new Error('unknown backend ' + route.backend);
    }
    return route.backend;
}

async function handler(event) {
    const request = event.request;
    const headers = request.headers;
    const tenant = readTenant(headers);
    stripRoutingHeaders(headers);
    headers[TENANT_HEADER] = { value: tenant };

    const switchedOff = await routingSwitchedOff(headers);
    if (switchedOff) {
        headers[BACKEND_HEADER] = { value: 'off' };
        return request;
    }

    try {
        const backend = await lookupBackend(tenant);
        request.uri = '/' + backend + request.uri;
        headers[BACKEND_HEADER] = { value: backend };
    } catch (error) {
        // Fail open: TypeError, TimeoutError, InternalError, or a bad answer.
        headers[ERROR_HEADER] = { value: describeError(error) };
    }
    return request;
}
```

------

For a complete list of AWS SDK developer guides and code examples, see [Using CloudFront with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.