#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import tkinter as tk
import time

pub = rospy.Publisher('/r2d2_diff_drive_controller/cmd_vel', Twist, queue_size=10)

def stopbot():
	botmsg.config(text='bot is static now')
	pub.publish(Twist())

def nomeula():
	botmsg.config(text='Not enough meula')

def move_forward():
	if chkmeu(-1):
		return
	msg = Twist()
	msg.linear.x = 1
	pub.publish(msg)
	botmsg['text']="Bot is moving forward"
	root.after(1000, stopbot)

def move_backward():
	if chkmeu(-1):
		return
	msg = Twist()
	msg.linear.x = -1
	pub.publish(msg)
	botmsg['text']="Bot is moving backward"
	root.after(1000, stopbot)

def move_left():
	if chkmeu(-1):
		return
	msg = Twist()
	msg.angular.z = 1
	pub.publish(msg)
	botmsg['text']="Bot is rotating left"
	root.after(1000, stopbot)

def move_right():
	if chkmeu(-2):
		return
	msg = Twist()
	msg.angular.z = -1
	pub.publish(msg)
	botmsg['text']="Bot is rotating right"
	root.after(1000, stopbot)


def chkmeu(x=1):
	num=int(meulanum['text'])
	if((num+x)<0):
		botmsg.config(text='Not enough meulas')
		return True
	meulanum.config(text=str(num+x))
	return False


if __name__=="__main__":
	rospy.init_node("robot_control_app", anonymous = True)
	rate = rospy.Rate(10)
	# start_time=-1
	# if rospy.Time.now().to_sec() - start_time > 1:
	# 	pub.publish(Twist())
	# 	botmsg.config(text="Bot is static now")
	root = tk.Tk()

	root.title("Robot Control App")
	root.geometry("600x400")
	root.minsize(300,400)

	control= tk.Frame(root)
	control.grid(row=0,column=0, padx=10)

	button_forward = tk.Button(control, text="Forward", command=move_forward)
	button_forward.grid(row = 0, column = 1, padx=10, pady=10)

	button_backward = tk.Button(control, text="Backward", command=move_backward)
	button_backward.grid(row = 2, column = 1, padx=10, pady=10)

	button_left = tk.Button(control, text="Left", command=move_left)
	button_left.grid(row = 1, column = 0, padx=10, pady=10)

	button_right = tk.Button(control, text="Right", command=move_right)
	button_right.grid(row = 1, column = 2, padx=10, pady=10)

	meulas=tk.Frame(root,padx=50)
	meulas.grid(row=0,column=1)

	rem=tk.Frame(meulas)
	rem.grid(row=0,column=0)
	tk.Label(rem,text='Remaining Meulas:',highlightthickness=1,highlightbackground="black",highlightcolor="black").grid(row=0,column=0,padx=10)
	meulanum=tk.Label(rem,text="10",highlightthickness=1,highlightbackground="black",highlightcolor="black")
	meulanum.grid(row=0,column=1,padx=5)

	inc=tk.Button(meulas,text="Increase Meulas",command=chkmeu)
	inc.grid(row=1,column=0,pady=10)

	msg=tk.Frame(meulas)
	msg.grid(row=2,column=0,pady=30)
	tk.Label(msg,text='Message',padx=30,highlightthickness=1,highlightbackground="black",highlightcolor="black").grid(row=0,column=0)
	botmsg=tk.Label(msg,text='Bot is static now')
	botmsg.grid(row=1,column=0)

	root.mainloop()