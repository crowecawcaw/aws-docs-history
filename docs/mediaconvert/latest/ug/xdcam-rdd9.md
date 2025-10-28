# XDCAM RDD9 output requirements

MediaConvert supports the following combinations of encoding settings when your
output **MXF profile** is **XDCAM RDD9**.

In this table, read down the rows to find the **Resolution** that you
want. Then read across to find a valid combination of **Bitrate**,
**Frame rate**, **Interlace mode**,
**GOP size**, and **Codec profile**.

| Resolution | Bitrate(s)    | Frame rate(s)      | Interlace mode | GOP size | Codec profile |
| ---------- | ------------- | ------------------ | -------------- | -------- | ------------- | -------------------------------------------------------------------------------------------------------------------- |
| 1280x720   | 25M 35M 50M   | 23.976 50 59.94    | Progressive    | 12       | Main (HD420)  |
| 1280x720   | 50M           | 23.976 25 50 59.94 | Progressive    | 12       | HD422         |
| 1280x720   | 50M           | 29.97              | Progressive    | 15       | HD422         |
| 1440x1080  | 17.5M 25M 35M | 23.976 25          | Progressive    | 12       | Main (HD420)  |
| 1440x1080  | 17.5M 25M 35M | 29.97              | Progressive    | 15       | Main (HD420)  |
| 1440x1080  | 17.5M 25M 35M | 25                 | Interlaced     | 12       | Main (HD420)  |
| 1440x1080  | 17.5M 25M 35M | 29.97              | Interlaced     | 15       | Main (HD420)  |
| 1920x1080  | 50M           | 23.976 25          | Progressive    | 12       | HD422         |
| 1920x1080  | 50M           | 29.97              | Progressive    | 15       | HD422         |
| 1920x1080  | 50M           | 25                 | Interlaced     | 12       | HD422         |
| 1920x1080  | 50M           | 29.97              | Interlaced     | 15       | HD422         | For additional information about MXF RDD9 requirements, see the SMPTE RDD 9:2013 MXF interoperability specification. |
