class DataLoader:
    def __init__(self, source="default"):
        self.source = source
        self.data = None

    def load_data(self):
        # Implement logic to load data from the specified source
        pass

    def get_data(self):
        # Return the loaded data
        return self.data