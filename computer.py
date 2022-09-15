class Computer:

    """
    All information about the computer is stored here.
    """
    def __init__(self, description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int
                    ):
        self.computer = {'description': description,
        'processor_type': processor_type,
        'hard_drive_capacity': hard_drive_capacity,
        'memory': memory,
        'operating_system': operating_system,
        'year_made': year_made,
        'price': price}
    
    """
    Return attributes called when prompted
    """
    def get_attribute(self, attribute):
        if attribute == "all attributes":
            # return information of computer
            return self.computer
        else:
            # only return the specific attribute called
            return self.computer[attribute]
    """
    Update computer value if called
    """
    def update_attribute(self, attribute, updated_value):
        self.computer[attribute] = updated_value