import math
import numpy as np
from math import acos, asin, atan2, cos, pi, radians, sin, sqrt
def from_euler(roll, pitch, yaw):
    
    cp = cos(pitch)
    sp = sin(pitch)
    sr = sin(roll)
    cr = cos(roll)
    sy = sin(yaw)
    cy = cos(yaw)
    
    HMatrix = np.zeros((3,3), np.float32)
    HMatrix[0][0] = cp * cy
    HMatrix[0][1] = (sr * sp * cy) - (cr * sy)
    HMatrix[0][2] = (cr * sp * cy) + (sr * sy)
    HMatrix[1][0] = cp * sy
    HMatrix[1][1] = (sr * sp * sy) + (cr * cy)
    HMatrix[1][2] = (cr * sp * sy) - (sr * cy)
    HMatrix[2][0] = -sp
    HMatrix[2][1] = sr * cp
    HMatrix[2][2] = cr * cp
    return HMatrix
    
def Quaternion2EulerAngles(w, x, y, z):
    PIby2 = (math.pi / 2)

    # roll : rotation in x axis
    roll_x = float(2 * (w * x + y * z))
    roll_y = float(1 - 2 * (x * x + y * y))
    roll = math.atan2(roll_x, roll_y);

    # pitch : rotation in y axis
    pitch_var = float(2 * (w * y - z * x))
    if (abs(pitch_var) >= 1):
	#In the event of out of range -> use 90 degrees
        pitch = math.copysign(PIby2, pitch_var);
    else:
        pitch = math.asin(pitch_var);

    # yaw : rotation in z-axis
    yaw_x = 2 * (w * z + x * y);
    yaw_y = 1 - 2 * (y * y + z * z);
    yaw = math.atan2(yaw_x, yaw_y);

    print("roll     ( radians )  : "+str(roll))
    print("pitch    ( radians )  : "+str(pitch))
    print("yaw      ( radians )  : "+str(yaw))

    roll_  = math.degrees(roll)
    pitch_ = math.degrees(pitch)
    yaw_   = math.degrees(yaw)

    print("roll     ( degrees )  : "+str(roll_))
    print("pitch    ( degrees )  : "+str(pitch_))
    print("yaw      ( degrees )  : "+str(yaw_))

    return roll, pitch, yaw
    
def q2matrix(w, x, y, z):
  r, p, y = Quaternion2EulerAngles(z, w, x, y) #stupid but need
  return from_euler(r, p, y)
  
q2matrix(0.513, -0.471, 0.498, 0.517)

inv = from_euler(math.radians(-87.81), math.radians(-1.17), math.radians(-86.36))
translation = [0.528, 0.077, -0.482]
inv = np.c_[inv, translation]
inv = np.vstack([inv, [0, 0, 0, 1]])
print(inv)
A = np.linalg.inv(inv) 
print(A)
for i in range(4):
  for j in range(4):
    print(round(A[i][j], 4), ', ', end='', sep='')
  print()
