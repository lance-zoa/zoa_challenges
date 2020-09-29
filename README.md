# ZOA Robotics Challenges
This repository has a set of challenges for prospective interns to complete. We use it to find out more about
you, where your skills and interests lie and to assess if you would be a good fit for the internship role.

These challenges are designed, on purpose, to be more open ended than other 'coding' challenges you might
have seen. We want to see how you deal with a more open problem and if you can use the resources available
to come up with a solution.

## The Challenges:
The following challenges are available for you to try; please read through the description for each and
decide which one or ones you would like do.

1.  Introduction to PyBullet:	(You'll use: Python3)

	PyBullet is one of the tools we use to simulate our robot and test our control algorithms before
	deploying to the physical robot. Its a great physics engine with a decent renderer to boot. This
	challenge involves setting up a PyBullet environment to load and place 3D models into a virtual
	world.

	Specifically:
	*  Pick some 3D models (as \*.obj or \*.stl files) convert them into a format compatible with
	   PyBullet (\*.urdf) (one or two models is more than enought).
	*  Use the provide script that creates a virtual world in PyBullet with a floor as a starting point.
	*  Write a script that place each 3D model in the virtual world at any location with any orientation
	   (relative to the origin and floor).
	*  (Bonus Points) Make the models able to interact/collide with each other and demonstrate it.

	Resources you'll need:
	* [PyBullet Documentation](https://pybullet.org/wordpress/index.php/forum-2/)
	* [Turbosquid](https://www.turbosquid.com/) has lots of free 3D models to choose from.
	* Search for projects online (github/gitlab/etc) that use PyBullet for guidance.

2.  Data Visualisation:	 (You'll use: Python3 or Javascript)

	Data is critical to the development process. How do we know our new algorithm is better than its
	predecessor? Why is the robot not walking as expected? These are just some of questions we ask
	ourselves all the time and we have to go to the data logs for the answers. You're going to get a
	taste of what we have to do in this challenge. 
	
	Specifically:
	*  You'll get a data log from the robot as a CSV file. The data will contain position, orientation,
	   velocity and angular velocity.
	*  Create a data visualisation tool that can parse an input data log and display graphs of the
	   robot's state over time.
	*  Do some analysis on the graphs - can you tell if the robot is walking or trotting on the spot,
	   what direction is it moving in, is it turning?
	*  Using the provider tool that replays a data log back convert the data visualisation tool
	   to update the plots in real-time. Implement the real-time plotting to plot every data point
	   received until the current time and to only plot the data points in a finite time window.
	*  (Bonus Points) Can you make the graphs renderable to a browser? (You will probably need to
	   use Javascript/HTML for this)

	Resources you'll need:
	* [smoothie.js](http://smoothiecharts.org/)
	* [plotly](https://plotly.com/nodejs/)
	* [matplotlib](https://matplotlib.org/)

3.  PID Control: (You'll use: Python3 | Some control systems theory)

	PID controllers are a fundamental control architecture and they tend to be used broadly in engineering.
	In fact we use them in certain parts of our robot! Being able to design and build control systems is
	essential for work in robotics and this challenge is setup to test your ability to build and
	implement a simple PID controller for controlling the speed of a motor. 

	Specifically:
	*  You have been provided with a numerical model that implements a basic motor, you need to design a
	   PID controller to control the speed of the motor.
	*  We want to see you explore the dynamics of the provided motor model: plot the impulse and step
	   responses of the motor. What do you notice about the model?
	*  Design a PID controller that will have a response time of 1s and a maximum overshoot of 5%.
	*  Implement the PID controller in a digital form (think about how the classical control theory
	   changes once time becomes discrete).
	*  Generate plots that demonstrate the performance of your controller. Critically evaluate this
	   performance.
	*  (Bonus Points) Describe some other options we could have used for motor control if this motor
	   is part of a robot arm working close to people and/or other equipment.
	
	Resources you'll need:
	* [PID Overview](https://m.eet.com/media/1112634/f-wescot.pdf)
	* [matplotlib](https://matplotlib.org/)

4.  Robot Kinematics: (You'll use: Python3 | rigid body kinematics)

	Modelling the kinematics of robot limbs is important as it allows control algorithms developed in
	the Cartesian space to have their outputs mapped to the actuators available. For example, mapping
	a force required into torques at all the joints in a robot arm. This challenge will explore a simple
	2D robotic arm with a shoulder and elbow joint actuated by direct drive motors. A diagram of the
	robotic arm is given:

	![Robot Arm](https://github.com/lance-zoa/zoa_challenges/blob/main/robotic_arm_2d.png)

	Specifically:
	*  Given a diagram of the robotic arm find the following:
		- Position of the end-effector/hand in the reference co-ordinate system.
		- Velocity and acceleration of the end-effector/hand.
	*  Plot the position, velocity and acceleration of the end-effector/hand assuming the shoulder and elbow
	   joint angles are proportional to `sin(wt)` where `w = 0.25 rad/s` and `0.1 rad/s` respectively.
	*  Play around with different equations for the joint angles to get a feel for the kinematics.
	*  Using the kinematic equations you derived previously derive the Jacobian for the system.
	*  Given a reaction force, `F = 15j N`, acting on the end-effector/hand, compute the torque output of
	   each joint motor to maintain equilibrium.
	*  (Bonus Points) Plot/render a real-time 2D visualisation of the robotic arm moving under some periodic
	    equations for the joint angles with respect to time.

	Resources you'll need:
	* [Jacobian](https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant)
	* [matplotlib](https://matplotlib.org/)

	
