# RAISP02-BP07 Incorporate explainability mechanisms into the

core AI system

Adding explainability to your AI system assists to address
explainability release criteria by verifying stakeholders can
understand and trust how decisions are made for your specific use
case. Include confidence scores with predictions to show how certain
the model is about its outputs, and for generative AI systems, use
techniques such as content attribution, and token probabilities to
explain what influenced the generated content. When explanations are
critical, use interpretable models like decision trees that are
simple to understand and when more complex models are required add
explanation tools (like LIME or SHAP) afterward to interpret their
decisions.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

1. Build confidence scoring into your system's output pipeline so
   users can see how certain your model is about each prediction.
   Test different confidence calculation methods to find ones
   that actually correlate with accuracy, since some approaches
   give misleading confidence scores that don't assist users to
   make better decisions.
2. Choose interpretable model architectures, such as decision
   trees or linear models when stakeholders need to understand
   exactly how decisions are made. Compare the performance
   trade-offs between interpretable and complex models for your
   specific use case to see if the explanation benefits justify
   accuracy costs.
3. Add explanation tools like LIME or SHAP to complex models that
   you can't make interpretable but still need to explain. Test
   these tools with your actual users to make sure the
   explanations are helpful rather than confusing, since some
   explanation methods work better for different types of models
   and use cases.
4. For generative AI systems, build in techniques like
   chain-of-thought prompting that show the reasoning process,
   content attribution that traces outputs back to source
   material, and token probability displays that reveal
   uncertainty. Test these explanation methods to see which ones
   assist users to understand and trust the generated content.
   For example, each response from an Amazon Bedrock agent is
   accompanied by a trace that details the steps being
   orchestrated by the agent. The trace assists to follow the
   agent's reasoning process that leads it to the response it
   gives at that point in the conversation.
5. Build automatic source attribution into your Retrieval
   Augmented Generation (RAG) system by linking retrieved
   information directly to its origin document with specific
   citations, page numbers, and document identifiers. Display
   these citations alongside generated content so users can
   independently verify where information came from.

Create explanation validation processes that check whether your
explainability mechanisms are effective in assisting users make
better decisions about trusting or acting on your system's
outputs. Regularly test explanations with real users to catch
when explanation methods become misleading or stop being useful
as your system evolves.

## Resources

**Related documents:**

- [ISO/IEC
  42001:2023 A.8.2 System documentation and information for
  users](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001")
