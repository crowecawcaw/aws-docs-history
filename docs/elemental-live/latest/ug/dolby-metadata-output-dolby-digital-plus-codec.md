# Output with

Dolby Digital Plus (EC2, EAC3) codec

| Named metadata parameters    | Category | Field                                                                                      | API tag (stream_assembly\ audio_description\ac3_settings) | Default            |
| ---------------------------- | -------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------------- | ------------------ |
| Dialogue Level               | D        | Dialnorm                                                                                   | dialnorm                                                  | Not set            |
| Channel Mode                 | D        | Coding Mode                                                                                | coding_mode                                               | 3/2 – L,R,C,LS,Rs  |
| LFE Channel                  | D        | When Coding Mode is 7 or 3/2, the LFE checkbox appears three lines below that<br>checkbox. | lfe                                                       | Enabled            |
| Bitstream Mode               | D        | Bitstream Mode                                                                             | bitstream_mode                                            | Complete Main      |
| Line Mode Compression        | D        | DRC Line Mode Profile                                                                      | drc_line                                                  | Film Std.          |
| RF Mode Compression          | D        | DRC RF Mode Profile                                                                        | drc_rf                                                    | Film Std.          |
| RF Overmodulation Protection | D        | No user control                                                                            | -                                                         |                    |
| Center Downmix Level         | D        | No user control                                                                            | -                                                         | -3dB               |
| Surround Downmix Level       | D        | Stereo Downmix                                                                             | stereo_downmix                                            | Not indicated      |
| Dolby Surround Mode          | D        | No user control                                                                            | -                                                         | Disabled           |
| Audio Production Information | D        | No user control                                                                            | -                                                         | 0 (does not exist) |
| Mix Level                    | D        | No user control                                                                            | -                                                         | Not set            |
| Room Type                    | D        | No user control                                                                            | -                                                         | Note set           |
| Copyright Bit                | D        | No user control                                                                            | -                                                         | 0                  |
| Original Bitstream           | D        | No user control                                                                            | -                                                         | 0                  |
| Preferred Stereo Downmix     | D        | No user control                                                                            | -                                                         | Not indicated      |
| Lt/Rt Center Downmix Level   | D        | Lt/Rt Center Mix Level                                                                     | lt_rt_center_mix_level                                    | -3.0 dB            |
| Lt/Rt Surround Downmix Level | D        | Lt/Rt Surround Mix Level                                                                   | lt_rt_surround_mix_level                                  | -3.0 dB            |
| Lo/Ro Center Downmix Level   | D        | Lo/Ro Center Mix Level                                                                     | lo_ro_center_mix_level                                    | -3.0 dB            |
| Lo/Ro Surround Downmix Level | D        | Lo/Ro Surround Mix Level                                                                   | lo_ro_surround_mix_level                                  | -3.0 dB            |
| Dolby Surround EX Mode       | D        | Surround EX Mode                                                                           | surround_ex_mode                                          | Disabled           |
| A/D Converter Type           | D        | No user control                                                                            |                                                           | 0 (standard)       |
| DC Filter                    | EC       | CD Highpass Filter                                                                         | dc_filter                                                 | Enabled            |
| LFE Lowpass Filter           | EC       | LFE Filter                                                                                 | lfe_filter                                                | Enabled            |
| Surround 3 dB Attenuation    | EC       | 3 dB Attenuation                                                                           | attenuate_3_db                                            | Disabled           |
| Surround Phase Shift         | EC       | 90-degree Phase Shift                                                                      | phase_shift_90_degree                                     | Enabled            |
| Surround Mode                | D        | When Coding Mode is 2/0, the Surround Mode checkbox appears.                               | surround_mode                                             | Not indicated      |
