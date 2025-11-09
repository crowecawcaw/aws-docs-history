# Reference: Location of fields

Read this section if you know how to handle color space in MediaLive, and you only need a
reminder of where the fields are located in the MediaLive Console.

| Topic                                                                                      | Location on the Channel page           | Field                                                                                                                    |
| ------------------------------------------------------------------------------------------ | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------ |
| Input handling                                                                             | **Input attachments**                  | **Video Selector**                                                                                                       | **Color space**          |
| **Color space usage**                                                                      |
| Enter the display metadata for an input from a AWS Elemental Link device                   | **Input attachments**                  | **Video Selector**, then **Color space<br>settings**                                                                     | **Max CLL**              |
| **Max Fall**                                                                               |
| Output, configure the video codec                                                          | **Output groups**, then<br>**Outputs** | **Stream settings**, then **Video**                                                                                      | **Codec settings**       |
| **Stream settings**, then<br>**Video**, then **Codec settings**, then<br>**Codec details** | **Profile**                            |
| **Tier**                                                                                   |
| **Level**                                                                                  |
| Output, convert the color space                                                            | **Output groups**, then **Outputs**    | **Stream settings**, then **Video**, then<br>**Color space**                                                             | **Color space settings** |
| Output, include or omit color space metadata                                               | **Output groups**, then **Outputs**    | **Stream settings**, then **Video**, then<br>**Codec settings**, then **Codec details**, then<br>**Additional settings** | **Color metadata**       |
| Output, specify display metadata to include, only if you are<br>converting to HDR10        | **Output groups**, then<br>**Outputs** | **Stream settings**, then<br>**Video**, then **Color space**, then<br>**Color space settings**                           | **Max CLL**              |
| **Max Fall**                                                                               |
| Output, set up enhanced VQ, only if the output codec is<br>H.264                           | **Output groups**, then<br>**Outputs** | **Stream settings**, then<br>**Video**, then **Codec settings**, then<br>**Additional encoding settings**                | **Quality level**        |
| **Filter settings**                                                                        |
