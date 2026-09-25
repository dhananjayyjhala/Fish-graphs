# Import the CSV module to read data from the reef fish dataset.
import csv
# Import defaultdict so we can store counts in a nested dictionary without extra setup.
from collections import defaultdict
# Import Path so we can locate the CSV file relative to this script.
from pathlib import Path

# Import pyplot from matplotlib to create the chart.
from matplotlib import pyplot as plt

# Build the path to the ReefFish.csv file in the same folder as this script.
data_file = Path(__file__).with_name("ReefFish.csv")
# Create a nested dictionary to store abundance counts by reef and species.
abundance_by_reef = defaultdict(lambda: defaultdict(int))

# Open the CSV file and read it line by line as rows of dictionary data.
with data_file.open(newline="") as csv_file:
    # Loop through every row in the CSV file.
    for row in csv.DictReader(csv_file):
        # Only keep records from January for this chart.
        if row["Month"] == "January":
            # Add the abundance value to the count for this site and species.
            abundance_by_reef[row["Site"]][row["Species"]] += int(
                row["Abundance"]
            )

# Sort the reef names so the chart is ordered consistently.
sites = sorted(abundance_by_reef)
# Collect every species name that appears across all reefs and sort them alphabetically.
species = sorted(
    {
        # Pull each fish species from the nested abundance dictionary.
        fish_species
        for species_by_reef in abundance_by_reef.values()
        for fish_species in species_by_reef
    }
)
# Create one x-axis position for each species in the chart.
positions = list(range(len(species)))
# Set the width of each bar used in the grouped bars.
bar_width = 0.35

# Create a figure and axes for the chart with a size suited to the data.
figure, axis = plt.subplots(figsize=(10, 6))
# Loop once for each reef to draw a grouped bar for that reef.
for site_index, site in enumerate(sites):
    # Calculate the x positions for this site's bars so they sit beside each other.
    bar_positions = [
        position + (site_index - (len(sites) - 1) / 2) * bar_width
        for position in positions
    ]
    # Get the abundance value for each species at this reef, defaulting to 0 if missing.
    abundance = [
        abundance_by_reef[site].get(fish_species, 0)
        for fish_species in species
    ]
    # Draw each reef as a separate bar group with its own label.
    axis.bar(bar_positions, abundance, width=bar_width, label=site)

# Set the chart title to describe what the plot is showing.
axis.set_title("January fish abundance by species and reef")
# Label the x-axis to show the fish species categories.
axis.set_xlabel("Species")
# Label the y-axis to show how many fish were counted.
axis.set_ylabel("Abundance")
# Place species names at the tick positions on the x-axis.
axis.set_xticks(positions, species)
# Add a legend so each reef can be identified by color.
axis.legend(title="Reef")
# Add light horizontal grid lines to make the values easier to read.
axis.grid(axis="y", alpha=0.25)
# Adjust the layout so titles, labels, and legend fit neatly in the figure.
figure.tight_layout()
# Display the finished chart in a window for viewing.
plt.show()
