# Troubleshoot CDN manifest 404 errors for

MediaTailor

AWS Elemental MediaTailor content delivery network (CDN) manifest 404 errors are a common integration
issue that prevents playback from starting. This section provides step-by-step
troubleshooting for manifest delivery failures.

Multivariant playlist, media playlist, or MPD requests return 404
errors

**Quick fix (try first):**

1. Verify the MediaTailor configuration name in your URL matches exactly
   (case-sensitive)
2. Test the manifest URL directly against MediaTailor without CDN:
   `curl -v
"https://your-emt-endpoint.mediatailor.region.amazonaws.com/v1/master/hls/config-name/master.m3u8"`
3. If direct test works, check CDN routing rules for manifest
   requests

**If quick fix doesn't work:**

**Symptoms:** Players fail to start playback,
manifest requests return HTTP 404 errors in CDN logs.

**Example error messages:**

- Browser console: `"Failed to load resource: the server
responded with a status of 404 (Not Found)"`
- Player error: `"MANIFEST_LOAD_ERROR"` or
  `"NETWORK_ERROR"`
- CDN logs: `GET /v1/master/hls/example-config/master.m3u8
404`

**Resolution:**

Verify that your CDN routing rules are correctly configured to forward
multivariant playlist, media playlist, and MPD requests to MediaTailor.

Check that the MediaTailor configuration exists and is correctly set up.

Ensure your CDN behavior patterns match the expected manifest request
paths (for example, `*.m3u8`, `*.mpd`).
