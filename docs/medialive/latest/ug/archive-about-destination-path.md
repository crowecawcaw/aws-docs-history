# Design

the path for the output destination

1. Design the destination path or paths, following this syntax:

`protocol bucket folders baseFilename nameModifier counter
 extension`

For example, for a standard channel:

`s3ssl://amzn-s3-demo-bucket/channel59/delivery/curling-20171012T033162.000000.m2ts`

`s3ssl://amzn-s3-demo-bucket1/channel59/delivery/curling-20171012T033162.000000.m2ts`
If you have two destinations, the destination paths must be different from
each other in some way. At least one of the portions of one path must be
different from the other. It is acceptable for all the portions to be
different.

The following table maps each portion in the example
to the portion in the syntax.

| Portion of the URL           | Example             | Comment                                                                                                                                                                                                                                                                                                                 |
| ---------------------------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| protocol                     | s3ssl://            | The protocol is always `s3ssl://` because the destination for an Archive output is always an S3 bucket.                                                                                                                                                                                                                 |
| bucket portion of the path   | amzn-s3-demo-bucket | With MediaLive, the Amazon S3 bucket name must not use dot notation. For example, `mycompany-videos` is acceptable but `mycompany.videos` isn't.                                                                                                                                                                        |
| folders portion of the path  | channel59/delivery/ | The folders can be present or not, and can be as long as you want.The folders must always end with a slash.                                                                                                                                                                                                             |
| baseFilename                 | curling             | Don't terminate the file name with a slash.                                                                                                                                                                                                                                                                             |
| nameModifier                 | -20171012T033162    | The modifier is optional for an Archive output.                                                                                                                                                                                                                                                                         |
| delimiter before the counter | .                   | MediaLive automatically inserts this delimiter.                                                                                                                                                                                                                                                                         |
| counter                      | 000000              | MediaLive automatically generates this counter. Initially, this is a six-digit number starting at 000000, and increasing by 1. So 000000, 000001, 000002 and so on. After 999999, the next number is 1000000 (seven digits), then 1000001, 1000002, and so on. Then from 9999999 to 10000000 (eight digits), and so on. |
| dot before the extension     | .                   | MediaLive automatically inserts this dot.                                                                                                                                                                                                                                                                               |
| extension                    | m2ts                | Always `m2ts`.                                                                                                                                                                                                                                                                                                          |
