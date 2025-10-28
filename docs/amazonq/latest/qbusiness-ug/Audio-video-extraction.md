# Extracting semantic meaning from audio and

video content

Amazon Q Business extracts semantic information from audio and video files,
making data sources queryable and enhancing information retrieval.

## Capabilities

- Processes up to 10 GB of video and 2 GB of audio
- Builds a comprehensive knowledge base

## Enabling Content

Extraction

- Use the Amazon Q Business console or API
- Available when adding connectors or importing files

## Audio and video extraction

###### The System extracts the following from audio and video files:

- Transcribed text from audio voice content
- Time-stamped indexing of content
- Summary and theme detection

###### Important

Processing multimedia content takes longer than text-only documents.
Incremental sync mode is recommended for multimedia processing.

Query audio and video content using natural language, and explore deeper with
follow-up questions.

## Processing

Considerations

- Audio and video files take longer to process than text-only files
- Amazon Q Business doesn't charge for re-synchronizations (re-syncs) when content
  remains unchanged.

## Additional

Information

- For sync modes, see [Sync mode](connector-concepts.md#connector-sync-mode "connector-concepts.md#connector-sync-mode")
- For pricing details, see [Amazon Q Business
  pricing](https://aws.amazon.com/q/business/pricing/ "https://aws.amazon.com/q/business/pricing/")

## Guidelines and

requirements

###### The following guidelines and best practices apply to content extraction from

audio and video. Supported formats:

- Audio files - MP3, WAV, M4A, FLAC, OGG
- Video files - MP4, MOV, M4V

###### File limitations:

- Audio and video maximum duration: 4 hours
- English-language content only

###### The following connectors use incremental sync mode for connectors processing

multimedia content, and can consider additional costs for multimedia processing:

- [Amazon S3](s3-connector.md "s3-connector.md")
- [Google
  Drive](google-connector.md "google-connector.md")

## Ingest Audio/Video

documents using the console

1. Login to your personal AWS account
2. Create a new application or use an existing application

### Ingest

Audio/Video files using direct upload

Open the application, whether it is a newly created application or an application
you have used previously:

1. Click **Add data source**
2. Select the **Upload Files** option
3. Upload a supported Audio/Video file
4. In the **File Indexing Configuration**, select the
   audio/video files option based on the files you uploaded
5. Click the upload button on the bottom right corner
6. Monitor the uploaded file source under the data source tab. The status
   will update in sequence: "Received" => "Processing" => "Indexed/Updated"
7. Once the status is Indexed/Updated, it means your file is indexed
   successfully

###### Note

For file uploads, the Audio/Video size limit is consistent with the general
file size limit of 50 MB.

### Ingest

Audio/Video documents using data source

Open the application, whether it is a newly created application or an application
you have used previously:

1. Click **Add data source**
2. Select any supported data source
3. Fill in the following information:
   1. Enter the data source name
   2. For the IAM role, select from the dropdown menu **Create
      new service role**
   3. Enter the S3 bucket containing the Audio/Video files in the
      **Data Source Location** field under
      **Sync scope**
   4. Set **Sync Mode** and **Sync Run** as per your requirement
   5. Click on **Add data source** on the bottom right
      corner

4. Navigate to the **Data sources** pag and select the data
   source created and click **Sync now**
5. Click on the data source created, wait for the sync to complete and verify
   no documents from the Sync history tab **Failed to be
   indexed**
