{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "vscode": {
     "languageId": "plaintext"
    }
   },
   "outputs": [],
   "source": [
    "# Re-attempting to generate the visual representation of final deliverables\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Create figure and axis\n",
    "fig, ax = plt.subplots(figsize=(8, 6))\n",
    "ax.axis(\"off\")\n",
    "\n",
    "# Define text content in a structured way\n",
    "text_content = \"\"\"\n",
    "🏡 **Final Deliverables:**  \n",
    "✔ Completed 3-bedroom, 2-bath home  \n",
    "✔ Installed electrical, plumbing, and HVAC systems  \n",
    "✔ Landscaping and final inspections completed  \n",
    "\n",
    "📅 **Transition Timing:**  \n",
    "🗓 Home handover to owners: **June 2025**  \n",
    "🗓 Final city inspection & occupancy permit: **May 2025**  \n",
    "\n",
    "💰 **Ongoing Costs:**  \n",
    "💵 Home maintenance ($5,000 annually estimated)  \n",
    "💡 Utilities & property taxes  \n",
    "\n",
    "🔑 **Ownership:**  \n",
    "🏠 Transferred to homeowners upon final walkthrough & closing  \n",
    "\"\"\"\n",
    "\n",
    "# Add text to the figure\n",
    "ax.text(0.05, 0.5, text_content, fontsize=12, verticalalignment=\"center\", wrap=True)\n",
    "\n",
    "# Save the visual representation\n",
    "image_path = \"/mnt/data/final_deliverables_visual.png\"\n",
    "plt.savefig(image_path, bbox_inches=\"tight\", dpi=300)\n",
    "plt.show()\n",
    "\n",
    "# Provide file for download\n",
    "image_path\n"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
