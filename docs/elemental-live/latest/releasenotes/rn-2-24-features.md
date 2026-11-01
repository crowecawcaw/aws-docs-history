

# New features in version 2.24 and 3.24
<a name="rn-2-24-features"></a>

## New features in Elemental Live and Statmux 2.24
<a name="rn-2-24-features-live"></a>

This release includes the following new features.

### SMPTE 2110 audio inputs (SOCK-38535)
<a name="rn-2-24-features-live-smpte2110-audio"></a>

Elemental Live now supports the ability to ingest audio from more than one audio SDP file. This ability applies to both SMPTE ST 2110-30 (PCM) and SMPTE ST 2110-31 (Dolby Digital Plus).

The following limitations apply:
+ All the tracks in all the SDP files that you set up in the event must have the same audio sampling rates and the same bit depths.
+ The number of audio channels in the SDP file must be an even number.

There are no changes to the API as a result of this enhancement.

### Time zone for Nielsen audio watermarks (SOCK-38516)
<a name="rn-2-24-features-live-nielsen-timezone"></a>

When the Nielsen audio watermarks feature is configured, Elemental Live inserts watermarks that have a time stamp. The time stamp is in a time zone.

Previously, when you configured NAES watermarks, the only time zone that was supported was the "appliance time zone" that you configured when you installed the software or ran the configuration script with the `-t` option.

Now, Elemental Live includes a field to set the time zone for the time stamp.

On the web interface, open the audio output stream, choose **Advanced**, and enable the **Nielsen Watermarking** section. The field is called **Timezone**.

**Note**  
The new field doesn't apply to CBET. That process type has always used UTC, and still uses UTC.

**API change**

In the XML file, the new field is located at:

```
<stream_assembly><audio_description><nielsen_audio_watermarking_settings><timezone>
```

Value: One of these strings: `UTC`, `America/Puerto Rico`, `US/Eastern`, `US/Mountain`, `US/Arizona`, `US/Pacific`, `US/Hawaii`, `US/Samoa`.

Default: `UTC`.

The field applies only when the process type is NAES II \+ VI, or NAES II \+ VI \+ CBET.

**Required action**

After you install Elemental Live version 2.24.1 (or later), you must make a one-time change to events that use the Nielsen audio watermarks feature.

Make sure that you set the time zone in every output. The feature no longer uses the time zone that you configured using the configure or install script.

### Timestamp for RTMP output (SOCK-38443)
<a name="rn-2-24-features-live-rtmp-timestamp"></a>

In the event, an RTMP output now includes a **Timestamp Start Time** field. This field lets you control the handling of the timestamp within the RTMP packets. You can set it so that timestamps are based on 0, where 0 is the event start time. Timestamps reset back to 0 when events are restarted. Or you can set it so that timestamps are based on the Elemental Live system clock. In both cases, the timestamp is absolute, and its format follows the RTMP specification.

**API change**

In the XML file, the new field is located at:

```
<output_group><rtmp_group_settings><output><use_system_clock_start>
```

Value: `zero based`, `use_system_clock_start`.

Default: `zero based`.

### Virtual input switching – maximum inputs (SOCK-38429)
<a name="rn-2-24-features-live-vis-max-inputs"></a>

There is a new configuration parameter for the virtual input switching feature. You can now set the maximum number of virtual inputs allowed on each node. The parameter is on the **Settings** > **Advanced** page of the web interface.

If you increase the maximum, keep in mind that in the events on the node, every virtual input is being continually demuxed, which increases the load on the CPU.

In addition, in Elemental Live nodes running in a Conductor Live cluster, make sure that all the nodes in the same redundancy group have the same value in this field.

## New features in Conductor Live 3.24
<a name="rn-2-24-features-cl3"></a>

This release includes the following new features.

### More information on the Channel Details page (SC-4401, SC-4402, SC-4403)
<a name="rn-2-24-features-cl3-channel-details"></a>

New in version 3.24.3. More information is now included on the **Channel Details** page on the Conductor Live web interface. The page includes information for the following inputs:
+ SMPTE 2022-6 inputs
+ SMPTE 2110 inputs
+ AWS Elemental MediaConnect inputs

### New parameterized field in Conductor Live (SC-4399)
<a name="rn-2-24-features-cl3-esam-zone-param"></a>

The **Zone Identity** field for ESAM configuration (for SCTE 35 handling) can now be configured as a parameter.

### Virtual input switching – maximum inputs (SOCK-38429)
<a name="rn-2-24-features-cl3-vis-max-inputs"></a>

There is a new configuration parameter for the virtual input switching feature. You can now set the maximum number of virtual inputs allowed on each node. The parameter is on the **Settings** > **Advanced** page of the web interface.

If you increase the maximum, keep in mind that in the events on the node, every virtual input is being continually demuxed, which increases the load on the CPU.

In addition, in Elemental Live nodes running in a Conductor Live cluster, make sure that all the nodes in the same redundancy group have the same value in this field.