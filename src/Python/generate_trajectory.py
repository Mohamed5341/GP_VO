#!/usr/bin/env python

import math

file_name = "../models/moving_camera/moving_camera.sdf"

data = """<?xml version="1.0" ?>
<sdf version="1.6">
  <actor name="moving_camera">
    <include>
        <uri>model://camera</uri>
        <pose>0 0 0 0 1.570796 0</pose>
    </include>
    <script>
        <loop>true</loop>
        <delay_start>2.00000</delay_start>
        <trajectory id="0" type="square">
            """

end_file = """
        </trajectory>
    </script>
  </actor>
</sdf>"""

num_of_points = 50

z_locations = [1, 1.66, 2, 2.33]
x = [math.cos(2*math.pi*i/num_of_points) for i in range(0, num_of_points)]
y = [0.7*math.sin(2*math.pi*i/num_of_points) for i in range(0, num_of_points)]

x.insert(0, 0)
y.insert(0, 0)

time_i = 0
js = [j*0.08 for j in [1, 5, 15, 20]]

i_z = 0

for z in z_locations:
    i_z += 1
    time_i += 2
    for j in js[len(js)-i_z::-1]:
        dx = x[0]*j
        dy = y[0]*j
        dz = z
        wp_str = """<waypoint>
                <time>%.2f</time>
                <pose>%.2f %.2f %.2f %.5f %.5f 0</pose>
            </waypoint>
            """%(time_i,x[0]*j, y[0]*j, z, -1*math.atan2(dy, dz), math.atan2(dx, dz))
        time_i += 3
        data += wp_str
        for i in range(1, num_of_points):
            dx = x[i]*j
            dy = y[i]*j
            dz = z
            wp_str = """<waypoint>
                    <time>%.2f</time>
                    <pose>%.2f %.2f %.2f %.5f %.5f 0</pose>
                </waypoint>
                """%(time_i,x[i]*j, y[i]*j, z, -1*math.atan2(dy, dz), math.atan2(dx, dz))
            time_i += 0.3
            data += wp_str
        for i in range(1, num_of_points):
            wp_str = """<waypoint>
                    <time>%.2f</time>
                    <pose>%.2f %.2f %.2f 0 0 0</pose>
                </waypoint>
                """%(time_i,x[i]*j, y[i]*j, z)
            time_i += 0.3
            data += wp_str

data = data + end_file

with open(file_name, "w") as f:
    f.write(data)