#!/usr/bin/env python

import math

file_name = "../models/test1_camera/test1_camera.sdf"

data = """<?xml version="1.0" ?>
<sdf version="1.6">
  <actor name="test1_camera">
    <include>
        <uri>model://camera</uri>
        <pose>0 0 0 0 1.570796 0</pose>
    </include>
    <script>
        <loop>true</loop>
        <delay_start>0.00000</delay_start>
        <trajectory id="0" type="square">
            """

end_file = """
        </trajectory>
    </script>
  </actor>
</sdf>"""

z_sq = [3, 3, 3, 3, 3]
x_sq = [1, 1, -1, -1, 1]
y_sq = [1, -1, -1, 1, 1]
time_i = 0

for i in range(len(x_sq)):
    wp_str = """<waypoint>
                <time>%.2f</time>
                <pose>%.2f %.2f %.2f 0 0 0</pose>
            </waypoint>
            """%(time_i,x_sq[i], y_sq[i], z_sq[i])
    time_i += 3
    data += wp_str

data = data + end_file

with open(file_name, "w") as f:
    f.write(data)