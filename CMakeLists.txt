cmake_minimum_required(VERSION 3.16)
project(orbslam3)

# You should set the PYTHONPATH to your own python site-packages path
# set(ENV{PYTHONPATH} "/opt/ros/humble/lib/python3.10/site-packages")

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_SOURCE_DIR}/CMakeModules)

# Default to C++17 (required by rclcpp and Pangolin)
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(cv_bridge REQUIRED)
find_package(message_filters REQUIRED)
find_package(Eigen3 REQUIRED)
find_package(Pangolin REQUIRED)
find_package(ORB_SLAM3 REQUIRED)
find_package(OpenCV REQUIRED)

include_directories(
  include
  ${ORB_SLAM3_INCLUDE_DIRS}
  ${ORB_SLAM3_ROOT_DIR}/include
  ${ORB_SLAM3_ROOT_DIR}/include/CameraModels
  ${ORB_SLAM3_ROOT_DIR}/Thirdparty/Sophus
)

# ament_target_dependencies() was removed in Lyrical, link the targets directly
set(COMMON_LIBS
  rclcpp::rclcpp
  ${sensor_msgs_TARGETS}
  cv_bridge::cv_bridge
  ${ORB_SLAM3_LIBRARIES}
  ${Pangolin_LIBRARIES}
  ${OpenCV_LIBS}
  Eigen3::Eigen
)

add_executable(mono
  src/monocular/mono.cpp
  src/monocular/monocular-slam-node.cpp
)
target_link_libraries(mono ${COMMON_LIBS})

add_executable(rgbd
  src/rgbd/rgbd.cpp
  src/rgbd/rgbd-slam-node.cpp
)
target_link_libraries(rgbd ${COMMON_LIBS} message_filters::message_filters)

add_executable(stereo
  src/stereo/stereo.cpp
  src/stereo/stereo-slam-node.cpp
)
target_link_libraries(stereo ${COMMON_LIBS} message_filters::message_filters)

add_executable(stereo-inertial
  src/stereo-inertial/stereo-inertial.cpp
  src/stereo-inertial/stereo-inertial-node.cpp
)
target_link_libraries(stereo-inertial ${COMMON_LIBS})

install(TARGETS mono rgbd stereo stereo-inertial DESTINATION lib/${PROJECT_NAME})

# Install launch files.
#install(DIRECTORY launch config vocabulary
#  DESTINATION share/${PROJECT_NAME}/)

ament_package()

