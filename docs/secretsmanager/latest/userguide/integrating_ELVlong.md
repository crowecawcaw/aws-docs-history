# How AWS Elemental Live uses AWS Secrets Manager

AWS Elemental Live is a real-time video service that lets you create live outputs for broadcast
and streaming delivery.

AWS Elemental Live uses a secret ARN to get a secret that contains an encryption key from
Secrets Manager. Elemental Live uses the encryption key to encrypt/decrypt the video. For more information,
see [How delivery from AWS Elemental Live to MediaConnect works at runtime](../../../elemental-live/latest/ug/setting-up-live-as-contribution-encoder-for-mediaconnect-how-it-works-at-runtime.md "../../../elemental-live/latest/ug/setting-up-live-as-contribution-encoder-for-mediaconnect-how-it-works-at-runtime.md") in the
_Elemental Live User Guide_.
