from models.degree import Degree

class DegreeFactory:
    SYMBOLS = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
    NAMES = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 
             'Seventh', 'Eighth', 'Ninth', 'Tenth', 'Eleventh', 'Twelfth']

    @staticmethod
    def create_degree(name: str, symbol: str) -> Degree:
        """Create a single degree object"""
        return Degree(name, symbol)
    
    @staticmethod
    def create_all_degrees() -> list[Degree]:
        """Create all possible degrees"""
        return [DegreeFactory.create_degree(name, symbol) 
                for name, symbol in zip(DegreeFactory.NAMES, DegreeFactory.SYMBOLS)]