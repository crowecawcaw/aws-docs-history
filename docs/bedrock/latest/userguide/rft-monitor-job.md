# Monitor your RFT training job

During reinforcement fine-tuning, you can monitor training progress in real-time using visual graphs and metrics in the Amazon Bedrock
console. The training metrics dashboard shows key performance indicators including reward scores, loss curves, and accuracy
improvements over time. These metrics help you understand whether the model converges properly and if the reward function
effectively guides the learning process.

###### Topics

- [Real-time training metrics](#rft-real-time-metrics "#rft-real-time-metrics")
- [Job status tracking](#rft-job-status "#rft-job-status")

## Real-time training metrics

Amazon Bedrock provides real-time monitoring during RFT training with visual graphs displaying training and validation metrics.

### Core training metrics

- **Training loss** - Measures how well the model is learning from the training data
- **Training reward statistics** - Shows reward scores assigned by your reward functions
- **Reward margin** - Measures the difference between good and bad response rewards
- **Accuracy on training and validation sets** - Shows model performance on both the training and held-out data

### Training progress visualization

The console displays interactive graphs that update in real-time as your RFT job progresses. These visualizations can help you:

- Track convergence toward optimal performance
- Identify potential training issues early
- Determine optimal stopping points
- Compare performance across different epochs

## Job status tracking

Monitor your RFT job status through the Amazon Bedrock console.

**Job phases:**

1. Validation
2. Training

**Completion indicators:**

- Job status changes to **Completed** when training completes successfully
- Custom model ARN becomes available for deployment
- Training metrics reach convergence thresholds
