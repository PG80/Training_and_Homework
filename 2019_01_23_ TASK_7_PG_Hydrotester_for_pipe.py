# 2019_01_22_TASK_6_PG_HYDROTESTER_process_with_standard_logic

#Baseline_data_for_calculations
Pipes_for_test_139 = {'Pipe_139.70': {'OD': '139.70', 'WT': '10.54', 'length': '12000'}}
Pipes_for_test_168 = {'Pipe_168.28': {'OD': '168.28', 'WT': '12.06', 'length': '12000'}}
Pipes_for_test_177 = {'Pipe_177.80': {'OD': '177.80', 'WT': '12.65', 'length': '12300'}}
Pipes_for_test_193 = {'Pipe_193.68': {'OD': '193.68', 'WT': '12.70', 'length': '12300'}}
Pipes_for_test_219 = {'Pipe_219.08': {'OD': '219.08', 'WT': '14.15', 'length': '10800'}}
Pipes_for_test_244 = {'Pipe_244.48': {'OD': '244.48', 'WT': '15.11', 'length': '12300'}}
Pipes_for_test_273 = {'Pipe_273.05': {'OD': '273.05', 'WT': '15.11', 'length': '12300'}}
Pipes_for_test_298 = {'Pipe_298.45': {'OD': '298.45', 'WT': '15.11', 'length': '12300'}}
Pipes_for_test_323 = {'Pipe_323.90': {'OD': '323.90', 'WT': '25.40', 'length': '05100'}}
Pipes_for_test_339 = {'Pipe_339.72': {'OD': '339.72', 'WT': '15.11', 'length': '11400'}}
Pipes_for_test_365 = {'Pipe_365.12': {'OD': '365.12', 'WT': '25.40', 'length': '04500'}}



class General_Hydrotester_process:

    print('Hydrotester is a metallurgical equipment that is use for test of pipes under high pressure')
    print('Hydrotester consists of several stations for perform pipe testing')

    userInput = input("What_pipe_diameter_do_you_want_to_test? Print_please_diameter 139, 168, 177, 193, 219, 244, 273, 298, 323, 339 or 365: ")

    if userInput == '139': productivity_coefficient_for_139_pipe = 1.25
    if userInput != '139': productivity_coefficient_for_139_pipe = 1
    if userInput == '168': productivity_coefficient_for_168_pipe = 1.20
    if userInput != '168': productivity_coefficient_for_168_pipe = 1
    if userInput == '177': productivity_coefficient_for_177_pipe = 1.15
    if userInput != '177': productivity_coefficient_for_177_pipe = 1
    if userInput == '193': productivity_coefficient_for_193_pipe = 1.10
    if userInput != '193': productivity_coefficient_for_193_pipe = 1
    if userInput == '219': productivity_coefficient_for_219_pipe = 1.05
    if userInput != '219': productivity_coefficient_for_219_pipe = 1
    if userInput == '244': productivity_coefficient_for_244_pipe = 0.95
    if userInput != '244': productivity_coefficient_for_244_pipe = 1
    if userInput == '273': productivity_coefficient_for_273_pipe = 0.90
    if userInput != '273': productivity_coefficient_for_273_pipe = 1
    if userInput == '298': productivity_coefficient_for_298_pipe = 0.85
    if userInput != '298': productivity_coefficient_for_298_pipe = 1
    if userInput == '323': productivity_coefficient_for_323_pipe = 0.80
    if userInput != '323': productivity_coefficient_for_323_pipe = 1
    if userInput == '339': productivity_coefficient_for_339_pipe = 0.75
    if userInput != '339': productivity_coefficient_for_339_pipe = 1
    if userInput == '365': productivity_coefficient_for_365_pipe = 0.70
    if userInput != '365': productivity_coefficient_for_365_pipe = 1
    if userInput == '377': productivity_coefficient_for_365_pipe = 1
    if userInput != '377': productivity_coefficient_for_365_pipe = 1
    productivity_coefficient_for_use = (
    productivity_coefficient_for_139_pipe * \
    productivity_coefficient_for_168_pipe * \
    productivity_coefficient_for_177_pipe * \
    productivity_coefficient_for_193_pipe * \
    productivity_coefficient_for_219_pipe * \
    productivity_coefficient_for_244_pipe * \
    productivity_coefficient_for_273_pipe * \
    productivity_coefficient_for_298_pipe * \
    productivity_coefficient_for_323_pipe * \
    productivity_coefficient_for_339_pipe * \
    productivity_coefficient_for_365_pipe)

    print('Pipe_outer_diameter_', (Pipes_for_test_139['Pipe_139.70']['OD']), '  Pipe_wall_thickness', (Pipes_for_test_139['Pipe_139.70']['WT']), '  Pipe_length', (Pipes_for_test_139['Pipe_139.70']['length']))
    print('Pipe_outer_diameter_', (Pipes_for_test_168['Pipe_168.28']['OD']), '  Pipe_wall_thickness', (Pipes_for_test_168['Pipe_168.28']['WT']), '  Pipe_length', (Pipes_for_test_168['Pipe_168.28']['length']))
    print('Pipe_outer_diameter_', (Pipes_for_test_177['Pipe_177.80']['OD']), '  Pipe_wall_thickness', (Pipes_for_test_177['Pipe_177.80']['WT']), '  Pipe_length', (Pipes_for_test_177['Pipe_177.80']['length']))
    print('Pipe_outer_diameter_', (Pipes_for_test_193['Pipe_193.68']['OD']), '  Pipe_wall_thickness', (Pipes_for_test_193['Pipe_193.68']['WT']), '  Pipe_length', (Pipes_for_test_193['Pipe_193.68']['length']))
    print('Pipe_outer_diameter_', (Pipes_for_test_219['Pipe_219.08']['OD']), '  Pipe_wall_thickness', (Pipes_for_test_219['Pipe_219.08']['WT']), '  Pipe_length', (Pipes_for_test_219['Pipe_219.08']['length']))
    print('Pipe_outer_diameter_', (Pipes_for_test_244['Pipe_244.48']['OD']), '  Pipe_wall_thickness', (Pipes_for_test_244['Pipe_244.48']['WT']), '  Pipe_length', (Pipes_for_test_244['Pipe_244.48']['length']))
    print('Pipe_outer_diameter_', (Pipes_for_test_273['Pipe_273.05']['OD']), '  Pipe_wall_thickness', (Pipes_for_test_273['Pipe_273.05']['WT']), '  Pipe_length', (Pipes_for_test_273['Pipe_273.05']['length']))
    print('Pipe_outer_diameter_', (Pipes_for_test_298['Pipe_298.45']['OD']), '  Pipe_wall_thickness', (Pipes_for_test_298['Pipe_298.45']['WT']), '  Pipe_length', (Pipes_for_test_298['Pipe_298.45']['length']))
    print('Pipe_outer_diameter_', (Pipes_for_test_323['Pipe_323.90']['OD']), '  Pipe_wall_thickness', (Pipes_for_test_323['Pipe_323.90']['WT']), '  Pipe_length', (Pipes_for_test_323['Pipe_323.90']['length']))
    print('Pipe_outer_diameter_', (Pipes_for_test_339['Pipe_339.72']['OD']), '  Pipe_wall_thickness', (Pipes_for_test_339['Pipe_339.72']['WT']), '  Pipe_length', (Pipes_for_test_339['Pipe_339.72']['length']))
    print('Pipe_outer_diameter_', (Pipes_for_test_365['Pipe_365.12']['OD']), '  Pipe_wall_thickness', (Pipes_for_test_365['Pipe_365.12']['WT']), '  Pipe_length', (Pipes_for_test_365['Pipe_365.12']['length']))

# for calculation of process_time_for_step
    The_signal_from_the_station_The_pipe_is_ready_for_relocation = 0.1
    The_pipe_is_relocated_from_previous_station = 6
    The_pipe_is_positioning_on_the_place = 2
    The_process_time = 0  #each station will have its own special time, some times not
    The_signal_of_the_end_of_operation = 0.1
#for calculation of pipe_pieces_per_hour
    Seconds_per_hour = 3600
    Pi = 3.14
    Transfer_coefficient_values_of_killogram_in_tons = 1000
# for calculation of tonns_per_hour ВОПРОС!!! Ка ксделать автоматический выбор трубы для дальнейшего расчета - нужна маленькая консультация )
    #сейчас считает только для 139 трубы
    Pipes_for_test_139_OD = 139.70
    Pipes_for_test_139_WT = 10.54
    Pipes_for_test_139_length = 12000


    def __init__(self, name, description=''):
        self.name = name
        self.description = description

    def process_time_for_step(self):
        print('The_time_for_', (self.name))
        return (
               self.The_signal_from_the_station_The_pipe_is_ready_for_relocation +\
               self.The_pipe_is_relocated_from_previous_station +\
               self.The_pipe_is_positioning_on_the_place +\
               self.The_process_time +\
               self.The_signal_of_the_end_of_operation\
                ) * \
               self.productivity_coefficient_for_use

    def pipe_pieces_per_hour(self):
        print('The_pieces_of_pipe_per_hour', (self.name))
        return self.Seconds_per_hour / \
       ((
                self.The_signal_from_the_station_The_pipe_is_ready_for_relocation + \
                self.The_pipe_is_relocated_from_previous_station + \
                self.The_pipe_is_positioning_on_the_place + \
                self.The_process_time + \
                self.The_signal_of_the_end_of_operation \
            ) * \
        self.productivity_coefficient_for_use)
# 3600 секунд в часе
# 3600 делим на время затрачиваемое на одну трубу и получаем сколько возможно пропустит труб для одной станции (Шаг 1 или...)

    def tons_per_hour(self):

        print('The_tons_per_hour_for_139', (self.name))
        return (self.Seconds_per_hour / ((self.The_signal_from_the_station_The_pipe_is_ready_for_relocation + self.The_pipe_is_relocated_from_previous_station + self.The_pipe_is_positioning_on_the_place + self.The_process_time + self.The_signal_of_the_end_of_operation) * self.productivity_coefficient_for_use)) * \
              ((self.Pipes_for_test_139_OD - self.Pipes_for_test_139_WT) * self.Pipes_for_test_139_length * self.Pi / self.Transfer_coefficient_values_of_killogram_in_tons / self.Transfer_coefficient_values_of_killogram_in_tons)

#M = (D - s) * s * 0, 02466 еще по времени!!!!!!!!!!!!!!!!!!!!!
#, где
#M — масса одного погонного метра трубы, кг;
#D — наружный диаметр рассчитываемой трубы, мм;
#s — толщина стенки трубы, мм;
#0,02466 —коэффициент при плотности стали равной 7, 850 г / см3.



class Step_1_Load_the_pipe_by_over_head_crane_to_inlet_area (General_Hydrotester_process):

    def process_time_for_step (self, *args, pipe_unpacking_process = 3, **kwargs):
        Step_1_Load_the_pipe_by_over_head_crane_to_inlet_area = super().process_time_for_step (*args, **kwargs)
        return Step_1_Load_the_pipe_by_over_head_crane_to_inlet_area + pipe_unpacking_process

    def pipe_pieces_per_hour (self, *args, pipe_unpacking_process = 1, **kwargs):
        Step_1_Load_the_pipe_by_over_head_crane_to_inlet_area = super().pipe_pieces_per_hour (*args, **kwargs)
        return Step_1_Load_the_pipe_by_over_head_crane_to_inlet_area

    def tons_per_hour (self, *args, pipe_unpacking_process = 1, **kwargs):
        Step_1_Load_the_pipe_by_over_head_crane_to_inlet_area = super().tons_per_hour(*args, **kwargs)
        return Step_1_Load_the_pipe_by_over_head_crane_to_inlet_area

process_time = Step_1_Load_the_pipe_by_over_head_crane_to_inlet_area (Step_1_Load_the_pipe_by_over_head_crane_to_inlet_area, 'Step_1_Load_the_pipe_by_over_head_crane_to_inlet_area')
pipe_pieces_per_hour = Step_1_Load_the_pipe_by_over_head_crane_to_inlet_area (Step_1_Load_the_pipe_by_over_head_crane_to_inlet_area, 'Step_1_Load_the_pipe_by_over_head_crane_to_inlet_area')
tons_per_hour = Step_1_Load_the_pipe_by_over_head_crane_to_inlet_area (Step_1_Load_the_pipe_by_over_head_crane_to_inlet_area, 'Step_1_Load_the_pipe_by_over_head_crane_to_inlet_area')
print(process_time.process_time_for_step())
print(process_time.pipe_pieces_per_hour())
print(process_time.tons_per_hour())



class Step_2_Relocation_of_pipe_to_entry_station (General_Hydrotester_process):

    def process_time_for_step (self, *args, **kwargs):
        Step_2_Relocation_of_pipe_to_entry_station = super().process_time_for_step (*args, **kwargs)
        print ('process_time_for_step')
        return Step_2_Relocation_of_pipe_to_entry_station

    def pipe_pieces_per_hour (self, *args, pipe_unpacking_process = 1, **kwargs):
        Step_2_Relocation_of_pipe_to_entry_station = super().pipe_pieces_per_hour (*args, **kwargs)
        return Step_2_Relocation_of_pipe_to_entry_station

    def tons_per_hour (self, *args, pipe_unpacking_process = 1, **kwargs):
        Step_2_Relocation_of_pipe_to_entry_station = super().tons_per_hour(*args, **kwargs)
        return Step_2_Relocation_of_pipe_to_entry_station


process_time = Step_2_Relocation_of_pipe_to_entry_station (Step_2_Relocation_of_pipe_to_entry_station, 'Step_2_Relocation_of_pipe_to_entry_station')
pipe_pieces_per_hour = Step_2_Relocation_of_pipe_to_entry_station (Step_2_Relocation_of_pipe_to_entry_station, 'Step_2_Relocation_of_pipe_to_entry_station')
tons_per_hour = Step_2_Relocation_of_pipe_to_entry_station (Step_2_Relocation_of_pipe_to_entry_station, 'Step_2_Relocation_of_pipe_to_entry_station')
print(process_time.process_time_for_step())
print(process_time.pipe_pieces_per_hour())
print(process_time.tons_per_hour())



class Step_3_Entry_station_positioning (General_Hydrotester_process):

    def process_time_for_step (self, *args, **kwargs):
        Step_3_Entry_station_positioning = super().process_time_for_step (*args, **kwargs)
        Step_3_1_Entry_station_the_pipe_eligned_accoding_to_cetre_of_filling_head = 2
        Step_3_2_Entry_station_the_pipe_length_measured = 1
        Step_3_3_Entry_station_the_pipe_connection_of_two_filling_heads = 4
        Step_3_4_Entry_station_the_pipe_flashed_by_emulsion = 10
        Step_3_5_Entry_station_the_pipe_disconnection_of_two_filling_heads = 4
        The_process_time_for_Step_3 = (
            Step_3_1_Entry_station_the_pipe_eligned_accoding_to_cetre_of_filling_head +
            Step_3_2_Entry_station_the_pipe_length_measured +
            Step_3_3_Entry_station_the_pipe_connection_of_two_filling_heads +
            Step_3_4_Entry_station_the_pipe_flashed_by_emulsion +
            Step_3_5_Entry_station_the_pipe_disconnection_of_two_filling_heads
        )
        return Step_3_Entry_station_positioning + The_process_time_for_Step_3

    def pipe_pieces_per_hour (self, *args, pipe_unpacking_process = 1, **kwargs):
        Step_3_Entry_station_positioning = super().pipe_pieces_per_hour (*args, **kwargs)
        Step_3_1_Entry_station_the_pipe_eligned_accoding_to_cetre_of_filling_head = 2
        Step_3_2_Entry_station_the_pipe_length_measured = 1
        Step_3_3_Entry_station_the_pipe_connection_of_two_filling_heads = 4
        Step_3_4_Entry_station_the_pipe_flashed_by_emulsion = 10
        Step_3_5_Entry_station_the_pipe_disconnection_of_two_filling_heads = 4
        return Step_3_Entry_station_positioning -\
            (self.Seconds_per_hour / ( \
                Step_3_1_Entry_station_the_pipe_eligned_accoding_to_cetre_of_filling_head + \
                Step_3_2_Entry_station_the_pipe_length_measured + \
                Step_3_3_Entry_station_the_pipe_connection_of_two_filling_heads + \
                Step_3_4_Entry_station_the_pipe_flashed_by_emulsion + \
                Step_3_5_Entry_station_the_pipe_disconnection_of_two_filling_heads ) * \
                self.productivity_coefficient_for_use)
        return Step_3_Entry_station_positioning

    def tons_per_hour (self, *args, pipe_unpacking_process = 1, **kwargs):
        Step_3_Entry_station_positioning = super().tons_per_hour(*args, **kwargs)
        return Step_3_Entry_station_positioning

process_time = Step_3_Entry_station_positioning (Step_3_Entry_station_positioning, 'Step_3_Entry_station_positioning')
pipe_pieces_per_hour = Step_3_Entry_station_positioning (Step_3_Entry_station_positioning, 'Step_3_Entry_station_positioning')
tons_per_hour = Step_3_Entry_station_positioning (Step_3_Entry_station_positioning, 'Step_3_Entry_station_positioning')
print(process_time.process_time_for_step())
print(process_time.pipe_pieces_per_hour())
print(process_time.tons_per_hour())



class Step_4_The_pipe_transferred (General_Hydrotester_process):

    def process_time_for_step (self, *args, **kwargs):
        Step_4_The_pipe_transferred = super().process_time_for_step (*args, **kwargs)
        Step_4_1_The_pipe_prepositioning = 2
        return Step_4_The_pipe_transferred + Step_4_1_The_pipe_prepositioning

    def pipe_pieces_per_hour (self, *args, pipe_unpacking_process = 1, **kwargs):
        Step_4_The_pipe_transferred = super().pipe_pieces_per_hour (*args, **kwargs)
        return Step_4_The_pipe_transferred

    def tons_per_hour (self, *args, pipe_unpacking_process = 1, **kwargs):
        Step_4_The_pipe_transferred = super().tons_per_hour(*args, **kwargs)
        return Step_4_The_pipe_transferred

process_time = Step_4_The_pipe_transferred (Step_4_The_pipe_transferred, 'Step_4_The_pipe_transferred')
pipe_pieces_per_hour = Step_4_The_pipe_transferred (Step_4_The_pipe_transferred, 'Step_4_The_pipe_transferred')
tons_per_hour = Step_4_The_pipe_transferred (Step_4_The_pipe_transferred, 'Step_4_The_pipe_transferred')
print(process_time.process_time_for_step())
print(process_time.pipe_pieces_per_hour())
print(process_time.tons_per_hour())



class Step_5_Test_process (General_Hydrotester_process):

        userInput = input("What_standard API5CT_API5L_or_EN10216? Print_please_API5CT_API5L_or_EN10216: ")

        if userInput == 'API5CT':
            Coefficient_for_standard_API5CT = 0.8
            Coefficient2_for_standard_API5CT = 862
            print('The_max_pressure_according_to_API5CT_normal_Atmospheres')
        if userInput != 'API5CT':
            Coefficient_for_standard_API5CT = 1
            Coefficient2_for_standard_API5CT = 1

        if userInput == 'API5L':
            Coefficient_for_standard_API5L = 0.6
            Coefficient2_for_standard_API5L = 485
            print('The_max_pressure_according_to_API5L_normal_Atmospheres')
        if userInput != 'API5L':
            Coefficient_for_standard_API5L = 1
            Coefficient2_for_standard_API5L = 1

        if userInput == 'EN10216':
            Coefficient_for_standard_EN10216 = 0.7
            Coefficient2_for_standard_EN10216 = 265
            print('The_max_pressure_according_to_EN10216_normal_Atmospheres')
        if userInput != 'EN10216':
            Coefficient_for_standard_EN10216 = 1
            Coefficient2_for_standard_EN10216 = 1

            Coefficient_for_standard = Coefficient_for_standard_API5CT * Coefficient_for_standard_API5L * Coefficient_for_standard_EN10216
            Coefficient2_for_standard = Coefficient2_for_standard_API5CT * Coefficient2_for_standard_API5L * Coefficient2_for_standard_EN10216

            The_max_pressure_for_139 = Coefficient_for_standard * 2 * Coefficient2_for_standard * float(Pipes_for_test_139['Pipe_139.70']['WT']) / float(Pipes_for_test_139['Pipe_139.70']['OD'])
            The_max_pressure_for_168 = Coefficient_for_standard * 2 * Coefficient2_for_standard * float(Pipes_for_test_168['Pipe_168.28']['WT']) / float(Pipes_for_test_168['Pipe_168.28']['OD'])
            The_max_pressure_for_177 = Coefficient_for_standard * 2 * Coefficient2_for_standard * float(Pipes_for_test_177['Pipe_177.80']['WT']) / float(Pipes_for_test_177['Pipe_177.80']['OD'])
            The_max_pressure_for_193 = Coefficient_for_standard * 2 * Coefficient2_for_standard * float(Pipes_for_test_193['Pipe_193.68']['WT']) / float(Pipes_for_test_193['Pipe_193.68']['OD'])
            The_max_pressure_for_219 = Coefficient_for_standard * 2 * Coefficient2_for_standard * float(Pipes_for_test_219['Pipe_219.08']['WT']) / float(Pipes_for_test_219['Pipe_219.08']['OD'])
            The_max_pressure_for_244 = Coefficient_for_standard * 2 * Coefficient2_for_standard * float(Pipes_for_test_244['Pipe_244.48']['WT']) / float(Pipes_for_test_244['Pipe_244.48']['OD'])
            The_max_pressure_for_273 = Coefficient_for_standard * 2 * Coefficient2_for_standard * float(Pipes_for_test_273['Pipe_273.05']['WT']) / float(Pipes_for_test_273['Pipe_273.05']['OD'])
            The_max_pressure_for_298 = Coefficient_for_standard * 2 * Coefficient2_for_standard * float(Pipes_for_test_298['Pipe_298.45']['WT']) / float(Pipes_for_test_298['Pipe_298.45']['OD'])
            The_max_pressure_for_323 = Coefficient_for_standard * 2 * Coefficient2_for_standard * float(Pipes_for_test_323['Pipe_323.90']['WT']) / float(Pipes_for_test_323['Pipe_323.90']['OD'])
            The_max_pressure_for_339 = Coefficient_for_standard * 2 * Coefficient2_for_standard * float(Pipes_for_test_339['Pipe_339.72']['WT']) / float(Pipes_for_test_339['Pipe_339.72']['OD'])
            The_max_pressure_for_365 = Coefficient_for_standard * 2 * Coefficient2_for_standard * float(Pipes_for_test_365['Pipe_365.12']['WT']) / float(Pipes_for_test_365['Pipe_365.12']['OD'])

            print('The_max_pressure_for_139_', The_max_pressure_for_139)
            print('The_max_pressure_for_168_', The_max_pressure_for_168)
            print('The_max_pressure_for_177_', The_max_pressure_for_177)
            print('The_max_pressure_for_193_', The_max_pressure_for_193)
            print('The_max_pressure_for_219_', The_max_pressure_for_219)
            print('The_max_pressure_for_244_', The_max_pressure_for_244)
            print('The_max_pressure_for_273_', The_max_pressure_for_273)
            print('The_max_pressure_for_298_', The_max_pressure_for_298)
            print('The_max_pressure_for_323_', The_max_pressure_for_323)
            print('The_max_pressure_for_339_', The_max_pressure_for_339)
            print('The_max_pressure_for_365_', The_max_pressure_for_365)



class Step_5_1_Test_process (General_Hydrotester_process):

    def process_time_for_step (self, *args, **kwargs):
        Step_5_1_Test_process = super().process_time_for_step (*args, **kwargs)
        Step_5_1_The_filling_head_is_positioned_onto_the_pipe_end = 3
        Step_5_2_The_venting_head_is_positioned_onto_testing_position = 3 #parallel_with_filling_head
        Step_5_3_The_tube_clamping_devices_are_clouse = 2
        Step_5_4_The_pipe_sealed_at_both_ends = 2
        Step_5_5_The_has_been_filled_by_water = 18
        Step_5_6_The_pipe_test_pressure_by_intensifier = 7
        Step_5_7_The_test_pressure_is_held_for_the_set_pressure_holding_time = 10
        Step_5_8_the_venting_head_is_open = 4
        Step_5_9_emptying_the_pipe = 7
        Step_5_10_The_tube_clamping_devices_are_opened = 4

        The_process_time_for_Step_5 = (
            Step_5_1_The_filling_head_is_positioned_onto_the_pipe_end +\
            Step_5_2_The_venting_head_is_positioned_onto_testing_position +\
            Step_5_3_The_tube_clamping_devices_are_clouse +\
            Step_5_4_The_pipe_sealed_at_both_ends +\
            Step_5_5_The_has_been_filled_by_water +\
            Step_5_6_The_pipe_test_pressure_by_intensifier +\
            Step_5_7_The_test_pressure_is_held_for_the_set_pressure_holding_time +\
            Step_5_8_the_venting_head_is_open +\
            Step_5_9_emptying_the_pipe +\
            Step_5_10_The_tube_clamping_devices_are_opened
        )
        return Step_5_1_Test_process + The_process_time_for_Step_5

    def pipe_pieces_per_hour (self, *args, pipe_unpacking_process = 1, **kwargs):
        Step_5_1_Test_process = super().process_time_for_step(*args, **kwargs)
        Step_5_1_The_filling_head_is_positioned_onto_the_pipe_end = 3
        Step_5_2_The_venting_head_is_positioned_onto_testing_position = 3 #parallel_with_filling_head
        Step_5_3_The_tube_clamping_devices_are_clouse = 2
        Step_5_4_The_pipe_sealed_at_both_ends = 2
        Step_5_5_The_has_been_filled_by_water = 18
        Step_5_6_The_pipe_test_pressure_by_intensifier = 7
        Step_5_7_The_test_pressure_is_held_for_the_set_pressure_holding_time = 10
        Step_5_8_the_venting_head_is_open = 4
        Step_5_9_emptying_the_pipe = 7
        Step_5_10_The_tube_clamping_devices_are_opened = 4
        return Step_5_1_Test_process + self.Seconds_per_hour / ((
            Step_5_1_The_filling_head_is_positioned_onto_the_pipe_end +\
            Step_5_2_The_venting_head_is_positioned_onto_testing_position +\
            Step_5_3_The_tube_clamping_devices_are_clouse +\
            Step_5_4_The_pipe_sealed_at_both_ends +\
            Step_5_5_The_has_been_filled_by_water +\
            Step_5_6_The_pipe_test_pressure_by_intensifier +\
            Step_5_7_The_test_pressure_is_held_for_the_set_pressure_holding_time +\
            Step_5_8_the_venting_head_is_open +\
            Step_5_9_emptying_the_pipe +\
            Step_5_10_The_tube_clamping_devices_are_opened)*\
            self.productivity_coefficient_for_use)
        return Step_5_1_Test_process

    def tons_per_hour (self, *args, pipe_unpacking_process = 1, **kwargs):
        Step_5_1_Test_process = super().tons_per_hour(*args, **kwargs)
        return Step_5_1_Test_process

process_time = Step_5_1_Test_process (Step_5_1_Test_process, 'Step_5_1_Test_process')
pipe_pieces_per_hour = Step_5_1_Test_process (Step_5_1_Test_process, 'Step_5_1_Test_process')
tons_per_hour = Step_5_1_Test_process (Step_5_1_Test_process, 'Step_5_1_Test_process')
print(process_time.process_time_for_step())
print(process_time.pipe_pieces_per_hour())
print(process_time.tons_per_hour())



class Step_6_The_pipe_water_drainage_station (General_Hydrotester_process):

    def process_time_for_step (self, *args, **kwargs):
        Step_6_The_pipe_water_drainage_station = super().process_time_for_step (*args, **kwargs)
        Step_6_2_Elevator_of_one_side_of_pipe = 4
        Step_6_3_The_drainage_of_water = 25
        return Step_6_The_pipe_water_drainage_station + Step_6_2_Elevator_of_one_side_of_pipe + Step_6_3_The_drainage_of_water

    def pipe_pieces_per_hour (self, *args, pipe_unpacking_process = 1, **kwargs):
        Step_6_The_pipe_water_drainage_station = super().pipe_pieces_per_hour (*args, **kwargs)
        return Step_6_The_pipe_water_drainage_station

    def tons_per_hour (self, *args, pipe_unpacking_process = 1, **kwargs):
        Step_6_The_pipe_water_drainage_station = super().tons_per_hour(*args, **kwargs)
        return Step_6_The_pipe_water_drainage_station

process_time = Step_6_The_pipe_water_drainage_station (Step_6_The_pipe_water_drainage_station, 'Step_6_The_pipe_water_drainage_station')
pipe_pieces_per_hour = Step_6_The_pipe_water_drainage_station (Step_6_The_pipe_water_drainage_station, 'Step_6_The_pipe_water_drainage_station')
tons_per_hour = Step_6_The_pipe_water_drainage_station (Step_6_The_pipe_water_drainage_station, 'Step_6_The_pipe_water_drainage_station')
print(process_time.process_time_for_step())
print(process_time.pipe_pieces_per_hour())
print(process_time.tons_per_hour())



class Step_7_Drifter_process (General_Hydrotester_process):

    def process_time_for_step (self, *args, **kwargs):
        Step_7_Drifter_process = super().process_time_for_step (*args, **kwargs)
        Step_7_Drifter_process_for_to_check_the_flatness_of_the_pipe = 30
        return Step_7_Drifter_process + Step_7_Drifter_process_for_to_check_the_flatness_of_the_pipe

    def pipe_pieces_per_hour (self, *args, pipe_unpacking_process = 1, **kwargs):
        Step_7_Drifter_process = super().pipe_pieces_per_hour (*args, **kwargs)
        return Step_7_Drifter_process

    def tons_per_hour (self, *args, pipe_unpacking_process = 1, **kwargs):
        Step_7_Drifter_process = super().tons_per_hour(*args, **kwargs)
        return Step_7_Drifter_process

process_time = Step_7_Drifter_process (Step_7_Drifter_process, 'Step_7_Drifter_process')
pipe_pieces_per_hour = Step_7_Drifter_process (Step_7_Drifter_process, 'Step_7_Drifter_process')
tons_per_hour = Step_7_Drifter_process (Step_7_Drifter_process, 'Step_7_Drifter_process')
print(process_time.process_time_for_step())
print(process_time.pipe_pieces_per_hour())
print(process_time.tons_per_hour())



class Step_8_Relocation_of_pipe_to_machine_outlet (General_Hydrotester_process):

    def process_time_for_step (self, *args, **kwargs):
        Step_8_Relocation_of_pipe_to_machine_outlet = super().process_time_for_step (*args, **kwargs)
        return Step_8_Relocation_of_pipe_to_machine_outlet

    def pipe_pieces_per_hour (self, *args, pipe_unpacking_process = 1, **kwargs):
        Step_8_Relocation_of_pipe_to_machine_outlet = super().pipe_pieces_per_hour (*args, **kwargs)
        return Step_8_Relocation_of_pipe_to_machine_outlet

    def tons_per_hour (self, *args, pipe_unpacking_process = 1, **kwargs):
        Step_8_Relocation_of_pipe_to_machine_outlet = super().tons_per_hour(*args, **kwargs)
        return Step_8_Relocation_of_pipe_to_machine_outlet

process_time = Step_8_Relocation_of_pipe_to_machine_outlet (Step_8_Relocation_of_pipe_to_machine_outlet, 'Step_8_Relocation_of_pipe_to_machine_outlet')
pipe_pieces_per_hour = Step_8_Relocation_of_pipe_to_machine_outlet (Step_8_Relocation_of_pipe_to_machine_outlet, 'Step_8_Relocation_of_pipe_to_machine_outlet')
tons_per_hour = Step_8_Relocation_of_pipe_to_machine_outlet (Step_8_Relocation_of_pipe_to_machine_outlet, 'Step_8_Relocation_of_pipe_to_machine_outlet')
print(process_time.process_time_for_step())
print(process_time.pipe_pieces_per_hour())
print(process_time.tons_per_hour())