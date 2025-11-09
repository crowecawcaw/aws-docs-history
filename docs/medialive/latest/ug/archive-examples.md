# Examples of

destination fields for an Archive output
group

These examples show how to set up the fields that
relate to file locations. They don't show how to set up
other fields such as fields in the individual
outputs.

## Example

1

You want to create an archive of the streaming
output from TV channel 59. You want to store the
output in the S3 bucket named
`amzn-s3-demo-bucket`, and
you want to break up the stream into 5-minute
chunks.

| Field                                                                       | Value                                                                                                                                                                                                |
| --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Rollover<br>interval\*<br>• field in<br>**Archive settings\*\*<br>section | `300`                                                                                                                                                                                                |
| **URL\*<br>• in<br>**Archive group destination<br>A\*<br>• section          | `s3ssl://amzn-s3-demo-bucket/channel59/delivery/curling`                                                                                                                                             |
| **URL\*<br>• in<br>**Archive group destination<br>B\*<br>• section          | `s3ssl://amzn-s3-demo-bucket/channel59/backup/curling`Using<br>*delivery<br>• and<br>*backup<br>• as folder<br>names is only an example.                                                             |
| **Name<br>modifier\*<br>• in **Archive<br>outputs\*<br>• section            | `-$dt$`For<br>information about identifiers for<br>variable data (such as<br>`$dt$`), see [Identifiers for variable data in MediaLive](variable-data-identifiers.md "variable-data-identifiers.md"). |
| **Extension\*<br>• in<br>**Archive outputs\*\*<br>section                   | Leave blank to use the default<br>(`.m2ts`).                                                                                                                                                         |

Result: the output will be broken into files of 5
minutes (300 seconds) each. Each file will have a
file name of `curling`, the
time that the channel started and a counter (000000,
000001, and so on), and the file name extension. For
example:

- The first file will be
  `curling-20171012T033162-000001.m2ts`.
- The second file will be
  `curling-20171012T033162-000002.m2ts`.

Each file will be stored in both
`s3ssl://amzn-s3-demo-bucket/channel59/delivery` and
`s3ssl://amzn-s3-demo-bucket/channel59/backup`.

A given file is not visible in Amazon S3 while it is
being written. As soon as the rollover happens (or
if the user stops the channel), MediaLive closes the
current file. At that point, the file becomes
visible.

## Example

2

You want to create an archive of highlights from
the curling game that are also being streamed (in a
separate HLS output group). You want to create three
outputs: one that has audio languages for Europe,
one for audio languages for Asia, and one for audio
languages for Africa. You want to store the outputs
in the S3 buckets named
`amzn-s3-demo-bucket1` and
`amzn-s3-demo-bucket2`. You
want to break up the stream into 5 minute chunks.

| Field                                                                       | Value                                                                                                                                                                                                                               |
| --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Rollover<br>interval\*<br>• field in<br>**Archive settings\*\*<br>section | `300`                                                                                                                                                                                                                               |
| **URL\*<br>• in<br>**Archive group destination<br>A\*<br>• section          | `s3ssl://amzn-s3-demo-bucket1/sports-delivery/highlights/curling/10312017`In<br>this example, the<br>`10312017` folder<br>is set to match today's<br>date.                                                                          |
| **URL\*<br>• in<br>**Archive group destination<br>B\*<br>• section          | `s3ssl://amzn-s3-demo-bucket2/sports-delivery/highlights/curling/10312017`In<br>this example, the paths have different<br>bucket names.                                                                                             |
| **Name<br>modifier\*<br>• in **Archive<br>outputs\*<br>• section            | Choose **Add<br>output\*<br>• twice: two more<br>**Output\*<br>• lines are<br>added to this section, for a total of<br>three lines. In each line, enter a<br>modifier:<br>`-audiogroup1`,<br>`-audiogroup2`, and<br>`-audiogroup3`. |
| **Extension\*<br>• in<br>**Archive outputs\*\*<br>section                   | Leave blank to use the default<br>(`.m2ts`).                                                                                                                                                                                        |

Result: three separate categories of files are
created for each output. Each file has a file name
of `10312017`, plus the
modifier, the sequential counter, and the file name
extension. For example:

- `10312017-audiogroup1-000000.m2ts`,
  `10312017-audiogroup2-000000.m2ts`,
  and
  `10312017-audiogroup3-000000.m2ts`.
- `10312017-audiogroup1-000001.m2ts`,
  `10312017-audiogroup2-000001.m2ts`,
  and
  `10312017-audiogroup3-000001.m2ts`.

Each file will be stored in both
`s3ssl://amzn-s3-demo-bucket1/sports-delivery/highlights/curling`
and
`s3ssl://amzn-s3-demo-bucket2/sports-delivery/highlights/curling`.

A given file is not visible in Amazon S3 while it is
being written. As soon as the rollover happens (or
if the user stops the channel), MediaLive closes the
current file. At that point, the file becomes
visible.
