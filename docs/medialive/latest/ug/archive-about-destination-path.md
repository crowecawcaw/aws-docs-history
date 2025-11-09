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

| Portion of the URL           | Example             | Comment                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| protocol                     | s3ssl://            | The protocol is always<br>`s3ssl://` because<br>the destination for an Archive output is<br>always an S3 bucket.                                                                                                                                                                                                                                |
| bucket portion of the path   | amzn-s3-demo-bucket | With MediaLive, the Amazon S3 bucket name must not use dot<br>notation. For example,<br>`mycompany-videos` is acceptable<br>but `mycompany.videos` isn't.                                                                                                                                                                                       |
| folders portion of the path  | channel59/delivery/ | The folders can be present or not,<br>and can be as long as you want.The<br>folders must always end with a<br>slash.                                                                                                                                                                                                                            |
| baseFilename                 | curling             | Don't terminate the file name with a<br>slash.                                                                                                                                                                                                                                                                                                  |
| nameModifier                 | -20171012T033162    | The modifier is optional for an<br>Archive output.                                                                                                                                                                                                                                                                                              |
| delimiter before the counter | .                   | MediaLive automatically inserts this<br>delimiter.                                                                                                                                                                                                                                                                                              |
| counter                      | 000000              | MediaLive automatically generates this<br>counter. Initially, this is a six-digit<br>number starting at 000000, and<br>increasing by 1. So 000000, 000001,<br>000002 and so on. After 999999, the next<br>number is 1000000 (seven digits), then<br>1000001, 1000002, and so on. Then from<br>9999999 to 10000000 (eight digits), and<br>so on. |
| dot before the extension     | .                   | MediaLive automatically inserts this<br>dot.                                                                                                                                                                                                                                                                                                    |
| extension                    | m2ts                | Always<br>`m2ts`.                                                                                                                                                                                                                                                                                                                               |
