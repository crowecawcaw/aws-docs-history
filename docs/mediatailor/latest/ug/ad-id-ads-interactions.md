# Ad Decision Server (ADS) interactions

MediaTailor uses the creative `id` attribute value from the VAST response as a
value in the ad ID signaling. If the `id` attribute value is empty or not
present in the VAST response, MediaTailor places an empty value in the ad ID signaling.

###### Example VAST response:

The following sample VAST response includes an `id` attribute value for
the inline linear `Creative`. MediaTailor extracts the value from the custom
VAST `Extension` element and places that value in the creative metadata
of the manifest.

```
<?xml version="1.0" encoding="utf-8"?>
<VAST version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <Ad sequence="3">
        <InLine>
            <AdSystem>2.0</AdSystem>
            <AdTitle>AD-caribbean2-15</AdTitle>
            <Impression><![CDATA[https://n8ljfs0xxx.execute-api.us-west-2.amazonaws.com/v1/impression]]></Impression>
            <Creatives>
                <Creative sequence="3" apiFramework="inLine" id="1234">
                    <Linear>
                        <Duration>00:00:15</Duration>
                        <MediaFiles>
                            <MediaFile id="00002" delivery="progressive" type="video/mp4" width="1280" height="720"><![CDATA[https://d3re4i3vgppxxx.cloudfront.net/Media/Bumpers/AD-caribbean2-15-HD.mp4]]></MediaFile>
                        </MediaFiles>
                    </Linear>
                </Creative>
            </Creatives>
          <Extensions>
            <Extension type="creative_signaling"><![CDATA[999999|TVNlDDNpFTchtpRj,E5TfTtcYd5IEzvEt,ChA05OHcvWRGFY6Zp5VSSlxUEJ2B9p8GGhQIDzIQkFeQC-Ho67FR3P9qNa6khSAGKgAyAA]]></Extension>
          </Extensions>
        </InLine>
    </Ad>
</VAST>
```
