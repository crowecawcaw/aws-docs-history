

# Send fire-and-forget events with a network call from CloudFront Functions

The following code example shows how to send a fire-and-forget event with cf.beacon from viewer request and viewer response events.

------
#### [ JavaScript ]

**JavaScript runtime 2.0 for CloudFront Functions**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [CloudFront Functions examples](https://github.com/aws-samples/amazon-cloudfront-functions/tree/main/network-call-beacon-signal) repository. 

```javascript
import cf from 'cloudfront';
import crypto from 'crypto';

// Viewer request function.
// Fires one small JSON event at an origin of this distribution with cf.beacon
// (fire-and-forget), then forwards the request whatever happened.
//   x-signal: beacon -> handed off; nothing to await, no answer to read
//   x-signal: failed -> cf.beacon threw (x-signal-error)
// cf.beacon counts as the one network call of this invocation.

// The origin id (the origin's Name in the console) of the event collector on this distribution.
const SIGNAL_ORIGIN_ID = 'signal-collector';
const SIGNAL_PATH = '/signal';
const MAX_SIGNAL_ID_LENGTH = 128; // fits an SQS FIFO deduplication id
const MAX_USER_AGENT_LENGTH = 200;
const VIEWER_HASH_LENGTH = 16;
const SIGNAL_ID_HEADER = 'x-signal-id';
const SIGNAL_HEADER = 'x-signal';
const ERROR_HEADER = 'x-signal-error';

// Never send the raw viewer IP: a truncated hash is enough to tell viewers apart.
function hashViewerIp(ip) {
    return crypto.createHash('sha256').update(ip).digest('hex').slice(0, VIEWER_HASH_LENGTH);
}

function requestedSignal(event, signalId) {
    const headers = event.request.headers;
    const userAgent = headers['user-agent'] ? headers['user-agent'].value : '';
    return {
        kind: 'requested',
        uri: signalId,
        ip: hashViewerIp(event.viewer.ip),
        ua: userAgent.slice(0, MAX_USER_AGENT_LENGTH),
        ts: Date.now(),
    };
}

async function handler(event) {
    const request = event.request;

    // Never pass on viewer-supplied copies of the headers this function sets.
    delete request.headers[SIGNAL_ID_HEADER];
    delete request.headers[SIGNAL_HEADER];
    delete request.headers[ERROR_HEADER];

    // The URI is the deduplication id; carried forward so response-function.js can correlate.
    const signalId = request.uri.slice(0, MAX_SIGNAL_ID_LENGTH);
    request.headers[SIGNAL_ID_HEADER] = { value: signalId };

    try {
        cf.beacon(SIGNAL_PATH, {
            originId: SIGNAL_ORIGIN_ID,
            method: 'POST',
            headers: { 'content-type': 'application/json' }, // plain strings, not { value } objects
            body: JSON.stringify(requestedSignal(event, signalId)),
            logDeliveryErrors: true, // a delivery failure after the function returned goes to CloudWatch Logs
        });
        request.headers[SIGNAL_HEADER] = { value: 'beacon' };
    } catch (error) {
        // Only an invalid call throws here (TypeError): a bad option, or a second call in one invocation.
        request.headers[SIGNAL_HEADER] = { value: 'failed' };
        request.headers[ERROR_HEADER] = { value: error.name + ': ' + error.message };
    }
    return request;
}

import cf from 'cloudfront';
import crypto from 'crypto';

// Viewer response function.
// The viewer response event runs on every response, cache hits included, so a network
// call here must be rare by construction: this function fires a "served" event with
// cf.beacon only for a sample of requests, chosen from a hash of the request id.
// Everything else gets x-signal-served: skipped and no call.
// The sample is a hash, not Math.random(): a function cannot make a network call after
// it has generated random values.

// The origin id (the origin's Name in the console) of the event collector on this distribution.
const SIGNAL_ORIGIN_ID = 'signal-collector';
const SIGNAL_PATH = '/signal';
// Share of responses that send a "served" event, in percent.
const SAMPLE_PERCENT = 1;
const MAX_SIGNAL_ID_LENGTH = 128; // fits an SQS FIFO deduplication id
const SIGNAL_ID_HEADER = 'x-signal-id';
const SERVED_HEADER = 'x-signal-served';
const ERROR_HEADER = 'x-signal-served-error';

function headerValue(headers, name) {
    return headers[name] ? headers[name].value : '';
}

// The first 16 bits of SHA-256(request id), as a share of 65536.
function sampled(requestId) {
    if (!requestId) {
        return false;
    }
    const bucket = parseInt(crypto.createHash('sha256').update(requestId).digest('hex').slice(0, 4), 16);
    return bucket < (SAMPLE_PERCENT / 100) * 65536;
}

function servedSignal(request, status) {
    const uri = request.uri.slice(0, MAX_SIGNAL_ID_LENGTH);
    return {
        kind: 'served',
        uri: uri,
        status: status,
        // Correlates with the "requested" event that index.js sent on the way in.
        signalId: headerValue(request.headers, SIGNAL_ID_HEADER) || uri,
        // Its own deduplication id, so it never collapses into the "requested" event.
        dedupId: ('served:' + uri + ':' + status).slice(0, MAX_SIGNAL_ID_LENGTH),
        ts: Date.now(),
    };
}

async function handler(event) {
    const request = event.request;
    const response = event.response;

    if (!sampled(event.context.requestId)) {
        response.headers[SERVED_HEADER] = { value: 'skipped' };
        return response;
    }

    try {
        cf.beacon(SIGNAL_PATH, {
            originId: SIGNAL_ORIGIN_ID,
            method: 'POST',
            headers: { 'content-type': 'application/json' }, // plain strings, not { value } objects
            body: JSON.stringify(servedSignal(request, response.statusCode)),
            logDeliveryErrors: true, // a delivery failure after the function returned goes to CloudWatch Logs
        });
        response.headers[SERVED_HEADER] = { value: 'beacon' };
    } catch (error) {
        response.headers[SERVED_HEADER] = { value: 'failed' };
        response.headers[ERROR_HEADER] = { value: error.name + ': ' + error.message };
    }
    return response;
}
```

------

For a complete list of AWS SDK developer guides and code examples, see [Using CloudFront with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.