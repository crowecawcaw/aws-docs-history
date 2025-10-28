# Training a reinforcement learning model in AWS DeepRacer Student

This walkthrough demonstrates how to train your first model in AWS DeepRacer Student. It also provides you with
some useful tips to help you make the most of your experience and fast-track your learning.

## Step 1: Train a reinforcement learning model using AWS DeepRacer Student

Begin your journey in AWS DeepRacer Student by learning where to find the **Create
model** button and start training your first model. Keep in mind that creating and
training a model is an iterative process. Experiment with different algorithms and reward
functions to achieve your best results.

###### To train a reinforcement learning model

1. In the AWS DeepRacer Student **Home** page, choose **Create a model**. Alternatively,
   navigate to **Your Models** in the left navigation pane. In the **Models**
   page, in **Your models**, choose **Create model**.
2. In the **Overview** page, read about how to train a reinforcement model. Each step in the process is explained on this page. When you've finished reading, choose **Next**.

## Step 2: Name your model

Name your model. It's good practice to give your models unique names to quickly locate
individual models when you want to improve and clone them. For example, you may want to name
your models using a naming convention such as:
`yourinitials-date-version`.

###### To name your model

1. On the **Name your
   model** page, enter a name in the **Model name** field.

###### Note

When you begin training a model, the model's name becomes fixed and is no longer changeable. 2. Choose **Next**.

## Step 3: Choose your track

Choose your simulation track. The track serves as the environment and provides data to
your car. If you choose a very complex track, your car requires a longer total training time
and the reward function you use is more complex.

###### To choose your track (environment)

1. On the **Choose track** page, choose a track to serve as a training environment for
   your car.
2. Choose **Next**.

## Step 4: Choose an algorithm

The AWS DeepRacer Student has two training algorithms from which to choose. Different
algorithms maximize rewards in different ways. To make the most of your AWS DeepRacer Student
experience, experiment with both algorithms. For more information about algorithms, see [AWS DeepRacer Training Algorithms](../developerguide/deepracer-how-it-works-reinforcement-learning-algorithm.md "../developerguide/deepracer-how-it-works-reinforcement-learning-algorithm.md").

###### To choose a training algorithm

1. On the **Choose algorithm type** page, select an algorithm type. Two algorithm types
   are available:
   - **Proximal Policy Optimization (PPO)**. This stable but data hungry algorithm performs consistently
     between training iterations.
   - **Soft Actor Critic (SAC)**. This unstable but data efficient algorithm can perform inconsistently between training iterations.

2. Choose **Next**.

## Step 5: Customize your reward function

The reward function is at the core of reinforcement learning. Use it to incentivize your
car (agent) to take specific actions as it explores the track (environment). Just as you would
encourage and discourage certain behaviors in a pet, you can use this tool to encourage your
car to finish a lap as fast as possible and discourage it from driving off of the track and
zig-zagging.

When training your first model, you may want to use a default sample reward function. When
you're ready to experiment and optimize your model, you can customize the reward function by editing the code in the code editor.
For more information about customizing the reward function, see [Customizing a reward function](reward-function.md "reward-function.md").

###### To customize your reward function

1. On the **Customize reward function** page, choose a sample reward function. There are 3 sample reward functions available that
   you can customize:
   - **Follow the centerline**. Rewards your car when it autonomously drives as close as it can to the centerline of the track.
   - **Stay within borders**. Rewards your car when it autonomously drives with all four wheels staying within the track borders.
   - **Prevent zig-zag**. Rewards your car for staying near the centerline. Penalizes your car if it uses high steering angles or goes off track.

###### Note

If you don't want to customize the reward function, choose **Next**. 2. (Optional) Modify the reward function code.

    * Select a sample reward function and choose **Walk me through this code**.
    * For each section of the code, you can view more information by selecting the
     **+** to reveal a pop-up textbox with explantory text. Progress through the code walkthrough by choosing **Next** in each pop-up. To exit out
     of a pop-up textbox, choose the **X** in the corner. To exit the walkthrough, choose **Finish**.


    ###### Note

    You can choose not to edit the sample reward function code by selecting
     **Go with default code**.
    * Optionally, edit the sample reward function code by selecting a sample reward function and choosing **Edit sample code**. Edit the code and select **Validate**
     to check your code. If your code can't be validated or
     you would like to reset the code to its original state, choose **Reset**.

3. Choose **Next**.

## Step 6: Choose duration and submit your model to the leaderboard

The duration of your model's training impacts its performance. When experimenting in the early phase of training, you should start with a small value for this parameter
and then progressively train for longer periods of time.

In this step of training your model, your trained model is submitted to a leaderboard. You
can opt out by deselecting the checkbox.

###### To choose duration and submit a model to the leaderboard

1. On the **Choose duration** page, select a time in **Choose duration of model training**.
2. In the **Model description** field, enter a useful description for your model that will
   help you to remember the selections you made.

###### Tip

It's good practice to add information about your model such as current selections and modifications for the reward function
and algorithm as well as your hypothesis about how the model will
perform. 3. Select the checkbox to automatically have your model submitted to the AWS DeepRacer Student leaderboard after training is complete.
Optionally, you may opt out of entering
your model by deselecting the checkbox.

###### Tip

We recommend that you submit your model to the leaderboard. Submitting your model helps you to see how your model compares to others and
provides you with feedback so you can improve your model. 4. Choose **Train your model**. 5. In the **Initializing model training** pop-up, choose **Okay**. 6. On the **Training configuration** page, you can review your model's training status and configuration. You can also view
a video of your model training on the selected track when the training **Status** is **In progress**. Watching the video
can help you develop valuable insights that you can use to improve your model.

## Step 7: View your model's performance on the leaderboard

After you have trained your model and submitted it to a leaderboard, you can view its performance.

###### To view your model's performance

1. In the left navigation pane, navigate to and expand **Compete**. Choose a
   season. On the
   **Leaderboard** page, your model and your rank appear in a section. The
   page also includes a **Leaderboard** section with a list of the submitted
   models, race details, and a **Race details** section.
2. In the page that displays the leaderboard, in the section with your profile, select **Watch Video** to view a video of your model's
   performance.

## Step 8: Use **Clone** to improve your model

After you have trained and optionally submitted your model to a leaderboard, you can
clone it to improve it. Cloning your model saves you steps and makes training more efficient
by using a previously trained model as the starting point for a new model.

###### To clone and impove a model

1. In AWS DeepRacer Student, in the left navigation pane, navigate to **Your
   models**.
2. On the **Your models** page, select a model and choose
   **Clone**.
3. In the **Name your model** field, provide a new name for your cloned model and choose **Next**.
4. On the **Customize a reward function** page, customize the reward function
   and choose **Next**. For more information about customizing the reward
   function, see [Step 5: Customize your reward function](#student-league-create-model-step-five "#student-league-create-model-step-five").
5. In the **Choose duration** page, enter a time in the **Choose
   duration of model training** field, enter a description in the **Model
   description** field, and select the checkbox to submit the cloned model to the
   leaderboard.
6. Choose **Train your model**. Your training is initialized. The **Training configuration** page appears with information about your cloned model.
   You can also view a video of your model training on the selected track when the training **Status** is **In progress**.
7. Continue cloning and modifying your pre-trained models to achieve your best performance on the leaderboard.

## Step 9: (Optional) Download a model

After training a model and optionally submitting it to the leaderboard, you may want to
download it for future use on a AWS DeepRacer physical device. Your model is saved as a `.tar.gz` file.

###### To download a model

1. In AWS DeepRacer Student, in the left navigation pane, navigate to **Your
   models**.
2. On the **Your models** page, select a model and choose
   **Download**.
3. Track the progress of the model download in your browser. When your model is downloaded, you can save it to your local hard drive or other
   preferred storage device.

To learn more about working with AWS DeepRacer devices, see [Operate Your AWS DeepRacer Vehicle](../developerguide/operate-deepracer-vehicle.md "../developerguide/operate-deepracer-vehicle.md") in the _AWS DeepRacer guide_.
