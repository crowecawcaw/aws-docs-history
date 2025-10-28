# How K-Means Clustering Works

K-means is an algorithm that trains a model that groups similar objects together. The
k-means algorithm accomplishes this by mapping each observation in the input dataset to
a point in the _n_-dimensional space (where _n_ is the number of attributes of the observation). For
example, your dataset might contain observations of temperature and humidity in a
particular location, which are mapped to points (_t,
h_) in 2-dimensional space.

###### Note

Clustering algorithms are unsupervised. In unsupervised learning, labels that
might be associated with the objects in the training dataset aren't used. For more
information, see [Unsupervised learning](algorithms-choose.md#algorithms-choose-unsupervised-learning "algorithms-choose.md#algorithms-choose-unsupervised-learning").

In k-means clustering, each cluster has a center. During model training, the k-means
algorithm uses the distance of the point that corresponds to each observation in the
dataset to the cluster centers as the basis for clustering. You choose the number of
clusters (_k_) to create.

For example, suppose that you want to create a model to recognize handwritten digits
and you choose the MNIST dataset for training. The dataset provides thousands of images
of handwritten digits (0 through 9). In this example, you might choose to create 10
clusters, one for each digit (0, 1, …, 9). As part of model training, the k-means
algorithm groups the input images into 10 clusters.

Each image in the MNIST dataset is a 28x28-pixel image, with a total of 784 pixels.
Each image corresponds to a point in a 784-dimensional space, similar to a point in a
2-dimensional space (x,y). To find a cluster to which a point belongs, the k-means
algorithm finds the distance of that point from all of the cluster centers. It then
chooses the cluster with the closest center as the cluster to which the image belongs.

###### Note

Amazon SageMaker AI uses a customized version of the algorithm where, instead of specifying
that the algorithm create _k_ clusters, you might
choose to improve model accuracy by specifying extra cluster centers _(K = k\*x)_. However, the algorithm ultimately reduces
these to _k_ clusters.

In SageMaker AI, you specify the number of clusters when creating a training job. For more
information, see [`CreateTrainingJob`](../APIReference/API_CreateTrainingJob.md "../APIReference/API_CreateTrainingJob.md"). In the request body, you add the
`HyperParameters` string map to specify the `k` and
`extra_center_factor` strings.

The following is a summary of how k-means works for model training in SageMaker AI:

1. It determines the initial _K_ cluster
   centers.

###### Note

In the following topics, _K_ clusters
refer to _k \* x_, where you specify
_k_ and _x_ when creating a model training job. 2. It iterates over input training data and recalculates cluster centers. 3. It reduces resulting clusters to _k_ (if the
data scientist specified the creation of _k\*x_
clusters in the request).
The following sections also explain some of the parameters that a data scientist might
specify to configure a model training job as part of the `HyperParameters`
string map.

###### Topics

- [Step 1: Determine the Initial Cluster Centers](#kmeans-step1 "#kmeans-step1")
- [Step 2: Iterate over the Training Dataset and
  Calculate Cluster Centers](#kmeans-step2 "#kmeans-step2")
- [Step 3: Reduce the Clusters from K to k](#kmeans-step3 "#kmeans-step3")

## Step 1: Determine the Initial Cluster Centers

When using k-means in SageMaker AI, the initial cluster centers are chosen from the
observations in a small, randomly sampled batch. Choose one of the following
strategies to determine how these initial cluster centers are selected:

- The random approach—Randomly choose _K_ observations in your input dataset as
  cluster centers. For example, you might choose a cluster center that points
  to the 784-dimensional space that corresponds to any 10 images in the MNIST
  training dataset.
- The k-means++ approach, which works as follows:
  1.  Start with one cluster and determine its center. You randomly
      select an observation from your training dataset and use the point
      corresponding to the observation as the cluster
      center. For example, in the MNIST
      dataset, randomly choose a handwritten digit image. Then choose the
      point in the 784-dimensional space that corresponds to the image as
      your cluster center. This is cluster center 1.
  2.  Determine the center for cluster 2. From the remaining
      observations in the training dataset, pick an observation at random.
      Choose one that is different than the one you previously selected.
      This observation corresponds to a point that is far away from
      cluster center 1. Using the MNIST dataset as an example, you do the
      following:
      - For each of the remaining images, find the distance of the
        corresponding point from cluster center 1. Square the
        distance and assign a probability that is proportional to
        the square of the distance. That way, an image that is
        different from the one that you previously selected has a
        higher probability of getting selected as cluster center 2.
      - Choose one of the images
        randomly,
        based on probabilities assigned in the previous
        step. The point that corresponds to the
        image is cluster center 2.

  3.  Repeat Step 2 to find cluster center 3. This time, find the
      distances of the remaining images from cluster center 2.
  4.  Repeat the process until
      you
      have the _K_ cluster
      centers.

To
train a model in SageMaker AI, you create a training job. In the request, you provide
configuration information by specifying the following `HyperParameters`
string maps:

- To specify the number of clusters to create, add the `k`
  string.
- For greater accuracy, add the optional `extra_center_factor`
  string.
- To specify the strategy that you want to use to determine the initial
  cluster centers, add the `init_method` string and set its value
  to `random` or `k-means++`.

For more information about the SageMaker AI k-means estimator, see [K-means](https://sagemaker.readthedocs.io/en/stable/algorithms/unsupervised/kmeans.html "https://sagemaker.readthedocs.io/en/stable/algorithms/unsupervised/kmeans.html") in the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable") documentation.

You now have an initial set of cluster centers.

## Step 2: Iterate over the Training Dataset and

Calculate Cluster Centers

The cluster centers that you created in the preceding step are mostly random, with
some consideration for the training dataset. In this step, you use the training
dataset to move these centers toward the true cluster centers. The algorithm
iterates over the training dataset, and recalculates the _K_ cluster centers.

1. Read a mini-batch of observations (a small, randomly chosen subset of all
   records) from the training dataset and do the following.

###### Note

When creating a model training job, you specify the batch size in the
`mini_batch_size` string in the
`HyperParameters` string map.

    1. Assign all of the observations in the mini-batch to one of the
     clusters with the closest cluster center.
    2. Calculate the number of observations assigned to each cluster.
     Then, calculate the proportion of new points assigned per
     cluster.


    For example, consider the following clusters:


    Cluster c1 = 100 previously assigned points. You added 25 points
     from the mini-batch in this step.


    Cluster c2 = 150 previously assigned points. You added 40 points
     from the mini-batch in this step.


    Cluster c3 = 450 previously assigned points. You added 5 points
     from the mini-batch in this step.


    Calculate the proportion of new points assigned to each of
     clusters as follows:



    ```
    p1 = proportion of points assigned to c1 = 25/(100+25)
    p2 = proportion of points assigned to c2 = 40/(150+40)
    p3 = proportion of points assigned to c3 = 5/(450+5)
    ```
    3. Compute the center of the new points added to each cluster:



    ```
    d1 = center of the new points added to cluster 1
    d2 = center of the new points added to cluster 2
    d3 = center of the new points added to cluster 3
    ```
    4. Compute the weighted average to find the updated cluster centers
     as follows:



    ```
    Center of cluster 1 = ((1 - p1) * center of cluster 1) + (p1 * d1)
    Center of cluster 2 = ((1 - p2) * center of cluster 2) + (p2 * d2)
    Center of cluster 3 = ((1 - p3) * center of cluster 3) + (p3 * d3)
    ```

2. Read the next mini-batch, and repeat Step 1 to recalculate the cluster
   centers.
3. For more information about mini-batch _k_-means, see [Web-scale k-means Clustering](https://citeseerx.ist.psu.edu/document?repid=rep1type=pdf&doi=b452a856a3e3d4d37b1de837996aa6813bedfdcf "https://citeseerx.ist.psu.edu/document?repid=rep1type=pdf&doi=b452a856a3e3d4d37b1de837996aa6813bedfdcf")).

## Step 3: Reduce the Clusters from _K_ to _k_

If the algorithm created _K_
clusters—_(K = k\*x)_ where _x_ is greater than 1—then it reduces the
_K_ clusters to _k_ clusters. (For more information, see
`extra_center_factor` in the preceding discussion.) It does this by
applying Lloyd's method with `kmeans++` initialization to the _K_ cluster centers. For more information about Lloyd's
method, see [k-means clustering](https://pdfs.semanticscholar.org/0074/4cb7cc9ccbbcdadbd5ff2f2fee6358427271.pdf "https://pdfs.semanticscholar.org/0074/4cb7cc9ccbbcdadbd5ff2f2fee6358427271.pdf").
