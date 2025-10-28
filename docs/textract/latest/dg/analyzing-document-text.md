# Analyzing Document Text with Amazon Textract

To analyze text in a document, you use the [AnalyzeDocument](API_AnalyzeDocument.md "API_AnalyzeDocument.md") operation, and pass a document file as input.
`AnalyzeDocument` returns a JSON structure that contains the analyzed
text. For more information, see [Analyzing Documents](how-it-works-analyzing.md "how-it-works-analyzing.md").

You can provide an input document as an image byte array (base64-encoded image
bytes), or as an Amazon S3 object. In this procedure, you upload an image file to
your S3 bucket and specify the file name.

###### To analyze text in a document (API)

1. If you haven't already:
   1. Give a user the `AmazonTextractFullAccess` and
      `AmazonS3ReadOnlyAccess` permissions. For more
      information, see [Step 1: Set Up an AWS Account and Create a User](setting-up.md "setting-up.md").
   2. Install and configure the AWS CLI and the AWS SDKs. For more information, see [Step 2: Set Up the AWS CLI and AWS SDKs](setup-awscli-sdk.md "setup-awscli-sdk.md").

2. Upload an image that contains a document to your S3 bucket.

For instructions, see [Uploading Objects
into Amazon S3](../../../AmazonS3/latest/userguide/upload-objects.md "../../../AmazonS3/latest/userguide/upload-objects.md") in the
_Amazon Simple Storage Service User Guide_. 3. Use the following examples to call the `AnalyzeDocument` operation.

Java
The following example code displays the document and boxes around detected
items.

In the function `main`, replace the values of `bucket` and
`document` with the names of the Amazon S3 bucket and document image that
you used in step 2. Replace the value of `credentialsProvider` with the
name of your developer profile.

```

//Loads document from S3 bucket. Displays the document and polygon around detected lines of text.
import java.awt.*;
import java.awt.image.BufferedImage;
import java.util.List;
import javax.imageio.ImageIO;
import javax.swing.*;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.S3ObjectInputStream;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.textract.AmazonTextract;
import com.amazonaws.services.textract.AmazonTextractClientBuilder;
import com.amazonaws.services.textract.model.AnalyzeDocumentRequest;
import com.amazonaws.services.textract.model.AnalyzeDocumentResult;
import com.amazonaws.services.textract.model.Block;
import com.amazonaws.services.textract.model.BoundingBox;
import com.amazonaws.services.textract.model.Document;
import com.amazonaws.services.textract.model.S3Object;
import com.amazonaws.services.textract.model.Point;
import com.amazonaws.services.textract.model.Relationship;
import com.amazonaws.client.builder.AwsClientBuilder.EndpointConfiguration;

public class AnalyzeDocument extends JPanel {

    private static final long serialVersionUID = 1L;

    BufferedImage image;

    AnalyzeDocumentResult result;

    public AnalyzeDocument(AnalyzeDocumentResult documentResult, BufferedImage bufImage) throws Exception {
        super();

        result = documentResult; // Results of text detection.
        image = bufImage; // The image containing the document.

    }

    // Draws the image and text bounding box.
    public void paintComponent(Graphics g) {

        int height = image.getHeight(this);
        int width = image.getWidth(this);

        Graphics2D g2d = (Graphics2D) g; // Create a Java2D version of g.

        // Draw the image.
        g2d.drawImage(image, 0, 0, image.getWidth(this), image.getHeight(this), this);

        // Iterate through blocks and display bounding boxes around everything.

        List<Block> blocks = result.getBlocks();
        for (Block block : blocks) {
            DisplayBlockInfo(block);
            switch(block.getBlockType()) {

            case "KEY_VALUE_SET":
                if (block.getEntityTypes().contains("KEY")){
                    ShowBoundingBox(height, width, block.getGeometry().getBoundingBox(), g2d, new Color(255,0,0));
                }
                else {  //VALUE
                    ShowBoundingBox(height, width, block.getGeometry().getBoundingBox(), g2d, new Color(0,255,0));
                }
                break;
            case "TABLE":
                ShowBoundingBox(height, width, block.getGeometry().getBoundingBox(), g2d, new Color(0,0,255));
                break;
            case "CELL":
                ShowBoundingBox(height, width, block.getGeometry().getBoundingBox(), g2d, new Color(255,255,0));
                break;
            case "SELECTION_ELEMENT":
                if (block.getSelectionStatus().equals("SELECTED"))
                    ShowSelectedElement(height, width, block.getGeometry().getBoundingBox(), g2d, new Color(0,0,255));
                break;
            default:
                //PAGE, LINE & WORD
                //ShowBoundingBox(height, width, block.getGeometry().getBoundingBox(), g2d, new Color(200,200,0));
            }
        }

         // uncomment to show polygon around all blocks
         //ShowPolygon(height,width,block.getGeometry().getPolygon(),g2d);


    }

    // Show bounding box at supplied location.
    private void ShowBoundingBox(int imageHeight, int imageWidth, BoundingBox box, Graphics2D g2d, Color color) {

        float left = imageWidth * box.getLeft();
        float top = imageHeight * box.getTop();

        // Display bounding box.
        g2d.setColor(color);
        g2d.drawRect(Math.round(left), Math.round(top),
                Math.round(imageWidth * box.getWidth()), Math.round(imageHeight * box.getHeight()));

    }
    private void ShowSelectedElement(int imageHeight, int imageWidth, BoundingBox box, Graphics2D g2d, Color color) {

        float left = imageWidth * box.getLeft();
        float top = imageHeight * box.getTop();

        // Display bounding box.
        g2d.setColor(color);
        g2d.fillRect(Math.round(left), Math.round(top),
                Math.round(imageWidth * box.getWidth()), Math.round(imageHeight * box.getHeight()));

    }

    // Shows polygon at supplied location
    private void ShowPolygon(int imageHeight, int imageWidth, List<Point> points, Graphics2D g2d) {

        g2d.setColor(new Color(0, 0, 0));
        Polygon polygon = new Polygon();

        // Construct polygon and display
        for (Point point : points) {
            polygon.addPoint((Math.round(point.getX() * imageWidth)),
                    Math.round(point.getY() * imageHeight));
        }
        g2d.drawPolygon(polygon);
    }
    //Displays information from a block returned by text detection and text analysis
    private void DisplayBlockInfo(Block block) {
        System.out.println("Block Id : " + block.getId());
        if (block.getText()!=null)
            System.out.println("    Detected text: " + block.getText());
        System.out.println("    Type: " + block.getBlockType());

        if (block.getBlockType().equals("PAGE") !=true) {
            System.out.println("    Confidence: " + block.getConfidence().toString());
        }
        if(block.getBlockType().equals("CELL"))
        {
            System.out.println("    Cell information:");
            System.out.println("        Column: " + block.getColumnIndex());
            System.out.println("        Row: " + block.getRowIndex());
            System.out.println("        Column span: " + block.getColumnSpan());
            System.out.println("        Row span: " + block.getRowSpan());

        }

        System.out.println("    Relationships");
        List<Relationship> relationships=block.getRelationships();
        if(relationships!=null) {
            for (Relationship relationship : relationships) {
                System.out.println("        Type: " + relationship.getType());
                System.out.println("        IDs: " + relationship.getIds().toString());
            }
        } else {
            System.out.println("        No related Blocks");
        }

        System.out.println("    Geometry");
        System.out.println("        Bounding Box: " + block.getGeometry().getBoundingBox().toString());
        System.out.println("        Polygon: " + block.getGeometry().getPolygon().toString());

        List<String> entityTypes = block.getEntityTypes();

        System.out.println("    Entity Types");
        if(entityTypes!=null) {
            for (String entityType : entityTypes) {
                System.out.println("        Entity Type: " + entityType);
            }
        } else {
            System.out.println("        No entity type");
        }

        if(block.getBlockType().equals("SELECTION_ELEMENT")) {
            System.out.print("    Selection element detected: ");
            if (block.getSelectionStatus().equals("SELECTED")){
                System.out.println("Selected");
            }else {
                System.out.println(" Not selected");
            }
        }

        if(block.getPage()!=null)
            System.out.println("    Page: " + block.getPage());
        System.out.println();
    }

    public static void main(String arg[]) throws Exception {

        // The S3 bucket and document
        String document = "";
        String bucket = "";

        // set provider credentials
        AWSCredentialsProvider credentialsProvider = new ProfileCredentialsProvider("default");

        AmazonS3 s3client = AmazonS3ClientBuilder.standard().withCredentials(credentialsProvider)
                .withEndpointConfiguration(
                        new EndpointConfiguration("https://s3.amazonaws.com","us-east-1"))
                .build();


        // Get the document from S3
        com.amazonaws.services.s3.model.S3Object s3object = s3client.getObject(bucket, document);
        S3ObjectInputStream inputStream = s3object.getObjectContent();
        BufferedImage image = ImageIO.read(inputStream);

        // Call AnalyzeDocument
        EndpointConfiguration endpoint = new EndpointConfiguration(
                "https://textract.us-east-1.amazonaws.com", "us-east-1");
        AmazonTextract client = AmazonTextractClientBuilder.standard().withCredentials(credentialsProvider)
                .withEndpointConfiguration(endpoint).build();


        AnalyzeDocumentRequest request = new AnalyzeDocumentRequest()
                .withFeatureTypes("TABLES","FORMS","SIGNATURES")
                 .withDocument(new Document().
                        withS3Object(new S3Object().withName(document).withBucket(bucket)));


        AnalyzeDocumentResult result = client.analyzeDocument(request);

        // Create frame and panel.
        JFrame frame = new JFrame("RotateImage");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        AnalyzeDocument panel = new AnalyzeDocument(result, image);
        panel.setPreferredSize(new Dimension(image.getWidth(), image.getHeight()));
        frame.setContentPane(panel);
        frame.pack();
        frame.setVisible(true);

    }
}
```

Java V2
The following example code displays the document and boxes around
lines of detected text.

In the function `main`, replace the values of
`bucket` and `document` with the names of the Amazon S3 bucket
and document that you used in step 2. Replace `profile-name` in the line
that creates the `TextractClient` with the name of your developer
profile.

```
import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.core.SdkBytes;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.textract.TextractClient;
import software.amazon.awssdk.services.textract.model.AnalyzeDocumentRequest;
import software.amazon.awssdk.services.textract.model.Document;
import software.amazon.awssdk.services.textract.model.FeatureType;
import software.amazon.awssdk.services.textract.model.S3Object;
import software.amazon.awssdk.services.textract.model.AnalyzeDocumentResponse;
import software.amazon.awssdk.services.textract.model.Block;
import software.amazon.awssdk.services.textract.model.TextractException;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
// snippet-end:[textract.java2._analyze_doc.import]

/**
 * Before running this Java V2 code example, set up your development environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class AnalyzeDocument {

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
        Region region = Region.US_EAST_1;
        TextractClient textractClient = TextractClient.builder()
                .region(region)
                .credentialsProvider(ProfileCredentialsProvider.create("profile-name"))
                .build();

        analyzeDoc(textractClient, bucketName, docName);
        textractClient.close();
    }

    // snippet-start:[textract.java2._analyze_doc.main]
    public static void analyzeDoc(TextractClient textractClient, String bucketName, String docName) {

        try {
            S3Object s3Object = S3Object.builder()
                    .bucket(bucketName)
                    .name(docName)
                    .build();

                // Create a Document object and reference the s3Object instance
                Document myDoc = Document.builder()
                    .s3Object(s3Object)
                    .build();

            List<FeatureType> featureTypes = new ArrayList<FeatureType>();
            featureTypes.add(FeatureType.FORMS);
            featureTypes.add(FeatureType.TABLES);

            AnalyzeDocumentRequest analyzeDocumentRequest = AnalyzeDocumentRequest.builder()
                    .featureTypes(featureTypes)
                    .document(myDoc)
                    .build();

            AnalyzeDocumentResponse analyzeDocument = textractClient.analyzeDocument(analyzeDocumentRequest);
            List<Block> docInfo = analyzeDocument.blocks();
            Iterator<Block> blockIterator = docInfo.iterator();

            while(blockIterator.hasNext()) {
                Block block = blockIterator.next();
                System.out.println("The block type is " +block.blockType().toString());
            }

        } catch (TextractException e) {

            System.err.println(e.getMessage());
            System.exit(1);
        }
    }
    // snippet-end:[textract.java2._analyze_doc.main]
}
```

AWS CLI
This AWS CLI command displays the JSON output for the
`analyze-document` CLI operation.

Replace the values of `Bucket` and `Name` with the names
of the Amazon S3 bucket and document that you used in step 2. Replace
`profile-name` with the name of a profile that can assume the role
and `region` with the region in which you want to run the code.

```
aws textract analyze-document \
    --document '{"S3Object":{"Bucket":"`bucket`","Name":"`document`"}}' \
    --feature-types '["TABLES","FORMS","SIGNATURES"]' \
    --profile `profile-name` \
    --region `region`
```

In order to use the Queries feature, include the
'`QUERIES`' value in the '`feature-types`' parameter and
then provide a `Queries` object to the '`queries-config`'
parameter. To use an adapter, include any `AdapterId`s and
`Version`s in a list of `Adapters` provided to the
`AdapterConfig` parameter.

```
aws textract analyze-document \
--document '{"S3Object":{"Bucket":"`bucket`","Name":"`document`"}}'\
 --feature-types '["QUERIES"]' \
--queries-config '{"Queries":[{"Text":"`Question`"}]}' \
--profile `profile-name` \
--region `region`
--adapters-config '{"Adapters": [{"AdapterId": "`AdapterId`", "Version": "`1`"]}'
```

Python
The following example code displays the document and boxes around detected
items.

In the function `main`, replace the values of `bucket` and
`document` with the names of the Amazon S3 bucket and document that you used
in step 2. Replace `profile-name` with the name of a profile that can
assume the role and `region` with the region in which you want to run the
code. To use an adapter, include any `AdapterId`s and
`Version`s in a list of `Adapters` provided to the
`AdapterConfig` parameter.

```
#Analyzes text in a document stored in an S3 bucket. Display polygon box around text and angled text
import boto3
import io
from PIL import Image, ImageDraw

def ShowBoundingBox(draw,box,width,height,boxColor):

    left = width * box['Left']
    top = height * box['Top']
    draw.rectangle([left,top, left + (width * box['Width']), top +(height * box['Height'])],outline=boxColor)

def ShowSelectedElement(draw,box,width,height,boxColor):

    left = width * box['Left']
    top = height * box['Top']
    draw.rectangle([left,top, left + (width * box['Width']), top +(height * box['Height'])],fill=boxColor)

# Displays information about a block returned by text detection and text analysis
def DisplayBlockInformation(block):
    print('Id: {}'.format(block['Id']))
    if 'Text' in block:
        print('    Detected: ' + block['Text'])
    print('    Type: ' + block['BlockType'])

    if 'Confidence' in block:
        print('    Confidence: ' + "{:.2f}".format(block['Confidence']) + "%")

    if block['BlockType'] == 'CELL':
        print("    Cell information")
        print("        Column:" + str(block['ColumnIndex']))
        print("        Row:" + str(block['RowIndex']))
        print("        Column Span:" + str(block['ColumnSpan']))
        print("        RowSpan:" + str(block['ColumnSpan']))

    if 'Relationships' in block:
        print('    Relationships: {}'.format(block['Relationships']))
    print('    Geometry: ')
    print('        Bounding Box: {}'.format(block['Geometry']['BoundingBox']))
    print('        Polygon: {}'.format(block['Geometry']['Polygon']))

    if block['BlockType'] == "KEY_VALUE_SET":
        print ('    Entity Type: ' + block['EntityTypes'][0])

    if block['BlockType'] == 'SELECTION_ELEMENT':
        print('    Selection element detected: ', end='')

        if block['SelectionStatus'] =='SELECTED':
            print('Selected')
        else:
            print('Not selected')

    if 'Page' in block:
        print('Page: ' + block['Page'])
    print()

def process_text_analysis(s3_connection, client, bucket, document):

    # Get the document from S3
    s3_object = s3_connection.Object(bucket,document)
    s3_response = s3_object.get()

    stream = io.BytesIO(s3_response['Body'].read())
    image=Image.open(stream)

    # Analyze the document
    image_binary = stream.getvalue()
    response = client.analyze_document(Document={'Bytes': image_binary},
        FeatureTypes=["TABLES", "FORMS", "SIGNATURES"])

    ### Uncomment to process using S3 object ###
    #response = client.analyze_document(
    #    Document={'S3Object': {'Bucket': bucket, 'Name': document}},
    #    FeatureTypes=["TABLES", "FORMS", "SIGNATURES"])

    ### Uncomment to analyze a local file ###
    # with open("pathToFile", 'rb') as img_file:
        ### To display image using PIL ###
    #    image = Image.open()
        ### Read bytes ###
    #    img_bytes = img_file.read()
    #    response = client.analyze_document(Document={'Bytes': img_bytes}, FeatureTypes=["TABLES", "FORMS", "SIGNATURES"])

    #Get the text blocks
    blocks=response['Blocks']
    width, height =image.size
    print ('Detected Document Text')

    # Create image showing bounding box/polygon the detected lines/text
    for block in blocks:
        DisplayBlockInformation(block)
        draw=ImageDraw.Draw(image)

        # Draw bounding boxes for different detected response objects
        if block['BlockType'] == "KEY_VALUE_SET":
            if block['EntityTypes'][0] == "KEY":
                ShowBoundingBox(draw, block['Geometry']['BoundingBox'],width,height,'red')
            else:
                ShowBoundingBox(draw, block['Geometry']['BoundingBox'],width,height,'green')
        if block['BlockType'] == 'TABLE':
            ShowBoundingBox(draw, block['Geometry']['BoundingBox'],width,height, 'blue')
        if block['BlockType'] == 'CELL':
            ShowBoundingBox(draw, block['Geometry']['BoundingBox'],width,height, 'yellow')
        if block['BlockType'] == 'SELECTION_ELEMENT':
            if block['SelectionStatus'] =='SELECTED':
                ShowSelectedElement(draw, block['Geometry']['BoundingBox'],width,height, 'blue')

    # Display the image
    image.show()
    return len(blocks)

def main():

    session = boto3.Session(profile_name='profile-name')
    s3_connection = session.resource('s3')
    client = session.client('textract', region_name='region')
    bucket = ""
    document = ""
    block_count=process_text_analysis(s3_connection, client, bucket, document)
    print("Blocks detected: " + str(block_count))

if __name__ == "__main__":
    main()

```

In order to use different features of the `AnalyzeDocument`
operation, you provide the proper feature type to the `features-type`
parameter. For example, to use the Queries feature, include the `QUERIES`
value in the `feature-types` parameter and then provide a
`Queries` object to the `queries-config` parameter. To query
your document, add the `query_document` function in the following code to
the preceding code example. Then, include the `question` variable and
line that invokes the `query_document` function to the preceding
`main` function.

```
def query_document(client, bucket, document, question):
    # Analyze the document
    response = client.analyze_document(Document={'S3Object': {'Bucket': bucket, 'Name': document}},
                                       FeatureTypes=["TABLES", "FORMS", "QUERIES"],
                                       QueriesConfig={'Queries':[
                                           {'Text':'{}'.format(question)}
                                       ]})

    for block in response['Blocks']:
        if block["BlockType"] == "QUERY":
            print("Query info:")
            print(block["Query"])
        if block["BlockType"] == "QUERY_RESULT":
            print("Query answer:")
            print(block["Text"])

question = "`query here`"
query_document(client, bucket, document, question)
```

Node.js
The following example code displays the document and boxes around detected
items.

In the following code, replace the values of `bucket` and
`photo` with the names of the Amazon S3 bucket and document that you used in
step 2. Replace the value of `region` with the region associated with
your account. Replace the value of `credentials` with the name of your
developer profile.

```
// Import required AWS SDK clients and commands for Node.js
import { AnalyzeDocumentCommand } from  "@aws-sdk/client-textract";
import  { TextractClient } from "@aws-sdk/client-textract";
import {fromIni} from '@aws-sdk/credential-providers';

// Set the AWS Region.
const REGION = "region"; //e.g. "us-east-1"
const profileName = "default";

// Create SNS service object.
const textractClient = new TextractClient({region: REGION,
  credentials: fromIni({profile: profileName,}),
});

const bucket = 'buckets'
const photo = 'photo'

// Set params
const params = {
    Document: {
      S3Object: {
        Bucket: bucket,
        Name: photo
      },
    },
    FeatureTypes: ['TABLES', 'FORMS', 'SIGNATURES'],
  }

const displayBlockInfo = async (response) => {
    try {
        response.Blocks.forEach(block => {
            console.log(`ID: ${block.Id}`)
            console.log(`Block Type: ${block.BlockType}`)
            if ("Text" in block && block.Text !== undefined){
                console.log(`Text: ${block.Text}`)
            }
            else{}
            if ("Confidence" in block && block.Confidence !== undefined){
                console.log(`Confidence: ${block.Confidence}`)
            }
            else{}
            if (block.BlockType == 'CELL'){
                console.log("Cell info:")
                console.log(`   Column Index - ${block.ColumnIndex}`)
                console.log(`   Row - ${block.RowIndex}`)
                console.log(`   Column Span - ${block.ColumnSpan}`)
                console.log(`   Row Span - ${block.RowSpan}`)
            }
            if ("Relationships" in block && block.Relationships !== undefined){
                console.log(block.Relationships)
                console.log("Geometry:")
                console.log(`   Bounding Box - ${JSON.stringify(block.Geometry.BoundingBox)}`)
                console.log(`   Polygon - ${JSON.stringify(block.Geometry.Polygon)}`)
            }
            console.log("-----")
        });
      } catch (err) {
        console.log("Error", err);
      }
}

const analyze_document_text = async () => {
    try {
        const analyzeDoc = new AnalyzeDocumentCommand(params);
        const response = await textractClient.send(analyzeDoc);
        //console.log(response)
        displayBlockInfo(response)
        return response; // For unit tests.
      } catch (err) {
        console.log("Error", err);
      }
}

analyze_document_text()
```

.NETThe following example displays detected text and their relationships in a list.

Replace the values of `bucket` and `document` with the names of the
Amazon S3 bucket and document image that you used in step 2.

```

using System;
using System.Linq;
using System.Reflection.Emit;
using Amazon.Runtime;
using Amazon.Textract;
using Amazon.Textract.Model;

namespace TextractAnalyzeExpense
{
    class Program
    {
        static async Task Main()
        {
            String document = "`document`";
            String bucket = "`bucket`";

            AmazonTextractClient textractClient = new AmazonTextractClient();

            AnalyzeExpenseRequest analyzeExpenseRequest = new AnalyzeExpenseRequest()
            {
                Document = new Document()
                {
                    S3Object = new S3Object()
                    {
                        Name = document,
                        Bucket = bucket
                    }
                }
            };

            try
            {
                var ExpenseAnalysis = await textractClient.AnalyzeExpenseAsync(analyzeExpenseRequest);
                Console.WriteLine("Line Items:");
                foreach (ExpenseDocument expenseDocument in ExpenseAnalysis.ExpenseDocuments)
                {
                    Console.WriteLine("Line Items:");
                   foreach(LineItemGroup linegroup in expenseDocument.LineItemGroups)
                   {
                    PrintLineItems.LineItemPrinter.LineItemParse(linegroup);
                   }

                   Console.WriteLine("Summary:\n");
                   foreach(ExpenseField summary in expenseDocument.SummaryFields)
                   {
                    if (summary.LabelDetection is not null)
                    {
                        Console.WriteLine(summary.LabelDetection.Text);
                    }
                   if (summary.ValueDetection is not null)
                    {
                        Console.WriteLine(summary.ValueDetection.Text);
                    }

                   }
                }


            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }

    }
}

namespace PrintLineItems
{
    class LineItemPrinter
    {
        public static void LineItemParse(LineItemGroup lineitemgroup)
        {
            foreach(LineItemFields lineitem in lineitemgroup.LineItems) {
                foreach(ExpenseField expense in lineitem.LineItemExpenseFields){
                   if (expense.LabelDetection is not null)
                   {
                    Console.WriteLine(expense.LabelDetection.Text);
                   }
                   if (expense.ValueDetection is not null)
                   {
                    Console.WriteLine(expense.ValueDetection.Text);
                   }

                }

            }

        }
    }
}

```

4.  Run the example. The Python and Java examples display the document image with the following
    colored bounding boxes:

        * Red – KEY Block objects
        * Green – VALUE Block objects
        * Blue – TABLE Block objects
        * Yellow – CELL Block objects

    Selection elements that are selected are filled with blue.

The AWS CLI example displays only the JSON output for the
`AnalyzeDocument` operation.
