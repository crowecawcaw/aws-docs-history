# Time-shifted viewing examples in AWS Elemental MediaPackage

These are MediaPackage time-shifted viewing examples.

**Start parameters use case**
I need content to start playing from where the customer left off.

**Solution**: Include the `start` parameter in
the playback request URL. Program your playback device to record the time that they
customer stopped the stream, then use this timestamp as the value for the
`start` parameter.

###### Example

```
...stream.mpd?`aws.manifestsettings=start:1732285823`
```

**End parameters use case**
I need to define when the live content ends. Content is available for playback after
this point, but live content won't be added.

**Solution**: Ensure the **startover
window** on the endpoint accurately reflects how long you want the live
content to be available for playback (up to 14 days). In playback requests, include the
`end` parameter and use the time that live content ends as the parameter
value.

###### Example

```
...stream.mpd?`aws.manifestsettings=end:1732300175`
```

**Manifest window use case**
I need to serve manifests of varying length from the same manifest URL because my
customers use a variety of devices that have different limitations on manifest window
lengths.

**Solution**: Include the
`manifest_window_seconds` parameter in playback request URLs. Use the
length limitations from each device as the value of for the
`manifest_window_seconds` parameter.

###### Example

```
...stream.mpd?`aws.manifestsettings=manifest_window_seconds:30`
```

```
...stream.mpd?`aws.manifestsettings=manifest_window_seconds:120`
```
