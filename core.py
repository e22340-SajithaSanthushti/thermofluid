from pathlib import Path
import pandas as pd
from scipy.interpolate import interp1d

# Dynamically locate the data folder relative to this file's location
DATA_DIR = Path(__file__).parent / "data"

class ThermoTable:
    def __init__(self, table_name="water_sat_T.csv"):
        """Initializes the table dynamically for any fluid or gas CSV file."""
        self.csv_path = DATA_DIR / table_name
        
        if not self.csv_path.exists():
            raise FileNotFoundError(f"Thermodynamic table '{table_name}' could not be found in {DATA_DIR}")
            
        # Load data and ensure it's sorted by the independent variable (First Column)
        self.df = pd.read_csv(self.csv_path)
        self.df = self.df.sort_values(by=self.df.columns[0]).reset_index(drop=True)

    def query(self, input_value):
        """
        Universal look-up method. Queries the table using the first column 
        as the independent variable and returns all interpolated properties.
        """
        if not hasattr(self, 'df') or self.df is None:
            raise ValueError("Dataframe not initialized. Check if your data file is empty or corrupted.")

        independent_col = self.df.columns[0]
        
        # Check if the requested value is outside our table limits
        val_min = self.df[independent_col].min()
        val_max = self.df[independent_col].max()
        if input_value < val_min or input_value > val_max:
            raise ValueError(f"Input {input_value} is out of bounds ({val_min} to {val_max} for {independent_col}).")

        properties = {}
        
        # Loop through each column and perform linear interpolation
        for col in self.df.columns:
            if col == independent_col:
                properties[col] = float(input_value)
                continue
                
            interpolator = interp1d(self.df[independent_col], self.df[col], kind='linear')
            properties[col] = float(interpolator(input_value))
            
        return properties

    def get_sat_properties(self, T):
        """Backwards compatible alias specifically for water saturation temperature lookups."""
        return self.query(T)