# Audio:

Transcode support and passthrough support for Dolby audio
codecs

Three Dolby codecs are supported and can be transcoded or passed
through as follows:

- Dolby Digital (AC-3): Can be re-encoded as Dolby Digital or
  the original Dolby Digital can be passed through.
- Dolby Digital Plus (E-AC-3): Can be re-encoded as Dolby
  Digital Plus or the original Dolby Digital Plus can be passed
  through.
- Dolby E: Can be passed through as Dolby E. Cannot be
  re-encoded as Dolby E.
  The following table specifies the fields on the input side and on
  the output side that control passthrough versus transcoding.

| Input                                                    | Output > Stream                 | Result                      |
| -------------------------------------------------------- | ------------------------------- | --------------------------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Codec Detected in Input                                  | Value in Unwrap SMPTE 337 Field | Value in Output Codec Field | Value in Automatic Passthrough Field |                                                                                                                                                                                  |
| Dolby Digital                                            | n/a                             | Dolby Digital               | n/a                                  | Re-encoded to Dolby Digital                                                                                                                                                      |
| Dolby Digital                                            | n/a                             | Dolby Digital Passthrough   | n/a                                  | Passthrough of Dolby Digital                                                                                                                                                     |
| Dolby Digital Plus                                       | n/a                             | Dolby Digital Plus          | Checked                              | Passthrough of Dolby Digital Plus                                                                                                                                                |
| Dolby Digital Plus                                       | n/a                             | Dolby Digital Plus          | Unchecked                            | Re-encoded to Dolby Digital Plus                                                                                                                                                 |
| Dolby Digital Plus                                       | n/a                             | Dolby Digital Passthrough   | n/a                                  | Passthrough of Dolby Digital Plus                                                                                                                                                |
| Dolby Digital Plus and a non-Dolby Digital Plus<br>codec | n/a                             | Dolby Digital Plus          | Checked                              | The non-Dolby Digital Plus audio is transcoded to<br>Dolby Digital Plus. The Dolby Digital Plus audio is<br>passed through (it will not be re-encoded as Dolby<br>Digital Plus). |
| Dolby Digital Plus and a non-Dolby Digital Plus<br>codec | n/a                             | Dolby Digital Plus          | Unchecked                            | The non-Dolby Digital Plus audio is transcoded to<br>Dolby Digital Plus. The Dolby Digital Plus audio is<br>re-encoded to Dolby Digital Plus.                                    |
| Dolby Digital Plus and a non-Dolby Digital Plus<br>codec | n/a                             | Dolby Digital Passthrough   | n/a                                  | Not valid: setting up like this causes a validation<br>error.                                                                                                                    |
| Dolby E in a PCM stream tagged with SMPTE<br>337         | Unchecked                       | Uncompressed WAV            | n/a                                  | Passthrough of Dolby E.                                                                                                                                                          |
| Dolby E in a PCM stream tagged with SMPTE<br>337         | Unchecked                       | Uncompressed AIFF           | n/a                                  | Passthrough of Dolby E.                                                                                                                                                          |
