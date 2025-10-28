# Manifest caching

MediaTailor periodically and opportunistically caches source playlists to improve channel
assembly performance and reliability. Sometimes, the cached version becomes stale
compared to the origin version at your source location. To force MediaTailor to refresh the
cached version of the source, call [UpdateVodSource](../apireference/API_UpdateVodSource.md "../apireference/API_UpdateVodSource.md"). For example, use this call when the embedded paths change
in your source. Make sure that you always keep an up-to-date version of the source
available on your source location, even if you see few requests from MediaTailor.
