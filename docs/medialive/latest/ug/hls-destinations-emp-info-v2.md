# Collect the information

for MediaPackage v2

For MediaPackage v2, the two URLs for a channel look like these
examples:

`mz82o4-1.ingest.hnycui.mediapackagev2.us-west-2.amazonaws.com/in/v1/live-sports/1/curling/index`

`mz82o4-2.ingest.hnycui.mediapackagev2.us-west-2.amazonaws.com/in/v1/live-sports/2/curling/index`

Where:

| Element                                             | Description                                                                                                        |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `mz82o4-1` and `mz82o4-2`                           | Indicate that the two endpoints are for a redundant channel in MediaPackage. The prefixes are always `-1` and `-2` |
| `mediapackagev2`                                    | Indicates that the input endpoints uses version 2 of the MediaPackage API                                          |
| `live-sports/1/curling` and `live-sports/2/curling` | Folders for the redundant ingests. One folder always includes `/1/`, and the other folder always includes `/2/`    |
| `index`                                             | Always appears at the end of the URL. It is the base filename for all the files for this destination.              |
