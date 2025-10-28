# Analyzing Identity Documentation with Amazon Textract

To analyze identity documents, you use the AnalyzeID API operation, and pass a document
file as input. `AnalyzeID` returns a JSON structure that contains the analyzed
text. For more information, see [Analyzing Identity Documents](how-it-works-identity.md "how-it-works-identity.md").

You can provide an input document as an image byte array (base64-encoded image bytes), or as an Amazon S3
object. In this procedure, you upload an image file to your S3 bucket and specify the file name.

###### To analyze an identity document (API)

1. If you haven't already:
   1. Give a user the `AmazonTextractFullAccess` and
      `AmazonS3ReadOnlyAccess` permissions. For more
      information, see [Step 1: Set Up an AWS Account and Create a User](setting-up.md "setting-up.md").
   2. Install and configure the AWS CLI and the AWS SDKs. For more information, see [Step 2: Set Up the AWS CLI and AWS SDKs](setup-awscli-sdk.md "setup-awscli-sdk.md").

2. Upload an image that contains a document to your S3 bucket.

For instructions, see [Uploading Objects
into Amazon S3](../../../AmazonS3/latest/userguide/UploadingObjectsintoAmazonS3.md "../../../AmazonS3/latest/userguide/UploadingObjectsintoAmazonS3.md") in the
_Amazon Simple Storage Service User Guide_. 3. Use the following examples to call the `AnalyzeID` operation.

AWS CLI

The following example takes in an input file from an S3 bucket and runs the
`AnalyzeID` operation on it. In the following code, replace the value
of `Bucket` with the name of your S3 bucket and the value of
`Name` with the name of the file in your bucket. Replace
`profile-name` with the name of a profile that can assume the role and
`region` with the region in which you want to run the code.

```
aws textract analyze-id \
    --document-pages '{"S3Object":{"Bucket":"`bucket`","Name":"`name`"}}' \
    --profile `profile-name` \
    --region `region`
```

You can also call the API with the front and back of a driver's license by
adding another Amazon S3 object to the input.

```
aws textract analyze-id \
    --document-pages '[{"S3Object":{"Bucket":"`bucket`","Name":"`name front`"}}, {"S3Object":{"Bucket":"`bucket`","Name":"`name back`"}}]' \
    --profile `profile-name` \
    --region `region`
```

If you are accessing the CLI on a Windows device, use double quotes instead of
single quotes and escape the inner double quotes by backslash (\) to address any
parser errors you might encounter. For an example, see the following:

```
aws textract analyze-id --document-pages "[{\"S3Object\":{\"Bucket\":\"`bucket`\",\"Name\":\"`name`\"}}]" --region `region`
```

Python
The following example takes in an input file from an S3 bucket and runs the
`AnalyzeID` operation on it, returning the detected key-value pairs. In
the following code, replace the value of `bucket_name` with the name of
your S3 bucket and the value of `file_name` with the name of the file in
your bucket. Replace `profile-name` with the name of a profile that can
assume the role and `region` with the region in which you want to run the
code.

```
import boto3

def analyze_id(client, bucket_name, file_name):

    # Analyze document
    # process using S3 object
    response = client.analyze_id(
        DocumentPages=[{'S3Object': {'Bucket': bucket_name, 'Name': file_name}}])

    for doc_fields in response['IdentityDocuments']:
        for id_field in doc_fields['IdentityDocumentFields']:
            for key, val in id_field.items():
                if "Type" in str(key):
                    print("Type: " + str(val['Text']))
            for key, val in id_field.items():
                if "ValueDetection" in str(key):
                    print("Value Detection: " + str(val['Text']))
            print()

def main():
    session = boto3.Session(profile_name='profile-name')
    client = session.client('textract', region_name='region')
    bucket_name = "bucket"
    file_name = "file"

    analyze_id(client, bucket_name, file_name)

if __name__ == "__main__":
    main()

```

Java
The following example takes in an input file from an S3 bucket and runs the
`AnalyzeID` operation on it, returning the detected data. In the
function main, replace the values of `s3bucket` and
`sourceDoc` with the names of the Amazon S3 bucket and document image
that you used in step 2. Replace the value of `credentialsProvider` with
the name of your developer profile.

```
/*
   Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
   SPDX-License-Identifier: Apache-2.0
*/

package com.amazonaws.samples;


import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.textract.AmazonTextractClient;
import com.amazonaws.services.textract.AmazonTextractClientBuilder;
import com.amazonaws.services.textract.model.*;
import java.util.ArrayList;
import java.util.List;

public class AppTest1 {

 public static void main(String[] args) {

     final String USAGE = "\n" +
             "Usage:\n" +
             "    <s3bucket><sourceDoc> \n\n" +
             "Where:\n" +
             "    s3bucket - the Amazon S3 bucket where the document is located. \n" +
             "    sourceDoc - the name of the document. \n";

     if (args.length != 1) {
         System.out.println(USAGE);
         System.exit(1);
     }


  // set provider credentials
     AWSCredentialsProvider credentialsProvider = new ProfileCredentialsProvider("default");

     String s3bucket = "bucket-name"; //args[0];
     String sourceDoc = "sourcedoc-name";  //args[1];
     AmazonTextractClient textractClient = (AmazonTextractClient) AmazonTextractClientBuilder.standard().withCredentials(credentialsProvider)
             .withRegion(Regions.US_EAST_1)
             .build();

     getDocDetails(textractClient, s3bucket, sourceDoc);
 }

 public static void getDocDetails(AmazonTextractClient textractClient, String s3bucket, String sourceDoc ) {

    try {

         S3Object s3 = new S3Object();
         s3.setBucket(s3bucket);
         s3.setName(sourceDoc);

         com.amazonaws.services.textract.model.Document myDoc = new com.amazonaws.services.textract.model.Document();
         myDoc.setS3Object(s3);

         List<Document> list1 = new ArrayList();
         list1.add(myDoc);

         AnalyzeIDRequest idRequest = new AnalyzeIDRequest();
         idRequest.setDocumentPages(list1);

         AnalyzeIDResult result = textractClient.analyzeID(idRequest);
         List<IdentityDocument> docs =  result.getIdentityDocuments();
         for (IdentityDocument doc: docs) {

             List<IdentityDocumentField>idFields = doc.getIdentityDocumentFields();
             for (IdentityDocumentField field: idFields) {
                 System.out.println("Field type is "+ field.getType().getText());
                 System.out.println("Field value is "+ field.getValueDetection().getText());
             }
         }

    } catch (Exception e) {
         e.printStackTrace();
    }
 }
}
```

Java V2
The following example takes in an input file from an S3 bucket and runs the
`AnalyzeID` operation on it, returning the detected data. In the
function main, replace the values of `s3bucket` and
`sourceDoc` with the names of the S3 bucket and document image that you
used in step 2.

Replace `profile-name` in the line that creates the
`TextractClient` with the name of your developer profile.

```
import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.core.SdkBytes;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.textract.TextractClient;
import software.amazon.awssdk.services.textract.model.*;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
// snippet-end:[textract.java2._analyze_doc.import]
import java.util.Optional;

import org.json.JSONObject;

/**
 * Before running this Java V2 code example, set up your development environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class DetectCelebrityVideo {

    public static void main(String[] args) {

        final String usage = "\n" +
                 "Usage:\n" +
                 "    <bucketName> <docName> \n\n" +
                 "Where:\n" +
                 "    bucketName - The name of the Amazon S3 bucket that contains the document. \n\n" +
                 "    docName - The document name (must be an image, i.e., book.png). \n";

        if (args.length != 2) {
                 System.out.println(usage);
                 System.exit(1);
        }

       String bucketName = args[0];
       String docName = args[1];
       Region region = Region.US_WEST_2;
       TextractClient textractClient = TextractClient.builder()
                .region(region)
                .credentialsProvider(ProfileCredentialsProvider.create("default"))
                .build();

        analyzeID(textractClient, bucketName, docName);
        textractClient.close();
    }

    // snippet-start:[textract.java2._analyze_doc.main]
    public static void analyzeID(TextractClient textractClient, String bucketName, String docName) {

        try {
            S3Object s3Object = S3Object.builder()
                    .bucket(bucketName)
                    .name(docName)
                    .build();

                // Create a Document object and reference the s3Object instance
            Document myDoc = Document.builder()
                    .s3Object(s3Object)
                    .build();

            AnalyzeIdRequest analyzeIdRequest = AnalyzeIdRequest.builder()
                    .documentPages(myDoc).build();

            AnalyzeIdResponse analyzeId = textractClient.analyzeID(analyzeIdRequest);

           // System.out.println(analyzeExpense.toString());
            List<IdentityDocument> Docs = analyzeId.identityDocuments();
            for (IdentityDocument doc: Docs) {
               System.out.println(doc);
            }


        } catch (TextractException e) {

            System.err.println(e.getMessage());
            System.exit(1);
        }
    }
    // snippet-end:[textract.java2._analyze_doc.main]
}
```

4. This will provide you with the JSON output for the `AnalyzeID` operation.
