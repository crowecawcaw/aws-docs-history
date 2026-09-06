

# SageMaker AI Crowd HTML Elements
<a name="general-topiclist"></a>

The following is a list of Crowd HTML Elements that make building a custom template easier and provide a familiar UI for workers. These elements are supported in Ground Truth, Augmented AI, and Mechanical Turk.

## Crowd HTML Elements V2
<a name="elements-v2"></a>

Crowd HTML V2 Elements introduce enhanced labeling capabilities designed to support workers, with new features tailored for GenAI model training use cases. These V2 elements are compatible with the Crowd HTML Elements crowd-form, short-instructions, crowd-button, crowd-tabs, and crowd-tab. If you use other elements with V2 elements, the annotation application won't work properly.

### crowd-text-ranking
<a name="sms-ui-template-crowd-text-ranking"></a>

A widget for workers to slide and rank various text inputs based on dimensions that you specify.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements_2/pen/ZYGqBPQ).

```
<script src="https://assets.crowd.aws/crowd-html-elements-v2.js"></script>

<crowd-form>
  <crowd-text-ranking
    name="textRanking"
    ordinal-ranking-dimensions='[{"name":"Clarity","allowTie":true},{"name":"Inclusivity","allowTie":false}]'
    text="Explain why you can see yourself in a mirror at a level that a 16 year old can understand."
    responses='["When light is emitted from light source like a light bulb, some of it travels toward your body, where it may be reflected toward the mirror with some probability or it may be absorbed. If it were reflected off your body, then some of it could travel toward the mirror, where it could be reflected again. If it is the case where light strikes the mirror, the light is then again redirected as a reflection. If that light is pointed in the direction of your eyes, then the light will enter your eyes. Then, your brain processes the electrical signal made by your eyes and sees it as an image.","You can see yourself because of a series of light reflections. Light travels from the light source, hits and reflects off of your body and travels toward the mirror. Then, it reflects off of the mirror and travels to your eyes, where your brain registers it as a picture of yourself.","Light travels in various directions from a light source like a light bulb. Some of the light reflects off of your body with some probability, after which some of it travels to the mirror. Upon striking the mirror, the some of the light again reflects off the mirror and travels toward your eyes, wherein your eyes detect the light after absorbing it. After this process, your brain processes the signal as an image of yourself.","The phenomenon of self-visual perception via a mirror at an ontological plane derives from the intricate interplay of photons within the electromagnetic spectrum, quantum mechanical principles, and the neurocognitive processes underpinning self-recognition. In essence, the mirror serves as an interface wherein incident photons, emitted from an external object, interact with the reflective surface at a specific angle of incidence governed by the laws of geometric optics. This interaction culminates in the process of specular reflection, leading to the formation of a virtual image."]'
  >
    <short-instructions>
      <h1>Hello these are my instructions 1</h1>
      <p>Hello these are my instructions 2</p>
      <p>Hello these are my instructions 3</p>
    </short-instructions>
  </crowd-text-ranking>
</crowd-form>
```

#### Attributes
<a name="crowd-text-ranking-attributes"></a>

The following are attributes supported by this element.

##### text
<a name="crowd-text-ranking-attributes-text"></a>

The text or S3 reference to the text to reference when ranking the responses.

##### ordinal-ranking-dimensions
<a name="crowd-text-ranking-attributes-ordinal-ranking"></a>

A required array of the `ordinal-ranking-dimensions` object, which specify the dimension on which to rank the responses. This dimension contains a **name** and a property named **allowTie**, which determines whether a worker can give responses the same ranking.

##### responses
<a name="crowd-text-ranking-attributes-responses"></a>

A required array of the `ordinal-ranking-dimensions` object, which specify the dimension on which to rank the responses. This dimension contains a **name** and a property named **allowTie**, which determines whether a worker can give responses the same ranking.

##### name
<a name="crowd-text-ranking-attributes-name"></a>

A required string field that identifies the answer submitted that the worker submits. It matches a key in the output data contract of the worker submission.

For more information, see the following.
+ [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md)
+ [Crowd HTML Elements Reference](sms-ui-template-reference.md)

### crowd-question-answer-generation
<a name="sms-ui-template-crowd-question-answer-generation"></a>

A widget for workers to highlight sections of text and assign question and answer pairs based on your instructions

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements_2/pen/zxGmobo).

```
<script src="https://assets.crowd.aws/crowd-html-elements-v2.js"></script>

<crowd-form>
  <crowd-question-answer-generation
    name="questionAnswerGeneration"
    text='The Amazon rainforest (Portuguese: Floresta Amazônica or Amazônia; Spanish: Selva Amazónica, Amazonía or usually Amazonia; French: Forêt amazonienne; Dutch: Amazoneregenwoud), also known in English as Amazonia or the Amazon Jungle, is a moist broadleaf forest that covers most of the Amazon basin of South America. This basin encompasses 7,000,000 square kilometres (2,700,000 sq mi), of which 5,500,000 square kilometres (2,100,000 sq mi) are covered by the rainforest. This region includes territory belonging to nine nations. The majority of the forest is contained within Brazil, with 60% of the rainforest, followed by Peru with 13%, Colombia with 10%, and with minor amounts in Venezuela, Ecuador, Bolivia, Guyana, Suriname and French Guiana. States or departments in four nations contain "Amazonas" in their names. The Amazon represents over half of the planet's remaining rainforests, and comprises the largest and most biodiverse tract of tropical rainforest 
    in the world, with an estimated 390 billion individual trees divided into 16,000 species. For a long time, it was thought that the 
    Amazon rainforest was only ever sparsely populated, as it was impossible to sustain a large population through agriculture given the poor soil. 
    Archeologist Betty Meggers was a prominent proponent of this idea, as described in her book Amazonia: Man and Culture in a Counterfeit Paradise. 
    She claimed that a population density of 0.2 inhabitants per square kilometre (0.52/sq mi) is the maximum that can be sustained in the rainforest 
    through hunting, with agriculture needed to host a larger population. However, recent anthropological findings have suggested that the region was 
    actually densely populated. Some 5 million people may have lived in the Amazon region in AD 1500, divided between dense coastal settlements, such as that at
    Marajó, and inland dwellers. By 1900 the population had fallen to 1 million and by the early 1980s it was less than 200,000.'
    min-questions="1"
    max-questions="10"
    question-min-words="1"
    question-max-words="100"
    answer-min-words="1"
    answer-max-words="100"
    question-tags='[
      "tag1",
      "tag2",
      "tag3"
    ]'
    allow-custom-question-tags="true"
  >
    <short-instructions>
      <p>User instructions will be displayed here.</p>
    </short-instructions>
  </crowd-question-answer-generation>
</crowd-form>
```

#### Attributes
<a name="crowd-question-answer-generation-attributes"></a>

The following are attributes supported by this element.

##### text
<a name="crowd-question-answer-generation-attributes-text"></a>

The text or S3 reference to the text to reference when ranking the responses.

##### min-questions
<a name="crowd-question-answer-generation-attributes-min-questions"></a>

Optional integer that specifies the minimum amount of questions that a worker would have to create during the task. If not provided, you will be asked to write at least one question and answer pair.

##### max-questions
<a name="crowd-question-answer-generation-attributes-max-questions"></a>

Optional integer that specifies the maximum amount of questions a worker can create during the task.

##### question-min-words
<a name="crowd-question-answer-generation-attributes-question-min-words"></a>

Optional integer that specifies the minimum amount of words allowed in an question. If not provided, you will be asked to provide at least one word in the question.

##### question-max-words
<a name="crowd-question-answer-generation-attributes-question-max-words"></a>

Optional integer that specifies the maximum amount of words allowed in an question.

##### answer-min-words
<a name="crowd-question-answer-generation-attributes-answer-min-words"></a>

Optional integer that specifies the minimum amount of words allowed in an answer. If not provided, you will be asked to write at least one word in the answer.

##### answer-max-words
<a name="crowd-question-answer-generation-attributes-answer-max-words"></a>

Optional integer that specifies the maximum amount of words allowed in an answer.

##### question-tags
<a name="crowd-question-answer-generation-attributes-question-tags"></a>

A required array of strings that specifies the possible tags a worker can assign to a question-answer pair. If this array is empty, then question-tags field isn't visible.

##### allow-custom-question-tags
<a name="crowd-question-answer-generation-attributes-allow-custom-question-tags"></a>

Required Boolean field that indicates whether a worker can specify a custom question tag.

##### name
<a name="crowd-question-answer-generation-attributes-name"></a>

A required string field that identifies the answer submitted that the worker submits. It matches a key in the output data contract of the worker submission.

For more information, see the following.
+ [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md)
+ [Crowd HTML Elements Reference](sms-ui-template-reference.md)