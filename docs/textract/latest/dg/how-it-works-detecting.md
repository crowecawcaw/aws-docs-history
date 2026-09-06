

# Detecting Text
<a name="how-it-works-detecting"></a>

Amazon Textract provides synchronous and asynchronous operations that return only the text detected in a document. For both sets of operations, the following information is returned in multiple [Block](https://docs.aws.amazon.com/textract/latest/APIReference/API_Block.html) objects:
+ The lines and words of detected text
+ The relationships between the lines and words of detected text
+ The page that the detected text appears on
+ The location of the lines and words of text on the document page

For more information, see [Lines and Words of Text](how-it-works-lines-words.md).

To detect text synchronously, use the [DetectDocumentText](https://docs.aws.amazon.com/textract/latest/APIReference/API_DetectDocumentText.html) API operation, and pass a document file as input. The entire set of results is returned by the operation. For more information and an example, see [Processing Documents Synchronously](sync.md). 

**Note**  
The Amazon Rekognition API operation `DetectText` is different from `DetectDocumentText`. You use `DetectText` to detect text in live scenes, such as posters or road signs.

To detect text asynchronously, use [StartDocumentTextDetection](https://docs.aws.amazon.com/textract/latest/APIReference/API_StartDocumentTextDetection.html) to start processing an input document file. To get the results, call [GetDocumentTextDetection](https://docs.aws.amazon.com/textract/latest/APIReference/API_GetDocumentTextDetection.html). The results are returned in one or more responses from `GetDocumentTextDetection`. For more information and an example, see [Processing Documents Asynchronously](async.md). 