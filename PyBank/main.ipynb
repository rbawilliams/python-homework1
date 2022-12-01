{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "db88e15a-d982-45bd-9472-34c5329bb543",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dependencies\n",
    "import csv\n",
    "from pathlib import Path"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "40c447df-b9a9-4a25-bfb8-4240e6d6444a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Files to load and output \n",
    "file_to_load = Path(r'C:\\Users\\romai\\OneDrive\\Documents\\Desktop\\FinTech 2022\\Starter_Code\\Instructions\\PyBank\\Resources\\budget_data.csv')\n",
    "file_to_output = Path (\"output.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f30afd6f-a614-4207-a170-77154f40facc",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Track various financial parameters\n",
    "total_months = 0\n",
    "month_of_change = []\n",
    "net_change_list = []\n",
    "greatest_increase = [\"\", 0]\n",
    "greatest_decrease = [\"\", 9999999999999999999]\n",
    "total_net = 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c86f809e-9901-4e08-a36d-14bca4ba7942",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Read the csv and convert it into a list of dictionaries\n",
    "with open(file_to_load) as financial_data:\n",
    "    reader = csv.reader(financial_data)\n",
    "\n",
    "    # Read the header row\n",
    "    header = next(reader)\n",
    "\n",
    "    # Extract first row to avoid appending to net_change_list\n",
    "    first_row = next(reader)\n",
    "    total_months = total_months + 1\n",
    "    total_net = total_net + int(first_row[1])\n",
    "    prev_net = int(first_row[1])\n",
    "\n",
    "    for row in reader:\n",
    "\n",
    "        # Track the total\n",
    "        total_months = total_months + 1\n",
    "        total_net = total_net + int(row[1])\n",
    "\n",
    "        # Track the net change\n",
    "        net_change = int(row[1]) - prev_net\n",
    "        prev_net = int(row[1])\n",
    "        net_change_list = net_change_list + [net_change]\n",
    "        month_of_change = month_of_change + [row[0]]\n",
    "\n",
    "        # Calculate the greatest increase\n",
    "        if net_change > greatest_increase[1]:\n",
    "            greatest_increase[0] = row[0]\n",
    "            greatest_increase[1] = net_change\n",
    "\n",
    "        # Calculate the greatest decrease\n",
    "        if net_change < greatest_decrease[1]:\n",
    "            greatest_decrease[0] = row[0]\n",
    "            greatest_decrease[1] = net_change\n",
    "\n",
    "# Calculate the Average Net Change\n",
    "net_monthly_avg = sum(net_change_list) / len(net_change_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ce48d724-adc4-42b1-9737-aa13f2280cdd",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Generate Output Summary\n",
    "output = (\n",
    "    f\"\\nFinancial Analysis\\n\"\n",
    "    f\"----------------------------\\n\"\n",
    "    f\"Total Months: {total_months}\\n\"\n",
    "    f\"Total: ${total_net}\\n\"\n",
    "    f\"Average  Change: ${net_monthly_avg:.2f}\\n\"\n",
    "    f\"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\\n\"\n",
    "    f\"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "db5e12db-acd5-4435-b452-f6cc660ab29b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Financial Analysis\n",
      "----------------------------\n",
      "Total Months: 86\n",
      "Total: $38382578\n",
      "Average  Change: $-2315.12\n",
      "Greatest Increase in Profits: Feb-2012 ($1926159)\n",
      "Greatest Decrease in Profits: Sep-2013 ($-2196167)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Print the output \n",
    "print(output)\n",
    "\n",
    "# Export the results to text file\n",
    "with open(file_to_output, \"w\") as txt_file:\n",
    "    txt_file.write(output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "62eea17d-a282-417a-aeb2-e7e74375f3d5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
