# robot_sim

## [Brief Usage]
### step 1 编译
#### mkdir catkin_ws_robot_sim
#### cd catkin_ws_robot_sim
#### mkdir src
#### cd src
#### git clone
#### cd ..
#### cd ..
#### catkin_make
### step 2 启动roscore
#### bash
#### roscore 
### step 3 启动建图
#### bash
#### cd catkin_ws_robot_sim
#### source devel/setup.bash
#### roslaunch robot_sim robot_mapping.launch
### step 4 启动键盘控制
#### bash
#### cd catkin_ws_robot_sim
#### source devel/setup.bash
#### rosrun robot_sim teleop_twist_keyboard

## [See record.txt]