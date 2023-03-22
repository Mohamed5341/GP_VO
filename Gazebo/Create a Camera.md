# Create a Camera

First, you need to understand [model](./Create%20a%20model.md) and how to create a model. For creating a camera it is easy. Define SDF model with regular structure, and put inside the model a link which represents the camera.

```XML
<?xml version="1.0" ?>
<sdf version="1.6">
  <model name="box">
    <link name="link">

        ...

    </link>
  </model>
</sdf>
```

Inside this link tag you add all its properties. We are concerned with one thing of camera, which is camera properties (not mass, Inertia, ...). A camera is a sensor so you add the sensor tag, with unique name and a type (which is camera).

```XML
<sensor type="camera" name="my_camera">
    
    ...

</sensor>
```

Inside sensor tag, you add all properties of this sensor, we can divide these properties as camera properties and sensor properties. Camera properties are placed inside camera tag.

```XML
<sensor type="camera" name="my_camera">
          <camera>

            <horizontal_fov>1.047</horizontal_fov>
            
            <image>
              <width>320</width>
              <height>240</height>
            </image>
            
            <clip>
              <near>0.1</near>
              <far>100</far>
            </clip>
          </camera>
          
          <always_on>1</always_on>
          <update_rate>30</update_rate>
          <visualize>true</visualize>
          <topic>images_stream</topic>

        </sensor>
```

|  Type  |    Property    | Description                                                      |
| :----: | :------------: | ---------------------------------------------------------------- |
| Sensor |   always_on    | Make the sensor reads data continuously with specified rate      |
|        |  update_rate   | number of samples taken by the sensor in one second              |
|        |   visualize    | if it is true it shows graphics for sensor measuring space       |
|        |     topic      | it is the name of gazebo topic that sensor publish its output    |
| Camera |     image      | it contains 2 child tages width and height for camera resolution |
|        |      clip      | its child tags are near and far which are limits of camera scene |
|        | horizontal_fov | horizontal field of view in radians                              |

Now, if you added this model to gazebo (but remember to use static tag for model so camera is fixed). You can open visualizer to camera output form topic visualizer.

![Gazebo open topics](../Images/Gazebo/Create%20a%20Camera/camera_open_topics_menu.png)

![Select camera topic](../Images/Gazebo/Create%20a%20Camera/camera_topic_selection.png)

You will see the topic under the type of Gazebo.msgs.ImageStamped.

![Camera visualizer](../Images/Gazebo/Create%20a%20Camera/camera_visualizer.png)


You can add objects to the scene inside camera and it will appear.

![Camera Image Colored](../Images/Gazebo/Create%20a%20Camera/camera_colored_image.png)

As you can see image here contains objects which are added to scene. One importat thing is that image is colored, we need it to be gray scale (black and white), this is done by editing `image` tag and add `format` tag to it, which is by default is RGB with 8 bits data for each channel. So we make it L8 (which is gray scale).

![Camera Black and white image](../Images/Gazebo/Create%20a%20Camera/camera_bw_image.png)

# Run camera with Rose

This camera works fine with gazebo. But we need this camera to export images to ROS topic. There is a gazebo plugin used to publish images over ROS topic. This plugin has some properties.

```XML
<sensor>
  
  ...

  <plugin name="camera_controller" filename="libgazebo_ros_camera.so">
    <alwaysOn>true</alwaysOn>
    <updateRate>0.0</updateRate>
    <cameraName>uav/camera1</cameraName>
    <imageTopicName>image_raw</imageTopicName>
    <cameraInfoTopicName>camera_info</cameraInfoTopicName>
    <frameName>camera_link</frameName>
  </plugin>
</sensor>
```

Plugin here is a camera plugin that takes image from gazebo and publish it to ROS. Here is file name and plugin properties. 


```XML
<cameraName>uav/camera1</cameraName>
```

Here camera name is the name that topic is listed under. So topic becomes `uav/camera1/<topic-name>`

```XML
<imageTopicName>image_raw</imageTopicName>
```

Here is topic name is `image_raw`, now topic name becomes fully `uav/camera1/image_raw.

```XML
<cameraInfoTopicName>camera_info</cameraInfoTopicName>
```

Here is the topic name thta publish camera info, `uav/camera1/camera_info`


```XML
<frameName>camera_link</frameName>
```

Frame here is name for camera frame which is required with ROS.

After you add plugin to camera model to run it, first you need to run ros.

```
roscore
```

then, in new terminal, run gazebo window.

```
rosrun gazebo_ros gazebo
```

add camera model to gazebo world, then to make sure that there is a topic that publish camera images, checkout topics list.

![Camera Topic](../Images/Gazebo/Create%20a%20Camera/camera_ros_topic.png)

To show camera output you can use Rviz, which is GUI used with ROS to show output in graphical way, which also includes camera view. To run it use.

```
rosrun rviz rviz
```

It will open new window, add camera view to it then select images topic.

![Rviz add button](../Images/Gazebo/Create%20a%20Camera/rviz_add_view_button.png)

![Rviz add camera view](../Images/Gazebo/Create%20a%20Camera/rviz_add_camera_view.png)

![Rviz select camera topic](../Images/Gazebo/Create%20a%20Camera/rviz_select_camera_topic.png)

After this you will find error for camera frame. that what we called previously when we define plugin for camera.

![Camera frame Error](../Images/Gazebo/Create%20a%20Camera/rviz_camera_error.png)

Rviz defines views according to certain frame, it is called `map` (under general options). Camera frame is not defined to Rviz, so it can't display image. you need to create a transformation that relates map frame to camera frame. This is done using `tf` node.

```
rosrun tf static_transform_publisher 0.0 0.0 0.0 0.0 0.0 0.0 map camera_link 100
```

![Camera view](../Images/Gazebo/Create%20a%20Camera/rviz_camera_view.png)

This is how to create a camera with ROS, you can find model [here](../src/models/camera).