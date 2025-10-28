# Translation processing modes

When translating documents, you can use two different translation processing modes:
real-time translation or asynchronous batch processing. The mode you use is based on the size
and type of the target documents and affects how you submit the translation job and view its
results.

- [Real-time translation](sync.md "sync.md") – You make a synchronous request
  to translate a small amount of text (or a text file) and Amazon Translate responds immediately with
  the translated text.
- [Asynchronous batch processing](async.md "async.md") – You put a
  collection of documents in an Amazon Simple Storage Service (Amazon S3) location and start an asynchronous
  processing job to translate them. Amazon Translate sends the translated output documents to a
  specified Amazon S3 location.
