# Static overlay, creating and modifying a non-running

event

## Overlays at top

level

|                   |                     |                         |                         |
| ----------------- | ------------------- | ----------------------- | ----------------------- | -------------------------------------------------------- | -------------------------------------------------------------------- | ---------------- |
| <image_inserter>  |                     |                         |                         |
|                   | enable_rest         |                         |                         |
|                   | <insertable_image>  |                         |                         |
|                   |                     | duration                |                         |
|                   |                     | fade_in                 |                         |
|                   |                     | fade_out                |                         |
|                   |                     | height                  |                         |
|                   |                     | image_x                 |                         |
|                   |                     | image_y                 |                         |
|                   |                     | layer                   |                         |
|                   |                     | opacity                 |                         |
|                   |                     | start_time              |                         |
|                   |                     | width                   |                         |
|                   |                     | <image_inserter_input>  |                         |
|                   |                     |                         | certificate_file        |
|                   |                     |                         | interface               |
|                   |                     |                         | password                |
|                   |                     |                         | uri                     |
|                   |                     |                         | username                |
|                   |                     | </image_inserter_input> |                         |
|                   | </insertable_image> |                         |                         |
| </image_inserter> |                     |                         |                         | ## Overlays in input section **Data in <input> element** |
|                   |                     |                         |                         |                                                          |
| ---               | ---                 | ---                     | ---                     | ---                                                      |
| <input>           |                     |                         |                         |                                                          |
|                   | <image_inserter>    |                         |                         |                                                          |
|                   |                     | enable_rest             |                         |                                                          |
|                   |                     | <insertable_image>      |                         |                                                          |
|                   |                     |                         | duration                |                                                          |
|                   |                     |                         | fade_in                 |                                                          |
|                   |                     |                         | fade_out                |                                                          |
|                   |                     |                         | height                  |                                                          |
|                   |                     |                         | image_x                 |                                                          |
|                   |                     |                         | image_y                 |                                                          |
|                   |                     |                         | layer                   |                                                          |
|                   |                     |                         | opacity                 |                                                          |
|                   |                     |                         | start_time              |                                                          |
|                   |                     |                         | width                   |                                                          |
|                   |                     |                         | <image_inserter_input>  |                                                          |
|                   |                     |                         |                         | certificate_file                                         |
|                   |                     |                         |                         | interface                                                |
|                   |                     |                         |                         | password                                                 |
|                   |                     |                         |                         | uri                                                      |
|                   |                     |                         |                         | username                                                 |
|                   |                     |                         | </image_inserter_input> |                                                          |
|                   |                     | </insertable_image>     |                         |                                                          | ## Overlays in Ssream assembly section **Data in <stream_assembly>** |
|                   |                     |                         |                         |                                                          |                                                                      |                  |
| ---               | ---                 | ---                     | ---                     | ---                                                      | ---                                                                  | ---              |
| <stream_assembly> |                     |                         |                         |                                                          |                                                                      |                  |
|                   | <video_description> |                         |                         |                                                          |                                                                      |                  |
|                   |                     | <video_preprocessors>   |                         |                                                          |                                                                      |                  |
|                   |                     |                         | <image_inserter>        |                                                          |                                                                      |                  |
|                   |                     |                         |                         | enable_rest                                              |                                                                      |                  |
|                   |                     |                         |                         | <insertable_image>                                       |                                                                      |                  |
|                   |                     |                         |                         |                                                          | duration                                                             |                  |
|                   |                     |                         |                         |                                                          | fade_in                                                              |                  |
|                   |                     |                         |                         |                                                          | fade_out                                                             |                  |
|                   |                     |                         |                         |                                                          | height                                                               |                  |
|                   |                     |                         |                         |                                                          | image_x                                                              |                  |
|                   |                     |                         |                         |                                                          | image_y                                                              |                  |
|                   |                     |                         |                         |                                                          | layer                                                                |                  |
|                   |                     |                         |                         |                                                          | opacity                                                              |                  |
|                   |                     |                         |                         |                                                          | start_time                                                           |                  |
|                   |                     |                         |                         |                                                          | width                                                                |                  |
|                   |                     |                         |                         |                                                          | <image_inserter \_input>                                             |                  |
|                   |                     |                         |                         |                                                          |                                                                      | certificate_file |
|                   |                     |                         |                         |                                                          |                                                                      | interface        |
|                   |                     |                         |                         |                                                          |                                                                      | password         |
|                   |                     |                         |                         |                                                          |                                                                      | uri              |
|                   |                     |                         |                         |                                                          |                                                                      | username         |
|                   |                     |                         |                         |                                                          | </image_inserter \_input>                                            |                  |
|                   |                     |                         |                         | </insertable_image>                                      |                                                                      |                  |
|                   |                     |                         | <image_inserter>        |                                                          |                                                                      |                  |
