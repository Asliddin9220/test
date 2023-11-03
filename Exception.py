class InvalidTaxiName(Exception):
    def __init__(self, message="Taksi nomi notogri: bu identifikatorli taksi allaqachon mavjud"):
        self.message = message
        super().__init__(self.message)