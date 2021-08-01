# Plugins

Gazebo simulator provides user with the ability to write plugins, which are pieces of code that run during simulation. There are types of plugins according to the thing that is used with. Model plugin which is used with models. World plugin used with worlds ... and so on. 

Before you write your plugin you need first to download developer package for gazebo.

    sudo apt-get install libgazebo9-dev

# Create a plugin

Here is an example of plugin with [car model](Create a model.md). Create a folder `gazebo_car_plugin` that will contain plugin files. For a plugin, you need C++ file and cmake file.

    ├── gazebo_car_plugin
    |   ├── car_model_control.cc
    |   ├── CMakeLists.txt

Using

    mkdir ~/gazebo_car_plugin && cd ~/gazebo_car_plugin
    touch car_model_control.cc
    touch CMakeLists.txt

![Plugin files](../Images/Gazebo/Create%20a%20plugin/create_plugin_files.png)

## C++ file

In `car_model_control.cc` write code for your plugin.

```c++
#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>
#include <ignition/math/Vector3.hh>

namespace gazebo{
    class CarControlPlugin : public ModelPlugin
    {
        public: void Load(physics::ModelPtr _parent, sdf::ElementPtr _sdf)
        {
          // Store the pointer to the model
          this->model = _parent;
          
          
          // Listen to the update event. This event is broadcast every simulation iteration.
          this->updateConnection = event::Events::ConnectWorldUpdateBegin(std::bind(&CarControlPlugin::OnUpdate, this));
        }

        // Called by the world update start event
        public: void OnUpdate()
        {
          // Apply a linear velocity to model.
          this->model->SetLinearVel(ignition::math::Vector3d(1, 0, 0));
        }
        
        // Pointer to the model
        private: physics::ModelPtr model;
        
        // Pointer to the update event connection
        private: event::ConnectionPtr updateConnection;
    };
    GZ_REGISTER_MODEL_PLUGIN(CarControlPlugin);
}
```

Lets break this code into parts.

```c++
#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>
#include <ignition/math/Vector3.hh>
```

First, include required files, which contains functions that will be used in code.

```c++
namespace gazebo{
    class CarControlPlugin : public ModelPlugin
    {
        ...
    };
    ...
}
```

Define the plugin under `gazebo` namespace and in its own class. Class inherits `ModelPlugin` class.

```c++
GZ_REGISTER_MODEL_PLUGIN(CarControlPlugin);
```

At the end we register this class with Gazebo.

Inside this class there is two functions, `load` which is called when model is loaded into world. `OnUpdate` function which is called at each iteration for simulation. `load` function creates event to call update function at each iteration. `OnUpdate` sets model linear velocity to be 1 in x-direction.

## CMake file
In cmake file, you add compilation instructions.

```cmake
cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

find_package(gazebo REQUIRED)
include_directories(${GAZEBO_INCLUDE_DIRS})
link_directories(${GAZEBO_LIBRARY_DIRS})
list(APPEND CMAKE_CXX_FLAGS "${GAZEBO_CXX_FLAGS}")

add_library(car_control_plugin SHARED car_model_control.cc)
target_link_libraries(car_control_plugin ${GAZEBO_LIBRARIES})
```

## Compilation

Now, you can compile this plugin using:

    mkdir build && cd build
    cmake ..
    make

Plugin is compiled and can be found in build file.

![Plugin file](../Images/Gazebo/Create%20a%20plugin/plugin_after_compilation.png)

The required file after compilation is the file `.so` extension (Here, it is `libcar_control_plugin.so` file).

## Adding plugin to model

Now, we have [model](../src/models/car) and [plugin](../src/plugins/gazebo_car_plugin). We need to add plugin to the model. This is done by adding plugin tag inside model tag with file name.

```xml
<?xml version='1.0'?>
<sdf version="1.6">
  <model name="car">
    ...
    <plugin name="car_control" filename="libcar_control_plugin.so"/>
    ...
  </model>
</sdf>
```

Before we run gazebo and add model, we need to add location of our file to Gazebo path.

    export GAZEBO_PLUGIN_PATH=$HOME/gazebo_car_plugin/build:$GAZEBO_PLUGIN_PATH

Then you can run gazebo.

    gazebo

And add model to gazebo. As soon you add model to simulator it starts to move. You can find this code [here](../src/plugins/gazebo_car_plugin)
