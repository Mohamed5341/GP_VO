# Model

In Gazebo, everything in the world has a model (vehicle, ground, wall, tree, ...). Model can be created using Model Editor which is a GUI window in Gazebo, or by creating model files manually. Basically, model consists of two files: configuration and SDF file, that are grouped together in one folder. For example, for a plane it will be


├── plane
|   ├── model.config
|   ├── plane.sdf

Configuration file contains general information about model, like name, author, description, ..., while SDF file contains details about appearance and behavior of model in world, like size, apperance, shape, .... Both files are written in XML. which is some known tags with model data.

# Create a model

Here is an example of creating a model of a car. First, create a folder called `car` and create two files inside it called `model.config` and `car.sdf`.

├── car
|   ├── model.config
|   ├── car.sdf

![Model Directory](../Images/Gazebo/Create%20a%20model/model_folder.png)

## Configuration file

Then in configuration file write:

```XML
<?xml version="1.0"?>
<model>
  <name>car</name>
  <sdf version='1.6'>car.sdf</sdf>

  <author>
   <name>Mohamed Ashraf</name>
  </author>

  <description>
    This is a model of a car.
  </description>
</model>
```

Lets break this into lines

```XML
<?xml version="1.0"?>
```

It just specify version of XML.


```XML
<model>
  ...
</model>
```

We write all details about model in model tag.

```XML
<name>car</name>
```

Name tag contains the name of the model which is car.

```XML
<sdf version='1.6'>car.sdf</sdf>
```

Next we specify SDF file using its name, and specify SDF version which is 1.6. Check [Gazebo](http://gazebosim.org/tutorials?tut=install_dependencies_from_source#Versions) for more information about SDF versions. But here we use Gazebo 9 so 1.6 or earlier is good.

```XML
<author>
 <name>Mohamed Ashraf</name>
</author>

<description>
  This is a model of a car.
</description>
```

Author tag contains information about author of model like name, email. Description contains a small description about model.

## SDF file

In SDF file it contains some defined XML tags that are used to describe shape and behavior of model, for more information about [SDF](http://sdformat.org/spec?elem=sdf&ver=1.6). Our car here consists of simple geometry, two boxes (car body) and four cylinders (wheels).

![Car extruded image](../Images/Gazebo/Create%20a%20model/car_extruded.png)

![Car](../Images/Gazebo/Create%20a%20model/car_expectations.png)

Here is the whole file.

```XML
<?xml version='1.0'?>
<sdf version="1.6">
  <model name="car">
    <pose>0 0 1 0 0 0</pose>
    <static>false</static>

    <link name="main">

      <pose>0 0 0 0 0 0</pose>

      <inertial>
        <mass>1.0</mass>
        <inertia>
          <ixx>0.03</ixx>
          <ixy>0.0</ixy>
          <ixz>0.0</ixz>
          <iyy>0.03</iyy>
          <iyz>0.0</iyz>
          <izz>0.03</izz>
        </inertia>
      </inertial>

      <collision name="collision">
        <geometry>
          <box>
            <size>1 1 1</size>
          </box>
        </geometry>
      </collision>

      <visual name="visual">

        <geometry>
          <box>
            <size>1 1 1</size>
          </box>
        </geometry>

        <material>
          <ambient>0.2 0 0 1</ambient>
        </material>
      </visual>

    </link>

    <link name="front">

      <pose>0.75 0 -0.25 0 0 0</pose>

      <inertial>
        <mass>.25</mass>
        <inertia>
          <ixx>0.015</ixx>
          <ixy>0.0</ixy>
          <ixz>0.0</ixz>
          <iyy>0.015</iyy>
          <iyz>0.0</iyz>
          <izz>0.015</izz>
        </inertia>
      </inertial>

      <collision name="collision">
        <geometry>
          <box>
            <size>0.5 1 0.5</size>
          </box>
        </geometry>
      </collision>

      <visual name="visual">

        <geometry>
          <box>
            <size>0.5 1 0.5</size>
          </box>
        </geometry>

        <material>
          <ambient>0.2 0 0 1</ambient>
        </material>
      </visual>

    </link>

    <link name="frwheel">

      <pose>0.75 -0.575 -0.5 -1.570791 0 0</pose>

      <inertial>
        <mass>.2</mass>
        <inertia>
          <ixx>0.01</ixx>
          <ixy>0.0</ixy>
          <ixz>0.0</ixz>
          <iyy>0.01</iyy>
          <iyz>0.0</iyz>
          <izz>0.01</izz>
        </inertia>
      </inertial>

      <collision name="collision">
        <geometry>
          <cylinder>
            <radius>0.25</radius>
            <length>0.15</length>
          </cylinder>
        </geometry>
      </collision>

      <visual name="visual">

        <geometry>
          <cylinder>
            <radius>0.25</radius>
            <length>0.15</length>
          </cylinder>
        </geometry>

        <material>
          <ambient>0 0 0.2 1</ambient>
        </material>
      </visual>

    </link>

    <link name="brwheel">

      <pose>-0.25 -0.575 -0.5 -1.570791 0 0</pose>

      <inertial>
        <mass>.2</mass>
        <inertia>
          <ixx>0.01</ixx>
          <ixy>0.0</ixy>
          <ixz>0.0</ixz>
          <iyy>0.01</iyy>
          <iyz>0.0</iyz>
          <izz>0.01</izz>
        </inertia>
      </inertial>

      <collision name="collision">
        <geometry>
          <cylinder>
            <radius>0.25</radius>
            <length>0.15</length>
          </cylinder>
        </geometry>
      </collision>

      <visual name="visual">

        <geometry>
          <cylinder>
            <radius>0.25</radius>
            <length>0.15</length>
          </cylinder>
        </geometry>

        <material>
          <ambient>0 0 0.2 1</ambient>
        </material>
      </visual>

    </link>

    <link name="flwheel">

      <pose>0.75 0.575 -0.5 1.570791 0 0</pose>

      <inertial>
        <mass>.2</mass>
        <inertia>
          <ixx>0.01</ixx>
          <ixy>0.0</ixy>
          <ixz>0.0</ixz>
          <iyy>0.01</iyy>
          <iyz>0.0</iyz>
          <izz>0.01</izz>
        </inertia>
      </inertial>

      <collision name="collision">
        <geometry>
          <cylinder>
            <radius>0.25</radius>
            <length>0.15</length>
          </cylinder>
        </geometry>
      </collision>

      <visual name="visual">

        <geometry>
          <cylinder>
            <radius>0.25</radius>
            <length>0.15</length>
          </cylinder>
        </geometry>

        <material>
          <ambient>0 0 0.2 1</ambient>
        </material>
      </visual>

    </link>

    <link name="blwheel">

      <pose>-0.25 0.575 -0.5 1.570791 0 0</pose>

      <inertial>
        <mass>.2</mass>
        <inertia>
          <ixx>0.01</ixx>
          <ixy>0.0</ixy>
          <ixz>0.0</ixz>
          <iyy>0.01</iyy>
          <iyz>0.0</iyz>
          <izz>0.01</izz>
        </inertia>
      </inertial>

      <collision name="collision">
        <geometry>
          <cylinder>
            <radius>0.25</radius>
            <length>0.15</length>
          </cylinder>
        </geometry>
      </collision>

      <visual name="visual">

        <geometry>
          <cylinder>
            <radius>0.25</radius>
            <length>0.15</length>
          </cylinder>
        </geometry>

        <material>
          <ambient>0 0 0.2 1</ambient>
        </material>
      </visual>

    </link>

    <joint name="joint_2_boxes" type="fixed">
      <parent>main</parent>
      <child>front</child>
    </joint>


    <joint name="joint_frwheel" type="revolute">
      <pose>0.75 -0.575 -0.5 0 0 0</pose>
      <parent>front</parent>
      <child>frwheel</child>
      <axis>
        <xyz>0 1 0</xyz>
      </axis>
    </joint>

    <joint name="joint_flwheel" type="revolute">
      <pose>0.75 0.575 -0.5 0 0 0</pose>
      <parent>front</parent>
      <child>flwheel</child>
      <axis>
        <xyz>0 1 0</xyz>
      </axis>
    </joint>


    <joint name="joint_brwheel" type="revolute">
      <pose>-0.25 -0.575 -0.5 0 0 0</pose>
      <parent>main</parent>
      <child>brwheel</child>
      <axis>
        <xyz>0 1 0</xyz>
      </axis>
    </joint>

    <joint name="joint_blwheel" type="revolute">
      <pose>-0.25 0.575 -0.5 0 0 0</pose>
      <parent>main</parent>
      <child>blwheel</child>
      <axis>
        <xyz>0 1 0</xyz>
      </axis>
    </joint>

  </model>
</sdf>
```

First, it specify XML version.

```XML
<sdf version="1.6">
  <model name="car">
    ...
  </model>
</sdf>
```

We put all tags inside sdf tag. Inside model tag we put tags that describe model. Inside model there is three main things (in addition to other things).

1. Links: each part of model is called link, for example car here has 6 components (2 boxes and 4 cylinders) each one is a link.
    1.1. Collision: Describes the shape of link that collide with other.
    1.2. Visual: Describe the shape that appears on screen.
    1.3. Inertia: Inertia values for Link.
    1.4. Sensor: If this link is a sensor, describe this sensor characteristics.
2. Joints: Relations between links.
3. Plugin: A library that can be used to control this model.

```XML
<static>false</static>
```

Starting with specify static tag to be false, if this model is static then it will be like a wall or ground that does not move.

Next moving to links, we define 6 links with their properties like pose, mass, inertia, collision and visual, define pose for each link so it will be in its specified location. Then we have joint tag to define the relation between main part and front part to be `fixed` (relative to each other). Define joints for 4 wheels to be `revolute` which means to be hinged around certain point and rotate about one axis.

To add this model to gazebo, you can move this file to `.gazebo/models` folder. `.gazebo` is a hidden folder in home directory. Then open Gazebo, go to insert tab and you will find your car model.

![Model is added](../Images/Gazebo/Create%20a%20model/gazebo_model_is_added.png)

![Car](../Images/Gazebo/Create%20a%20model/car_in_gazebo.png)

You can find this model [here](../src/models/car).
