# Elements and tags in an event

input XML

This section lists all the elements and tags that could appear in
the input element of an event XML. This section does not include
exhaustive information about rules for if and when an element or tag
can be included. For tips on some tags, see [Add dynamic
playlist inputs](add-dynamic-playlist-inputs.md "add-dynamic-playlist-inputs.md").

```
<href></href>
<version></version>
<product></product>
<input>
  <deblock_enable></deblock_enable>
  <deblock_strength></deblock_strength>
  <error_clear_time></error_clear_time>
  <failback_rule></failback_rule>
  <hot_backup_pair></hot_backup_pair>
  <input_label></input_label>
  <loop_source></loop_source>
  <name></name>
  <no_psi></no_psi>
  <order></order>
  <program_id></program_id>
  <service_name></service_name>
  <service_provider_name></service_provider_name>
  `<image_inserter>`
    <image_x></image_x>
    <image_y></image_y>
    <opacity></opacity>
    `<image_inserter_input>`
      <uri></uri>
      <username></username>
      <password></password>
      <interface></interface>
    `</image_inserter_input>`
  `</image_inserter>`
  `<network_input>`
    <enable_fec_rx></enable_fec_rx>
    <interface ></interface >
    <password></password>
    <quad></quad>
    <udp_igmp_source></udp_igmp_source>
    <uri></uri>
    <username></username>
  `</network_input>`
  `<device_input>`
    <channel></channel>
    <channel_type></channel_type>
    <device_id></device_id>
    <device_name></device_name>
    <device_number></device_number>
    <device_type></device_type>
    <input_format></input_format>
    `<fec_settings>`
      <udp_igmp_source></udp_igmp_source>
      <uri></uri>
    `</fec_settings>`
    `<hdmi_settings>`
      <input_format></input_format>
    `</hdmi_settings>`
    `<sdi_settings>`
      <input_format></input_format>
      <scte104_offset></scte104_offset>
    `</sdi_settings>`
  `</device_input>`
  `<router_input>`
    <input_number></input_number>
    <input_number_end></input_number_end>
    <quad></quad>
    <router_ip></router_ip>
    <router_type></router_type>
  `</router_input>`
  `<file_input>`
    <certificate_file></certificate_file>
    <interface></interface>
    <password></password>
    <uri></uri>
    <username></username>
  `</file_input>`
  `<failover_condition>`
    <description></description>
    <duration></duration>
    <order></order>
  `</failover_condition>`
  `<video_selector>`
    <color_space></color_space>
    <default_afd></default_afd>
    <name></name>
    <order></order>
    <pid></pid>
    <program_id></program_id>
  `</video_selector>`
  `<audio_selector>`
    <default_selection></default_selection>
    <external_audio_file_input></external_audio_file_input>
    <infer_external_filename></infer_external_filename>
    <language_code></language_code>
    <name></name>
    <offset></offset>
    <order></order>
    <pid></pid>
    <program_selection></program_selection>
    <strict_language_selection></strict_language_selection>
    <strict_pid_option></strict_pid_option>
    <track></track>
    <unwrap_smpte337></unwrap_smpte337>
  `</audio_selector>`
  `<audio_selector_group>`
    <audio_selector_name></audio_selector_name>
    <name></name>
  </audio_selector_group>
  <caption_selector>
    <order></order>
    <source_type></source_type>
    <language_code></language_code>
    `<embedded_source_settings>`
      <autodetect_scte20></autodetect_scte20>
      <source_608_channel_number> </source_608_channel_number>
      <source_608_track_number ></source_608_track_number>
      <upconvert_608_to_708></upconvert_608_to_708>
    `</embedded_source_settings>`
    `<file_source_settings>`
      <time_delta></time_delta>
      <upconvert_608_to_708></upconvert_608_to_708>
      `<source_file>`
        <certificate_file></certificate_file>
        <interface></interface>
        <password></password>
        <uri></uri>
        <username></username>
      `</source_file>`
    `</file_source_settings>`
    `<teletext_source_settings>`
      <page_number></page_number>
    `</teletext_source_settings>`
    `<dvb_sub_source_settings>`
      <pid></pid>
    `</dvb_sub_source_settings>`
    <scte27_source_settings>
      <pid></pid>
    `</scte27_source_settings>`
  `</caption_selector>`
  `<input_clipping>`
    <end_timecode></end_timecode>
    <order></order>
    <start_timecode></start_timecode>
  `</input_clipping>`

```

Broken down into individual components, you can see:

| Function of code excerpt      | Example code excerpt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Various tags                  | `<br><href></href><br><version></version><br><product></product><br><input><br><deblock_enable></deblock_enable><br><deblock_strength></deblock_strength><br><error_clear_time></error_clear_time><br><failback_rule></failback_rule><br><hot_backup_pair></hot_backup_pair><br><input_label></input_label><br><loop_source></loop_source><br><name></name><br><no_psi></no_psi><br><order></order><br><program_id></program_id><br><service_name></service_name><br><service_provider_name></service_provider_name><br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Image inserter for this input | ``<br>`<image_inserter>`<br><image_x></image_x><br><image_y></image_y><br><opacity></opacity><br>`<image_inserter_input>`<br><uri></uri><br><username></username><br><password></password><br><interface></interface><br>`</image_inserter_input>`<br>`</image_inserter>`<br>``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Input source                  | ``<br>`<network_input>`<br><enable_fec_rx></enable_fec_rx><br><interface ></interface ><br><password></password><br><quad></quad><br><udp_igmp_source></udp_igmp_source><br><uri></uri><br><username></username><br>`</network_input>`<br>`<device_input>`<br><channel></channel><br><channel_type></channel_type><br><device_id></device_id><br><device_name></device_name><br><device_number></device_number><br><device_type></device_type><br><input_format></input_format><br>`<fec_settings>`<br><udp_igmp_source></udp_igmp_source><br><uri></uri><br>`</fec_settings>`<br>`<hdmi_settings>`<br><input_format></input_format><br>`</hdmi_settings>`<br>`<sdi_settings>`<br><input_format></input_format><br><scte104_offset></scte104_offset><br>`</sdi_settings>`<br>`</device_input>`<br>`<router_input>`<br><input_number></input_number><br><input_number_end></input_number_end><br><quad></quad><br><router_ip></router_ip><br><router_type></router_type><br>`</router_input>`<br>`<file_input>`<br><certificate_file></certificate_file><br><interface></interface><br><password></password><br><uri></uri><br><username></username><br>`</file_input>`<br>`` |
| Failover                      | ``<br>`<failover_condition>`<br><description></description><br><duration></duration><br><order></order><br>`</failover_condition>`<br>``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Source video                  | ``<br>`<video_selector>`<br><color_space></color_space><br><default_afd></default_afd><br><name></name><br><order></order><br><pid></pid><br><program_id></program_id><br>`</video_selector>`<br>``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Source audio                  | ``<br>`<audio_selector>`<br><default_selection></default_selection><br><external_audio_file_input></external_audio_file_input><br><infer_external_filename></infer_external_filename><br><language_code></language_code><br><name></name><br><offset></offset><br><order></order><br><pid></pid><br><program_selection></program_selection><br><strict_language_selection></strict_language_selection><br><strict_pid_option></strict_pid_option><br><track></track><br><unwrap_smpte337></unwrap_smpte337><br>`</audio_selector>`<br>`<audio_selector_group>`<br><audio_selector_name></audio_selector_name><br><name></name><br></audio_selector_group><br>``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Source captions               | ``<br><caption_selector><br><order></order><br><source_type></source_type><br><language_code></language_code><br>`<embedded_source_settings>`<br><autodetect_scte20></autodetect_scte20><br><source_608_channel_number> </source_608_channel_number><br><source_608_track_number ></source_608_track_number><br><upconvert_608_to_708></upconvert_608_to_708><br>`</embedded_source_settings>`<br>`<file_source_settings>`<br><time_delta></time_delta><br><upconvert_608_to_708></upconvert_608_to_708><br>`<source_file>`<br><certificate_file></certificate_file><br><interface></interface><br><password></password><br><uri></uri><br><username></username><br>`</source_file>`<br>`</file_source_settings>`<br>`<teletext_source_settings>`<br><page_number></page_number><br>`</teletext_source_settings>`<br>`<dvb_sub_source_settings>`<br><pid></pid><br>`</dvb_sub_source_settings>`<br><scte27_source_settings><br><pid></pid><br>`</scte27_source_settings>`<br>`</caption_selector>`<br>``                                                                                                                                                                     |
| Input clipping                | ``<br>`<input_clipping>`<br><end_timecode></end_timecode><br><order></order><br><start_timecode></start_timecode><br>`</input_clipping>`<br>``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
