import math
import scipy

# ----------------    DIA 2 ----------------------

# constants
g = 9.81 # m / s^2
μ = 0.02 # friction coefficient has no units

# assumptions
m = 50 # kg
F_push_horizontal = 100 # Push force is kg * m / s^2
F_push_vertical = 300 # Push force is kg * m / s^2


# μ = F/N, where F is the frictional force and N is the normal force.
N = m * g # Normal force is kg * m / s^2
F_r = μ * N # Friction force is kg * m / s^2

# momento 0 (time 0) - The ice skater is standing still on the ice, right before they push off with their skate
v_x_m0 = 0 # velocidad horizontal (x) initial momento 0 (m / s)
v_y_m0 = 0 # velocidad vertical (y) initial momento 0 (m / s)
t_m0 = 0 # tiempo initial momento 0 (s)
x_m0 = 0
y_m0 = 0
F_x_m0 = F_push_horizontal - F_r # Total force acting on your body
F_y_m0 = 0 # Total force acting on your body vertically

# momento 1 (time 1) - The ice skater is gliding forward on the ice, and is about to jump
t_m1 = 3.0 # time since moment 0
v_y_m1 = 0 # velocidad vertical initial momento 0 (m / s)
y_m1 = 0

# F = m*a and v = a*t
a_x_m1 = (F_x_m0 / m) # acceleration horizontal (x) momento 1 (m / s^2)
v_x_m1 = a_x_m1*t_m1 # velocidad horizontal (x) momento 1 (m / s)
x_m1 = v_x_m1*t_m1 # position horizontal (x) momento 1 (m)

F_x_m1 = F_x_m0
F_y_m1 = F_push_vertical


# momento 2 (time 2) - the ice skater is at the height of their jump

# momento 3 (time 3) - the ice skater lands on the ice

# f_total = m*a
# a = f / m
a_m1 = F_total / m # acceleration horizontal m / s^2

# v = v0 + at
v_f_m1 = v_0_m1 + a_m1 * (t_f_m1 - t_0_m1)
print(f'final velocity at m1 {v_f_m1}')

# maximum RPM for figure skaters is 342 RPM (revolutions per minute)
# freq = 

# momento 2
t_0_m2 = t_f_m1
v_0_m2 = v_f_m1
θ = math.radians(45) # 45 degrees in radians
vueltas = 5
t_f_m2 = t_0_m2

# F_s = 
# v_f_m2 = 


# ----------------    DIA 1 ----------------------
 
 # this is a comment

 # this 
 # is  
 # a
 # comment

'''
 this 
 is  
 a
 comment
'''

'''
# what are the variables for ice skating physics?
 
# mass in KG
 
def time_in_air(mass = 50, jump_force = 100, jump_angle = math.radians(45)):
    initial_momentum = float(jump_force) * float(mass)
    g = 9.81
    time = (2.0 * initial_momentum * math.sin(jump_angle)) / g
    return time
 
my_mass = input('What is your mass? (type in and hit enter)')
print(f"Your mass is {my_mass}")
 
 
# my_jump_angle = input('What is your jump angle? (type in and hit enter)')
# is_in_radians = input('Is your jump angle in radians? (y/n)')
 
# if is_in_radians == 'y':
#    print('Jump angle is already in radians')
#    my_jump_angle = my_jump_angle
#else:
#    print('Jump angle is in degrees, converting to radians ...')
    # Convert jump_angle from degrees to radians
#    my_jump_angle = math.radians(float(my_jump_angle))
 
total_time = time_in_air(mass=my_mass) # jump_angle=my_jump_angle)
 
# Will limit the print output to 2 decimal places
print("Total time in the air is {:.2f}".format(total_time))
 
# Datatypes = types of Datatypes
# int => integer => 1
# float = 1.0
# string = "asdfasdfasdf"
'''
