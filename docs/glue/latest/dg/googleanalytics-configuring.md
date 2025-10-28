# Configuring Google Analytics 4

Before you can use AWS Glue to transfer from Google Analytics 4, you must meet these requirements:

## Minimum requirements

- You have a Google Analytics account with one or more data streams that collect the data that you want to
  transfer.
- You have a Google Cloud Platform account and a Google Cloud project.
- In your Google Cloud project, you've enabled the following APIs:
  - Google Analytics API
  - Google Analytics Admin API
  - Google Analytics Data API

- In your Google Cloud project, you've configured an OAuth consent screen for external users. For information about
  the OAuth consent screen, see
  [Setting up your OAuth consent screen](https://support.google.com/cloud/answer/10311615# "https://support.google.com/cloud/answer/10311615#")
  in the Google Cloud Platform Console Help.
- In your Google Cloud project, you've configured an OAuth 2.0 client ID. For more information, see
  [Setting up OAuth 2.0](https://support.google.com/cloud/answer/6158849?hl=en#zippy= "https://support.google.com/cloud/answer/6158849?hl=en#zippy=") .

If you meet these requirements, you’re ready to connect AWS Glue to your Google Analytics 4 account.
