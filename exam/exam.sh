# 1. Write a one-line Unix command that counts the number of entries (i.e. years) in the Land_and_Ocean_summary.txt and prints it to screen.
cat ./data/Land_and_Ocean_summary.txt | grep -E "^\s{2}" | wc -l

# 2. Write a one-line Unix command that sorts the file by year (most recent first), and by CO2 value (largest first, if the year is equal) - excluding all lines that do not have a 3 character country code, selects the top 10, and saves the output to a new file called top10_CO2.csv
cat ./data/annual-co-emissions-by-region.csv | sort -r -k3 -k4 -t "," -g | grep -E ".+,[a-zA-Z]{3},.+" | head -n 10 > top10_CO2.csv
