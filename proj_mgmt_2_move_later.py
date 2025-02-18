import pandas as pd





# Define data without special characters
data = {
    "Category": ["Final Deliverables", "Final Deliverables", "Final Deliverables", 
                 "Transition Timing", "Transition Timing", 
                 "Ongoing Costs", "Ongoing Costs", 
                 "Ownership"],
    "Details": ["Completed 3-bedroom, 2-bath home", 
                "Installed electrical, plumbing, and HVAC systems", 
                "Landscaping and final inspections completed",
                "Home handover to owners: June 2025",
                "Final city inspection & occupancy permit: May 2025",
                "Home maintenance ($5,000 annually estimated)",
                "Utilities & property taxes",
                "Transferred to homeowners upon final walkthrough & closing"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel file (ensure safe path)
file_path = r"C:\Users\blake\OneDrive\Documents\final_deliverables_cleaned.xlsx"  # Change the path as needed

df.to_excel(file_path, index=False)

print(f"Excel file saved successfully at: {file_path}")
