from TIR_Parser import parse_tir_file

import math 
#Longitudinal Force 

file_path = '/home/mar/Tire_Params_IAC/Tir Files/2021021_Firestone_IAC_LF_B4112T_MF62_UM4 - extended.tir'
# Parse the .tir file and extract parameters
extracted_parameters = parse_tir_file(file_path)


b0  =   float(extracted_parameters['LONGITUDINAL_COEFFICIENTS'].get('PCX1'))   # Shape Factor


b1  =   float(extracted_parameters['LONGITUDINAL_COEFFICIENTS'].get('PDX2'))    # Load influence on longitudinal fricttion coefficient

b2  =   float(extracted_parameters['LONGITUDINAL_COEFFICIENTS'].get('PDX1'))  # Longitudinal friction coefficient 



b3  =   float(extracted_parameters['LONGITUDINAL_COEFFICIENTS'].get('REX1')) # Curvature factor of stiffness/load
b4  =   float(extracted_parameters['LONGITUDINAL_COEFFICIENTS'].get('PKX1')) # Change of stiffness with slip	


b5  =    float(extracted_parameters['LONGITUDINAL_COEFFICIENTS'].get('PKX2'))# Change of progressivity of stiffness/load	
b6  =    float(extracted_parameters['LONGITUDINAL_COEFFICIENTS'].get('PEX3'))# Curvature change with load^2
b7  =    float(extracted_parameters['LONGITUDINAL_COEFFICIENTS'].get('PEX2'))# Curvature change with load
b8  =    float(extracted_parameters['LONGITUDINAL_COEFFICIENTS'].get('PEX4'))# Curvature Factor
b9  =    float(extracted_parameters['LONGITUDINAL_COEFFICIENTS'].get('PVX2'))# Load Influence on Horizontal Shift 
b10 =    float(extracted_parameters['LONGITUDINAL_COEFFICIENTS'].get('PHX1 '))# Horizontal shift	

b11 =    float(extracted_parameters['LONGITUDINAL_COEFFICIENTS'].get('PVX1'))# Vertical shift	
b12 =    float(extracted_parameters['LONGITUDINAL_COEFFICIENTS'].get('RHX1'))# Vertical shift at load = 0
b13 =    float(extracted_parameters['LONGITUDINAL_COEFFICIENTS'].get('RBX3 '))# Curvature shift	


Fz  =  float(extracted_parameters['VERTICAL'].get('FNOMIN'))

slip = 0.5 # slip ratio which can be a range from 0 to 1

C   =   b0   #Shape Factor
D   =   Fz*(b1*Fz+b2) # Peak Factor

BCD =   (b3*Fz**2+b4*Fz)*math.exp(-b5*Fz)  

B   =   BCD/(C*D)
H   =   b9*Fz+b10
E   =   (b6*Fz**2+b7*Fz+b8)*(1-b13*math.sign(slip+H))
V   =   b11*Fz+b12


Fx   =   D * math.sin(C*math.atan(B-E(B-math.atan(B))))+V


