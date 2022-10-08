from factory.calculate_pib_per_capta_factory import CalculatePibPerCaptaFactory

def main():
    calculate = CalculatePibPerCaptaFactory.create_instance()
    
    print(calculate)
    
    calculate.load_file()
    calculate.load_uf_by_region()
    calculate.print_all_content()
    calculate.get_state_by_region('CO')
    calculate.get_region_by_state('Alagoas')
    calculate.state_for('CO')
    calculate.region_for('Amapa')
    calculate.data_frame_for_state('CO')
    calculate.data_frame_for_region('Goias')
    calculate.tot_state()
    calculate.tot_region()
    calculate.first_region()
    calculate.last_region()

main()