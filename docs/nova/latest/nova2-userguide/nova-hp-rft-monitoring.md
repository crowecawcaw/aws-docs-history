# Monitoring RFT training

Monitor key metrics during training to ensure effective learning and identify potential
issues early.

###### Topics

- [Key metrics to track](#nova-hp-rft-monitoring-metrics "#nova-hp-rft-monitoring-metrics")
- [Evaluation after RFT](#nova-hp-rft-monitoring-evaluation "#nova-hp-rft-monitoring-evaluation")
- [Using fine-tuned models](#nova-hp-rft-monitoring-checkpoints "#nova-hp-rft-monitoring-checkpoints")
- [Limitations and best
  practices](#nova-hp-rft-monitoring-limitations "#nova-hp-rft-monitoring-limitations")
- [Troubleshooting](#nova-hp-rft-monitoring-troubleshooting "#nova-hp-rft-monitoring-troubleshooting")

## Key metrics to track

Monitor the following metrics using MlFlow during training:

**Reward metrics:**

- **Average reward score**: Overall quality of model
  responses (should increase over time)
- **Reward distribution**: Percentage of responses
  receiving high, medium, and low rewards
- **Training vs. validation rewards**: Compare to
  detect overfitting

**Training metrics:**

- **Policy updates**: Number of successful weight
  updates
- **Rollout completion rate**: Percentage of samples
  successfully evaluated

**Concerning patterns:**

- Rewards plateauing (indicates poor learning)
- Validation rewards dropping while training rewards increase (overfitting)
- Reward variance increasing significantly over time (instability)
- High percentage of reward function errors (implementation issues)

**When to stop training:**

- Target performance metrics are achieved
- Rewards plateau and no longer improve
- Validation performance degrades (overfitting detected)
- Maximum training budget is reached

## Evaluation after RFT

After training completes, evaluate your fine-tuned model to assess performance
improvements:

- **Run RFT evaluation job**: Use the checkpoint from
  your RFT training as the model
- **Compare to baseline**: Evaluate both base model and
  fine-tuned model on the same test set
- **Analyze metrics**: Review task-specific metrics
  (accuracy, reward scores, etc.)
- **Conduct qualitative review**: Manually inspect
  sample outputs for quality

For detailed evaluation procedures, see the Evaluation section.

## Using fine-tuned models

**Accessing checkpoints:**

After training completes, locate your checkpoint:

1. Navigate to your `output_path` in S3
2. Download and extract `output.tar.gz`
3. Open `manifest.json`
4. Copy the `checkpoint_s3_bucket` value

**Deploying for inference:**

Use the checkpoint S3 path for inference or further training:

```
run:
    model_type: amazon.nova-2-lite-v1:0:256k
    model_name_or_path: "s3://customer-escrow-<account-number>-smtj-<unique-identifier>/<job-name>"
```

For deployment and inference instructions, refer to the Inference section.

## Limitations and best

practices

**Current limitations:**

**Beta restrictions:**

- Need to create a new RIG group for RFT. This limitation will be resolved by
  GA.
- Non-RIG instance groups not allowed: Ensure your HyperPod cluster contains only
  Restricted Instance Groups (RIGs) - no regular instance groups. This limitation will
  be resolved by GA.
- Instance type requirements: Only P5 instances supported (minimum 8x P5.48xlarge).
  Coming Soon: Support for smaller instance types (ETA: mid-January 2025).

**Functional limitations:**

- 15-minute Lambda timeout: Reward functions must complete within 15 minutes
- Single-turn only: Multi-turn conversations not supported
- Validation datasets: Not supported during training. Use separate evaluation jobs
  to assess training progress.

**Training considerations:**

- Low reward scenarios: May struggle when less than 5% of examples receive positive
  rewards - consider SFT first
- Data requirements: Needs sufficient diversity to learn effectively
- Computational cost: More expensive than supervised fine-tuning

**Nova Forge removes some of these limitations:**

- Supports multi-turn conversations
- Allows reward functions exceeding 15-minute timeouts
- Provides advanced algorithms and tuning options
- Designed for complex enterprise use cases, specifically tuned to build frontier
  models

**Best practices:**

**Start small and scale:**

- Begin with minimal datasets (100-200 examples) and few training epochs
- Validate your approach before scaling up
- Gradually increase dataset size and training steps based on results

**Baseline with SFT first:**

- If reward scores are consistently low (e.g., always 0), perform SFT before
  RFT
- RFT requires reasonable baseline performance to improve effectively

**Design efficient reward functions:**

- Execute in seconds, not minutes
- Minimize external API calls
- Use efficient algorithms and data structures
- Implement proper error handling
- Test thoroughly before training
- Leverage Lambda's parallel scaling capabilities

**Monitor training actively:**

- Track average reward scores over time
- Watch reward distribution across samples
- Compare training vs. validation rewards
- Look for concerning patterns (plateaus, overfitting, instability)

**Iterate based on results:**

- If rewards don't improve after several iterations, adjust reward function
  design
- Increase dataset diversity to provide clearer learning signals
- Consider switching to SFT if rewards remain near zero
- Experiment with different hyperparameters (learning rate, batch size)

**Optimize data quality:**

- Ensure diverse, representative examples
- Include edge cases and difficult samples
- Verify reward function correctly scores all example types
- Remove or fix samples that confuse the reward function

## Troubleshooting

**Reward function errors:**

Symptoms: High error rate in reward function calls during training

| Issue                    | Symptoms                           | Resolution                                                                    |
| ------------------------ | ---------------------------------- | ----------------------------------------------------------------------------- |
| Lambda timeout           | Frequent timeouts after 15 minutes | Optimize function performance; consider Nova Forge for complex<br>evaluations |
| Insufficient concurrency | Lambda throttling errors           | Increase lambda_concurrency_limit or request quota increase                   |
| Invalid return format    | Training fails with format errors  | Verify return structure matches required interface format                     |
| Unhandled exceptions     | Intermittent errors                | Add comprehensive error handling and logging                                  |
| External API failures    | Inconsistent scoring               | Implement retry logic and fallback strategies                                 |

**Poor training performance:**

Symptoms: Rewards not improving or plateauing at low values

Resolutions:

- **Verify reward function correctness**: Test with
  known good/bad examples
- **Check baseline performance**: Evaluate base model;
  if near-zero accuracy, do SFT first
- **Increase data diversity**: Add more varied examples
  covering different scenarios
- **Adjust hyperparameters**: Try different learning
  rates or batch sizes
- **Review reward signal quality**: Ensure rewards
  differentiate between good and bad responses

**Overfitting:**

Symptoms: Training rewards increase while validation rewards decrease

Resolutions:

- **Reduce training steps**: Stop training
  earlier
- **Increase dataset size**: Add more training
  examples
- **Add regularization**: Adjust
  `weight_decay` or `entropy_coeff`
- **Increase data diversity**: Ensure training set
  represents full distribution
