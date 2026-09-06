

# Stream video using CloudFront
<a name="tutorial-stream-video-with-cloudfront"></a>

Media workflows commonly store finished content — video on demand (VOD) files, HTTP Live Streaming (HLS) packages, images, and graphics — on an FSx for ONTAP volume that editors, producers, and automation systems write to using NFS or SMB.

With an Amazon S3 access point attached to the FSx for ONTAP volume, CloudFront can serve content directly from the volume. Editors and production systems publish to the volume over NFS or SMB the way they always have, CloudFront fetches content through the access point, and viewers receive the content from the nearest CloudFront edge location.

In this tutorial, you encode a sample video as an HLS adaptive-bitrate package, upload the output to an access point attached to an FSx for ONTAP volume, configure a CloudFront distribution with origin access control so viewers cannot bypass CloudFront to reach the volume directly, and verify that the stream plays end to end.

**Note**  
This tutorial takes approximately **40 to 60 minutes** to complete. The AWS services used incur charges for the resources you create. If you complete all the steps, including the **Clean up** section promptly, the expected cost is less than **$1** in the US East (N. Virginia) AWS Region. This estimate does not include ongoing charges for the FSx for ONTAP volume itself.

## How the pattern works
<a name="tutorial-cf-how-it-works"></a>

The request flow is:
+ A viewer's player (browser, mobile app, smart TV) requests the HLS master playlist from the CloudFront domain.
+ CloudFront checks its edge cache. On a miss, CloudFront signs a request using Signature Version 4 (SigV4) with its origin access control (OAC) and forwards it to the Amazon S3 endpoint for the access point.
+ The access point authorizes the request against its access policy, which allows the CloudFront service principal scoped to your distribution, and returns the requested object from the FSx for ONTAP volume.
+ CloudFront caches the response at the edge and returns it to the viewer.

HLS packages mix two types of files that benefit from different cache policies:
+ **Playlists** (`.m3u8`) describe which segments make up the stream. Use a short `Cache-Control` TTL so you can publish updated playlists quickly.
+ **Segments** (`.ts`) contain the encoded video and audio. Once written, a segment's contents never change, so use a long, immutable `Cache-Control` TTL.

## Prerequisites
<a name="tutorial-cf-prerequisites"></a>
+ An FSx for ONTAP volume with an Amazon S3 access point attached. The access point must have an **internet** network origin so that CloudFront can reach it. For instructions, see [Creating an access point](fsxn-creating-access-points.md).
+ AWS CLI version 2 installed and configured with credentials that can create CloudFront distributions, origin access controls, and access point policies.
+ [FFmpeg](https://ffmpeg.org/) installed locally, for encoding the sample video to HLS.
+ A source video file. This tutorial uses the [Sintel trailer](https://download.blender.org/durian/trailer/sintel_trailer-1080p.mp4) from the Blender Foundation, a 52-second 1080p clip released under Creative Commons.

## Step 1: Encode the source video as an HLS package
<a name="tutorial-cf-encode"></a>

Use FFmpeg to produce a three-variant HLS package at 360p, 720p, and 1080p with realistic over-the-top (OTT) bitrates. The resulting package includes a master playlist that references per-variant playlists, each of which lists four-second transport stream segments.

1. Download the source video.

   ```
   $ mkdir -p ~/media && cd ~/media
   curl -sSL -o sintel-1080p.mp4 \
       https://download.blender.org/durian/trailer/sintel_trailer-1080p.mp4
   ```

1. Encode the video to HLS with three adaptive-bitrate variants.

   ```
   $ mkdir hls && cd hls
   ffmpeg -i ../sintel-1080p.mp4 \
       -filter_complex "[0:v]split=3[v1][v2][v3]; \
           [v1]scale=w=640:h=360[v1out]; \
           [v2]scale=w=1280:h=720[v2out]; \
           [v3]scale=w=1920:h=1080[v3out]" \
       -map "[v1out]" -c:v:0 libx264 -b:v:0 800k  -maxrate:v:0 856k  -bufsize:v:0 1200k \
       -map "[v2out]" -c:v:1 libx264 -b:v:1 3000k -maxrate:v:1 3200k -bufsize:v:1 4500k \
       -map "[v3out]" -c:v:2 libx264 -b:v:2 5500k -maxrate:v:2 5900k -bufsize:v:2 8250k \
       -preset veryfast -g 48 -keyint_min 48 -sc_threshold 0 \
       -map a:0 -map a:0 -map a:0 -c:a aac -b:a:0 96k -b:a:1 128k -b:a:2 128k \
       -f hls -hls_time 4 -hls_playlist_type vod -hls_flags independent_segments \
       -hls_segment_filename "stream_%v/seg_%03d.ts" \
       -master_pl_name master.m3u8 \
       -var_stream_map "v:0,a:0,name:360p v:1,a:1,name:720p v:2,a:2,name:1080p" \
       "stream_%v/playlist.m3u8"
   ```

   The command produces a directory tree with one master playlist, three variant playlists, and the transport stream segments for each variant.

   ```
   hls/
   ├── master.m3u8
   ├── stream_360p/
   │   ├── playlist.m3u8
   │   ├── seg_000.ts
   │   └── ...
   ├── stream_720p/
   │   ├── playlist.m3u8
   │   ├── seg_000.ts
   │   └── ...
   └── stream_1080p/
       ├── playlist.m3u8
       ├── seg_000.ts
       └── ...
   ```

## Step 2: Upload the HLS package to the access point
<a name="tutorial-cf-upload"></a>

Upload the package twice — once for playlists with a short TTL, and once for segments with a long, immutable TTL. Setting the correct `Content-Type` is important: most players require `application/vnd.apple.mpegurl` for `.m3u8` and `video/mp2t` for `.ts`.

Replace {{access-point-alias}} with your access point alias.

```
$ # Playlists: short TTL, m3u8 content type
aws s3 cp ~/media/hls/ "s3://{{access-point-alias}}/content/sintel/" \
    --recursive --exclude "*" --include "*.m3u8" \
    --content-type "application/vnd.apple.mpegurl" \
    --cache-control "max-age=60"

# Segments: long immutable TTL, ts content type
aws s3 cp ~/media/hls/ "s3://{{access-point-alias}}/content/sintel/" \
    --recursive --exclude "*" --include "*.ts" \
    --content-type "video/mp2t" \
    --cache-control "max-age=31536000,immutable"
```

Verify that both files uploaded with the expected content types and cache headers.

```
$ aws s3api head-object --bucket {{access-point-alias}} \
    --key content/sintel/master.m3u8 \
    --query '{ContentType:ContentType,CacheControl:CacheControl}'
```

## Step 3: Create an origin access control
<a name="tutorial-cf-oac"></a>

An origin access control (OAC) lets CloudFront sign requests to your access point so only CloudFront can fetch objects. Without OAC, viewers could bypass CloudFront by requesting objects directly from the access point endpoint.

```
$ aws cloudfront create-origin-access-control \
    --origin-access-control-config \
    'Name=fsxn-media-oac,SigningProtocol=sigv4,SigningBehavior=always,OriginAccessControlOriginType=s3'
```

Note the `Id` in the response. You use it in the next step.

## Step 4: Create the CloudFront distribution
<a name="tutorial-cf-distribution"></a>

Create a CloudFront distribution with the access point alias as the origin domain. Use the `CachingOptimized` managed cache policy, which honors the `Cache-Control` headers you set in Step 2.

1. Save the following configuration to a file named `dist.json`, replacing the placeholders.

   ```
   {
       "CallerReference": "fsxn-media-1",
       "Comment": "FSx for ONTAP media delivery",
       "Enabled": true,
       "DefaultRootObject": "",
       "Origins": {
           "Quantity": 1,
           "Items": [{
               "Id": "fsxn-ap",
               "DomainName": "{{access-point-alias}}.s3.{{region}}.amazonaws.com",
               "S3OriginConfig": {"OriginAccessIdentity": ""},
               "OriginAccessControlId": "{{oac-id}}",
               "ConnectionAttempts": 3,
               "ConnectionTimeout": 10
           }]
       },
       "DefaultCacheBehavior": {
           "TargetOriginId": "fsxn-ap",
           "ViewerProtocolPolicy": "redirect-to-https",
           "AllowedMethods": {
               "Quantity": 2, "Items": ["GET", "HEAD"],
               "CachedMethods": {"Quantity": 2, "Items": ["GET", "HEAD"]}
           },
           "Compress": true,
           "CachePolicyId": "658327ea-f89d-4fab-a63d-7e88639e58f6"
       },
       "PriceClass": "PriceClass_100",
       "ViewerCertificate": {"CloudFrontDefaultCertificate": true}
   }
   ```
**Note**  
`PriceClass_100` uses CloudFront edge locations only in North America and Europe, which keeps cost lower for this tutorial. For global edge coverage, change the value to `PriceClass_All`. For more information, see [Choosing the price class for a CloudFront distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PriceClass.html).

1. Create the distribution.

   ```
   $ aws cloudfront create-distribution --distribution-config file://dist.json \
       --query 'Distribution.{Id:Id,DomainName:DomainName,ARN:ARN}'
   ```

   Note the distribution ID, ARN, and domain name in the response. The distribution takes approximately five minutes to deploy. You can continue to Step 5 while it deploys.

## Step 5: Attach an access point policy that allows CloudFront
<a name="tutorial-cf-ap-policy"></a>

The access point policy grants the CloudFront service principal permission to read objects, scoped to your specific distribution using the `AWS:SourceArn` condition.

1. Save the following policy to a file named `ap-policy.json`, replacing the placeholders.

   ```
   {
       "Version": "2012-10-17", 		 	 	 
       "Statement": [{
           "Sid": "AllowCloudFrontServicePrincipal",
           "Effect": "Allow",
           "Principal": {"Service": "cloudfront.amazonaws.com"},
           "Action": "s3:GetObject",
           "Resource": "arn:aws:s3:{{region}}:{{account-id}}:accesspoint/{{access-point-name}}/object/*",
           "Condition": {
               "StringEquals": {
                   "AWS:SourceArn": "arn:aws:cloudfront::{{account-id}}:distribution/{{distribution-id}}"
               }
           }
       }]
   }
   ```

1. Attach the policy to the access point.

   ```
   $ aws s3control put-access-point-policy \
       --account-id {{account-id}} \
       --name {{access-point-name}} \
       --policy file://ap-policy.json
   ```

## Step 6: Verify playback
<a name="tutorial-cf-verify"></a>

Wait for the distribution to reach `Deployed` status.

```
$ aws cloudfront get-distribution --id {{distribution-id}} \
    --query 'Distribution.Status'
```

Fetch the master playlist through CloudFront.

```
$ curl -sS "https://{{distribution-domain}}/content/sintel/master.m3u8"
```

The response should list the three variants.

```
#EXTM3U
#EXT-X-VERSION:6
#EXT-X-STREAM-INF:BANDWIDTH=1031744,RESOLUTION=640x360,CODECS="avc1.64001e,mp4a.40.2"
stream_360p/playlist.m3u8

#EXT-X-STREAM-INF:BANDWIDTH=3497301,RESOLUTION=1280x720,CODECS="avc1.64001f,mp4a.40.2"
stream_720p/playlist.m3u8

#EXT-X-STREAM-INF:BANDWIDTH=6311285,RESOLUTION=1920x1080,CODECS="avc1.640028,mp4a.40.2"
stream_1080p/playlist.m3u8
```

Check the response headers for correct content type, cache control, and cache status.

```
$ curl -sSI "https://{{distribution-domain}}/content/sintel/stream_1080p/seg_000.ts"
```

A successful response shows `content-type: video/mp2t`, `cache-control: max-age=31536000,immutable`, and an `x-cache` header indicating whether the response came from the edge or the origin.

Finally, play the stream end to end with FFmpeg to confirm all segments fetch and decode correctly.

```
$ ffprobe -v error \
    -show_entries stream=codec_name,width,height \
    -show_entries format=duration \
    "https://{{distribution-domain}}/content/sintel/master.m3u8"
```

You can also open the master playlist URL in Safari or VLC, or embed it in a web page using a JavaScript player such as [hls.js](https://github.com/video-dev/hls.js).

## Extending the pattern
<a name="tutorial-cf-extending"></a>
+ **Use a custom domain with HTTPS.** Request an ACM certificate for your domain, attach it to the distribution, and add a CNAME record pointing to the CloudFront domain. For instructions, see [Using custom URLs with CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cnames-and-https-procedures.html).
+ **Protect premium content with signed URLs or signed cookies.** For content that requires authorization (subscription services, early-access previews, geo-fenced content), use CloudFront signed URLs or signed cookies. See [Serving private content with signed URLs and signed cookies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-signed-urls.html).
+ **Invalidate the cache when you publish new content.** When you replace a playlist or upload a new HLS package, use `aws cloudfront create-invalidation` to remove the old versions from CloudFront edges. For immutable segments with long TTLs, invalidation is usually unnecessary because segment file names are unique per package.
+ **Enable CORS for browser-based players.** If a browser-based HLS player on a different domain loads your stream, add `Access-Control-Allow-Origin` headers to responses using a CloudFront response headers policy.
+ **Log viewer requests.** Enable CloudFront standard logging or real-time logs to capture viewer requests for analytics, billing, or abuse detection.

## Troubleshooting
<a name="tutorial-cf-troubleshooting"></a>

403 Forbidden from CloudFront  
The access point policy is missing, does not include the CloudFront service principal, or the `AWS:SourceArn` condition references the wrong distribution ARN. Verify the policy with `aws s3control get-access-point-policy` and confirm the distribution ARN matches the one in your `aws cloudfront create-distribution` response.

Player loads the master playlist but fails to play  
Check that segment files have `Content-Type: video/mp2t` and playlists have `Content-Type: application/vnd.apple.mpegurl`. Some players reject segments with generic content types. Re-upload with the correct `--content-type` flag.

New playlists take time to reach viewers  
CloudFront caches playlists for the TTL set by your `Cache-Control` header. If you need a shorter TTL, re-upload the playlist with a smaller `max-age` value, or create an invalidation. Segments do not have this problem because their content does not change.

`x-cache: Miss from cloudfront` on every request  
This is normal the first time a viewer in a region requests a file. CloudFront fetches from the origin on a miss and caches the response for the TTL. Subsequent requests for the same file from that edge location return `Hit from cloudfront`.

Direct access to the access point is denied  
This is expected. The OAC requires SigV4-signed requests from CloudFront, and the access point policy restricts access to the CloudFront service principal. Viewers can only reach the content through the distribution domain.

## Clean up
<a name="tutorial-cf-clean-up"></a>

Disable and delete the distribution, then delete the remaining resources. The distribution must be disabled before it can be deleted, which takes a few minutes.

Disabling requires two values from `get-distribution-config`: the `ETag` for `--if-match`, and the inner `DistributionConfig` object for `--distribution-config` (the full response also contains the ETag, which `update-distribution` does not accept).

```
$ # Capture the current ETag and the DistributionConfig body
GET_ETAG=$(aws cloudfront get-distribution-config --id {{distribution-id}} \
    --query 'ETag' --output text)
aws cloudfront get-distribution-config --id {{distribution-id}} \
    --query 'DistributionConfig' --output json \
    | jq '.Enabled = false' > dist-updated.json

# Disable the distribution. The response returns a new ETag.
UPDATE_ETAG=$(aws cloudfront update-distribution --id {{distribution-id}} \
    --if-match "$GET_ETAG" --distribution-config file://dist-updated.json \
    --query 'ETag' --output text)

# Wait for Status to reach Deployed before deleting.
aws cloudfront get-distribution --id {{distribution-id}} \
    --query 'Distribution.Status'

# Delete the distribution using the ETag from the update call.
aws cloudfront delete-distribution --id {{distribution-id}} \
    --if-match "$UPDATE_ETAG"

# Fetch the OAC ETag, then delete the OAC.
OAC_ETAG=$(aws cloudfront get-origin-access-control --id {{oac-id}} \
    --query 'ETag' --output text)
aws cloudfront delete-origin-access-control --id {{oac-id}} \
    --if-match "$OAC_ETAG"
aws s3control delete-access-point-policy \
    --account-id {{account-id}} --name {{access-point-name}}
aws s3 rm "s3://{{access-point-alias}}/content/sintel/" --recursive
```