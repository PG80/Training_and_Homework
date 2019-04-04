# 2019_01_15_TASK_6_PG_HYDROTESTER_process_with_standard_logic

#Hydrotester is a metallurgical equipment that is used for test of pipes under high pressure.
#Hydro tester consists of several stations for perform pipe testing.

#Standart_time_of_process_flow (seconds)
Step_1_Load_the_pipe_by_over_head_crane_to_inlet_area = 10
Step_2_Relocation_of_pipe_to_entry_station = 10
Step_3_Entry_station_positioning = 10
Step_3_1_Entry_station_the_pipe_eligned_accoding_to_cetre_of_filling_head = 10
Step_3_2_Entry_station_the_pipe_connection_of_two_filling_heads = 10
Step_3_3_Entry_station_the_pipe_flashed_by_emulsion = 10
Step_3_4_Entry_station_the_pipe_disconnection_of_two_filling_heads = 10
Step_3_5_Entry_station_the_pipe_length_measured = 10
Step_4_The_pipe_transferred_into_the_testing_station = 10
Step_4_1_The_pipe_prepositioning = 10
Step_5_1_The_filling_head_is_positioned_onto_the_pipe_end = 10
Step_5_2_The_venting_head_is_positioned_onto_testing_position = 10
Step_5_3_The_tube_clamping_devices_are_clouse = 10
Step_5_4_The_pipe_sealed_at_both_ends = 10
Step_5_5_The_has_been_filled_by_water = 10
Step_5_6_The_pipe_test_pressure_by_intensifier = 10
Step_5_7_The_test_pressure_is_held_for_the_set_pressure_holding_time = 10
Step_5_8_the_venting_head_is_open = 10
Step_5_9_emptying_the_pipe = 10
Step_5_10_The_tube_clamping_devices_are_opened = 10
Step_6_1_The_pipe_relocation_water_drainage_station = 10
Step_6_2_The_drainage_of_water = 10
Step_7_The_pipe_relocation_to_drifter = 10
Step_8_Drifter_process = 10
Step_9_Relocation_of_pipe_towards_the_machine_outlet = 10

#INITIAL_DATA
#pipe_outer_diameter_mm
#pipe_wall_thickness_mm
#pipe_length_max_mm

The_outer_diameter_of_pipe_and_wall_thickness = {
    '139.70': '10.54',
    '168.28': '12.06',
    '177.80': '12.65',
    '193.68': '12.70',
    '219.08': '14.15',
    '244.48': '15.11',
    '273.05': '15.11',
    '298.45': '15.11',
    '323.90': '25.40',
    '339.72': '15.11',
    '365.12': '25.40',
}

The_outer_diameter_of_pipe_and_length = {
    '139.70': '12000',
    '168.28': '12000',
    '177.80': '12300',
    '193.68': '12300',
    '219.08': '10800',
    '244.48': '12300',
    '273.05': '12300',
    '298.45': '12300',
    '323.90': '5100',
    '339.72': '11400',
    '365.12': '4500',
}

print ('Diameter_139.70', 'wall_thickness_', (The_outer_diameter_of_pipe_and_wall_thickness['139.70']), 'length_', (The_outer_diameter_of_pipe_and_length['139.70']))
print ('Diameter_168.28', 'wall_thickness_', (The_outer_diameter_of_pipe_and_wall_thickness['168.28']), 'length_', (The_outer_diameter_of_pipe_and_length['168.28']))
print ('Diameter_177.80', 'wall_thickness_', (The_outer_diameter_of_pipe_and_wall_thickness['177.80']), 'length_', (The_outer_diameter_of_pipe_and_length['177.80']))
print ('Diameter_193.68', 'wall_thickness_', (The_outer_diameter_of_pipe_and_wall_thickness['193.68']), 'length_', (The_outer_diameter_of_pipe_and_length['193.68']))
print ('Diameter_219.08', 'wall_thickness_', (The_outer_diameter_of_pipe_and_wall_thickness['219.08']), 'length_', (The_outer_diameter_of_pipe_and_length['219.08']))
print ('Diameter_244.48', 'wall_thickness_', (The_outer_diameter_of_pipe_and_wall_thickness['244.48']), 'length_', (The_outer_diameter_of_pipe_and_length['244.48']))
print ('Diameter_273.05', 'wall_thickness_', (The_outer_diameter_of_pipe_and_wall_thickness['273.05']), 'length_', (The_outer_diameter_of_pipe_and_length['273.05']))
print ('Diameter_298.45', 'wall_thickness_', (The_outer_diameter_of_pipe_and_wall_thickness['298.45']), 'length_', (The_outer_diameter_of_pipe_and_length['298.45']))
print ('Diameter_323.90', 'wall_thickness_', (The_outer_diameter_of_pipe_and_wall_thickness['323.90']), 'length_', (The_outer_diameter_of_pipe_and_length['323.90']))
print ('Diameter_339.72', 'wall_thickness_', (The_outer_diameter_of_pipe_and_wall_thickness['339.72']), 'length_', (The_outer_diameter_of_pipe_and_length['339.72']))
print ('Diameter_365.12', 'wall_thickness_', (The_outer_diameter_of_pipe_and_wall_thickness['365.12']), 'length_', (The_outer_diameter_of_pipe_and_length['365.12']))


#Requarements
#pipe_value_of_the_hydraulic_pressure_test_on_the_API5CT_MPa
#pipe_value_of_the_hydraulic_pressure_test_on_the_API5L_MPa
#pipe_value_of_the_hydraulic_pressure_test_on_the_EN10216_MPa
#pipe_holding_time
# Данные и расчеты на стадии разработки )))
#maximum_pressure_according_to_API_5CT_and_Q125 == 2 * 0.8 * 862 * (The_outer_diameter_of_pipe_and_wall_thickness['139.70']) / 139.70



class General_Hydrotester_process:
    The_signal_from_the_station_The_pipe_is_ready_for_relocation = 0.1
    The_pipe_is_relocated_from_previous_station = 6
    The_pipe_is_pisitioning_on_the_place = 2
    The_prosess_time = 0
    The_signal_of_the_end_of_operation = 0.1
    name = 'Step_0'
    print(name)

    def __init__(self, The_signal_from_the_station_The_pipe_is_ready_for_relocation, The_pipe_is_relocated_from_previous_station, The_pipe_is_pisitioning_on_the_place, The_prosess_time, The_signal_of_the_end_of_operation=''):
        self.The_signal_from_the_station_The_pipe_is_ready_for_relocation = The_signal_from_the_station_The_pipe_is_ready_for_relocation
        self.The_pipe_is_relocated_from_previous_station = The_pipe_is_relocated_from_previous_station
        self.The_pipe_is_pisitioning_on_the_place = The_pipe_is_pisitioning_on_the_place
        self.The_prosess_time = The_prosess_time
        self.The_signal_of_the_end_of_operation = The_signal_of_the_end_of_operation

    def get_of_process_time(self, The_signal_from_the_station_The_pipe_is_ready_for_relocation, The_pipe_is_relocated_from_previous_station, The_pipe_is_pisitioning_on_the_place, The_prosess_time, The_signal_of_the_end_of_operation):
        print(self.get_of_process_time)
        time_for_one_step = self.The_signal_from_the_station_The_pipe_is_ready_for_relocation + self.The_pipe_is_relocated_from_previous_station + self.The_pipe_is_pisitioning_on_the_place + self.The_prosess_time + self.The_signal_of_the_end_of_operation
        print('time_for_one_step')
        return self.The_signal_from_the_station_The_pipe_is_ready_for_relocation + self.The_pipe_is_relocated_from_previous_station + self.The_pipe_is_pisitioning_on_the_place + self.The_prosess_time + self.The_signal_of_the_end_of_operation


#ДОРАБОТАТЬ!!!!!!!!!!!!!!!!!!!!!!!!!!
#транспортирование
#остановка
#фиксирование
#выполнение операции
#передача сигнала

#class Step_11 (General_Hydrotester_process):
#    pass

#Step_11_total_time = Step_11(132, 'Step_11_total_time')
#print(Step_11_total_time.get_of_process_time())



class Step_1 (General_Hydrotester_process):
    process_time_for_operation = 123
    name = 'Step_1'
    description = '11111111111'
    print(name)

    def __init__(self, process_time_for_operation, name, description=''):
        self.process_time = process_time_for_operation
        self.name = name
        self.description = description

    def get_time_of_process_flow(self, process_relocation_of_pipe=2):
        print(self.name)
        return self.process_time + self.process_time * process_relocation_of_pipe

#Step_1_Load_the_pipe_by_over_head_crane_to_inlet_area = General_Hydrotester_process(Step_1_Load_the_pipe_by_over_head_crane_to_inlet_area, 'Step_1_Load_the_pipe_by_over_head_crane_to_inlet_area')
#print(Step_1_Load_the_pipe_by_over_head_crane_to_inlet_area.get_time_of_process_flow())






class Step_2 (General_Hydrotester_process):
    process_time_for_operation = 123
    name = 'Step_2'
    description = '2222222222222'
    print(name)

    def __init__(self, process_time_for_operation, name, description=''):
        self.process_time = process_time_for_operation
        self.name = name
        self.description = description

    def get_time_of_process_flow(self, process_relocation_of_pipe=33333):
        print(self.name)
        return self.process_time + self.process_time * process_relocation_of_pipe

Step_2_Relocation_of_pipe_to_entry_station = General_Hydrotester_process(Step_2_Relocation_of_pipe_to_entry_station, 'Step_2_Relocation_of_pipe_to_entry_station')
print(Step_2_Relocation_of_pipe_to_entry_station.get_time_of_process_flow())


class Step_3 (General_Hydrotester_process):
    process_time_for_operation = 123
    name = 'Step_3'
    description = '333333333333'
    print(name)

    def __init__(self, process_time_for_operation, name, description=''):
        self.process_time = process_time_for_operation
        self.name = name
        self.description = description

    def get_time_of_process_flow(self, process_relocation_of_pipe=3):
        print(self.name)
        return self.process_time + self.process_time * process_relocation_of_pipe

Step_3_1_Entry_station_the_pipe_eligned_accoding_to_cetre_of_filling_head = General_Hydrotester_process(Step_3_1_Entry_station_the_pipe_eligned_accoding_to_cetre_of_filling_head, 'Step_3_1_Entry_station_the_pipe_eligned_accoding_to_cetre_of_filling_head')
Step_3_2_Entry_station_the_pipe_connection_of_two_filling_heads = General_Hydrotester_process(Step_3_2_Entry_station_the_pipe_connection_of_two_filling_heads, 'Step_3_2_Entry_station_the_pipe_connection_of_two_filling_heads')
Step_3_3_Entry_station_the_pipe_flashed_by_emulsion = General_Hydrotester_process(Step_3_3_Entry_station_the_pipe_flashed_by_emulsion, 'Step_3_3_Entry_station_the_pipe_flashed_by_emulsion')
Step_3_4_Entry_station_the_pipe_disconnection_of_two_filling_heads = General_Hydrotester_process(Step_3_4_Entry_station_the_pipe_disconnection_of_two_filling_heads, 'Step_3_4_Entry_station_the_pipe_disconnection_of_two_filling_heads')
Step_3_5_Entry_station_the_pipe_length_measured = General_Hydrotester_process(Step_3_5_Entry_station_the_pipe_length_measured, 'Step_3_5_Entry_station_the_pipe_length_measured')
print(Step_3_1_Entry_station_the_pipe_eligned_accoding_to_cetre_of_filling_head.get_time_of_process_flow())
print(Step_3_2_Entry_station_the_pipe_connection_of_two_filling_heads.get_time_of_process_flow())
print(Step_3_3_Entry_station_the_pipe_flashed_by_emulsion.get_time_of_process_flow())
print(Step_3_4_Entry_station_the_pipe_disconnection_of_two_filling_heads.get_time_of_process_flow())
print(Step_3_5_Entry_station_the_pipe_length_measured.get_time_of_process_flow())


class Step_4 (General_Hydrotester_process):
    process_time_for_operation = 123
    name = 'Step_4'
    description = '4444444444'
    print(name)

    def __init__(self, process_time_for_operation, name, description=''):
        self.process_time = process_time_for_operation
        self.name = name
        self.description = description

    def get_time_of_process_flow(self, process_relocation_of_pipe=444444):
        print(self.name)
        return self.process_time + self.process_time * process_relocation_of_pipe

Step_4_The_pipe_transferred_into_the_testing_station = General_Hydrotester_process(Step_4_The_pipe_transferred_into_the_testing_station, 'Step_4_The_pipe_transferred_into_the_testing_station')
Step_4_1_The_pipe_prepisitioning = General_Hydrotester_process(Step_4_1_The_pipe_prepositioning, 'Step_4_1_The_pipe_prepisitioning')
print(Step_4_The_pipe_transferred_into_the_testing_station.get_time_of_process_flow())
print(Step_4_The_pipe_transferred_into_the_testing_station.get_time_of_process_flow())


class Step_5 (General_Hydrotester_process):
    process_time_for_operation = 123
    name = 'Step_5'
    description = '55555555'
    print(name)

    def __init__(self, process_time_for_operation, name, description=''):
        self.process_time = process_time_for_operation
        self.name = name
        self.description = description

    def get_time_of_process_flow(self, process_relocation_of_pipe=5):
        print(self.name)
        return self.process_time + self.process_time * process_relocation_of_pipe

Step_5_1_The_filling_head_is_positioned_onto_the_pipe_end = General_Hydrotester_process(Step_5_1_The_filling_head_is_positioned_onto_the_pipe_end, 'Step_5_1_The_filling_head_is_positioned_onto_the_pipe_end')
Step_5_2_The_venting_head_is_positioned_onto_testing_position = General_Hydrotester_process(Step_5_2_The_venting_head_is_positioned_onto_testing_position, 'Step_5_2_The_venting_head_is_positioned_onto_testing_position')
Step_5_3_The_tube_clamping_devices_are_clouse = General_Hydrotester_process(Step_5_3_The_tube_clamping_devices_are_clouse, 'Step_5_3_The_tube_clamping_devices_are_clouse')
Step_5_4_The_pipe_sealed_at_both_ends = General_Hydrotester_process(Step_5_4_The_pipe_sealed_at_both_ends, 'Step_5_4_The_pipe_sealed_at_both_ends')
Step_5_5_The_has_been_filled_by_water = General_Hydrotester_process(Step_5_5_The_has_been_filled_by_water, 'Step_5_5_The_has_been_filled_by_water')
Step_5_6_The_pipe_test_pressure_by_intensifier = General_Hydrotester_process(Step_5_6_The_pipe_test_pressure_by_intensifier, 'Step_5_6_The_pipe_test_pressure_by_intensifier')
Step_5_7_The_test_pressure_is_held_for_the_set_pressure_holding_time = General_Hydrotester_process(Step_5_7_The_test_pressure_is_held_for_the_set_pressure_holding_time, 'Step_5_7_The_test_pressure_is_held_for_the_set_pressure_holding_time')
Step_5_8_the_venting_head_is_open = General_Hydrotester_process(Step_5_8_the_venting_head_is_open, 'Step_5_8_the_venting_head_is_open')
Step_5_9_emptying_the_pipe = General_Hydrotester_process(Step_5_9_emptying_the_pipe, 'Step_5_9_emptying_the_pipe')
Step_5_10_The_tube_clamping_devices_are_opened = General_Hydrotester_process(Step_5_10_The_tube_clamping_devices_are_opened, 'Step_5_10_The_tube_clamping_devices_are_opened')
print(Step_5_1_The_filling_head_is_positioned_onto_the_pipe_end.get_time_of_process_flow())
print(Step_5_2_The_venting_head_is_positioned_onto_testing_position.get_time_of_process_flow())
print(Step_5_3_The_tube_clamping_devices_are_clouse.get_time_of_process_flow())
print(Step_5_4_The_pipe_sealed_at_both_ends.get_time_of_process_flow())
print(Step_5_5_The_has_been_filled_by_water.get_time_of_process_flow())
print(Step_5_6_The_pipe_test_pressure_by_intensifier.get_time_of_process_flow())
print(Step_5_7_The_test_pressure_is_held_for_the_set_pressure_holding_time.get_time_of_process_flow())
print(Step_5_8_the_venting_head_is_open.get_time_of_process_flow())
print(Step_5_9_emptying_the_pipe.get_time_of_process_flow())
print(Step_5_10_The_tube_clamping_devices_are_opened.get_time_of_process_flow())


class Step_6 (General_Hydrotester_process):
    process_time_for_operation = 123
    name = 'Step_6'
    description = '6666666666666'
    print(name)

    def __init__(self, process_time_for_operation, name, description=''):
        self.process_time = process_time_for_operation
        self.name = name
        self.description = description

    def get_time_of_process_flow(self, process_relocation_of_pipe=5):
        print(self.name)
        return self.process_time + self.process_time * process_relocation_of_pipe

Step_6_1_The_pipe_relocation_water_drainage_station = General_Hydrotester_process(Step_6_1_The_pipe_relocation_water_drainage_station, 'Step_6_1_The_pipe_relocation_water_drainage_station')
Step_6_2_The_drainage_of_water = General_Hydrotester_process(Step_6_2_The_drainage_of_water, 'Step_6_2_The_drainage_of_water')
print(Step_6_1_The_pipe_relocation_water_drainage_station.get_time_of_process_flow())
print(Step_6_2_The_drainage_of_water.get_time_of_process_flow())


class Step_7 (General_Hydrotester_process):
    process_time_for_operation = 123
    name = 'Step_7'
    description = '77777777_'
    print(name)

    def __init__(self, process_time_for_operation, name, description=''):
        self.process_time = process_time_for_operation
        self.name = name
        self.description = description

    def get_time_of_process_flow(self, process_relocation_of_pipe=5):
        print(self.name)
        return self.process_time + self.process_time * process_relocation_of_pipe

    def total_get_time_of_process_flow(self, process_relocation_of_pipe=25):
        print('sum of (sum self.name)')
        return self.process_time + self.process_time

Step_7_The_pipe_relocation_to_drifter = General_Hydrotester_process(Step_7_The_pipe_relocation_to_drifter, 'Step_7_The_pipe_relocation_to_drifter')
print(Step_7_The_pipe_relocation_to_drifter.get_time_of_process_flow())


class Step_8 (General_Hydrotester_process):
    process_time_for_operation = 123
    name = 'Step_8'
    description = '8888888888'
    print(name)

    def __init__(self, process_time_for_operation, name, description=''):
        self.process_time = process_time_for_operation
        self.name = name
        self.description = description

    def get_time_of_process_flow(self, process_relocation_of_pipe=5):
        print(self.name)
        return self.process_time + self.process_time * process_relocation_of_pipe

Step_8_Drifter_process = General_Hydrotester_process(Step_8_Drifter_process, 'Step_8_Drifter_process')
print(Step_8_Drifter_process.get_time_of_process_flow())


class Step_9 (General_Hydrotester_process):
    process_time_for_operation = 123
    name = 'Step_9'
    description = '99999999999999'
    print(name)

    def __init__(self, process_time_for_operation, name, description=''):
        self.process_time = process_time_for_operation
        self.name = name
        self.description = description

    def get_time_of_process_flow(self, process_relocation_of_pipe=5):
        print(self.name)
        return self.process_time + self.process_time * process_relocation_of_pipe

Step_9_Relocation_of_pipe_towards_the_machine_outlet = General_Hydrotester_process(Step_9_Relocation_of_pipe_towards_the_machine_outlet, 'Step_9_Relocation_of_pipe_towards_the_machine_outlet')
print(Step_9_Relocation_of_pipe_towards_the_machine_outlet.get_time_of_process_flow())
