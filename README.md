# Boetverse

To run the robot model, you need to first source the package and then put this in terminal

**roslaunch boetverse urdf_visualize.launch**

After that, the gazebo gui as well as the controlling gui should appear and look like this

![image](https://github.com/user-attachments/assets/0c77626a-5dc5-4d75-ba7d-197f9ad081d7)

The robot is not much good. So it will move slow. I kept the movement less so that it doesnt fall :')

Also to see the robot model only, put this in the terminal

**roslaunch boetverse show_model.launch**

then after setting 'robot_body' in Fixed Frame and adding RobotModel, it should look like this

![image](https://github.com/user-attachments/assets/5fc608df-ee89-4600-a548-a858c9df0704)
