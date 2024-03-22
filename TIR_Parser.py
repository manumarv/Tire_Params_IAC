# Define a function to parse the .tir file and extract specific parameters
def parse_tir_file(file_path):
    parameters = {}

    with open(file_path, 'r') as file:
        current_section = None

        for line in file:
            line = line.strip()

            # Check if the line contains a section header
            if line.startswith('[') and line.endswith(']'):
                current_section = line[1:-1]
            elif current_section and '=' in line:
                # Extract parameter name and value
                split_line = line.split('=')
                param_name = split_line[0].strip()
                param_value = split_line[1].split()[0].strip()
                #param_value = '='.join(split_line[1:]).strip()
                # Store parameter in dictionary
                if current_section not in parameters:
                    parameters[current_section] = {}
                parameters[current_section][param_name] = param_value

    return parameters


# Specify the path to the .tir file
#file_path = '/home/mar/Tire_Params_IAC/Tir Files/2021021_Firestone_IAC_LF_B4112T_MF62_UM4 - extended.tir'
# Parse the .tir file and extract parameters
#extracted_parameters = parse_tir_file(file_path)

# Example: Access specific parameters
# if 'OPERATING_CONDITIONS' in extracted_parameters:
#     operating_conditions = extracted_parameters['OPERATING_CONDITIONS']
#     inflpres = operating_conditions.get('INFLPRES')  # Example parameter extraction

#     # Do something with the extracted parameter value
#     print("Inflation Pressure:", inflpres)
# else:
#     print("OPERATING_CONDITIONS section not found in the .tir file.")
