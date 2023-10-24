class Product: 
    def __init__ (name, description, date_fabrication, is_active, category: Category ):
        self.name = name
        self.description = description
        self.date_fabrication = date_fabrication
        self.is_active = is_active
        