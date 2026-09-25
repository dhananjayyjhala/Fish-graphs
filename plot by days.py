# Import the CSV module so the dataset can be read as rows.
import csv
# Import defaultdict so missing transect, reef, or species entries default to zero.
from collections import defaultdict
# Import Path so the CSV path is relative to this script.
from pathlib import Path

# Import pyplot so the grouped bar charts can be created.
from matplotlib import pyplot as plt


# Choose which month to plot.
month_to_plot = "January"
# Find the CSV file in the same folder as this script.
data_file = Path(__file__).with_name("ReefFish.csv")
# Store abundance totals using transect, reef, and species as nested keys.
abundance_by_transect = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
matching_rows = 0

# Open the CSV file while preserving its row structure.
with data_file.open(newline="") as csv_file:
	# Read each CSV row as a dictionary using the header names.
	for row in csv.DictReader(csv_file):
		# Keep only records from the selected month.
		if row["Month"] == month_to_plot:
			matching_rows += 1
			# Add this observation to its transect, reef, and species total.
			abundance_by_transect[row["Transect"]][row["Site"]][row["Species"]] += int(
				row["Abundance"]
			)

if matching_rows == 0:
	raise ValueError(f"No CSV rows found for month {month_to_plot!r}")

print(f"Plotting {month_to_plot}: {matching_rows} CSV rows")

# Sort the selected month's transect identifiers numerically.
transects = sorted(abundance_by_transect, key=int)
	# Collect every reef that appears in the selected month's records.
sites = sorted(
	{
		# Add the current reef name to the set.
		site
		# Visit each transect's data.
		for transect_data in abundance_by_transect.values()
		# Visit each reef recorded for that transect.
		for site in transect_data
	}
)
	# Collect every species recorded in the selected month across all reefs and days.
species = sorted(
	{
		# Add the current species name to the set.
		fish_species
		# Visit each transect's data.
		for transect_data in abundance_by_transect.values()
		# Visit each reef's species totals.
		for species_by_site in transect_data.values()
		# Visit each species recorded for that reef.
		for fish_species in species_by_site
	}
)
# Create one horizontal position for each species group.
positions = list(range(len(species)))
# Set the width shared by each reef's bar.
bar_width = 0.35

# Remove figures from earlier runs when this file is rerun in the same session.
plt.close("all")
# Create one narrow subplot for each selected-month transect.
figure, axes = plt.subplots(
	# Use one row for every recorded transect.
	len(transects),
	# Place the transect plots in one column.
	1,
	# Use a narrower figure with compact height per subplot.
	figsize=(7, 3.4 * len(transects)),
	# Keep the abundance scale consistent across all days.
	sharey=True,
	# Keep axes in a two-dimensional structure for consistent indexing.
	squeeze=False,
)
figure.canvas.manager.set_window_title(f"{month_to_plot} fish abundance")

# Draw the grouped bars for each selected-month transect.
for transect_index, transect in enumerate(transects):
	# Select the subplot belonging to this transect.
	axis = axes[transect_index][0]
	# Draw one bar series for each reef.
	for site_index, site in enumerate(sites):
		# Offset reef bars so they sit side by side within each species group.
		bar_positions = [
			# Center all reef bars around the species position.
			position + (site_index - (len(sites) - 1) / 2) * bar_width
			# Calculate an offset for every species position.
			for position in positions
		]
		# Get each species' abundance for this reef and transect.
		abundance = [
			# Use zero when a species was not recorded for this reef and transect.
			abundance_by_transect[transect][site].get(fish_species, 0)
			# Build the values in the same order as the species labels.
			for fish_species in species
		]
		# Draw the reef's bars and add it to the legend.
		axis.bar(bar_positions, abundance, width=bar_width, label=site)

	# Give this subplot a title containing the selected month and transect.
	axis.set_title(
		f"{month_to_plot} Transect {transect} fish abundance by species and reef"
	)
	# Label the shared vertical measurement.
	axis.set_ylabel("Abundance")
	# Put species names beneath their grouped bars.
	axis.set_xticks(positions, species)
	# Add light horizontal guides for easier value comparison.
	axis.grid(axis="y", alpha=0.25)
	# Identify the reef represented by each bar color.
	axis.legend(title="Reef")

# Label the horizontal axis on the final subplot.
axes[-1][0].set_xlabel("Species")
# Reduce vertical gaps and outer padding between the compact subplots.
figure.subplots_adjust(hspace=0.3, left=0.1, right=0.98, top=0.96, bottom=0.06)
# Display the completed selected-month comparison charts.
plt.show()
