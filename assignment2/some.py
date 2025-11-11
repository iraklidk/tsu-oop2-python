from abc import ABC, ABCMeta, abstractmethod

class Statistic(ABC):
    """
    Abstract class representing a generic statistic entry.
    """
    
    def __init__(self, region, parameter, powertrain, year, unit, value):
        self.region = region
        self.parameter = parameter
        self.powertrain = powertrain
        self.year = int(year)
        self.unit = unit
        self.value = float(value)

    @abstractmethod
    def display(self):
        """
        Display the statistic in a readavle format
        """
        pass
    
    @abstractmethod
    def to_dict(self):
        """
        Return the statistic as a dictionary.
        """
        pass
    
class EVStatistic(Statistic):
    """
    Concrete class for electir vehicle statistics.
    """
    
    def display(self):
        """Print the statistic in human-readable form."""
        print(f"{self.region} | {self.parameter} | {self.powertrain} | "
                f"{self.year} | {self.unit} | {self.value}")

    def to_dict(self):
        """Return the statistic as a dictionary."""
        return {
            "region": self.region,
            "parameter": self.parameter,
            "powertrain": self.powertrain,
            "year": self.year,
            "unit": self.unit,
            "value": self.value
        }
        
class StatisticCollection:
    """
    Class to hold multiple statistics and provide static analysis methods.
    """

    def __init__(self):
        self.stats = []

    @staticmethod
    def analyze(stats, **filters):
        """
        Flexible static method to filter stats by multiple fields.
        
        Example:
            analyze(collection.stats, region="Australia", unit="percent", year_start=2012, year_end=2015)
            analyze(collection.stats, parameter="EV sales", powertrain="BEV", unit="Vehicles", value_lt=1)
        """
        results = stats
        for key, val in filters.items():
            if key == "year_start":
                results = [s for s in results if s.year >= val]
            elif key == "year_end":
                results = [s for s in results if s.year <= val]
            elif key == "value_lt":
                results = [s for s in results if s.value < val]
            else:
                # Match attribute by name
                results = [s for s in results if getattr(s, key) == val]
        return results
    
# # -------------------- T E S T I N G -------------------- ##
        
# Create collection
collection = StatisticCollection()
folder_path = "cars" 

for i in range(10):  # 0 to 9
    filename = f"part_{i:02d}"  # part_00, part_01, ..., part_09
    file_path = folder_path + "/" + filename
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("#@#")
            if len(parts) == 6:
                stat = EVStatistic(*parts)
                collection.stats.append(stat)

print(f"Total records read: {len(collection.stats)}\n")

# Case 1: Australia 2012-2015, percent
result1 = StatisticCollection.analyze(
    collection.stats,
    region="Australia",
    unit="percent",
    year_start=2012,
    year_end=2015
)
print("Case 1 results:")
for r in result1:
    r.display()

# # Analysis case 2: parameter, powertrain, unit, value < 1
result2 = StatisticCollection.analyze(
    collection.stats,
    parameter="EV sales",
    powertrain="BEV",
    unit="Vehicles",
    value_lt=1
)
print("\nCase 2 results:")
for r in result2:
    r.display()
    
# # Just some test case, which takes only one parameter - region
result3 = StatisticCollection.analyze(
    collection.stats,
    region="USA",
)
print("\nCase 3 results:")
for r in result3:
    r.display()