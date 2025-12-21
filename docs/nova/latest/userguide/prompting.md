# Prompting best practices for Amazon Nova understanding models

###### Note

This documentation is for Amazon Nova Version 1. For the Amazon Nova 2 prompt engineering guide, visit [Prompt engineering guide](../nova2-userguide/prompt-engineering-guide.md "../nova2-userguide/prompt-engineering-guide.md").

_Prompt engineering_ refers to the practice of optimizing textual input
to a large language model (LLM) to improve output and receive the responses you want. Prompting
helps an LLM perform a wide variety of tasks, including classification, question answering, code
generation, creative writing, and more. The quality of prompts that you provide to a LLM can
impact the quality of the model's responses. This section provides you the necessary information
to get started with prompt engineering. It also covers tools to help you find the best possible
prompt format for your use case when using a LLM on Amazon Bedrock.

The effectiveness of prompts is contingent upon the quality of the information provided and
the craftsmanship of the prompt itself. Prompts may encompass instructions, questions,
contextual details, inputs, and examples to effectively guide the model and enhance the quality
of the results. This document outlines strategies and tactics for optimizing the performance of
Amazon Nova Family of Models. The methods presented herein may be employed in various combinations
to amplify their effectiveness. We encourage users to engage in experimentation to identify the
approaches most suitable for their specific needs.

Before you start prompt engineering, we recommend that you have the following elements in
place, so you can iteratively develop the most optimal prompt for your use case:

1. **Define your use case:** Define your use case you want to
   achieve on 4 dimensions
   1. **What is the Task** - Define the task you want to
      accomplish from the model
   2. **Whats the Role** - Define the role that the model should assume to accomplish that task
   3. **Whats the Response Style** - Define the response
      structure or style that should be followed based on the consumer of the output.
   4. **What set of Instructions to be followed:** Define the
      set of instructions that the model should follow to respond as per the success
      criteria

2. **Success Criteria:** Clearly define the success criteria
   or evaluation criteria. This can be in the form of a list of bullet points or as specific as
   some evaluation metrics (Eg: Length checks, BLEU Score, Rouge, Format, Factuality,
   Faithfulness).
3. **Draft Prompt:** Finally, a draft prompt is necessary to
   initiate the iterative process of prompt engineering.
   The Amazon Nova model family consists of two broad model categories, understanding models
   (Amazon Nova Micro, Lite, Pro, and Premier) and content generation models (Amazon Nova Canvas and Reel). The
   following guidance addresses the text understanding model and the vision understanding models.
   For guidance on image generation prompting, see [Amazon Nova Canvas prompting best
   practices](prompting-image-generation.md "prompting-image-generation.md") and for guidance on video generation prompting,
   see [Amazon Nova Reel prompting best practices](prompting-video-generation.md "prompting-video-generation.md").

###### Topics

- [Text understanding prompting best
  practices](prompting-text-understanding.md "prompting-text-understanding.md")
- [Vision understanding prompting best
  practices](prompting-video-understanding.md "prompting-video-understanding.md")
- [General prompting tips](prompting-general-tips.md "prompting-general-tips.md")
