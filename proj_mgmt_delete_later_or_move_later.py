# Re-attempting to generate the visual representation of final deliverables

import matplotlib.pyplot as plt

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
ax.axis("off")

# Define text content in a structured way
text_content = """
🏡 **Final Deliverables:**  
✔ Completed 3-bedroom, 2-bath home  
✔ Installed electrical, plumbing, and HVAC systems  
✔ Landscaping and final inspections completed  

📅 **Transition Timing:**  
🗓 Home handover to owners: **June 2025**  
🗓 Final city inspection & occupancy permit: **May 2025**  

💰 **Ongoing Costs:**  
💵 Home maintenance ($5,000 annually estimated)  
💡 Utilities & property taxes  

🔑 **Ownership:**  
🏠 Transferred to homeowners upon final walkthrough & closing  
"""

# Add text to the figure
ax.text(0.05, 0.5, text_content, fontsize=12, verticalalignment="center", wrap=True)

# Save the visual representation
image_path = "final_deliverables_visual.png"
plt.savefig(image_path, bbox_inches="tight", dpi=300)
plt.show()

# Provide file for download
image_path

import pandas as pd
import ace_tools as tools

# Define the tabular structure without special characters to avoid font issues
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

# Display the table
tools.display_dataframe_to_user(name="Final Deliverables Table", dataframe=df)
