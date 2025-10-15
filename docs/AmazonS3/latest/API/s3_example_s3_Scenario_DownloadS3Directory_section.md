# Download S3 'directories' from an Amazon Simple Storage Service (Amazon S3) bucket

The following code example shows how to download and filter the contents of Amazon S3 bucket 'directories'.


Java


**SDK for Java 2.x**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3#code-examples").
 


This example show how to use the [S3TransferManager](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/transfer/s3/S3TransferManager.html "https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/transfer/s3/S3TransferManager.html") in the AWS SDK for Java 2.x to download 'directories' from an Amazon S3 bucket. It also demonstrates how to use [DownloadFilters](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/transfer/s3/config/DownloadFilter.html "https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/transfer/s3/config/DownloadFilter.html") in the request.



```
    /**
     * For standard buckets, S3 provides the illusion of a directory structure through the use of keys. When you upload
     * an object to an S3 bucket, you specify a key, which is essentially the "path" to the object. The key can contain
     * forward slashes ("/") to make it appear as if the object is stored in a directory structure, but this is just a
     * logical representation, not an actual directory.
     * <p><pre>
     * In this example, our S3 bucket contains the following objects:
     *
     * folder1/file1.txt
     * folder1/file2.txt
     * folder1/file3.txt
     * folder2/file1.txt
     * folder2/file2.txt
     * folder2/file3.txt
     * folder3/file1.txt
     * folder3/file2.txt
     * folder3/file3.txt
     *
     * When method `downloadS3Directories` is invoked with
     * `destinationPathURI` set to `/test`, the downloaded
     * directory looks like:
     *
     * |- test
     *    |- folder1
     *    	  |- file1.txt
     *    	  |- file2.txt
     *    	  |- file3.txt
     *    |- folder3
     *    	  |- file1.txt
     *    	  |- file2.txt
     *    	  |- file3.txt
     * </pre>
     *
     * @param transferManager    An S3TransferManager instance.
     * @param destinationPathURI local directory to hold the downloaded S3 'directories' and files.
     * @param bucketName         The S3 bucket that contains the 'directories' to download.
     * @return The number of objects (files, in this case) that were downloaded.
     */
    public Integer downloadS3Directories(S3TransferManager transferManager,
                                         URI destinationPathURI, String bucketName) {

        // Define the filters for which 'directories' we want to download.
        DownloadFilter folder1Filter = (S3Object s3Object) -> s3Object.key().startsWith("folder1/");
        DownloadFilter folder3Filter = (S3Object s3Object) -> s3Object.key().startsWith("folder3/");
        DownloadFilter folderFilter = s3Object -> folder1Filter.or(folder3Filter).test(s3Object);

        DirectoryDownload directoryDownload = transferManager.downloadDirectory(DownloadDirectoryRequest.builder()
                .destination(Paths.get(destinationPathURI))
                .bucket(bucketName)
                .filter(folderFilter)
                .build());
        CompletedDirectoryDownload completedDirectoryDownload = directoryDownload.completionFuture().join();

        Integer numFilesInFolder1 = Paths.get(destinationPathURI).resolve("folder1").toFile().list().length;
        Integer numFilesInFolder3 = Paths.get(destinationPathURI).resolve("folder3").toFile().list().length;

        try {
            assert numFilesInFolder1 == 3;
            assert numFilesInFolder3 == 3;
            assert !Paths.get(destinationPathURI).resolve("folder2").toFile().exists(); // `folder2` was not downloaded.
        } catch (AssertionError e) {
            logger.error("An assertion failed.");
        }

        completedDirectoryDownload.failedTransfers()
                .forEach(fail -> logger.warn("Object failed to transfer  [{}]", fail.exception().getMessage()));
        return numFilesInFolder1 + numFilesInFolder3;
    }


```




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
