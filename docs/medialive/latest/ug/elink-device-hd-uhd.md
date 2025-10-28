# HD and UHD Link devices

There are two versions of the Link device. Each device can handle different usages,
ingest different resolutions, and stream different formats.

| Device                            | Usage                        | Resolutions that the device is ingesting          | Resolutions and codecs that the device produces |
| --------------------------------- | ---------------------------- | ------------------------------------------------- | ----------------------------------------------- |
| AWS Elemental Link HD (Link HD)   | Connect to a MediaLive input | HD or lower                                       | The same resolution as the ingest, in HEVC      |
| AWS Elemental Link UHD (Link UHD) | Connect to a MediaLive input | UHD or lower                                      | The same resolution as the ingest, in HEVC      |
| Connect to a MediaConnect flow    | UHD or lower                 | The same resolution as the ingest, in AVC or HEVC |
