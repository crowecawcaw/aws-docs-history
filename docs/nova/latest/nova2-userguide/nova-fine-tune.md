

# Supervised fine-tuning (SFT)
<a name="nova-fine-tune"></a>

Supervised fine-tuning (SFT) trains a model using labeled input-output pairs. The model learns from demonstration examples consisting of prompts and responses, refining its capabilities to align with specific tasks, instructions, or desired behaviors.

**When to use SFT**  
Use SFT when you can specify what the right behavior looks like through labeled examples. SFT is ideal when:
+ You have high-quality input-output pairs that demonstrate the desired behavior
+ You want to teach the model a specific response format, tone, or style
+ Your task requires following domain-specific instructions or workflows
+ You need to adapt the model for multimodal tasks (text, image, video, or tool calling)

**Supported models**  
SFT is available for the following Amazon Nova models:
+ Nova 1.0 (Micro, Lite, Pro)
+ Nova 2.0 (Lite)

**When to use Nova 1.0 versus Nova 2.0**  
The Amazon Nova family of models offers multiple price-performance operating points to optimize between accuracy, speed, and cost.

Choose Nova 2.0 when you need the following:
+ Enhanced reasoning abilities with explicit reasoning mode support
+ Broader multilingual performance across additional languages
+ Improved performance on complex tasks including coding and tool use
+ Extended context handling with better accuracy and stability at longer context lengths

**Note**  
The larger model is not always better. Consider the cost-performance tradeoff and your specific business requirements when selecting between Nova 1.0 and Nova 2.0 models.