# Setting up using the REST

API

This topic lists the parameters found on the Elemental Live event or profile and
specifies the location of those parameters in the XML for an event or profile. This
topic does not cover control of SCTE-35 message via the REST API at runtime; that
information is in [SCTE-35 message insertion
into currently running events](scte-35-message-insertion.md "scte-35-message-insertion.md").

| Set the Ad Avail Mode                      | Field      | XML Tag |
| ------------------------------------------ | ---------- | ------- |
| Advanced Avail Controls > Ad Avail Trigger | ad_trigger |

| Manifest Decoration                              | Field                                                      | XML Tag |
| ------------------------------------------------ | ---------------------------------------------------------- | ------- |
| Output Group > Apple HLS > Advanced > Ad Markers | output_group/apple_live_group_settings/ad_markers          |
| Output Group > MS Smooth > Enable Sparse Track   | output_group/ms_smooth_group_settings/enable_sparse_track  |
| Output Group > MS Smooth > Acquisition Point ID  | output_group/ms_smooth_group_settings/acquisition_point_id |
| Output Group > RTMP> Ad Markers                  | output_group/rtmp_group_settings/ad_markers                |

| Ad Avail Blanking and Blackout                                                                                                                   | Field                                                      | XML Tag |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------- | ------- |
| Advanced Avail Controls > Ignore no_regional_blackout_flag                                                                                       | ignore_no_regional_blackout_flag                           |
| Advanced Avail Controls > Ignore web_delivery_allowed_flag                                                                                       | ignore_web_delivery_allowed_flag                           |
| Processors > Global Processors > Ad Avail Blanking > On/Off                                                                                      | avail_blanking/enabled/                                    |
| Processors > Global Processors > Ad Avail Blanking > Browse                                                                                      | avail_blanking/avail_blanking_image/certificate_file       |
| Processors > Global Processors > Ad Avail Blanking > Browse                                                                                      | avail_blanking/avail_blanking_image/interface              |
| Processors > Global Processors > Ad Avail Blanking > Credentials icon ><br>Password                                                              | avail_blanking/avail_blanking_image/password               |
| Processors > Global Processors > Ad Avail Blanking > Browse                                                                                      | avail_blanking/avail_blanking_image/uri                    |
| Processors > Global Processors > Ad Avail Blanking > > Credentials icon ><br>Username                                                            | avail_blanking/avail_blanking_image/username               |
| Processors > Global Processors > Blackout Image Insertion > On/Off                                                                               | blackout_slate/enabled/                                    |
| Processors > Global Processors > Blackout Image Insertion > Enable Network<br>End Blackout > Network ID                                          | blackout_slate/network_id                                  |
| Processors > Global Processors > Blackout Image Insertion > Browse                                                                               | blackout_slate/blackout_slate_image/certificate_file       |
| Processors > Global Processors > Blackout Image Insertion > Browse                                                                               | blackout_slate/blackout_slate_image/interface              |
| Processors > Global Processors > Blackout Image Insertion > Browse                                                                               | blackout_slate/blackout_slate_image/password               |
| Processors > Global Processors > Blackout Image Insertion > Browse                                                                               | blackout_slate/blackout_slate_image/uri                    |
| Processors > Global Processors > Blackout Image Insertion > Browse                                                                               | blackout_slate/blackout_slate_image/username               |
| Processors > Global Processors > Blackout Image Insertion > Enable Network<br>End Blackout > Network End Blackout Image > Browse                 | blackout_slate/network_end_blackout_image/certificate_file |
| Processors > Global Processors > Blackout Image Insertion > Enable Network<br>End Blackout > Network End Blackout Image > Browse                 | blackout_slate/network_end_blackout_image/interface        |
| Processors > Global Processors > Blackout Image Insertion > Enable Network<br>End Blackout > Network End Blackout Image > Credentials > Password | blackout_slate/network_end_blackout_image/password         |
| Processors > Global Processors > Blackout Image Insertion > Enable Network<br>End Blackout > Network End Blackout Image > Browse                 | blackout_slate/network_end_blackout_image/uri              |
| Processors > Global Processors > Blackout Image Insertion > Enable Network<br>End Blackout > Network End Blackout Image > Credentials > Username | blackout_slate/network_end_blackout_image/username         |

| Passthrough or Removal                                                   | Field                                        | XML Tag |
| ------------------------------------------------------------------------ | -------------------------------------------- | ------- |
| Archive Output Group > Output > MPEG-2 TS > PID Control > SCTE-35        | output_group/output/scte35_passthrough       |
| Archive Output Group > Output > MPEG-2 TS > PID Control > SCTE-35<br>PID | output_group/output/m2ts_settings/scte35_pid |
| Apple HLS Output Group > Output > PID Control > SCTE-35                  | output_group/output/scte35_passthrough       |
| Apple HLS Output Group > Output > PID Control > SCTE-35 PID              | output_group/output/m3u8_settings/scte35_pid |
| UDP/TS Output Group > Output > SCTE-35                                   | output_group/output/scte35_passthrough       |
| UDP/TS Output Group > Output > SCTE-35 PID                               | output_group/output/ts_settings/scte35_pid   |

| POIS conditioning                                                                       | Field                                   | XML Tag |
| --------------------------------------------------------------------------------------- | --------------------------------------- | ------- |
| Advanced Avail Controls > Ad Avail Trigger > Acquisition Point<br>Identifier            | esam/acquisition_point_id/              |
| Advanced Avail Controls > Ad Avail Trigger > Asset URI Identifier                       | esam/asset_uri_id/                      |
| Advanced Avail Controls > Ad Avail Trigger > Signal Conditioner<br>Endpoint             | esam/scc_uri/certificate_file           |
| Advanced Avail Controls > Ad Avail Trigger > Signal Conditioner<br>Endpoint             | esam/scc_uri/interface                  |
| Advanced Avail Controls > Ad Avail Trigger > Signal Conditioner<br>Endpoint             | esam/scc_uri/password                   |
| Advanced Avail Controls > Ad Avail Trigger > Signal Conditioner<br>Endpoint             | esam/scc_uri/uri                        |
| Advanced Avail Controls > Ad Avail Trigger > Signal Conditioner<br>Endpoint             | esam/scc_uri/username                   |
| Advanced Avail Controls > Ad Avail Trigger > Alternate Signal Conditioner<br>Endpoint   | esam/alternate_scc_uri/certificate_file |
| Advanced Avail Controls > Ad Avail Trigger > Alternate Signal Conditioner<br>Endpoint   | esam/alternate_scc_uri/interface        |
| Advanced Avail Controls > Ad Avail Trigger > Alternate Signal Conditioner<br>Endpoint   | esam/alternate_scc_uri/password         |
| Advanced Avail Controls > Ad Avail Trigger > Alternate Signal Conditioner<br>Endpoint   | esam/alternate_scc_uri/uri              |
| Advanced Avail Controls > Ad Avail Trigger > Alternate Signal Conditioner<br>Endpoint   | esam/alternate_scc_uri/username         |
| Advanced Avail Controls > Ad Avail Trigger > Manifest Conditioner<br>Endpoint           | esam/mcc_uri/certificate_file           |
| Advanced Avail Controls > Ad Avail Trigger > Manifest Conditioner<br>Endpoint           | esam/mcc_uri/interface                  |
| Advanced Avail Controls > Ad Avail Trigger > Manifest Conditioner<br>Endpoint           | esam/mcc_uri/password                   |
| Advanced Avail Controls > Ad Avail Trigger > Manifest Conditioner<br>Endpoint           | esam/mcc_uri/uri                        |
| Advanced Avail Controls > Ad Avail Trigger > Manifest Conditioner<br>Endpoint           | esam/mcc_uri/username                   |
| Advanced Avail Controls > Ad Avail Trigger > Alternate Manifest Conditioner<br>Endpoint | esam/alternate_mcc_uri/certificate_file |
| Advanced Avail Controls > Ad Avail Trigger > Alternate Manifest Conditioner<br>Endpoint | esam/alternate_mcc_uri/interface        |
| Advanced Avail Controls > Ad Avail Trigger > Alternate Manifest Conditioner<br>Endpoint | esam/alternate_mcc_uri/password         |
| Advanced Avail Controls > Ad Avail Trigger > Alternate Manifest Conditioner<br>Endpoint | esam/alternate_mcc_uri/uri              |
| Advanced Avail Controls > Ad Avail Trigger > Alternate Manifest Conditioner<br>Endpoint | esam/alternate_mcc_uri/username         |
| Advanced Avail Controls > Ad Avail Trigger > Response Signal<br>Preroll                 | esam/response_signal_preroll/           |
