# RAIER03-BP01 For each failed release criterion, re-assess the

implementation strategy

Re-evaluate the original implementation strategy assigned to each
release criteria. Either improve the execution of the implementation
strategy or design a new approach based of baking techniques (for
example, additional fine-tuning, new training approaches or
component choices), blocking techniques (for example, adding
additional guardrails or filtering strategies) or a user steering
strategy (for example, publishing user guidance).

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

1. Analyze why your current implementation strategy failed to
   meet the release criteria by looking at the specific test
   results, edge cases where it did not work, and patterns in the
   failures. Understanding the root cause assists you to decide
   whether you need to alter your existing approach or add
   completely new implementation techniques.
2. Add new or enhance existing baking solutions by building
   additional implementations directly into your model through
   extra training rounds, refined fine-tuning approaches, or
   different model component choices. These approaches modify the
   model's core behavior rather than trying to catch problems
   afterward, which can be more effective for persistent issues
   that keep appearing.
3. Implement new or strengthen existing filtering techniques by
   adding more sophisticated content filters, better output
   classifiers, or additional input validation rules that catch
   harmful content before it reaches users. You might need to
   layer multiple blocking approaches or make your existing
   filters more sensitive to handle the specific failure cases
   you discovered.
4. Create new or improve existing guiding approaches that assist
   users to avoid harmful interactions through redesigned
   interfaces, clearer guidance, better warnings about
   limitations, or more comprehensive educational content about
   appropriate use cases. This works particularly well for
   criteria that depend on how people choose to interact with
   your system.
5. Test your new or modified implementation approaches against
   the same evaluation criteria that your original strategy
   failed on. Document what you added or changed and what you can
   learn from this experience for future implementations.

## Resources

**Related documents:**

- [Build
  responsible AI applications with Amazon Bedrock
  Guardrails](https://aws.amazon.com/blogs/machine-learning/build-responsible-ai-applications-with-amazon-bedrock-guardrails/ "https://aws.amazon.com/blogs/machine-learning/build-responsible-ai-applications-with-amazon-bedrock-guardrails/")
