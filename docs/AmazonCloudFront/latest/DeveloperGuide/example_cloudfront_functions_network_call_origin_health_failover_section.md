

# Fail over to a secondary origin after a health check network call in a CloudFront Functions viewer request event

The following code example shows how to probe the primary origin with cf.fetch and select a secondary origin when it is unhealthy.

------
#### [ JavaScript ]

**JavaScript runtime 2.0 for CloudFront Functions**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [CloudFront Functions examples](https://github.com/aws-samples/amazon-cloudfront-functions/tree/main/network-call-origin-health-failover) repository. 

```javascript
import cf from 'cloudfront';

// Viewer request function.
// Failover for POST, which origin groups cannot do: they fail over only GET, HEAD and
// OPTIONS, so a POST to a primary that is down simply fails. This function decides before
// the request leaves the edge, with one network call: GET /health on the primary.
// "Slow" means the runtime's fixed 1 s TimeoutError.
//   2xx                                              -> x-route: primary
//   non-2xx, TimeoutError, InternalError, or a
//   TypeError "... could not be completed due to ..."
//   (the edge could not reach the primary)           -> x-route: fallback
//       POST, PUT, PATCH, DELETE -> the secondary origin
//       GET, HEAD                -> the static mirror
//   any other TypeError (the call itself is invalid) -> x-route: primary (fail open)
// GET and HEAD on the primary route also get an origin group (primary, then the mirror
// on 5xx). The probe costs a call per request, so it runs only when the KeyValueStore
// key health-probe is "on".

// Origin ids (the origins' Names in the console), all on this distribution.
const PRIMARY_ORIGIN_ID = 'primary';
const SECONDARY_ORIGIN_ID = 'secondary';
const MIRROR_ORIGIN_ID = 'static-mirror';
const HEALTH_PATH = '/health';
const PROBE_SWITCH_KEY = 'health-probe';
const FAILOVER_STATUS_CODES = [500, 502, 503, 504];
const ROUTE_HEADER = 'x-route';
const ROUTE_ERROR_HEADER = 'x-route-error';
const PROBE_HEADER = 'x-health-probe';
const PROBE_ERROR_HEADER = 'x-health-probe-error';

function describeError(error) {
    return error.name + ': ' + error.message;
}

// The runtime also uses TypeError when the edge could not reach the origin, naming the
// result type: "The request could not be completed due to OriginDnsError".
// That says the primary is down, so it fails over; any other TypeError is a bad call.
function originUnreachable(error) {
    return error.name === 'TypeError' && error.message.indexOf('could not be completed due to') !== -1;
}

// Never trust routing headers coming from the viewer.
function stripRoutingHeaders(headers) {
    delete headers[ROUTE_HEADER];
    delete headers[ROUTE_ERROR_HEADER];
    delete headers[PROBE_HEADER];
    delete headers[PROBE_ERROR_HEADER];
}

// The KVS key health-probe switches the probe on. No KVS, no key, or any other value: off.
async function probeEnabled() {
    try {
        const probeSwitch = await cf.kvs().get(PROBE_SWITCH_KEY);
        return probeSwitch === 'on';
    } catch (error) {
        return false;
    }
}

// The one network call. Resolves to { route, probe }; never throws.
async function probePrimary(headers) {
    try {
        // No body read (includeBody defaults to false): the status is the verdict.
        const healthResponse = await cf.fetch(HEALTH_PATH, { originId: PRIMARY_ORIGIN_ID });
        if (!healthResponse.ok) {
            return { route: 'fallback', probe: 'unhealthy:' + healthResponse.status };
        }
        return { route: 'primary', probe: 'ok' };
    } catch (error) {
        headers[PROBE_ERROR_HEADER] = { value: describeError(error) };
        // A bad call says nothing about the origin: fail open.
        if (error.name === 'TypeError' && !originUnreachable(error)) {
            return { route: 'primary', probe: 'unavailable' };
        }
        return { route: 'fallback', probe: error.name === 'TimeoutError' ? 'unhealthy:timeout' : 'unhealthy:error' };
    }
}

// Fallback: the mirror can serve a GET or HEAD, only the secondary can take a write.
// Primary: a GET or HEAD still fails over to the mirror on 5xx.
function selectOrigins(route, replayable) {
    if (route === 'fallback') {
        cf.selectRequestOriginById(replayable ? MIRROR_ORIGIN_ID : SECONDARY_ORIGIN_ID);
    } else if (replayable) {
        cf.createRequestOriginGroup({
            originIds: [{ originId: PRIMARY_ORIGIN_ID }, { originId: MIRROR_ORIGIN_ID }],
            failoverCriteria: { statusCodes: FAILOVER_STATUS_CODES },
        });
    }
}

async function handler(event) {
    const request = event.request;
    const headers = request.headers;
    stripRoutingHeaders(headers);
    // The static mirror needs a file name.
    if (request.uri.slice(-1) === '/') {
        request.uri += 'index.html';
    }
    const replayable = request.method === 'GET' || request.method === 'HEAD';

    let health = { route: 'primary', probe: 'off' };
    const enabled = await probeEnabled();
    if (enabled) {
        health = await probePrimary(headers);
    }

    try {
        selectOrigins(health.route, replayable);
    } catch (error) {
        // The request still goes to the cache behavior's origin, the primary.
        headers[ROUTE_ERROR_HEADER] = { value: describeError(error) };
    }
    headers[ROUTE_HEADER] = { value: health.route };
    headers[PROBE_HEADER] = { value: health.probe };
    return request;
}

// Viewer response function. No network call.
// CloudFront does not run viewer response functions when the origin answered 400 or
// higher, so this only sees successes and only annotates them:
//   x-served-by: primary    the primary set x-origin: primary
//   x-served-by: secondary  the secondary set x-origin: secondary
//   x-served-by: fallback   no marker: the static mirror answered
//   x-fallback: true        on anything but primary
// It also copies the request function's verdict headers onto the response.
// Compare x-route with x-served-by to tell "the probe decided" from "the origin group failed over".

const ORIGIN_MARKER_HEADER = 'x-origin';
const SERVED_BY_HEADER = 'x-served-by';
const FALLBACK_HEADER = 'x-fallback';
const PRIMARY_MARKER = 'primary';
const SECONDARY_MARKER = 'secondary';
const VERDICT_HEADERS = ['x-route', 'x-health-probe', 'x-health-probe-error', 'x-route-error'];

function servedBy(marker) {
    if (marker === PRIMARY_MARKER) {
        return 'primary';
    }
    if (marker === SECONDARY_MARKER) {
        return 'secondary';
    }
    return 'fallback';
}

function copyVerdictHeaders(requestHeaders, responseHeaders) {
    for (let i = 0; i < VERDICT_HEADERS.length; i++) {
        const header = requestHeaders[VERDICT_HEADERS[i]];
        if (header) {
            responseHeaders[VERDICT_HEADERS[i]] = { value: header.value };
        }
    }
}

function handler(event) {
    const headers = event.response.headers;

    // The marker is internal: read it, then drop it.
    const marker = headers[ORIGIN_MARKER_HEADER] ? headers[ORIGIN_MARKER_HEADER].value : '';
    delete headers[ORIGIN_MARKER_HEADER];
    const origin = servedBy(marker);
    headers[SERVED_BY_HEADER] = { value: origin };
    if (origin !== 'primary') {
        headers[FALLBACK_HEADER] = { value: 'true' };
    }

    copyVerdictHeaders(event.request.headers, headers);
    return event.response;
}
```

------

For a complete list of AWS SDK developer guides and code examples, see [Using CloudFront with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.