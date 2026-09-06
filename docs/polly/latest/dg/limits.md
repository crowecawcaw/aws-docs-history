

# Quotas in Amazon Polly
<a name="limits"></a>

 Amazon Polly applies quotas to customer traffic by rejecting excessive requests. The default quota for the `SynthesizeSpeech` request with standard voices is 80 transactions per second (tps), in a single region, for a single AWS account. If limits did not increase, and if you generated 100 `SynthesizeSpeech` requests per second using a standard voice, 80 requests per second would succeed, and 20 requests per second would be throttled by Amazon Polly. These requests would return a response with HTTP status 400, and a response header indicating `ThrottlingException`. Amazon Polly also throttles traffic to all operations based on the request rate. 

**Speech synthesis limit examples**
+ **Synthesize the first 24 letters of the English alphabet one letter at a time**. If the synthesis of each letter took less than 50 milliseconds, with an operation limit of eight tps, synthesizing 24 letters would take at least three seconds. During that time, you could synthesize up to eight letters per second. Any further requests would be throttled. As the requests last a short time, they would be synthesized serially without overlap.
+ **Synthesize 16 paragraphs of text**. If each paragraph was synthesized and fully received on the client side in two seconds or less, with an operation limit of eight concurrent requests, it would take at least four seconds to synthesize all 16 articles. In the first second, you could start up to eight requests. During concurrent requests, any attempt to start a new synthesis would be throttled due to the concurrency limit. You could synthesize the remaining eight paragraphs after the first two seconds, after the first batch of requests finishes. 

Keep the following limits in mind when using Amazon Polly.

**Topics**
+ [Supported regions](#limits-regions)
+ [Quotas and throttle rates](#limits-throttle)
+ [Pronunciation lexicons](#limits-lexicons)
+ [SynthesizeSpeech API operations](#limits-synthesizespeech)
+ [SpeechSynthesisTask API operations](#limits-long)
+ [Speech Synthesis Markup Language (SSML)](#limits-ssml)

## Supported regions
<a name="limits-regions"></a>

 For a list of AWS Regions where Amazon Polly is available, see [Amazon Polly Endpoints and Quotas](https://docs.aws.amazon.com/general/latest/gr/pol.html) in the *Amazon Web Services General Reference*.
+ For Regions that support generative voices, see [Generative voices](https://docs.aws.amazon.com/polly/latest/dg/generative-voices.html).
+ For Regions that support long-form voices, see [Long-form voices](long-form-voices.md#long-form-regions). 
+ For Regions that support neural voices, see [Feature and region compatibility](neural-voices.md#ntts-regions) for neural TTS.

## Quotas and throttle rates
<a name="limits-throttle"></a>

 The following table defines throttle rates per Amazon Polly operation. You can use the AWS Management Console to request quota increases for the adjustable quotas when needed. 


| Operation | Limit | 
| --- | --- | 
| **Lexicon** |  | 
| `DeleteLexicon`<br />`PutLexicon`<br />`GetLexicon`<br />`ListLexicons` | Any 5 transactions per second (tps) from these operations combined.<br />Maximum allowed burst of 10 tps. | 
| **Speech** |   | 
| `DescribeVoices` | 80 tps with a burst limit of 100 tps | 
| `SynthesizeSpeech` | Generative voice: 8 tps<br />Long-form voice: 8 tps with a burst limit of 10 tps<br />Neural voice: 8 tps with a burst limit of 10 tps<br />Standard voice: 80 tps with a burst limit of 100 tps | 
| `StartSpeechSynthesisTask` | Generative voice: 1 tps<br />Long-form voice: 1 tps<br />Neural voice: 10 tps <br />Standard voice: 10 tps with a burst limit of 12 tps | 
| `StartSpeechSynthesisStream` | Generative voice: 8 tps | 
| `GetSynthesizeSpeechTask` and `ListSynthesizeSpeechTask` | Maximum allowed 10 tps combined | 

### Concurrent requests
<a name="concurrent-requests"></a>

 For **generative voice**, Amazon Polly supports up to 26 concurrent requests. For **long-form voice**, Amazon Polly supports up to 26 concurrent requests. For **neural voice**, Amazon Polly supports 8 tps with a burst limit of 10 tps, for up to 18 concurrent requests. Amazon Polly also supports limits for concurrent requests. For **standard voice**, Amazon Polly supports 80 tps for up to 80 concurrent requests. 

 For **StartSpeechSynthesisStream**, Amazon Polly supports up to 8 concurrent requests. 

### Best practices to mitigate throttling
<a name="best-practices-to-mitigate-throttling"></a>
+  **Retry throttles with backoff and jitter** so you can spread the load over a short period of time, and handle unexpected peaks in usage without compromising availability. AWS Code Sample Catalog is already configured to do this by default in many programming languages. Visit [feature retry behavior](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html) to see the details. 
+  **Use [Amazon Polly metrics](https://docs.aws.amazon.com/polly/latest/dg/cloud-watch.html#polly-metrics.html)**. Amazon Polly automatically publishes to CloudWatch to analyze your current usage and forecast usage growth. 

**Note**  
 Before requesting a quota increase (where applicable), calculate your tps needs following the guidelines on this page. Amazon Polly secures only the required computational resources according to customer demand in order to keep your costs low. 

## Pronunciation lexicons
<a name="limits-lexicons"></a>
+ You can store up to 100 lexicons per account.
+ Lexicon names can be an alphanumeric string up to 20 characters long.
+ Each lexicon can be up to 40,000 characters in size. (Note that the size of the lexicon affects the latency of the SynthesizeSpeech operation.)
+ You can specify up to 100 characters for each <phoneme> or <alias> replacement in a lexicon.

For information about using lexicons, see [Managing lexicons](managing-lexicons.md). 

## SynthesizeSpeech API operations
<a name="limits-synthesizespeech"></a>

 When estimating the usage of `SynthesizeSpeech`, keep in mind that the audio produced by Amazon Polly, especially for interactive applications, usually takes at least several seconds to be played. This reduces the rate of requests to `SynthesizeSpeech`, even for a large number of concurrent consumers. Additionally, Amazon Polly throttles `SynthesizeSpeech` requests by the number of concurrent requests that it synthesizes. There is no separate setting for concurrent requests. The concurrent requests limit has always the same value as the number of tps allowed and scales with it. 

 **Short story example application**. You can use Amazon Polly to build an application that plays a series of short stories. With this kind of app, the first story would start playing, and then the next, and so on, until a user quit the application. Each story would take around 0.5 seconds to synthesize and 10 seconds to play. In this scenario, you could expect one call to `SynthesizeSpeech` for every 10 seconds that the customer spent using the application. This would translate to one call per second for every 10 customers who were concurrently using the application. If you had 1000 customers concurrently using the application, you could expect an average call rate to `SynthesizeSpeech` of only 100 transactions per second. 

Note the following limits related to using the `SynthesizeSpeech` API operation:
+ The size of the input text can be up to 3000 billed characters (6000 total characters). SSML tags are not counted as billed characters.
+ You can specify up to five lexicons to apply to the input text.
+ The output audio stream (synthesis) is limited to 10 minutes. After this is reached, any remaining speech is cut off.

For more information, see [SynthesizeSpeech](https://docs.aws.amazon.com/polly/latest/APIReference/API_SynthesizeSpeech.html). 

**Note**  
Some limitations of the `SynthesizeSpeech` API operation can be bypassed using the `StartSythensizeSpeechTask` API operation. For more information, see [Long audio files](asynchronous.md). 

## SpeechSynthesisTask API operations
<a name="limits-long"></a>

Note the following limit relating to using the `StartSpeechSynthesisTask`, `GetSpeechSynthesisTask`, and `ListSpeechSynthesisTasks` API operations:
+ The size of the input text can be up to 100,000 billed characters (200,000 total characters). SSML tags are not counted as billed characters.
+ You can specify up to five lexicons to apply to the input text.

## Speech Synthesis Markup Language (SSML)
<a name="limits-ssml"></a>

Note the following limits related to using SSML:
+ The `<audio>`, `<lexicon>`, `<lookup>`, and `<voice>` tags are not supported.
+ `<break>` elements can specify a maximum duration of 10 seconds each.
+ The `<prosody>` tag doesn't support values for the rate attribute lower than -80%.

 For more information, see [Generating speech from SSML documents](ssml.md).