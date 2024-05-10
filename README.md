# DLS_project (advanced thread)
 Final project for the DLS MIPT course


 In my task, it is necessary to learn how to carry out active phasing of a multi-channel system using a neural network.

 1. This is a new technology in a physical system, but there are applications to it,
 on the basis of which the dataset is built.

 2. Data - numerical algorithms will be used to generate data.  The data is a matrix of field intensities with a certain partition.

 3. Conceptually, I would like to develop 2 grids.  Convolutional and fully connected, conduct experiments on hyperparameters,
 choose the best one, justify the results.  The network should be simple and lightweight, because in a real experiment, fast phasing is important.  It is for this task that the convolutional one seems to be most suitable, it will be possible to “screw up” it and expand the functionality,
 but again, the choice of architecture will be in favor of the speed of the system.

a physical quantity indicating the phasing of the system after applying a grid to the intensity matrix.
 Also, for a more complete understanding of the problem being solved, I provide a block diagram of the project


 ![image](https://github.com/sammorozov/DLS_project/assets/109150200/cdd4d4be-4e02-40ad-b267-1bd459bd4fd9)

 # Implementation plan:

 1. Simulation of multichannel laser radiation in the near and far zones
 2. Creating a training sample for the neural network
 3. Development of a fully connected neural network
 4. Analysis of results
 5. Development of a convolutional neural network
 6. Experiments with hyperparameters of the best model

# laser radiation in the near zone.

 ![image](https://github.com/sammorozov/DLS_project/assets/109150200/a858d1f5-a3f7-4e34-95ba-5a98210f8b53)

 ![image](https://github.com/sammorozov/DLS_project/assets/109150200/aaf934dc-76e8-469a-8900-507d9136d9ba)


 # Simulation of multichannel laser radiation in the far zone.

 ![image](https://github.com/sammorozov/DLS_project/assets/109150200/58dd8903-b8f4-437e-b0bb-d2b064a0f53e)


 ![image](https://github.com/sammorozov/DLS_project/assets/109150200/133932c6-d9e6-4de5-b1c8-30759b4546a4)


 # Creating a training sample

 The principle of forming one pair of data:

There is a segment [0, 2π] for possible values ​​of one of the four phases of the laser channel.
 Loss:

 ![image](https://github.com/sammorozov/DLS_project/assets/109150200/37f549aa-27fd-462a-bf6f-835ffcf7c213)


 # Analysis of results

 Single case
 ![image](https://github.com/sammorozov/DLS_project/assets/109150200/2a4a0edf-8d62-40fa-838e-b3d6f8df300f)

 On the left is a matrix on randomly generated phases

 On the right is the matrix after applying “neurophasing”

 ![image](https://github.com/sammorozov/DLS_project/assets/109150200/d4b5fa4a-42b2-48eb-8795-cba086d3b13e)

 General case

 ![image](https://github.com/sammorozov/DLS_project/assets/109150200/bdc2a411-2d5b-44b1-b4ae-f9e60fa11026)

 # Development of a fully connected neural network

 Architecture.  LeNet5 was taken as the base model, but was modified to solve the regression problem,
 and also underwent changes in the dimension of the layers, shift and convolution size, the pooling layers worked greedily for such a task,
 in the end, after numerous experiments with hyperparameters, the following architecture was chosen, which gave
 best results.

 ![image](https://github.com/sammorozov/DLS_project/assets/109150200/864bddad-871f-492a-bd46-ad8d08e0334b)
 ![image](https://github.com/sammorozov/DLS_project/assets/109150200/c0246bb7-9f98-41ba-9d09-45c70ab9fb39)



 # Analysis of the results of a convolutional neural network.

 ![image](https://github.com/sammorozov/DLS_project/assets/109150200/9eada714-fa30-44bf-8b1f-4c367e346702)

 Next, let’s calculate how much the Strehl number increases on average for this configuration, which is currently the best according to the results of the graphs.  On average, after passing any data set through a convolutional neural network, the Strehl number increases by 0.42, and through a fully connected one by 0.37.  Obviously, a convolutional neural network will be used for phasing since it gives the best quality and quantity of phasing cases.  From the initial distribution, the average Strehl number is: 0.25, which means when added, the average result will be 0.69, which falls short of phasing by several points, but is already a good result.
