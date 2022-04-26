Để launch được 2 con turtlebot3: đặt file two_robot.launch vào trong turtlebot3_gazebo/launch. Chạy:
```
roslaunch turtlebot3_gazebo two_robot.launch
```
___
Ban đầu em định thêm một tb thứ 2 vào map là một con follower để cho nó tự động đi theo con còn lại. Để làm thế thì cần install 2 package là 
turtlebot3_applications và turtlebot3_applications_msgs từ github (https://github.com/ROBOTIS-GIT/turtlebot3_applications). Để build được 2 package này thì cần install cả ar-track-alvar. 
ros-noetic không có sẵn cái đấy, đã clone về từ github (https://github.com/machinekoder/ar_track_alvar/tree/noetic-devel) bản noetic-devel nhưng vẫn không build được (em không fix được)

Sau đó vì không biết làm tiếp nên em chuyển qua hướng khác.
Là launch ra 2 con tb luôn và dùng teleop để điều khiển 2 con, với mỗi con tb thì sẽ tạo ra 1 map tương ứng, merge_map để tạo ra 1 map chung 
(giống như bài hướng dẫn SLAM & Navigation 2 tuần trước). Kết quả là vẫn không xong.


## References:

https://learn.turtlebot.com/

https://emanual.robotis.com/docs/en/platform/turtlebot3/basic_examples/#turtlebot-follower-demo

https://www.theconstructsim.com/ros-qa-130-how-to-launch-multiple-robots-in-gazebo-simulator/

https://wiki.nps.edu/pages/viewpage.action?pageId=1018462212 - (nps.edu)Multiple turtlebot3 mapping in gazebo

https://github.com/bbingham-nps/turtlebot3_nps

https://github.com/ROBOTIS-GIT/turtlebot3_applications

https://github.com/ros-perception/ar_track_alvar/issues/82#issuecomment-893859329
