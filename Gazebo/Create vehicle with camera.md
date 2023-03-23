# Create a vehicle with camera

After creating a camera [model](./Create%20a%20Camera.md). Now we need to add this camera to ou vehicle. So when runnung simulation, we have our complete system.

# Include models

Gazebo models offer include external model to your model, by using `include` tag. To show what it means, here is our case, we have VTOL UAV.

![VTOL UAV](../Images/Gazebo/Create%20a%20vehicle%20with%20camera/standard_vtol_vehicle.png)

Now, we want to add a camera under the UAV and looks downward. To include this we need to create a new model.

```XML
<include>
    <uri>model://standard_vtol</uri>
</include>

<include>
    <uri>model://camera</uri>
    <pose>0 0 0 0 1.570796 0</pose>
</include>

<joint name="uav_cam_joint" type="fixed">
    <parent>standard_vtol::base_link</parent>
    <child>camera::camera_link</child>
</joint>
```

Here,  first we added vtol model, then we added camera model, camera model with relative position to model origin, it is only rotated by $90{\degree} \approx 1.570796 \text{ rad}$. Then created a joint relation between vehicle and camera, which is of type fixed, it means child is fixed to its parent. Running simulation and add objects to scene.

![VTOL Camera Image](../Images/Gazebo/Create%20a%20vehicle%20with%20camera/vtol_camera_image.png)

# Add vehicle to PX4

we need to add vehicle to PX4 gazebo repo. This can be done in multiple steps:

1. copy both camera and vtol model folders into

```
PX4-Autopilot/Tools/simulation/gazebo-classic/sitl_gazebo-classic/models
```
2. Add a parameters folder to:
```
PX4-Autopilot/ROMFS/px4fmu_common/init.d-posix/airframes
```
You will found alot of vehicles, you can copy standard_vtol file, and just edit the number(use any unused number) and the name.
![Parameters file](../Images/Gazebo/Create%20a%20vehicle%20with%20camera/parameters_file.png)
remember you can edit its parameters from here. Then add file name to `CMakeFile.text` in same directory

3. add name of vehicle to make file.
```
PX4-Autopilot/src/modules/simulation/simulator_mavlink/sitl_targets_gazebo-classic.cmake
```
Move to the part which says `set(models ...` and contains alot of vehicles. Insert your vehicle name.

now you can run model with camera and ROS usind.

```
source setup_ros_pack.bash
roslaunch px4 mavros_posix_sitl.launch vehicle:=standard_vtol_with_camera
```

<!--add video of running vehicle-->