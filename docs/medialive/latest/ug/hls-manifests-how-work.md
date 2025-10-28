# How manifests work

The following sections describe how MediaLive handles manifest paths.

## How manifest paths work by default

The manifests that MediaLive creates include information about the paths to other files,
specifically:

- The content inside the main manifest includes a path to each child manifest.

By default, the syntax of this path is the following:

```
baseFilename nameModifier extension
```

For example:

```
curling-high.m3u8
```

The path is relative to the location of the main manifest.

- The content inside each child manifest includes a path to its media files.

By default, the syntax of this path is the following:

```
baseFilename nameModifier optionalSegmentModifier counter extension
```

For example:

```
curling-high-000001.ts
```

The path is relative to the location of the child manifest.

## How custom paths work

If the default paths inside the manifests are not suitable for the way that the downstream
system handles the three sets of files, you can complete the _base
URL_ fields:

- Complete the **Base URL manifest** fields so that MediaLive constructs
  custom paths to the child manifests.
- Complete the **Base URL content** fields so that MediaLive constructs custom
  paths to the media files.

When you customize the paths, the syntax changes.

- When you complete the **Base URL manifest** fields, the syntax for the
  child manifest path (inside the main manifest) is the following:

```
baseURLManifest baseFilename nameModifier extension
```

For example:

```
http://viewing/sports/curling-high.m3u8
```

- When you complete the **Base URL content** fields, the syntax for the
  media file paths (inside the child manifests) is the following:

```
baseURLContent baseFilename nameModifier optionalSegmentModifier counter
        extension
```

For example:

```
http://viewing/media/sports/curling-high-000001.ts
```

## How MediaLive constructs these paths

The custom paths to the child manifests are constructed as follows:

- You complete the **Base URL manifest** fields, or the **Base URL
  content** fields, or both.

For example:

```
http://198.51.100/sports/viewing/
```

Note the slash at the end of the value.

- MediaLive prepends that value to the [default
  path](#hls-default-manifest-paths "#hls-default-manifest-paths"). For example:

```
http://198.51.100/sports/viewing/curling-high.m3u8
```
