from TIR_Parser import parse_tir_file


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


# C   =   b0   #Shape Factor
# D   =   Fz*(b1*Fz+b2) # Peak Factor
# BCD =   (b3*Fz**2+b4*Fz)*exp(-b5*Fz)   
# B   =   BCD/(C*D)
# E   =   (b6*Fz**2+b7*Fz+b8)*(1-b13*sign(slip+H))
# H   =   b9*Fz+b10
# V   =   b11*Fz+b12


# Fx   =   D * sin(C*atan(B-E(B-atan(B))))+V


# if 'OPERATING_CONDITIONS' in extracted_parameters:
#     operating_conditions = extracted_parameters['LONGITUDINAL_COEFFICIENTS']
#     inflpres = operating_conditions.get('PCX1')  # Example parameter extraction

#     # Do something with the extracted parameter value
#     print("Inflation Pressure:", inflpres)
# else:
#     print("OPERATING_CONDITIONS section not found in the .tir file.")
