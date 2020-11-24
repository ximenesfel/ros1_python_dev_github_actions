FROM ros:melodic-ros-base

RUN echo "source /opt/ros/melodic/setup.bash" >> /root/.bashrc

RUN apt update && \
    apt install -y  ros-melodic-rospy-tutorials ros-melodic-genpy lcov python-coverage python-pip ros-melodic-code-coverage ros-melodic-roslint

RUN pip install --upgrade pip
RUN pip install pyyaml rospkg pylint --ignore-installed

RUN mkdir -p /root/catkin_ws/src
WORKDIR /root/catkin_ws
RUN /bin/bash -c '. /opt/ros/melodic/setup.bash; cd /root/catkin_ws; catkin_make -DENABLE_COVERAGE_TESTING=ON -DCMAKE_BUILD_TYPE=Debug'

RUN echo "source /root/catkin_ws/devel/setup.bash" >> /root/.bashrc \
    && /bin/bash -c "source /root/.bashrc"

WORKDIR /root