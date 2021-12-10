from panels import *
from datahandler import *

if __name__ == '__main__':
    # Sheet to be processed, processing handles linking sheets together
    file = "excel_sheets/floor1.xlsx"
    panel_dict, xfmr_list = load_file(file)
    for p in panel_dict.values():
        p.print_panel()
    for xfmr in xfmr_list:
        xfmr.print_info()

    # Generate Panel Network
    panel_network = Network('power_dist')
    for p in panel_dict.keys():
        panel_network.add_node(p)
    for xfmr in xfmr_list:
        panel_network.add_node(xfmr.name)
        panel_network.connect_nodes(xfmr.input_con, xfmr.name)
        panel_network.connect_nodes(xfmr.name, xfmr.output_con)

    # Update Transformer and Feeder Schedule
    write_xfmr_sched(xfmr_list)
    write_feeder_sched(xfmr_list, panel_network, 'CU')







