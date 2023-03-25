# SVO Getting Saturated

Download SVO [source code](https://github.com/uzh-rpg/rpg_svo_pro_open.git) put it in new workspace then build workspace, as mentioned in SVO repo.

# Camera Calibration

Calibration step is mentioned in SVO repo. It uses ROS camera calibration tool. Before running calibration you need a checker board with specified dimentions in gazebo. Here is a python [script](https://gist.github.com/Kukanani/4b09debf29eafdd4d96c4717520e6f18) to create checker board for gazebo.

![Gazebo Checkerboard](../Images/SVO/Getting%20Started/gazebo_checkerboard.png)

Now, you need to run camera and Gazebo with ROS. Or instead of doing this just simply add camera parameters to SDF model file, and use these parameters in SVO model. You need to put parameters in `.yaml` file in

```
rpg_svo_pro_open/svo_ros/param/calib
```

You can find examples of files in this folder.

# Test SVO

Now, that you have a calibrated camera, You need to run and test it. First you need a world with enough scene texture so it can detect motion. Here is an example of camera simple mission.

<!-- add video to camera motion -->

![First Output](../Images/SVO/Getting%20Started/first_output_actual_svo.png)

Here you can see true position is measured in meters, estimated position is similar in shape, but different in size and initial condition, so you need to edit initial condition, then scale output. Scale is modified in `pinhole.yaml` file, which is a file contains parameters for SVO algorithm, it is located at:

```
rpg_svo_pro_open/svo_ros/param
```

![After scaling and translation](../Images/SVO/Getting%20Started/second_output_actual_svo.png)

Now estimated position is closer to actual one. Here is [launch](../src/launch/test1.launch) and [world](../src/worlds/test1.world) files