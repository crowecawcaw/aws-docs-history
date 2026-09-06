

# Use TensorBoard in Amazon SageMaker Studio Classic
<a name="studio-tensorboard"></a>

**Note**  
As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md).  
Studio Classic is still maintained for existing workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md).

 The following doc outlines how to install and run TensorBoard in Amazon SageMaker Studio Classic. 

**Note**  
This guide shows how to open the TensorBoard application through a SageMaker Studio Classic notebook server of an individual SageMaker AI domain user profile. For a more comprehensive TensorBoard experience integrated with SageMaker Training and the access control functionalities of SageMaker AI domain, see [TensorBoard in Amazon SageMaker AI](tensorboard-on-sagemaker.md).

## Prerequisites
<a name="studio-tensorboard-prereq"></a>

This tutorial requires a SageMaker AI domain. For more information, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md)

## Set Up `TensorBoardCallback`
<a name="studio-tensorboard-setup"></a>

1. Launch Studio Classic, and open the Launcher. For more information, see [Use the Amazon SageMaker Studio Classic Launcher](studio-launcher.md)

1. In the Amazon SageMaker Studio Classic Launcher, under `Notebooks and compute resources`, choose the **Change environment** button.

1. On the **Change environment** dialog, use the dropdown menus to select the `TensorFlow 2.6 Python 3.8 CPU Optimized` Studio Classic **Image**.

1. Back to the Launcher, click the **Create notebook** tile. Your notebook launches and opens in a new Studio Classic tab.

1. Run this code from within your notebook cells.

1. Import the required packages. 

   ```
   import os
   import datetime
   import tensorflow as tf
   ```

1. Create a Keras model.

   ```
   mnist = tf.keras.datasets.mnist
   
   (x_train, y_train),(x_test, y_test) = mnist.load_data()
   x_train, x_test = x_train / 255.0, x_test / 255.0
   
   def create_model():
     return tf.keras.models.Sequential([
       tf.keras.layers.Flatten(input_shape=(28, 28)),
       tf.keras.layers.Dense(512, activation='relu'),
       tf.keras.layers.Dropout(0.2),
       tf.keras.layers.Dense(10, activation='softmax')
     ])
   ```

1. Create a directory for your TensorBoard logs

   ```
   LOG_DIR = os.path.join(os.getcwd(), "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
   ```

1. Run training with TensorBoard.

   ```
   model = create_model()
   model.compile(optimizer='adam',
                 loss='sparse_categorical_crossentropy',
                 metrics=['accuracy'])
                 
                 
   tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=LOG_DIR, histogram_freq=1)
   
   model.fit(x=x_train,
             y=y_train,
             epochs=5,
             validation_data=(x_test, y_test),
             callbacks=[tensorboard_callback])
   ```

1. Generate the EFS path for the TensorBoard logs. You use this path to set up your logs from the terminal.

   ```
   EFS_PATH_LOG_DIR = "/".join(LOG_DIR.strip("/").split('/')[1:-1])
   print (EFS_PATH_LOG_DIR)
   ```

   Retrieve the `EFS_PATH_LOG_DIR`. You will need it in the TensorBoard installation section.

## Install TensorBoard
<a name="studio-tensorboard-install"></a>

1. Click on the  `Amazon SageMaker Studio Classic` button on the top left corner of Studio Classic to open the Amazon SageMaker Studio Classic Launcher. This launcher must be opened from your root directory. For more information, see [Use the Amazon SageMaker Studio Classic Launcher](studio-launcher.md)

1. In the Launcher, under `Utilities and files`, click `System terminal`. 

1. From the terminal, run the following commands. Copy `EFS_PATH_LOG_DIR` from the Jupyter notebook. You must run this from the `/home/sagemaker-user` root directory.

   ```
   pip install tensorboard
   tensorboard --logdir {{<EFS_PATH_LOG_DIR>}}
   ```

## Launch TensorBoard
<a name="studio-tensorboard-launch"></a>

1. To launch TensorBoard, copy your Studio Classic URL and replace `lab?` with `proxy/6006/` as follows. You must include the trailing `/` character.

   ```
   https://{{<YOUR_URL>}}.studio.{{region}}.sagemaker.aws/jupyter/default/proxy/6006/
   ```

1. Navigate to the URL to examine your results. 