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

| Function of code excerpt      | Example code excerpt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Various tags                  | `<href></href> <version></version> <product></product> <input> <deblock_enable></deblock_enable> <deblock_strength></deblock_strength> <error_clear_time></error_clear_time> <failback_rule></failback_rule> <hot_backup_pair></hot_backup_pair> <input_label></input_label> <loop_source></loop_source> <name></name> <no_psi></no_psi> <order></order> <program_id></program_id> <service_name></service_name> <service_provider_name></service_provider_name>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Image inserter for this input | `` `<image_inserter>` <image_x></image_x> <image_y></image_y> <opacity></opacity> `<image_inserter_input>` <uri></uri> <username></username> <password></password> <interface></interface> `</image_inserter_input>` `</image_inserter>` ``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Input source                  | `` `<network_input>` <enable_fec_rx></enable_fec_rx> <interface ></interface > <password></password> <quad></quad> <udp_igmp_source></udp_igmp_source> <uri></uri> <username></username> `</network_input>` `<device_input>` <channel></channel> <channel_type></channel_type> <device_id></device_id> <device_name></device_name> <device_number></device_number> <device_type></device_type> <input_format></input_format> `<fec_settings>` <udp_igmp_source></udp_igmp_source> <uri></uri> `</fec_settings>` `<hdmi_settings>` <input_format></input_format> `</hdmi_settings>` `<sdi_settings>` <input_format></input_format> <scte104_offset></scte104_offset> `</sdi_settings>` `</device_input>` `<router_input>` <input_number></input_number> <input_number_end></input_number_end> <quad></quad> <router_ip></router_ip> <router_type></router_type> `</router_input>` `<file_input>` <certificate_file></certificate_file> <interface></interface> <password></password> <uri></uri> <username></username> `</file_input>` `` |
| Failover                      | `` `<failover_condition>` <description></description> <duration></duration> <order></order> `</failover_condition>` ``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Source video                  | `` `<video_selector>` <color_space></color_space> <default_afd></default_afd> <name></name> <order></order> <pid></pid> <program_id></program_id> `</video_selector>` ``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Source audio                  | `` `<audio_selector>` <default_selection></default_selection> <external_audio_file_input></external_audio_file_input> <infer_external_filename></infer_external_filename> <language_code></language_code> <name></name> <offset></offset> <order></order> <pid></pid> <program_selection></program_selection> <strict_language_selection></strict_language_selection> <strict_pid_option></strict_pid_option> <track></track> <unwrap_smpte337></unwrap_smpte337> `</audio_selector>` `<audio_selector_group>` <audio_selector_name></audio_selector_name> <name></name> </audio_selector_group> ``                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Source captions               | `` <caption_selector> <order></order> <source_type></source_type> <language_code></language_code> `<embedded_source_settings>` <autodetect_scte20></autodetect_scte20> <source_608_channel_number> </source_608_channel_number> <source_608_track_number ></source_608_track_number> <upconvert_608_to_708></upconvert_608_to_708> `</embedded_source_settings>` `<file_source_settings>` <time_delta></time_delta> <upconvert_608_to_708></upconvert_608_to_708> `<source_file>` <certificate_file></certificate_file> <interface></interface> <password></password> <uri></uri> <username></username> `</source_file>` `</file_source_settings>` `<teletext_source_settings>` <page_number></page_number> `</teletext_source_settings>` `<dvb_sub_source_settings>` <pid></pid> `</dvb_sub_source_settings>` <scte27_source_settings> <pid></pid> `</scte27_source_settings>` `</caption_selector>` ``                                                                                                                                 |
| Input clipping                | `` `<input_clipping>` <end_timecode></end_timecode> <order></order> <start_timecode></start_timecode> `</input_clipping>` ``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
