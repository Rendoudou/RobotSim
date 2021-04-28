# RobotSim V1.7.3
## 一、[Brief Usage]
### Step 1 编译
#### mkdir catkin_ws_robot_sim
#### cd catkin_ws_robot_sim
#### mkdir src
#### cd src
#### git clone
#### cd ..
#### cd ..
#### catkin_make
### Step 2 启动roscore
#### bash
#### roscore 
### Step 3 启动建图
#### bash
#### cd catkin_ws_robot_sim
#### source devel/setup.bash
#### roslaunch robot_sim robot_mapping.launch
### Step 4 启动键盘控制（可选）
#### bash
#### cd catkin_ws_robot_sim
#### source devel/setup.bash
#### rosrun robot_sim teleop_twist_keyboard
### ...
## 二、[See record.txt]