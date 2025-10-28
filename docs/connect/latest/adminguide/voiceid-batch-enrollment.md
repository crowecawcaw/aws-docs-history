# Batch enrollment in Amazon Connect Voice ID using

audio data from prior calls

###### Note

End of support notice: On May 20, 2026, AWS will end support for Amazon Connect
Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the
Amazon Connect console, access Voice ID features on the Amazon Connect admin website or Contact Control Panel, or access Voice ID
resources. For more information, visit [Amazon Connect
Voice ID end of support](amazonconnect-voiceid-end-of-support.md "amazonconnect-voiceid-end-of-support.md").

You can get a jump start on using biometrics by batch enrolling customers who have
already consented for biometrics. Using stored audio recordings in your S3 bucket,
and a JSON input file that provides the speaker identifier and a link to the audio
recordings, you can invoke the [Voice ID
batch](../../../voiceid/latest/APIReference/API_StartSpeakerEnrollmentJob.md "../../../voiceid/latest/APIReference/API_StartSpeakerEnrollmentJob.md") APIs.

To enroll customers programmatically, pass the following data to the API:

1. The domain ID to specify the domain to associate recordings to.
2. The location for the output file.
3. An input file containing a list of speakers. See [Input and output file schema for the
   Speaker Enrollment Job in Amazon Connect Voice ID](speaker-enrollment-job-schema.md "speaker-enrollment-job-schema.md").

For each speaker the file must include:

    * A link to a call audio recording in a .wav file with 8KHz sample
     rate and PCM-16 encoding.
    * The corresponding `CustomerSpeakerId` for the
     customer.
    * A channel for the caller in the audio recording. If the audio has
     multiple channels, you can select only one.

4.  A KMS key to use when writing the output.
5.  A role that Voice ID can assume. It must have access to the S3 bucket
    where the audio files are stored. This role must have access to any
    KMS key used to encrypt the files. It must also be able to write to the
    specified output location and use the KMS key requested for writing the
    output. Specifically, it must have the following permissions:

        * `s3:GetObject` on the input bucket.
        * `s3:PutObject` on the output bucket.
        * `kms:Decrypt` on the KMS key used for input bucket’s
         default encryption.
        * `kms:Decrypt` and `kms:GenerateDataKey` on
         the KMS key provided in the input which will be used for writing
         output file to the output bucket.

    You must have `iam:PassRole` permissions when making the call
    and providing the `dataAccessRole`. To enable confused deputy
    protection for the `dataAccessRole`, see [Amazon Connect Voice ID cross-service confused deputy
    prevention](cross-service-confused-deputy-prevention.md#voiceid-cross-service "cross-service-confused-deputy-prevention.md#voiceid-cross-service").

6.  Optionally, a fraud check skip flag in case you want to skip checks for
    fraud and voice spoofing on the enrollment audio.
7.  Optionally, specify a fraudster watchlist that you want to perform fraud
    checks against. If no watchlist is specified, Voice ID uses the default
    fraudster watchlist for the domain.
8.  Optionally, the fraud threshold in case you want to raise or lower the
    risk.
9.  Optionally, a flag to re-enroll enrolled customers. This is useful if you
    want to refresh the audio recording, since the default is to ignore
    previously enrolled customers.
    The batch enrollment returns the `CustomerSpeakerId`,
    `GeneratedSpeakerId`, and associated status for each entry. It stores
    this data in a JSON file at the output path you specify in the API.

###### Note

You are charged for enrolling speakers. For more information, see [Amazon Connect Voice ID
Pricing](https://aws.amazon.com/connect/pricing/ "https://aws.amazon.com/connect/pricing/").
