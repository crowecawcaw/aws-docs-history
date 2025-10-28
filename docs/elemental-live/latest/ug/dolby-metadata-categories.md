# Categories of metadata: Delivered

and encoder control

There are two categories of parameters in the Dolby metadata, characterized by how
Elemental Live uses it:

- Delivered: Elemental Live does not read these parameters, so they have no
  effect on the audio produced by Elemental Live. Instead, they are included as
  metadata in the output in order to **deliver** them to the
  downstream decoder.

“Delivered” metadata is also called _Consumer_ metadata
because it is intended to be used by the end consumer’s home decoder.

- Encoder Control: Elemental Live uses these parameters to manipulate the audio
  just before encoding the stream and producing the output. They provide a mechanism for Elemental Live to control the transcoding performed by Elemental Live. These parameters
  are never included in the output metadata.

“Encoder Control” metadata is also called _Professional_
metadata because it is intended to be used by a professional device – in our case
Elemental Live. It is never intended for the end consumer's home
decoder.
